---

title: "Two-Point Statistics in the Star-Forming Interstellar Medium"
summary: "Using two-point statistics to measure the characteristic scale of metallicity homogeneity in simulated star-forming gas."
featured: false
weight: 50
authors:
  - admin
tags:
  - "Interstellar Medium"
  - "Star Formation"
  - "Scientific Computing"
  - "Data Visualization"
image:
  preview_only: true
---

<video controls playsinline muted loop style="width: 100%; border-radius: 0.5rem;">
  <source src="PlotFluct.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>

*The simulation shows metallicity fluctuations evolving as supernovae inject metals and turbulence redistributes them through the interstellar medium.*

Chemical tagging uses stellar abundances to identify stars that may have formed together, but its effectiveness depends on the spatial scale over which star-forming gas is chemically homogeneous. In this project, I analyzed the metal distribution in **TIGRESS** simulations of the star-forming interstellar medium. These simulations include magnetohydrodynamics, self-gravity, Galactic shear, star formation, and supernova feedback. Supernovae play two competing roles: they introduce localized metal enrichment while also driving turbulence that mixes those metals through the gas.

I quantified the spatial structure of the metallicity field using a **two-point correlation function**, measuring how rapidly the similarity between metallicity fluctuations declined with separation. The correlation fell to one-half at an average separation of approximately **\(120 \pm 25\) pc** and approached zero at scales of roughly 300 pc. I also compared the evolving half-correlation scale with the supernova rate and velocity dispersion. The initial analysis did not reveal a clear direct relationship, suggesting that the competition between enrichment and turbulent mixing requires a more detailed time-dependent treatment.

![Evolution of the metallicity half-correlation length in the TIGRESS simulation.](correlation-length.png)

*The characteristic scale at which the metallicity correlation falls to one-half fluctuates around approximately \(120 \pm 25\) pc.*

{{< button text="View the Research Talk" url="/events/2018-08-02-talk-1/" />}}
