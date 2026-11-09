"""Chord against arc on the unit circle: 2 sin(t/2) and t."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 104, 50
fig, ax = canvas(W, H)
c = np.array([23.0, 26.0]); u = 17.5
t = np.linspace(0, 2*np.pi, 361)
ax.plot(c[0]+u*np.cos(t), c[1]+u*np.sin(t), color=STROKE, lw=.95, zorder=2)
a = np.linspace(0, np.pi/2, 91)
ax.plot(c[0]+u*np.cos(a), c[1]+u*np.sin(a), color=BLUE, lw=1.5, zorder=3)
P, Q = c+[u, 0], c+[0, u]
ax.plot(*np.array([P, Q]).T, color=RED, lw=1.4, zorder=3)
ax.plot(*np.array([c, P]).T, color=MUTED, lw=.75, ls=(0, (3, 2)), zorder=2); ax.plot(*np.array([c, Q]).T, color=MUTED, lw=.75, ls=(0, (3, 2)), zorder=2)
b = np.linspace(0, np.pi/2, 31)
ax.plot(c[0]+5.2*np.cos(b), c[1]+5.2*np.sin(b), color=MUTED, lw=.8, zorder=3)
dot(ax, P, INK); dot(ax, Q, INK); dot(ax, c, INK, size=.9)
label(ax, P+[3.0, -1], '$p$', halo=True); label(ax, Q+[0, 3.0], '$q$', halo=True)
label(ax, c+[2.4, 2.2], r'$\vartheta$', 7.5, MUTED)
label(ax, c+.5*(P+Q-2*c)+[-4.2, -2.6], r'$\sqrt{2}$', color=RED, halo=True)
label(ax, c+[u*.91, u*.91], r'$\pi/2$', color=BLUE)
panel_tag(ax, c[0], 3, '(a)')
x0, y0, sx, sy = 58.0, 10.0, 13.2, 10.5
arrow(ax, (x0-1, y0), (x0+3.4*sx, y0), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (x0, y0-1), (x0, y0+3.45*sy), color=MUTED, lw=.75, scale=5.5)
th = np.linspace(0, np.pi, 241)
ax.plot(x0+sx*th, y0+sy*th, color=BLUE, lw=1.4, zorder=3)
ax.plot(x0+sx*th, y0+sy*2*np.sin(th/2), color=RED, lw=1.4, zorder=3)
for v, n in ((np.pi/2, r'$\pi/2$'), (np.pi, r'$\pi$')):
    ax.plot([x0+sx*v]*2, [y0, y0+sy*v], color=GRID, lw=.85, zorder=1)
    ax.plot([x0+sx*v]*2, [y0-.9, y0], color=MUTED, lw=.8)
    label(ax, (x0+sx*v, y0-3.0), n, 7.5, MUTED)
dot(ax, (x0+sx*np.pi/2, y0+sy*np.pi/2), BLUE, size=1.2); dot(ax, (x0+sx*np.pi/2, y0+sy*2*np.sin(np.pi/4)), RED, size=1.2)
label(ax, (x0+sx*2.25, y0+sy*2.75), r'$d_g=\vartheta$', color=BLUE, halo=True)
label(ax, (x0+sx*2.65, y0+sy*1.55), r'$2\sin(\vartheta/2)$', color=RED, halo=True)
label(ax, (x0+3.45*sx, y0+2.2), r'$\vartheta$', 7.5, MUTED)
panel_tag(ax, x0+sx*1.6, 3, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'intrinsic distance t and chord 2 sin(t/2), t in [0,pi]'})
