"""Distance correlation of the standard bivariate Gaussian as a function of |rho| (closed form of Szekely-Rizzo-Bakirov),
purple dashed reference |rho|; red dot rho = 0.5, dCor = 0.454.  Spot check by Gauss-Hermite quadrature (60 x 60 nodes)."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

r = np.linspace(0, 1, 401)
fig, ax = figure(width_mm=80, height_mm=50)
ax.plot(r, r, color=PURPLE, lw=.9, ls='--')
ax.plot(r, gauss_dcor(r), color=BLUE, lw=1.4)
ax.plot([.5], [gauss_dcor(.5)], 'o', color=RED, ms=3)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .454, 1])
ax.set_xlabel('$|\\rho|$', labelpad=0)
ax.set_box_aspect(.8); gfmt(ax)
zs, zw = np.polynomial.hermite_e.hermegauss(60); zw = zw/zw.sum()
Z1, Z2 = np.meshgrid(zs, zs, indexing='ij'); W = np.outer(zw, zw).ravel()
chk = {}
for rho in (.3, .5, .8):
    X = Z1.ravel(); Y = (rho*Z1+math.sqrt(1-rho*rho)*Z2).ravel()
    chk[str(rho)] = [float(gauss_dcor(rho)), dcor_points(X, Y, W)]
save(fig, HERE, 'figure', {'formula_vs_quadrature': chk})
