"""Coverage by delta-discs, stripes that are dense but direction-deficient, and bounded observation noise."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 48
fig, ax = canvas(W, H)
# (a) closed curve r(t)=1+.25 cos 3t, samples equally spaced in arc length; delta is computed.
t = np.linspace(0, 2*np.pi, 6001)
rad = 1+.25*np.cos(3*t)
c = np.stack([rad*np.cos(t), rad*np.sin(t)], 1)
s = np.r_[0, np.cumsum(np.linalg.norm(np.diff(c, axis=0), axis=1))]
n = 14
idx = [np.argmin(np.abs(s-v)) for v in np.linspace(0, s[-1], n, endpoint=False)]
P = c[idx]
delta = np.max(np.min(np.linalg.norm(c[:, None]-P[None], axis=2), axis=1))
u = 11.5; o = np.array([20, 27])
for p in P:
    ax.add_patch(Circle(o+u*p, u*delta, fc=BLUE_FILL, ec='none', zorder=1))
ax.plot(*(o+u*c).T, color=BLUE, lw=1.3, zorder=3)
for p in P:
    dot(ax, o+u*p, INK, size=.9)
q = P[3]; d = np.array([np.cos(.9), np.sin(.9)])
ax.add_patch(Circle(o+u*q, u*delta, fc='none', ec=MUTED, lw=.7, zorder=4))
ax.plot(*zip(o+u*q, o+u*(q+delta*d)), color=INK, lw=.8, zorder=5)
label(ax, o+u*(q+delta*d)+(2.8, 1.4), r'$\delta_P$', 7.5, MUTED)
label(ax, o+(0, 0), '$M$', 8, BLUE)
panel_tag(ax, 20, 1.4, '(a)')
# (b) flat patch; three horizontal lines v=1/6,1/2,5/6, spacing 1/24 along each line.
x0, y0, S = 44, 9.5, 33
ax.add_patch(Polygon([(x0, y0), (x0+S, y0), (x0+S, y0+S), (x0, y0+S)], fc=BLUE_FILL, ec='none', zorder=1))
ax.plot([x0, x0+S, x0+S, x0, x0], [y0, y0, y0+S, y0+S, y0], color=STROKE, lw=.75, zorder=2)
X = lambda a: x0+a*S; Y = lambda a: y0+a*S
uu = np.arange(0, 1+1e-9, 1/24)
for v in (1/6, 1/2, 5/6):
    ax.plot(X(uu), np.full_like(uu, Y(v)), 'o', ms=1.5, mfc=INK, mec=INK, mew=0, zorder=3)
cu, cv, r = 12/24, 1/2, .25
th = np.linspace(0, 2*np.pi, 241)
ax.plot(X(cu+r*np.cos(th)), Y(cv+r*np.sin(th)), color=RED, lw=1.1, zorder=4)
sel = uu[np.abs(uu-cu) <= r+1e-9]
ax.plot(X(sel), np.full_like(sel, Y(cv)), 'o', ms=2.1, mfc=RED, mec=RED, mew=0, zorder=5)
ax.plot(*zip((X(cu), Y(cv)), (X(cu+r*np.cos(1.1)), Y(cv+r*np.sin(1.1)))), color=RED, lw=.8, zorder=5)
label(ax, (X(cu+.03), Y(cv+.12)), '$r$', 7.5, RED, halo=True)
label(ax, (x0+S/2, y0-2.8), '$u$', 7.5, MUTED); label(ax, (x0-2.6, y0+S/2), '$v$', 7.5, MUTED)
panel_tag(ax, x0+S/2, 1.4, '(b)')
# (c) tube of radius sigma around y=.28 sin(1.5x); noise from a fixed seed.
rng = np.random.default_rng(431)
xs = np.linspace(-1, 1, 401)
f = lambda x: .28*np.sin(1.5*x)
df = lambda x: .42*np.cos(1.5*x)
sig = .16
ux, uy = 14.5, 14.5
ox, oy = 94, 27
N = np.stack([-df(xs), np.ones_like(xs)], 1); N /= np.linalg.norm(N, axis=1, keepdims=True)
cur = np.stack([xs, f(xs)], 1)
up, lo = cur+sig*N, cur-sig*N
ax.add_patch(Polygon(np.r_[up, lo[::-1]]*[ux, uy]+[ox, oy], fc=YELLOW_FILL, ec='none', zorder=1))
ax.plot(ox+ux*xs, oy+uy*f(xs), color=BLUE, lw=1.3, zorder=3)
tp = np.linspace(-.9, .9, 9)
for a in tp:
    ang = rng.uniform(0, 2*np.pi); rr = sig*np.sqrt(rng.uniform(.25, .95))
    p = np.array([a, f(a)]); x = p+rr*np.array([np.cos(ang), np.sin(ang)])
    P0, X0 = (ox+ux*p[0], oy+uy*p[1]), (ox+ux*x[0], oy+uy*x[1])
    ax.plot(*zip(P0, X0), color=STROKE, lw=.6, zorder=4)
    dot(ax, P0, BLUE, size=.95, hollow=True)
    dot(ax, X0, INK, size=.9)
a = .62; p = np.array([a, f(a)]); n0 = np.array([-df(a), 1]); n0 /= np.linalg.norm(n0)
b = p+sig*n0
label(ax, (ox+ux*.95, oy+uy*f(.95)-4.6), '$M$', 8, BLUE)
ax.plot(*zip((ox+ux*p[0], oy+uy*p[1]), (ox+ux*b[0], oy+uy*b[1])), color=YELLOW, lw=.9, zorder=2)
label(ax, (ox+ux*.62+2.2, oy+uy*(f(.62)+.3)), r'$\sigma$', 7.5, MUTED)
panel_tag(ax, ox, 1.4, '(c)')
print('delta=', delta)
save(fig, OUT, 'figure', {'formula': 'curve r(t)=1+.25cos3t with 14 arc-equal samples; patch lines v=1/6,1/2,5/6 spacing 1/24; noise seed 431, sigma=.16'})
