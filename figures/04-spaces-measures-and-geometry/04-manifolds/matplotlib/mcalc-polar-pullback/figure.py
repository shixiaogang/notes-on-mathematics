"""Polar map F(r,theta): a coordinate cell, its image, the forward push of tangent vectors and the backward pull of the area form."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
# (a) (r,theta) coordinates, r in [1,2.5], theta in [0,pi/2]
A = lambda r, t: np.c_[np.atleast_1d(9+12*(r-.5)), np.atleast_1d(10+21*t)]
R = [1, 2.5]; T = [0, np.pi/2]
ax.add_patch(Polygon(np.r_[A(R[0], T[0]), A(R[1], T[0]), A(R[1], T[1]), A(R[0], T[1])], fc=BLUE_FILL, ec=BLUE, lw=.95, zorder=1))
for r in (1.5, 2.0):
    ax.plot(*A(np.full(2, r), np.array(T)).T, color=BLUE, lw=.55, zorder=2)
for t in (np.pi/8, np.pi/4, 3*np.pi/8):
    ax.plot(*A(np.array(R), np.full(2, t)).T, color=BLUE, lw=.55, zorder=2)
r0, t0, h = 2.0, np.pi/6, .25
cell = np.r_[A(r0, t0), A(r0+h, t0), A(r0+h, t0+h), A(r0, t0+h)]
ax.add_patch(Polygon(cell, fc=YELLOW_FILL, ec=YELLOW, lw=1.0, zorder=3))
P = A(r0, t0)[0]
arrow(ax, P, A(r0+.6, t0)[0], color=RED, lw=1.3, scale=7, zorder=8)
arrow(ax, P, A(r0, t0+.6)[0], color=GREEN, lw=1.3, scale=7, zorder=8)
label(ax, A(r0+.6, t0)[0]+[3.0, -1.4], r'$\partial_r$', color=RED, halo=True)
label(ax, A(r0, t0+.6)[0]+[-2.6, 1.4], r'$\partial_\theta$', color=GREEN, halo=True)
arrow(ax, (9, 10), (9+12*2.3, 10), color=MUTED, lw=.75, scale=5.5); label(ax, (9+12*2.3+1.5, 12.1), '$r$', 7.5, MUTED)
arrow(ax, (9, 10), (9, 10+21*1.72), color=MUTED, lw=.75, scale=5.5); label(ax, (6.7, 10+21*1.72), r'$\theta$', 7.5, MUTED)
for r in R:
    label(ax, A(r, 0)[0]+[0, -2.6], {1: '$1$', 2.5: r'$\frac{5}{2}$'}[r], 7.5, MUTED)
label(ax, A(.5, np.pi/2)[0]+[-2.2, 0], r'$\frac{\pi}{2}$', 7.5, MUTED)
panel_tag(ax, 26, 2.0, '(a)')
# (b) plane
B = lambda x, y: np.c_[np.atleast_1d(70+12.6*x), np.atleast_1d(9+12.6*y)]
pol = lambda r, t: B(r*np.cos(t), r*np.sin(t))
tt = np.linspace(0, np.pi/2, 121)
reg = np.r_[pol(1, tt), pol(2.5, tt[::-1])]
ax.add_patch(Polygon(reg, fc=BLUE_FILL, ec=BLUE, lw=.95, zorder=1))
for r in (1.5, 2.0):
    ax.plot(*pol(r, tt).T, color=BLUE, lw=.55, zorder=2)
for t in (np.pi/8, np.pi/4, 3*np.pi/8):
    rr = np.linspace(1, 2.5, 2); ax.plot(*pol(rr, np.full(2, t)).T, color=BLUE, lw=.55, zorder=2)
rs = np.linspace(r0, r0+h, 30); ts = np.linspace(t0, t0+h, 30)
imag = np.r_[pol(rs, np.full(30, t0)), pol(np.full(30, r0+h), ts), pol(rs[::-1], np.full(30, t0+h)), pol(np.full(30, r0), ts[::-1])]
ax.add_patch(Polygon(imag, fc=YELLOW_FILL, ec=YELLOW, lw=1.0, zorder=3))
Q = pol(r0, t0)[0]
er, et = np.array([np.cos(t0), np.sin(t0)]), np.array([-np.sin(t0), np.cos(t0)])
arrow(ax, Q, Q+.6*12.6*er, color=RED, lw=1.3, scale=7, zorder=8)
arrow(ax, Q, Q+.6*12.6*2*et, color=GREEN, lw=1.3, scale=7, zorder=8)
label(ax, Q+.6*12.6*er+[3.8, .3], r'$\mathrm{d}F(\partial_r)$', 7.5, RED, halo=True)
label(ax, Q+.6*12.6*2*et+[-3, 2.0], r'$\mathrm{d}F(\partial_\theta)$', 7.5, GREEN, halo=True)
arrow(ax, (70, 9), (70+12.6*2.85, 9), color=MUTED, lw=.75, scale=5.5); label(ax, (70+12.6*2.85+1.2, 11.1), '$x_1$', 7.5, MUTED)
arrow(ax, (70, 9), (70, 9+12.6*2.95), color=MUTED, lw=.75, scale=5.5); label(ax, (67.5, 9+12.6*2.95-.5), '$x_2$', 7.5, MUTED)
panel_tag(ax, 88, 2.0, '(b)')
# direction arrows between panels
arrow(ax, (46, 33), (62, 33), color=STROKE, lw=.9, scale=6.5); label(ax, (54, 35.3), '$F$')
arrow(ax, (62, 21), (46, 21), color=PURPLE, lw=.9, scale=6.5); label(ax, (54, 23.3), '$F^{*}$', color=PURPLE)
label(ax, (54, 18.3), r'$\mathrm{d}x_1\wedge\mathrm{d}x_2$', 7.5, PURPLE)
label(ax, (54, 14.6), r'$\mapsto r\,\mathrm{d}r\wedge\mathrm{d}\theta$', 7.5, PURPLE)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F(r,theta)=(r cos theta, r sin theta); cell [2,2.25]x[pi/6,pi/6+0.25]; arrows 0.6*dF(d_r), 0.6*dF(d_theta), dF(d_theta) has length r=2'})
