from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Generalized Lloyd iteration for the correlated Gaussian pair (unit variances, correlation 0.9), N = 16, on
# n = 50000 simulated vectors (seed 1). Ten starts: codebooks drawn as 16 distinct sample vectors (seeds 11..20).
# Curves: average squared error per component on the simulated vectors after each round (green).
# Purple dotted: the product of two 4-level Lloyd-Max quantizers (exact value 0.1175).
rho = .9; A = np.linalg.cholesky(np.array([[1, rho], [rho, 1]]))
X = np.random.default_rng(1).standard_normal((50000, 2))@A.T
_, _, D4 = gauss_lloyd(4)
R = 40; finals = []
fig, ax = figure(width_mm=92, height_mm=50)
panel(fig, left=.15, right=.97, bottom=.17, top=.97)
for s in range(11, 21):
    C = X[np.random.default_rng(s).choice(len(X), 16, replace=False)].copy(); Ds = []
    for r in range(R+1):
        j, d2 = nearest(X, C); Ds.append(d2.mean()/2)
        for k in range(16):
            if (j == k).any(): C[k] = X[j == k].mean(0)
    finals.append(Ds[-1]); ax.plot(range(R+1), Ds, color=GREEN, lw=1.0)
ax.axhline(D4, color=PURPLE, lw=1.1, ls=DOT)
lab(ax, 20, D4+.006, '逐分量码本', PURPLE)
ax.set_xlim(0, R); ax.set_ylim(.03, .2); ax.set_xlabel('轮次', labelpad=1); ax.set_ylabel('每分量误差', labelpad=2)
save(fig, HERE, 'figure', {'finals': sorted(float(v) for v in finals), 'product_exact': float(D4)})
