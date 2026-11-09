"""Three limits of the reach: curvature at the ellipse tips, a pinched Cassini neck, two nearby components."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 40
fig, ax = canvas(W, H)
th = np.linspace(0, 2*np.pi, 1201)
# (a) ellipse a=2,b=1. Medial axis [-1.5,1.5]x{0}; reach b^2/a=.5 attained at the tips.
u = 8.7; o = np.array([19, 22])
E = np.stack([2*np.cos(th), np.sin(th)], 1)
ax.plot(*(o+u*E).T, color=BLUE, lw=1.3, zorder=3)
ax.plot(o[0]+u*np.array([-1.5, 1.5]), [o[1]]*2, color=RED, lw=1.2, zorder=3)
cc = np.array([1.5, 0]); ax.add_patch(Circle(o+u*cc, u*.5, fc=YELLOW_FILL, ec=YELLOW, lw=.85, zorder=1))
ax.plot(*zip(o+u*cc, o+u*(cc+[.5, 0])), color=INK, lw=.8, zorder=5)
dot(ax, o+u*cc, RED, size=.9)
label(ax, o+u*(cc+[.18, .16]), r'$\tau$', 7.5, INK)
label(ax, o+u*np.array([-.75, .4]), '$M$', 8, BLUE)
panel_tag(ax, o[0], 1.4, '(a)')
# (b) Cassini oval c=1,e=1.05: neck half-width b=sqrt(e^2-c^2).
u = 12; o = np.array([58, 22])
c, e = 1.0, 1.05
b = np.sqrt(e*e-c*c)
r2 = c*c*np.cos(2*th)+np.sqrt(c**4*np.cos(2*th)**2+e**4-c**4)
C = np.sqrt(r2)[:, None]*np.stack([np.cos(th), np.sin(th)], 1)
ax.plot(*(o+u*C).T, color=BLUE, lw=1.3, zorder=3)
z = np.array([0., 0.])
for s in (1, -1):
    ax.plot(*zip(o+u*z, o+u*np.array([0, s*b])), color=INK, lw=.8, zorder=4)
    dot(ax, o+u*np.array([0, s*b]), INK, size=.9)
dot(ax, o+u*z, RED, size=1.0)
label(ax, o+u*np.array([.13, .16]), '$b$', 7.5, INK)
label(ax, o+u*np.array([.15, -.2]), r'$\bm{z}$'.replace(r'\bm', r'\mathbf'), 7.5, RED)
panel_tag(ax, o[0], 1.4, '(b)')
# (c) two unit circles at gap s=.5 (components); midpoint is equidistant.
u = 7.2; 
cx = 95
for sgn in (1, -1):
    C2 = np.array([cx+sgn*u*(1+.25), 22])+u*np.stack([np.cos(th), np.sin(th)], 1)
    ax.plot(*C2.T, color=BLUE if sgn < 0 else GREEN, lw=1.3, zorder=3)
    p = np.array([cx+sgn*u*.25, 22])
    dot(ax, p, INK, size=.9)
    ax.plot([cx, p[0]], [22, 22], color=INK, lw=.8, zorder=4)
dot(ax, (cx, 22), RED, size=1.0)
label(ax, (cx+u*(-1.25), 22), '$M_1$', 8, BLUE); label(ax, (cx+u*1.25, 22), '$M_2$', 8, GREEN)
ax.annotate('', (cx-u*.25, 16.5), (cx+u*.25, 16.5), arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.7, shrinkA=0, shrinkB=0, mutation_scale=5))
label(ax, (cx, 14.2), '$s$', 7.5, MUTED)
panel_tag(ax, cx, 1.4, '(c)')
save(fig, OUT, 'figure', {'formula': 'ellipse a=2,b=1 (reach .5); Cassini c=1,e=1.05; unit circles with gap .5'})
