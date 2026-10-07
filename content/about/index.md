---
title: "About Me"
summary: "Computational physicist interested in numerical modeling, statistical inference, inverse problems, and complex physical systems."
share: false
pager: false
show_date_updated: false
---

My name is Mohammad, and I am a New York City native. I first became interested in physics through the [Science Research Mentoring Program (SRMP)](https://www.amnh.org/learn-teach/teens/science-research-mentoring-program) at the American Museum of Natural History. I earned a bachelor's degree in computational astrophysics through the [CUNY Baccalaureate for Unique and Interdisciplinary Studies](https://cunyba.cuny.edu/) and an M.S. in astrophysics at the [CUNY Graduate Center](https://www.gc.cuny.edu/astrophysics).

My research has included stellar surface mapping, brown-dwarf atmospheres, stellar spectroscopy, galactic archaeology, and numerical simulations. Across these areas, I’m drawn to computational problems that connect physical models with incomplete or noisy observations. I’m now interested in applying those methods to soft condensed matter and biophysics.

---

## Research Interests

Many physical systems cannot be observed directly. We measure a light curve, a spectrum, or a spatial distribution, then use a model to infer the hidden system that produced it. I’m especially interested in this inverse problem: what can we reliably learn about a physical system from the data available to us?

That question brings together physics, mathematics, statistics, and computation. Measurements contain noise, different physical configurations can produce similar observations, and some information may not be present in the data at all. Understanding those limits is part of the problem.

---

## Mapping a Star You Can't Resolve

For my master's thesis, I studied how much of a star's surface structure can be inferred from its brightness over time. As a star rotates, starspots move in and out of view and alter its light curve. The challenge is to work backward from that one-dimensional time series to a possible two-dimensional surface map.

The animation below shows real spherical-harmonic modes, a mathematical basis I used to represent surface brightness patterns. The star is not physically deformed; the modes describe how brightness varies over a fixed sphere. Combining modes lets a model represent progressively finer structure, while the light curve constrains which combinations are supported by the observations.

<div style="max-width: 850px; margin: 2rem auto;">
  <video autoplay muted loop playsinline controls style="display:block;width:100%;border-radius:0.8rem;">
    <source src="/media/spherical-harmonics.mp4" type="video/mp4">
    Your browser does not support embedded video.
  </video>
</div>

<p style="max-width:700px;margin:-1rem auto 2rem;text-align:center;font-size:0.85rem;opacity:0.7;">
  Individual real spherical-harmonic modes. Increasing the degree allows progressively finer angular structure.
</p>


---

## Similar Methods Across Different Systems

The physical systems I’ve studied vary, but many of the computational questions recur: how do we connect indirect measurements to the properties of the system that produced them?

**Stellar surface mapping.** I used time-series analysis, forward modeling, and statistical inference to test what starspot patterns could be recovered from rotational light curves. [Explore the project →](/research/starspots/)

**Brown dwarfs and giant exoplanets.** I studied rotational variability as a way to infer evolving cloud structures on unresolved atmospheres. [Explore the project →](/research/brown-dwarf-atmospheres/)

**Galactic archaeology.** I worked on characterizing the Jhelum stellar stream using stellar chemistry, spectroscopy, velocities, and phase-space information. [Explore the project →](/research/jhelum-stellar-stream/)

**Stellar spectroscopy.** I analyzed spectra to estimate physical properties such as stellar parameters and chemical abundances. [Explore the project →](/research/stellar-spectroscopy/)

**Simulations and spatial structure.** I used two-point statistics to study metallicity structure in simulated star-forming gas. [Explore the project →](/research/star-forming-ism/)

---

## What I'm Interested in Now

I’m interested in applying inverse methods, probabilistic modeling, numerical simulation, and scientific computing to complex systems in soft condensed matter and biophysics. I’m especially drawn to emergent behavior, nonequilibrium systems, and the relationship between microscopic interactions and macroscopic structure.

---

## Outside of Physics

Outside of physics, I enjoy basketball (Go Knicks!) and competitive Pokémon VGC. I built an interactive explorer for Pokémon Champions Doubles data as a way to combine those interests with data visualization. [Explore the VGC project →](/projects/vgc-metagame/)

---

## Explore My Work

- [Projects](/projects/)
- [Research](/research/)
- [Publications](/publications/)
- [Presentations](/events/)
- [Curriculum Vitae](/uploads/Mohammad_Alvi_Refat_CV.pdf)
