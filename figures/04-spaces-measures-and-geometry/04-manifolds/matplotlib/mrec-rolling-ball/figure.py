"""The tangent ball of radius tau contains no point of M; the midpoint projection and dyadic refinement."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 58
fig, ax = canvas(W, H)
# (a) M: y=x^2/(2 rho), rho=1.6, tau=1 ; ball centre (0,1). Reach inequality for w at x=1.25.
u = 18; o = np.array([28, 12])
rho = 1.6
f = lambda x: x*x/(2*rho)
ax.add_patch(Circle(o+u*np.array([0, 1]), u, fc=BLUE_FILL, ec=BLUE, lw=.85, zorder=1))
xs = np.linspace(-1.42, 1.42, 301)
ax.plot(o[0]+u*xs, o[1]+u*f(xs), color=BLUE, lw=1.4, zorder=4)
ax.plot(o[0]+u*np.array([-1.42, 1.42]), [o[1]]*2, color=MUTED, lw=.85, ls=(0, (2.2, 1.8)), zorder=3)
q = o; c = o+u*np.array([0, 1])
ax.plot(*zip(q, c), color=RED, lw=.9, zorder=5)
arrow(ax, q, q+(0, 9), color=RED, lw=1.0)
dot(ax, q, INK, size=1.0); dot(ax, c, RED, size=.9)
label(ax, q+(-3.2, -3), r'$\mathbf{q}$', 8)
label(ax, q+(2.5, 8), r'$\mathbf{v}$', 7.5, RED)
label(ax, c+(4.0, .4), r'$\mathbf{q}+\tau\mathbf{v}$', 7.5, RED)
label(ax, q+(-2.6, 16), r'$\tau$', 7.5, RED)
wx = 1.25; w = o+u*np.array([wx, f(wx)]); foot = o+u*np.array([wx, 0])
ax.plot(*zip(w, foot), color=GREEN, lw=1.1, zorder=5)
ax.plot(*zip(q, w), color=INK, lw=.8, zorder=5)
dot(ax, w, INK, size=1.0)
label(ax, w+(3.4, .8), r'$\mathbf{w}$', 8)
label(ax, foot+(3, 2.8), '$d$', 7.5, GREEN)
label(ax, (o[0]+u*.75, o[1]+u*.36), '$a$', 7.5, INK, halo=True)
label(ax, (o[0]-u*1.36, o[1]+u*f(1.36)+2.2), '$M$', 8, BLUE)
label(ax, (o[0]+u*1.42+1, o[1]-2.5), r'$T_{\mathbf{q}}M$', 7.5, MUTED, ha='right')
panel_tag(ax, o[0], 1.4, '(a)')
# (b) unit circle of radius tau; chord a=2 tau sin(theta), theta=60 deg. Midpoint m, arc-mid w.
u = 26; o2 = np.array([85, 8.5])
theta = np.radians(60)
th = np.linspace(np.pi/2-theta*1.3, np.pi/2+theta*1.3, 301)
ax.plot(o2[0]+u*np.cos(th), o2[1]+u*np.sin(th), color=BLUE, lw=1.4, zorder=3)
P = lambda a: o2+u*np.array([np.cos(np.pi/2+a), np.sin(np.pi/2+a)])
p, qq, wp = P(theta), P(-theta), P(0)
m = (p+qq)/2
ax.plot(*zip(p, qq), color=INK, lw=.85, zorder=4)
ax.plot(*zip(m, wp), color=RED, lw=1.1, zorder=5)
for a, b in ((theta, theta/2), (theta/2, 0), (0, -theta/2), (-theta/2, -theta)):
    ax.plot(*zip(P(a), P(b)), color=GREEN, lw=1.0, zorder=4)
for a in (theta/2, -theta/2):
    dot(ax, P(a), GREEN, size=.8)
for z in (p, qq, m, wp):
    dot(ax, z, INK, size=1.0)
label(ax, p+(-3, 1.5), r'$\mathbf{p}$', 8); label(ax, qq+(3, 1.5), r'$\mathbf{q}$', 8)
label(ax, m+(-3, -2.6), r'$\mathbf{m}$', 8); label(ax, wp+(0, 3), r'$\mathbf{w}$', 8)
label(ax, (m[0]+2.6, (m[1]+wp[1])/2), '$h$', 7.5, RED)
label(ax, ((m[0]+qq[0])/2, m[1]-2.6), r'$a/2$', 7.5, INK)
label(ax, (P(-theta*.98)[0]-4, P(-theta*.98)[1]+6.5), '$M$', 8, BLUE)
panel_tag(ax, o2[0], 1.4, '(b)')
save(fig, OUT, 'figure', {'formula': '(a) y=x^2/3.2, ball radius tau=1 at (0,1); (b) circle radius tau, chord half-angle 60 deg, dyadic refinement'})
