from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# E 在 u=x 处、方向 H_0^1 上的微分 int x eta；三种内积下的表示。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.29, bottom=.25)
w1 = X; w2 = (X-X**3)/6; w3 = X-np.sinh(X)/np.sinh(1)
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85); ax.plot(X, w1, color=YELLOW, lw=1.4); ax.plot([1], [1], 'o', ms=4.6, color=RED, mew=0)
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.06, 1.12); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('L² 梯度', labelpad=-2)
ax = axes[1]
ax.axhline(0, color=MUTED, lw=.85); ax.plot(X, w2, color=GREEN, lw=1.4); ax.plot(X, w3, color=PURPLE, lw=1.4)
ax.text(.5, .0705, r'$(x-x^3)/6$', color=GREEN, fontsize=7.5, ha='center')
ax.text(.47, .036, r'$x-\sinh x/\sinh 1$', color=PURPLE, fontsize=7.5, ha='center', va='top')
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.006, .082); ax.set_xticks([0, 1]); ax.set_yticks([0, .03, .06]); ax.set_yticklabels(['0', '0.03', '0.06']); ax.set_xlabel('$x$', labelpad=-4)
tags(fig, axes)
eta = X*(1-X); deta = 1-2*X; d = X[1]-X[0]
I = lambda y: float(d*(y.sum()-.5*y[0]-.5*y[-1]))
dw2 = (1-3*X**2)/6; dw3 = 1-np.cosh(X)/np.sinh(1)
save(fig, HERE, 'figure', {'check_all_equal_1/12': [I(X*eta), I(dw2*deta), I(dw3*deta+w3*eta)]})
