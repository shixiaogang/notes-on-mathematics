"""Regularity counterexamples: level sets of y1^2-y2^2, and the two defining functions of the circle along a radius."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 54
fig, ax = canvas(W, H)
c = np.array([27., 29.]); u = 11.5
lim = 1.95
for cv, col, lw in ((-1, MUTED, .7), (-.4, MUTED, .7), (.4, MUTED, .7), (1, MUTED, .7)):
    y2 = np.linspace(-lim, lim, 400)
    if cv > 0:
        y1 = np.sqrt(cv+y2**2)
        keep = y1 <= lim
        for sgn in (1, -1):
            ax.plot(c[0]+u*sgn*y1[keep], c[1]+u*y2[keep], color=col, lw=lw, zorder=2)
    else:
        y1 = np.linspace(-lim, lim, 400)
        yy = np.sqrt(-cv+y1**2)
        keep = yy <= lim
        for sgn in (1, -1):
            ax.plot(c[0]+u*y1[keep], c[1]+u*sgn*yy[keep], color=col, lw=lw, zorder=2)
for sgn in (1, -1):
    ax.plot([c[0]-u*lim, c[0]+u*lim], [c[1]-u*sgn*lim, c[1]+u*sgn*lim], color=RED, lw=1.3, zorder=3)
dot(ax, c, RED, size=1.7, hollow=True)
label(ax, c+u*np.array([1.5, .08]), r'$c=1$', 7.5, MUTED, halo=True)
label(ax, c+u*np.array([.1, 1.45]), r'$c=-1$', 7.5, MUTED, halo=True)
label(ax, c+u*np.array([1.62, .98]), r'$c=0$', 7.5, RED, halo=True)
panel_tag(ax, c[0], 1.6, '(a)')
ox = 67.; oy = 22.; sx = 19.; sy = 15.
r = np.linspace(.0, 1.5, 400)
arrow(ax, (ox-2, oy), (ox+sx*1.8, oy), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (ox, oy-sy*1.1), (ox, oy+sy*1.75), color=MUTED, lw=.75, scale=5.5)
label(ax, (ox+sx*1.8, oy+2.4), '$r$', 7.5, MUTED)
ax.plot(ox+sx*r, oy+sy*(r**2-1), color=BLUE, lw=1.3, zorder=3)
r2 = r[r > .0]
y = (r**2-1)**2
keep = y <= 1.5
ax.plot(ox+sx*r[keep], oy+sy*y[keep], color=GREEN, lw=1.3, zorder=3)
dot(ax, (ox+sx, oy), INK, zorder=8)
label(ax, (ox+sx+.4, oy-3.4), '$1$', 7.5, MUTED)
ax.plot([ox+sx*.65, ox+sx*1.35], [oy+sy*(-.7), oy+sy*.7], color=BLUE, lw=.7, ls=(0, (2.2, 1.8)), zorder=2)
ax.plot([ox+sx*.65, ox+sx*1.35], [oy, oy], color=GREEN, lw=.9, ls=(0, (2.2, 1.8)), zorder=4)
label(ax, (ox+sx*.62, oy-sy*.98), r'$r^2-1$', 7.5, BLUE, halo=True)
label(ax, (ox+sx*.62, oy+sy*.95), r'$(r^2-1)^2$', 7.5, GREEN, halo=True)
panel_tag(ax, ox+sx*.8, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Phi=y1^2-y2^2 at levels -1,-.4,0,.4,1; along a radius r: r^2-1 and (r^2-1)^2, slopes at r=1 are 2 and 0'})
