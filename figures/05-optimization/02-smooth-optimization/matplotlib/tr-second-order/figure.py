from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# (a) g=(0,1), B=diag(-1,3), Delta=1：截断共轭梯度与精确解；(b) x^3。
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]; P1, P2 = np.meshgrid(np.linspace(-1.35, 1.35, 400), np.linspace(-1.35, 1.35, 400)); disk(ax, (0, 0), 1)
ax.contour(P1, P2, P2 - .5*P1**2 + 1.5*P2**2, levels=[-.8, -.6, -.4, -.2, 0, .3, .8, 1.6], colors=[BLUE], linewidths=.7)
a = np.sqrt(15)/4
ax.plot([0, 0], [0, -1/3], color=GREEN, lw=1.7); ax.plot([0], [-1/3], 'o', color=GREEN, ms=5, mew=0, zorder=6)
ax.plot([a, -a], [-.25, -.25], 'o', color=RED, ms=5, mew=0, zorder=6); ax.plot([0], [0], 'o', color=INK, ms=3.6, mew=0, zorder=6)
ax.set_aspect('equal'); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35); ax.set_xlabel('$p_1$', labelpad=1); ax.set_ylabel('$p_2$', labelpad=1)
ax = axs[1]; x = np.linspace(-1.3, 1.3, 300); ax.plot(x, x**3, color=BLUE, lw=1.4); ax.axhline(0, color=MUTED, lw=.85); ax.plot([0], [0], 'o', color=INK, ms=4.6, mew=0, zorder=6)
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-2.2, 2.2); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f$', labelpad=1)
panels(fig, .08, .985, .985, .22, .28); tags(fig, axs)
save(fig, HERE, 'figure', {'a': 'g=(0,1),B=diag(-1,3),radius 1', 'b': 'x^3'})
