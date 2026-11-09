"""Pullback of d theta along E: reading lines on the circle pull back to equally spaced lines on R; t is not a function on the circle."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 52
fig, ax = canvas(W, H)
sc = 3.5; x0 = 3.5; yL = 13
ax.plot([x0-.5, x0+4*np.pi*sc+.5], [yL, yL], color=INK, lw=1.0, zorder=3)
cx = x0+2*np.pi*sc; cy = 37; R = 9.5
th = np.linspace(0, 2*np.pi, 361)
ax.plot(cx+R*np.cos(th), cy+R*np.sin(th), color=BLUE, lw=1.1, zorder=3)
for k in range(12):
    a = k*np.pi/6
    ax.plot([cx+(R-2.2)*np.cos(a), cx+(R+2.2)*np.cos(a)], [cy+(R-2.2)*np.sin(a), cy+(R+2.2)*np.sin(a)], color=PURPLE, lw=.75, zorder=2)
for k in range(25):
    x = x0+k*np.pi/6*sc
    ax.plot([x, x], [yL-2.0, yL+2.0], color=PURPLE, lw=.75, zorder=2)
t0 = 3*np.pi/2
for t in (t0, t0+2*np.pi):
    x = x0+t*sc
    dot(ax, (x, yL), INK, zorder=8)
    arrow(ax, (x, yL+2.6), (cx+(-.0)*R, cy-R-3.0), color=MUTED, lw=.55, scale=5, zorder=1)
dot(ax, (cx, cy-R), INK, zorder=8)
label(ax, (x0+t0*sc, yL-4.4), r'$t_0$', 7.5); label(ax, (x0+(t0+2*np.pi)*sc, yL-4.4), r'$t_0+2\pi$', 7.5)
label(ax, (cx+12.7, cy-R+.5), r'$E(t_0)$', 7.5, halo=True)
ox, oy, s = 72, 7.5, 2.85
arrow(ax, (ox-1, oy), (ox+4*np.pi*s+3, oy), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (ox, oy-1), (ox, oy+4*np.pi*s+3), color=MUTED, lw=.75, scale=5.5)
label(ax, (ox+4*np.pi*s+3, oy+2.3), '$t$', 7.5, MUTED)
ax.plot([ox, ox+4*np.pi*s], [oy, oy+4*np.pi*s], color=BLUE, lw=1.4, zorder=4)
for t, lab in ((t0, r'$t_0$'), (t0+2*np.pi, r'$t_0+2\pi$')):
    x, y = ox+t*s, oy+t*s
    ax.plot([x, x], [oy, y], color=MUTED, lw=.55, ls=(0, (2, 2)), zorder=2)
    ax.plot([ox, x], [y, y], color=MUTED, lw=.55, ls=(0, (2, 2)), zorder=2)
    dot(ax, (x, y), INK, zorder=8)
    label(ax, (ox-1.2, y), lab, 7, MUTED, ha='right', halo=True)
panel_tag(ax, cx, 1.7, '(a)'); panel_tag(ax, 88, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'E(t)=(cos t,sin t); ticks at k pi/6; primitive of E^*(d theta)=dt is t, not 2 pi periodic; t0=3 pi/2'})
