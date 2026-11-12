"""Total expectation as centre of mass on the sensor table.
Top three tiers: joint masses P(X=x, Y=y) (blue stems, height proportional to mass) for x=0,1,2,
group centroids m(x)=1/3, 1, 5/3 (green triangles).
Bottom tier: masses P(X=x)=0.3, 0.4, 0.3 moved to m(x) (green stems); their centroid E[Y]=1 (red triangle)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

fig, ax = figure(width_mm=96, height_mm=58)
H = 2.2   # stem height per unit mass
levels = {0: 3.0, 1: 2.0, 2: 1.0}
for x, base in levels.items():
    ax.plot([-0.25, 2.25], [base, base], color=STROKE, lw=0.8)
    row = P[x]
    for y in range(3):
        if row[y] > 0:
            ax.plot([y, y], [base, base + H*row[y]], color=BLUE, lw=2.2, solid_capstyle='butt')
            ax.text(y + 0.06, base + H*row[y] - 0.02, f'{row[y]:.1f}', fontsize=7, color=MUTED, va='top')
    mx = (np.arange(3)*row).sum()/row.sum()
    ax.scatter([mx], [base - 0.08], marker='^', s=26, color=GREEN, zorder=4)
    ax.text(-0.32, base + 0.18, f'$x={x}$', ha='right', fontsize=7.5)
base = 0.0
ax.plot([-0.25, 2.25], [base, base], color=STROKE, lw=0.8)
for x, mx in zip(range(3), [1/3, 1, 5/3]):
    p = P[x].sum()
    ax.plot([mx, mx], [base, base + H*p], color=GREEN, lw=2.2, solid_capstyle='butt')
    ax.text(mx + 0.06, base + H*p - 0.02, f'{p:.1f}', fontsize=7, color=MUTED, va='top')
ax.scatter([1], [base - 0.08], marker='^', s=30, color=RED, zorder=4)
ax.text(-0.32, base + 0.18, r'$m(X)$', ha='right', fontsize=7.5)
ax.set_xlim(-0.75, 2.3); ax.set_ylim(-0.3, 3.75)
ax.set_xticks([0, 1/3, 1, 5/3, 2]); ax.set_xticklabels(['0', '1/3', '1', '5/3', '2'])
ax.set_yticks([]); ax.spines['left'].set_visible(False)
ax.set_xlabel('$y$', labelpad=1)
save(fig, Path(__file__).resolve().parent, 'figure', {'group_means': [1/3, 1, 5/3], 'weights': [.3, .4, .3], 'EY': 1})
