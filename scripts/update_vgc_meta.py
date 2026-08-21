from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests


# ============================================================
# Configuration
# ============================================================

BASE_URL = "https://championsbattledata.com"
INDEX_URL = f"{BASE_URL}/api"

FORMAT = "Doubles"
TOP_N = 15

OUTPUT = Path("static/data/vgc-meta.json")

REQUEST_TIMEOUT = 30
REQUEST_DELAY = 0.15

HEADERS = {
    "User-Agent": (
        "MohammadRefat23.github.io "
        "monthly competitive-data visualization"
    ),
    "Accept": "application/json",
}


# ============================================================
# HTTP
# ============================================================

session = requests.Session()
session.headers.update(HEADERS)




def get_json(url: str) -> dict:
    print(f"GET {url}")

    response = session.get(
        url,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    try:
        return response.json()

    except ValueError as exc:
        raise RuntimeError(
            f"Expected JSON from {url}."
        ) from exc


ITEM_NAME_FIXES = {
    "Tyra nitarite": "Tyranitarite",
}


def clean_item_name(name):
    name = " ".join(str(name).split())
    return ITEM_NAME_FIXES.get(name, name)

# ============================================================
# Helpers
# ============================================================

def normalize_name(value: str) -> str:
    return re.sub(
        r"[^a-z0-9]",
        "",
        str(value).lower(),
    )


def numeric(value):
    if value is None:
        return None

    if isinstance(value, (int, float)):
        return value

    text = (
        str(value)
        .strip()
        .replace("%", "")
        .replace(",", "")
    )

    if not text:
        return None

    try:
        number = float(text)

        if number.is_integer():
            return int(number)

        return number

    except ValueError:
        return None


def get_current_doubles_summary(
    entry: dict,
) -> dict:

    return (
        entry
        .get("summary", {})
        .get("battleSummary", {})
        .get("Current", {})
        .get(FORMAT, {})
    )


def get_doubles_rank(
    entry: dict,
) -> int | None:
    """
    Get the overall current Doubles position.

    The API stores this directly at:

    summary
      -> battleSummary
      -> Current
      -> Doubles
      -> position
    """

    summary = get_current_doubles_summary(
        entry
    )

    rank = numeric(
        summary.get("position")
    )

    if rank is not None:
        return int(rank)

    # Fallback: each top row also carries the
    # overall Pokémon position.
    top = summary.get(
        "top",
        {},
    )

    if isinstance(top, dict):

        for category in (
            "move",
            "held_item",
            "ability",
            "teammate",
        ):

            row = top.get(
                category
            )

            if not isinstance(row, dict):
                continue

            rank = numeric(
                row.get("position")
            )

            if rank is not None:
                return int(rank)

    return None


def has_current_doubles_data(
    entry: dict,
) -> bool:

    for record in entry.get(
        "battleDataCsvs",
        [],
    ):

        if (
            record.get("season") == "Current"
            and
            record.get("format") == FORMAT
        ):
            return True

    return False


def get_display_name(
    entry: dict,
) -> str:

    return str(
        entry.get("name")
        or entry.get("showdownName")
        or entry.get("showdownId")
        or "Unknown"
    )


def get_showdown_id(
    entry: dict,
) -> str:

    showdown_id = entry.get(
        "showdownId"
    )

    if not showdown_id:
        raise RuntimeError(
            f"No Showdown ID for "
            f"{get_display_name(entry)}."
        )

    return str(showdown_id)


def get_saved_name(
    entry: dict,
) -> str:

    primary = (
        entry
        .get("summary", {})
        .get("primary", {})
    )

    return str(
        primary.get("saved_name")
        or get_display_name(entry)
    )


def get_types(
    entry: dict,
) -> list[str]:

    types = (
        entry
        .get("summary", {})
        .get("types", [])
    )

    if not isinstance(types, list):
        return []

    return [
        str(value)
        for value in types
    ]


def get_base_stats(
    entry: dict,
) -> dict:

    stats = (
        entry
        .get("summary", {})
        .get("baseStats", {})
    )

    if not isinstance(stats, dict):
        return {}

    return stats


# ============================================================
# Find top Doubles Pokémon
# ============================================================

def get_top_doubles(
    index_data: dict,
) -> list[dict]:

    entries = index_data.get(
        "pokemon",
        []
    )

    if not isinstance(entries, list):
        raise RuntimeError(
            "API index does not contain pokemon[]."
        )

    ranked = {}

    for entry in entries:

        if not isinstance(entry, dict):
            continue

        if not has_current_doubles_data(
            entry
        ):
            continue

        rank = get_doubles_rank(
            entry
        )

        if rank is None:
            continue

        showdown_id = get_showdown_id(
            entry
        )

        # Dedupe by Showdown ID.
        existing = ranked.get(
            showdown_id
        )

        if (
            existing is None
            or rank < existing["rank"]
        ):

            ranked[showdown_id] = {
                "rank": rank,
                "entry": entry,
            }

    result = list(
        ranked.values()
    )

    result.sort(
        key=lambda x: x["rank"]
    )

    if len(result) < TOP_N:

        raise RuntimeError(
            f"Only found {len(result)} "
            f"current Doubles Pokémon."
        )

    return result[:TOP_N]


# ============================================================
# Battle data
# ============================================================

def rows_for_category(
    rows: list[dict],
    category: str,
    limit: int,
) -> list[dict]:

    selected = []

    for row in rows:

        if (
            str(
                row.get(
                    "category",
                    ""
                )
            ).lower()
            != category.lower()
        ):
            continue

        name = row.get(
            "name"
        )

        if not name:
            continue

        selected.append(
            {
                "rank": numeric(
                    row.get("rank")
                ),
                "name": str(name),
                "percentage": numeric(
                    row.get(
                        "percentage_value"
                    )
                ),
            }
        )

    selected.sort(
        key=lambda row:
            row["rank"]
            if row["rank"] is not None
            else 9999
    )

    return selected[:limit]


def fetch_battle_data(
    showdown_id: str,
) -> dict:

    url = (
        f"{BASE_URL}/api/battle/"
        f"{FORMAT}/{showdown_id}"
    )

    data = get_json(
        url
    )

    if not isinstance(data, dict):
        raise RuntimeError(
            f"Invalid battle response "
            f"for {showdown_id}."
        )

    rows = data.get(
        "rows",
        []
    )

    if not isinstance(rows, list):
        raise RuntimeError(
            f"Battle response for "
            f"{showdown_id} "
            "does not contain rows[]."
        )

    # IMPORTANT:
    # this return must remain inside this function.
    return {
        "season": data.get(
            "season",
            "Current"
        ),
        "source": data.get(
            "source"
        ),

        "moves": rows_for_category(
            rows,
            "move",
            5
        ),

"items": [
    {
        **item,
        "name": clean_item_name(
            item.get("name", "")
        ),
    }
    for item in rows_for_category(
        rows,
        "held_item",
        3
    )
],

        "abilities": rows_for_category(
            rows,
            "ability",
            2
        ),

        "teammates": rows_for_category(
            rows,
            "teammate",
            8
        ),
    }


# ============================================================
# Network
# ============================================================

def build_links(
    pokemon: list[dict],
) -> list[dict]:
    """
    Build edges between top-N Pokémon.

    The API currently ranks teammates but does not provide
    a numeric teammate percentage, so network strength is
    based on reciprocal teammate rank:

        rank 1 -> 1.0
        rank 2 -> 0.5
        rank 3 -> 0.333...
    """

    lookup = {}

    for mon in pokemon:

        aliases = {
            normalize_name(
                mon["name"]
            ),
            normalize_name(
                mon["showdown_id"]
            ),
            normalize_name(
                mon["saved_name"]
            ),
        }

        for alias in aliases:

            if alias:
                lookup[alias] = mon["id"]

    pairs = {}

    for mon in pokemon:

        source = mon["id"]

        for teammate in mon[
            "teammates"
        ]:

            target = lookup.get(
                normalize_name(
                    teammate["name"]
                )
            )

            if (
                target is None
                or target == source
            ):
                continue

            rank = teammate.get(
                "rank"
            )

            if rank is None:
                continue

            rank = int(rank)

            key = tuple(
                sorted(
                    (source, target)
                )
            )

            record = pairs.setdefault(
                key,
                {
                    "source": key[0],
                    "target": key[1],
                    "scores": [],
                    "directions": [],
                }
            )

            record[
                "scores"
            ].append(
                1.0 / rank
            )

            record[
                "directions"
            ].append(
                {
                    "from": source,
                    "teammate_rank": rank,
                }
            )

    links = []

    for pair in pairs.values():

        scores = pair[
            "scores"
        ]

        strength = (
            sum(scores)
            /
            len(scores)
        )

        links.append(
            {
                "source": pair[
                    "source"
                ],
                "target": pair[
                    "target"
                ],
                "strength": round(
                    strength,
                    4
                ),
                "mutual": (
                    len(scores) > 1
                ),
                "directions": pair[
                    "directions"
                ],
            }
        )

    links.sort(
        key=lambda x: x[
            "strength"
        ],
        reverse=True
    )

    return links


# ============================================================
# Main
# ============================================================

def main():

    print(
        "Fetching Pokémon Champions "
        "Battle Data index..."
    )

    index = get_json(
        INDEX_URL
    )

    ranked = get_top_doubles(
        index
    )

    print()
    print(
        f"Found top {len(ranked)} "
        f"{FORMAT} Pokémon."
    )
    print()

    pokemon = []

    season = "Current"

    for item in ranked:

        rank = item[
            "rank"
        ]

        entry = item[
            "entry"
        ]

        name = get_display_name(
            entry
        )

        showdown_id = get_showdown_id(
            entry
        )

        print(
            f"#{rank:>2} "
            f"{name} "
            f"({showdown_id})"
        )

        battle = fetch_battle_data(
            showdown_id
        )

        season = battle.get(
            "season",
            season
        )

        pokemon.append(
            {
                "id": showdown_id,

                "name": name,

                "showdown_id":
                    showdown_id,

                "saved_name":
                    get_saved_name(
                        entry
                    ),

                "rank": rank,

                "types":
                    get_types(
                        entry
                    ),

                "base_stats":
                    get_base_stats(
                        entry
                    ),

                "moves":
                    battle[
                        "moves"
                    ],

                "items":
                    battle[
                        "items"
                    ],

                "abilities":
                    battle[
                        "abilities"
                    ],

                "teammates":
                    battle[
                        "teammates"
                    ],
            }
        )

        time.sleep(
            REQUEST_DELAY
        )

    links = build_links(
        pokemon
    )

    output = {
        "source":
            "Pokémon Champions Battle Data",

        "source_url":
            "https://championsbattledata.com/",

        "api_guide":
            "https://championsbattledata.com/api_guide",

        "attribution":
            (
                "Battle data provided by "
                "Pokémon Champions Battle Data."
            ),

        "format":
            FORMAT,

        "season":
            season,

        "updated":
            datetime.now(
                timezone.utc
            ).strftime(
                "%Y-%m-%d"
            ),

        "top_n":
            TOP_N,

        "pokemon":
            pokemon,

        "links":
            links,
    }

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    temporary = OUTPUT.with_suffix(
        ".json.tmp"
    )

    temporary.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False
        )
        + "\n",
        encoding="utf-8"
    )

    temporary.replace(
        OUTPUT
    )

    print()
    print(
        f"Wrote {OUTPUT}"
    )

    print(
        f"Pokémon nodes: "
        f"{len(pokemon)}"
    )

    print(
        f"Network links: "
        f"{len(links)}"
    )

    print()
    print(
        "Top Doubles Pokémon:"
    )

    for mon in pokemon:

        top_move = (
            mon["moves"][0]["name"]
            if mon["moves"]
            else "—"
        )

        top_item = (
            mon["items"][0]["name"]
            if mon["items"]
            else "—"
        )

        print(
            f"  #{mon['rank']:>2} "
            f"{mon['name']:<25} "
            f"{top_move:<20} "
            f"{top_item}"
        )

    if links:

        names = {
            mon["id"]: mon["name"]
            for mon in pokemon
        }

        print()
        print(
            "Strongest teammate links:"
        )

        for link in links[:10]:

            print(
                f"  "
                f"{names[link['source']]} "
                f"↔ "
                f"{names[link['target']]} "
                f"({link['strength']:.3f})"
            )


if __name__ == "__main__":
    main()
