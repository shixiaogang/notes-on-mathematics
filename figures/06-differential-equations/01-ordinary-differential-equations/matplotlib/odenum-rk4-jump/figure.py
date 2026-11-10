from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: RK4 loses order on a right-hand side with a time jump unless the grid contains the jump.
T = 1.0; ts = 1/np.sqrt(2)
r = lambda t: 1.0 if t < ts else 2.0
R = lambda t: t if t <= ts else ts+2*(t-ts)
g = lambda t, x: r(t)*x*(1-x)
x1 = 1/(1+4*np.exp(-R(T)))
Ns = 2**np.arange(2, 13)
err_bad = np.array([abs(integrate(rk4_step, g, T/n, int(n))[-1]-x1) for n in Ns])
# Grid aligned with the jump: two uniform pieces, about the same total step count.
err_good = []
g1 = lambda s, y: y*(1-y)
g2 = lambda s, y: 2*y*(1-y)
for n in Ns:
    n1 = max(1, int(round(n*ts))); n2 = max(1, int(n)-n1); x = X0
    t = 0.0
    h = ts/n1
    for k in range(n1):
        x = rk4_step(g1, t, x, h); t += h
    h = (T-ts)/n2
    for k in range(n2):
        x = rk4_step(g2, t, x, h); t += h
    err_good.append(abs(x-x1))
err_good = np.array(err_good)
fig, ax = figure(width_mm=92, height_mm=58)
ax.loglog(T/Ns, err_bad, 'o-', color=RED, lw=1.2, ms=2.8)
ax.loglog(T/Ns, err_good, 'o-', color=PURPLE, lw=1.2, ms=2.8)
ax.loglog(T/Ns, .03*(T/Ns), color=MUTED, lw=.9, ls=(0, (4, 2)))
ax.set_xlabel('步长 h'); ax.set_ylabel('终点误差')
ax.set_ylim(1e-16, 1e-1)
ax.text(.0035, 2.5e-3, '跳变在步内', color=RED, ha='center')
ax.text(.018, 1.5e-11, '网格对齐跳变', color=PURPLE, ha='left')
save(fig, Path(__file__).resolve().parent, 'figure', {'t_jump': float(ts), 'N': Ns.tolist(), 'unaligned': err_bad.tolist(), 'aligned': err_good.tolist()})
print(err_bad, err_good)
