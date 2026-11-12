"""Minimum KL under the mean constraint, P uniform on {0,1,2}, T(x)=x, m=10/7.
Level curves of D(Q||P) at 0.05, 0.3, 0.5 (thin blue) and at D*=10/7 ln2 - ln(7/3)=0.1429 (thick blue),
feasible segment E_Q[X]=10/7 (red), tilt family Q_theta propto e^{theta x}/3 (yellow),
Q*=(1/7,2/7,4/7) (red point), another feasible Q=(2/7,0,5/7) (green point)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

fig, ax = figure(width_mm=84, height_mm=70)
simplex_axes(ax)
# contour on fine barycentric mesh via tricontour
G = simplex_grid(220)
D = np.array([kl(g, U3) for g in G])
gx, gy = simplex_xy(G)
Dst = (10/7)*math.log(2)-math.log(7/3)
ax.tricontour(gx, gy, D, levels=[0.05, 0.3, 0.5], colors=[BLUE], linewidths=0.6)
ax.tricontour(gx, gy, D, levels=[Dst], colors=[BLUE], linewidths=1.3)
th = np.linspace(-7, 7, 600)
F = np.array([tilt(U3, X3, t) for t in th]); fx, fy = simplex_xy(F)
ax.plot(fx, fy, color=YELLOW, lw=1.5)
seg = np.array([[2/7, 0, 5/7], [0, 4/7, 3/7]]); sx, sy = simplex_xy(seg)
ax.plot(sx, sy, color=RED, lw=1.8)
Qs = tilt(U3, X3, math.log(2)); qx, qy = simplex_xy(Qs)
ax.scatter([qx], [qy], s=20, color=RED, zorder=6)
ax.text(qx+0.03, qy+0.005, r'$Q^{*}$', ha='left', va='bottom')
qx2, qy2 = sx[0], sy[0]
ax.scatter([qx2], [qy2], s=16, color=GREEN, zorder=6); ax.text(qx2-0.03, qy2, r'$Q$', ha='right', va='center')
px, py = simplex_xy(U3); ax.scatter([px], [py], s=14, color=STROKE, zorder=6); ax.text(px+0.03, py-0.01, r'$P$', va='top')
save(fig, HERE, 'figure', {'D_star': Dst, 'Qstar': Qs.tolist(), 'Q_alt': [2/7, 0, 5/7], 'D_alt': kl([2/7, 0, 5/7], U3),
     'D_alt_to_star': kl([2/7, 0, 5/7], Qs)})
