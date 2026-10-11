---
title: VGC Metagame Explorer
summary: Comparing Pokémon Showdown Champions VGC usage ranks across monthly reports.
date: 2026-10-11
hide_date: true
project: true
project_url: /projects/vgc-metagame/
tags:
  - Pokémon VGC
  - Data Visualization
  - Interactive Tools
---

This project asks how stable Pokémon usage rankings are from one month to the next in Smogon's Champions VGC best-of-three ladder. I built a reproducible import and comparison workflow around Smogon's published monthly reports, then use the archived snapshots to inspect usage changes over time.

The first comparison uses Regulation M-B reports from August and September 2026 at the same 1630 rating cutoff. It compares weighted usage percentages, source ranks, top-15 overlap, and Spearman rank correlation across Pokémon present in both reports. The page also animates the monthly top 15 within a selected regulation and provides the full adjacent-month comparison table as a CSV download.

### August to September 2026

The two reports contain 307 Pokémon in common. Fourteen of the August top 15 remain in September's top 15 (93.3% overlap). Across the shared roster, the Spearman rank correlation is 0.9253, indicating that the overall rank ordering was similar between reports. Froslass-Mega moved from rank 21 to rank 14, entering the top 15 while already present in the earlier report.

The largest weighted-usage increases were Sneasler (+7.69 percentage points), Dragonite-Mega (+6.89), and Kingambit (+6.85). The largest decreases were Charizard-Mega-Y (−9.51) and Incineroar (−9.37). These are percentage-point changes in the report's weighted usage estimate, not changes in win rate.

### Method and limits

For each Pokémon in both reports, usage change is September usage minus August usage. Rank movement is August rank minus September rank, so a positive value means the Pokémon climbed. Spearman correlation is calculated after re-indexing the two source rank lists over the 307 shared Pokémon. The three August-only Pokémon are excluded from that correlation.

The September report contains 38,449 battles compared with 179,434 in August. This is a descriptive comparison: the different report sizes and aggregate format do not support a claim that small shifts are statistically reliable or causal. The data are from Pokémon Showdown's simulator ladder, not official in-game Pokémon Champions rankings.

The [SQL query, source database, and reproducibility script are available in the project repository](https://github.com/MohammadRefat23/MohammadRefat23.github.io/tree/main/analysis).

{{< vgc-meta >}}
