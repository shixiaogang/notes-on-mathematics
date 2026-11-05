"""Analytic teaching figure, not experimental observations. Re-run from any directory."""
from pathlib import Path
import sys, json, hashlib
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0, str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as style
style.configure()
from fontTools.ttLib import TTFont
import numpy as np
import matplotlib.pyplot as plt
OUT = Path(__file__).resolve().parent
WIDTH_MM, HEIGHT_MM = 105, 57
fig, ax = plt.subplots(figsize=(WIDTH_MM/25.4, HEIGHT_MM/25.4))
fig.subplots_adjust(left=.155, right=.965, bottom=.235, top=.94)

TITLE = 'Gibbs temperature controls reward preference'
SPEC={'outcomes':['a','b','c'],'reference':[1/3,1/3,1/3],'rewards':[0,1,2],'formula':'q_j(beta)=exp(r_j/beta)/sum_k exp(r_k/beta)','beta_grid':[.1,3,500]}
b=np.linspace(.1,3,500);r=np.array(SPEC['rewards']);w=np.exp((r[None,:]-2)/b[:,None]);q=w/w.sum(axis=1,keepdims=True)
assert np.allclose(q.sum(axis=1),1)
for j,c,ls in [(2,style.BLUE,'-'),(1,style.GREEN,'--'),(0,style.YELLOW,':')]:
 ax.plot(b,q[:,j],color=c,ls=ls,label=r'$r='+str(j)+'$')
ax.axhline(1/3,color=style.MUTED,ls='-.',lw=.6)
ax.text(2.96,.36,r'$1/3$',ha='right',va='bottom',fontsize=7.5,color=style.MUTED)
ax.set(xlim=(.1,3),ylim=(0,1.03),xlabel='温度 '+r'$\beta$',ylabel='最优概率 '+r'$q_j^\star$')
ax.set_xticks([.1,1,2,3]);ax.set_yticks([0,.25,.5,.75,1]);ax.legend(loc='upper right',ncol=3,fontsize=7.5,handlelength=1.2,columnspacing=.9)
DATA={'beta':b.tolist(),'optimal_probabilities':q.tolist()}

style.prepare_figure(fig)
fig.savefig(OUT/'figure.pdf')
fig.savefig(OUT/'figure.png', dpi=400)
meta = {'title': TITLE, 'kind': 'analytic teaching construction; not experimental data',
        'formula_and_parameters': SPEC, 'data': DATA,
        'physical_size_mm':[WIDTH_MM, HEIGHT_MM], 'body_reference_width_mm':WIDTH_MM,
        'scale':1, 'main_label_size_pt':8, 'note_size_pt':7.5,
        'provenance':'Analytic expressions and finite examples in the surrounding textbook section; original teaching drawing',
        'external_data':None, 'missing_values':None, 'filtering':None, 'sampling':'deterministic grids stated in formula_and_parameters; no stochastic data generated',
        'font_licenses': ['fonts/licenses/SourceHanSans-OFL.txt', 'fonts/licenses/LXGWWenKai-OFL.txt', 'fonts/licenses/FiraMath-font-license.txt', 'fonts/licenses/STIX-OFL.txt'],
        'generation_date':'2026-10-17',
        'style':style.style_record(),
        'font_versions':{p.name:TTFont(p)['name'].getDebugName(5) for p in [style.CN_FILE,style.NOTE_FILE,style.EN_FILE,style.STIX_FILE]},
        'files_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [OUT/'source.py', OUT/'figure.pdf', OUT/'figure.png']}}
(OUT/'metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n')
plt.close(fig)
