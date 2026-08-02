---
layout: home
permalink: /
title: ""
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<div class="home-gradient-zone">
  <div class="home-page-shell">
    {% include profile-hero.html %}
  </div>
</div>

<div class="home-page-shell home-page-shell--sections">
  <section class="home-section">
    {% include section-heading.html title="Research Areas" %}
    <div class="feature-grid feature-grid--three">
      {% assign featured_research = site.data.research_cards | where: "featured", true | sort: "order" %}
      {% for project in featured_research limit: 3 %}
        {% include research-card.html project=project %}
      {% endfor %}
    </div>
  </section>

  <section class="home-section">
    {% include section-heading.html title="Recorded Talks" %}
    <div class="feature-grid feature-grid--two">
      {% assign recorded_talks = site.talks | where: "recorded", true | sort: "card_order" %}
      {% for talk in recorded_talks limit: 2 %}
        {% include talk-card.html talk=talk %}
      {% endfor %}
    </div>
  </section>

  <section class="home-section">
    {% capture publication_note %}<a class="publication-list-button" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener noreferrer">Full publication profile on Google Scholar</a><span class="publication-note-copy">Below I highlight my thesis and peer-reviewed work.</span>{% endcapture %}
    {% include section-heading.html title="Publications" note=publication_note %}
    <div class="feature-grid feature-grid--two">
      {% assign featured_publications = site.publications | where: "featured", true | sort: "date" | reverse %}
      {% for publication in featured_publications limit: 2 %}
        {% include publication-card.html publication=publication %}
      {% endfor %}
    </div>
  </section>
</div>
