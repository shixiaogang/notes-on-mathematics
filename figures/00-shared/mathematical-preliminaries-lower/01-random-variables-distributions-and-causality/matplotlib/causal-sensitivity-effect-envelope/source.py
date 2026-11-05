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

TITLE = 'Assumed selection-bias strength and causal-effect envelope'
SPEC={'fixed_stratum':'x','e(x)':.3,'mu1_minus_mu0':.5,'Gamma1':'.2s','Gamma0':'.1s','Delta':'.17s','lower':'.5-.17s','upper':'.5+.17s','s_grid':[0,3.5,351],'zero_lower_threshold':'50/17'}
s=np.linspace(0,3.5,351);lo=.5-.17*s;hi=.5+.17*s
ax.fill_between(s,lo,hi,color=style.BLUE_FILL)
ax.plot(s,hi,color=style.BLUE);ax.plot(s,lo,color=style.BLUE)
ax.axhline(0,color=style.STROKE,lw=.6)
ax.axhline(.5,color=style.GREEN,lw=1.1,ls='--')
ax.axvline(50/17,color=style.YELLOW,lw=.8,ls=':')
ax.plot([1],[.33],marker='o',color=style.BLUE,ms=3);ax.plot([1],[.67],marker='o',color=style.BLUE,ms=3)
style.note(ax.text(2.55,1.08,'上界',ha='right',va='bottom'))
style.note(ax.text(2.55,-.12,'下界',ha='right',va='top'))
style.note(ax.text(1.35,.53,'观测均值差',va='bottom',color=style.INK))
style.note(ax.text(50/17-.06,.22,r'$s=50/17$',ha='right'))
ax.set(xlim=(0,3.5),ylim=(-.2,1.2),xlabel='偏差上界的共同放宽倍数 '+r'$s$',ylabel='效应（结果单位）')
ax.set_xticks([0,1,2,3]);ax.set_yticks([0,.5,1])
DATA={'s':s.tolist(),'lower_effect_bound':lo.tolist(),'upper_effect_bound':hi.tolist()}

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
