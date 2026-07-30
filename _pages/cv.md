---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
---

<div style="margin-bottom: 1rem;">
  <a
    id="cv-download-link"
    href="{{ '/assets/cv/cv.pdf' | relative_url }}"
    target="_blank"
    rel="noopener"
  >
    Open CV in a new tab
  </a>
</div>

<iframe
  id="cv-frame"
  width="100%"
  height="1050px"
  style="border: none;"
  title="Mohammad Refat Curriculum Vitae">
</iframe>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const cvPath = "{{ '/assets/cv/cv.pdf' | relative_url }}";
    const cacheBuster = Date.now();
    const refreshedUrl = `${cvPath}?v=${cacheBuster}`;

    document.getElementById("cv-frame").src = refreshedUrl;
    document.getElementById("cv-download-link").href = refreshedUrl;
  });
</script>
