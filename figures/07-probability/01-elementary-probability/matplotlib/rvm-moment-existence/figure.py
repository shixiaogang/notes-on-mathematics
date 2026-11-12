from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Density f(x)=3x^{-4}, x>=1.  (a) integrands x^p f(x) = 3x^{p-4} for p=1,2,3 on log-log axes.
# (b) truncated moments int_1^M x^p f(x) dx = 3/2(1-M^-2), 3(1-M^-1), 3 ln M.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.11, right=.98, bottom=.3, wspace=.32)
x = np.logspace(0, 3, 400)
cols = {1: YELLOW, 2: BLUE, 3: RED}
ax = axes[0]
for p in (1, 2, 3):
    ax.plot(x, 3*x**(p-4.), color=cols[p], lw=1.4)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(1, 1e3); ax.set_ylim(1e-8, 5)
lab(ax, 300, 3*300**-3*4, '$p=1$', YELLOW, ha='left', va='bottom')
lab(ax, 300, 3*300**-2*4, '$p=2$', BLUE, ha='left', va='bottom')
lab(ax, 300, 3*300**-1*4, '$p=3$', RED, ha='left', va='bottom')
ax.set_xticks([1, 10, 100, 1000]); ax.set_xticklabels(['1', '10', '$10^2$', '$10^3$'])
ax.set_yticks([1e-8, 1e-4, 1]); ax.set_yticklabels(['$10^{-8}$', '$10^{-4}$', '1'])
axlab(ax, '$x$', '$x^p f(x)$')
ax = axes[1]
M = np.logspace(0, 4, 400)
ax.plot(M, 1.5*(1-M**-2.), color=YELLOW, lw=1.6)
ax.plot(M, 3*(1-1/M), color=BLUE, lw=1.4)
ax.plot(M, 3*np.log(M), color=RED, lw=1.4)
ax.axhline(1.5, color=STROKE, lw=.7, ls=DOT); ax.axhline(3, color=STROKE, lw=.7, ls=DOT)
lab(ax, 9000, 1.5-.25, '$p=1$', YELLOW, ha='right', va='top')
lab(ax, 9000, 3-.25, '$p=2$', BLUE, ha='right', va='top')
lab(ax, 300, 3*np.log(300)+.4, '$p=3$', RED, ha='right', va='bottom')
ax.set_xscale('log'); ax.set_xlim(1, 1e4); ax.set_ylim(0, 12)
ax.set_xticks([1, 10, 100, 1000, 10000]); ax.set_xticklabels(['1', '10', '$10^2$', '$10^3$', '$10^4$']); ax.set_yticks([0, 1.5, 3, 6, 12]); ax.set_yticklabels(['0', '1.5', '3', '6', '12'])
axlab(ax, '$M$', '截断矩')
tags(fig, axes)
save(fig, HERE, 'figure', {'M=1e4': [1.5*(1-1e-8), 3*(1-1e-4), 3*np.log(1e4)]})
