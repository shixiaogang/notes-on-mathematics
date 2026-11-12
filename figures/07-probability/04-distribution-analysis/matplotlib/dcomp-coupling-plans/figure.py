from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
from matplotlib.colors import LinearSegmentedColormap
# Couplings of P=(0.6,0.3,0.1) (rows, x) and Q=(0.3,0.3,0.4) (columns, y) on {0,1,2}.
# (a) independent pi=p q^T: sum|x-y|pi = 0.96, sum|x-y|^2 pi = 1.5
# (b) monotone: (0,0).3 (0,1).3 (1,2).3 (2,2).1: 0.6 and 0.6
# (c) jump: (0,0).3 (0,2).3 (1,1).3 (2,2).1: 0.6 and 1.2
p, q = P_EX, Q_EX
plans = [np.outer(p, q),
         np.array([[.3, .3, 0], [0, 0, .3], [0, 0, .1]]),
         np.array([[.3, 0, .3], [0, .3, 0], [0, 0, .1]])]
C = np.abs(np.subtract.outer(np.arange(3), np.arange(3))).astype(float)
cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.06, right=.99, top=.9, bottom=.2, wspace=.35)
facts = []
for ax, P in zip(axs, plans):
    assert np.allclose(P.sum(1), p) and np.allclose(P.sum(0), q)
    ax.imshow(P, cmap=cmap, vmin=0, vmax=.36)
    for i in range(3):
        for j in range(3):
            v = P[i, j]
            ax.text(j, i, '0' if v < 1e-12 else f'{v:.2f}',
                    ha='center', va='center', fontsize=7, color=INK if v < .25 else 'white')
    for k in range(4):
        ax.plot([-.5, 2.5], [k-.5, k-.5], color=GRID, lw=.65)
        ax.plot([k-.5, k-.5], [-.5, 2.5], color=GRID, lw=.65)
    ax.set_xticks(range(3)); ax.set_yticks(range(3))
    ax.xaxis.tick_top(); ax.tick_params(length=0, pad=2)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xlabel('$y$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
    facts.append({'cost1': float((C*P).sum()), 'cost2': float((C**2*P).sum())})
tags(fig, axs)
save(fig, HERE, 'figure', {'costs': facts})
