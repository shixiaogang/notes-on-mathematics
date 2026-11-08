"""Batch-render the active TikZ inventory with the publication stroke policy.
Run from any directory. Each picture remains an independently editable source.
"""
from pathlib import Path
import hashlib,json,subprocess,argparse
import pymupdf as fitz
from render_tikz import ROOT,PREAMBLE,publication_strokes
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--changed-sources',action='store_true',help='Only export assets whose editable source hash has changed or which lack an export.')
args=parser.parse_args()
records=json.loads((ROOT/'figures/00-shared/academic-drawing/integration-manifest.json').read_text())['records']
items=[]
for r in records:
    if '/tikz/' not in r['asset']: continue
    asset=ROOT/r['asset']
    candidates=[asset.with_suffix('.tex'),asset.parent/'source.tex']+[ROOT/p for p in r['source'] if p.endswith('.tex')]
    source=next((p for p in candidates if p.exists() and '\\begin{tikzpicture}' in p.read_text()),None)
    if source is None: raise ValueError('No editable TikZ source: '+r['asset'])
    if args.changed_sources and asset.exists() and asset.with_suffix('.render.json').exists():
        old=json.loads(asset.with_suffix('.render.json').read_text())
        if old.get('source_sha256')==hashlib.sha256(source.read_bytes()).hexdigest():continue
    if not any(item[0]==asset for item in items):items.append((asset,source))
if not items:
    print('No changed TikZ sources');raise SystemExit(0)
work=ROOT/'build/figure-proofs/inventory';work.mkdir(parents=True,exist_ok=True)
inputs=[]
for i,(asset,source) in enumerate(items):
    prepared=work/f'drawing-{i:03}.tex';prepared.write_text(publication_strokes(source.read_text()))
    inputs.append('\\begingroup\\input{'+str(prepared.relative_to(ROOT))+'}\\endgroup')
(work/'batch.tex').write_text(PREAMBLE+'\n'.join(inputs)+'\n\\end{document}\n')
with (work/'compile.log').open('w') as log:
    subprocess.run(['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(work.relative_to(ROOT)),str((work/'batch.tex').relative_to(ROOT))],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
    subprocess.run(['xdvipdfmx','-o',str(work/'batch.pdf'),str(work/'batch.xdv')],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
if 'Missing character:' in (work/'compile.log').read_text():raise ValueError('Missing glyph in batch')
with fitz.open(work/'batch.pdf') as doc:
    if len(doc)!=len(items):raise ValueError((len(doc),len(items)))
    for i,(asset,source) in enumerate(items):
        one=fitz.open();one.insert_pdf(doc,from_page=i,to_page=i);one.save(asset);one.close();page=doc[i]
        asset.with_suffix('.png').write_bytes(page.get_pixmap(dpi=300).tobytes('png'))
        asset.with_suffix('.svg').write_text(page.get_svg_image(text_as_path=True))
        report=dict(source=str(source.relative_to(ROOT)),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),physical_size_mm=[round(x*25.4/72,3) for x in [page.rect.width,page.rect.height]],stroke_policy='explicit widths x1.35, minimum .65pt; default .95pt',exports=['PDF','PNG 300 dpi','SVG'],status='rendered; visual review separately recorded')
        asset.with_suffix('.render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Rendered',len(items),'active TikZ figures')
