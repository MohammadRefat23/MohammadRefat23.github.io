---
title: Accelerated calibration of semi-analytic galaxy formation models

event: MockNYC
event_url: https://mocknyc.owlstown.net/pages/7882

summary: A method for rapidly calibrating semi-analytic galaxy formation models using stellar-to-halo mass relation constraints.
abstract: I will present an accelerated calibration framework for semi-analytic galaxy formation models, demonstrated with Galacticus. Rather than fitting directly to properties such as the low-redshift stellar mass function (SMF) - which requires evolving thousands of halos per likelihood evaluation - I constructed a fast likelihood from the stellar-to-halo mass relation (SHMR; mean and scatter) evaluated at a small set of target halo masses, reducing each evaluation to simulating only tens of galaxies. I will discuss the pros and cons of such an approach, as well as attempts to extend this approach to handle calibrating to properties other than stellar masses (stellar sizes, black hole masses, etc.).

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2026-01-13T12:20:00Z'
#date_end: '2030-06-01T15:00:00Z'
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: '2017-01-01T00:00:00Z'

authors:
  - admin

tags: []

# Is this a featured talk? (true/false)
featured: true
hide_featured: true

#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

links:
  - type: code
    url: https://github.com/Andrew-Robertson/CalibratingGalacticus-Paper1
  - type: slides
    url: Robertson_v1.pdf
  - type: video
    url: https://www.youtube.com/watch?v=a4LUxn30VSo
  - type: preprint
    provider: arxiv
    id: 2509.00143

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
  - example
---

{{< youtube a4LUxn30VSo >}}
