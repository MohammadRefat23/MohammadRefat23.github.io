---

title: "Starspot Inference Using Light Curve Inversion Techniques"
summary: "Testing what stellar rotation, activity, and surface structure can be recovered from photometric light-curve inversion."
date: 2023-08-01
featured: true
weight: 10
authors:
  - admin

card_label: "Inverse Problems"

tags:
  - "Inverse Problems"
  - "Light-Curve Inversion"
  - "Time-Series Analysis"
  - "Scientific Computing"
image:
  preview_only: true
---

## Overview

Most stars cannot be spatially resolved, so their surface features must be inferred indirectly from changes in brightness as the star rotates. This thesis investigated which physical properties can be recovered reliably from that one-dimensional signal.

I generated synthetic, evolving starspot light curves with **butterpy** and analyzed them using two contrasting approaches: **starry**, which represents surface brightness with spherical harmonics, and **fleck**, which models discrete circular spots.

## My Contributions

- Generated and analyzed 1,000 synthetic evolving starspot light curves using **butterpy**.
- Implemented and compared light-curve inversion workflows using **starry** and **fleck**.
- Evaluated which rotational, activity, and surface properties could be recovered reliably from photometric observations.
- Quantified relationships between stellar activity, photometric variability, and spherical-harmonic power.
- Investigated degeneracies in stellar surface reconstruction by comparing different maps that produced similar light-curve fits.

## Methods

The analysis combined forward modeling, time-series analysis, spherical-harmonic surface representations, discrete starspot models, numerical optimization, and statistical comparisons across simulated stellar populations.

## Key Results

- Both inversion methods reliably recovered stellar rotation.
- Neither method consistently reproduced changes in light-curve amplitude as starspots evolved.
- Similar light-curve fits could correspond to substantially different surface maps, demonstrating that individual spot locations, sizes, and shapes are not uniquely constrained by photometry alone.
- Greater stellar activity was associated with stronger photometric variability and increased power in higher-order spherical harmonics.
- Light-curve inversion was therefore more reliable for recovering statistical indicators of rotation and activity than for producing unique maps of individual starspots.

![Relationship between simulated stellar activity and spherical-harmonic power.](activity-harmonic-power.png)

*Higher activity levels generally require greater power in higher-order spherical harmonics, providing a statistical connection between the inversion output and stellar magnetic activity.*

## Research Outputs

{{< button text="Read Thesis" url="https://academicworks.cuny.edu/gc_etds/6480/" />}}
{{< button text="Watch Thesis Talk" url="/events/2025-06-10-talk-6/" />}}