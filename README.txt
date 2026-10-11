VGC site build fix

Extract at the repository root, preserving folders:
- content/about/index.md (replace)
- layouts/shortcodes/site-video.html (add)

Delete layouts/shortcodes/video.html if it exists. The About page uses the unique site-video shortcode to avoid Hugo Blox's built-in video shortcode, which expects a page-bundle resource.

Commit and push, then rerun the GitHub Pages workflow.
