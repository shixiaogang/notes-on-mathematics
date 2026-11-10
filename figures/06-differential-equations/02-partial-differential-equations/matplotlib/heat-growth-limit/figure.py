from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# u0=exp(a x^2), a=1/2: the convolution solution blows up at t=1/(4a)=1/2.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
a = .5; xx = np.linspace(-2, 2, 500)
U = lambda x, t: (1-4*a*t)**-.5*np.exp(a*x**2/(1-4*a*t))
ax = axes[0]; cc = shades(3)
ax.plot(xx, U(xx, 0), color=RED, lw=1.5)
for t, c in zip((.2, .35, .45), cc): ax.plot(xx, U(xx, t), color=c, lw=1.4)
lab(ax, 0, .35, '$t=0$', RED, ha='center'); lab(ax, 0, 8.8, '$t=0.45$', cc[2], ha='center')
ax.set_xlim(-2, 2); ax.set_ylim(0, 10); ax.set_xticks([-2, 0, 2]); ax.set_yticks([0, 5, 10]); axlab(ax, yl='$u$')
ax = axes[1]; T = np.linspace(0, .4985, 400)
ax.plot(T, (1-4*a*T)**-.5, color=BLUE, lw=1.4); ax.axvline(.5, color=RED, lw=1.2, ls=DASH)
# quadrature check of the closed form
y = np.linspace(-200, 200, 2000001)
chk = [(t, float(np.trapezoid(np.exp(-y**2/(4*t)+a*y**2)/np.sqrt(4*pi*t), y)), float((1-4*a*t)**-.5)) for t in (.1, .25, .4)]
for t, q, c in chk: dot(ax, t, q, GREEN, ms=4.2)
lab(ax, .48, 8.5, '$t=1/(4a)$', RED, ha='right')
ax.set_xlim(0, .55); ax.set_ylim(0, 10); ax.set_xticks([0, .25, .5]); ax.set_yticks([0, 5, 10]); axlab(ax, '$t$', '$u(0,t)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'check': chk}); print(chk)
