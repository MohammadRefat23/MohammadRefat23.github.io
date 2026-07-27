---
layout: project
title: "Mapping Brown Dwarf and Giant Exoplanet Atmospheres"
subtitle: "Using rotational photometric variability to probe evolving cloud structures in substellar atmospheres"
permalink: /research/brown-dwarf-atmospheres/

image: images/research/browndwarfs/2mass.png
image_alt: "Illustration of a rotating brown dwarf with heterogeneous atmospheric cloud structures"
image_caption: "Photometric variability produced by evolving cloud structures rotating across the visible hemisphere."

dates: "May 2021 -- August 2023"
institution: "American Museum of Natural History"
advisor: "Dr. Johanna Vos"
role: "Undergraduate Researcher"

outputs:
  - "AAS 240 presentation"
  - "CCA/CUNY/AMNH Symposium presentation"
  - "Computational time-series analysis workflows"

methods:
  - "Time-series analysis"
  - "Photometric variability modeling"
  - "Light-curve analysis"
  - "Period estimation"
  - "Atmospheric variability interpretation"
  - "Scientific visualization"
  - "Python"
---

## Overview

Brown dwarfs and directly imaged giant exoplanets occupy the physical regime between stars and planets. Their atmospheres contain condensate clouds, molecular absorption features, and evolving weather patterns that can produce measurable changes in brightness as the object rotates.

This project investigated how rotational photometric variability can be used to infer the presence and evolution of heterogeneous cloud structures in substellar atmospheres. I analyzed time-series observations of brown dwarfs and giant exoplanet analogs, with the goal of connecting observed light-curve morphology to atmospheric dynamics and spatially varying cloud coverage.

The work introduced me to computational inference from incomplete observational data and motivated my later research on stellar surface mapping. In both cases, a one-dimensional brightness time series is used to constrain spatial structure on a rotating object.

## Scientific Motivation

Brown dwarfs are valuable laboratories for studying atmospheric physics under conditions that are difficult to reproduce on Earth. Their atmospheres span a wide range of temperatures, gravities, cloud properties, and chemical compositions, while their rapid rotation makes it possible to observe atmospheric evolution over relatively short timescales.

Brightness variations can arise when regions with different temperatures or cloud thicknesses rotate into and out of view. By measuring these variations, researchers can investigate:

- the presence of heterogeneous cloud structures,
- characteristic rotational periods,
- changes in atmospheric features over time,
- the stability and evolution of large-scale weather patterns,
- and connections between brown dwarf atmospheres and directly imaged exoplanets.

Because these objects are unresolved point sources, their atmospheric structures cannot usually be imaged directly. Their light curves therefore provide an indirect probe of spatial and temporal atmospheric behavior.

## Research Questions

This project focused on several related questions:

- How can periodic and quasi-periodic variability be identified in brown dwarf light curves?
- What does the shape and amplitude of a light curve reveal about heterogeneous atmospheric structures?
- How stable are inferred rotational signals across multiple observing intervals?
- How do evolving cloud patterns affect the interpretation of measured periods and amplitudes?
- Which computational tools are most effective for extracting atmospheric information from noisy, irregular time-series data?

## Methods

The analysis centered on processing and interpreting photometric time-series observations.

### Data Preparation

I worked with observational light curves containing brightness measurements collected over time. The preprocessing workflow included:

- inspecting data quality,
- removing invalid or contaminated measurements,
- normalizing flux values,
- identifying outliers,
- organizing observations by target and observing interval,
- and preparing the data for period and variability analysis.

### Time-Series Analysis

I used computational methods to characterize both periodic and evolving signals in the observations. The analysis included:

- visual inspection of light-curve morphology,
- estimation of variability amplitudes,
- identification of candidate rotational periods,
- comparison of repeated observing segments,
- analysis of phase-folded light curves,
- and evaluation of changes in brightness patterns across time.

### Rotational Modulation

The primary physical interpretation was that nonuniform atmospheric structures rotate across the visible hemisphere, producing brightness variations. Conceptually, the workflow followed:

```text
Photometric observations
        ↓
Data cleaning and normalization
        ↓
Variability and period analysis
        ↓
Phase-folded light curves
        ↓
Interpretation of atmospheric structure
```

### Visualization

I produced figures to compare:

- raw and processed photometric observations,
- light curves from different observing intervals,
- phase-folded rotational signals,
- changes in variability amplitude,
- and possible atmospheric interpretations.

These visualizations were used to communicate both the observational results and the limitations of inferring spatial structure from unresolved measurements.

## Key Results

The project demonstrated how rotational brightness variations can be used to identify evidence of heterogeneous and evolving atmospheric structures in brown dwarfs and giant exoplanet analogs.

The main conclusions were:

- Rotational modulation can produce measurable periodic or quasi-periodic brightness variations.
- Light-curve morphology may evolve between observations, indicating changing atmospheric structures.
- A single rotational period does not always capture the full complexity of an evolving atmosphere.
- Variability amplitude and phase behavior provide complementary information about atmospheric evolution.
- Time-series observations offer a practical way to probe unresolved substellar weather patterns.

The work also highlighted an important inverse-problem limitation: multiple atmospheric configurations can produce similar integrated light curves. Robust interpretation therefore requires careful treatment of uncertainty and model degeneracy.

## My Contributions

My contributions to the project included:

- processing and organizing photometric time-series observations,
- developing Python-based workflows for light-curve analysis,
- investigating candidate rotational signals,
- comparing variability across observing intervals,
- producing publication- and presentation-quality visualizations,
- interpreting changes in light-curve morphology in the context of atmospheric evolution,
- and presenting the research at scientific meetings.

This project strengthened my ability to move between raw observational data, computational analysis, physical interpretation, and scientific communication.

## Presentations

### Towards Mapping Brown Dwarf and Giant Exoplanet Atmospheres

**American Astronomical Society Meeting 240**  
Pasadena, California, 2022

This presentation discussed the use of rotational photometric variability to investigate heterogeneous atmospheric structures in brown dwarfs and giant exoplanet analogs.

### CCA/CUNY/AMNH Symposium

**Center for Computational Astrophysics**  
New York, 2021

This presentation summarized the project's early analysis and the connection between observed brightness variations and evolving substellar atmospheres.

## Software and Tools

The project used computational tools for data processing, time-series analysis, and visualization, including:

- Python
- NumPy
- SciPy
- Matplotlib
- Astropy
- Jupyter Notebook
- Git

## Skills and Techniques

<div class="project-tags">
  <span class="archive__item-tag">Time-Series Analysis</span>
  <span class="archive__item-tag">Signal Processing</span>
  <span class="archive__item-tag">Photometric Variability</span>
  <span class="archive__item-tag">Period Estimation</span>
  <span class="archive__item-tag">Scientific Computing</span>
  <span class="archive__item-tag">Data Visualization</span>
  <span class="archive__item-tag">Python</span>
  <span class="archive__item-tag">Atmospheric Physics</span>
</div>

## Broader Relevance

Although this work focused on brown dwarf and giant exoplanet atmospheres, the underlying computational problem is broadly applicable: spatially and temporally evolving systems must be inferred from incomplete, indirect, and noisy measurements.

The methods used in this project—time-series analysis, signal extraction, model comparison, and interpretation of rotational variability—connect naturally to research in computational physics, soft condensed matter, biological dynamics, and other fields involving complex systems observed through limited data.
