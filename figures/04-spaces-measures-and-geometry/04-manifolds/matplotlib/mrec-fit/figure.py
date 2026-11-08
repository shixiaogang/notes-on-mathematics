"""Quadratic fit on the unit circle (h=.5), its residual, and a zigzag with small values and large slopes."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 46
fig, ax = canvas(W, H)
def inset(x, y, w, h):
    a = fig.add_axes([x/W, y/H, w/W, h/H]); a.spines[['top', 'right']].set_visible(False); a.tick_params(length=2, width=.75, pad=1.5); return a
R, h = 1., .5
c = R-np.sqrt(R*R-h*h); k = c/h**2
print('c=', c, 'k=', k)
g = lambda u: R-np.sqrt(R*R-u*u); q = lambda u: k*u*u
a = inset(9, 12.5, 26, 31)
u = np.linspace(-.8, .8, 321)
a.plot(u, g(u), color=BLUE, lw=1.4); a.plot(u, q(u), color=GREEN, lw=1.2, ls=(0, (4, 2)))
a.plot([-h, 0, h], [c, 0, c], 'o', ms=3.2, mfc=INK, mec=INK)
a.set_xlim(-.8, .8); a.set_ylim(-.02, .42); a.set_xticks([-.5, 0, .5], ['$-0.5$', '$0$', '$0.5$']); a.set_yticks([0, .2, .4], ['$0$', '$0.2$', '$0.4$']); a.set_xlabel('$u$', labelpad=.5)
a.text(-.72, .40, r'$\widetilde g$', color=BLUE, fontsize=8); a.text(.66, .13, '$g$', color=GREEN, fontsize=8)
b = inset(46, 12.5, 27, 31)
u = np.linspace(-.5, .5, 321)
b.plot(u, (g(u)-q(u))*1e3, color=RED, lw=1.4)
b.axhline(0, color=MUTED, lw=.75)
b.set_xlim(-.55, .55); b.set_ylim(-2.7, .4); b.set_xticks([-.5, 0, .5], ['$-0.5$', '$0$', '$0.5$']); b.set_yticks([-2, -1, 0], ['$-2$', '$-1$', '$0$']); b.set_xlabel('$u$', labelpad=.5); b.set_ylabel(r'$\widetilde g-g\ (\times 10^{-3})$', labelpad=.5)
print('min res', (g(u)-q(u)).min(), 'at', u[(g(u)-q(u)).argmin()])
cc = inset(83, 12.5, 27, 31)
s, sg = .1, .05
xk = np.arange(0, .8+1e-9, s); wk = sg*(-1)**np.arange(len(xk))
cc.plot([0, .8], [0, 0], color=BLUE, lw=1.4)
cc.plot(xk, wk, color=RED, lw=1.0, marker='o', ms=2.6, mfc=INK, mec=INK)
cc.set_xlim(0, .8); cc.set_ylim(-.13, .13); cc.set_xticks([0, .4, .8], ['$0$', '$0.4$', '$0.8$']); cc.set_yticks([-.05, 0, .05], [r'$-\sigma$', '$0$', r'$\sigma$']); cc.set_xlabel('$u$', labelpad=.5)
panel_tag(ax, 22, 1.4, '(a)'); panel_tag(ax, 59.5, 1.4, '(b)'); panel_tag(ax, 96.5, 1.4, '(c)')
save(fig, OUT, 'figure', {'formula': 'R=1,h=.5; g=R-sqrt(R^2-u^2), fit k u^2, k=c/h^2; zigzag spacing s=.1 amplitude sigma=.05'})
