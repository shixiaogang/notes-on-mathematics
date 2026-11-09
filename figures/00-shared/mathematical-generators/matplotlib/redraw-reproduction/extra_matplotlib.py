"""New exact data panels for paths and mixed TikZ/Matplotlib figures."""
from pathlib import Path
import sys,json,math,argparse,hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pymupdf as fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
REGISTRY=json.loads((OUT/'registry.json').read_text())
# Current canonical location after the volume migration. Keep the historical
# redraw registry read-only while generating the asset referenced by the book.
CURRENT_FOLDERS = {'ch06-transient-growth':
 'figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ch06-transient-growth'}
def production_figure_dir(key):
 return ROOT / Path(CURRENT_FOLDERS.get(key, REGISTRY['figures']['v1-'+key]['folder']))
def figure_dir(key):
 p=production_figure_dir(key)
 return Path(__import__('os').environ['ACADEMIC_PROOF_DIR'])/p.relative_to(ROOT/'figures') if __import__('os').environ.get('ACADEMIC_PROOF_DIR') else p
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,RED,GREEN,MUTED,note
from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
configure()
sys.path.insert(0,str(OUT));import instrument_export

def export(fig,key,name='figure'):
 d=figure_dir(key);d.mkdir(parents=True,exist_ok=True)
 prepare_figure(fig)
 for ext in ['pdf','svg','png']:fig.savefig(d/f'{name}.{ext}',dpi=360)
 plt.close(fig)

def paths():
 t=np.arange(0,100,10);values=np.array([[14,16,12,23,20,26,23,31,27,34],[14,10,15,10,14,8,11,7,13,9],[14,20,24,19,27,32,30,24,34,37]])
 fig,ax=plt.subplots(figsize=(112/25.4,69/25.4),layout='constrained')
 for i,(y,c,m) in enumerate(zip(values,[BLUE,GREEN,PURPLE],['o','s','^']),1):ax.plot(t,y,color=c,marker=m,ms=3,ls=['-','--',':'][i-1],label=rf'$\omega_{i}$')
 ax.axvline(50,color=MUTED,ls=':',lw=.65)
 ax.set(xlabel=r'时间 $t$',ylabel=r'过程取值 $X_t(\omega)$',xlim=(-2,92),ylim=(0,41),xticks=[0,25,50,75,90],yticks=[0,10,20,30,40])
 ax.legend(loc='upper left',ncols=3)
 note(ax.text(52,39,r'固定 $t_0=50$，沿竖线取随机变量',fontsize=8,va='top'))
 export(fig,'rv-paths')
 (figure_dir('rv-paths')/'data.json').write_text(json.dumps({'kind':'Exact teaching coordinates copied from active TikZ source, not simulated observations','time':t.tolist(),'paths':values.tolist(),'fixed_time':50,'section_values':[26,8,32]},ensure_ascii=False,indent=2)+'\n')

def mixed(key,which,reuse_tikz=False):
 if which=='transient':
  k=np.arange(21);x1=40/3*(.8**k-.5**k);x2=.5**k;y=np.hypot(x1,x2)
  assert y[1]>y[0] and y[-1]<.2
  fig,ax=plt.subplots(figsize=(82/25.4,65/25.4),layout='constrained')
  ax.plot(k,y,color=BLUE,marker='o',ms=2.6)
  ax.axhline(1,color=MUTED,ls=':',lw=.6)
  ax.set(xlabel=r'迭代步 $k$',ylabel=r'$\Vert A^k x_0\Vert_2$',xlim=(-.4,20.4),ylim=(0,5.7),xticks=[0,5,10,15,20],yticks=[0,1,3,5])
  definition={'matrix':[[.8,4],[0,.5]],'x0':[0,1],'steps':k.tolist(),'trajectory':np.c_[x1,x2].tolist(),'norm2':y.tolist(),'formula':'x1[k]=(40/3)(0.8^k-0.5^k), x2[k]=0.5^k'}
 else:
  theta=np.linspace(0,np.pi,601);arc=theta;chord=2*np.sin(theta/2)
  fig,ax=plt.subplots(figsize=(82/25.4,65/25.4),layout='constrained')
  ax.plot(theta,arc,color=BLUE,label='短弧长度')
  ax.plot(theta,chord,color=GREEN,ls='--',label='弦长')
  ax.set(xlabel=r'圆心角 $\theta$',ylabel='距离',xlim=(0,np.pi),ylim=(0,3.4),xticks=[0,np.pi/2,np.pi],xticklabels=['0',r'$\pi/2$',r'$\pi$'],yticks=[0,1,2,3])
  ax.legend(loc='upper left')
  definition={'circle_radius':1,'theta':theta.tolist(),'arc':arc.tolist(),'chord':chord.tolist(),'formulas':['d_intrinsic=theta, 0<=theta<=pi','d_extrinsic=2*sin(theta/2)']}
 export(fig,key,'data-panel')
 d=figure_dir(key);(d/'data-panel-definitions.json').write_text(json.dumps(definition,ensure_ascii=False,indent=2)+'\n')
 # Reproduction includes the geometry panel. The shared renderer applies the
 # publication stroke policy once to a temporary input, preserving source widths.
 if not reuse_tikz:
  from render_tikz import render
  render(production_figure_dir(key)/'source.tex', output_dir=d)
 left=fitz.open(d/'source.pdf');right=fitz.open(d/'data-panel.pdf');doc=fitz.open();page=doc.new_page(width=169/25.4*72,height=65/25.4*72)
 page.show_pdf_page(fitz.Rect(0,0,82/25.4*72,page.rect.height),left,0)
 page.show_pdf_page(fitz.Rect(87/25.4*72,0,page.rect.width,page.rect.height),right,0)
 doc.save(d/'figure.pdf');page.get_pixmap(dpi=360).save(d/'figure.png');(d/'figure.svg').write_text(page.get_svg_image(text_as_path=True))
 (d/'composition.json').write_text(json.dumps({'route':'TikZ geometry + Matplotlib quantitative panel, vector PDF composition with PyMuPDF at native 82mm panel widths','left':'source.pdf','right':'data-panel.pdf','page_mm':[169,65],'definitions':'data-panel-definitions.json','style':style_record()},ensure_ascii=False,indent=2)+'\n')
 left.close();right.close();doc.close()
 recipe_path=d/'generation.json'
 recipe=json.loads(recipe_path.read_text()) if recipe_path.exists() else {'key':'v1-'+key}
 source_files=[production_figure_dir(key)/'source.tex',Path(__file__).resolve(),ROOT/'figures/00-shared/academic-drawing/render_tikz.py',ROOT/'figures/00-shared/academic-drawing/plot_style.py']
 recipe.update(route='mixed',stage='Reproduced with current publication fonts and strokes',actually_rendered=True,
   source=[str(p.relative_to(ROOT)) for p in source_files],
   data=str((production_figure_dir(key)/'data-panel-definitions.json').relative_to(ROOT)),
   assets_sha256={f'figure.{ext}':hashlib.sha256((d/f'figure.{ext}').read_bytes()).hexdigest() for ext in ['pdf','svg','png']},
   source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files},
   replay='python3 '+str(Path(__file__).resolve().relative_to(ROOT))+' --only '+key,
   replay_scope='Selected TikZ panel, analytical Matplotlib panel and vector composition; no unrelated outputs.')
 if key=='ch06-transient-growth':
  recipe['body_owner']='tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/05-linear-recurrence-stability.tex'
 recipe_path.write_text(json.dumps(recipe,ensure_ascii=False,indent=2)+'\n')
if __name__ == '__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--only',choices=['rv-paths','ch06-transient-growth','geometry-circle-distances'],help='Generate only the selected asset.')
 parser.add_argument('--reuse-tikz',action='store_true',help='Use an existing source.pdf after a separate shared-renderer batch.')
 args=parser.parse_args()
 if args.only in (None,'rv-paths'): paths()
 if args.only in (None,'ch06-transient-growth'): mixed('ch06-transient-growth','transient',args.reuse_tikz)
 if args.only in (None,'geometry-circle-distances'): mixed('geometry-circle-distances','circle',args.reuse_tikz)
