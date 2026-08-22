---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
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
        {{< button text="View Research" url="/research/" />}}
        {{< button text="Download CV" url="/uploads/Mohammad_Refat_CV.pdf" />}}
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
      title: Featured Research
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
      title: Recorded Talks
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
      title: Publications
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
  #- block: collection
  #  content:
  #    title: Recent Publications
  #    text: ''
  #    filters:
  #      folders:
  #        - publications
  #      exclude_featured: false
  #  design:
  #    view: citation
  - block: collection
    demo: true # Only display this section in the Hugo Blox Builder demo site (to hide it for now, maybe should delete it)
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
