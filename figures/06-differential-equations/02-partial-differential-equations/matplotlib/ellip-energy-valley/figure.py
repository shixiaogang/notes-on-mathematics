from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# 2-dof energy 1/2 c^T K c - l^T c.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.03, wspace=.12, bottom=.2, right=.985, top=.98)
g = np.linspace(-3, 3, 401); P, Q = np.meshgrid(g, g)
cases = [([[2, -1], [-1, 2]], (1, 1)), ([[1, -1], [-1, 1]], (1, -1)), ([[1, -1], [-1, 1]], (1, 0))]
for ax, (K, l) in zip(axes, cases):
    K = np.array(K); E = .5*(K[0, 0]*P**2+2*K[0, 1]*P*Q+K[1, 1]*Q**2)-l[0]*P-l[1]*Q
    ax.contour(P, Q, E, 9, colors=BLUE, linewidths=.85, linestyles='solid')
axes[0].plot(1, 1, 'o', ms=4.6, color=RED, mew=0, zorder=5)
ax = axes[1]
ax.plot([-2.5, 3], [-3.5, 2], color=RED, lw=1.6)
ax = axes[2]
ax.annotate('', xy=(2.4, -.3), xytext=(.8, -1.0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.2, mutation_scale=9))
for ax in axes:
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel('$c_0$', labelpad=1)
    for s in ax.spines.values(): s.set_color(STROKE)
    ax.spines['top'].set_visible(True); ax.spines['right'].set_visible(True)
axes[0].set_ylabel('$c_1$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'cases': 'K=[[2,-1],[-1,2]],l=(1,1); K=[[1,-1],[-1,1]],l=(1,-1); same K,l=(1,0)'})
