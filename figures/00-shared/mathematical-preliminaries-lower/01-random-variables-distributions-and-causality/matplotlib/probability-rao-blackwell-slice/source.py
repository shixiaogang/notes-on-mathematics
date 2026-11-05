"""Exact teaching construction; no experimental data. Run from any directory."""
from pathlib import Path
import sys,json,hashlib
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as style
style.configure()
from fontTools.ttLib import TTFont
import numpy as np
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent

WIDTH_MM,HEIGHT_MM=140,60
TITLE='Conditional averaging removes the extra Bernoulli draw'
SPEC={'X':'Uniform(0,1)','U':'Uniform(0,1), independent of X','Y':'indicator(U <= X**2)','conditional_mean':'E[Y|X]=X**2','slice_x':.6,'slice_height':.36,'means':[1/3,1/3],'variances':[2/9,4/45],'grid':'501 equally spaced points over [0,1]'}
x=np.linspace(0,1,501);f=x*x
fig,axes=plt.subplots(1,2,figsize=(WIDTH_MM/25.4,HEIGHT_MM/25.4))
fig.subplots_adjust(left=.08,right=.98,bottom=.23,top=.86,wspace=.36)
a,b=axes
for ax in axes:
 ax.set(xlim=(0,1),ylim=(0,1.03),xticks=[0,.5,1],yticks=[0,.5,1])
 ax.grid(False)
a.fill_between(x,0,f,color=style.BLUE_FILL)
a.plot(x,f,color=style.BLUE)
a.plot([.6,.6],[0,.36],color=style.GREEN,lw=2)
a.plot([.6,.6],[.36,1],color=style.MUTED,lw=.6,ls=':')
a.plot([.6],[.36],marker='o',ms=3,color=style.GREEN)
a.text(.69,.20,r'$Y=1$',color=style.BLUE)
a.text(.16,.72,r'$Y=0$',color=style.MUTED)
a.annotate(r'$x^2=0.36$',xy=(.6,.18),xytext=(.10,.37),arrowprops={'arrowstyle':'-','lw':.6,'color':style.STROKE})
a.set(xlabel=r'$x$',ylabel=r'$u$')
a.set_title('一次命中抽取',pad=8)
b.plot(x,f,color=style.GREEN,lw=1.1,label=r'$X^2$')
b.axhline(1/3,color=style.MUTED,lw=.6,ls='--')
b.text(.04,.37,r'$I=1/3$',color=style.MUTED)
b.text(.53,.83,r'$\mathbb{E}[Y\mid X=x]=x^2$',ha='center')
b.set(xlabel=r'$x$',ylabel='条件平均')
b.set_title('固定横坐标后求平均',pad=8)
DATA={'x':x.tolist(),'conditional_mean':f.tolist(),'selected_slice':{'x':.6,'length':.36}}

style.prepare_figure(fig)
fig.savefig(OUT/'figure.pdf')
fig.savefig(OUT/'figure.png',dpi=400)
meta={'title':TITLE,'kind':'analytic or finite teaching construction; not experimental observations',
 'formula_and_parameters':SPEC,'data':DATA,'physical_size_mm':[WIDTH_MM,HEIGHT_MM],
 'body_reference_width_mm':WIDTH_MM,'scale':1,'main_label_size_pt':8,'note_size_pt':7.5,
 'provenance':'Original teaching figure from the surrounding textbook formulas and explicitly constructed values',
 'external_data':None,'missing_values':None,'filtering':None,
 'sampling':'deterministic analytic grids or fully displayed finite construction; no stochastic samples generated',
 'font_licenses':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/LXGWWenKai-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/STIX-OFL.txt'],
 'generation_date':'2026-10-17','style':style.style_record(),
 'font_versions':{p.name:TTFont(p)['name'].getDebugName(5) for p in [style.CN_FILE,style.NOTE_FILE,style.EN_FILE,style.STIX_FILE]},
 'files_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [OUT/'source.py',OUT/'figure.pdf',OUT/'figure.png']}}
(OUT/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
plt.close(fig)
