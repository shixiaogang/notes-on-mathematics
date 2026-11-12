from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Standardized reward table Z=(X-2)/sqrt5 and standardized density Z=(X-2/3)*sqrt(18), X~2x on (0,1).
# Both have mean 0, variance 1, yet their shapes differ and neither is bell-shaped.
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.1, right=.98, bottom=.3, wspace=.32)
ax = axes[0]
z = (XV-2)/np.sqrt(5)
bars(ax, z, PV, width=.22)
ax.axvline(0, color=RED, lw=1.2)
for zi, p in zip(z, PV):
    lab(ax, zi, p+.02, f'{zi:.2f}', INK, ha='center', va='bottom')
ax.set_xlim(-3.9, 2.2); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_ylim(0, .62); ax.set_yticks([0, .25, .5]); axlab(ax, '$z$', '$p_Z(z)$')
ax = axes[1]
r = np.sqrt(18)
zz = np.linspace(-2/3*r, 1/3*r, 300)
f = 2*(2/3+zz/r)/r
ax.fill_between(zz, 0, f, color=BLUE_FILL, lw=0); ax.plot(zz, f, color=BLUE, lw=1.4)
ax.plot([zz[-1], zz[-1]], [0, f[-1]], color=BLUE, lw=1.0)
ax.axvline(0, color=RED, lw=1.2)
ax.set_xlim(-3.9, 2.2); ax.set_ylim(0, .55); ax.set_xticks([-2, -1, 0, 1, 2])
lab(ax, -2.9, .05, '$-2\\sqrt{2}$', INK, ha='right', va='bottom'); lab(ax, 1.41, .49, '$\\sqrt{2}$', INK, ha='center', va='bottom')
ax.set_yticks([0, .25, .5]); axlab(ax, '$z$', '$f_Z(z)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'z table': z.tolist(), 'mean z density': float(np.trapezoid(zz*f, zz)), 'var z density': float(np.trapezoid(zz**2*f, zz))})
