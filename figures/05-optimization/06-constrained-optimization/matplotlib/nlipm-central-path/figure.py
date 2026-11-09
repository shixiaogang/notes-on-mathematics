from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Central path of the running example.
fig, ax = figure(width_mm=84, height_mm=62)
data = central_path(np.logspace(4, -5, 500)); pth = np.array([c for _, c in data])
lim = (-1.5, 2.7, .2, 4.3)
region(ax); f_contours(ax, lim, [1.5, 2.5, 3.5, 5, 7, 9.5, 12.5])
ax.plot(pth[:, 0], pth[:, 1], color=GREEN, lw=1.5, zorder=4)
pts = {}
for m, y in ((3., 2.3), (1., 1.8), (.3, 1.3)):
    c, _ = center(m, [0, 2]); pts[str(m)] = c.tolist(); ax.plot(*c, 'o', color=GREEN, ms=4, zorder=6)
    ax.annotate(f'$\\mu={m:g}$', xy=c, xytext=(1.75, y), fontsize=7.5, va='center', zorder=7, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6, shrinkA=1, shrinkB=2))
ax.plot([0], [2], 'x', color=INK, ms=5, mew=1.1, zorder=6); ax.text(-.12, 2.08, '解析中心', fontsize=7.5, ha='right')
ax.plot(*XSTAR, 'o', color=RED, ms=5, zorder=7); ax.text(1.12, .88, '$x^*$', fontsize=8)
ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3]); ax.set_aspect('equal')
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'points': pts})
