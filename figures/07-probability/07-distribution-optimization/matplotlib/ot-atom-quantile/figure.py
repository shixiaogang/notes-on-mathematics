from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Source mu = 1/2 delta_0 + 1/2 Unif(1,2); target nu = Unif(0,2).
# (a) F (blue) and G (yellow), area |F-G| = 1/4 = W_1.
# (b) quantile coupling (F^{-1}(U), G^{-1}(U)): atom at 0 spread over [0,1] (vertical segment), identity on [1,2].
xs = np.linspace(-.3, 2.3, 2601)
F = np.where(xs < 0, 0, np.where(xs < 1, .5, np.where(xs < 2, .5+(xs-1)/2, 1.)))
G = np.clip(xs/2, 0, 1)
area = float(np.trapezoid(np.abs(F-G), xs))
u = np.linspace(1e-6, 1-1e-6, 200001)
qF = np.where(u <= .5, 0., 1+(2*u-1)); qG = 2*u
W1 = float(np.mean(np.abs(qF-qG))); W22 = float(np.mean((qF-qG)**2))
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, left=.07, right=.98, top=.95, bottom=.29, wspace=.28)
ax = axs[0]
ax.fill_between(xs, F, G, color=BLUE_FILL, lw=0)
ax.plot(xs[xs < 0], F[xs < 0], color=BLUE, lw=1.4); ax.plot(xs[xs >= 0], F[xs >= 0], color=BLUE, lw=1.4)
ax.plot(xs, G, color=YELLOW, lw=1.6)
dot(ax, 0, .5, color=BLUE, ms=3.6)
ax.text(.1, .6, '$F$', color=BLUE); ax.text(1.05, .3, '$G$', color=YELLOW)
ax.set_xlim(-.3, 2.3); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$x$', labelpad=1)
ax = axs[1]
ax.plot([0, 0], [0, 1], color=BLUE, lw=1.6)
ax.plot([1, 2], [1, 2], color=BLUE, lw=1.6)
ax.plot([-.2, 2.2], [-.2, 2.2], color=STROKE, lw=.6, ls=DOT)
ax.text(.08, .45, '原子拆开', color=INK, fontsize=7.5)
ax.set_xlim(-.3, 2.3); ax.set_ylim(-.1, 2.15); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$y$', labelpad=1)
ax.set_aspect('equal')
tags(fig, axs)
save(fig, HERE, 'figure', {'area': area, 'W1': W1, 'W2sq': W22, 'W2sq_exact': 1/6})
