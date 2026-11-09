from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# E+beta/2 u(0)^2，u(1)=1：u=(cosh x+beta sinh x)/(cosh 1+beta sinh 1)。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.27, bottom=.27)
ax = axes[0]
c1, s1 = np.cosh(1), np.sinh(1)
for beta, col, lab, xy in ((0, GREEN, r'$\beta=0$', (.02, .72)), (1, YELLOW, r'$\beta=1$', (.02, .46)), (5, PURPLE, r'$\beta=5$', (.075, .27))):
    ax.plot(X, (np.cosh(X)+beta*np.sinh(X))/(c1+beta*s1), color=col, lw=1.4)
    ax.text(*xy, lab, color=col, fontsize=7.5)
ax.plot(X, np.sinh(X)/s1, color=BLUE, lw=1.4)
ax.text(.42, .22, r'固定端点', color=BLUE, fontsize=7.5)
ax.plot([0, .18], [1/c1, 1/c1], color=STROKE, lw=.85, ls=(0, (2, 2)))
ax.plot([1], [1], 'o', ms=4.4, color=STROKE, mew=0, zorder=6)
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.06, 1.12); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=-2)
ax = axes[1]
b = np.logspace(-2, 3, 200); val = .5*(s1+b*c1)/(c1+b*s1)
ax.semilogx(b, val, color=BLUE, lw=1.4)
ax.axhline(.5*s1/c1, color=GREEN, lw=1.1, ls=(0, (4, 2))); ax.axhline(.5*c1/s1, color=RED, lw=1.1, ls=(0, (4, 2)))
ax.text(1000, .5*s1/c1+.012, r'$\frac{1}{2}\tanh 1$', color=GREEN, fontsize=7.5, ha='right')
ax.text(.014, .5*c1/s1-.02, r'$\frac{1}{2}\coth 1$', color=RED, fontsize=7.5, va='top')
ax.set_xlim(.01, 1000); ax.set_ylim(.34, .7); ax.set_xticks([.01, 1, 100]); ax.minorticks_off(); ax.set_yticks([.4, .6]); ax.set_yticklabels(['0.4', '0.6']); ax.set_xlabel(r'$\beta$', labelpad=1); ax.set_ylabel(r'$J^*(\beta)$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'tanh/2': .5*s1/c1, 'coth/2': .5*c1/s1})
