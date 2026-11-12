"""Continuous mixtures. (a) Bin(10,u) for u=0.2 (yellow), 0.8 (purple) and the uniform mixture 1/11 (light blue bars);
(b) t_5 as a normal scale mixture: components N(0,5/u) at the 10% and 90% quantiles of chi^2_5, t_5 density, N(0,1)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
n = 10; k = np.arange(n + 1)
a.bar(k, np.full(n + 1, 1/(n + 1)), width=0.7, color=BLUE_FILL, edgecolor=BLUE, lw=0.7)
for uv, c in ((0.2, YELLOW), (0.8, PURPLE)):
    pk = np.array([math.comb(n, j)*uv**j*(1 - uv)**(n - j) for j in k])
    a.plot(k, pk, color=c, lw=1.3, marker='o', ms=2.5)
a.set_xlim(-0.7, 10.7); a.set_ylim(0, 0.33); a.set_xticks([0, 5, 10]); a.set_yticks([0, 0.1, 0.2, 0.3])
a.set_xlabel('$k$', labelpad=1)
nu = 5
# chi^2_5 quantiles by numerical integration of the density
uu = np.linspace(1e-9, 60, 600001)
dens = uu**(nu/2 - 1)*np.exp(-uu/2)/(2**(nu/2)*math.gamma(nu/2))
cdf = np.cumsum(dens)*(uu[1] - uu[0])
q10, q90 = (float(uu[np.searchsorted(cdf, p)]) for p in (0.1, 0.9))
x = np.linspace(-6, 6, 600)
def normal(x, var): return np.exp(-x**2/(2*var))/np.sqrt(2*math.pi*var)
tden = math.gamma((nu + 1)/2)/(math.sqrt(nu*math.pi)*math.gamma(nu/2))*(1 + x**2/nu)**(-(nu + 1)/2)
b.plot(x, normal(x, nu/q10), color=YELLOW, lw=1.3)
b.plot(x, normal(x, nu/q90), color=PURPLE, lw=1.3)
b.plot(x, normal(x, 1.0), color=STROKE, lw=0.9, ls=DASH)
b.plot(x, tden, color=BLUE, lw=1.5)
b.set_xlim(-6, 6); b.set_ylim(0, 0.58); b.set_xticks([-5, 0, 5]); b.set_yticks([0, 0.2, 0.4])
b.set_xlabel('$x$', labelpad=1)

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'chi2_5_q10': q10, 'chi2_5_q90': q90, 'nu': nu})
