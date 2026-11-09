from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# 变分基本引理：g(x)>0 于 x0 附近，凸起 eta 只在那里非零。
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.075, wspace=.26, bottom=.27)
g = np.sin(5*X-.6)+.25
x0 = .3; r = .1
def bump(x):
    y = np.zeros_like(x); m = np.abs(x-x0) < r
    y[m] = np.exp(1-1/(1-((x[m]-x0)/r)**2)); return y
eta = bump(X)
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(X, g, color=BLUE, lw=1.4); ax.plot(X, eta, color=GREEN, lw=1.4)
dot(ax, x0, np.sin(5*x0-.6)+.25, RED)
ax.text(.75, .35, '$g$', color=BLUE, fontsize=8); ax.text(.42, .42, r'$\eta$', color=GREEN, fontsize=8)
ax.set_xlim(0, 1); ax.set_ylim(-1.05, 1.5); ax.set_xticks([.3]); ax.set_xticklabels(['$x_0$']); ax.set_yticks([0]); ax.set_xlabel('$x$', labelpad=1)
ax = axes[1]
ax.axhline(0, color=MUTED, lw=.85)
ax.fill_between(X, 0, g*eta, color=GREEN_FILL, lw=0)
ax.plot(X, g*eta, color=GREEN, lw=1.4)
ax.set_xlim(0, 1); ax.set_ylim(-.3, 1.5); ax.set_xticks([.3]); ax.set_xticklabels(['$x_0$']); ax.set_yticks([0]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel(r'$g\,\eta$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'g': 'sin(5x-.6)+.25', 'x0': x0, 'r': r})
