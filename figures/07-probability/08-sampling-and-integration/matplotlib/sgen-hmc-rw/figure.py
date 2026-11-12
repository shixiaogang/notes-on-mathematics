from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: N(0, Sigma), Sigma = [[1, .95], [.95, 1]], U(x) = x^T Sigma^{-1} x / 2, start (-2, -2).
# (a) random-walk Metropolis, proposal N(x, 0.25^2 I), 200 iterations (200 density evaluations), seed 13.
# (b) HMC, identity mass, eps = 0.18, L = 10, 20 iterations (200 gradient evaluations), seed 13.
S = np.array([[1, .95], [.95, 1]]); Si = np.linalg.inv(S)
U = lambda x: .5*x@Si@x; gU = lambda x: Si@x
def rw(n, s, rng):
    x = np.array([-2., -2.]); P = [x.copy()]; acc = 0
    for _ in range(n):
        y = x+s*rng.standard_normal(2)
        if math.log(rng.random()) <= U(x)-U(y): x = y; acc += 1
        P.append(x.copy())
    return np.array(P), acc/n
def hmc(n, eps, L, rng):
    x = np.array([-2., -2.]); P = [x.copy()]; acc = 0
    for _ in range(n):
        p = rng.standard_normal(2); x1, p1 = x.copy(), p.copy()
        for _ in range(L):
            p1 = p1-eps/2*gU(x1); x1 = x1+eps*p1; p1 = p1-eps/2*gU(x1)
        dH = U(x1)+.5*p1@p1-U(x)-.5*p@p
        if math.log(rng.random()) <= -dH: x = x1; acc += 1
        P.append(x.copy())
    return np.array(P), acc/n
Pr, ar = rw(200, .25, np.random.default_rng(13))
Ph, ah = hmc(20, .18, 10, np.random.default_rng(13))
fig, (A, B) = figure(width_mm=104, height_mm=54, ncols=2)
th = np.linspace(0, 2*np.pi, 300); Lc = np.linalg.cholesky(S)
for ax, P, L in ((A, Pr, 'a'), (B, Ph, 'b')):
    style(ax)
    for r in (1, 2):
        E = Lc@(r*np.stack([np.cos(th), np.sin(th)])); ax.plot(E[0], E[1], color=BLUE, lw=.9)
    ax.plot(P[:, 0], P[:, 1], '-o', ms=1.8, lw=.7, color=GREEN)
    ax.plot([-2], [-2], 'o', ms=3.6, color=RED, zorder=5)
    ax.set_aspect('equal'); ax.set_xlim(-2.7, 2.7); ax.set_ylim(-2.7, 2.7); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
    sub(ax, L, '$x_1$')
A.set_ylabel('$x_2$')
save(fig, HERE(__file__), 'figure', {'acc_rw': ar, 'acc_hmc': ah})
print(ar, ah)
