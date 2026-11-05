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

TITLE = 'The exponential moment domain depends on the evaluated variable'
SPEC={'X':'N(0,1)','M_X':'exp(lambda^2/2), finite for all real lambda','M_X_squared':'(1-2lambda)^(-1/2), finite iff lambda<1/2','lambda_X_grid':[-.5,1,601],'lambda_X2_grid':[-.5,.499,1000]}
l=np.linspace(-.5,1,601);l2=np.linspace(-.5,.499,1000)
m=np.exp(l*l/2);m2=1/np.sqrt(1-2*l2)
ax.axvspan(.5,1,color=style.RED_FILL,zorder=0)
ax.axvline(.5,color=style.RED,lw=.6,ls=':')
ax.plot(l,m,color=style.BLUE,label=r'$\mathbb{E}e^{\lambda X}$')
ax.plot(l2,m2,color=style.GREEN,ls='--',label=r'$\mathbb{E}e^{\lambda X^2}$')
style.note(ax.text(.73,4.2,'平方读数\n指数矩无限',ha='center',va='center'))
ax.set(xlim=(-.5,1),ylim=(0,5.5),xlabel='指数参数 '+r'$\lambda$',ylabel='指数矩')
ax.set_xticks([-.5,0,.5,1]);ax.set_yticks([0,1,2,3,4,5]);ax.legend(loc='upper left',fontsize=7.5)
DATA={'lambda_for_X':l.tolist(),'M_X':m.tolist(),'lambda_for_X2':l2.tolist(),'M_X2':m2.tolist(),'infinite_region_for_X2':[.5,1]}

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
