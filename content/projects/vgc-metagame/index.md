---
title: "Competitive Doubles Metagame Explorer"
summary: "An interactive network explorer for Pokémon Champions Doubles metagame data."
date: 2026-10-01
tags:
  - Data analysis
  - Visualization
  - Pokémon VGC
share: false
---

I built this interactive explorer to look at relationships among Pokémon in a periodically updated snapshot of the Pokémon Champions Doubles metagame. Node size represents overall rank, and connections represent teammate affinity. Select a Pokémon to inspect its commonly used moves, items, abilities, and teammates.

{{< vgc-meta >}}

The visualization uses a saved data snapshot rather than querying the source whenever the page loads. This makes each version reproducible and lets the data be refreshed as a distinct update.

Battle data is provided by [Pokémon Champions Battle Data](https://championsbattledata.com/). This is an unofficial fan project and is not affiliated with or endorsed by Pokémon, Nintendo, Game Freak, Creatures Inc., or Pokémon Champions.
