---
layout: archive
title: "Talks and presentations"
permalink: /talks/
author_profile: false
redirect_from: 
- /talks/
---

{% for post in site.talks reversed %}
  {% include presentation-card.html %}
{% endfor %}

---