from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Running example. For each eps: regularized optimum pi_eps (Sinkhorn, 4000 log-domain rounds).
# Blue: transport cost <C,pi_eps>; yellow: regularized optimum value <C,pi_eps> + eps KL(pi_eps||a b^T);
# purple dashed: unregularized optimal cost 0.6.
a, b, C = A_EX, B_EX, C_EX
eps_grid = np.geomspace(.08, 3, 40)
cost, obj, res = [], [], []
for eps in eps_grid:
    f, g, _ = sinkhorn_log(a, b, C, eps, 4000)
    P = plan(a, b, C, eps, f, g)
    cost.append(float((C*P).sum())); obj.append(float((C*P).sum()+eps*kl_ref(P, a, b)))
    res.append(float(np.abs(P.sum(1)-a).sum()))
fig, ax = figure(width_mm=80, height_mm=50)
panel(fig, left=.13, right=.97, top=.95, bottom=.2)
ax.semilogx(eps_grid, cost, color=BLUE, lw=1.4)
ax.semilogx(eps_grid, obj, color=YELLOW, lw=1.6)
ax.axhline(.6, color=PURPLE, lw=.85, ls=DASH)
ax.axhline(1.58, color=STROKE, lw=.6, ls=DOT)
ax.text(.09, 1.5, '$a\\otimes b$', color=STROKE, fontsize=7.5)
ax.text(1.6, .95, '$\\langle C,\\pi_\\varepsilon\\rangle$', color=BLUE, fontsize=7.5)
ax.text(.35, 1.0, '正则化目标值', color=YELLOW, fontsize=7.5)
ax.text(1.5, .53, '$0.6$', color=PURPLE, fontsize=7.5)
ax.set_xlabel('$\\varepsilon$', labelpad=1); ax.set_ylim(.4, 1.7)
pick = {str(e): (c, o) for e, c, o in zip(eps_grid, cost, obj)}
save(fig, HERE, 'figure', {'max_row_residual': max(res), 'cost_at_eps1': float(np.interp(1, eps_grid, cost)),
                           'samples': pick})
