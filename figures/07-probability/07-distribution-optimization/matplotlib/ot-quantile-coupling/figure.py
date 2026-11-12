from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Running example on the line. (a) distribution functions F (a, blue) and G (b, yellow),
# |F-G| shaded: area 0.6 = W_1. (b) quantile functions on (0,1); horizontal bands give the
# quantile coupling: (0,0) 0.2, (0,1) 0.3, (1,2) 0.3, (2,2) 0.2, equal to PI_OPT.
a, b = A_EX, B_EX
xs = np.linspace(-.5, 2.5, 3001)
F = np.array([a[X_EX <= x].sum() for x in xs]); G = np.array([b[Y_EX <= x].sum() for x in xs])
area = float(np.trapezoid(np.abs(F-G), xs))
u = np.linspace(1e-6, 1-1e-6, 20001)
qF = quantile(X_EX, a, u); qG = quantile(Y_EX, b, u)
W1 = float(np.mean(np.abs(qF-qG))); W22 = float(np.mean((qF-qG)**2))
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.98, top=.95, bottom=.29, wspace=.28)
ax = axs[0]
ax.fill_between(xs, F, G, color=BLUE_FILL, lw=0, step=None)
ax.plot(xs, F, color=BLUE, lw=1.4, drawstyle='steps-post')
ax.plot(xs, G, color=YELLOW, lw=1.6, drawstyle='steps-post')
ax.text(-.45, .56, '$F$', color=BLUE); ax.text(-.45, .26, '$G$', color=YELLOW)
ax.set_xlim(-.5, 2.5); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .2, .5, .8, 1])
ax.set_xlabel('$x$', labelpad=1)
ax = axs[1]
cuts = [0, .2, .5, .8, 1]
ax.plot(qF, u, color=BLUE, lw=1.4); ax.plot(qG, u, color=YELLOW, lw=1.6)
for lo in cuts[1:-1]:
    ax.axhline(lo, color=STROKE, lw=.6, ls=DOT)
for lo, hi in zip(cuts[:-1], cuts[1:]):
    m = (lo+hi)/2; xa = quantile(X_EX, a, m); yb = quantile(Y_EX, b, m)
    if xa == yb:
        dot(ax, xa, m, color=STROKE, ms=3.4)
    ax.annotate('', xy=(yb, m), xytext=(xa, m), arrowprops=dict(arrowstyle='->', color=STROKE, lw=.8, shrinkA=2, shrinkB=2))
    ax.text(2.25, m, f'{hi-lo:.1f}', fontsize=7, va='center', color=MUTED)
ax.set_xlim(-.3, 2.5); ax.set_ylim(0, 1); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .2, .5, .8, 1])
ax.set_xlabel('$x,\\ y$', labelpad=1); ax.set_ylabel('$u$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'area_F_minus_G': area, 'W1_quantile': W1, 'W2sq_quantile': W22})
