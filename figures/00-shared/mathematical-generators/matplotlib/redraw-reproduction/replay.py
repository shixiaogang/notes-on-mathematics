"""Reproduce archived volume-one figures without relying on output/ previews.

Run from any directory. Optional --proof-dir keeps audited assets unchanged.
Model backgrounds are retained because the image generation tool is stochastic.
"""
from pathlib import Path
import argparse, json, os, runpy, sys, types, shutil
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
B=Path(__file__).resolve().parent
REG=json.loads((B/'registry.json').read_text())
STYLE=ROOT/'figures/00-shared/academic-drawing'
if os.environ.get('ACADEMIC_STYLE_DIR'):
 STYLE=Path(os.environ['ACADEMIC_STYLE_DIR']).resolve()  # Read-only local integration check before root installs canonical style.
sys.path.insert(0,str(STYLE))

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('keys',nargs='+');p.add_argument('--proof-dir',type=Path)
 a=p.parse_args();proof=(ROOT/a.proof_dir).resolve() if a.proof_dir else None
 if proof:proof.mkdir(parents=True,exist_ok=True)
 os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/figure-proofs/matplotlib-cache'))
 if proof:os.environ['ACADEMIC_PROOF_DIR']=str(proof)
 import plot_style
 sys.modules['plot_style']=plot_style
 sys.path.insert(0,str(B));import instrument_export
 from matplotlib.figure import Figure
 original=Figure.savefig
 current_source=None
 mapping={(x['source'],x['name']):ROOT/x['target'] for x in REG['output_map']}
 def target(file):
  file=Path(file).resolve()
  file=mapping.get((current_source,file.name),file)
  if proof:
   try:file=proof/file.relative_to(ROOT/'figures')
   except ValueError:pass
  file.parent.mkdir(parents=True,exist_ok=True);return file
 def save(fig,file,*args,**kwargs):return original(fig,target(file),*args,**kwargs)
 Figure.savefig=save
 r=types.ModuleType('resource_paths')
 def asset_path(directory,name):
  out=mapping.get((current_source,name))
  if out is None:out=ROOT/'build/figure-proofs/volume-one-metadata'/Path(current_source).parent.name/name
  if proof:
   try:out=proof/out.relative_to(ROOT/'figures')
   except ValueError:pass
  out.parent.mkdir(parents=True,exist_ok=True);return out
 r.asset_path=asset_path;sys.modules['resource_paths']=r
 done=set()
 for key in a.keys:
  row=REG['figures'][key]
  if row['route'] in ['simple','mixed']:
   import render_tikz
   render_tikz.ROOT=ROOT
   preamble=(STYLE/'preamble.tex').read_text()
   # Canonical inputs stay relative to ROOT: an absolute iCloud path contains
   # a literal '~', which TeX would otherwise expand as an active character.
   if STYLE != ROOT/'figures/00-shared/academic-drawing':
    preamble=preamble.replace('figures/00-shared/academic-drawing',str(STYLE).replace('~',r'\string~'))
   border=row.get('preview_border_pt',2)
   render_tikz.PREAMBLE=preamble+'\n\\PreviewBorder='+str(border)+'pt\n\\begin{document}\n'
   dest=ROOT/row['folder']
   if proof:dest=proof/Path(row['folder']).relative_to('figures')
   result=render_tikz.render(ROOT/row['source'][0],dest)
   if row['route']=='simple':
    native=Path(row['source'][0]).stem
    body=Path(row['asset']).stem
    if native != body:
     for ext in ['pdf','png','svg']:shutil.copy2(dest/(native+'.'+ext),dest/(body+'.'+ext))
   print(key,'TikZ',result['physical_size_mm'],flush=True)
  if row['route'] in ['data','mixed']:
   src=next(s for s in row['source'] if s.endswith('.py'))
   if src in done:continue
   done.add(src);current_source=src
   # The extra panel source assembles one new quantitative graph and two vector composites.
   if src.endswith('extra_matplotlib.py') and proof:
    for k in ['v1-ch06-transient-growth','v1-geometry-circle-distances']:
     f=REG['figures'][k];out=proof/Path(f['folder']).relative_to('figures');out.mkdir(parents=True,exist_ok=True)
     if not (out/'source.pdf').exists():shutil.copy2(ROOT/f['folder']/'source.pdf',out/'source.pdf')
   sys.argv=[str(ROOT/src)];runpy.run_path(str(ROOT/src),run_name='__main__');print(src,'Matplotlib',flush=True)
  if row['route']=='generated':
   if proof:raise ValueError('Generated composition proofs are run with their local typeset source; backgrounds remain immutable.')
   sys.argv=[str(ROOT/row['source'][0])];runpy.run_path(str(ROOT/row['source'][0]),run_name='__main__')
if __name__=='__main__':main()
