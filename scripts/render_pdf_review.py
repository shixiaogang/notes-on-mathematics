#!/usr/bin/env python3
"""Render page contact sheets and optional detail images for human PDF review.

Requires PyMuPDF. Rendered pages are evidence for inspection, not an automatic
visual verdict. Each output directory identifies the exact input PDF hash.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import pymupdf as fitz


def page_selection(value: str | None, count: int) -> list[int]:
    """Return zero-based pages; the CLI always uses physical PDF page numbers."""
    if value is None:
        return list(range(count))
    selected = set()
    for part in value.split(","):
        bounds = [int(item.strip()) for item in part.split("-")]
        if len(bounds) == 1:
            first = last = bounds[0]
        elif len(bounds) == 2:
            first, last = bounds
        else:
            raise ValueError(f"Invalid page range: {part}")
        if not 1 <= first <= last <= count:
            raise ValueError(f"Page range outside 1..{count}: {part}")
        selected.update(range(first - 1, last))
    return sorted(selected)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pages", help="Physical PDF pages, e.g. 1,8-15,23")
    parser.add_argument("--detail", action="store_true",
                        help="Also render each selected page at --dpi")
    parser.add_argument("--only-detail", action="store_true")
    parser.add_argument("--dpi", type=int, default=140)
    args = parser.parse_args()
    if args.dpi < 72:
        parser.error("--dpi must be at least 72")

    source = args.pdf.resolve()
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    destination = args.output.resolve() / source_hash[:16]
    destination.mkdir(parents=True, exist_ok=True)
    document = fitz.open(source)
    pages = page_selection(args.pages, len(document))
    scope = hashlib.sha256(",".join(map(str, pages)).encode()).hexdigest()[:10]
    records = []
    sheets = []
    # Three columns preserve the page aspect ratio and keep a sheet manageable.
    columns, rows = 3, 4
    cell_width, cell_height = 320, 470
    margin, label_height = 12, 20
    batch_size = columns * rows
    if not args.only_detail:
        for start in range(0, len(pages), batch_size):
            batch = pages[start:start + batch_size]
            grid = fitz.open()
            page = grid.new_page(
                width=columns * cell_width,
                height=math.ceil(len(batch) / columns) * cell_height,
            )
            for slot, number in enumerate(batch):
                x = (slot % columns) * cell_width
                y = (slot // columns) * cell_height
                page.insert_text(
                    (x + margin, y + margin + 8),
                    f"PDF page {number + 1}", fontsize=10,
                )
                rectangle = fitz.Rect(
                    x + margin, y + margin + label_height,
                    x + cell_width - margin, y + cell_height - margin,
                )
                # A truly blank page cannot be imported with show_pdf_page.
                if document[number].get_contents():
                    page.show_pdf_page(rectangle, document, number)
                page.draw_rect(rectangle, color=(0.82, 0.82, 0.82), width=0.3)
            name = f"sheet-{batch[0] + 1:04d}-{batch[-1] + 1:04d}-{scope}.png"
            page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).save(
                destination / name
            )
            sheets.append({
                "image": name, "pdf_pages": [p + 1 for p in batch],
                "sha256": hashlib.sha256((destination / name).read_bytes()).hexdigest(),
            })
            grid.close()

    for number in pages:
        page = document[number]
        record = {
            "pdf_page": number + 1,
            "pdf_page_label": page.get_label(),
            "size_points": [page.rect.width, page.rect.height],
            "text_characters": len(page.get_text()),
            "inspection_status": "not inspected",
        }
        if args.detail or args.only_detail:
            name = f"page-{number + 1:04d}-{args.dpi}dpi.png"
            page.get_pixmap(dpi=args.dpi, alpha=False).save(destination / name)
            record["detail_image"] = name
            record["detail_sha256"] = hashlib.sha256(
                (destination / name).read_bytes()
            ).hexdigest()
        records.append(record)
    # Distinct page selections must not overwrite a previous evidence manifest.
    mode = "detail" if args.only_detail else ("both" if args.detail else "sheets")
    manifest = destination / f"manifest-{mode}-{scope}-{args.dpi}dpi.json"
    manifest.write_text(json.dumps({
        "source_pdf": str(source),
        "source_sha256": source_hash,
        "pdf_total_pages": len(document),
        "page_number_convention": "Physical PDF pages, starting at 1",
        "detail_dpi": args.dpi if args.detail or args.only_detail else None,
        "scope": "Rendering only; no visual inspection verdict is implied.",
        "contact_sheets": sheets,
        "pages": records,
    }, ensure_ascii=False, indent=2) + "\n")
    document.close()
    print(manifest)


if __name__ == "__main__":
    main()
