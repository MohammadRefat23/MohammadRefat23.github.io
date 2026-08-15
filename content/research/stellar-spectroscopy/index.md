---

title: "Stellar Spectroscopy and Chemical Abundance Analysis"
summary: "Validating a high-resolution spectroscopic workflow for measuring stellar parameters and chemical abundances in red giants."
date: 2020-01-01
featured: false
weight: 40
authors:
  - admin

card_label: "Parameter Inference"

tags:
  - "Stellar Spectroscopy"
  - "Chemical Abundances"
  - "Scientific Computing"
  - "Data Analysis"
image:
  preview_only: true
---

## Overview

The chemical composition and motion of a star provide clues to where it formed within the Milky Way.

In this project, I developed and validated a high-resolution stellar-spectroscopy workflow for analyzing red giants near the interface between the Galactic disk and halo. The goal was to measure stellar atmospheric parameters and chemical abundances accurately enough to support later chemical-tagging analyses.

## My Contributions

- Developed a spectroscopic analysis workflow using **Spectroscopy Made Harder (SMHr)**.
- Normalized high-resolution echelle spectra and measured individual absorption-line strengths.
- Iteratively inferred stellar atmospheric parameters by comparing observed spectra with stellar models.
- Validated the workflow using the benchmark red giant **Arcturus**.
- Compared derived stellar parameters with published literature values to assess the accuracy of the method.

## Methods

The workflow combined high-resolution spectroscopy, continuum normalization, equivalent-width measurements, stellar-atmosphere modeling, iterative parameter estimation, and comparison against literature benchmarks.

## Key Results

- Derived an effective temperature of **4300 K** for Arcturus.
- Measured a surface gravity of **log \(g = 1.6\)**.
- Derived a metallicity of **[Fe/H] = −0.65**.
- All three values agreed with published measurements within their reported uncertainties.
- The validation established a proof of concept for applying the same workflow to a broader sample of red giants for chemical-tagging studies.

![Comparison between the stellar parameters derived for Arcturus and published literature values.](arcturus-results.png)

*The parameters derived with SMHr were consistent with previous measurements, validating the analysis procedure before applying it to additional red giants.*

## Research Outputs

{{< button text="Watch Research Talk" url="/events/2019-07-31-talk-2/" />}}