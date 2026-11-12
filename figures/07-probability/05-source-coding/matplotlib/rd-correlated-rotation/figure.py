"""X ~ N(0, Sigma), Sigma=[[2,1],[1,2]], eigenvalues 3 and 1, eigenvectors (1,1)/sqrt2, (-1,1)/sqrt2.
(a) 600 samples (seed SEED) with eigen-axes; (b) Y=U^T X, uncorrelated with variances 3 and 1."""
from pathlib import Path
import sys
import math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

S = np.array([[2., 1.], [1., 2.]])
lam, U = np.linalg.eigh(S)          # ascending: 1, 3
U = U[:, ::-1]; lam = lam[::-1]
if U[0, 0] < 0: U[:, 0] *= -1
if U[1, 1] < 0: U[:, 1] *= -1
rng = np.random.default_rng(SEED)
X = rng.multivariate_normal([0, 0], S, size=600)
Y = X @ U
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, left=.07, right=.985, top=.97, bottom=.24, wspace=.28)
ax = axs[0]
ax.plot(X[:, 0], X[:, 1], 'o', ms=1.3, color=GREEN, mew=0)
t = np.linspace(0, 2*math.pi, 200)
for c in (1, 2):
    E = (U*np.sqrt(lam)*c) @ np.vstack([np.cos(t), np.sin(t)])
    ax.plot(E[0], E[1], color=BLUE, lw=.9)
for k in range(2):
    v = U[:, k]*math.sqrt(lam[k])*2.4
    ax.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.0, mutation_scale=7))
lab(ax, 2.7, 3.2, '$\\mathbf{u}_1$', RED); lab(ax, -2.2, 1.6, '$\\mathbf{u}_2$', RED)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-5, 5)
axlab(ax, '$x_1$', '$x_2$')
ax = axs[1]
ax.plot(Y[:, 0], Y[:, 1], 'o', ms=1.3, color=GREEN, mew=0)
for c in (1, 2):
    ax.plot(c*math.sqrt(lam[0])*np.cos(t), c*math.sqrt(lam[1])*np.sin(t), color=BLUE, lw=.9)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-5, 5)
axlab(ax, '$y_1$', '$y_2$')
tags(fig, axs)
save(fig, HERE, 'figure', {'eigvals': lam.tolist(), 'sample_cov_Y': np.cov(Y.T).round(3).tolist()})
