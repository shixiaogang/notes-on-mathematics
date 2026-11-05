"""Render the chapter 1–9 whitelist from the single canonical figure sources.

All exports first land in a worktree-local proof directory. Shared generators
may execute their other figures, but these exports remain under _unselected;
this runner never installs them. No scientific or visual acceptance is inferred.
"""
from pathlib import Path
import argparse, hashlib, json, os, runpy, shutil, sys, types
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE = Path(__file__).resolve().parent
STYLE = ROOT/'figures/00-shared/academic-drawing'
BASE = ROOT/'figures/00-shared/mathematical-generators/matplotlib/redraw-reproduction'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('keys',nargs='*')
    parser.add_argument('--proof-dir',type=Path,default=Path('build/figure-proofs/redraw-ch01-09'))
    args=parser.parse_args()
    proof=(ROOT/args.proof_dir).resolve();proof.mkdir(parents=True,exist_ok=True)
    scope=json.loads((HERE/'scope-baseline.json').read_text())['figures']
    allowed={x['key']:x for x in scope}
    reg=json.loads((BASE/'registry.json').read_text())
    fragment=json.loads((HERE/'registry-fragment.json').read_text())
    reg['figures'].update(fragment['figures']);reg['output_map'].extend(fragment['output_map'])
    keys=args.keys or list(allowed)
    for key in keys:
        if key not in allowed:raise ValueError('Not in chapter 1–9 whitelist: '+key)
    selected={key:reg['figures'][key] for key in keys}
    # The complete ownership whitelist protects all exports from a shared source;
    # only selected sources are executed, and install remains an explicit step.
    mapping={(x['source'],x['name']):ROOT/x['target'] for x in reg['output_map']
             if any(Path(x['target']).parent==Path(v['asset']).parent
                    and Path(x['target']).name.startswith(Path(v['asset']).stem+'.')
                    for v in allowed.values())}
    os.environ['ACADEMIC_PROOF_DIR']=str(proof)
    os.environ.setdefault('MPLCONFIGDIR','/private/tmp/volume-one-foundations-mpl-cache')
    sys.path[:0]=[str(STYLE),str(BASE)]
    import plot_style
    sys.modules['plot_style']=plot_style
    import instrument_export
    from matplotlib.figure import Figure
    original_save=Figure.savefig
    original_write=Path.write_text
    current_source=None
    def target(file):
        file=Path(file).resolve()
        if file.is_relative_to(proof):return file
        out=mapping.get((current_source,file.name))
        if out is not None:return proof/out.relative_to(ROOT/'figures')
        return proof/'_unselected'/Path(current_source or 'tikz').parent/file.name
    def save(fig,file,*args,**kwargs):
        out=target(file);out.parent.mkdir(parents=True,exist_ok=True)
        return original_save(fig,out,*args,**kwargs)
    Figure.savefig=save
    def write(self,data,*args,**kwargs):
        file=self.resolve()
        # Historic source records from flat generator groups are never overwritten.
        if file.is_relative_to(ROOT/'figures'):
            out=target(file);out.parent.mkdir(parents=True,exist_ok=True)
            return original_write(out,data,*args,**kwargs)
        return original_write(self,data,*args,**kwargs)
    Path.write_text=write
    module=types.ModuleType('resource_paths')
    def asset_path(directory,name):
        out=target(Path(directory)/name);out.parent.mkdir(parents=True,exist_ok=True);return out
    module.asset_path=asset_path;sys.modules['resource_paths']=module
    import render_tikz
    render_tikz.ROOT=ROOT
    render_tikz.PREAMBLE=(STYLE/'preamble.tex').read_text()+'\n\\PreviewBorder=0pt\n\\begin{document}\n'
    done=set();rendered=[]
    for key,row in selected.items():
        if row['route'] in ['simple','mixed']:
            src=ROOT/row['source'][0]
            dest=proof/Path(row['folder']).relative_to('figures')
            current_source=row['source'][0]
            result=render_tikz.render(src,dest)
            if row['route']=='simple':
                asset=Path(row['asset']);stem=asset.stem if asset.suffix=='.pdf' else src.stem
                for ext in ['pdf','png','svg']:
                    source=dest/(src.stem+'.'+ext);out=dest/(stem+'.'+ext)
                    if source!=out:shutil.copy2(source,out)
            print(key,'TikZ',result['physical_size_mm'],flush=True)
            rendered.append({'key':key,**result})
        if row['route'] in ['data','mixed']:
            src=next(s for s in row['source'] if s.endswith('.py'))
            if src in done:continue
            done.add(src);current_source=src
            if src.endswith('extra_matplotlib.py'):
                for other in ['v1-ch06-transient-growth','v1-geometry-circle-distances']:
                    f=reg['figures'][other];d=proof/Path(f['folder']).relative_to('figures');d.mkdir(parents=True,exist_ok=True)
                    if not (d/'source.pdf').exists():shutil.copy2(ROOT/f['folder']/'source.pdf',d/'source.pdf')
            sys.argv=[str(ROOT/src)]
            runpy.run_path(str(ROOT/src),run_name='__main__')
            print(src,'Matplotlib (owned exports only for installation)',flush=True)
    Path.write_text=original_write
    (proof/'run.json').write_text(json.dumps({'keys':keys,'source_sha256':{s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for row in selected.values() for s in row['source']},'tikz':rendered,'status':'Rendered proof only; scientific and visual acceptance pending'},ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
