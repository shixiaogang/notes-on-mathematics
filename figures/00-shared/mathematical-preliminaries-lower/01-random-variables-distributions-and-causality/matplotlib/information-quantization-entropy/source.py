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

TITLE = 'Finite resolution entropy versus differential entropy'
SPEC={'distribution':'X ~ Unif[0,1]','bins':'n equal bins, Delta=1/n','n':[1,2,4,8,16,32,64],'bin_mass':'1/n','H_nats':'log(n)','differential_entropy_nats':0}
n=np.array(SPEC['n']);h=np.log(n)
ax.plot(n,h,'o-',color=style.BLUE,ms=3,label=r'$H(X_\Delta)=\log n$')
ax.axhline(0,color=style.GREEN,ls='--',lw=1.1,label=r'$h(X)=0$')
ax.set_xscale('log',base=2)
ax.set(xlim=(.9,72),ylim=(-.2,4.65),xlabel='等宽格数 '+r'$n=1/\Delta$',ylabel='熵（nat）')
ax.set_xticks([1,2,4,8,16,32,64],['1','2','4','8','16','32','64']);ax.set_yticks([0,1,2,3,4]);ax.legend(loc='upper left',fontsize=7.5)
DATA={'n':n.tolist(),'bin_width':(1/n).tolist(),'discrete_entropy_nats':h.tolist(),'differential_entropy_nats':[0]*len(n)}

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
