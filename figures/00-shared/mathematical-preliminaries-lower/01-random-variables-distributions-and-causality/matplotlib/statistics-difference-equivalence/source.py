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

WIDTH_MM,HEIGHT_MM=112,76
TITLE='Difference testing and equivalence testing answer separate questions'
SPEC={'Delta':.2,'alpha':.05,'normal_standard_errors_known':True,'estimates':[0,0,.10],'standard_errors':[.30,.04,.02],'rows':['未证等效','未显著且等效','显著且等效'],'difference_interval_level':.95,'TOST_interval_level':.90,'quantile_source':'Python standard library statistics.NormalDist.inv_cdf; Gaussian teaching model'}
from statistics import NormalDist
z95=NormalDist().inv_cdf(.975);z90=NormalDist().inv_cdf(.95)
est=np.array(SPEC['estimates']);se=np.array(SPEC['standard_errors']);ys=np.array([2,1,0])
fig,ax=plt.subplots(figsize=(WIDTH_MM/25.4,HEIGHT_MM/25.4))
fig.subplots_adjust(left=.27,right=.98,bottom=.18,top=.80)
ax.axvspan(-.2,.2,color=style.GREEN_FILL)
ax.axvline(0,color=style.MUTED,lw=.6,ls=':')
for bound in [-.2,.2]:ax.axvline(bound,color=style.GREEN,lw=.7,ls='--')
for mu,s,y in zip(est,se,ys):
 ax.plot([mu-z95*s,mu+z95*s],[y+.09,y+.09],color=style.BLUE,lw=.9)
 ax.plot([mu-z90*s,mu+z90*s],[y-.09,y-.09],color=style.GREEN,lw=2)
 ax.plot([mu],[y+.09],marker='o',color=style.BLUE,ms=2.7)
 ax.plot([mu],[y-.09],marker='s',color=style.GREEN,ms=2.7)
ax.plot([],[],color=style.BLUE,lw=.9,marker='o',ms=2.7,label='差异检验：95%区间')
ax.plot([],[],color=style.GREEN,lw=2,marker='s',ms=2.7,label='等效检验：90%区间')
ax.set(xlim=(-.66,.66),ylim=(-.45,2.45),yticks=ys,yticklabels=SPEC['rows'],xlabel=r'差异 $\delta$',xticks=[-.6,-.2,0,.2,.6],xticklabels=['−0.6',r'$-\Delta$','0',r'$\Delta$','0.6'])
ax.tick_params(axis='y',length=0,pad=5)
ax.spines['left'].set_visible(False)
ax.legend(loc='lower left',bbox_to_anchor=(-.30,1.01),ncol=1,handlelength=1.7,borderaxespad=0)
DATA={'estimates':est.tolist(),'standard_errors':se.tolist(),'z975':z95,'z95':z90,'interval95':np.column_stack([est-z95*se,est+z95*se]).tolist(),'interval90':np.column_stack([est-z90*se,est+z90*se]).tolist(),'difference_reject':(np.abs(est)>z95*se).tolist(),'TOST_reject':((est-z90*se>-.2)&(est+z90*se<.2)).tolist()}

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
