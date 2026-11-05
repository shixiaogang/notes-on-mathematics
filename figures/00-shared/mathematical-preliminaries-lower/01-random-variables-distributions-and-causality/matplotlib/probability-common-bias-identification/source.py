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

TITLE = 'Identifiable sum does not identify signal and common bias'
SPEC={'model':'Y_i=theta+b+epsilon_i','noise':'independent N(0,1)','fixed_observable_law':'N(2,1)','equivalent_parameters':[[0,2],[1,1],[2,0]],'theta_grid':[-.3,3.3,300]}
t=np.linspace(-.3,3.3,300)
for c in [0,1,3]:ax.plot(t,c-t,color=style.GRID,lw=.6)
ax.plot(t,2-t,color=style.BLUE)
for ti,bi in SPEC['equivalent_parameters']:
 ax.plot(ti,bi,'o',color=style.BLUE,ms=3.3)
 ax.annotate(f'({ti}, {bi})',(ti,bi),xytext=(5,4),textcoords='offset points',fontsize=7.5)
style.note(ax.text(1.85,2.15,r'$\theta+b=2$',color=style.INK))
ax.set(xlim=(-.3,3.3),ylim=(-1.3,2.8),xlabel='真实信号 '+r'$\theta$',ylabel='共同偏移 '+r'$b$')
ax.set_xticks([0,1,2,3]);ax.set_yticks([-1,0,1,2]);ax.grid(True,axis='both')
DATA={'theta':t.tolist(),'bias_on_equivalence_line':(2-t).tolist(),'marked_pairs':SPEC['equivalent_parameters']}

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
