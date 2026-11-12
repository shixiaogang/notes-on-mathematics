from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Kantorovich-Rubinstein for the running example (positions 0,1,2, d=|x-y|).
# (a) distribution functions F_P (blue) and F_Q (yellow); the region between them has area 0.6.
# (b) dual LP max sum p_i u_i + sum q_j v_j s.t. u_i+v_j<=|x_i-y_j|; optimal u=(0,-1,-2), v=(0,1,2), value 0.6.
#     c-transform g(z)=min_j(|z-y_j|-v_j): tents |z-y_j|-v_j (purple dotted), g(z)=-z for z<=2 (blue);
#     red dots g(x_i)=u_i. E_P g - E_Q g = -0.5+1.1 = 0.6 = W_1.
p, q, xs = P_EX, Q_EX, X_EX
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.07, right=.98, top=.95, bottom=.26, wspace=.28)
ax = axs[0]
F, G = np.cumsum(p), np.cumsum(q)
edges = [-.5, 0, 1, 2, 2.5]
Fv = [0, F[0], F[1], 1]; Gv = [0, G[0], G[1], 1]
for k in range(4):
    a, b = edges[k], edges[k+1]
    lo, hi = sorted([Fv[k], Gv[k]])
    if hi > lo:
        ax.fill_between([a, b], [lo, lo], [hi, hi], color=BLUE_FILL, lw=0)
    ax.plot([a, b], [Fv[k], Fv[k]], color=BLUE, lw=1.4, solid_capstyle='butt')
    ax.plot([a, b], [Gv[k], Gv[k]], color=YELLOW, lw=1.6, solid_capstyle='butt')
lab(ax, .5, .93, '$F_P$', BLUE, ha='center')
lab(ax, .5, .5, '$F_Q$', YELLOW, ha='center')
ax.set_xlim(-.5, 2.5); ax.set_ylim(0, 1.08); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .3, .6, .9, 1])
axlab(ax, '$x$', None)
ax = axs[1]
z = np.linspace(-.6, 2.6, 600)
v = np.array([0., 1., 2.])
tents = np.abs(z[None, :]-xs[:, None])-v[:, None]
for t in tents:
    ax.plot(z, t, color=PURPLE, lw=.9, ls=DOT)
g = tents.min(0)
ax.plot(z, g, color=BLUE, lw=1.4)
for xi in xs:
    dot(ax, xi, -xi, RED, ms=3.8)
lab(ax, .9, -1.55, '$g(z)$', BLUE, ha='left')
ax.set_xlim(-.6, 2.6); ax.set_ylim(-2.4, 1.6); ax.set_xticks([0, 1, 2]); ax.set_yticks([-2, -1, 0, 1])
axlab(ax, '$z$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'area': float(np.sum(np.abs(F-G)[:2])), 'EPg': float(-p@xs), 'EQg': float(-q@xs)})
