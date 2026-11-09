from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Gradient descent iterations on each weighted subproblem, cold start at (0,2), tolerance 1e-3 versus warm start from the previous solution.
W = np.arange(1, 40)/40
def solve(w, x0, tol=1e-3):
    x = np.array(x0, float); L = max(1., 9*w+1-w); k = 0
    while True:
        g1, g2 = gm(x); g = w*g1+(1-w)*g2
        if np.linalg.norm(g) <= tol: return x, k
        x = x-g/L; k += 1
cold = [solve(w, (0, 2))[1] for w in W]; warm = []; x = np.array([0., 2.])
for w in W:
    x, k = solve(w, x); warm.append(k)
fig, ax = figure(width_mm=96, height_mm=52)
setup(ax, (0, 1), (0, max(cold)*1.08), [0, .25, .5, .75, 1], None, '$w$', '迭代次数')
ax.plot(W, cold, 'o-', color=YELLOW, lw=1.6, ms=3.2, mew=0); ax.plot(W, warm, 'o-', color=GREEN, lw=1.4, ms=3.2, mew=0)
save(fig, HERE, 'figure', {'cold_total': int(sum(cold)), 'warm_total': int(sum(warm))}); print(sum(cold), sum(warm), cold[:3], warm[:3])
