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


WIDTH_MM,HEIGHT_MM=140,61
TITLE='Skorokhod J1 convergence aligns nearby jump times'
SPEC={'domain':[0,1],'limit_path':'x(t)=indicator(t>=.5)','approximating_path':'x_n(t)=indicator(t>=tau_n)','tau_n':'.5+.1/n','n_displayed':1,'lambda_n':'piecewise linear through (0,0),(.5,tau_n),(1,1)','uniform_path_error':1,'time_change_error':.1,'aligned_path_error':0,'sampling':'exact piecewise lines; no smoothing'}
tau=.6
fig,axes=plt.subplots(1,2,figsize=(WIDTH_MM/25.4,HEIGHT_MM/25.4))
fig.subplots_adjust(left=.095,right=.98,bottom=.23,top=.84,wspace=.38)
a,b=axes
for ax in axes:
 ax.set(xlim=(0,1),ylim=(-.04,1.08),xticks=[0,.5,1],yticks=[0,.5,1])
a.axvspan(.5,tau,color=style.RED_FILL)
a.plot([0,.5],[0,0],color=style.BLUE,lw=1.1)
a.plot([.5,1],[1,1],color=style.BLUE,lw=1.1)
a.plot([0,tau],[0,0],color=style.GREEN,lw=1.1,ls='--')
a.plot([tau,1],[1,1],color=style.GREEN,lw=1.1,ls='--')
a.plot([.5],[0],marker='o',mfc='white',mec=style.BLUE,ms=3)
a.plot([.5],[1],marker='o',color=style.BLUE,ms=3)
a.plot([tau],[0],marker='s',mfc='white',mec=style.GREEN,ms=3)
a.plot([tau],[1],marker='s',color=style.GREEN,ms=3)
a.annotate('',xy=(.55,.94),xytext=(.55,.06),arrowprops={'arrowstyle':'<->','lw':.6,'color':style.RED})
a.text(.70,.48,'差为 1',color=style.RED,ha='center')
a.text(.20,.18,r'$x_n(t)$',color=style.GREEN)
a.text(.80,.85,r'$x(t)$',color=style.BLUE)
a.set(xlabel=r'原时刻 $t$',ylabel='路径取值')
a.set_title('未对齐：最大取值差不趋零',pad=7)
b.plot([0,1],[0,1],color=style.MUTED,lw=.6,ls=':')
b.plot([0,.5,1],[0,tau,1],color=style.GREEN,lw=1.1)
b.plot([.5],[tau],marker='s',color=style.GREEN,ms=3)
b.plot([.5,.5],[.5,tau],color=style.RED,lw=1)
b.text(.57,.52,r'$0.1/n$',color=style.RED)
b.text(.66,.84,r'$\lambda_n(t)$',color=style.GREEN)
b.text(.76,.50,r'$t$',color=style.MUTED)
b.set(xlabel=r'目标时刻 $t$',ylabel='校正后时刻')
b.set_title('时间校正：将跳跃时刻对齐',pad=7)
DATA={'n':1,'jump_time_limit':.5,'jump_time_n':tau,'time_map_knots':[[0,0],[.5,tau],[1,1]],'errors':{'sup_xn_minus_x':1,'sup_lambda_minus_identity':.1,'sup_xn_composed_lambda_minus_x':0}}
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
