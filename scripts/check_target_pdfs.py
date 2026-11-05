#!/usr/bin/env python3
"""Bind each independent PDF to its own inputs and staged source files."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from book_catalog import group, references, tex_inputs, uncomment, volumes

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "target/.build-manifest.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def bib_entries(text):
    result = {}
    for match in re.finditer(r"@([A-Za-z]+)\s*\{", text):
        body, end = group(text, match.end() - 1)
        kind = match[1].lower()
        if kind in {"comment", "preamble"}:
            continue
        key = body.split(",", 1)[0].strip() if kind != "string" else "@string:" + body
        if key in result:
            raise ValueError(f"重复文献键：{key}")
        result[key] = text[match.start():end]
        aliases = re.search(r"\bids\s*=\s*\{([^{}]+)\}", body)
        if aliases:
            for alias in aliases[1].split(","):
                result[alias.strip()] = result[key]
    return result


def inputs():
    """Hash used bibliography/index records; unrelated volumes stay unchanged."""
    inventory = references(ROOT)
    bibliography = bib_entries((ROOT / "tex/references.bib").read_text())
    mappings = {}
    for path in sorted((ROOT / "tex/index-terms").glob("*.tex")):
        for line in path.read_text().splitlines():
            match = re.match(r"\\DeclareBookIndexTerm(?:Alias)?\{([^{}]+)\}", line)
            if match:
                mappings[match[1]] = line
    cache = {}

    def hash_file(name):
        if name not in cache:
            cache[name] = digest((ROOT / name).read_bytes())
        return cache[name]

    common = ["build.sh", ".latexmkrc", ".gitattributes",
              "scripts/check_target_pdfs.py", "scripts/book_catalog.py", "scripts/publish_volume.py"]
    if (ROOT / "tex/planned-references.json").is_file():
        common.append("tex/planned-references.json")
    # Document-class and xindy inputs are loaded by LaTeX/tool lookup rather
    # than literal \input, so include their pinned repository versions.
    common += [p.relative_to(ROOT).as_posix() for p in (ROOT / "tex/styles").glob("*")
               if p.is_file() and p.suffix in {".cls", ".def", ".sty", ".xdy"}]
    common += [p.relative_to(ROOT).as_posix() for p in (ROOT / "fonts").rglob("*")
               if p.is_file() and p.name != ".DS_Store"]
    result = {}
    for volume in volumes(ROOT):
        sources = tex_inputs(ROOT, volume["entry"])
        sources.update(tex_inputs(ROOT, volume["content"]))
        # The index dictionary is shared, but only the records used here matter.
        sources = {p: t for p, t in sources.items()
                   if p != "tex/index-terms.tex" and not p.startswith("tex/index-terms/")}
        text = "\n".join(sources.values())
        names = set(common) | set(sources)
        for name in re.findall(r"\{(figures/[^{}\n]+)\}", text):
            path = ROOT / name
            if not path.is_file() and not path.suffix:
                path = path.with_suffix(".tex")
                name = path.relative_to(ROOT).as_posix()
            if not path.is_file():
                raise ValueError(f"缺少图像资源：{name}")
            names.add(name)
            for source in path.parent.rglob("*"):
                if source.is_file() and source.suffix in {".py", ".tex", ".json", ".csv", ".md"}:
                    if "__pycache__" not in source.parts:
                        names.add(source.relative_to(ROOT).as_posix())
        # Follow generator/data paths recorded beside used graphics. Do not
        # make an unused cross-volume generator a dependency of every volume.
        for name in list(names):
            if not name.startswith("figures/") or not name.endswith(".json"):
                continue
            metadata = (ROOT / name).read_text()
            for dependency in re.findall(r'"((?:figures|fonts|tex/styles)/[^"\n]+)"', metadata):
                path = ROOT / dependency
                if path.is_file():
                    names.add(dependency)
        records = {name: hash_file(name) for name in sorted(names)}
        records["@volume"] = digest(json.dumps(volume, sort_keys=True).encode())
        terms = set(re.findall(r"\\term(?:\[[^\]]*\])?\{([^{}]+)\}", text))
        terms.update(re.findall(r"\\termalias\{([^{}]+)\}", text))
        records["@index"] = digest("\n".join(mappings.get(t, "") for t in sorted(terms)).encode())
        keys = set()
        for call in re.findall(
                r"\\(?:[A-Za-z]*cite[A-Za-z]*)(?:\*?)(?:\[[^\]]*\])*\s*\{([^{}]+)\}", text):
            keys.update(k.strip() for k in call.split(",") if "#" not in k and "\\" not in k)
        if "*" in keys:
            keys = set(bibliography)
        keys.update(k for k in bibliography if k.startswith("@string:"))
        missing = keys - set(bibliography)
        if missing:
            raise ValueError(f"{volume['slug']} 缺少文献：{sorted(missing)}")
        records["@bibliography"] = digest("\n".join(bibliography[k] for k in sorted(keys)).encode())
        calls = set(re.findall(
            r"\\(?:Book\w*Ref|BookReference|ref|eqref|autoref|nameref)\*?\s*\{([^{}]+)\}", text))
        calls = {k for k in calls if "#" not in k and "\\" not in k}
        missing = calls - set(inventory)
        if missing:
            raise ValueError(f"{volume['slug']} 缺少标签：{sorted(missing)}")
        records["@references"] = digest(json.dumps(
            {k: inventory[k] for k in sorted(calls)}, ensure_ascii=False, sort_keys=True).encode())
        result[volume["slug"]] = records
    return result


def source_files():
    names = ["build.sh", ".latexmkrc", ".gitattributes",
             "scripts/check_target_pdfs.py", "scripts/book_catalog.py", "scripts/publish_volume.py"]
    for directory in ["tex", "figures", "fonts"]:
        names.extend(p.relative_to(ROOT).as_posix() for p in (ROOT / directory).rglob("*")
                     if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts)
    return set(names)


def check_index():
    current = source_files()
    staged = set(git("ls-files", "-z", "--", "tex", "figures", "fonts",
                     "build.sh", ".latexmkrc", ".gitattributes",
                     "scripts/check_target_pdfs.py", "scripts/book_catalog.py",
                     "scripts/publish_volume.py").decode().split("\0"))
    staged.discard("")
    staged = {p for p in staged if Path(p).name != ".DS_Store" and "__pycache__" not in Path(p).parts}
    if staged != current:
        raise ValueError("正文或构建输入的暂存文件列表与工作目录不同；请暂存对应新增和删除。")
    for name in sorted(current):
        if not staged_matches(name, (ROOT / name).read_bytes()):
            raise ValueError(f"正文或构建输入存在未暂存修改：{name}")


def pdf_record(volume):
    path = ROOT / "target" / volume["pdf"]
    data = path.read_bytes()
    if not data.startswith(b"%PDF-") or not data.rstrip().endswith(b"%%EOF"):
        raise ValueError(f"PDF 损坏或尚未构建完成：{path.name}")
    import pymupdf
    with pymupdf.open(path) as document:
        pages = len(document)
    return {"file": volume["pdf"], "sha256": digest(data), "pages": pages}


def staged_matches(name, data):
    staged = git("show", ":" + name)
    if staged == data:
        return True
    pointer = re.fullmatch(
        rb"version https://git-lfs.github.com/spec/v1\noid sha256:([0-9a-f]{64})\nsize ([0-9]+)\n", staged)
    if not pointer:
        return False
    attribute = git("check-attr", "--cached", "filter", "--", name).decode().strip()
    return (attribute == name + ": filter: lfs"
            and pointer[1].decode() == digest(data) and int(pointer[2]) == len(data))


def manifest():
    path = ROOT / MANIFEST
    if path.exists():
        value = json.loads(path.read_text())
        if value.get("version") == 2:
            return value
    return {"version": 2, "volumes": {}}


def affected(current, state):
    result = []
    for volume in volumes(ROOT):
        previous = state["volumes"].get(volume["slug"], {})
        if previous.get("inputs") != current[volume["slug"]]:
            result.append(volume["slug"])
            continue
        try:
            if previous.get("pdf") != pdf_record(volume):
                result.append(volume["slug"])
        except (OSError, ValueError):
            result.append(volume["slug"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["snapshot", "record", "check", "check-index", "affected"])
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--volume", action="append")
    parser.add_argument("--staged", action="store_true")
    args = parser.parse_args()
    if args.command == "check-index":
        check_index()
        return
    current = inputs()
    state = manifest()
    if args.command == "snapshot":
        print(json.dumps(current, sort_keys=True))
    elif args.command == "affected":
        print("\n".join(affected(current, state)))
    elif args.command == "record":
        before = json.loads(args.snapshot.read_text()) if args.snapshot else {}
        selected = args.volume or list(current)
        for volume in volumes(ROOT):
            slug = volume["slug"]
            if slug not in selected:
                continue
            if before.get(slug) != current[slug]:
                raise ValueError(f"构建过程中{slug}的输入发生变化，请重新编译该卷。")
            state["volumes"][slug] = {"inputs": current[slug], "pdf": pdf_record(volume)}
        state["volumes"] = {s: r for s, r in state["volumes"].items() if s in current}
        temp = ROOT / (MANIFEST + ".tmp")
        temp.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        temp.replace(ROOT / MANIFEST)
    else:
        expected = {v["pdf"] for v in volumes(ROOT)}
        actual = {p.name for p in (ROOT / "target").glob("*.pdf")}
        if actual != expected:
            raise ValueError(f"target/ 的 {len(expected)} 卷 PDF 不完整或存在旧产物；请运行 ./build.sh all。")
        stale = affected(current, state)
        if stale:
            raise ValueError(f"以下卷的构建输入已过期或 PDF 与构建记录不同：{', '.join(stale)}；运行 ./build.sh build。")
        if args.staged:
            check_index()
            for name in [MANIFEST] + ["target/" + n for n in sorted(expected)]:
                if not staged_matches(name, (ROOT / name).read_bytes()):
                    raise ValueError(f"成品尚未暂存或暂存版本已过期：{name}")
        print(f"成品检查通过：{len(expected)} 卷 PDF 与各卷当前输入一致。")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"成品检查失败：{error}", file=sys.stderr)
        sys.exit(1)
