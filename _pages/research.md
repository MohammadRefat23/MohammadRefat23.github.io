---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

My research focuses on developing computational methods for extracting physical insight from complex data. Across projects in astrophysics, spectroscopy, Galactic archaeology, and time-series analysis, I have used scientific computing, statistical inference, numerical modeling, and inverse methods to study complex physical systems.

A common theme throughout my work is the use of computational approaches to solve inverse problems: inferring hidden physical structure from indirect, incomplete, or noisy observations. Although my previous work has focused primarily on astrophysical applications, my broader research interests lie in computational physics, soft condensed matter, and biological physics.

---

## Research Projects

<div class="research-card">
  <img src="/images/research/starspots/aumicstarry.png" alt="Starspot inference project image">
  <div>
    <h2>Starspot Inference Using Light Curve Inversion Techniques</h2>
    <p><strong>M.S. Thesis, CUNY Graduate Center, 2023–2025</strong><br>
    Advisor: Dr. Lucy Lu</p>
    <p>
    Developed computational approaches for reconstructing stellar surface features from photometric light curves. This project treated starspot mapping as an inverse problem, using time-series analysis, forward modeling, and numerical methods to explore how surface structure can be inferred from unresolved stellar observations.
    </p>
    <p><strong>Methods:</strong> Python, starry, light curve inversion, time-series analysis, inverse problems, statistical inference</p>
    <p>
      <a href="https://academicworks.cuny.edu/gc_etds/6480/" target="_blank">Thesis</a>
    </p>
  </div>
</div>

<div class="research-card">
  <img src="/images/research/browndwarfs/2mass.png" alt="Brown dwarf atmospheres project image">
  <div>
    <h2>Brown Dwarf and Giant Exoplanet Atmospheres</h2>
    <p><strong>American Museum of Natural History, 2021–2023</strong><br>
    Advisor: Dr. Johanna Vos</p>
    <p>
    Studied atmospheric variability in brown dwarfs and giant exoplanets through analysis of photometric light curves. This work focused on using unresolved time-series observations to investigate rotational variability and infer atmospheric structure in low-mass objects.
    </p>
    <p><strong>Methods:</strong> Python, photometric time-series analysis, atmospheric variability, computational modeling</p>
  </div>
</div>

<div class="research-card">
  <img src="/images/research/jhelum/alfe.png" alt="Jhelum stellar stream project image">
  <div>
    <h2>Galactic Archaeology: The Jhelum Stellar Stream</h2>
    <p><strong>American Museum of Natural History, 2020–2021</strong><br>
    Advisor: Dr. Allyson Sheffield</p>
    <p>
    Analyzed APOGEE-2 spectroscopic data to identify and characterize candidate members of the Jhelum stellar stream. This project used chemical tagging and statistical analysis to study stellar populations and contribute to the broader reconstruction of the Milky Way's assembly history.
    </p>
    <p><strong>Methods:</strong> APOGEE-2 spectroscopy, chemical tagging, statistical analysis, Galactic archaeology</p>
  </div>
</div>

<div class="research-card">
  <img src="/images/research/spectroscopy/arcturus.png" alt="Stellar spectroscopy project image">
  <div>
    <h2>Stellar Spectroscopy and Chemical Abundances</h2>
    <p><strong>American Museum of Natural History, 2018–2020</strong><br>
    Advisor: Dr. Allyson Sheffield</p>
    <p>
    Processed and analyzed stellar spectra to derive chemical abundances and characterize stellar populations. This early research experience developed my foundation in observational data analysis, spectral line measurement, and quantitative stellar astrophysics.
    </p>
    <p><strong>Methods:</strong> Spectroscopy, equivalent widths, chemical abundance analysis, stellar populations</p>
  </div>
</div>

<div class="research-card">
  <video autoplay loop muted playsinline>
  <source src="/images/research/ism/PlotFluct.mp4" type="video/mp4">
</video>
  <div>
    <h2>Two-Point Statistics in the Star-Forming ISM</h2>
    <p><strong>Center for Computational Astrophysics, Flatiron Institute, 2018</strong><br>
    Advisor: Dr. Chang-Goo Kim</p>
    <p>
    Investigated metallicity correlations in star-forming regions using statistical methods. This project introduced me to computational approaches for studying complex astrophysical systems through spatial correlations and numerical analysis.
    </p>
    <p><strong>Methods:</strong> Two-point statistics, numerical analysis, star formation, interstellar medium</p>
  </div>
</div>

<style>
.research-card {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 1.5em;
  margin: 2.5em 0;
  align-items: start;
}

.research-card img {
  width: 220px;
  height: 160px;
  object-fit: cover;
  border-radius: 6px;
  border: 1px solid #ddd;
}

.research-card video {
  width: 220px;
  height: 160px;
  object-fit: cover;
  border-radius: 6px;
  border: 1px solid #ddd;
}

.research-card h2 {
  margin-top: 0;
}

@media (max-width: 700px) {
  .research-card {
    grid-template-columns: 1fr;
  }

  .research-card img {
    width: 100%;
    height: auto;
  }
}
</style>