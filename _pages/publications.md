---

layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

My publications and thesis work span Galactic archaeology, stellar spectroscopy, time-series analysis, and computational inverse problems.

{% assign publications = site.publications | sort: "date" | reverse %}

{% for post in publications %}

<div class="publication-entry">

  <h2 class="publication-title">
    {{ post.title }}
  </h2>

  <p class="publication-meta">
    {% if post.authors %}
      {{ post.authors }}<br>
    {% endif %}


{% if post.venue %}
  <em>{{ post.venue }}</em>
{% endif %}

{% if post.date %}
  · {{ post.date | date: "%Y" }}
{% endif %}

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

{% if post.excerpt %} <p class="publication-summary">
{{ post.excerpt | strip_html | strip_newlines }} </p>
{% endif %}

  <div class="project-actions">


{% if post.paperurl %}
  <a href="{{ post.paperurl }}"
     class="btn btn--primary"
     target="_blank"
     rel="noopener">
    View Publication
  </a>
{% endif %}

{% if post.pdfurl %}
  <a href="{{ post.pdfurl }}"
     class="btn btn--primary"
     target="_blank"
     rel="noopener">
    PDF
  </a>
{% endif %}

{% if post.doiurl %}
  <a href="{{ post.doiurl }}"
     class="btn btn--primary"
     target="_blank"
     rel="noopener">
    DOI
  </a>
{% endif %}

{% if post.projecturl %}
  <a href="{{ post.projecturl | relative_url }}"
     class="btn btn--primary">
    Related Project
  </a>
{% endif %}


  </div>

</div>

{% unless forloop.last %}

<hr class="publication-divider">
{% endunless %}

{% endfor %}
