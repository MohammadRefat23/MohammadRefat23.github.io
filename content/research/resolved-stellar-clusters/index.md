---
title: "Resolved Stellar Clusters: Probabilistic Membership Inference"
summary: "Auditing and correcting the statistics of an error-aware mixture model that assigns stellar-cluster membership from Gaia astrometry."
date: 2026-09-01
hide_date: true
featured: true
weight: 5
authors:
  - admin
card_label: "Ongoing Statistical Modeling"
card_placeholder: "Ongoing project"
tags:
  - "Statistical Inference"
  - "Scientific Computing"
  - "Stellar Clusters"
---

**Project context:** Volunteer Researcher · American Museum of Natural History · Advisor: Dave Zurek · Sep 2026 – present

## Overview

This ongoing project at the American Museum of Natural History estimates which stars belong to resolved stellar clusters using **Gaia** astrometry. The Python code fits an **expectation–maximization (EM) mixture model** that separates cluster members from field stars, using each star's reported measurement errors, and assigns every star a membership probability.

## My Contributions

- Audited the statistical calculations in the membership code and corrected errors in them.
- Incorporated per-star proper-motion measurement uncertainties into the mixture-model likelihood.
- Evaluated how the field-star model interacts with one or more candidate cluster components.
- Checked model assumptions and probability outputs with diagnostic calculations and visualizations.

## Methods

The workflow uses Python for data handling and numerical analysis. An expectation–maximization algorithm fits a mixture of cluster and field-star components to Gaia proper motions, with each star's measurement errors included in its likelihood, and returns per-star membership probabilities.

## Current Status

The project is in progress. I am validating the corrected probability calculations; final model validation and scientific conclusions are not yet reported here.
