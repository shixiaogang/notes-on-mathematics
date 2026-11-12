from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Reward table X in {0,3,6}, p = (1/2,1/3,1/6).
# (a) E[(X-c)^2] = 5 + (c-2)^2, minimum 5 at c = E X = 2.
# (b) E|X-c| is piecewise linear, constant 2 on [0,3] (every median minimizes it).
c = np.linspace(-2, 8, 801)
sq = np.array([((XV-t)**2*PV).sum() for t in c])
ab = np.array([(np.abs(XV-t)*PV).sum() for t in c])
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.09, right=.98, bottom=.3, wspace=.3)
ax = axes[0]
ax.plot(c, sq, color=BLUE, lw=1.4)
ax.axhline(5, color=STROKE, lw=.85, ls=DOT)
dot(ax, 2, 5)
lab(ax, 2, 6.2, '$(2,\\,5)$', RED, ha='center', va='bottom')
ax.set_xlim(-2, 8); ax.set_ylim(0, 42); ax.set_xticks([0, 2, 3, 6]); ax.set_yticks([0, 5, 20, 40])
axlab(ax, '$c$', r'$\mathrm{E}[(X-c)^2]$')
ax = axes[1]
ax.plot(c, ab, color=BLUE, lw=1.4)
ax.plot([0, 3], [2, 2], color=RED, lw=2.4, solid_capstyle='butt')
dot(ax, 2, 2, color=INK, ms=3.6)
lab(ax, 1.5, 2.35, '$[0,3]$', RED, ha='center', va='bottom')
lab(ax, 2.1, 1.6, '均值 2', INK, ha='left', va='top')
ax.set_xlim(-2, 8); ax.set_ylim(0, 6.5); ax.set_xticks([0, 2, 3, 6]); ax.set_yticks([0, 2, 4, 6])
axlab(ax, '$c$', r'$\mathrm{E}|X-c|$')
tags(fig, axes)
save(fig, HERE, 'figure', {'min sq': float(sq.min()), 'argmin sq': float(c[sq.argmin()]), 'min abs': float(ab.min())})
