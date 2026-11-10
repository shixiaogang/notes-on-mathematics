from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: endpoint error of Euler, midpoint and RK4 vs step size and vs cost.
T = 1.0; x1 = float(exact(T))
Ns = 2**np.arange(1, 11)
M = [('Euler', euler_step, 1, GREEN), ('中点', midpoint_step, 2, YELLOW), ('RK4', rk4_step, 4, PURPLE)]
fig, ax = figure(width_mm=112, height_mm=58, ncols=2, sharey=True)
E_ = {}
for name, st, s, c in M:
    err = np.array([abs(integrate(st, f, T/n, int(n))[-1]-x1) for n in Ns])
    E_[name] = err
    ax[0].loglog(T/Ns, err, 'o-', color=c, lw=1.2, ms=2.8)
    ax[1].loglog(Ns*s, err, 'o-', color=c, lw=1.2, ms=2.8)
ax[0].set_xlabel('步长 h'); ax[1].set_xlabel('右端求值次数'); ax[0].set_ylabel('终点误差')
ax[0].set_ylim(3e-16, .2)
ax[0].text(.0035, 2e-3, 'Euler', color=GREEN)
ax[0].text(.0035, 2.6e-7, '中点', color=YELLOW, ha='right')
ax[0].text(.031, 3e-11, 'RK4', color=PURPLE, ha='left')
ax[1].axhline(1e-6, color=MUTED, lw=.8, ls=(0, (2, 2)))
panel(ax[0], '(a)', -.27); panel(ax[1], '(b)', -.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'N': Ns.tolist(), **{k: v.tolist() for k, v in E_.items()}})
