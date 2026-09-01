"""Add the site's shared disclaimer to every Markdown page."""

DISCLAIMER = """
---

<small style="color: #777;">
<em><strong>Disclaimer:</strong> Optical Intelligence is an independent personal hobby website. The articles, Python Code, simulations, and opinions published here are created independently of my employment and professional work; this website is not affiliated with, sponsored by, endorsed by, or operated on behalf of my employer, and nothing published here represents the views and opinions of my employer. The content and Code are provided primarily for educational and experimental purposes, with no guarantee that the information, simulations, or results are accurate, complete, or suitable for any particular purpose; use them at your own discretion.</em>
</small>
""".strip()


def on_page_markdown(markdown, page, **kwargs):
    """Append the disclaimer after each page's authored content."""
    if page.file.src_path == "blog/index.md":
        return markdown

    return f"{markdown.rstrip()}\n\n{DISCLAIMER}\n"
