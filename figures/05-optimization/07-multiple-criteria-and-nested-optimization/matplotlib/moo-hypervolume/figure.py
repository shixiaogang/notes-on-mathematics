from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Dominated area of A..D below r=(8,9), split into vertical strips.
P = np.array([CANDS[k] for k in 'ABCD'], float); r = np.array([8., 9.]); xs = np.r_[P[:, 0], r[0]]
fig, ax = figure(width_mm=86, height_mm=60)
setup(ax, (0, 9), (0, 10), range(0, 9, 2), range(0, 11, 2))
A = []
for i, c in enumerate((BLUE_FILL, GREEN_FILL, YELLOW_FILL, PURPLE_FILL)):
    x0, x1, y = xs[i], xs[i+1], P[i, 1]; ax.fill([x0, x1, x1, x0], [y, y, 9, 9], facecolor=c, edgecolor=MUTED, lw=.6, zorder=1); a = (x1-x0)*(9-y); A.append(a)
    ax.text((x0+x1)/2, (y+9)/2, f'{a:g}', ha='center', va='center', color=INK)
ax.plot(np.c_[xs[:-1], xs[1:]].ravel(), np.c_[P[:, 1], P[:, 1]].ravel(), color=RED, lw=1.2, zorder=3)
cands(ax, 'ABCD', off={'A': (-.55, -.1), 'B': (-.5, -.6), 'C': (-.5, -.6), 'D': (-.5, -.6)})
dot(ax, r, PURPLE); ax.text(8.15, 9.1, '$r$', color=PURPLE)
save(fig, HERE, 'figure', {'areas': A, 'hv': sum(A)}); print(A, sum(A))
