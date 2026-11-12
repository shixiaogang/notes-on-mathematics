from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Two-point quantizer for X ~ Laplace(0,1): cells S1=(-inf,0), S2=[0,inf), points c1=-1, c2=+1.
# (a) density with the two cells and the reconstruction points; (b) the map Q(x) against y=x.
x = np.linspace(-4.5, 4.5, 901)
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
panel(fig, left=.09, right=.98, bottom=.27, top=.95, wspace=.3)
a.fill_between(x[x < 0], 0, pdf(x[x < 0]), color=BLUE_FILL, lw=0)
a.fill_between(x[x >= 0], 0, pdf(x[x >= 0]), color=GREEN_FILL, lw=0)
a.plot(x, pdf(x), color=BLUE, lw=1.4)
a.axvline(0, color=STROKE, lw=.85, ls=DASH)
for c in (-1, 1): dot(a, c, 0)
lab(a, -1, .035, '$c_1=-1$', RED, ha='center'); lab(a, 1, .035, '$c_2=1$', RED, ha='center')
lab(a, -3.3, .16, '$S_1$', BLUE); lab(a, 2.8, .16, '$S_2$', GREEN)
lab(a, 1.6, .38, r'$f(x)=\frac{1}{2}\mathrm{e}^{-|x|}$', BLUE)
a.set_xlim(-4.5, 4.5); a.set_ylim(0, .55); a.set_yticks([0, .25, .5]); a.set_xlabel('$x$', labelpad=1)
b.plot(x, x, color=STROKE, lw=.85, ls=DOT)
b.plot(x[x < 0], -np.ones((x < 0).sum()), color=GREEN, lw=1.4)
b.plot(x[x >= 0], np.ones((x >= 0).sum()), color=GREEN, lw=1.4)
b.axhline(0, color=STROKE, lw=.6); b.axvline(0, color=STROKE, lw=.6)
lab(b, 2.2, 1.25, '$Q(x)$', GREEN); lab(b, 2.4, 3.0, '$y=x$', MUTED)
b.set_xlim(-4.5, 4.5); b.set_ylim(-4, 4); b.set_xlabel('$x$', labelpad=1)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'D': mse([0], [-1, 1]), 'centroid': cmean(0, math.inf)})
