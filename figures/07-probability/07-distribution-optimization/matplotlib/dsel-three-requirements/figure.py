"""Three separate requirements on Q=(q0,q1,q2) over {0,1,2}, drawn in the simplex.
Cost V(x)=x: level lines E_Q[V]=q1+2q2=c for c=0.5,1,1.5 (dashed grey), minimum at delta_0.
Mean constraint E_Q[X]=10/7: segment from (2/7,0,5/7) to (0,4/7,3/7) (red).
Reference P=uniform (blue point); closeness to P alone selects P itself."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

fig, ax = figure(width_mm=84, height_mm=68)
simplex_axes(ax)
# level lines q1+2q2=c: endpoints on boundary
def level(c):
    pts = []
    # edge p2=0: q1=c, q0=1-c (valid if c<=1)
    if c <= 1: pts.append((1-c, c, 0))
    # edge q1=0: 2q2=c -> q2=c/2, q0=1-c/2
    if c <= 2: pts.append((1-c/2, 0, c/2))
    # edge q0=0: q1+q2=1, q1+2q2=c -> q2=c-1, q1=2-c (valid if 1<=c<=2)
    if 1 <= c <= 2: pts.append((0, 2-c, c-1))
    return np.array(pts[:2])
for c in (0.5, 1.0, 1.5):
    L = level(c); x, y = simplex_xy(L)
    ax.plot(x, y, color=STROKE, lw=0.75, ls='--')
    lx, ly = simplex_xy(np.array([1-c/2, 0, c/2])); ax.text(lx-0.03, ly, rf'${c:g}$', fontsize=7.5, color=MUTED, ha='right', va='center')
seg = np.array([[2/7, 0, 5/7], [0, 4/7, 3/7]])
sx, sy = simplex_xy(seg)
ax.plot(sx, sy, color=RED, lw=1.8)
ax.text(sx[1]+0.03, sy[1]+0.01, r'$\mathrm{E}_Q[X]=10/7$', color=INK, fontsize=7.5, ha='left')
px, py = simplex_xy(U3)
ax.scatter([px], [py], s=18, color=BLUE, zorder=5)
ax.text(px+0.03, py-0.01, r'$P$', ha='left', va='top')
ax.scatter([0], [0], s=22, color=RED, zorder=6)
ax.annotate('', xy=(0.03, 0.02), xytext=(0.22, 0.13), arrowprops=dict(arrowstyle='->', color=STROKE, lw=0.8))
save(fig, HERE, 'figure', {'segment_endpoints': seg.tolist(), 'levels': [0.5, 1, 1.5], 'reference': U3.tolist()})
