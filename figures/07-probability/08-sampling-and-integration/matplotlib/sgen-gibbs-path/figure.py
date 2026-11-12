from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
from statistics import NormalDist
# Target: systematic-scan Gibbs sampler for N(0, [[1, rho], [rho, 1]]), start (2, 2), 20 sweeps.
# X1 | X2 = x2 ~ N(rho x2, 1 - rho^2), X2 | X1 = x1 ~ N(rho x1, 1 - rho^2).
# The first two sweeps use z = Phi^{-1}(0.37), Phi^{-1}(0.80), Phi^{-1}(0.15), Phi^{-1}(0.62) (hand-worked example);
# later normals from numpy seed 12.  (a) rho = 0.8, (b) rho = 0.99 with the same normals.
N = NormalDist()
z_hand = [N.inv_cdf(u) for u in (.37, .80, .15, .62)]
zs = np.concatenate([z_hand, np.random.default_rng(12).standard_normal(36)])
def path(rho):
    s = math.sqrt(1-rho**2); x1, x2 = 2., 2.; P = [(x1, x2)]
    for k in range(20):
        x1 = rho*x2+s*zs[2*k]; P.append((x1, x2))
        x2 = rho*x1+s*zs[2*k+1]; P.append((x1, x2))
    return np.array(P)
fig, (A, B) = figure(width_mm=104, height_mm=54, ncols=2)
th = np.linspace(0, 2*np.pi, 300)
out = {}
for ax, rho, L in ((A, .8, 'a'), (B, .99, 'b')):
    style(ax)
    S = np.array([[1, rho], [rho, 1]]); Lc = np.linalg.cholesky(S)
    for r in (1, 2):
        E = Lc@(r*np.stack([np.cos(th), np.sin(th)]))
        ax.plot(E[0], E[1], color=BLUE, lw=.9)
    P = path(rho); out[rho] = P[:5].tolist()
    ax.plot(P[:, 0], P[:, 1], color=GREEN, lw=.8)
    ax.plot(P[::2, 0], P[::2, 1], 'o', ms=2.0, color=GREEN)
    ax.plot([2], [2], 'o', ms=3.6, color=RED, zorder=5)
    ax.set_aspect('equal'); ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
    sub(ax, L, '$x_1$')
A.set_ylabel('$x_2$')
save(fig, HERE(__file__), 'figure', {'first_states': {str(k): v for k, v in out.items()}})
print(out[.8])
