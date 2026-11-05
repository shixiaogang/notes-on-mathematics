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

TITLE = 'Finite response change and local derivative'
SPEC={'response':'R_M(t,0)=t^2','reference_t':1,'local_derivative':2,'finite_step_h':1,'finite_response_change':3,'curve_grid':[0,2.2,441],'tangent_domain':[.6,1.65],'secant_domain':[1,2]}
t=np.linspace(0,2.2,441);tt=np.linspace(.6,1.65,200);ts=np.linspace(1,2,200)
ax.plot(t,t*t,color=style.BLUE,label='响应曲线')
ax.plot(tt,2*tt-1,color=style.GREEN,ls='--',label='局部切线')
ax.plot(ts,3*ts-2,color=style.YELLOW,ls=':',label='有限差割线')
ax.plot([1,2],[1,4],'o',color=style.BLUE,ms=3.5)
ax.axvline(1,color=style.GRID,lw=.6,ymax=1/5.2);ax.axvline(2,color=style.GRID,lw=.6,ymax=4/5.2)
ax.set(xlim=(0,2.2),ylim=(0,5.2),xlabel='设定剂量 '+r'$t$',ylabel='响应 '+r'$R_M(t,0)$')
ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2,3,4,5]);ax.legend(loc='upper left',fontsize=7.5)
DATA={'t':t.tolist(),'response':(t*t).tolist(),'tangent_t':tt.tolist(),'tangent':(2*tt-1).tolist(),'secant_t':ts.tolist(),'secant':(3*ts-2).tolist()}

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
