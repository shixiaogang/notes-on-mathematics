from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# (a) Cell cost g(c) = int_0^1 (x-c)^2 f(x) dx for Laplace(0,1) on the cell [0,1): parabola with minimum at the
#     conditional mean m = 0.418 (red); value at the midpoint 0.5 shown in yellow.
# (b) Squared errors (x-c_j)^2 for points c = 0.5, 1.5 (round-0 points of the Lloyd example); the lower envelope
#     switches at the midpoint t = 1 (red).
m = cmean(0, 1); p = mass(0, 1)
c = np.linspace(-.1, 1.1, 400)
g = np.array([cell_mse(0, 1, ci) for ci in c])
fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2)
panel(fig, left=.1, right=.98, bottom=.27, top=.95, wspace=.33)
a.plot(c, g, color=BLUE, lw=1.4)
a.axvline(m, color=RED, lw=.85, ls=DASH)
dot(a, m, cell_mse(0, 1, m)); dot(a, .5, cell_mse(0, 1, .5), color=YELLOW)
lab(a, m-.03, .072, '$m=0.418$', RED, ha='right'); lab(a, .55, .006, '$c=0.5$', YELLOW)
for e in (0, 1): a.axvline(e, color=STROKE, lw=.6, ls=DOT)
a.set_xlim(-.1, 1.1); a.set_ylim(0, .2); a.set_xlabel('$c$', labelpad=1)
lab(a, .02, .175, r'$\int_0^1(x-c)^2f(x)\,\mathrm{d}x$', BLUE, fontsize=7)
x = np.linspace(-.5, 2.5, 400)
e1 = (x-.5)**2; e2 = (x-1.5)**2
b.plot(x, e1, color=BLUE, lw=1.0, ls=DASH); b.plot(x, e2, color=YELLOW, lw=1.3, ls=DASH)
b.plot(x, np.minimum(e1, e2), color=GREEN, lw=1.4)
b.axvline(1, color=RED, lw=.85)
for cc, col in ((.5, BLUE), (1.5, YELLOW)): dot(b, cc, 0, color=col)
lab(b, .5, .2, '$c_1$', BLUE, ha='center'); lab(b, 1.5, .2, '$c_2$', YELLOW, ha='center')
lab(b, 1.04, 2.2, '$t=1$', RED)
b.set_xlim(-.5, 2.5); b.set_ylim(0, 2.6); b.set_xlabel('$x$', labelpad=1)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'m': m, 'mass': p, 'g_min': cell_mse(0, 1, m), 'g_mid': cell_mse(0, 1, .5)})
