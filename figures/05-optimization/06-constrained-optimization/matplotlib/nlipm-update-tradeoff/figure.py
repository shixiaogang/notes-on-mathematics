from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Barrier method on the running example: how the update factor trades outer against inner work.
T = [.9, .7, .5, .3, .2, .1, .05, .02, .01, .003, .001]
tot = []; out = []; mx = []
for t in T:
    r = barrier_method([0, 2], 1., t, tol=1e-6, inner=1e-8); tot.append(sum(r['counts'])); out.append(len(r['counts'])); mx.append(max(r['counts']))
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
a.semilogx(T, tot, color=GREEN, lw=1.5, marker='o', ms=3); a.invert_xaxis(); a.set_ylim(0, None); tag(a, '$\\tau$', '(a)'); a.set_ylabel('Newton步总数', labelpad=1)
b.semilogx(T, out, color=PURPLE, lw=1.5, marker='o', ms=3); b.semilogx(T, mx, color=YELLOW, lw=1.7, marker='o', ms=3)
b.set_yscale('log'); b.invert_xaxis(); tag(b, '$\\tau$', '(b)')
b.text(.25, 30, '外层轮数', fontsize=7.5); b.text(.012, 10, '单轮最多Newton步', fontsize=7.5, ha='center')
save(fig, OUT, 'figure', {'tau': T, 'newton_total': tot, 'outer': out, 'max_inner': mx})
