"""F(x)=x^3 is a smooth bijection with non-smooth inverse; the pushforward of d/dx has component 3 y^(2/3)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 96, 44
fig, ax = canvas(W, H)
def axes(ox, oy, xa, ya, xn, yn, sx, sy):
    arrow(ax, (ox+sx*xa[0], oy), (ox+sx*xa[1], oy), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (ox, oy+sy*ya[0]), (ox, oy+sy*ya[1]), color=MUTED, lw=.75, scale=5.5)
    label(ax, (ox+sx*xa[1], oy+2.3), xn, 7.5, MUTED); label(ax, (ox+2.8, oy+sy*ya[1]-.2), yn, 7.5, MUTED)
ox, oy, sx, sy = 25, 23, 13, 13
axes(ox, oy, (-1.6, 1.6), (-1.5, 1.5), '$x$', '$y$', sx, sy)
x = np.linspace(-1.04, 1.04, 400)
ax.plot(ox+sx*x, oy+sy*x**3, color=BLUE, lw=1.4, zorder=4)
ox2, oy2, sx2, sy2 = 71, 8, 13, 8.5
axes(ox2, oy2, (-1.6, 1.6), (-.3, 3.5), '$y$', r'$3y^{2/3}$', sx2, sy2)
y = np.linspace(-1.35, 1.35, 1201)
ax.plot(ox2+sx2*y, oy2+sy2*3*np.abs(y)**(2/3), color=RED, lw=1.4, zorder=4)
dot(ax, (ox2, oy2), INK, zorder=7)
panel_tag(ax, 25, 1.7, '(a)'); panel_tag(ax, ox2, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F(x)=x^3; (F_*X)_y=3 y^(2/3) d/dy'})
