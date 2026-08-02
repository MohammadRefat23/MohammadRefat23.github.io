---
layout: clean
title: "Publications"
permalink: /publications/
author_profile: false
description: "Peer-reviewed research and thesis work in computational astrophysics."
wide: true
---

<p class="page-intro-link"><a href="{{ site.author.googlescholar }}" target="_blank" rel="noopener noreferrer">Full publication profile on Google Scholar <span aria-hidden="true">↗</span></a></p>

<div class="feature-grid feature-grid--two">
  {% assign publications = site.publications | sort: "date" | reverse %}
  {% for publication in publications %}
    {% include publication-card.html publication=publication %}
  {% endfor %}
</div>
