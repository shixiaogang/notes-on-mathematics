from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Sup-norm recovery fails for sign(x) and sin(x^2).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.25, bottom=.27)
ax = axes[0]; xx = np.linspace(-.5, .5, 1200); cc = shades(3)
ax.plot(xx[xx < 0], -1+0*xx[xx < 0], color=RED, lw=1.5); ax.plot(xx[xx > 0], 1+0*xx[xx > 0], color=RED, lw=1.5)
for t, c in zip((.001, .01), cc[1:]): ax.plot(xx, erf(xx/(2*np.sqrt(t))), color=c, lw=1.4)
dot(ax, 0, 0, BLUE, ms=4.2)
ax.set_xlim(-.5, .5); ax.set_ylim(-1.15, 1.15); ax.set_xticks([-.4, 0, .4]); ax.set_yticks([-1, 0, 1]); axlab(ax, yl='$u$')
ax = axes[1]; xx = np.linspace(0, 8, 8000); t = .02
z = (1-4j*t); U = (z**-.5*np.exp(1j*xx**2/z)).imag
env = (1+16*t**2)**-.25*np.exp(-4*xx**2*t/(1+16*t**2))
ax.plot(xx, np.sin(xx**2), color=RED, lw=.75); ax.plot(xx, U, color=BLUE, lw=1.2); ax.plot(xx, env, color=PURPLE, lw=1, ls=DASH); ax.plot(xx, -env, color=PURPLE, lw=1, ls=DASH)
ax.set_xlim(0, 8); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([-1, 0, 1]); axlab(ax)
tags(fig, axes)
yq = np.linspace(-30, 30, 3000001); x0 = 2.; q = float(np.trapezoid(gauss(x0-yq, t)*np.sin(yq**2), yq)); c = float((z**-.5*np.exp(1j*x0**2/z)).imag)
save(fig, HERE, 'figure', {'quadrature u(2,.02)': q, 'closed': c}); print(q, c)
