"""Fisher ellipses {delta: (1/2) delta^T G delta = eps}, eps=0.01, in the (mu,sigma) half-plane; G=diag(1/sigma^2, 2/sigma^2).
Semi-axes sqrt(2 eps) sigma (mu-direction) and sqrt(eps) sigma (sigma-direction)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, ax = figure(width_mm=100, height_mm=56)
eps = 0.01; ang = np.linspace(0, 2*np.pi, 200)
for s in (0.25, 0.75, 1.25, 1.75, 2.25):
    for m in (-2, -1, 0, 1, 2):
        a_ = np.sqrt(2*eps)*s; b_ = np.sqrt(eps)*s
        ax.fill(m+a_*np.cos(ang), s+b_*np.sin(ang), color=BLUE_FILL, lw=0)
        ax.plot(m+a_*np.cos(ang), s+b_*np.sin(ang), color=BLUE, lw=1.0)
        ax.scatter([m], [s], s=3, color=STROKE, zorder=4)
ax.axhline(0, color=STROKE, lw=0.9, ls='--')
ax.set_xlim(-2.7, 2.7); ax.set_ylim(-0.1, 2.65); ax.set_aspect('equal')
ax.set_xlabel(r'$\mu$', labelpad=1); ax.set_ylabel(r'$\sigma$', labelpad=1)
ax.set_yticks([0, 0.25, 0.75, 1.25, 1.75, 2.25])
save(fig, HERE, 'figure', {'eps': eps, 'semi_axes_at_sigma_2.25': [np.sqrt(2*eps)*2.25, np.sqrt(eps)*2.25]})
