"""E(t)=(cos t,sin t) with the fields d/dt and t d/dt, and the inclusion of (0,1) with (1/t) d/dt."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 54
fig, ax = canvas(W, H)
t0 = -np.pi/2; ks = (-1, 0, 1); ky = 37.5; Rc = 9.5
def base(cx, sc=1.7):
    Lx = 16
    ax.plot([cx-Lx, cx+Lx], [14, 14], color=INK, lw=1.0, zorder=2)
    th = np.linspace(0, 2*np.pi, 361)
    ax.plot(cx+Rc*np.cos(th), ky+Rc*np.sin(th), color=BLUE, lw=1.1, zorder=2)
    for k in ks:
        x = cx+sc*(t0+2*np.pi*k)
        dot(ax, (x, 14), INK, size=1.1)
        ax.plot([x, cx], [14.4, ky-Rc], color=MUTED, lw=.45, ls=(0, (2, 2)), zorder=1)
    label(ax, (cx-sc*np.pi*2+sc*t0, 10.5), r'$t_0\!-\!2\pi$', 7, MUTED)
    label(ax, (cx+sc*t0, 10.5), r'$t_0$', 7, MUTED)
    label(ax, (cx+sc*(t0+2*np.pi), 10.5), r'$t_0\!+\!2\pi$', 7, MUTED)
    return sc
cx = 19.5; sc = base(cx)
for k in ks:
    x = cx+sc*(t0+2*np.pi*k)
    arrow(ax, (x, 16.2), (x+3.2, 16.2), color=RED, lw=1.3, scale=6.5, zorder=7)
top = (cx, ky-Rc)
# d_theta at the bottom of the circle points to the right.
arrow(ax, top, (cx+3.2, ky-Rc), color=RED, lw=1.3, scale=6.5, zorder=7); dot(ax, top, INK, size=1.2, zorder=8)
cx = 56; base(cx)
kv = .8
for k in ks:
    t = t0+2*np.pi*k; x = cx+sc*t
    arrow(ax, (x, 16.2+.0), (x+kv*t, 16.2), color=RED, lw=1.3, scale=6.5, zorder=7)
# the three pushed vectors are at one point; they are spread along the normal so that all are visible
for j, k in enumerate(ks):
    t = t0+2*np.pi*k; y = ky-Rc+1.2+1.9*j
    ax.plot([cx, cx], [ky-Rc, y], color=MUTED, lw=.45, zorder=4)
    arrow(ax, (cx, y), (cx+kv*t, y), color=RED, lw=1.3, scale=6.5, zorder=7)
dot(ax, (cx, ky-Rc), INK, size=1.2, zorder=8)
# (c) inclusion of (0,1) in R
cx = 95; sc = 27
ax.plot([cx-sc*.5, cx+sc*.5], [14, 14], color=INK, lw=1.0, zorder=2)
ax.plot([cx-sc*.5, cx+sc*.5], [34, 34], color=INK, lw=1.0, zorder=2)
ax.plot([cx-sc*.5-4, cx-sc*.5], [34, 34], color=MUTED, lw=.8, ls=(0, (2, 2)), zorder=2)
ax.plot([cx+sc*.5, cx+sc*.5+4], [34, 34], color=MUTED, lw=.8, ls=(0, (2, 2)), zorder=2)
for yy in (14, 34):
    dot(ax, (cx-sc*.5, yy), BLUE, size=1.1, hollow=True, zorder=8); dot(ax, (cx+sc*.5, yy), BLUE, size=1.1, hollow=True, zorder=8)
arrow(ax, (cx, 18), (cx, 30), color=INK, lw=.8, zorder=2)
label(ax, (cx+2.4, 24), r'$\iota$', 8, INK, halo=True)
label(ax, (cx-sc*.5-2.4, 37.6), '?', 8, MUTED); label(ax, (cx+sc*.5+2.4, 37.6), '?', 8, MUTED)
for tt in (.1, .17, .3, .5, .8):
    x = cx-sc*.5+sc*tt; L = 1.25/tt
    for yy in (16.2, 36.2):
        arrow(ax, (x, yy), (x+L, yy), color=RED, lw=1.2, scale=6, zorder=7)
    dot(ax, (x, 14), INK, size=.9); dot(ax, (x, 34), INK, size=.9)
label(ax, (cx-sc*.5, 10.5), '$0$', 7, MUTED); label(ax, (cx+sc*.5, 10.5), '$1$', 7, MUTED)
panel_tag(ax, 19.5, 2.5, '(a)'); panel_tag(ax, 56, 2.5, '(b)'); panel_tag(ax, 95, 2.5, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 't0=-pi/2; d/dt lengths 3.2 mm; t d/dt length .8*t mm; (1/t) d/dt length 1.25/t mm; E(t)=(cos t,sin t), d_theta at (0,-1) is (1,0)'})
