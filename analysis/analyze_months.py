#!/usr/bin/env python3
"""Summarize the paired Smogon usage reports stored in smogon_vgc_usage.sqlite."""

import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATABASE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "smogon_vgc_usage.sqlite"
QUERY = (ROOT / "compare_months.sql").read_text().strip().rstrip(";")


def rank_from_source_order(rows, column, index):
    ordered = sorted(range(len(rows)), key=lambda i: rows[i][index[column]])
    ranks = [0] * len(rows)
    for rank, row_index in enumerate(ordered, start=1):
        ranks[row_index] = rank
    return ranks


with sqlite3.connect(DATABASE) as db:
    cursor = db.execute(QUERY)
    rows = cursor.fetchall()
    columns = {column[0]: i for i, column in enumerate(cursor.description)}
    reports = db.execute(
        "SELECT month, total_battles FROM monthly_reports ORDER BY month"
    ).fetchall()

both = [row for row in rows if row[columns["coverage"]] == "both months"]
only_aug = [row[columns["pokemon"]] for row in rows if row[columns["coverage"]] == "August only"]
only_sep = [row[columns["pokemon"]] for row in rows if row[columns["coverage"]] == "September only"]
aug_ranks = rank_from_source_order(both, "aug_rank", columns)
sep_ranks = rank_from_source_order(both, "sep_rank", columns)
n = len(both)
sum_d_squared = sum((a - s) ** 2 for a, s in zip(aug_ranks, sep_ranks))
rho = 1 - 6 * sum_d_squared / (n * (n**2 - 1))

print(f"Reports: {reports}")
print(f"Roster rows: {len(rows)}; shared: {n}; August only: {only_aug}; September only: {only_sep}")
print(f"Spearman rho on shared roster: {rho:.6f} (n={n}, sum d^2={sum_d_squared})")
for title, reverse in (("Largest usage gains", True), ("Largest usage declines", False)):
    ordered = sorted(both, key=lambda row: row[columns["usage_change_pp"]], reverse=reverse)
    print(title + ":")
    for row in ordered[:5]:
        print(
            f"  {row[columns['pokemon']]}: {row[columns['usage_change_pp']]:+.5f} pp "
            f"({row[columns['aug_rank']]} -> {row[columns['sep_rank']]})"
        )
