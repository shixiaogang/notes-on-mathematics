from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: trapezoidal rule with a loosely solved inner equation: endpoint error vs the inner tolerance.
T = 1.0; x1 = float(exact(T))
tols = 10.0**np.arange(-12, -0.5, .5)
def run(n, tol):
    h = T/n; x = X0; iters = 0
    for k in range(n):
        y = x
        fx = f(0, x)
        while True:
            new = x+h/2*(fx+f(0, y)); iters += 1
            d = abs(new-y); y = new
            if d <= tol:
                break
        x = y
    return abs(x-x1), iters
fig, ax = figure(width_mm=112, height_mm=60, ncols=2)
out = {}
for n, c in ((16, YELLOW), (128, GREEN)):
    res = np.array([run(n, t) for t in tols])
    out[n] = res.tolist()
    ax[0].loglog(tols, res[:, 0], 'o-', color=c, lw=1.2, ms=2.6)
    ax[1].semilogx(tols, res[:, 1]/n, 'o-', color=c, lw=1.2, ms=2.6)
ax[0].set_xlabel('内部容差'); ax[0].set_ylabel('终点误差')
ax[1].set_xlabel('内部容差'); ax[1].set_ylabel('每步内部迭代次数')
panel(ax[0], '(a)', -.3); panel(ax[1], '(b)', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'tols': tols.tolist(), 'runs': out})
for n in out: print(n, ['%.2e'%r[0] for r in out[n]][::3], ['%.1f'%(r[1]/n) for r in out[n]][::3])
