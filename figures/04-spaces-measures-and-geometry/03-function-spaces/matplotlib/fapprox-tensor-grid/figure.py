from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# (a) product hat basis support on a 5x5 grid. (b) coefficient count m^d needed for error <= 1e-3 with |d_i^2 f|<=1: h^2 <= 8 eps/d, m-1 = ceil(1/h).
from matplotlib.patches import Rectangle
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.04, right=.985, top=.97, bottom=.25, wspace=.28)
ax = axes[0]
g = np.arange(5)/4
ax.add_patch(Rectangle((g[0], g[1]), g[2]-g[0], g[3]-g[1], facecolor=BLUE_FILL, edgecolor='none'))
for v in g:
    ax.plot([0, 1], [v, v], color=MUTED, lw=.7); ax.plot([v, v], [0, 1], color=MUTED, lw=.7)
ax.plot([g[1]], [g[2]], 'o', ms=4.2, color=BLUE, mew=0)
qx, qy = .63, .36
for cx in (g[2], g[3]):
    for cy in (g[1], g[2]):
        ax.plot([cx], [cy], 'o', ms=4, color=GREEN, mew=0)
ax.plot([qx], [qy], 'o', ms=4.4, mfc='white', mec=INK, mew=.85)
ax.set_xlim(-.04, 1.04); ax.set_ylim(-.04, 1.04); ax.set_aspect('equal'); ax.set_xticks(g); ax.set_xticklabels(['$t_0$', '$t_1$', '$t_2$', '$t_3$', '$t_4$']); ax.set_yticks(g); ax.set_yticklabels(['$t_0$', '$t_1$', '$t_2$', '$t_3$', '$t_4$'])
for s in ('top', 'right', 'bottom', 'left'): ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax = axes[1]
eps = 1e-3; ds = np.arange(1, 7); cnt = []
for d in ds:
    mm = int(np.ceil(1/np.sqrt(8*eps/d)-1e-12))+1; cnt.append(float(mm)**d); print(d, mm, float(mm)**d)
ax.bar(ds, cnt, width=.6, color=BLUE, bottom=1)
ax.set_yscale('log'); ax.set_ylim(1, 3e9); ax.set_xlim(.4, 6.6); ax.set_xticks(ds); ax.set_xlabel('$d$', labelpad=0); ax.set_ylabel('$m^d$', labelpad=1); ax.set_yticks([1e1, 1e3, 1e5, 1e7, 1e9])
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'm^d with m-1=ceil(1/h), h^2=8 eps/d, eps=1e-3'})
