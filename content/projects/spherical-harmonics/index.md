---
title: Spherical Harmonics Explorer
summary: An animation and interactive tool showing how the degree and order of a spherical harmonic change its surface pattern.
date: 2026-10-30
hide_date: true
project: true
stack:
  - Manim
  - JavaScript
repo_url: https://github.com/MohammadRefat23/MohammadRefat23.github.io/blob/main/manim/spherical_harmonics.py
project_url: /projects/spherical-harmonics/
tags:
  - Data Visualization
  - Interactive Tools
  - Scientific Computing
card_label: Interactive Tool
card_image: /media/spherical-harmonics-card.jpg
card_image_alt: "Frame from the spherical-harmonics animation showing the l = 2, m = 2 harmonic."
---

Spherical harmonics describe patterns on a sphere. They are the basis I used to represent stellar and brown-dwarf surfaces in my [starspot](/research/starspots/) and [brown-dwarf atmosphere](/research/brown-dwarf-atmospheres/) research. The animation and interactive tool below show how changing the degree \(\ell\) and order \(m\) changes the surface pattern.

{{< site-video src="media/spherical-harmonics.mp4" label="Animation of spherical-harmonic surface patterns as degree and order change." >}}

{{< spherical-harmonics >}}

The animation was made with [Manim](https://www.manim.community/); its [source script](https://github.com/MohammadRefat23/MohammadRefat23.github.io/blob/main/manim/spherical_harmonics.py) is in this site's repository.
