"""The torus as S^1 x S^1: square of angles with glued edges and the embedded surface, same curves in both."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common'))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
TWO = 2*np.pi
TH0, TH1, PH0, PH1 = 4.75, 5.8, .5, 1.6   # highlighted coordinate patch
TH_C, PH_C = 3.75, 2.25                        # constant-angle curves
# (a) angle square.
x0, y0, S = 10, 9.5, 35.5
X = lambda v: x0+v/TWO*S; Y = lambda v: y0+v/TWO*S
ax.add_patch(Polygon([(x0, y0), (x0+S, y0), (x0+S, y0+S), (x0, y0+S)], fc=BLUE_FILL, ec='none', zorder=1))
ax.add_patch(Polygon([(X(TH0), Y(PH0)), (X(TH1), Y(PH0)), (X(TH1), Y(PH1)), (X(TH0), Y(PH1))], fc=YELLOW_FILL, ec=YELLOW, lw=.85, zorder=2))
ax.plot([x0, x0+S], [Y(PH_C)]*2, color=BLUE, lw=1.3, zorder=3)
ax.plot([X(TH_C)]*2, [y0, y0+S], color=GREEN, lw=1.3, zorder=3)
def edge(a, b, n):
    ax.plot(*zip(a, b), color=RED, lw=1.3, zorder=4)
    a, b = np.array(a), np.array(b); d = (b-a)/np.linalg.norm(b-a)
    m = (a+b)/2
    for k in range(n):
        arrow(ax, m+d*(k*2.2-1.4), m+d*(k*2.2+1.0), color=RED, lw=1.0, scale=6.2)
edge((x0, y0), (x0+S, y0), 1); edge((x0, y0+S), (x0+S, y0+S), 1)
edge((x0, y0), (x0, y0+S), 2); edge((x0+S, y0), (x0+S, y0+S), 2)
label(ax, (x0+S/2, y0-2.9), r'$\theta$', 7.5, MUTED); label(ax, (x0-3.4, y0+S/2), r'$\phi$', 7.5, MUTED)
label(ax, (x0, y0-2.9), '$0$', 7.5, MUTED); label(ax, (x0+S, y0-2.9), r'$2\pi$', 7.5, MUTED)
label(ax, (x0-3.2, y0+S-.2), r'$2\pi$', 7.5, MUTED)
# (b) embedded torus; the same patch and curves.
place = Placed(View(-62, 34), 81, 26, 8.6)
T = Torus(place)
def colour(th, ph):
    return YELLOW_FILL if (TH0 < th < TH1 and PH0 < ph < PH1) else BLUE_FILL
T.fill(ax, colour)
n = 721
for v in np.linspace(0, TWO, 13)[:-1]:
    T.curve(ax, np.full(n, v), np.linspace(0, TWO, n), MUTED, lw=.4)
for v in np.linspace(0, TWO, 13)[:-1]:
    T.curve(ax, np.linspace(0, TWO, n), np.full(n, v), MUTED, lw=.4)
s = np.linspace(0, 1, 181)
for (a, b) in (((TH0, PH0), (TH1, PH0)), ((TH1, PH0), (TH1, PH1)), ((TH1, PH1), (TH0, PH1)), ((TH0, PH1), (TH0, PH0))):
    T.curve(ax, a[0]+(b[0]-a[0])*s, a[1]+(b[1]-a[1])*s, YELLOW, lw=.9)
T.curve(ax, np.linspace(0, TWO, n), np.full(n, PH_C), BLUE, lw=1.3)
T.curve(ax, np.full(n, TH_C), np.linspace(0, TWO, n), GREEN, lw=1.3)
T.curve(ax, np.linspace(0, TWO, n), np.zeros(n), RED, lw=1.3)
T.curve(ax, np.zeros(n), np.linspace(0, TWO, n), RED, lw=1.3)
T.silhouette(ax)
panel_tag(ax, x0+S/2, 1.5, '(a)'); panel_tag(ax, 81, 1.5, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'X=((2+.82cos phi)cos theta,(2+.82cos phi)sin theta,.82 sin phi); view az=-62, el=34; visibility by depth buffer'})
