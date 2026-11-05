#!/usr/bin/env python3
"""Describe independent volumes and their active TeX inputs."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = "tex/volumes.json"


def volumes(root=ROOT):
    result = json.loads((root / CATALOG).read_text())["volumes"]
    for item in result:
        item.setdefault("content", f"tex/{item['slug']}/volume.tex")
        item.setdefault("entry", f"tex/{item['slug']}/main.tex")
        item.setdefault("pdf", f"vol{item['number']}-{item['slug'][3:]}.pdf")
    return result


def uncomment(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def group(text, start):
    if text[start:start + 1] != "{":
        raise ValueError(f"Expected group at {start}")
    depth, pos = 1, start + 1
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
            if not depth:
                return text[start + 1:pos], pos + 1
        pos += 1
    raise ValueError("Unclosed TeX group")


def tex_inputs(root, entry):
    result = {}

    def walk(name, stack=()):
        path = Path(name)
        if not path.suffix:
            path = path.with_suffix(".tex")
        key = path.as_posix()
        if key in stack:
            raise ValueError(f"Recursive input: {key}")
        if key in result:
            return
        absolute = root / path
        if not absolute.is_file():
            raise FileNotFoundError(key)
        text = uncomment(absolute.read_text())
        result[key] = text
        for value in re.findall(r"\\input\s*\{([^{}]+)\}", text):
            if "\\" not in value:
                walk(value, (*stack, key))
    walk(entry)
    return result


def plain_title(title):
    title = re.sub(r"\\(?:term|textbf|emph|textit|mathrm)\{([^{}]*)\}", r"\1", title)
    return re.sub(r"\s+", " ", title).strip()


def references(root=ROOT):
    """Label locations come from source headings, never another PDF's cache."""
    result = {}
    for volume in volumes(root):
        chapter, part = 0, 0
        levels = [0, 0, 0]
        chapter_title, section_title = "", ""
        section_number = ""
        def ordered_inputs(path, stack=()):
            source = Path(path)
            if not source.suffix:
                source = source.with_suffix(".tex")
            name = source.as_posix()
            if name in stack:
                raise ValueError(f"Recursive input: {name}")
            text = uncomment((root / name).read_text())
            cursor = 0
            for match in re.finditer(r"\\input\s*\{([^{}]+)\}", text):
                yield name, text[cursor:match.start()]
                if "\\" not in match[1]:
                    yield from ordered_inputs(match[1], (*stack, name))
                cursor = match.end()
            yield name, text[cursor:]

        for path, text in ordered_inputs(volume["content"]):
            pattern = r"\\(chapter|section|subsection|subsubsection|bookpart|label|functionalinlinefigurecaption|functionalinlinetablecaption)\s*\{"
            for match in re.finditer(pattern, text):
                command = match[1]
                title, end = group(text, match.end() - 1)
                title = plain_title(title)
                if command == "chapter":
                    chapter += 1
                    chapter_title = title
                    levels = [0, 0, 0]
                    section_title, section_number = "", ""
                elif command in {"section", "subsection", "subsubsection"}:
                    level = ["section", "subsection", "subsubsection"].index(command)
                    levels[level] += 1
                    for i in range(level + 1, 3):
                        levels[i] = 0
                    section_number = ".".join(map(str, [chapter] + levels[:level + 1]))
                    section_title = title
                elif command == "bookpart":
                    part += 1
                else:
                    if "#" in title:
                        continue
                    location = f"第{chapter}章“{chapter_title}”" if chapter else ""
                    if section_number:
                        location += f"第{section_number}节“{section_title}”"
                    if title.startswith("vol:"):
                        location = ""
                    elif title.startswith("part:"):
                        location = f"第{part}部分"
                    elif title.startswith("chap:"):
                        location = f"第{chapter}章“{chapter_title}”"
                    record = {"volume": volume["number"], "title": volume["title"],
                              "slug": volume["slug"], "location": location, "source": path}
                    if title in result:
                        raise ValueError(f"Duplicate label: {title}")
                    result[title] = record
            for label in re.findall(r"label\s*=\s*\{(code:[^{}]+)\}", text):
                result[label] = {"volume": volume["number"], "title": volume["title"],
                                 "slug": volume["slug"], "source": path,
                                 "location": f"第{chapter}章“{chapter_title}”"}
    return result


def reference_calls(text):
    pattern = r"\\(?:Book\w*Ref|BookReference|ref|eqref|autoref|nameref)\*?\s*\{([^{}]+)\}"
    return set(re.findall(pattern, uncomment(text)))


def write_references(slug, root=ROOT):
    volume = next(v for v in volumes(root) if v["slug"] == slug)
    used = set()
    for text in tex_inputs(root, volume["content"]).values():
        used.update(reference_calls(text))
    inventory = references(root)
    missing = used - set(inventory)
    if missing:
        raise ValueError(f"Undefined references in {slug}: {sorted(missing)}")
    records = {label: inventory[label] for label in sorted(used)}
    destination = root / "build" / f"{slug}-references.tex"
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(
        f"\\BookDeclareReference{{{label}}}{{{item['volume']}}}"
        "{卷\\zhnumber{%s}%s}" % (item["volume"], item["location"] or "《" + item["title"] + "》")
        for label, item in records.items()) + "\n"
    if not destination.exists() or destination.read_text() != text:
        destination.write_text(text)
    return records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["slugs", "references"])
    parser.add_argument("slug", nargs="?")
    args = parser.parse_args()
    if args.command == "slugs":
        for volume in volumes():
            print(volume["slug"])
    else:
        write_references(args.slug)
