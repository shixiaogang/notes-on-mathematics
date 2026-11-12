from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
from matplotlib.colors import LinearSegmentedColormap
# Running example, dual potentials f=(0,-1,-2), g=(0,1,2) for c=(x-y)^2.
# (a) curves (x-y_j)^2 - g_j (purple dotted), lower envelope f^c(x)=min_j (blue), red dots f_i at x_i.
# (b) slack s_ij = c_ij - f_i - g_j (white-to-blue), plan support of PI_OPT ringed in red.
a, b, C, f, g = A_EX, B_EX, C_EX, F_EX, G_EX
S = C-f[:, None]-g[None, :]
assert S.min() >= 0 and np.all(S[PI_OPT > 0] == 0)
xs = np.linspace(-.4, 2.9, 400)
cur = np.array([(xs-y)**2-gj for y, gj in zip(Y_EX, g)])
env = cur.min(0)
fig, axs = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [1.5, 1]})
panel(fig, left=.08, right=.98, top=.9, bottom=.27, wspace=.3)
ax = axs[0]
for k in range(3):
    ax.plot(xs, cur[k], color=PURPLE, lw=.85, ls=DOT)
    ax.text(Y_EX[k]+.62, .3844-g[k], f'$j={k}$', color=PURPLE, fontsize=7, va='center')
ax.plot(xs, env, color=BLUE, lw=1.4)
for i in range(3):
    dot(ax, X_EX[i], f[i])
ax.axhline(0, color=STROKE, lw=.6)
ax.set_ylim(-2.7, 1.6); ax.set_xlim(-.4, 2.9)
ax.set_xticks([0, 1, 2]); ax.set_yticks([-2, -1, 0, 1])
ax.set_xlabel('$x$', labelpad=1)
ax = axs[1]
heat(ax, S, vmax=6, fmt='{:.0f}')
for i, j in zip(*np.nonzero(PI_OPT)):
    ax.add_patch(__import__('matplotlib').patches.Circle((j, i), .38, fill=False, ec=RED, lw=1.1))
ax.set_xlabel('$j$', labelpad=1); ax.set_ylabel('$i$', labelpad=6, rotation=0)
tags(fig, axs)
save(fig, HERE, 'figure', {'slack': S.tolist(), 'dual_value': float(a@f+b@g), 'primal': float((C*PI_OPT).sum())})
