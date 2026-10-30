# Mohammad Alvi Refat — Portfolio

This repository contains the source for my academic and research portfolio:

**[mohammadrefat23.github.io](https://mohammadrefat23.github.io/)**

My research interests are in computational physics and numerical methods: molecular dynamics and Monte Carlo simulation, inverse problems, and Bayesian inference (MCMC) for fitting and testing physical models against data, with applications in biological and materials physics. My research so far has been in astrophysics. The site brings together my background, research, publications, presentations, CV, and code.

## Site sections

- **Bio** — research interests, training, current research, and teaching.
- **Research** — research projects, each with my contributions, methods, results, and outputs.
- **Projects** — code, interactive tools, a course project, and a data side project.
- **Publications** — thesis and peer-reviewed work.
- **Presentations** — talks and posters.
- **CV & Résumé** — current academic CV and industry résumé.

## Run locally

Install [Hugo Extended](https://gohugo.io/installation/) and [pnpm](https://pnpm.io/installation/), then run:

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Hugo serves a local preview. To build the site:

```sh
pnpm build
```

## Deployment

GitHub Actions builds and deploys the site to GitHub Pages when changes are pushed to the `main` branch. Each build checks out the `main` branches of `MohammadRefat23/cv` and `MohammadRefat23/resume`, compiles both documents, includes them in the site, then generates a Pagefind search index. After changing either source repository, run the website repository's `Build CV, résumé, and Hugo Site` workflow to publish the updated documents. If either source repository is private, set the website repository secret `SOURCE_REPO_TOKEN` to a fine-grained token with Contents: read access to both source repositories.

## VGC history

The `Update VGC usage data from Smogon` workflow imports published Champions VGC best-of-three reports at the 1630 rating cutoff. It archives full rank, weighted usage, raw usage, battle totals, and average team weight by month and regulation under `static/data/vgc-history/`. Adjacent reports in the same regulation are compared in `monthly_comparison.csv`; the VGC project page shows the latest pair's top-15 overlap, shared-roster Spearman rank correlation, and largest usage shifts, and animates monthly top-15 usage.

The updater preserves archived Smogon snapshots, validates source rows before writing, and does not compare different regulations. The `analysis/` directory contains the August–September SQL comparison, source database, and summary script. Run the offline parser and comparison tests with `python -m unittest discover -s tests`. GitHub Actions updates the published data monthly and can also be started manually; when data changes, it dispatches the site deployment workflow. Source attribution appears on the project page. The reports describe Pokémon Showdown simulator ladder usage, not official Pokémon Champions in-game usage.

## Built with

- [Hugo](https://gohugo.io/)
- [Hugo Blox](https://hugoblox.com/)
- GitHub Pages and GitHub Actions
