#!/usr/bin/env python3
"""Check the labelled figure assets used by the active mathematics volumes."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'figures/00-shared/academic-drawing/integration-manifest.json'


def figure_blocks(text):
    """Include ordinary floats and explicitly numbered inline figures."""
    result = []
    for env, block in re.findall(r'\\begin\{(figure\*?)\}(.*?)\\end\{\1\}', text, re.S):
        labels = re.findall(r'\\label\{(fig:[^}]+)\}', block)
        result.append((env, block, labels))
    for block in re.findall(r'\\begin\{minipage\}.*?\\end\{minipage\}', text, re.S):
        labels = re.findall(r'\\functionalinlinefigurecaption\{(fig:[^}]+)\}', block)
        if labels:
            result.append(('inline', block, labels))
    return result


def check(registry):
    try:
        from scripts.book_catalog import volumes, tex_inputs
    except ModuleNotFoundError:
        from book_catalog import volumes, tex_inputs
    records = registry['records']
    labels = set()
    errors = []
    counts = {}
    active = {}
    for volume in volumes(ROOT):
        for owner, text in tex_inputs(ROOT, volume['content']).items():
            for env, block, figure_labels in figure_blocks(text):
                if figure_labels:
                    label = figure_labels[0]
                    if label in active:
                        errors.append(f'Duplicate active figure label: {label}')
                    active[label] = (owner, env, block)
    for item in records:
        label, owner, asset = item['label'], item['owner'], item['asset']
        if label in labels:
            errors.append(f'Duplicate registry label: {label}')
        labels.add(label)
        graphic = ROOT / asset
        if label not in active:
            errors.append(f'Inactive figure record: {label}')
            continue
        current_owner, env, block = active[label]
        if owner != current_owner:
            errors.append(f'Changed owner for {label}: {current_owner}')
        if not graphic.is_file():
            errors.append(f'Missing graphic: {asset}')
            continue
        raw_assets = re.findall(r'\{(figures/[^{}\n]+)\}', block)
        assets = [name if Path(name).suffix else name + '.tex' for name in raw_assets]
        if asset not in assets:
            errors.append(f'Figure does not use registered asset: {label}')
        if block.count('\\begingroup') != block.count('\\endgroup'):
            errors.append(f'Unbalanced figure group: {label}')
        if not any(cmd in block for cmd in ['\\caption', '\\functionalinlinefigurecaption']):
            errors.append(f'Missing caption: {label}')
        if graphic.suffix not in {'.pdf', '.png', '.tex'}:
            errors.append(f'Unexpected production format: {asset}')
        if item.get('sha256') != hashlib.sha256(graphic.read_bytes()).hexdigest():
            errors.append(f'Changed asset since registry: {asset}')
        for source in item.get('source', []):
            if not (ROOT / source).is_file():
                errors.append(f'Missing figure source: {source}')
        counts[str(item['volume'])] = counts.get(str(item['volume']), 0) + 1
    if counts != registry['expected_counts']:
        errors.append(f'Integration counts differ: {counts}')
    if set(active) != labels:
        errors.append(f'Body/registry mismatch: missing={sorted(set(active)-labels)}, unused={sorted(labels-set(active))}')
    return {'figures': len(records), 'counts': counts, 'errors': errors,
            'scope': 'active figure inventory and asset integrity; no content or visual review',
            'checks': ['unique labels', 'caption and body asset', 'asset SHA-256',
                       'active mathematics-volume coverage', 'figure source availability']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path)
    parser.add_argument('--assets-only', action='store_true',
                        help='Compatibility option; this tool checks asset integrity only.')
    args = parser.parse_args()
    result = check(json.loads(REGISTRY.read_text()))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))


if __name__ == '__main__':
    main()
