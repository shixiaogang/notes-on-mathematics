from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
X, gp, st, v = fw(T=400)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax = axs[0]; T = np.arange(0, 400); e = f(X[:-1])-FS
ax.loglog(T[1:], gp[1:], color=PURPLE, lw=1.1); ax.loglog(T[1:], e[1:], color=GREEN, lw=1.4)
ax.text(30, 3.3e-1*.6, '$\\Gamma(x^{(t)})$', color=PURPLE, fontsize=8); ax.text(2.0, 1.2e-3, '$f-f^*$', color=GREEN, fontsize=8)
setup(ax, (1, 400), (1e-5, 8), [1, 10, 100], [1e-4, 1e-2, 1], xl='$t$')
ax = axs[1]
# Inexact LMO: return the second-best vertex whenever it is within eps of the best.
eps = .1; x = E3.copy(); tg = []; cg = []
for t in range(400):
    g = grad(x); o = np.argsort(g); i = int(o[1]) if g[o[1]]-g[o[0]] <= eps else int(o[0]); s = np.eye(3)[i]
    tg.append(g@x-g.min()); cg.append(g@(x-s)); a = 2/(t+2); x = x+a*(s-x)
tg = np.array(tg); cg = np.array(cg); I = np.arange(60, 85); ax.step(I, cg[I]+eps, where='mid', color=RED, lw=1.0, ls=(0, (3, 2))); ax.step(I, tg[I], where='mid', color=PURPLE, lw=1.3); ax.step(I, cg[I], where='mid', color=YELLOW, lw=1.3)
setup(ax, (60, 84), None, [60, 70, 80], None, xl='$t$')
panels(fig, .07, .985, .98, .22, .22); tags(fig, axs)
save(fig, HERE, 'figure', {'inexact_eps': eps})
