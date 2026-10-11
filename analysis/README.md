# Reproducing the August–September comparison

The SQLite database contains the August and September 2026 Smogon Pokémon Showdown Champions VGC M-B Bo3 usage reports at the 1630 rating cutoff. The SQL query joins the reports by Pokémon and returns usage percentage-point changes, rank movement, and roster coverage. The Python script calculates the shared-roster Spearman rank correlation and prints the largest usage shifts.

Run from this directory:

```sh
python3 analyze_months.py
```

The source reports are linked in the database metadata and summarized in `full_roster_results.md`. Usage changes are descriptive; the report totals differ substantially, so the data do not support causal or significance claims. This is Pokémon Showdown simulator data, not official in-game Pokémon Champions usage.

Attribution: Usage statistics from [Smogon](https://www.smogon.com/stats/).
