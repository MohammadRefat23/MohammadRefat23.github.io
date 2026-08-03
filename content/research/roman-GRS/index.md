---
title: Roman Galaxy Redshift Survey
date: 2025-11-26
links:
  - type: site
    url: https://roman-grs-pit.caltech.edu
tags:
  - Galaxy clustering
  - Roman Space Telescope
featured: true
weight: 10
---

I am a member of the [Roman Space Telescope](https://roman.gsfc.nasa.gov)'s [Galaxy Redshift Survey (GRS) Project Infrastructure Team (PIT)](https://roman-grs-pit.caltech.edu), where I lead the development of mock galaxy catalogues used as input for simulating grism observations. These catalogues are generated using the [Galacticus](https://github.com/galacticusorg/galacticus/wiki) semi-analytic model, run on the [UNIT](http://www.unitsims.org) simulations, and incorporate a new calibration described [here](/publications/calibratingGalacticusPaper1). You can hear me talk about this work [here](/events/mocknyc-2026).

---

## Overview

The Roman Galaxy Redshift Survey (GRS) will measure precise redshifts for millions of galaxies over a large fraction of the sky. These measurements will enable detailed studies of large-scale structure, including [baryon acoustic oscillations](https://en.wikipedia.org/wiki/Baryon_acoustic_oscillations) (BAO) and [redshift-space distortions](https://en.wikipedia.org/wiki/Redshift-space_distortions) (RSD), providing powerful constraints on the expansion history of the Universe and the growth of cosmic structure.

Roman achieves this using **slitless spectroscopy** with a [grism](https://en.wikipedia.org/wiki/Grism): instead of targeting individual galaxies, every object in the field is dispersed into a spectrum. This makes the survey extremely efficient, but also introduces significant challenges for data analysis.

---

## Why grism spectroscopy is powerful—and difficult

<figure class="wrapped-figure wrapped-figure-right">
  <img src="/images/RomanGrism.png" alt="Roman GRS data">
  <figcaption>
    Simulated Roman data, with a <em>direct image</em> (top) and <em>grism image</em> (bottom). Image credit: IPAC/STScI/Goddard
  </figcaption>
</figure>

Grism observations provide a unique combination of depth, area, and spectral information:

- They obtain **spectra for all objects simultaneously**, avoiding target selection biases  
- They enable **precise redshift measurements** over large cosmological volumes  
- They combine deep imaging and spectroscopy of the same galaxies, enabling consistent measurements of both their shapes and their spectra  

However, these advantages come with complications:

- Spectra from nearby objects can **overlap and contaminate** one another  
- Light from each galaxy is **spread out across the detector**, so its position, shape, and orientation all affect how its spectrum appears  
- The ability to measure a redshift depends on factors such as galaxy size, orientation, emission-line strength, and proximity to other objects  

As a result, interpreting grism data is not straightforward. To be confident in our conclusions, we test analysis pipelines on simulated datasets where the true answer is known. These simulations also allow us to explore how different survey strategies affect the quality of the final measurements.

---

## Approach: realistic mock universes

My work focuses on building realistic mock datasets that connect theoretical models of galaxy formation to the data products that Roman will observe.

**Galaxy catalogues**  
I generate large mock catalogues using Galacticus, calibrated to reproduce key observables such as the stellar-to-halo mass relation and emission-line luminosity functions.

**Spectral modelling**  
These catalogues include emission-line predictions (e.g. Hα, [OIII]) and continuum spectra, enabling realistic modelling of the signals detected by the grism.

**Mock observations**  
The catalogues are passed through grism simulation pipelines to produce synthetic images that include instrumental effects, noise, and spectral overlap.

**Survey design and validation**  
These mocks are used to test survey strategies, optimise observing configurations, and validate analysis pipelines. They provide a controlled way to assess how well we can recover cosmological information from the data.

---

## Why this matters

The statistical power of Roman will be unprecedented, but so is the complexity of the data. Extracting robust cosmological constraints requires understanding the full chain from galaxy formation to observed spectra.

Mock datasets play a central role in this process. They allow us to:

- Quantify selection effects and biases  
- Test redshift recovery and catalogue construction  
- Validate clustering measurements and cosmological inference  

A major focus of my work is ensuring that these tests are realistic enough that any conclusions drawn from Roman data are reliable.

---

## Looking ahead

Roman will transform our ability to map the large-scale structure of the Universe.

By combining wide-area spectroscopy with high-resolution imaging, it will enable joint analyses of galaxy clustering, weak lensing, and other probes. The challenge will be to ensure that our modelling and analysis methods keep pace with the quality of the data.
