from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# 2x3 transport polytope: a=(0.4,0.6) at x=0,2; b=(0.2,0.3,0.5) at y=0,1,2; c=(x-y)^2.
# Coordinates s=pi_{1,1}, t=pi_{1,2}; feasible set 0<=s<=0.2, 0<=t<=0.3, s+t<=0.4.
# Cost = 2.7 - 8 s - 4 t, minimized at the vertex (0.2, 0.2) with value 0.3.
a = np.array([.4, .6]); b = np.array([.2, .3, .5]); C = (np.array([0, 2.])[:, None]-np.arange(3.)[None, :])**2
def full(s, t):
    return np.array([[s, t, a[0]-s-t], [b[0]-s, b[1]-t, b[2]-(a[0]-s-t)]])
V = np.array([[0, 0], [.2, 0], [.2, .2], [.1, .3], [0, .3]])
for s, t in V:
    assert full(s, t).min() > -1e-12
cost = lambda s, t: float((C*full(s, t)).sum())
fig, ax = figure(width_mm=76, height_mm=56)
panel(fig, left=.16, right=.96, top=.96, bottom=.17)
poly = np.vstack([V, V[:1]])
ax.fill(V[:, 0], V[:, 1], color=BLUE_FILL, lw=0)
ax.plot(poly[:, 0], poly[:, 1], color=BLUE, lw=1.2)
ss = np.linspace(-.02, .25, 2)
for lev in (.3, .7, 1.1, 1.5, 2.7):
    ax.plot(ss, (2.7-lev-8*ss)/4, color=PURPLE, lw=.85, ls=DASH)
off = {(0, 0): (-.012, -.022), (.2, 0): (.006, -.022), (.2, .2): (.008, .004), (.1, .3): (.004, .01), (0, .3): (-.012, .01)}
for (s0, t0), (dx, dy) in off.items():
    ax.text(s0+dx, t0+dy, f'{cost(s0, t0):.1f}', color=INK, fontsize=7.5)
ind = np.outer(a, b)
dot(ax, ind[0, 0], ind[0, 1], color=GREEN)
ax.text(ind[0, 0]+.008, ind[0, 1]-.022, '$a\\otimes b$', color=GREEN, fontsize=7.5)
dot(ax, .2, .2)
ax.set_xlim(-.02, .25); ax.set_ylim(-.03, .34)
ax.set_xlabel('$\\pi_{1,1}$'); ax.set_ylabel('$\\pi_{1,2}$')
ax.set_xticks([0, .1, .2]); ax.set_yticks([0, .1, .2, .3])
save(fig, HERE, 'figure', {'vertices': V.tolist(), 'vertex_costs': [cost(*v) for v in V],
                           'independent_cost': float((C*ind).sum()), 'optimum': full(.2, .2).tolist()})
