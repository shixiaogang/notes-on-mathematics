"""Gibbs path Q_tau propto P e^{-V/tau}, P uniform on {0,1,2}, V(x)=x, tau in (0,inf):
from delta_0 (tau->0) to P (tau->inf), drawn in the lower-left part of the simplex.
Green points tau=0.5,1,2,4; red point tau=1/ln2 -> (4/7,2/7,1/7); yellow point P."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

def gibbs(t):
    return tilt(U3, X3, -1/t)
fig, a = figure(width_mm=72, height_mm=46)
simplex_axes(a, labels=False)
a.text(-0.015, -0.015, r'$\delta_0$', ha='right', va='top')
ts = np.exp(np.linspace(math.log(0.08), math.log(200), 500))
Pth = np.array([gibbs(t) for t in ts]); x, y = simplex_xy(Pth)
a.plot(x, y, color=BLUE, lw=1.4)
for t in (0.5, 1, 2, 4):
    gx, gy = simplex_xy(gibbs(t)); a.scatter([gx], [gy], s=12, color=GREEN, zorder=4)
    if t == 0.5:
        a.text(gx-0.01, gy+0.02, rf'$\tau={t:g}$', fontsize=7, color=MUTED, ha='center', va='bottom')
    else:
        a.text(gx+0.012, gy-0.012, rf'$\tau={t:g}$', fontsize=7, color=MUTED, ha='left', va='top')
tau = 1/math.log(2); Qs = gibbs(tau); rx, ry = simplex_xy(Qs)
a.scatter([rx], [ry], s=18, color=RED, zorder=5)
a.text(rx-0.015, ry+0.012, r'$Q^{*}$', ha='right', va='bottom')
px, py = simplex_xy(U3); a.scatter([px], [py], s=16, color=YELLOW, zorder=5)
a.text(px-0.015, py+0.012, r'$P$', ha='right', va='bottom')
a.set_xlim(-0.06, 0.62); a.set_ylim(-0.06, 0.34)
save(fig, HERE, 'figure', {'tau_points': [0.5, 1, 2, 4], 'Qstar': Qs.tolist(),
     'points': {str(t): gibbs(t).tolist() for t in (0.5, 1, 2, 4)}})
