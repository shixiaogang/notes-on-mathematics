from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# (a) weights |x|^p for p = 1/2, 1, 2, 4: larger p puts more weight on large |x|.
# (b) reward table: (E|X|^p)^(1/p) increases with p (Lyapunov) towards max value 6.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, right=.98, bottom=.3, wspace=.3)
ax = axes[0]
x = np.linspace(-2.2, 2.2, 401)
for p, c, ls in [(.5, PURPLE, DASH), (1, YELLOW, '-'), (2, BLUE, '-'), (4, GREEN, '-')]:
    ax.plot(x, np.abs(x)**p, color=c, lw=1.4 if ls == '-' else 1.0, ls=ls)
lab(ax, 2.15, 1.05, '$p=1/2$', PURPLE, ha='right', va='top')
lab(ax, -2.15, 2.4, '$p=1$', YELLOW, ha='left', va='bottom')
lab(ax, -2.05, 4.7, '$p=2$', BLUE, ha='left', va='bottom')
lab(ax, -1.2, 6.0, '$p=4$', GREEN, ha='left')
ax.axvline(-1, color=STROKE, lw=.7, ls=DOT); ax.axvline(1, color=STROKE, lw=.7, ls=DOT)
ax.set_xlim(-2.2, 2.2); ax.set_ylim(0, 6.5); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([0, 1, 3, 6])
axlab(ax, '$x$', '$|x|^p$')
ax = axes[1]
p = np.linspace(.05, 20, 500)
L = np.array([((XV**q*PV).sum())**(1/q) for q in p])
ax.plot(p, L, color=BLUE, lw=1.4)
ax.axhline(6, color=PURPLE, lw=.9, ls=DASH)
for q in (1, 2, 3, 4):
    v = ((XV**q*PV).sum())**(1/q); dot(ax, q, v, color=RED, ms=3.6)
lab(ax, 19.5, 6.15, '最大值 6', PURPLE, ha='right', va='bottom')
ax.set_xlim(0, 20); ax.set_ylim(0, 7); ax.set_xticks([0, 1, 2, 3, 4, 10, 20]); ax.set_yticks([0, 2, 3, 6])
axlab(ax, '$p$', '$(\\mathrm{E}|X|^p)^{1/p}$')
tags(fig, axes)
save(fig, HERE, 'figure', {'Lp at 1..4': [float(((XV**q*PV).sum())**(1/q)) for q in (1, 2, 3, 4)]})
