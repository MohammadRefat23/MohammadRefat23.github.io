---
title: Presentations
type: landing
cms_exclude: true

design:
  spacing: '5rem'

sections:
  - block: collection
    id: talks
    content:
      title: Talks
      text: Research talks and recorded presentations.
      filters:
        folders:
          - events
      sort_by: date
      sort_ascending: false
    design:
      view: card
      columns: 3
      fill_image: true
      show_date: true
      show_read_time: false

  - block: collection
    id: posters
    content:
      title: Posters
      text: Selected research posters.
      filters:
        folders:
          - posters
      sort_by: date
      sort_ascending: false
    design:
      view: card
      columns: 3
      fill_image: true
      show_date: true
      show_read_time: false
---
