"""f=r^2 at (2,0): coordinate circle versus straight-line geodesic, and f along each."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 100, 48
fig, ax = canvas(W, H)
c = np.array([20., 25.]); s = 8.2
A = lambda x, y: np.c_[np.atleast_1d(c[0]+s*x), np.atleast_1d(c[1]+s*y)]
t = np.linspace(-2.9, 2.9, 300)
ax.plot(*A(2*np.cos(t/2)*1.0, 2*np.sin(t/2)).T, color=BLUE, lw=1.4, zorder=3)
th = np.linspace(0, 2*np.pi, 361)
for r in (1, 2, 2.6):
    ax.plot(*A(r*np.cos(th), r*np.sin(th)).T, color=PURPLE, lw=.5, ls=(0, (2.2, 1.8)), zorder=1)
ax.plot(*A(np.full(2, 2.), np.array([-2.2, 2.2])).T, color=GREEN, lw=1.4, zorder=3)
P = A(2, 0)[0]
arrow(ax, P, P+[0, s], color=RED, lw=1.4, scale=7.5, zorder=8)
dot(ax, P, INK, size=1.3, zorder=9)
label(ax, P+[2.4, s+.5], r'$\bm{v}$'.replace(r'\bm{v}', 'v'), color=RED, halo=True)
label(ax, P+[2.6, -2.2], '$(2,0)$', 7.5, halo=True)
label(ax, A(.75, 2.1)[0]+[0,.8], r'$\gamma$', color=BLUE, halo=True)
label(ax, A(2.3, -2.0)[0], r'$\ell$', color=GREEN, halo=True)
arrow(ax, A(-2.7, 0)[0], A(3.1, 0)[0], color=MUTED, lw=.7, scale=5, zorder=1); arrow(ax, A(0, -2.7)[0], A(0, 2.7)[0], color=MUTED, lw=.7, scale=5, zorder=1)
panel_tag(ax, c[0]+2, 1.2, '(a)')
x0, y0 = 62, 10; sx, sy = 11, 4.0
G = lambda t, v: np.c_[x0+sx*(t+1.5), y0+sy*(v-3.2)]
arrow(ax, G(-1.5, 3.2)[0], G(1.7, 3.2)[0], color=MUTED, lw=.75, scale=5.5); arrow(ax, G(-1.5, 3.2)[0], G(-1.5, 6.6)[0]+[0, 8], color=MUTED, lw=.75, scale=5.5)
label(ax, G(1.7, 3.2)[0]+[.6, 2.2], '$t$', 7.5, MUTED)
tt = np.linspace(-1.5, 1.5, 200)
ax.plot(*G(tt, 4+tt**2).T, color=GREEN, lw=1.4, zorder=3)
ax.plot(*G(tt, 4+0*tt).T, color=BLUE, lw=1.4, zorder=3)
ax.plot([G(0, 3.2)[0, 0]]*2, [y0-1, y0+1], color=MUTED, lw=.75); label(ax, G(0, 3.2)[0]+[0, -2.8], '$0$', 7.5, MUTED)
ax.plot([x0-1, x0+1], [G(-1.5, 4)[0, 1]]*2, color=MUTED, lw=.75); label(ax, G(-1.5, 4)[0]+[-2.6, 0], '$4$', 7.5, MUTED)
label(ax, G(1.1, 6.6)[0]+[0, 2.0], r'$f\circ\ell$', 7.5, GREEN, halo=True)
label(ax, G(1.1, 4)[0]+[0, 2.6], r'$f\circ\gamma$', 7.5, BLUE, halo=True)
panel_tag(ax, x0+sx*1.5, 1.2, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=r^2; gamma(t)=2(cos(t/2),sin(t/2)), l(t)=(2,t); f(gamma)=4, f(l)=4+t^2'})
