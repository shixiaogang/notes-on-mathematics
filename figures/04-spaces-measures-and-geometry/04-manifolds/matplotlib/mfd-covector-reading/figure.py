"""A covector drawn as level lines: the same reading of the same vector in two coordinate systems."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

from matplotlib.patches import Rectangle
W, H = 92, 50
fig, ax = canvas(W, H)
def panel(ox, oy, s, xr, yr, a, v, xn, yn):
    win = Rectangle((ox+s*xr[0], oy+s*yr[0]), s*(xr[1]-xr[0]), s*(yr[1]-yr[0]), transform=ax.transData)
    xs = np.array(xr)
    for c in range(-6, 12):
        # level line a1 x + a2 y = c intersected with a wide x-range
        X = np.array([xr[0]-3, xr[1]+3]); Y = (c-a[0]*X)/a[1]
        strong = 0 <= c <= 3
        line, = ax.plot(ox+s*X, oy+s*Y, color=PURPLE, lw=.95 if strong else .5, zorder=2)
        line.set_clip_path(win)
    arrow(ax, (ox+s*xr[0], oy), (ox+s*xr[1]+2, oy), color=MUTED, lw=.75, scale=5.5, zorder=3)
    arrow(ax, (ox, oy+s*yr[0]), (ox, oy+s*yr[1]+2), color=MUTED, lw=.75, scale=5.5, zorder=3)
    label(ax, (ox+s*xr[1]+1, oy-2.4), xn, 7.5, MUTED); label(ax, (ox-2.6, oy+s*yr[1]+1.5), yn, 7.5, MUTED)
    arrow(ax, (ox, oy), (ox+s*v[0], oy+s*v[1]), color=RED, lw=1.6, scale=8, zorder=6)
    dot(ax, (ox, oy), INK); 
ox1, oy1 = 8, 12
panel(ox1, oy1, 15.5, (-.25, 1.95), (-.25, 2.0), (2, 1), (1, 1), '$x_1$', '$x_2$')
ox2, oy2 = 56, 12
panel(ox2, oy2, 13.0, (-.2, 2.2), (-.25, 2.35), (4, .5), (.5, 2), r'$\tilde{x}_1$', r'$\tilde{x}_2$')
label(ax, (ox1+15.5-8.8, oy1+15.5+1.6), r'$v=(1,1)$', 7.5, RED, halo=True)
label(ax, (ox2+6.5+10.5, oy2+26+.6), r'$\tilde{v}=(\frac{1}{2},2)$', 7.5, RED, halo=True)
panel_tag(ax, ox1+13, 2, '(a)'); panel_tag(ax, ox2+13, 2, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'omega=2dx1+dx2, level lines at integers; v=(1,1); J=diag(1/2,2); tilde a=(4,1/2); tilde v=(1/2,2); reading 3 in both'})
