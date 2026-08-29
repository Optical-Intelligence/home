"""Add the site's shared disclaimer to every Markdown page."""

DISCLAIMER = """
---

<small style="color: #777;">
<em><strong>Disclaimer:</strong> Optical Intelligence is an independent personal hobby project. The articles, Python Code, simulations, models, calculations, and opinions published here are my own and are created independently of my employment and professional work; this website is not affiliated with, sponsored by, endorsed by, or operated on behalf of my employer, and nothing published here represents the views, opinions, policies, or technical positions of my employer. The content and Code are provided primarily for educational and experimental purposes, with no guarantee that the information, calculations, models, simulations, or results are accurate, complete, current, or suitable for any particular purpose; use them at your own discretion and independently verify important results.</em>
</small>
""".strip()


def on_page_markdown(markdown, **kwargs):
    """Append the disclaimer after each page's authored content."""
    return f"{markdown.rstrip()}\n\n{DISCLAIMER}\n"
