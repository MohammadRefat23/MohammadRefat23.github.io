# Champions VGC monthly usage comparison

## Scope

This comparison uses Smogon's M-B, Bo3 usage reports at the 1630 rating cutoff for August and September 2026. The report's weighted usage percentage and published rank are compared. Usage changes are percentage-point differences (September minus August); rank movement is August rank minus September rank, so positive means a climb.

## Results

- August report: 310 Pokémon, 179,434 battles.
- September report: 307 Pokémon, 38,449 battles.
- 307 Pokémon appear in both reports; three appear only in August (Banette, Meganium, and Victreebel); none appear only in September.
- Spearman rank correlation among the 307 shared Pokémon is **0.9253**. Ranks were re-indexed within the shared set using Smogon's published rank order before computing the correlation. This describes high overall rank-order consistency; it is not a significance test.
- The largest usage gains among shared Pokémon were Sneasler (+7.68653 pp), Dragonite-Mega (+6.88757), Kingambit (+6.84956), Froslass-Mega (+5.38457), and Basculegion (+5.35928).
- The largest usage declines were Charizard-Mega-Y (-9.51229 pp), Incineroar (-9.37084), Garchomp (-3.59289), Sinistcha (-3.03191), and Gengar-Mega (-2.66572).
- Froslass-Mega rose from rank 21 to rank 14, entering the top 15. It was already present in August, so this is a top-15 entry rather than a new roster appearance.

## Interpretation limits

This is a descriptive comparison of weighted Pokémon Showdown usage reports, not official Pokémon Champions in-game rankings. September's report contains substantially fewer battles than August's, so small month-to-month changes should not be treated as statistically reliable or causal. Rank shifts among low-usage Pokémon can also look large while reflecting small usage differences. Usage is not win rate or evidence that a Pokémon caused a team's result.

## Reproduction

Run `python3 analyze_months.py` to reproduce the roster summary, Spearman correlation, and largest usage changes. Run `compare_months.sql` against `smogon_vgc_usage.sqlite` to return one row for every Pokémon in either report, including source ranks, weighted usage percentages, percentage-point change, rank movement, and month coverage. `monthly_comparison.csv` is the exported result.
