# Mohammad Alvi Refat — Portfolio

This repository contains the source for my academic and research portfolio:

**[mohammadrefat23.github.io](https://mohammadrefat23.github.io/)**

I am a computational astrophysicist interested in inverse problems, statistical inference, numerical modeling, and complex physical systems. The site brings together my background, research, publications, presentations, CV, and selected projects.

## Site sections

- **Bio** — background, research interests, and selected work.
- **Research** — computational astrophysics research.
- **Projects** — selected research and data projects, including Pokémon VGC metagame analysis.
- **Publications** — thesis and peer-reviewed work.
- **Presentations** — recorded talks and presentations.
- **CV** — current curriculum vitae.

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

GitHub Actions builds and deploys the site to GitHub Pages when changes are pushed to the `main` branch. The workflow checks out the separate `MohammadRefat23/cv` and `MohammadRefat23/resume` repositories, compiles both documents, includes them in the site, then generates a Pagefind search index. A push to either source repository dispatches this deployment workflow.

## Built with

- [Hugo](https://gohugo.io/)
- [Hugo Blox](https://hugoblox.com/)
- GitHub Pages and GitHub Actions
