from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# E0=int u'^2/2，帐篷 u=min(x,1-x)；H_0^1 梯度=u；离散 L^2 梯度 (K u)/Delta 在中点 =2n。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.27, bottom=.28)
ax = axes[0]
u = np.minimum(X, 1-X)
ax.plot(X, u, color=GREEN, lw=1.4)
ax.set_xlim(-.03, 1.03); ax.set_ylim(-.03, .62); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .5]); ax.set_yticklabels(['0', '1/2']); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=-2)
ax = axes[1]
rec = {}
for n, c in ((8, YELLOW), (16, BLUE), (32, GREEN)):
    K, M = hats(n); nodes = np.arange(n+1)/n
    un = np.minimum(nodes, 1-nodes)
    r = (K@un)[1:-1]*n
    rec[n] = float(r.max())
    ax.plot(nodes[1:-1], r, color=c, lw=1.4)
    ax.text(.5+.055, r.max()-1, f'$n={n}$', color=c, fontsize=7.5, va='top')
ax.set_xlim(.1, .9); ax.set_ylim(-3, 72); ax.set_xticks([.25, .5, .75]); ax.set_xticklabels(['1/4', '1/2', '3/4']); ax.set_yticks([0, 16, 32, 64]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('离散 L² 梯度', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'max_L2_grad_by_n': rec})
