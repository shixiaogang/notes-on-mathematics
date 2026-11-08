"""Constant-rank normal form for F(x1,x2)=(x1+x2,(x1+x2)^2): the square T F G^{-1}, tracking (1,2)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 92
fig, ax = canvas(W, H)
class Pan:
    def __init__(s, ox, oy, sx, sy): s.o, s.sx, s.sy = np.array([ox, oy], float), sx, sy
    def __call__(s, x, y): return np.c_[s.o[0]+s.sx*np.asarray(x, float), s.o[1]+s.sy*np.asarray(y, float)]
    def pt(s, x, y): return s(np.array([x]), np.array([y]))[0]
def axes(P, xr, yr, xn, yn):
    arrow(ax, P.pt(xr[0], 0), P.pt(xr[1], 0), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, P.pt(0, yr[0]), P.pt(0, yr[1]), color=MUTED, lw=.75, scale=5.5)
    label(ax, P.pt(xr[1], 0)+[-1, 2.4], xn, 7.5, MUTED)
    label(ax, P.pt(0, yr[1])+[3.2, -1.2], yn, 7.5, MUTED)
cs = [-2, -1, 0, 1, 2, 3]
cols = [PURPLE, RED, YELLOW, GREEN, MUTED, BLUE]
s_ = 5.6
A = Pan(22, 71, s_, s_)
axes(A, (-3.6, 3.8), (-3.1, 3.7), '$x_1$', '$x_2$')
for c, col in zip(cs, cols):
    x2 = np.linspace(-2.8, 3.1, 2)
    x2 = np.array([max(-2.8, c-3.1), min(3.1, c+2.8)])
    ax.plot(*A(c-x2, x2).T, color=col, lw=1.2, zorder=3)
dot(ax, A.pt(1, 2), INK, zorder=8); label(ax, A.pt(1, 2)+[-1.8, 3.0], '$(1,2)$', 7.5, halo=True)
B = Pan(22, 21, s_, s_)
axes(B, (-2.9, 4.2), (-3.1, 3.5), '$z_1$', '$z_2$')
for c, col in zip(cs, cols):
    z2 = np.array([-2.8, 3.1])
    ax.plot(*B(np.full(2, c), z2).T, color=col, lw=1.2, zorder=3)
dot(ax, B.pt(3, 2), INK, zorder=8); label(ax, B.pt(3, 2)+[-5, 2.0], '$(3,2)$', 7.5, halo=True)
C = Pan(84, 55, 4.9, 2.85)
axes(C, (-3.6, 4.2), (-.8, 12.2) if False else (-1.2, 12.6), '$y_1$', '$y_2$')
yy = np.linspace(-3.2, 3.5, 300)
ax.plot(*C(yy, yy**2).T, color=STROKE, lw=1.3, zorder=2)
for c, col in zip(cs, cols):
    dot(ax, C.pt(c, c**2), col, size=1.5, zorder=7)
dot(ax, C.pt(3, 9), INK, zorder=8); label(ax, C.pt(3, 9)+[-6.5, 1.0], '$(3,9)$', 7.5, halo=True)
D = Pan(84, 21, 4.9, 4.9)
axes(D, (-3.6, 4.2), (-2.6, 3.0), '$\\tilde y_1$', '$\\tilde y_2$')
ax.plot(*D(np.array([-3.2, 3.5]), np.zeros(2)).T, color=STROKE, lw=1.3, zorder=2)
for c, col in zip(cs, cols):
    dot(ax, D.pt(c, 0), col, size=1.5, zorder=7)
dot(ax, D.pt(3, 0), INK, zorder=8); label(ax, D.pt(3, 0)+[0, 3.1], '$(3,0)$', 7.5, halo=True)
arrow(ax, (45, 72), (63, 72), color=STROKE, lw=.9); label(ax, (54, 75), '$F$')
arrow(ax, (36, 51.5), (36, 42.5), color=STROKE, lw=.9); label(ax, (39.5, 47.2), '$G$')
arrow(ax, (98, 51.2), (98, 42.2), color=STROKE, lw=.9); label(ax, (101.5, 46.8), '$T$')
arrow(ax, (45.5, 21), (63, 21), color=STROKE, lw=.9); label(ax, (54.2, 24.5), r'$T\circ F\circ G^{-1}$', 7.5)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F(x1,x2)=(s,s^2), s=x1+x2; G(x)=(x1+x2,x2); T(y)=(y1,y2-y1^2); level lines s=-2..3'})
