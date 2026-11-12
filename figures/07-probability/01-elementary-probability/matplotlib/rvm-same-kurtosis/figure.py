from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Two standardized laws with the same kurtosis 12/5:
# (a) density 2x on (0,1) standardized (skewness -2 sqrt2/5); (b) symmetric table on {-a,0,a},
# P(+-a)=5/24 each, a = sqrt(12/5) so that the variance is 1; kurtosis 1/(2q) = 12/5.
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.1, right=.98, bottom=.3, wspace=.32)
r = np.sqrt(18)
zz = np.linspace(-2/3*r, 1/3*r, 300); f = 2*(2/3+zz/r)/r
ax = axes[0]
ax.fill_between(zz, 0, f, color=BLUE_FILL, lw=0); ax.plot(zz, f, color=BLUE, lw=1.4)
ax.plot([zz[-1], zz[-1]], [0, f[-1]], color=BLUE, lw=1.0)
ax.set_xlim(-3.2, 3.2); ax.set_ylim(0, .65); ax.set_xticks([-3, -2, -1, 0, 1, 2, 3]); ax.set_yticks([0, .25, .5])
axlab(ax, '$z$', '$f_Z(z)$')
ax = axes[1]
q = 5/24; a = np.sqrt(1/(2*q))
zs = np.array([-a, 0, a]); ps = np.array([q, 1-2*q, q])
bars(ax, zs, ps, width=.22, color=YELLOW, fill=YELLOW_FILL)
for z, p, s in zip(zs, ps, ['5/24', '7/12', '5/24']):
    lab(ax, z, p+.02, s, INK, ha='center', va='bottom')
ax.set_xlim(-3.2, 3.2); ax.set_ylim(0, .65); ax.set_xticks([-3, -2, -1, 0, 1, 2, 3]); ax.set_yticks([0, .25, .5])
axlab(ax, '$z$', '$p(z)$')
m, v, g, k = moments(zs, ps)
tags(fig, axes)
save(fig, HERE, 'figure', {'table': [m, v, g, k], 'a': a, 'density kurt': float(np.trapezoid(zz**4*f, zz))})
print(m, v, g, k, a, np.trapezoid(zz**4*f, zz))
