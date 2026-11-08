"""Pullback of 2dy1+dy2 under F(x1,x2)=(x1,x1+x2) is 3dx1+dx2; v=(1,0) goes to Jv=(1,1); both readings are 3."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

from matplotlib.patches import Rectangle
W, H = 104, 54
fig, ax = canvas(W, H)
def panel(x0, y0, a, b, v, xn, yn, vlab):
    s = 22
    xr, yr = (-.2, 1.65), (-.25, 1.55)
    O = np.array([x0, y0])
    rect = Rectangle((x0+s*xr[0], y0+s*yr[0]), s*(xr[1]-xr[0]), s*(yr[1]-yr[0]), transform=ax.transData)
    for k in range(-4, 11):
        x = np.array([-3.0, 6.0])
        if abs(b) > 1e-9:
            y = (k-a*x)/b
        line, = ax.plot(x0+s*x, y0+s*y, color=PURPLE, lw=(1.05 if 0 <= k <= 3 else .55), zorder=2)
        line.set_clip_path(rect)
    for k in range(4):
        label(ax, (x0+s*(k-b*yr[0])/a, y0+s*yr[0]-2.1), str(k), 7, PURPLE)
    arrow(ax, O+[s*xr[0]-1, 0], O+[s*xr[1]+1, 0], color=MUTED, lw=.75, scale=5.5)
    arrow(ax, O+[0, s*yr[0]-1], O+[0, s*yr[1]+1], color=MUTED, lw=.75, scale=5.5)
    label(ax, O+[s*xr[1]+1, 2.3], xn, 7.5, MUTED); label(ax, O+[2.8, s*yr[1]+.8], yn, 7.5, MUTED)
    arrow(ax, O, O+s*np.array(v), color=RED, lw=1.5, scale=7.5, zorder=8)
    dot(ax, O, INK, zorder=9)
    label(ax, O+s*np.array(v)+[3.8, -2.2], vlab, 7.5, RED, halo=True)
panel(10, 13, 3, 1, (1, 0), '$x_1$', '$x_2$', '$(1,0)$')
panel(60, 13, 2, 1, (1, 1), '$y_1$', '$y_2$', '$(1,1)$')
arrow(ax, (54.5, 33), (46.8, 33), color=INK, lw=.8); label(ax, (50.6, 36.2), r'$F^*$')
panel_tag(ax, 28, 1.7, '(a)'); panel_tag(ax, 78, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F(x1,x2)=(x1,x1+x2); b=(2,1); a=J^T b=(3,1); v=(1,0), Jv=(1,1); a.v=b.Jv=3'})
