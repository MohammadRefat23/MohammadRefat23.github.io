---
title: 'Projects'
date: 2024-05-19
type: landing

cascade:
  share: false

design:
  # Section spacing
  spacing: '0rem'

# Page sections
sections:
  - block: collection
    content:
      title: Primary Research Areas
      text: These pages give an overview of some of the main things I currently work on.
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
  # - block: markdown
  #   content:
  #     title: Things I Think About
  #     text: |-
  #       Much of my work is driven by a broader set of questions that don’t always fit neatly into a single project:

  #       - When can we trust an inference about dark matter, and when are we being misled by modelling assumptions?  
  #       - How can simulations be used not just to interpret data, but to test entire analysis pipelines end-to-end?  
  #       - What are the real limitations of strong lensing as a probe of small-scale structure?  
  #       - How do observational effects and galaxy formation physics combine to shape what we actually measure?  

  #       I’m particularly interested in approaches that stress-test our conclusions, rather than simply refining them.
  #   design:
  #     columns: '1'
---