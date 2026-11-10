from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# weak derivative on kink: u=1/2-|x-1/2|, smooth bump v
x = np.linspace(0, 1, 40001)
u = .5-np.abs(x-.5); du = np.where(x < .5, 1., -1.)
c, w = .52, .3
z = (x-c)/w
v = np.zeros_like(x); m = np.abs(z) < 1
v[m] = np.exp(1-1/(1-z[m]**2))
dv = np.zeros_like(x); dv[m] = v[m]*(-2*z[m]/(1-z[m]**2)**2)/w
I1 = np.trapezoid(du*v, x); I2 = np.trapezoid(-u*dv, x)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.25, bottom=.27)
ax = axes[0]
ax.plot(x, u, color=BLUE, lw=1.4); ax.plot(x, .45*v, color=PURPLE, lw=1.3)
dot(ax, .5, .5, RED, 4)
lab(ax, .15, .3, '$u$', BLUE); lab(ax, .78, .22, '$v$', PURPLE)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.01, .58); ax.set_xticks([0, 1]); ax.set_yticks([0, .5]); hat01(ax)
ax = axes[1]
ax.axhline(0, color=STROKE, lw=.6)
ax.plot(x, du*v, color=BLUE, lw=1.4); ax.plot(x, -u*dv, color=GREEN, lw=1.3)
lab(ax, .37, 1.2, "$u'v$", BLUE, ha='right'); lab(ax, .74, 2.2, "$-uv'$", GREEN, ha='left')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-3.2, 3.2); ax.set_xticks([0, 1]); ax.set_yticks([-3, 0, 3]); hat01(ax)
tags(fig, axes)
save(fig, HERE, 'figure', {'int_du_v': float(I1), 'int_minus_u_dv': float(I2), 'bump_center': c, 'bump_halfwidth': w})
print(I1, I2)
