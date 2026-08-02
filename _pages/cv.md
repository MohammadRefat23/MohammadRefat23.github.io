---
layout: clean
title: "Curriculum Vitae"
permalink: /cv/
author_profile: false
description: "View the current CV below or download a copy."
wide: true
---

<div class="cv-toolbar">
  <a id="cv-download-link" class="site-button site-button--primary" href="{{ '/assets/cv/cv.pdf' | relative_url }}" download>Download CV</a>
  <a id="cv-open-link" class="site-button site-button--ghost" href="{{ '/assets/cv/cv.pdf' | relative_url }}" target="_blank" rel="noopener">Open in a new tab</a>
</div>

<div class="cv-viewer">
  <iframe id="cv-frame" title="Mohammad Alvi Refat curriculum vitae" loading="lazy"></iframe>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const cvPath = "{{ '/assets/cv/cv.pdf' | relative_url }}";
    const refreshedUrl = `${cvPath}?v=${Date.now()}`;
    document.getElementById("cv-frame").src = refreshedUrl;
    document.getElementById("cv-open-link").href = refreshedUrl;
  });
</script>
