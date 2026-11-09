from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# 固定端点 u(0)=0,u(1)=1 的候选及其与 u0=x 的差。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.075, wspace=.24, bottom=.25)
u0 = X
cands = [(X**2, BLUE, '-', '$x^2$'), (X+.25*np.sin(2*np.pi*X), YELLOW, '-', ''), (np.sinh(X)/np.sinh(1), GREEN, '-', '')]
ax = axes[0]
ax.plot(X, u0, color=STROKE, lw=1.1, ls=(0, (3, 2)))
for y, c, l, s in cands: ax.plot(X, y, color=c, lw=1.4, ls=l)
ax.plot([0, 1], [0, 1], 'o', ms=4.4, color=STROKE, mew=0, zorder=6)
ax.text(.62, .17, '$x^2$', color=BLUE, fontsize=8); ax.text(.03, .74, r'$x+\frac{1}{4}\sin 2\pi x$', color=YELLOW, fontsize=8)
ax.text(.72, .84, '$x$', color=STROKE, fontsize=8)
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.12, 1.12); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$u$', labelpad=-2)
ax = axes[1]
ax.axhline(0, color=MUTED, lw=.85)
for y, c, l, s in cands: ax.plot(X, y-u0, color=c, lw=1.4, ls=l)
ax.plot([0, 1], [0, 0], 'o', ms=4.4, color=STROKE, mew=0, zorder=6)
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.31, .31); ax.set_xticks([0, 1]); ax.set_yticks([-.25, 0, .25]); ax.set_yticklabels(['$-0.25$', '0', '0.25']); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel(r'$\eta=u-x$', labelpad=-2)
tags(fig, axes)
save(fig, HERE, 'figure', {'candidates': ['x^2', 'x+sin(2 pi x)/4', 'sinh x/sinh 1'], 'u0': 'x'})
