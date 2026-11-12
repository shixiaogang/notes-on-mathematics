from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Discrete transport in the plane, squared Euclidean cost.
# Sources (blue) x=(0,0),(0,2),(3,1) with a=(0.4,0.4,0.2); targets (yellow) y=(1,0),(2,2),(4,0),(1,3) with b=(0.3,0.3,0.2,0.2).
# Exact LP optimum by enumeration of basic solutions: cost 2.7, five positive entries.
X = np.array([[0, 0], [0, 2], [3, 1]], float); a = np.array([.4, .4, .2])
Y = np.array([[1, 0], [2, 2], [4, 0], [1, 3]], float); b = np.array([.3, .3, .2, .2])
C = ((X[:, None, :]-Y[None, :, :])**2).sum(-1)
val, P, S = lp_bruteforce(a, b, C)
fig, ax = figure(width_mm=72, height_mm=54)
panel(fig, left=.1, right=.97, top=.97, bottom=.13)
for i in range(3):
    for j in range(4):
        if P[i, j] > 1e-9:
            ax.annotate('', xy=Y[j], xytext=X[i], arrowprops=dict(arrowstyle='->', color=STROKE, lw=.6+4*P[i, j], shrinkA=6, shrinkB=6))
            mid = (X[i]+Y[j])/2
            d = Y[j]-X[i]; nrm = np.array([-d[1], d[0]])/np.hypot(*d)
            ax.text(*(mid+.28*nrm), f'{P[i, j]:.1f}', fontsize=7, color=MUTED, ha='center', va='center')
for i in range(3):
    ax.plot(*X[i], 'o', ms=5+14*a[i], color=BLUE_FILL, mec=BLUE, mew=1)
    ax.text(X[i, 0]-.18, X[i, 1]+.25, f'{a[i]:.1f}', fontsize=7.5, color=BLUE)
for j in range(4):
    ax.plot(*Y[j], 's', ms=5+14*b[j], color=YELLOW_FILL, mec=YELLOW, mew=1)
    ax.text(Y[j, 0]+.22, Y[j, 1]-.08, f'{b[j]:.1f}', fontsize=7.5, color=YELLOW)
ax.set_aspect('equal'); ax.set_xlim(-.6, 4.7); ax.set_ylim(-.6, 3.6)
ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2, 3])
save(fig, HERE, 'figure', {'cost_matrix': C.tolist(), 'optimal_plan': P.round(6).tolist(), 'optimal_cost': val})
