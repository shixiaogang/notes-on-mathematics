from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Reward table shifted by b: raw moments of X+b change with b, central moments do not.
# m2(b) = 9 + 4b + b^2 ; m3(b) = E[(X+b)^3]; c2 = 5, c3 = 7.
b = np.linspace(-6, 4, 400)
m2 = np.array([((XV+t)**2*PV).sum() for t in b])
m3 = np.array([((XV+t)**3*PV).sum() for t in b])
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.09, right=.98, bottom=.3, wspace=.3)
for ax, raw, c, k in [(axes[0], m2, 5, 2), (axes[1], m3, 7, 3)]:
    ax.plot(b, raw, color=BLUE, lw=1.4)
    ax.plot(b, c+0*b, color=YELLOW, lw=1.6)
    ax.axvline(-2, color=STROKE, lw=.7, ls=DOT)
    dot(ax, -2, c)
    lab(ax, 3.9, c+(3 if k == 2 else -12), f'{k}阶中心矩', YELLOW, ha='right', va='bottom' if k == 2 else 'top')
    ax.set_xlim(-6, 4); ax.set_xticks([-6, -4, -2, 0, 2, 4]); axlab(ax, '$b$')
axes[0].set_ylim(0, 45); axes[0].set_yticks([0, 5, 20, 40])
axes[1].set_ylim(-80, 330); axes[1].set_yticks([0, 7, 150, 300]); axes[1].set_yticklabels(['0', '', '150', '300'])
lab(axes[0], -5.8, 40, '$\\mathrm{E}[(X+b)^2]$', BLUE, ha='left', va='top')
lab(axes[1], -5.8, 300, '$\\mathrm{E}[(X+b)^3]$', BLUE, ha='left', va='top')
tags(fig, axes)
save(fig, HERE, 'figure', {'m2(0)': float(m2[np.argmin(abs(b))]), 'm3 at b=-2': float(np.interp(-2, b, m3))})
