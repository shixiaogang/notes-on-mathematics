from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Central path of the running example, closed form x_i = mu/(c_i-y), mu = 1/sum 1/(c_i-y).
ys = np.concatenate([-np.logspace(4, -2, 300), np.linspace(0, 1 - 1e-5, 400)]); P, M = central_run(C_RUN, ys)
fig, ax = figure(width_mm=90, height_mm=74)
draw_tri(ax)
ax.plot(*tri(P).T, color=GREEN, lw=1.6, zorder=3)
marks = [(0., '$y=0,\\ \\mu=6/11$', (-.34, .62), 'center'), (.5, '$y=1/2,\\ \\mu=15/46$', (.42, .78), 'center'), (.9, '$y=0.9,\\ \\mu\\approx0.088$', (.3, .5), 'center')]
for y, lab, off, ha in marks:
    p, m = central_run(C_RUN, [y]); q = tri(p[0])
    ax.plot(*q, 'o', color=GREEN, ms=4.2, zorder=5)
    ax.annotate(lab, xy=q, xytext=q + off, fontsize=7.5, ha=ha, va='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6, shrinkA=0, shrinkB=2), zorder=6)
c0 = tri(np.ones(3) / 3); ax.plot(*c0, 'x', color=INK, ms=5, mew=1.1, zorder=5)
ax.text(c0[0] - .08, c0[1] - .02, '解析中心', fontsize=7.5, ha='right', va='center')
ax.plot(*V3['e1'], 'o', color=RED, ms=5.2, zorder=7, clip_on=False)
ax.set_xlim(-1.2, 1.55)
save(fig, OUT, 'figure', {'central_y0': central_run(C_RUN, [0.])[0][0].tolist()})
