from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: endpoint error of Euler under step refinement at T=1.
fig, ax = figure(width_mm=112, height_mm=52, ncols=2)
T = 1.0; x1 = float(exact(T))
t = np.linspace(0, 1, 200)
a = ax[0]
a.plot(t, exact(t), color=BLUE, lw=1.4)
cols = {2: PURPLE, 4: YELLOW, 16: GREEN}
for n, c in cols.items():
    h = T/n; xs = integrate(euler_step, f, h, n)
    a.plot(h*np.arange(n+1), xs, color=c, lw=1.15, marker='o', ms=2.6 if n > 4 else 3.4)
a.plot([0], [X0], 'o', color=RED, ms=4.8, zorder=6)
a.set_xlabel(r'$t$'); a.set_ylabel(r'$x$')
a.set_xlim(-.02, 1.05); a.set_ylim(.18, .43)
a.text(.76, .297, r'$N=2$', color=PURPLE)
a.text(.42, .335, r'$x(t)$', color=BLUE, ha='right')
b = ax[1]
Ns = 2**np.arange(1, 11)
err = np.array([abs(integrate(euler_step, f, T/n, int(n))[-1]-x1) for n in Ns])
b.loglog(Ns, err, 'o-', color=GREEN, lw=1.2, ms=3.4)
b.loglog(Ns, .05/Ns, color=PURPLE, lw=.95, ls=(0, (4, 2)))
b.set_xlabel('右端求值次数 N'); b.set_ylabel('终点误差')
b.text(45, 2.5e-3, r'$0.05/N$', color=PURPLE)
panel(ax[0], '(a)', -.3); panel(ax[1], '(b)', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x=x(1-x), Euler, T=1', 'N': Ns.tolist(), 'err': err.tolist()})
