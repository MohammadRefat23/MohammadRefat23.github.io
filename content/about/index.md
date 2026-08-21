---
title: "About Me"
summary: "Computational physicist interested in numerical modeling, statistical inference, inverse problems, and complex physical systems."
---

# About Me

My name is Mohammad I am a New York City native, born and raised in Queens. I first became interested in physics through the [Science Research Mentoring Program (SRMP)](https://www.amnh.org/learn-teach/teens/science-research-mentoring-program) at the American Museum of Natural History. I later completed my bachelor's through the [City University of New York (CUNY) Baccalaureate for Unique and Interdisciplinary Studies](https://cunyba.cuny.edu/) program in computational physics. Then, I finished my master's at the [CUNY Graduate Center's Astrophysics program](https://www.gc.cuny.edu/astrophysics). 

My academic background is in astrophysics, but I'm generally interested in computational problems as a whole. I've done work with stellar surface mapping, brown-dwarf atmospheres, stellar spectroscopy, galactic archaeology, and numerical simulations. I am also interested in problems in condensed matter, soft matter, and biophysics.

---

## Research Interests

A lot of the problems I've worked on have the same basic structure.

We observe something:

- a light curve,
- a spectrum,
- a spatial distribution,
- a set of chemical abundances,
- or some other incomplete measurement.

But the observable is usually not the physical quantity we ultimately care about.

Instead, there is some hidden system that produced it.

```text
Physical system
      ↓
Physical model
      ↓
Observable data
```

The forward problem asks:

**If I know the physical system, what should I observe?**

The inverse problem asks:

**If I know what I observed, what can I infer about the physical system?**

The second question is usually much harder.

Real measurements contain noise. Multiple physical configurations can produce similar observations. Some information may never have been encoded in the data in the first place.

For me, that intersection of physics, mathematics, statistics, and computation is where things become especially cool.

---

## Mapping a Star You Can't Resolve

My master's thesis research provides a particularly visual example.

For almost every star, we cannot directly resolve its surface well enough to see individual starspots.

Instead, one of the easiest things we can measure is a light curve, which is simply a star’s brightness over time.

As the star rotates, darker regions move into and out of view and change the observed brightness.

So instead of directly observing a surface map, we see a one-dimensional time series:

```text
brightness
   │
   │      ╭─╮
   │  ╭───╯ ╰──╮
   │──╯        ╰──
   └──────────────── time
```

The challenge is to work backward from that light curve toward a possible two-dimensional surface structure.

That is an inverse problem.

---

## Spherical Harmonics

One mathematical tool that is useful for this is the  **spherical-harmonic basis**. One way to think of spherical harmonics is as sine waves wrapped around a sphere.

Just as Fourier modes can be combined to describe increasingly complicated periodic signals, spherical harmonics can be combined to describe increasingly complicated patterns across a sphere.

The animation below (made with manim) shows several individual real spherical-harmonic modes.

<div style="max-width: 850px; margin: 2rem auto;">
  <video
    autoplay
    muted
    loop
    playsinline
    controls
    style="
      display: block;
      width: 100%;
      border-radius: 0.8rem;
    "
  >
    <source
      src="/media/spherical-harmonics.mp4"
      type="video/mp4"
    >
    Your browser does not support embedded video.
  </video>
</div>

<p style="
  max-width: 700px;
  margin: -1rem auto 2rem;
  text-align: center;
  font-size: 0.85rem;
  opacity: 0.7;
">
  Individual real spherical-harmonic modes. Increasing the degree
  allows progressively finer angular structure.
</p>

The lobed representation is useful for visualizing the mathematics, but it is important to distinguish that from how I use the basis for surface mapping.

The star itself is not being physically deformed.

Instead, the spherical harmonics describe how a quantity such as **brightness varies across the surface of a fixed sphere**.

See this in action by changing the degree \(\ell\) and order \(m\) below.

{{< spherical-harmonics >}}

Higher values of \(\ell\) allow progressively smaller-scale angular structure to be represented. A complete surface map can be constructed from a weighted combination of many such basis functions.

The interesting part is then determining which combinations of those modes are actually supported by the observed light curve.

---

## Different Systems, Similar Computational Problems

One of the things I have come to appreciate is how often the same computational ideas appear in very different areas of physics.

### Stellar Surface Mapping

For my M.S. research, I worked on inferring starspot distributions from rotational light curves.

The problem combined time-series analysis, forward modeling, spherical representations, statistical inference, and the degeneracies inherent to reconstructing a surface from unresolved observations.

[Explore the project →](/research/starspots/)

### Brown Dwarfs and Giant Exoplanets

Before that, I studied rotational variability in brown dwarfs and directly imaged giant exoplanets.

Their atmospheres can contain evolving cloud structures that rotate into and out of view, producing brightness variations that again encode information about an unresolved surface.

This was what first introduced me to surface mapping as an inverse problem.

[Explore the project →](/research/brown-dwarf-atmospheres/)

### Galactic Archaeology

I have also worked on the chemodynamical characterization of the Jhelum stellar stream.

There, the inputs were stellar chemistry, spectroscopy, velocities, and phase-space information rather than light curves, but the basic inference problem was familiar: use incomplete measurements to recover information about the history and membership of a larger physical system.

[Explore the project →](/research/jhelum/)

### Stellar Spectroscopy

Earlier work with stellar spectra introduced me to extracting physical parameters from indirect measurements.

Spectra contain an enormous amount of information, but converting absorption features into temperatures, chemical abundances, velocities, or other physical quantities requires a model connecting the observation to the underlying star.

[Explore the project →](/research/stellar-spectroscopy/)

### Simulations and Spatial Structure

I have also worked with numerical simulation data and spatial statistics.

That experience pushed my interests beyond individual inverse problems toward a broader question:

**How does complicated large-scale structure emerge from comparatively simple underlying physical rules?**

---

## What I'm Interested in Now

I’m currently interested in extending the computational approaches I’ve used in astrophysics toward problems in condensed matter, soft matter, and biophysics.

I’m especially drawn to problems involving emergent behavior, statistical inference, nonequilibrium systems, and the relationship between microscopic interactions and macroscopic structure.

---

## Outside of Physics

Outside of physics, I enjoy things like basketball (<span style="color:#F58426">Go New York Go New York Go!</span>.)

I also enjoy competitive Pokémon, particularly the official VGC formats. While I’m not the best player, I do enjoy looking at trends and trying to predict what will pop off next. I think the sheer number of choices is what makes the game interesting.

I also enjoy finding ways to turn data into something visual and interactive.

The network below uses a periodically updated snapshot of Pokémon Champions data.

{{< vgc-meta >}}

Each node represents one of the highest-ranked Pokémon in the current dataset.

Node size reflects overall ranking, while connections represent **teammate affinity**. A stronger connection means that the two Pokémon rank more highly among one another's commonly used teammates.

The visualization is updated periodically rather than querying the source every time somebody loads this page, so it also acts as a small snapshot of how the competitive metagame changes over time.

---

## Explore My Work

If you are primarily here for my academic work, you can find it throughout the rest of the site:

- [Research](/research/)
- [Publications](/publication/)
- [Presentations](/events/)
- [Curriculum Vitae](/uploads/Mohammad_Refat_CV.pdf)