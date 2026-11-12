from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Correlated noise Sigma = [[2,1],[1,2]] = U diag(1,3) U^T, u1 = (1,-1)/sqrt2 (eigenvalue 1), u2 = (1,1)/sqrt2 (eigenvalue 3).
# Green dots: 250 noise samples (seed 3). Blue ellipse: z^T Sigma^{-1} z = 1. Dark arrows: sqrt(lambda_j) u_j.
# Purple dashed circle: |x| = sqrt(P), P = 2. Red segment: support of the optimal input N(0, 2 u1 u1^T) to +-1 std.
# (a) original coordinates; (b) after the rotation U^T: the noise components are independent with variances 1 and 3.
rng = np.random.default_rng(3)
S = np.array([[2., 1.], [1., 2.]]); lam, U = np.linalg.eigh(S)        # lam = (1, 3)
U[:, 0] *= np.sign(U[0, 0]); U[:, 1] *= np.sign(U[0, 1])               # u1 = (1,-1)/sqrt2, u2 = (1,1)/sqrt2
Z = rng.multivariate_normal([0, 0], S, 250)
th = np.linspace(0, 2*np.pi, 300); circ = np.stack([np.cos(th), np.sin(th)])
ell = U @ np.diag(np.sqrt(lam)) @ circ
P = 2.0
fig, axs = figure(width_mm=104, height_mm=54, ncols=2)
panel(fig, left=.03, right=.97, top=.97, bottom=.17, wspace=.1)
for ax, R, name in ((axs[0], np.eye(2), 'orig'), (axs[1], U.T, 'rot')):
    z = Z @ R.T; e = R @ ell
    ax.plot(z[:, 0], z[:, 1], 'o', ms=1.1, color=GREEN, mew=0)
    ax.plot(e[0], e[1], color=BLUE, lw=1.4)
    ax.plot(math.sqrt(P)*circ[0], math.sqrt(P)*circ[1], color=PURPLE, lw=1.0, ls=DASH)
    for j in range(2):
        v = R @ U[:, j]*math.sqrt(lam[j])
        ax.annotate('', xy=(v[0], v[1]), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=STROKE, lw=.9))
    w = R @ U[:, 0]*math.sqrt(P)
    ax.plot([-w[0], w[0]], [-w[1], w[1]], color=RED, lw=2.0, solid_capstyle='butt')
    ax.set_xlim(-4.6, 4.6); ax.set_ylim(-4.6, 4.6); ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.axhline(0, color=STROKE, lw=.5); ax.axvline(0, color=STROKE, lw=.5)
v1 = U[:, 0]*1.0; v2 = U[:, 1]*math.sqrt(3)
lab(axs[0], v1[0]+.2, v1[1]-.5, r'$u_1$', INK)
lab(axs[0], v2[0]+.1, v2[1]+.1, r'$u_2$', INK)
lab(axs[1], 1.1, .15, r'$\tilde z_1$', INK); lab(axs[1], -.75, 1.75, r'$\tilde z_2$', INK)
tags(fig, axs)
save(fig, HERE, 'figure', {'eigenvalues': [float(v) for v in lam], 'U': U.tolist(),
                            'sample covariance rotated': np.cov((Z @ U).T).tolist()})
