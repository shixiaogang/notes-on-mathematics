from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
from statistics import NormalDist
# Target: Gaussian generation X = mu + A Z from Z = (Phi^{-1}(U_1), Phi^{-1}(U_2)).
# (a) 600 standard normal pairs, numpy seed 5; red point z = (Phi^{-1}(0.37), Phi^{-1}(0.80)).
# (b) mu = (1, 0), Sigma = [[4, 2], [2, 2]] = L L^T with L = [[2, 0], [1, 1]]; ellipse {(x-mu)^T Sigma^{-1} (x-mu) = 4}.
# (c) singular Sigma = [[1, 2], [2, 4]] = a a^T, a = (1, 2): all samples on the line mu + t a.
N = NormalDist()
rng = np.random.default_rng(5)
Z = rng.standard_normal((600, 2))
z0 = np.array([N.inv_cdf(.37), N.inv_cdf(.80)])
mu = np.array([1., 0.]); L = np.array([[2., 0.], [1., 1.]]); a = np.array([1., 2.])
X = mu+Z@L.T; x0 = mu+L@z0
S = X[:, :1]*a+mu
fig, axs = figure(width_mm=112, height_mm=48, ncols=3)
th = np.linspace(0, 2*np.pi, 300); circ = 2*np.stack([np.cos(th), np.sin(th)])
for ax in axs: style(ax)
axs[0].plot(Z[:, 0], Z[:, 1], 'o', ms=1.2, color=GREEN, mec='none')
axs[0].plot(circ[0], circ[1], color=BLUE, lw=1.1)
axs[0].plot(*z0, 'o', ms=3.6, color=RED)
axs[1].plot(X[:, 0], X[:, 1], 'o', ms=1.2, color=GREEN, mec='none')
E = mu[:, None]+L@circ
axs[1].plot(E[0], E[1], color=BLUE, lw=1.1)
axs[1].plot(*x0, 'o', ms=3.6, color=RED)
t = np.linspace(-3.2, 3.2, 2)
axs[2].plot(mu[0]+t*a[0], mu[1]+t*a[1], color=BLUE, lw=.8, ls='--')
Zs = Z[:, 0]
axs[2].plot(mu[0]+Zs[:150]*a[0], mu[1]+Zs[:150]*a[1], 'o', ms=2.4, zorder=4, color=GREEN, mec='none')
for ax, L_, lim in ((axs[0], 'a', 4), (axs[1], 'b', 6), (axs[2], 'c', 6)):
    ax.set_aspect('equal'); ax.set_xlim(-lim+(0 if L_ == 'a' else 1), lim+(0 if L_ == 'a' else 1)); ax.set_ylim(-lim, lim)
    sub(ax, L_, '$x_1$' if L_ != 'a' else '$z_1$')
axs[0].set_ylabel('$z_2$'); axs[1].set_ylabel('$x_2$'); axs[2].set_ylabel('$x_2$')
save(fig, HERE(__file__), 'figure', {'z0': z0.tolist(), 'x0': x0.tolist(), 'seed': 5, 'n': 600})
print(z0, x0)
