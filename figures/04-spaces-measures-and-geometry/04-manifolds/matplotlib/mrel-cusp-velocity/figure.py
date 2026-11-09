"""Velocity of E(t)=(cos t,sin t), never zero, against beta(t)=(t^2,t^3), whose velocity vanishes at the cusp."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 58
fig, ax = canvas(W, H)
# (a) circle
c = np.array([28., 31.]); r = 16.
th = np.linspace(0, 2*np.pi, 721)
ax.plot(c[0]+r*np.cos(th), c[1]+r*np.sin(th), color=BLUE, lw=1.3, zorder=2)
for t in np.arange(8)*np.pi/4:
    P = c+r*np.array([np.cos(t), np.sin(t)])
    arrow(ax, P, P+6.5*np.array([-np.sin(t), np.cos(t)]), color=RED, lw=1.2, scale=6.5)
    dot(ax, P, INK, size=1.2)
label(ax, c, '$E$', color=BLUE)
panel_tag(ax, 28, 1.6, '(a)')
# (b) cusp, one model unit = s mm
o = np.array([68., 31.]); s = 22.
tt = np.linspace(-1.06, 1.06, 500)
ax.plot(o[0]+s*tt**2, o[1]+s*tt**3, color=BLUE, lw=1.3, zorder=2)
arrow(ax, (o[0]-5, o[1]), (o[0]+33, o[1]), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (o[0], o[1]-24.5), (o[0], o[1]+24.5), color=MUTED, lw=.75, scale=5.5)
label(ax, (o[0]+33, o[1]+2.3), '$y_1$', 7.5, MUTED); label(ax, (o[0]+2.8, o[1]+24.2), '$y_2$', 7.5, MUTED)
k = .12
for t in (-.9, -.6, -.3, .3, .6, .9):
    P = o+s*np.array([t**2, t**3])
    arrow(ax, P, P+s*k*np.array([2*t, 3*t**2]), color=RED, lw=1.2, scale=6.5)
    dot(ax, P, INK, size=1.2)
dot(ax, o, RED, size=1.7)
label(ax, o+[-7.2, 3.2], r"$\beta'(0)=0$", 7.5, RED, halo=True)
label(ax, o+s*np.array([.81, .729])+[10, -1.2], r'$t=0.9$', 7.5, halo=True)
label(ax, o+s*np.array([.81, -.729])+[10.5, 1.2], r'$t=-0.9$', 7.5, halo=True)
panel_tag(ax, 85, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'E(t)=(cos t,sin t), unit velocities; beta(t)=(t^2,t^3), velocity (2t,3t^2) drawn at 0.12 of true length'})
