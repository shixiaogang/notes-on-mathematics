from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: Heun-Euler adaptive steps on a sharp logistic front.
r = 12.0; x0 = 0.02
g = lambda t, x: r*x*(1-x)
sol = lambda t: x0/(x0+(1-x0)*np.exp(-r*t))
acc, rej, nf = heun_euler_adaptive(g, 0.0, 1.5, x0, 0.1, 1e-3, 1e-3)
fig, ax = figure(width_mm=112, height_mm=64, nrows=2, sharex=True, gridspec_kw={'height_ratios': [1.3, 1]})
tt = np.linspace(0, 1.5, 500)
ax[0].plot(tt, sol(tt), color=BLUE, lw=1.4)
ta = np.array([a[0] for a in acc]); xa = np.array([a[1][0] for a in acc]); ha = np.array([a[2] for a in acc])
ax[0].plot(ta, xa, 'o', color=GREEN, ms=2.4, zorder=4)
ax[0].plot([ta[0]], [xa[0]], 'o', color=RED, ms=4.5, zorder=5)
ax[0].set_ylabel(r'$x$')
ax[1].plot(ta[1:], ha[1:], 'o-', color=GREEN, lw=.95, ms=2.4)
for tr, xr, hr in rej:
    ax[1].plot([tr], [hr], 'x', color=RED, ms=4)
ax[1].set_xlabel(r'$t$'); ax[1].set_ylabel('步长 h'); ax[1].set_xlim(0, 1.5)
save(fig, Path(__file__).resolve().parent, 'figure', {'accepted': len(acc)-1, 'rejected': len(rej), 'nfev': nf, 'error': float(abs(xa[-1]-sol(1.5)))})
print(len(acc)-1, len(rej), nf, abs(xa[-1]-sol(1.5)))
