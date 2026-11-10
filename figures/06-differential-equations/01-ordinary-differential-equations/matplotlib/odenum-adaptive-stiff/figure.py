from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

LAM = 50.0
def exact_stiff(t):
    t = np.asarray(t, float)
    return np.exp(-t), LAM/(LAM-1)*(np.exp(-t)-np.exp(-LAM*t))
def g2(t, x):
    return np.array([-x[0], LAM*(x[0]-x[1])])

# Target: adaptive explicit method on the stiff system keeps a step near the stability limit.
acc, rej, nf = heun_euler_adaptive(g2, 0.0, 4.0, [1.0, 0.0], 0.01, 1e-3, 1e-3)
ta = np.array([a[0] for a in acc]); ha = np.array([a[2] for a in acc])
fig, ax = figure(width_mm=100, height_mm=52)
ax.semilogy(ta[1:-1], ha[1:-1], '-', color=GREEN, lw=.95)
for tr, _, hr in rej:
    ax.plot([tr], [hr], 'x', color=RED, ms=3.2)
ax.axhline(.04, color=STROKE, lw=1.1)
ax.set_xlabel(r'$t$'); ax.set_ylabel('步长 h'); ax.set_xlim(0, 4)
ax.text(3.0, .026, r'$2/50$', color=STROKE)
save(fig, Path(__file__).resolve().parent, 'figure', {'accepted': len(acc)-1, 'rejected': len(rej), 'nfev': nf})
print(len(acc)-1, len(rej), nf, ha[len(ha)//2:].mean())
