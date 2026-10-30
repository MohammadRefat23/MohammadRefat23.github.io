---
title: "Course Project: MCMC Fitting of Starspot Parameters"
summary: Graduate course project using emcee to recover a starspot's contrast and size from a synthetic starry light curve.
date: 2023-12-11
hide_date: true
project: true
stack:
  - Python
  - starry
  - emcee
  - corner
repo_url: https://github.com/MohammadRefat23/StarryStarSpots_MCMC
tags:
  - Bayesian Inference
  - Inverse Problems
  - Course Project
card_label: Course Project
card_image: /media/starry-starspots-mcmc-card.png
card_image_alt: "Corner plot of posterior samples for starspot contrast and spot fraction, with the true values marked."
---

This was a course project for Computational Methods in Physics at the CUNY Graduate Center (Fall 2023). It is separate from my M.S. thesis code.

I generated a synthetic rotational light curve from a single starspot with **starry**, then used the **emcee** ensemble sampler to infer the spot's contrast and spot fraction. The likelihood was based on \(\chi^2\) between the model and synthetic light curves, with uniform priors on both parameters. I ran 64 walkers, discarded burn-in samples, and compared the posterior with the true input values in a corner plot.

![Corner plot of posterior samples for starspot contrast and spot fraction.](/media/starry-starspots-mcmc-card.png)

*The posterior covers the true values (blue lines) but shows a strong anti-correlation between contrast and spot fraction: a darker, smaller spot and a fainter, larger spot produce similar light curves.*

{{< button text="View Code" url="https://github.com/MohammadRefat23/StarryStarSpots_MCMC" />}}
