# SPDX-FileCopyrightText: 2026 Zw-awa
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path


STYLE_CSS = """\
:root {
  --bg: #f5f0df;
  --panel: #f8f4e8;
  --ink: #1f1b16;
  --muted: #665f55;
  --rule: #c9bea8;
  --accent: #3a342a;
  --shadow: rgba(31, 27, 22, 0.08);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: "Courier New", Courier, monospace;
  line-height: 1.65;
}

.page {
  max-width: 980px;
  margin: 0 auto;
  padding: 28px 20px 56px;
}

.hero,
.manual section,
.footer {
  background: var(--panel);
  border: 1px solid var(--rule);
  box-shadow: 0 6px 18px var(--shadow);
}

.hero {
  padding: 22px 24px;
  margin-bottom: 18px;
}

.hero__line {
  font-size: 0.92rem;
  color: var(--muted);
  letter-spacing: 0.08em;
}

.hero h1 {
  margin: 10px 0 8px;
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  line-height: 1.15;
}

.hero__summary {
  margin: 0;
  font-size: 1rem;
}

.hero__meta {
  margin-top: 14px;
  color: var(--muted);
}

.manual {
  display: grid;
  gap: 14px;
}

.manual section {
  padding: 18px 24px;
}

.manual h2 {
  margin: 0 0 12px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--rule);
  font-size: 1rem;
  letter-spacing: 0.08em;
}

.manual h3 {
  margin: 18px 0 8px;
  font-size: 1rem;
}

.manual p,
.manual ul,
.manual ol,
.manual pre,
.manual blockquote {
  margin: 0 0 12px;
}

.manual ul,
.manual ol {
  padding-left: 24px;
}

.manual code {
  background: #efe8d4;
  padding: 0 4px;
}

.manual pre {
  overflow-x: auto;
  padding: 12px 14px;
  background: #efe8d4;
  border: 1px solid var(--rule);
}

.manual pre code {
  background: transparent;
  padding: 0;
}

.manual a,
.hero a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px dotted var(--accent);
}

.manual a:hover,
.hero a:hover {
  border-bottom-style: solid;
}

.lang-switch,
.page-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 16px;
}

.muted {
  color: var(--muted);
}

.footer {
  margin-top: 14px;
  padding: 14px 24px;
  text-align: center;
  color: var(--muted);
}

@media (max-width: 640px) {
  .page {
    padding: 18px 12px 32px;
  }

  .hero,
  .manual section,
  .footer {
    padding-left: 16px;
    padding-right: 16px;
  }
}
"""


@dataclass(frozen=True)
class DocPage:
    source: Path
    slug: str
    lang: str
    output_name: str
    title: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a manual-style Pages site from docs markdown.")
    parser.add_argument("--source", default="docs", help="Source docs directory")
    parser.add_argument("--output", default="_site", help="Output directory")
    return parser.parse_args()


def detect_lang(path: Path) -> tuple[str, str]:
    name = path.name
    if name.endswith(".zh-CN.md"):
        return name[: -len(".zh-CN.md")], "zh-CN"
    if name.endswith(".zh-TW.md"):
        return name[: -len(".zh-TW.md")], "zh-TW"
    return name[: -len(".md")], "en"


def output_name_for(stem: str, lang: str) -> str:
    if stem == "README":
        if lang == "en":
            return "index.html"
        return f"index.{lang}.html"
    if lang == "en":
        return f"{stem}.html"
    return f"{stem}.{lang}.html"


def find_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def collect_pages(source_dir: Path) -> list[DocPage]:
    pages: list[DocPage] = []
    for path in sorted(source_dir.glob("*.md")):
        if path.name == ".gitkeep":
            continue
        stem, lang = detect_lang(path)
        text = path.read_text(encoding="utf-8")
        title = find_title(text, stem)
        pages.append(
            DocPage(
                source=path,
                slug=stem,
                lang=lang,
                output_name=output_name_for(stem, lang),
                title=title,
            )
        )
    return pages


def md_link_target_to_html(target: str) -> str:
    if not target.endswith(".md"):
        return target
    name = Path(target).name
    if name == "README.md":
        return "./index.html"
    if name == "README.zh-CN.md":
        return "./index.zh-CN.html"
    if name == "README.zh-TW.md":
        return "./index.zh-TW.html"
    if name.endswith(".zh-CN.md"):
        return f"./{name[:-3]}.html"
    if name.endswith(".zh-TW.md"):
        return f"./{name[:-3]}.html"
    return f"./{name[:-3]}.html"


def render_inline(text: str) -> str:
    escaped = html.escape(text)

    escaped = re.sub(
        r"`([^`]+)`",
        lambda m: f"<code>{html.escape(m.group(1))}</code>",
        escaped,
    )

    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(md_link_target_to_html(m.group(2)))}">{m.group(1)}</a>',
        escaped,
    )
    return escaped


def flush_paragraph(paragraph_lines: list[str], parts: list[str]) -> None:
    if paragraph_lines:
        text = " ".join(line.strip() for line in paragraph_lines)
        parts.append(f"<p>{render_inline(text)}</p>")
        paragraph_lines.clear()


def flush_list(list_type: str | None, items: list[str], parts: list[str]) -> None:
    if not list_type or not items:
        return
    tag = "ul" if list_type == "ul" else "ol"
    rendered = "".join(f"<li>{render_inline(item)}</li>" for item in items)
    parts.append(f"<{tag}>{rendered}</{tag}>")
    items.clear()


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    parts: list[str] = []
    paragraph_lines: list[str] = []
    list_type: str | None = None
    list_items: list[str] = []
    in_code = False
    code_lines: list[str] = []
    section_open = False

    for raw_line in lines:
        line = raw_line.rstrip()

        if line.startswith("```"):
            flush_paragraph(paragraph_lines, parts)
            flush_list(list_type, list_items, parts)
            list_type = None
            if in_code:
                code = html.escape("\n".join(code_lines))
                parts.append(f"<pre><code>{code}</code></pre>")
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(raw_line)
            continue

        if not line.strip():
            flush_paragraph(paragraph_lines, parts)
            flush_list(list_type, list_items, parts)
            list_type = None
            continue

        if line.startswith("# "):
            flush_paragraph(paragraph_lines, parts)
            flush_list(list_type, list_items, parts)
            list_type = None
            continue

        if line.startswith("## "):
            flush_paragraph(paragraph_lines, parts)
            flush_list(list_type, list_items, parts)
            list_type = None
            if section_open:
                parts.append("</section>")
            parts.append(f"<section><h2>{render_inline(line[3:].strip())}</h2>")
            section_open = True
            continue

        if line.startswith("### "):
            flush_paragraph(paragraph_lines, parts)
            flush_list(list_type, list_items, parts)
            list_type = None
            parts.append(f"<h3>{render_inline(line[4:].strip())}</h3>")
            continue

        bullet_match = re.match(r"^- (.+)$", line)
        ordered_match = re.match(r"^\d+\. (.+)$", line)
        if bullet_match:
            flush_paragraph(paragraph_lines, parts)
            if list_type not in (None, "ul"):
                flush_list(list_type, list_items, parts)
                list_type = None
            list_type = "ul"
            list_items.append(bullet_match.group(1))
            continue
        if ordered_match:
            flush_paragraph(paragraph_lines, parts)
            if list_type not in (None, "ol"):
                flush_list(list_type, list_items, parts)
                list_type = None
            list_type = "ol"
            list_items.append(ordered_match.group(1))
            continue

        paragraph_lines.append(line)

    flush_paragraph(paragraph_lines, parts)
    flush_list(list_type, list_items, parts)

    if section_open:
        parts.append("</section>")

    return "\n".join(parts)


def page_nav(pages: list[DocPage], current: DocPage) -> str:
    current_lang_pages = [page for page in pages if page.lang == current.lang]
    links = []
    for page in current_lang_pages:
        label = page.title
        href = page.output_name
        links.append(f'<a href="./{href}">{html.escape(label)}</a>')
    return " ".join(links)


def language_switch(pages: list[DocPage], current: DocPage) -> str:
    variants = {page.lang: page for page in pages if page.slug == current.slug}
    labels = [("en", "English"), ("zh-CN", "简体中文"), ("zh-TW", "繁體中文")]
    links = []
    for lang, label in labels:
        if lang in variants:
            href = variants[lang].output_name
            links.append(f'<a href="./{href}">{label}</a>')
    return " | ".join(links)


def hero_summary(page: DocPage) -> str:
    if page.slug == "README":
        if page.lang == "zh-CN":
            return "ManipPilot 使用手册入口。"
        if page.lang == "zh-TW":
            return "ManipPilot 使用手冊入口。"
        return "ManipPilot manual entry point."
    if page.lang == "zh-CN":
        return "由 docs 目录自动生成的手册页。"
    if page.lang == "zh-TW":
        return "由 docs 目錄自動產生的手冊頁。"
    return "Manual page generated from the docs directory."


def render_page(page: DocPage, pages: list[DocPage], body_html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{html.escape(page.lang)}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(page.title)} - ManipPilot Manual</title>
    <meta
      name="description"
      content="ManipPilot manual page generated from docs."
    />
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <div class="page">
      <header class="hero">
        <div class="hero__line">MANIPPILOT(7)</div>
        <h1>{html.escape(page.title)}</h1>
        <p class="hero__summary">{html.escape(hero_summary(page))}</p>
        <div class="hero__meta">
          <div class="lang-switch">{language_switch(pages, page)}</div>
        </div>
      </header>

      <main class="manual">
        <section>
          <h2>MANUAL INDEX</h2>
          <nav class="page-nav">{page_nav(pages, page)}</nav>
        </section>
        {body_html}
      </main>

      <footer class="footer">
        <p>Generated from docs/ for GitHub Pages</p>
      </footer>
    </div>
  </body>
</html>
"""


def main() -> None:
    args = parse_args()
    source_dir = Path(args.source)
    output_dir = Path(args.output)

    pages = collect_pages(source_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "styles.css").write_text(STYLE_CSS, encoding="utf-8")

    for page in pages:
        text = page.source.read_text(encoding="utf-8")
        body_html = markdown_to_html(text)
        rendered = render_page(page, pages, body_html)
        (output_dir / page.output_name).write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
