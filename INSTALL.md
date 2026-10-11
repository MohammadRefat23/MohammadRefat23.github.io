# Install the VGC analytics update

This bundle is prepared for `MohammadRefat23/MohammadRefat23.github.io`.

1. Extract the zip into the repository root so `.github/`, `analysis/`, `content/`, `layouts/`, `scripts/`, `static/`, `tests/`, and `README.md` merge into the matching paths.
2. Remove the retired source snapshot if it is still in your repository: `static/data/vgc-history/snapshots/Doubles/Current/2026-10-01.json`.
3. From the repository root, run `python3 -m unittest discover -s tests`.
4. Commit and push the files to `main`. The site build workflow deploys the VGC page. The Smogon updater will also backfill the available reports from April 2026 onward, retain monthly snapshots by regulation, and dispatch a new site deployment when it commits updated data.

If GitHub Actions cannot push updated data, open **Settings → Actions → General** and allow the repository workflow token to write repository contents and dispatch workflows. The update workflow requests `contents: write` and `actions: write` in its YAML permissions.

The page will be at `https://mohammadrefat23.github.io/projects/vgc-metagame/`. The first imported comparison is August–September 2026, Regulation M-B. Future comparisons are kept within the same regulation.

The local Hugo executable was unavailable in this workspace, so the Hugo page build itself was not run here. The included importer tests, JavaScript syntax check, SQLite analysis, and static-data consistency checks passed; GitHub Actions will run the full Hugo deployment after the push.
