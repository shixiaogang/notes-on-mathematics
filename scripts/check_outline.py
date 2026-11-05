#!/usr/bin/env python3
"""Read-only structural and local-link checks for the mathematics outlines."""
from __future__ import annotations

import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def markdown_links(text):
    """Ignore code and TeX math, whose brackets can resemble Markdown links."""
    text = re.sub(r"(?ms)^```.*?^```[^\n]*", "", text)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"(?s)\$\$.*?\$\$", "", text)
    text = re.sub(r"(?<!\\)\$[^$\n]*?(?<!\\)\$", "", text)
    return re.findall(r"(?<!!)\[[^\[\]\n]*\]\(([^\s)]+)\)", text)


def check(root=ROOT):
    outline = root / "plans/ten-volume-migration"
    manifest = json.loads(
        (root / "scripts/outline/math-ten-part-files-manifest.json").read_text()
    )
    errors, warnings = [], []
    counts = dict(volumes=len(manifest), parts=0, chapters=0, sections=0, subsections=0)
    expected = {Path("README.md")}
    all_chapters = []

    for volume_number, volume in enumerate(manifest, 1):
        volume_chapters = []
        for part in volume["parts"]:
            counts["parts"] += 1
            relative = Path(part["file"])
            expected.add(relative)
            path = outline / relative
            if not path.is_file():
                errors.append(f"Missing outline: {relative}")
                continue
            text = path.read_text()
            headings = list(re.finditer(r"^(#{2,}) ([\d.]+) (.+)$", text, re.M))
            chapters = [(m[2], m[3]) for m in headings if len(m[1]) == 2]
            wanted = [(c["number"], c["title"]) for c in part["chapters"]]
            if chapters != wanted:
                errors.append(f"Chapter titles/order differ from manifest: {relative}")
            volume_chapters.extend(chapters)
            chapter, section, subsection, last_section = None, 0, 0, None
            for index, heading in enumerate(headings):
                level, number, title = len(heading[1]), heading[2], heading[3]
                end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
                body = text[heading.end():end].strip()
                location = f"{relative}:{number}"
                if not body:
                    errors.append(f"Empty outline item: {location}")
                if level == 2:
                    counts["chapters"] += 1
                    if chapter and last_section != "本章小结":
                        errors.append(f"Missing chapter summary: {relative}:{chapter}")
                    chapter, section, subsection, last_section = number, 0, 0, None
                elif level == 3:
                    counts["sections"] += 1
                    section += 1
                    subsection, last_section = 0, title
                    if number != f"{chapter}.{section}":
                        errors.append(f"Section numbering: {location}")
                elif level == 4:
                    counts["subsections"] += 1
                    subsection += 1
                    if number != f"{chapter}.{section}.{subsection}":
                        errors.append(f"Subsection numbering: {location}")
                else:
                    errors.append(f"Unexpected heading depth: {location}")
                if level >= 3:
                    expanded = relative.name == "03-linear-equations-and-optimization.md" and "\n\n" in body
                    overview = body.split("\n\n", 1)[0] if expanded else body
                    sentences = len(re.findall(r"[。！？]", overview))
                    if not 1 <= sentences <= 2:
                        errors.append(f"Overview requires 1–2 sentences ({sentences}): {location}")
                    if len(overview) > 240:
                        warnings.append(f"Long overview ({len(overview)} characters): {location}")
                    if expanded and not re.search(r"^1\. ", body, re.M):
                        errors.append(f"Missing detailed paragraph steps: {location}")
            if last_section != "本章小结":
                errors.append(f"Missing chapter summary: {relative}:{chapter}")
        if len(volume_chapters) != volume["chapter_count"]:
            errors.append(f"Chapter count differs from manifest: {volume['volume']}")
        wanted_numbers = [f"{volume_number}.{i}" for i in range(1, len(volume_chapters) + 1)]
        if [number for number, title in volume_chapters] != wanted_numbers:
            errors.append(f"Discontinuous chapter numbers: {volume['volume']}")
        all_chapters.extend(volume_chapters)

    actual = {p.relative_to(outline) for p in outline.rglob("*.md")}
    if actual != expected:
        errors.append(f"Unexpected/missing outline files: {sorted(str(p) for p in actual ^ expected)}")
    overview_path = outline / "README.md"
    overview = overview_path.read_text() if overview_path.is_file() else ""
    if re.findall(r"^#### (\d+\.\d+) (.+)$", overview, re.M) != all_chapters:
        errors.append("Global outline chapter titles/order differ from detailed outlines")
    for relative in expected - {Path("README.md")}:
        if f"]({relative.as_posix()})" not in overview:
            errors.append(f"Part missing from global outline: {relative}")

    link_count = 0
    for directory in (root / "outlines", root / "plans"):
        for path in sorted(directory.rglob("*.md")):
            for target in markdown_links(path.read_text()):
                parsed = urlsplit(target.strip("<>"))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                link_count += 1
                if not (path.parent / unquote(parsed.path)).exists():
                    errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")
    return {"counts": counts, "local_links_checked": link_count, "errors": errors, "warnings": warnings}


if __name__ == "__main__":
    report = check()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(bool(report["errors"]))
