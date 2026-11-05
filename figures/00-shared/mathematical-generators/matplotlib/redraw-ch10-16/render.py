"""Replay only the C10–16 deterministic resource whitelist from canonical sources.
Unselected outputs of shared generators are confined to this worktree's build/.
Scientific arrays remain unchanged; approval is recorded separately after review.
"""
from pathlib import Path
import argparse, json, os, runpy, sys, shutil, hashlib, types
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
ROWS=json.loads((HERE/'baseline-source-map.json').read_text())+json.loads((HERE/'additions-source-map.json').read_text())
REPRO=ROOT/'figures/00-shared/mathematical-generators/matplotlib/redraw-reproduction'
REG=json.loads((REPRO/'registry.json').read_text())
STYLE=ROOT/'figures/00-shared/academic-drawing'
sys.path[:0]=[str(STYLE),str(REPRO)]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/redraw-ch10-16/mpl-cache'))

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('keys',nargs='*');a=p.parse_args()
 unknown=set(a.keys)-{x['key'] for x in ROWS}
 if unknown:p.error('Unknown resource keys: '+', '.join(sorted(unknown)))
 selected=[x for x in ROWS if not a.keys or x['key'] in a.keys]
 wanted={x['key'] for x in selected}
 folders={str((ROOT/Path(x['path']).parent).resolve()) for x in selected}
 mapping={(x['source'],x['name']):ROOT/x['target'] for x in REG['output_map']}
 current=[None]
 original_write=Path.write_text
 def route(file):
  q=Path(file).resolve();src=current[0]
  if src is None:return q
  exact=mapping.get((src,q.name))
  if exact and str(exact.parent.resolve()) in folders:return exact
  if str(q.parent) in folders:return q
  return ROOT/'build/redraw-ch10-16/unselected'/Path(src).parent.name/q.name
 def write(q,data,*args,**kwargs):
  target=route(q);target.parent.mkdir(parents=True,exist_ok=True)
  return original_write(target,data,*args,**kwargs)
 Path.write_text=write
 import plot_style, instrument_export
 from matplotlib.figure import Figure
 original=Figure.savefig
 def save(fig,file,*args,**kwargs):
  target=route(file);target.parent.mkdir(parents=True,exist_ok=True)
  return original(fig,target,*args,**kwargs)
 Figure.savefig=save
 r=types.ModuleType('resource_paths')
 def asset_path(directory,name):
  q=mapping.get((current[0],name),ROOT/'build/redraw-ch10-16/unselected'/Path(current[0]).parent.name/name)
  q=route(q);q.parent.mkdir(parents=True,exist_ok=True);return q
 r.asset_path=asset_path;sys.modules['resource_paths']=r
 sources=[]
 for row in selected:
  if row['route']=='data':
   src=next(s for s in row['source'] if s.endswith('.py'))
   if src not in sources:sources.append(src)
 for src in sources:
  current[0]=src
  if src.endswith('extra_matplotlib.py'):
   code=(ROOT/src).read_text().replace("paths();mixed('ch06-transient-growth','transient');mixed('geometry-circle-distances','circle')","paths()")
   exec(compile(code,str(ROOT/src),'exec'),{'__file__':str(ROOT/src),'__name__':'__main__'})
  else:
   sys.argv=[str(ROOT/src)];runpy.run_path(str(ROOT/src),run_name='__main__')
  print('Matplotlib',src,flush=True)
 current[0]=None
 import render_tikz
 render_tikz.ROOT=ROOT;render_tikz.PREAMBLE=(STYLE/'preamble.tex').read_text().replace(r'{\PreviewBorder}{2pt}',r'{\PreviewBorder}{0pt}')+'\n\\begin{document}\n'
 for row in selected:
  folder=ROOT/Path(row['path']).parent
  if row['route']=='simple':
   staging=ROOT/'build/redraw-ch10-16/tikz-exports'/row['key']
   result=render_tikz.render(ROOT/row['source'][0],staging)
   for ext in ['pdf','png','svg']:shutil.copy2(staging/('source.'+ext),folder/('figure.'+ext))
   shutil.copy2(staging/'source.render.json',folder/'figure.render.json')
   print(row['key'],result['physical_size_mm'],flush=True)
  else:
   for src,dest in [('figure.data.json','data.json'),('figure.typography.json','typography-check.json')]:
    if (folder/src).exists():shutil.copy2(folder/src,folder/dest)
  record={'key':row['key'],'chapter':row['chapter'],'canonical_source':row['source'],'source_sha256':{s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in row['source']},'baseline_source_sha256':row['source_shas'],'insertion_width_mm':row['insertion_width_mm'],'style':plot_style.style_record(),'approval':'exported; mathematical and visual review recorded separately'}
  (folder/'redraw-20261011.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
