---
layout: clean
title: "Research"
permalink: /research/
author_profile: false
description: "Computational projects centered on inverse problems, time-series analysis, spectroscopy, and statistical modeling."
wide: true
---

<div class="feature-grid feature-grid--three">
  {% assign projects = site.data.research_cards | sort: "order" %}
  {% for project in projects %}
    {% include research-card.html project=project %}
  {% endfor %}
</div>
