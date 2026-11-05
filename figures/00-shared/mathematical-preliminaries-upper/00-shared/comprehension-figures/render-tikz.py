#!/usr/bin/env python3
"""Compile the editable comprehension additions, in one serial build queue."""
from pathlib import Path
import argparse
import json
from support import ROOT, render_tikz, provenance

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('sources', nargs='*', help='Optional repository-relative fragments')
args = parser.parse_args()
sources = [ROOT/p for p in args.sources] if args.sources else sorted(
    (ROOT/'figures/01-mathematical-preliminaries-upper').glob('*/tikz/*comprehension-additions/*.tex'))
failures = []
for source in sources:
    try:
        render_tikz(source)
        print(source.relative_to(ROOT), flush=True)
    except RuntimeError as error:
        failures.append(str(source.relative_to(ROOT)))
        print(str(error), flush=True)
if not args.sources:
    (Path(__file__).parent/'typography.json').write_text(json.dumps(provenance(),ensure_ascii=False,indent=2)+'\n')
print('Compiled:', len(sources))
if failures:
    raise SystemExit('Failed: '+', '.join(failures))
