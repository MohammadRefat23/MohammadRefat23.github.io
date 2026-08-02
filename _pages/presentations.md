---
layout: clean
title: "Presentations"
permalink: /presentations/
author_profile: false
description: "Recorded talks, conference presentations, and posters."
wide: true
redirect_from:
  - /talks/
---

<section class="presentation-section">
  <h2>Recorded talks</h2>
  <div class="feature-grid feature-grid--two">
    {% assign recorded_talks = site.talks | where: "recorded", true | sort: "card_order" %}
    {% for talk in recorded_talks %}
      {% include talk-card.html talk=talk %}
    {% endfor %}
  </div>
</section>

<section class="presentation-section">
  <h2>Additional talks</h2>
  <ul class="presentation-list">
    {% assign additional_talks = site.talks | sort: "date" | reverse %}
    {% for talk in additional_talks %}
      {% unless talk.recorded %}{% include presentation-list-item.html item=talk %}{% endunless %}
    {% endfor %}
  </ul>
</section>

<section class="presentation-section">
  <h2>Posters</h2>
  <ul class="presentation-list">
    {% for poster in site.data.posters %}
      {% include presentation-list-item.html item=poster %}
    {% endfor %}
  </ul>
</section>
