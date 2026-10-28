---
title: "Water-Responsive Metal–Peptide Frameworks: Literature Review"
summary: "A literature review of how peptide side groups change water uptake and crystal motion in zinc–peptide frameworks, and of the MD and GCMC methods used to model them."
date: 2026-10-28
hide_date: true
featured: false
weight: 60
authors:
  - admin
card_label: "Literature Review in Progress"
tags:
  - "Materials Physics"
  - "Molecular Dynamics"
  - "Monte Carlo Methods"
  - "Literature Review"
---

## Status

This is a literature review at an early stage, carried out in weekly meetings with a graduate student in Dr. Qiang Zhu's group at the University of North Carolina at Charlotte. **I have not run simulations or produced results for this project yet.** The notes below summarize what I have read and the modeling path I am studying. Each claim comes from the cited paper; anything beyond that is marked as a working idea.

## The Question

Can a small change in a peptide change how a metal–peptide crystal takes up water and moves as humidity changes?

The starting point is a 2025 comparison of two zinc–peptide frameworks, Zn–Gly–Thr (Zn–GT) and Zn–Gly–Ser (Zn–GS), which differ by one methyl group (Yuan et al., 2025).

| | Zn–GT | Zn–GS |
|---|---|---|
| Water response | Gradual | Sharp uptake at 50–60% RH; release at 20–30% RH |
| Water uptake | About 11.9% gain | Up to about 19.5% gain |
| Crystal volume on drying | Falls about 1.7% | Falls about 22.3% |
| Coated-strip bending | Curvature about 0.6 mm⁻¹ | Curvature about 1.0 mm⁻¹ |

These are the values reported by Yuan et al. They show different response patterns in two crystals; they do not yet give a general design rule.

## Measured Versus Explained

The experiments measured water mass as humidity changes, crystal structure and size, infrared signals, and the bending of a crystal-coated plastic strip. The detailed order of water-site events is an interpretation supported partly by simulation. A plausible chain is: side-group change, then water and peptide packing, then crystal change as water leaves, then film bending. Each link needs its own evidence, and a correlation between water loss and bending does not prove every step.

## What Else I Read

- **Earlier peptide frameworks:** short peptides can link metal ions into porous crystals, and side groups and cooperative folding can affect whether pores close when guests leave (Mantion et al., 2008; Martí-Gastaldo et al., 2012, 2014; Katsoulidis et al., 2014).
- **Water-responsive MOFs:** MIL-53(Cr), CAU-10, X-dia-2-Cd and a flexible zinc MOF show water-driven structural changes. They are useful comparisons, not proof that peptide frameworks behave the same way.
- **Related peptide materials:** zinc-linked peptide nanofibers respond to humidity but are fibers, not porous crystals (Dey et al., 2024). A carnosine–zinc framework responds to force, not humidity (Chen et al., 2022).

## Methods I Am Studying

The question for each method is what it can answer and which measurement could check it.

**Grand-canonical Monte Carlo (GCMC)** lets the number of water molecules change. Trial insertions and deletions are accepted according to energy and vapor conditions, and averaging over many trials gives an adsorption isotherm. The grand partition function and mean loading are

$$\Xi(\mu,V,T)=\sum_{N}e^{\beta\mu N}Z_N,\qquad \langle N\rangle=\frac{\partial \ln \Xi}{\partial(\beta\mu)}$$

and for an ideal vapor the chemical potential relates to humidity through \(\mu-\mu_{\rm sat}=k_BT\ln(p/p_{\rm sat})\). The insertion and deletion acceptance rules I worked through are the standard textbook forms for random-position moves. They explain detailed balance and are not a claim about any one paper's implementation.

**Molecular dynamics (MD)** follows atoms through time using Newton's second law, advanced with velocity-Verlet,

$$\mathbf r_i(t+\Delta t)=\mathbf r_i(t)+\mathbf v_i(t)\,\Delta t+\frac{\mathbf F_i(t)}{2m_i}(\Delta t)^2,\qquad \mathbf F_i=-\nabla_i U,$$

where the force comes from an interaction model. Trajectories become structural results through radial distribution functions, whose peaks mark preferred contact distances.

**Two papers show how these methods are used:**

- Zhang et al. (2023) built an MD interaction model for water in UiO-66. They fitted framework–water parameters to DFT reference energies with a genetic algorithm, used the MB-pol water model, and found that water first sits at hydroxyl sites (about 67% of water at 10% RH). Their water counts came from the experimental isotherm, so the MD explains where water sits, not total uptake.
- Grenev et al. (2021) used GCMC on rigid, flexible and defective models of CAU-10-H. Framework flexibility and a small number of defects shifted the simulated uptake step, and the best match depended on model assumptions.

Only Said et al. (2022) directly designs metal–peptide networks, so the water simulations above use different MOFs. Their methods suggest questions, and their parameters do not transfer automatically.

## Open Questions

- Which water site empties first, and what directly triggers the sharp transition in Zn–GS?
- How much of the response depends on peptide sequence versus crystal packing and defects?
- Does bending stay stable over many wetting and drying cycles?
- Can a model predict the measured uptake curve and crystal change before synthesis?

## Proposed Path (Not Yet Done)

1. Start from the measured Zn–GT and Zn–GS structures in Yuan et al.
2. Check interaction-model settings against structure and spectra.
3. Use MD for water location and motion, and GCMC for uptake trends.
4. Compare predictions with diffraction, infrared, uptake and bending data.

The immediate task is to choose one measured Zn–GT or Zn–GS result for a future reproduction and list its inputs: the structure, the interaction parameters, and the experimental check. One untested design idea on the list is a more shape-restricted linker such as Gly–Hyp. It is a candidate to investigate, not an established framework.

## Selected References

- Chen, Y. et al. (2022). *J. Am. Chem. Soc.* 144(8), 3468–3476.
- Dey, A. et al. (2024). *Angew. Chem. Int. Ed.* 63(47), e202409391.
- Grenev, I. V. et al. (2021). *Phys. Chem. Chem. Phys.* 23, 21329–21337.
- Martí-Gastaldo, C. et al. (2014). *Nat. Chem.* 6, 343–351.
- Said, M. Y. et al. (2022). *Chem. Mater.* 34(21), 9736–9744.
- Yuan, H. et al. (2025). Discrete actuation of water-responsive crystalline metal–peptide frameworks. *Angew. Chem. Int. Ed.* 64, e202513629.
- Zhang, J., Paesani, F. and Lessio, M. (2023). *J. Mater. Chem. C* 11, 10247–10258.
