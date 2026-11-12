from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Whitening Sigma^{-1/2} for Sigma = [[2,1],[1,2]] (eigenvalues 1, 3; u1 = (1,-1)/sqrt2, u2 = (1,1)/sqrt2), P = 2.
# Green dots: the same 250 noise samples as gcc-correlated-noise (seed 3) after whitening -> unit circle (blue, noise contour).
# Purple ellipse: the true input constraint for xbar = Sigma^{-1/2} x, i.e. xbar^T Sigma xbar <= P
#   (semi-axes sqrt(P/1) = 1.414 along u1 and sqrt(P/3) = 0.816 along u2).
# Yellow dashed circle: the wrong constraint |xbar|^2 <= P. Red segment: optimal input direction (+-1 std, along u1).
rng = np.random.default_rng(3)
S = np.array([[2., 1.], [1., 2.]]); lam, U = np.linalg.eigh(S)
U[:, 0] *= np.sign(U[0, 0]); U[:, 1] *= np.sign(U[0, 1])
Z = rng.multivariate_normal([0, 0], S, 250)
Sih = U @ np.diag(lam**-.5) @ U.T
W = Z @ Sih.T
th = np.linspace(0, 2*np.pi, 300); circ = np.stack([np.cos(th), np.sin(th)])
P = 2.0
ell = U @ np.diag(np.sqrt(P/lam)) @ circ
fig, ax = figure(width_mm=62, height_mm=54)
panel(fig, left=.02, right=.98, top=.97, bottom=.03)
ax.plot(W[:, 0], W[:, 1], 'o', ms=1.1, color=GREEN, mew=0)
ax.plot(circ[0], circ[1], color=BLUE, lw=1.4)
ax.plot(math.sqrt(P)*circ[0], math.sqrt(P)*circ[1], color=YELLOW, lw=1.5, ls=DASH)
ax.plot(ell[0], ell[1], color=PURPLE, lw=1.4)
w = U[:, 0]*math.sqrt(P)
ax.plot([-w[0], w[0]], [-w[1], w[1]], color=RED, lw=2.0, solid_capstyle='butt')
ax.axhline(0, color=STROKE, lw=.5); ax.axvline(0, color=STROKE, lw=.5)
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-3.3, 3.3); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)
save(fig, HERE, 'figure', {'semi-axes of true constraint': [float(v) for v in np.sqrt(P/lam)],
                            'sample covariance after whitening': np.cov(W.T).tolist()})
