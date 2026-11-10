from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: local tolerance vs endpoint global error for stable, neutral and unstable problems.
T = 2.0; sig = (-5.0, 5.0)
tols = 10.0**np.arange(-9, -1.9, .5)
fig, ax = figure(width_mm=92, height_mm=58)
for s, c, ms in zip(sig, (YELLOW, RED), (2.8, 2.8)):
    g = lambda t, x: s*(x-np.cos(t))-np.sin(t)
    errs = []
    for tol in tols:
        acc, rej, nf = heun_euler_adaptive(g, 0.0, T, 1.0, 1e-3, tol, tol)
        errs.append(abs(acc[-1][1][0]-np.cos(T)))
    ax.loglog(tols, errs, 'o-', color=c, lw=1.2, ms=ms)
ax.loglog(tols, tols, color=PURPLE, lw=.95, ls=(0, (4, 2)))
ax.text(2e-4, 1.2e-2, r'$\sigma=5$', color=RED); ax.text(3e-5, 2e-6, r'$\sigma=-5$', color=YELLOW); ax.text(1e-7, 4e-6, '容差', color=PURPLE)
ax.set_xlabel('局部容差'); ax.set_ylabel('终点全局误差')
ax.text(1.5e-5, 2e-6*.3, '容差本身', color=PURPLE) if 0 else None
save(fig, Path(__file__).resolve().parent, 'figure', {'tols': tols.tolist()})
