from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Target N(0, Sigma), Sigma=[[1,rho],[rho,1]], rho=0.8 (blue).
# Best independent Gaussian for D(Q||Pi): N(0, (1-rho^2) I) = N(0, 0.36 I) (yellow);
# best independent Gaussian for D(Pi||Q): N(0, I) (purple). Both minima equal -0.5 ln(1-rho^2)=0.5108.
# (a) contours x^T C^{-1} x = c^2 for c=1,2. (b) marginal densities of X_1.
rho = RHO
Sig = np.array([[1, rho], [rho, 1]])
th = np.linspace(0, 2*np.pi, 400)
L = np.linalg.cholesky(Sig)
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.08, right=.98, top=.96, bottom=.24, wspace=.28)
ax = axs[0]
for c, lw in ((1, 1.4), (2, 1.0)):
    e = c*(L@np.vstack([np.cos(th), np.sin(th)]))
    ax.plot(e[0], e[1], color=BLUE, lw=lw)
    ax.plot(c*.6*np.cos(th), c*.6*np.sin(th), color=YELLOW, lw=lw+.2)
    ax.plot(c*np.cos(th), c*np.sin(th), color=PURPLE, lw=lw, ls=DASH)
ax.axhline(0, color=STROKE, lw=.6); ax.axvline(0, color=STROKE, lw=.6)
ax.set_aspect('equal'); ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
axlab(ax, '$x_1$', '$x_2$')
ax = axs[1]
x = np.linspace(-3.5, 3.5, 701)
ax.plot(x, npdf(x), color=BLUE, lw=1.4)
ax.plot(x, npdf(x, 0, .6), color=YELLOW, lw=1.6)
ax.plot(x, npdf(x), color=PURPLE, lw=1.2, ls=DASH)
lab(ax, .65, .55, r'$\mathcal{N}(0,0.36)$', YELLOW, fontsize=7)
lab(ax, 1.3, .26, r'$\mathcal{N}(0,1)$', BLUE, fontsize=7)
ax.set_xlim(-3.5, 3.5); ax.set_ylim(0, .72); axlab(ax, '$x_1$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'rho': rho, 'rev_var': 1-rho**2, 'fwd_var': 1, 'min_KL_both': -0.5*math.log(1-rho**2)})
