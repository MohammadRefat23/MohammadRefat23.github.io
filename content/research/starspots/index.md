---
title: "Starspot Inference Using Light Curve Inversion Techniques"
summary: "Recovering stellar surface structure from rotational photometric variability."
date: 2023-08-01
featured: true
weight: 10
authors:
  - admin
tags:
  - "Inverse Problems"
  - "Light-Curve Inversion"
  - "Time-Series Analysis"
  - "Scientific Computing"
---

## Project Details

- **Period:** August 2023 – September 2025
- **Institution:** American Museum of Natural History and CUNY Graduate Center
- **Advisor:** Dr. Lucy Lu

### Outputs

- [View Thesis](https://academicworks.cuny.edu/gc_etds/6480/)
- [Download Thesis PDF](https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=7595&context=gc_etds)

## Overview

This project investigated how stellar surface features can be inferred from rotational brightness variations. As starspots rotate into and out of view, they produce time-dependent changes in a star’s observed brightness. Recovering the underlying surface distribution from this one-dimensional signal is a highly degenerate inverse problem.

I developed and evaluated computational workflows for generating synthetic stellar surfaces, producing rotational light curves, fitting those light curves, and comparing inferred maps against known input configurations.

## Scientific Motivation

Starspots provide information about stellar magnetic activity, rotation, and surface evolution. Because most stars cannot be spatially resolved, their surface features must be inferred indirectly from integrated photometric observations.

The central challenge is that many different surface configurations can produce similar light curves. This project therefore focused not only on reconstructing maps, but also on determining which properties of stellar activity can be constrained reliably.

## Research Questions

- Which properties of stellar surface features can be recovered from rotational light curves?
- How accurately can inversion methods reconstruct the longitudinal distribution of active regions?
- How do inclination, observational noise, cadence, and spot configuration affect the inferred maps?
- Which recovered features are robust, and which remain fundamentally degenerate?

## Methods

Synthetic stellar surface maps and light curves were generated using forward-modeling tools including `starry`, `fleck`, and `butterpy`.

The analysis workflow included:

- generating synthetic spot configurations;
- producing rotational photometric light curves;
- dividing observations into individual stellar rotations;
- fitting each rotation with surface-mapping models;
- comparing inferred maps against known synthetic inputs;
- evaluating reconstruction quality across different inclinations, noise levels, and surface configurations.

## Key Results

The analysis showed that light-curve inversion can recover broad longitudinal structure and identify the evolution of dominant active regions under favorable observing conditions.

Latitude was substantially less constrained. Different surface configurations could often reproduce nearly identical one-dimensional light curves, demonstrating that inferred maps should be interpreted as constrained representations rather than unique images of a stellar surface.

Reconstruction quality was strongly affected by stellar inclination, observational cadence, photometric noise, and the number and distribution of active regions.

## My Contributions

- Designed and implemented the computational analysis workflow.
- Developed Python pipelines for segmenting, fitting, and comparing multiple stellar rotations.
- Generated synthetic stellar surfaces and rotational light curves.
- Evaluated inferred maps against known input configurations.
- Produced the figures, analysis, interpretation, and written thesis.
- Investigated the limitations and degeneracies of light-curve inversion.

## Research Outcome

This work resulted in my 2025 M.S. thesis, *Starspot Inference Using Light Curve Inversion Techniques*, completed at the CUNY Graduate Center.
