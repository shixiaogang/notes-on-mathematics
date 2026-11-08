"""Angle form on the punctured plane: its dual field, the unit circle, and the angle along the loop versus a single-valued branch."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 52
fig, ax = canvas(W, H)
# (a) rays of constant angle and tangent arrows -y,x / r^2
c = np.array([27., 28.]); s = 10.0
for a in np.arange(0, 2*np.pi, np.pi/6):
    d = np.array([np.cos(a), np.sin(a)])
    ax.plot(*zip(c+s*.28*d, c+s*2.2*d), color=PURPLE, lw=.55, zorder=1)
th = np.linspace(0, 2*np.pi, 241)
ax.plot(c[0]+s*np.cos(th), c[1]+s*np.sin(th), color=BLUE, lw=1.4, zorder=3)
for r in (.72, 1.42, 2.0):
    for a in np.arange(np.pi/8, 2*np.pi, np.pi/4):
        p = np.array([r*np.cos(a), r*np.sin(a)]); v = np.array([-p[1], p[0]])/r**2
        arrow(ax, c+s*p, c+s*(p+.3*v), color=RED, lw=.8, scale=5, zorder=5)
dot(ax, c, 'white', hollow=True, size=1.6)
ax.plot([c[0]], [c[1]], 'o', ms=3.3, mfc='white', mec=RED, mew=.85, zorder=8)
label(ax, c+[s*.74+2.3, -s*.72-1.3], '$c$', color=BLUE, halo=True)
panel_tag(ax, c[0], 1.7, '(a)')
# (b) lifted angle along the loop vs a principal branch
x0, y0 = 68, 14; sx, sy = 9.6/ (2*np.pi)*2.2, 1.45
A = lambda t, y: np.c_[x0+sx*t, y0+sy*y]
arrow(ax, A(0, 0)[0], A(13.6, 0)[0], color=MUTED, lw=.75, scale=5.5); label(ax, A(13.8, 0)[0]+[.5, 2.2], '$t$', 7.5, MUTED)
arrow(ax, A(0, -4.6)[0], A(0, 14.2)[0], color=MUTED, lw=.75, scale=5.5)
t = np.linspace(0, 4*np.pi, 500)
ax.plot(*A(t, t).T, color=BLUE, lw=1.4, zorder=3)
br = (t+np.pi) % (2*np.pi)-np.pi
idx = np.flatnonzero(np.abs(np.diff(br)) > 1)
for a, b in zip(np.r_[0, idx+1], np.r_[idx+1, len(t)]):
    ax.plot(*A(t[a:b], br[a:b]).T, color=RED, lw=1.4, ls='--', zorder=3)
for k, nam in ((2*np.pi, r'$2\pi$'), (4*np.pi, r'$4\pi$')):
    ax.plot([A(k, 0)[0, 0]]*2, [y0-1, y0+1], color=MUTED, lw=.75); label(ax, A(k, 0)[0]+[0, -2.8], nam, 7.5, MUTED)
ax.plot([x0-1, x0+1], [A(0, 2*np.pi)[0, 1]]*2, color=MUTED, lw=.75); label(ax, (x0-3.2, A(0, 2*np.pi)[0, 1]), r'$2\pi$', 7.5, MUTED)
ax.plot([x0-1, x0+1], [A(0, 4*np.pi)[0, 1]]*2, color=MUTED, lw=.75); label(ax, (x0-3.2, A(0, 4*np.pi)[0, 1]), r'$4\pi$', 7.5, MUTED)
label(ax, A(9.4, 9.4)[0]+[-4.0, 2.2], r'$\int_0^t c^*\omega$', 7.5, BLUE, halo=True)
panel_tag(ax, A(6.3, 0)[0, 0], 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'omega=(x1 dx2-x2 dx1)/(x1^2+x2^2); rays theta=k pi/6; arrows (-x2,x1)/r^2 scaled 0.3; (b) lifted angle t and principal value in (-pi,pi]'})
