from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Purification on an optimal edge: from a near-central interior point to a vertex.
fig, ax = figure(width_mm=90, height_mm=68)
draw_tri(ax)
ax.plot([1, 0], [0, np.sqrt(3.)], color='#4C4D4F', lw=2.4, zorder=2)
c = np.array([0., 0., 1.]); ys = -np.logspace(2, -3, 400); Q, _ = central_run(c, ys)
ax.plot(*tri(Q).T, color=BLUE, lw=1.0, zorder=2)
hat = np.array([.4995, .4995, .001]); p0 = tri(hat); mid = tri(np.array([.5, .5, 0.]))
ax.plot(*p0, 'o', color=GREEN, ms=4.6, zorder=6)
ax.annotate('', xy=V3['e1'] + np.array([-.03, .05]), xytext=mid, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.5, shrinkA=0, shrinkB=0, mutation_scale=9), zorder=7)
ax.plot(*V3['e1'], 'o', color=RED, ms=5.2, zorder=8, clip_on=False)
ax.text(mid[0] + .1, mid[1] + .05, '内点法的输出', fontsize=7.5, ha='left')
ax.text(.86, .45, '基恢复', fontsize=7.5, ha='left')
ax.text(.95, .16, '$B=(1)$', fontsize=7.5, ha='left')
ax.set_xlim(-1.2, 1.75)
save(fig, OUT, 'figure', {'hat_x': hat.tolist()})
