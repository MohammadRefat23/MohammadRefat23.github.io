---

layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
--------------------

My publications and thesis work span Galactic archaeology, stellar spectroscopy, time-series analysis, and computational inverse problems. Each entry links to a dedicated page describing the work, its main findings, and my contributions.

---

## Publications and Thesis

{% assign publications = site.publications | sort: "date" | reverse %}

{% for post in publications %}

<div class="research-card publication-card">

{% if post.image %} <a href="{{ post.url | relative_url }}"> <img src="{{ post.image | relative_url }}"
        alt="{{ post.title | escape }}"
        class="project-image research-media"> </a>
{% endif %}

  <div class="research-card-body">

```
<h2>
  <a href="{{ post.url | relative_url }}">
    {{ post.title }}
  </a>
</h2>

<p class="project-meta research-meta">
  <strong>
    {% if post.venue %}
      {{ post.venue }}
    {% endif %}

    {% if post.date %}
      · {{ post.date | date: "%Y" }}
    {% endif %}
  </strong>

  {% if post.category %}
    <br>
    {% case post.category %}
      {% when "journal-article" %}
        Journal Article
      {% when "thesis" %}
        M.S. Thesis
      {% when "conference-proceeding" %}
        Conference Proceeding
      {% when "preprint" %}
        Preprint
      {% else %}
        {{ post.category | replace: "-", " " | capitalize }}
    {% endcase %}
  {% endif %}
</p>

{% if post.excerpt %}
  <p>
    {{ post.excerpt | strip_html | strip_newlines }}
  </p>
{% endif %}

{% if post.tags %}
  <div class="project-tags">
    {% for tag in post.tags %}
      <span class="project-tag">{{ tag }}</span>
    {% endfor %}
  </div>
{% endif %}

<div class="project-actions">
  <a href="{{ post.url | relative_url }}"
     class="btn btn--primary">
    View Publication
  </a>

  {% if post.paperurl %}
    <a href="{{ post.paperurl }}"
       class="btn btn--primary"
       target="_blank"
       rel="noopener">
      Read Paper
    </a>
  {% endif %}
</div>
```

  </div>
</div>

{% endfor %}
