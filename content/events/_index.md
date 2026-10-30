---
title: Presentations
type: landing
cms_exclude: true
summary: "Research talks and posters by Mohammad Alvi Refat."
cascade:
  share: false
design:
  spacing: '5rem'

sections:
  - block: collection
    id: talks
    content:
      title: '<h2>Talks</h2>'
      text: Research talks and recorded presentations.
      count: 0 # 0 = show every talk (the default cap is 5)
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
      title: '<h2>Posters</h2>'
      text: Conference and symposium posters.
      count: 0 # 0 = show every poster (the default cap is 5)
      filters:
        folders:
          - posters
      sort_by: weight
      sort_ascending: true
    design:
      view: card
      columns: 3
      fill_image: true
      show_date: false
      show_read_time: false

---
