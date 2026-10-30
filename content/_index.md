---
# Leave the homepage title empty to use the site title
title: ''
date: 2026-10-30
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: |-
        My research interests are in computational physics and numerical methods: molecular dynamics and Monte Carlo simulation, inverse problems, and Bayesian inference (MCMC) for fitting and testing physical models against data, such as force-field parameterization. Applications in biological and materials physics, including how metal–peptide frameworks respond to water. My research so far has been in astrophysics, where I used light-curve inversion, spectroscopy, and statistical modeling to recover stellar surfaces, brown-dwarf atmospheres, and the chemistry of a stellar stream.

        **Applying to physics PhD programs for Fall 2027.**

        {{< button text="View Research" url="/research/" />}}
        {{< button text="View Projects" url="/projects/" />}}
        {{< button text="CV & Résumé" url="/cv/" />}}

        Email: moref17 AT gmail DOT com
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: large # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: collection
    id: research
    content:
      title: '<h2>Featured Research</h2>'
      text: 'Computational and statistical methods for studying physical systems.'
      count: 0 # 0 = show every featured project (the default cap is 5)
      filters:
        folders:
          - research
        featured_only: true
      sort_by: weight
      sort_ascending: true
    design:
      view: article-grid
      fill_image: false
      columns: 3
      show_date: false
      show_read_time: false
      show_read_more: false
  - block: collection
    id: talks
    content:
      title: '<h2>Recorded Talks</h2>'
      filters:
        folders:
          - events
        featured_only: true
    design:
      view: card
      show_read_time: false
  - block: collection
    id: papers
    content:
      title: '<h2>Publications</h2>'
      text:  |-
        {{< button text="Full publication profile on Google Scholar" url="https://scholar.google.com/citations?user=tXosG1EAAAAJ&hl=en" />}}  
        Below I highlight my thesis and peer-reviewed work. 
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
      show_read_time: false
---
