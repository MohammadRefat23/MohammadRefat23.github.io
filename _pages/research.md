---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

<p>
My research focuses on developing computational methods for extracting physical insight from complex data. Across projects in astrophysics, spectroscopy, Galactic archaeology, and time-series analysis, I have used scientific computing, statistical inference, numerical modeling, and inverse methods to study complex physical systems.
</p>

<h2>Featured Projects</h2>

{% assign sorted_projects = site.projects | sort: "order" %}

{% for project in sorted_projects %}
  <div style="margin-bottom: 2em;">
    <h3>
      <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
    </h3>

    {% if project.excerpt %}
      <p>{{ project.excerpt }}</p>
    {% endif %}

    {% if project.methods %}
      <p>
        <strong>Methods:</strong>
        {{ project.methods | join: ", " }}
      </p>
    {% endif %}

    <p>
      <a href="{{ project.url | relative_url }}">Read more →</a>
    </p>
  </div>
{% endfor %}