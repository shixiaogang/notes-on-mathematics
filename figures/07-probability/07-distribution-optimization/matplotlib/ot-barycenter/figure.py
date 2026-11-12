from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Three inputs on the line (blue): N(-3, 0.5^2), Unif(-1, 1), N(3.5, 0.8^2); weights 1/3 each.
# W_2 barycenter: quantile function = average of the three quantile functions (green);
# its density is 1/q'(u) at x = q(u). Mixture (1/3 each) shown in yellow for comparison.
import math
from statistics import NormalDist
u = np.linspace(1e-5, 1-1e-5, 40001)
nq = np.vectorize(NormalDist().inv_cdf)
z = nq(u)
q1 = -3+.5*z; q2 = -1+2*u; q3 = 3.5+.8*z
q = (q1+q2+q3)/3
dens = np.gradient(u, q)
xs = np.linspace(-5, 6, 1101)
def npdf(x, m, s): return np.exp(-(x-m)**2/(2*s*s))/(s*np.sqrt(2*np.pi))
f1 = npdf(xs, -3, .5); f2 = np.where(np.abs(xs) <= 1, .5, 0.); f3 = npdf(xs, 3.5, .8)
fig, ax = figure(width_mm=100, height_mm=46)
panel(fig, left=.08, right=.98, top=.96, bottom=.2)
for f in (f1, f3):
    ax.plot(xs, f, color=BLUE, lw=1.1)
ax.plot(xs, f2, color=BLUE, lw=1.1, drawstyle='steps-mid')
ax.plot(xs, (f1+f2+f3)/3, color=YELLOW, lw=1.6, ls=DASH)
ax.plot(q, dens, color=GREEN, lw=1.4)
ax.set_xlim(-5, 6); ax.set_ylim(0, .9); ax.set_xticks([-3, 0, 3.5], ['-3', '0', '3.5']); ax.set_xlabel('$x$', labelpad=1)
mean_b = float(np.mean(q))
save(fig, HERE, 'figure', {'barycenter_mean': mean_b, 'expected_mean': (-3+0+3.5)/3,
                           'barycenter_quantile_at_half': float(np.interp(.5, u, q))})
