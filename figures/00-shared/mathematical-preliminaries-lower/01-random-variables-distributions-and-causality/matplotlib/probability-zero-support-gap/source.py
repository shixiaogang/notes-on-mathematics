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

TITLE = 'Zero support cannot be restored by finite reweighting'
SPEC = {'outcomes':['a','b','c'],'P':[.5,.5,0],'Q':[.25,.25,.5],'support_gap':'P(c)=0,Q(c)=1/2; any finite w(c) yields P(c)w(c)=0'}
x=np.arange(3); p=np.array(SPEC['P']); q=np.array(SPEC['Q'])
ax.bar(x-.17,p,.30,color=style.BLUE,label=r'$P$')
ax.bar(x+.17,q,.30,color=style.GREEN,label=r'$Q$',hatch='//',edgecolor=style.STROKE,linewidth=.6)
ax.plot([2-.17],[0],marker='x',color=style.BLUE,ms=4.5,mew=1.1,clip_on=False)
ax.set(xticks=x,xticklabels=['a','b','c'],ylabel='概率',xlabel='同一结果',ylim=(0,.62))
ax.set_yticks([0,.25,.5]);ax.legend(ncol=2,loc='upper left',bbox_to_anchor=(0,1.04))
style.note(ax.annotate(r'$P(c)=0$',xy=(1.83,0),xytext=(1.35,.12),arrowprops={'arrowstyle':'-','color':style.STROKE,'lw':.6}))
DATA={'outcome_index':x.tolist(),'P':p.tolist(),'Q':q.tolist()}

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
