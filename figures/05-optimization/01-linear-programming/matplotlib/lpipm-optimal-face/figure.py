from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Central paths: unique optimal vertex against a whole optimal edge.
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
ys = np.concatenate([-np.logspace(4, -2, 300), np.linspace(0, 1 - 1e-5, 400)]); P, _ = central_run(C_RUN, ys)
draw_tri(a); a.plot(*tri(P).T, color=GREEN, lw=1.6, zorder=3); a.plot(*V3['e1'], 'o', color=RED, ms=5.2, zorder=7, clip_on=False)
a.text(0, -.14, '(a) $\\mathbf{c}=(1,2,3)$', ha='center', va='top', fontsize=8)
c = np.array([0., 0., 1.]); ys = -np.logspace(4, -6, 800); Q, _ = central_run(c, ys)
draw_tri(b)
b.plot([1, 0], [0, np.sqrt(3.)], color='#4C4D4F', lw=2.4, zorder=2)
b.plot(*tri(Q).T, color=GREEN, lw=1.6, zorder=3)
mid = tri(np.array([.5, .5, 0.])); b.plot(*mid, 'o', color=RED, ms=5.2, zorder=7)
b.text(mid[0] + .1, mid[1] + .1, '$(1/2,1/2,0)$', fontsize=7.5, ha='left')
b.text(.0, -.14, '(b) $\\mathbf{c}=(0,0,1)$', ha='center', va='top', fontsize=8)
save(fig, OUT, 'figure', {'limit_b': Q[-1].tolist()})
