---
title: "Accelerated calibration of semi-analytic galaxy formation models"
authors:
- admin
- Andrew Benson
date: "2026-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "The Open Journal of Astrophysics"
publication_short: "OJAp"

abstract: |
  We present an accelerated calibration framework for semi-analytic galaxy formation models, demonstrated with Galacticus. Rather than fitting directly to properties such as the low-redshift stellar mass function (SMF) - which requires evolving thousands of halos per likelihood evaluation - we construct a fast likelihood from the stellar-to-halo mass relation (SHMR; mean and scatter) evaluated at a small set of target halo masses, reducing each evaluation to simulating only tens of galaxies. We sample the posterior over Galacticus parameters with Markov Chain Monte Carlo and show that the resulting calibration reproduces the low-redshift SMF. We then extend the method to additional datasets, using a higher-redshift SHMR and the low-redshift stellar mass-size relation as examples, and assess performance for large scale structure survey-relevant properties: stellar masses, sizes, and emission-line strengths. The SMF matches data well at low redshift, but toward higher redshift the model yields too few massive galaxies and too many low-mass galaxies. Size evolution with redshift is approximately correct, but the mass-size relation is too flat, producing massive galaxies that are too small. The Hα luminosity function is well reproduced at z≈2, but by z≈0.4 the model overproduces highly star-forming, Hα-bright systems. These discrepancies suggest the model lacks sufficient flexibility (e.g. in gas cooling/recycling or feedback) to reconcile all datasets simultaneously. Our strategy complements emulator-based methods for calibrating semi-analytic models by enabling rapid, low-cost scans of model choices and parameterisations - a capability we envision leveraging to supply calibrated starting points for more detailed follow-up inference.

# Summary. An optional shortened abstract.
summary: A fast likelihood framework for calibrating semi-analytic galaxy formation models using stellar-to-halo mass relation constraints, demonstrated with Galacticus.

tags:
  - Galaxy formation
  - Galacticus

featured: true

hugoblox:
  ids:
    arxiv: 1512.04133v1

links:
- type: custom
  label: Paper
  url: https://astro.theoj.org/article/155306-accelerated-calibration-of-semi-analytic-galaxy-formation-models
- type: code
  url: https://github.com/Andrew-Robertson/CalibratingGalacticus-Paper1
- type: dataset
  url: https://zenodo.org/records/16952804
- type: video
  url: https://www.youtube.com/watch?v=a4LUxn30VSo
#- type: preprint
#  provider: arxiv
#  id: 2509.00143

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/s9CC2SKySJM)'
  #focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

Understanding how galaxies form is one of the major challenges in astrophysics. 
Researchers often use “semi-analytic models” — simplified but physically motivated simulations — to explore how processes such as gas cooling, star formation, and feedback from stars and black holes shape galaxy populations.

These models contain many uncertain parameters that must be calibrated so that the simulated galaxies resemble real ones observed in the Universe. Unfortunately, traditional calibration methods require running very large simulations, which can be computationally expensive and slow.

In this work we introduce a faster way to calibrate these models. Instead of matching the full distribution of galaxy stellar masses directly, we use the relationship between the stellar mass of a galaxy and the mass of the dark matter halo that hosts it. This allows us to evaluate each model using only a small number of simulated galaxies rather than thousands.

Using this approach with the [Galacticus](https://github.com/galacticusorg/galacticus/wiki) galaxy formation model, we show that it can reproduce key observational measurements while allowing rapid exploration of model assumptions. This makes it much easier to test different physical prescriptions and identify promising models for more detailed simulations.