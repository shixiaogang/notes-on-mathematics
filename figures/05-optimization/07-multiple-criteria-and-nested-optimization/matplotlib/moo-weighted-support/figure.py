from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Supporting lines of weighted sums: isotropic pair (a) and finite candidates (b).
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .24)
ax = axes[0]; setup(ax, (0, 1.2), (0, 1.2), [0, .5, 1], [0, .5, 1], equal=True); iso_fill(ax, 1.2)
u, v = iso_front(); ax.plot(u, v, color=RED, lw=2, zorder=3)
for w in (.25, .5, .75):
    p = np.array([(1-w)**2, w**2]); c = w*p[0]+(1-w)*p[1]
    t = np.array([0, 1.2]); ax.plot(t, (c-w*t)/(1-w), color=PURPLE, lw=1.1, zorder=4); dot(ax, p, RED, ms=5.5)
    ax.text(p[0]+.05, p[1]+.07, f'$w={w:g}$', color=INK, fontsize=7.5, zorder=8)
p = np.array([.25, .25]); arrow(ax, p, p-.17*np.array([1, 1]), PURPLE)
ax = axes[1]; setup(ax, (0, 8), (0, 9.5), range(0, 9, 2), range(0, 10, 2))
cands(ax, 'ABCD', off={'A': (.2, .2), 'B': (.2, .25), 'C': (.2, .25), 'D': (.15, .3)})
for w, k in ((.3, 'D'), (.65, 'B'), (.85, 'A')):
    q = CANDS[k]; c = w*q[0]+(1-w)*q[1]; t = np.array([0, 8.]); ax.plot(t, (c-w*t)/(1-w), color=PURPLE, lw=1.1, zorder=3)
B, D_ = CANDS['B'], CANDS['D']; ax.plot([B[0], D_[0]], [B[1], D_[1]], color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'weights_a': [.25, .5, .75], 'weights_b': {'D': .3, 'B': .65, 'A': .85}})
