---
title: "About Me"
summary: "Computational astrophysics, inverse problems, statistical inference, and complex physical systems."
share: false
pager: false
show_date_updated: false
---

My name is Mohammad, and I am a New York City native, born and raised in Queens. I first became interested in physics through the [Science Research Mentoring Program (SRMP)](https://www.amnh.org/learn-teach/teens/science-research-mentoring-program) at the American Museum of Natural History. I later completed my bachelor's through the [City University of New York (CUNY) Baccalaureate for Unique and Interdisciplinary Studies](https://cunyba.cuny.edu/) program in computational astrophysics, followed by a master's in astrophysics at the [CUNY Graduate Center](https://www.gc.cuny.edu/astrophysics).

My academic background is in astrophysics, but I'm generally interested in computational problems as a whole. My work has included stellar surface mapping, brown-dwarf atmospheres, stellar spectroscopy, Galactic archaeology, and numerical simulations. I am also interested in problems in condensed matter, soft matter, and biophysics.

---

## Research Interests

Many problems I've worked on share the same structure. We observe a light curve, a spectrum, a spatial distribution, or some other incomplete measurement, and use it to infer the physical system that produced it.

```text
Physical system
      ↓
Physical model
      ↓
Observable data
```

The forward problem asks: **If I know the physical system, what should I observe?** The inverse problem asks: **If I know what I observed, what can I infer about the physical system?** The second question is harder because measurements contain noise, multiple configurations can produce similar observations, and some information may not be present in the data at all.

That intersection of physics, mathematics, statistics, and computation is where things become especially cool to me.

---

## Mapping a Star You Can't Resolve

My master's thesis is a visual example of an inverse problem. For almost every star, we cannot resolve the surface well enough to see individual starspots. Instead, we measure a light curve: the star's brightness over time. As the star rotates, darker regions move into and out of view, changing its observed brightness.

We therefore work backward from a one-dimensional time series toward a possible two-dimensional surface map. The goal is to determine which surface structures are supported by the observations, while accounting for noise and ambiguity.

---

## Spherical Harmonics

One useful mathematical tool is the **spherical-harmonic basis**. Spherical harmonics can be thought of as sine waves wrapped around a sphere. Like Fourier modes for periodic signals, they can be combined to describe patterns of different scales across a spherical surface.

The animation below, made with Manim, shows individual real spherical-harmonic modes.

<div style="max-width: 850px; margin: 2rem auto;">
  <video autoplay muted loop playsinline controls style="display:block;width:100%;border-radius:0.8rem;">
    <source src="/media/spherical-harmonics.mp4" type="video/mp4">
    Your browser does not support embedded video.
  </video>
</div>

<p style="max-width:700px;margin:-1rem auto 2rem;text-align:center;font-size:0.85rem;opacity:0.7;">
  Increasing the degree allows progressively finer angular structure.
</p>

The lobed shapes visualize the mathematics; the star itself is not being deformed. The basis describes how a quantity such as **brightness varies across the surface of a fixed sphere**. The displayed modes illustrate how the degree \(\ell\) and order \(m\) change the angular pattern.

Higher values of \(\ell\) represent smaller-scale structure. A complete surface map can be built from a weighted combination of modes, and the inference problem is to determine which combinations the light curve supports.

---

## Different Systems, Similar Computational Problems

The measurements differ across my research, but each project uses data and models to infer something about a physical system:

- [Stellar surface mapping](/research/starspots/): infer starspot patterns from rotational light curves.
- [Brown dwarfs and giant exoplanets](/research/brown-dwarf-atmospheres/): study atmospheric structure through rotational variability.
- [Galactic archaeology](/research/jhelum-stellar-stream/): use stellar chemistry and phase-space data to characterize the Jhelum stream.
- [Stellar spectroscopy](/research/stellar-spectroscopy/): connect spectral features with stellar properties.

Work with simulations and spatial statistics also led me to a broader question: **How does large-scale structure emerge from comparatively simple physical rules?**

---

## What I'm Interested in Now

I’m interested in applying computational approaches from astrophysics—including inverse methods, probabilistic modeling, numerical simulation, and scientific computing—to complex systems in soft condensed matter and biophysics. I’m especially drawn to emergent behavior, nonequilibrium systems, and the relationship between microscopic interactions and macroscopic structure.

---

## Outside of Physics

Outside of physics, I enjoy sports, especially basketball (<span style="color:#F58426">Go Knicks!</span>). I also enjoy competitive Pokémon, particularly the official VGC formats, and looking at metagame trends. [Explore my VGC metagame project →](/projects/vgc-metagame/)

---

## Explore My Work

- [Projects](/projects/)
- [Research](/research/)
- [Publications](/publications/)
- [Presentations](/events/)
- [Curriculum Vitae](/uploads/Mohammad_Alvi_Refat_CV.pdf)
