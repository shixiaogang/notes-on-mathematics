from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Truncated backward recovery with deterministic noise of 1e-3 per odd mode; T=0.05.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.08, wspace=.36, bottom=.27)
T = .05; eta = 1e-3
def rec(N):
    k = np.arange(1, N+1, 2)
    y = cs(k)*np.exp(-(k*pi)**2*T)+eta
    return ((y*np.exp((k*pi)**2*T))[:, None]*np.sqrt(2)*np.sin(np.outer(k, pi*X))).sum(0)
for ax, N, yl in zip(axes, (1, 3, 5), ((0, .66), (-.2, .66), (-420, 420))):
    r = rec(N); ax.plot(X, tent(X), color=BLUE, lw=1.4); ax.plot(X, r, color=GREEN, lw=1.2 if N < 5 else 1.0)
    ax.set_xlim(0, 1); ax.set_ylim(*yl); ax.set_xticks([0, .5, 1]); axlab(ax)
axes[0].set_yticks([0, .25, .5]); axes[0].set_yticklabels(['0', '1/4', '1/2']); axes[1].set_yticks([0, .25, .5]); axes[1].set_yticklabels(['0', '1/4', '1/2']); axes[2].set_yticks([-400, 0, 400])
tags(fig, axes)
save(fig, HERE, 'figure', {'N': [1, 3, 5], 'sup': [float(np.abs(rec(n)).max()) for n in (1, 3, 5)]})
