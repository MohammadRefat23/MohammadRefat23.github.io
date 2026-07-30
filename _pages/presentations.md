---
layout: archive
title: "Talks and presentations"
permalink: /talks/
author_profile: true
redirect_from: 
- /talks/
---

{% for post in site.talks reversed %}
  {% include presentation-card.html %}
{% endfor %}

---