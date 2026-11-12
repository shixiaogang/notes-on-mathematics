"""Standard bivariate Gaussian rho = 0.5 under four coordinate changes: (a) identity, (b) Y -> 10 Y, (c) (e^X, e^Y), (d) (Phi(X), Phi(Y)).
Bars: |Pearson correlation| (yellow), distance correlation (blue), mutual information in nat (purple).
dCor by Gauss-Hermite quadrature (90 x 90 weighted nodes, about 0.2% error); correlation and MI exact."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

rho = .5
zs, zw = np.polynomial.hermite_e.hermegauss(90); zw = zw/zw.sum()
Z1, Z2 = np.meshgrid(zs, zs, indexing='ij'); W = np.outer(zw, zw).ravel()
X = Z1.ravel(); Y = (rho*Z1+math.sqrt(1-rho*rho)*Z2).ravel()
maps = [(X, Y), (X, 10*Y), (np.exp(X), np.exp(Y)), (Phi(X), Phi(Y))]
corr = [rho, rho, (math.exp(rho)-1)/(math.e-1), 6/math.pi*math.asin(rho/2)]
dc = [dcor_points(u, v, W) for u, v in maps]
mi = [float(gauss_mi(rho))]*4
fig, ax = figure(width_mm=96, height_mm=44)
pos = np.arange(4); wdt = .24
for k, (vals, col, fill) in enumerate([(corr, YELLOW, YELLOW_FILL), (dc, BLUE, BLUE_FILL), (mi, PURPLE, PURPLE_FILL)]):
    ax.bar(pos+(k-1)*wdt, vals, width=wdt*.92, color=fill, edgecolor=col, lw=.8)
ax.set_xticks(pos); ax.set_xticklabels(['(a)', '(b)', '(c)', '(d)'])
ax.set_ylim(0, .6); ax.set_yticks([0, .2, .4, .6])
ax.tick_params(axis='x', length=0)
save(fig, HERE, 'figure', {'pearson': corr, 'dcor_quadrature': dc, 'dcor_formula_identity': float(gauss_dcor(rho)), 'MI': mi[0]})
