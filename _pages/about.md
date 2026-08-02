---
layout: home
permalink: /
title: ""
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

{% include profile-hero.html %}

<section class="home-section">
  {% include section-heading.html title="Research areas" url="/research/" link_text="All research" %}
  <div class="feature-grid feature-grid--three">
    {% assign featured_research = site.data.research_cards | where: "featured", true | sort: "order" %}
    {% for project in featured_research limit: 3 %}
      {% include research-card.html project=project %}
    {% endfor %}
  </div>
</section>

<section class="home-section">
  {% include section-heading.html title="Recorded talks" url="/presentations/" link_text="All presentations" %}
  <div class="feature-grid feature-grid--two">
    {% assign recorded_talks = site.talks | where: "recorded", true | sort: "card_order" %}
    {% for talk in recorded_talks limit: 2 %}
      {% include talk-card.html talk=talk %}
    {% endfor %}
  </div>
</section>

<section class="home-section">
  {% include section-heading.html title="Publications" url="/publications/" link_text="All publications" %}
  <div class="feature-grid feature-grid--two">
    {% assign featured_publications = site.publications | where: "featured", true | sort: "date" | reverse %}
    {% for publication in featured_publications limit: 2 %}
      {% include publication-card.html publication=publication %}
    {% endfor %}
  </div>
</section>
