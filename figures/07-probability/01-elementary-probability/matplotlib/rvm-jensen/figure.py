from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# (a) f(x)=x^2 and the reward table: points (x_i, x_i^2) weighted by p_i have
#     centre of mass (E X, E X^2) = (2, 9), above f(E X) = 4; supporting line y = 4 + 4(x-2).
# (b) two-point X = 2 -/+ s with prob 1/2 each, f = exp: gap E f(X) - f(E X) = e^2 (cosh s - 1).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, wspace=.3)
ax = axes[0]
x = np.linspace(-.6, 6.6, 400)
ax.plot(x, x**2, color=BLUE, lw=1.4)
ax.plot(x, 4+4*(x-2), color=PURPLE, lw=.9, ls=DASH)
ax.fill([0, 3, 6], [0, 9, 36], color=BLUE_FILL, lw=0, zorder=1)
for xi, pi_ in zip(XV, PV):
    dot(ax, xi, xi**2, color=BLUE, ms=3.2+10*pi_)
dot(ax, 2, 9, color=GREEN, ms=5)
dot(ax, 2, 4, color=RED, ms=5)
ax.plot([2, 2], [4, 9], color=STROKE, lw=.85, ls=DOT)
lab(ax, 2.3, 10.2, '$(2,9)$', GREEN, ha='left', va='bottom')
lab(ax, 2.35, 3.0, '$(2,4)$', RED, ha='left', va='top')
lab(ax, 4.3, 25, '$x^2$', BLUE, ha='right')
ax.set_xlim(-.6, 6.6); ax.set_ylim(-4, 38); ax.set_xticks([0, 2, 3, 6]); ax.set_yticks([0, 4, 9, 36])
axlab(ax, '$x$')
ax = axes[1]
s = np.linspace(0, 2, 300)
ax.plot(s, np.exp(2)*np.cosh(s), color=GREEN, lw=1.4)
ax.plot(s, np.exp(2)+0*s, color=RED, lw=1.4)
ax.fill_between(s, np.exp(2), np.exp(2)*np.cosh(s), color=RED_FILL, lw=0)
lab(ax, 1.95, np.exp(2)*np.cosh(2)-1, r'$\mathrm{E}[\mathrm{e}^{X}]$', GREEN, ha='right', va='top')
lab(ax, 1.95, np.exp(2)-.6, r'$\mathrm{e}^{\mathrm{E}X}=\mathrm{e}^2$', RED, ha='right', va='top')
ax.set_xlim(0, 2); ax.set_ylim(0, 30); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 7.389, 20]); ax.set_yticklabels(['0', '7.39', '20'])
axlab(ax, '$s$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E X^2': float((XV**2*PV).sum()), 'gap s=1': float(np.exp(2)*(np.cosh(1)-1))})
