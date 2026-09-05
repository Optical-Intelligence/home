"""Add shared post controls and the site's disclaimer during the build."""

from html import escape
import re
from urllib.parse import quote, urljoin

DISCLAIMER = """
---

<small style="color: #777;">
<em><strong>Disclaimer:</strong> Optical Intelligence is an independent personal hobby website. The articles, Python Code, simulations, and opinions published here are created independently of my employment and professional work; this website is not affiliated with, sponsored by, endorsed by, or operated on behalf of my employer, and nothing published here represents the views and opinions of my employer. The content and Code are provided primarily for educational and experimental purposes, with no guarantee that the information, simulations, or results are accurate, complete, or suitable for any particular purpose; use them at your own discretion.</em>
</small>
""".strip()


def share_buttons(page, config, title):
    """Return share controls for an individual blog post."""
    post_url = urljoin(config["site_url"], page.url)
    encoded_url = quote(post_url, safe="")
    encoded_title = quote(title, safe="")
    safe_url = escape(post_url, quote=True)

    return f"""
<div class="share-buttons" aria-label="Share this article">
  <span class="share-buttons__label">Share this article:</span>
  <a href="https://www.facebook.com/sharer/sharer.php?u={encoded_url}" target="_blank" rel="noopener noreferrer">Facebook</a>
  <a href="https://x.com/intent/tweet?url={encoded_url}&amp;text={encoded_title}" target="_blank" rel="noopener noreferrer">X</a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
  <button type="button" class="share-buttons__copy" data-share-url="{safe_url}">Copy link</button>
</div>
""".strip()


def add_share_buttons(markdown, page, config):
    """Place sharing controls below the post title, preserving title detection."""
    title_match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)

    if not title_match:
        return f"{share_buttons(page, config, page.title or '')}\n\n{markdown}"

    title = title_match.group(1)
    buttons = share_buttons(page, config, title)
    return f"{markdown[:title_match.end()]}\n\n{buttons}{markdown[title_match.end():]}"


def on_page_markdown(markdown, page, config, **kwargs):
    """Add sharing controls to posts and append the disclaimer elsewhere."""
    if page.file.src_path == "blog/index.md":
        return markdown

    if page.file.src_path.startswith("blog/posts/"):
        markdown = add_share_buttons(markdown.rstrip(), page, config)
        return f"{markdown}\n\n{DISCLAIMER}\n"

    return f"{markdown.rstrip()}\n\n{DISCLAIMER}\n"
