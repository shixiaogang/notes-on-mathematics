"""X=tanh(x) d/dx on the line and its divergence sech^2 x, whose integral is 2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 96, 42
fig, ax = canvas(W, H)
x0, y0 = 48, 15; sx, sy = 10.5, 10.5
F = lambda x, y: np.c_[np.atleast_1d(x0+sx*x), np.atleast_1d(y0+sy*y)]
for x in np.arange(-3.5, 3.6, .875):
    if abs(x) < .1: continue
    v = np.tanh(x); arrow(ax, (x0+sx*x, 37), (x0+sx*(x+.72*v), 37), color=RED, lw=1.0, scale=5.5, zorder=3)
ax.plot([x0-sx*4.1, x0+sx*4.1], [37, 37], color=MUTED, lw=.7, zorder=1)
dot(ax, (x0, 37), RED, size=1.0)
x = np.linspace(-4, 4, 500)
y = 1/np.cosh(x)**2
ax.fill_between(x0+sx*x, y0, y0+sy*y, color=GREEN_FILL, lw=0, zorder=1)
ax.plot(*F(x, y).T, color=GREEN, lw=1.4, zorder=3)
ax.plot(*F(x, np.tanh(x)*0.92).T, color=BLUE, lw=0, zorder=0)
ax.plot(*F(x, np.tanh(x)).T, color=BLUE, lw=1.4, zorder=3)
arrow(ax, F(-4.2, 0)[0], F(4.2, 0)[0], color=MUTED, lw=.75, scale=5.5); label(ax, F(4.2, 0)[0]+[-.8, 2.2], '$x$', 7.5, MUTED)
arrow(ax, F(0, -.75)[0], F(0, 1.25)[0], color=MUTED, lw=.75, scale=5.5)
for v, n in ((1, '$1$'), (-1, '$-1$')):
    ax.plot([x0-1, x0+1], [F(0, v)[0, 1]]*2, color=MUTED, lw=.75); label(ax, (x0+3.0 if v<0 else x0-3.6, F(0, v)[0, 1]), n, 7.5, MUTED)
ax.plot(*F(np.array([-4, 4.]), np.ones(2)).T, color=BLUE, lw=.55, ls=(0, (2.2, 1.8)))
ax.plot(*F(np.array([-4, 4.]), -np.ones(2)).T, color=BLUE, lw=.55, ls=(0, (2.2, 1.8)))
label(ax, F(2.8, 1)[0]+[0, -2.6], r'$\tanh x$', 7.5, BLUE, halo=True)
label(ax, F(-1.6, .55)[0]+[-5, 3], r'$\operatorname{sech}^2 x$', 7.5, GREEN, halo=True)
label(ax, F(0, .5)[0]+[8, -1.5], '$2$', 8, GREEN, halo=True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'X=tanh x, div X=sech^2 x, integral over R equals 2'})
