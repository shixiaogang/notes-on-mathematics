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

TITLE = 'Gaussian signal posterior after one observation'
SPEC={'S':'N(0,4)','epsilon':'N(0,1), independent of S','Y':'S+epsilon','observed_y':2,'conditional':'S|Y=2 ~ N(1.6,0.8)','s_grid':[-6,7,650]}
s=np.linspace(-6,7,650)
def normal(x,m,v):return np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v)
p=normal(s,0,4);post=normal(s,1.6,.8)
ax.plot(s,p,color=style.BLUE,label='观测前')
ax.plot(s,post,color=style.GREEN,ls='--',label='给定 '+r'$Y=2$')
ax.axvline(0,color=style.BLUE,ls=':',lw=.6,ymax=.34)
ax.axvline(1.6,color=style.GREEN,ls=':',lw=.6,ymax=.83)
ax.set(xlim=(-5,6),ylim=(0,.52),xlabel='信号取值 '+r'$s$',ylabel='概率密度')
ax.set_xticks([-4,-2,0,2,4,6]);ax.set_yticks([0,.2,.4]);ax.legend(loc='upper left')
DATA={'s':s.tolist(),'prior_density':p.tolist(),'conditional_density':post.tolist()}

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
