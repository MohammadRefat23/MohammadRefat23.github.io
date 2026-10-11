from __future__ import annotations

import csv
import json
import math
import re
import time
from datetime import date
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen



ROOT = Path(__file__).resolve().parents[1]
STATS_INDEX_URL = "https://www.smogon.com/stats/"
STATS_BASE_URL = "https://www.smogon.com/stats"
OUTPUT = ROOT / "static/data/vgc-meta.json"
HISTORY_DIR = ROOT / "static/data/vgc-history"
SNAPSHOTS_DIR = HISTORY_DIR / "snapshots"
HISTORY_INDEX = HISTORY_DIR / "index.json"
COMPARISON_CSV = HISTORY_DIR / "monthly_comparison.csv"

# This project tracks the Pokémon Showdown Champions VGC best-of-three ladder.
FORMAT_PREFIX = "gen9championsvgc2026reg"
FORMAT_SUFFIX = "bo3"
REGULATIONS = ("ma", "mb", "mc")
RATING_CUTOFF = 1630
MIN_MONTH = "2026-04"
TOP_N = 15
REQUEST_TIMEOUT = 45
REQUEST_DELAY = 0.2

SOURCE = "Smogon / Pokémon Showdown"
ATTRIBUTION = "Usage statistics: Smogon / Pokémon Showdown"
HEADERS = {
    "User-Agent": "MohammadRefat23.github.io VGC usage-rank visualization",
    "Accept": "text/html,text/plain,application/json",
}

def get_text(url: str) -> str:
    request = Request(url, headers=HEADERS)
    with urlopen(request, timeout=REQUEST_TIMEOUT) as response:
        return response.read().decode("utf-8")


def get_months() -> list[str]:
    """Read Smogon's public stats directory and return available month folders."""
    page = get_text(STATS_INDEX_URL)
    months = sorted(set(re.findall(r'href="(\d{4}-\d{2})/"', page)))
    return [month for month in months if month >= MIN_MONTH]


def parse_usage_table(text: str) -> list[dict]:
    """Parse the full rank, usage, and count columns from a Smogon report."""
    pokemon = []
    seen_names = set()
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        columns = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(columns) < 7:
            continue
        try:
            rank = int(columns[0])
            usage = float(columns[2].replace("%", "").replace(",", ""))
            raw = int(columns[3].replace(",", ""))
            raw_pct = float(columns[4].replace("%", "").replace(",", ""))
            real = int(columns[5].replace(",", ""))
            real_pct = float(columns[6].replace("%", "").replace(",", ""))
        except (ValueError, TypeError):
            continue
        name = columns[1]
        if not name or name.lower() in {"pokemon", "pokémon"}:
            continue
        if name in seen_names:
            raise ValueError(f"Duplicate Pokémon row in Smogon report: {name}")
        if not all(math.isfinite(value) for value in (usage, raw_pct, real_pct)):
            raise ValueError(f"Non-finite usage value for {name}")
        if any(not 0 <= value <= 100 for value in (usage, raw_pct, real_pct)):
            raise ValueError(f"Usage percentage outside [0, 100] for {name}")
        seen_names.add(name)
        pokemon.append(
            {
                "id": re.sub(r"[^a-z0-9]", "", name.casefold()),
                "name": name,
                "rank": rank,
                "usage_pct": usage,
                "raw": raw,
                "raw_pct": raw_pct,
                "real": real,
                "real_pct": real_pct,
            }
        )

    pokemon.sort(key=lambda row: row["rank"])
    if not pokemon:
        raise ValueError("No Pokémon rows found in the Smogon stats file")
    expected_ranks = list(range(1, len(pokemon) + 1))
    observed_ranks = [row["rank"] for row in pokemon]
    if observed_ranks != expected_ranks:
        raise ValueError("Smogon source ranks are not a continuous sequence starting at 1")
    return pokemon


def parse_report(text: str) -> tuple[int, float, list[dict]]:
    """Parse report totals and species rows; reject incomplete source files."""
    battles_match = re.search(r"Total battles:\s*([\d,]+)", text)
    weight_match = re.search(r"Avg\. weight/team:\s*([\d.]+)", text)
    if not battles_match or not weight_match:
        raise ValueError("Smogon report is missing its battle or average-weight summary")
    battles = int(battles_match.group(1).replace(",", ""))
    weight = float(weight_match.group(1))
    if battles <= 0 or not math.isfinite(weight) or weight <= 0:
        raise ValueError("Smogon report has invalid battle totals or average weight")
    return battles, weight, parse_usage_table(text)


def regulation_label(code: str) -> str:
    return f"M-{code[-1].upper()}"


def snapshot_path(snapshot: dict) -> Path:
    return (
        Path("snapshots")
        / "Doubles-Bo3"
        / snapshot["regulation"]
        / f"{snapshot['month']}.json"
    )


def load_monthly_snapshots() -> list[dict]:
    snapshots = []
    months = get_months()
    if not months:
        raise RuntimeError("No Smogon monthly stats folders were found")

    for month in months:
        for regulation in REGULATIONS:
            format_id = f"{FORMAT_PREFIX}{regulation}{FORMAT_SUFFIX}"
            filename = f"{format_id}-{RATING_CUTOFF}.txt"
            url = f"{STATS_BASE_URL}/{month}/{filename}"
            try:
                body = get_text(url)
            except HTTPError as exc:
                if exc.code == 404:
                    continue
                raise
            total_battles, avg_weight, rows = parse_report(body)
            snapshots.append(
                {
                    "schema_version": 2,
                    "month": month,
                    "format": "Doubles Bo3",
                    "regulation": regulation_label(regulation),
                    "format_id": format_id,
                    "rating_cutoff": RATING_CUTOFF,
                    "total_battles": total_battles,
                    "avg_weight_per_team": avg_weight,
                    "source": SOURCE,
                    "source_url": url,
                    "attribution": ATTRIBUTION,
                    "pokemon": rows,
                }
            )
            print(
                f"Imported {month} · Regulation {regulation_label(regulation)} "
                f"({len(rows)} Pokémon; {total_battles:,} battles)"
            )
            time.sleep(REQUEST_DELAY)

    if not snapshots:
        raise RuntimeError("No Champions VGC Bo3 usage datasets were found")
    snapshots.sort(key=lambda row: (row["month"], row["regulation"]))
    return snapshots


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_saved_smogon_snapshots() -> list[dict]:
    """Keep archived Smogon snapshots even if a source month is later removed."""
    if not SNAPSHOTS_DIR.exists():
        return []
    saved = []
    for path in SNAPSHOTS_DIR.rglob("*.json"):
        try:
            snapshot = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if (
            snapshot.get("source") == SOURCE
            and snapshot.get("format") == "Doubles Bo3"
            and snapshot.get("rating_cutoff") == RATING_CUTOFF
            and snapshot.get("month")
            and snapshot.get("regulation")
            and isinstance(snapshot.get("pokemon"), list)
        ):
            saved.append(snapshot)
    return saved


def build_comparison_rows(snapshots: list[dict]) -> list[dict]:
    """Return union-roster comparisons for every adjacent pair per regulation."""
    grouped: dict[str, list[dict]] = {}
    for snapshot in snapshots:
        grouped.setdefault(snapshot["regulation"], []).append(snapshot)

    result = []
    for regulation, reports in grouped.items():
        reports.sort(key=lambda row: row["month"])
        for previous, current in zip(reports, reports[1:]):
            before = {row["name"]: row for row in previous["pokemon"]}
            after = {row["name"]: row for row in current["pokemon"]}
            for name in sorted(before.keys() | after.keys()):
                old = before.get(name)
                new = after.get(name)
                result.append(
                    {
                        "regulation": regulation,
                        "earlier_month": previous["month"],
                        "later_month": current["month"],
                        "pokemon": name,
                        "earlier_rank": old["rank"] if old else None,
                        "later_rank": new["rank"] if new else None,
                        "earlier_usage_pct": old["usage_pct"] if old else None,
                        "later_usage_pct": new["usage_pct"] if new else None,
                        "usage_change_pp": round(new["usage_pct"] - old["usage_pct"], 5)
                        if old and new
                        else None,
                        "rank_movement": old["rank"] - new["rank"] if old and new else None,
                        "coverage": "both months" if old and new else ("later only" if new else "earlier only"),
                    }
                )
    return result


def summarize_adjacent_pairs(snapshots: list[dict], top_n: int = TOP_N) -> list[dict]:
    """Calculate descriptive rank and usage summaries for each same-regulation pair."""
    grouped: dict[str, list[dict]] = {}
    for snapshot in snapshots:
        grouped.setdefault(snapshot["regulation"], []).append(snapshot)

    summaries = []
    for regulation, reports in grouped.items():
        reports.sort(key=lambda row: row["month"])
        for earlier, later in zip(reports, reports[1:]):
            old = {row["name"]: row for row in earlier["pokemon"]}
            new = {row["name"]: row for row in later["pokemon"]}
            common_names = old.keys() & new.keys()
            common = sorted(common_names)
            old_order = {name: rank for rank, name in enumerate(
                sorted(common, key=lambda name: old[name]["rank"]), start=1
            )}
            new_order = {name: rank for rank, name in enumerate(
                sorted(common, key=lambda name: new[name]["rank"]), start=1
            )}
            n_shared = len(common)
            sum_d_squared = sum((old_order[name] - new_order[name]) ** 2 for name in common)
            rho = 1 - (6 * sum_d_squared) / (n_shared * (n_shared**2 - 1)) if n_shared > 1 else None

            old_top = {row["name"] for row in earlier["pokemon"][:top_n]}
            new_top = {row["name"] for row in later["pokemon"][:top_n]}
            shared_changes = [
                {
                    "pokemon": name,
                    "usage_change_pp": round(new[name]["usage_pct"] - old[name]["usage_pct"], 5),
                    "earlier_rank": old[name]["rank"],
                    "later_rank": new[name]["rank"],
                }
                for name in common
            ]
            gains = sorted(shared_changes, key=lambda row: row["usage_change_pp"], reverse=True)[:5]
            declines = sorted(shared_changes, key=lambda row: row["usage_change_pp"])[:5]
            summaries.append(
                {
                    "regulation": regulation,
                    "earlier_month": earlier["month"],
                    "later_month": later["month"],
                    "earlier_battles": earlier.get("total_battles"),
                    "later_battles": later.get("total_battles"),
                    "shared_roster": n_shared,
                    "earlier_only": sorted(old.keys() - new.keys()),
                    "later_only": sorted(new.keys() - old.keys()),
                    "top_n": top_n,
                    "top_n_overlap": len(old_top & new_top),
                    "top_n_overlap_pct": round(100 * len(old_top & new_top) / top_n, 2),
                    "top_n_entered": sorted(new_top - old_top),
                    "top_n_exited": sorted(old_top - new_top),
                    "spearman_rho_shared": rho,
                    "sum_squared_rank_differences": sum_d_squared,
                    "largest_usage_gains": gains,
                    "largest_usage_declines": declines,
                }
            )
    return summaries


def write_comparison_csv(path: Path, snapshots: list[dict]) -> None:
    rows = build_comparison_rows(snapshots)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "regulation",
        "earlier_month",
        "later_month",
        "pokemon",
        "earlier_rank",
        "later_rank",
        "earlier_usage_pct",
        "later_usage_pct",
        "usage_change_pp",
        "rank_movement",
        "coverage",
    ]
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    fetched = load_monthly_snapshots()
    saved = load_saved_smogon_snapshots()
    by_key = {(row["regulation"], row["month"]): row for row in saved}
    by_key.update({(row["regulation"], row["month"]): row for row in fetched})
    snapshots = sorted(by_key.values(), key=lambda row: (row["month"], row["regulation"]))

    entries = []
    for snapshot in snapshots:
        relative_path = snapshot_path(snapshot)
        write_json(HISTORY_DIR / relative_path, snapshot)
        entries.append(
            {
                "month": snapshot["month"],
                "format": snapshot["format"],
                "regulation": snapshot["regulation"],
                "path": relative_path.as_posix(),
                "total_battles": snapshot["total_battles"],
            }
        )

    # Remove only snapshots from the retired Champions Battle Data source.
    for path in SNAPSHOTS_DIR.rglob("*.json") if SNAPSHOTS_DIR.exists() else []:
        try:
            source = json.loads(path.read_text(encoding="utf-8")).get("source")
        except (OSError, json.JSONDecodeError):
            source = None
        if source != SOURCE:
            path.unlink()

    current = max(fetched, key=lambda row: (row["month"], row["regulation"]))
    write_json(
        OUTPUT,
        {
            "schema_version": 2,
            "source": current["source"],
            "source_url": current["source_url"],
            "attribution": current["attribution"],
            "format": current["format"],
            "regulation": current["regulation"],
            "rating_cutoff": RATING_CUTOFF,
            "month": current["month"],
            "updated": date.today().isoformat(),
            "total_battles": current["total_battles"],
            "avg_weight_per_team": current["avg_weight_per_team"],
            "top_n": TOP_N,
            "roster_size": len(current["pokemon"]),
            "pokemon": current["pokemon"][:TOP_N],
        },
    )
    write_json(
        HISTORY_INDEX,
        {
            "schema_version": 2,
            "source": SOURCE,
            "source_url": STATS_INDEX_URL,
            "attribution": ATTRIBUTION,
            "snapshots": entries,
            "comparisons": summarize_adjacent_pairs(snapshots),
        },
    )
    write_comparison_csv(COMPARISON_CSV, snapshots)
    print(f"Current snapshot: {current['month']} · Regulation {current['regulation']}")
    print(f"Saved {len(entries)} monthly snapshot(s) and comparison CSV.")


if __name__ == "__main__":
    main()
