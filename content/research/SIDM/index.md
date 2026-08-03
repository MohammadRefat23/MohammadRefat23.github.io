---
title: "Self-Interacting Dark Matter (SIDM)"

summary: Using gravitational lensing and simulations to explore the small-scale behaviour of dark matter.

date: 2026-03-18
featured: true

tags:
  - Dark matter
  - Simulations
weight: 30
---

## Overview

Dark matter makes up most of the matter in the Universe, but its fundamental nature remains unknown. The standard model—cold dark matter (CDM)—successfully explains structure on large scales. In simulations that include only dark matter, it predicts that haloes develop steep, centrally concentrated *cusps*.

Early observations of dwarf and low-surface-brightness galaxies instead appeared to favour constant-density *cores*, in tension with these predictions. This “[core–cusp problem](https://en.wikipedia.org/wiki/Cuspy_halo_problem)” was one of the original motivations for considering alternatives such as self-interacting dark matter (SIDM), in which dark matter particles scatter off one another and naturally redistribute energy to produce lower-density centres.

Subsequent work complicated this picture. On the theoretical side, it became clear that baryonic processes—particularly energy injection from supernovae—can also transform cusps into cores within CDM. On the observational side, the situation evolved from a simple “cores vs cusps” dichotomy to a broader diversity of inner density profiles across galaxies, even at fixed mass.

At the same time, constraints from systems such as the [Bullet Cluster](https://en.wikipedia.org/wiki/Bullet_Cluster) showed that large, velocity-independent self-interaction cross-sections are ruled out. While modest cross-sections remain viable—and can produce cores in dwarf galaxies—much larger cross-sections lead to more dramatic evolution. In this regime, heat conduction can drive a process known as *core collapse*, producing dense central regions. This naturally generates a wide diversity of inner density profiles, but the cross-sections required are incompatible with constraints from galaxy clusters.

This has led to increasing interest in velocity-dependent SIDM models, which are well motivated in particle physics. In these models, interactions are strong in low-velocity systems (like dwarf galaxies), but suppressed in high-velocity environments (like galaxy clusters), allowing them to evade existing constraints while retaining observable signatures.

For a broader overview of these ideas, see this [review paper I co-authored](https://arxiv.org/abs/2207.10638), or this [earlier review](https://arxiv.org/abs/1705.02358), which provides an excellent introduction.

---


## Simulating an SIDM Universe

During my PhD, I developed and implemented methods to include dark matter self-interactions in large-scale simulations, and ran some of the first cosmological hydrodynamical simulations with SIDM—variants of the [EAGLE](https://icc.dur.ac.uk/Eagle/) and [BAHAMAS](https://www.astro.ljmu.ac.uk/~igm/BAHAMAS/) simulation programmes. These allowed us to study how self-interactions affect galaxies and clusters in realistic environments, where dark matter, gas, and stars all evolve together. While these simulations were not released as a public dataset, I am very happy to share them—please get in touch if they would be useful.

A key focus of this work has been connecting simulations to observable quantities. For example, I have generated mock observations to study [how SIDM affects inferred cluster shapes in weak lensing analyses](https://arxiv.org/abs/2210.13474), where projection effects and measurement noise make it difficult to robustly distinguish between dark matter models.

Although I no longer run large SIDM simulations myself, I remain closely involved in this area. In particular, I have helped supervise new simulation efforts as part of the [Darkium](https://www.darkium.org) collaboration, using the publicly released [OpenGadget-3 code](https://arxiv.org/abs/2603.10107). This code addresses many of the numerical challenges involved in modelling processes such as core collapse, which are central to the SIDM models of most current interest.

I am also supervising the development of a suite of simulations of merging galaxy clusters—selected from large cosmological simulations—which will be used to extract constraints on the nature of dark matter from recent [JWST observations of the Bullet Cluster](https://science.nasa.gov/asset/webb/bullet-cluster-nircam-image/).


---

## Strong lensing tests of the nature of dark matter

The cleanest tests of dark matter physics come from systems that are dominated by dark matter itself. The challenge is that such systems are, by definition, difficult to observe directly. However, we can detect them through their gravitational effects. Two of the main approaches currently being explored are stellar streams and strong gravitational lensing (see my [lensing page](/research/strongLensing) for more details).

Strong lensing is particularly powerful because it can probe small-scale structure directly, through the perturbations caused by dark matter subhaloes. There have been a number of intriguing results on galaxy scales—from both optical imaging and ([recently](https://www.nature.com/articles/s41550-025-02746-w)) from radio interferometry—as well as hints of unusual behaviour in cluster-scale systems.

At the same time, these measurements are highly sensitive to modelling assumptions. A useful example is [SDSS J0946+1006](https://en.wikipedia.org/wiki/SDSSJ0946%2B1006), which has been interpreted as hosting an unusually dense dark matter subhalo. In [recent work](/publications/jackpotluminousperturber/), we showed that the data can also be explained if the perturber hosts a faint galaxy, without requiring extreme dark matter properties. This highlights how easily astrophysical effects can masquerade as new physics.

A key goal going forward is to test these analyses using realistic mock data generated from both CDM and SIDM simulations, and to understand how robust the inferred constraints really are.
