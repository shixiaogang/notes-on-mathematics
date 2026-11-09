from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# (a) Weierstrass：J=int_{-1}^1 x^2 u'^2，u_k=clip(kx,-1,1)；(b) W^{1,1}：u_k=x^k。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.26, bottom=.24)
ax = axes[0]
x = np.linspace(-1, 1, 1601)
for k, c in ((2, YELLOW), (5, BLUE), (30, GREEN)):
    ax.plot(x, np.clip(k*x, -1, 1), color=c, lw=1.4)
ax.plot([-1, 1], [-1, 1], 'o', ms=4.4, color=STROKE, mew=0, zorder=6)
ax.text(.52, .55, '$k=2$', color=YELLOW, fontsize=7.5, ha='center'); ax.text(.22, 1.09, '$k=5$', color=BLUE, fontsize=7.5, ha='center'); ax.text(-.2, .8, '$k=30$', color=GREEN, fontsize=7.5, ha='right')
ax.set_xlim(-1.06, 1.06); ax.set_ylim(-1.2, 1.3); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$u^{(k)}$', labelpad=-2)
ax = axes[1]
for k, c in ((1, YELLOW), (4, BLUE), (40, GREEN)):
    ax.plot(X, X**k, color=c, lw=1.4)
ax.plot([0, 1], [0, 1], 'o', ms=4.4, color=STROKE, mew=0, zorder=6)
ax.text(.34, .42, '$k=1$', color=YELLOW, fontsize=7.5, ha='right'); ax.text(.68, .12, '$k=4$', color=BLUE, fontsize=7.5); ax.text(.82, .62, '$k=40$', color=GREEN, fontsize=7.5, ha='right')
ax.set_xlim(-.03, 1.06); ax.set_ylim(-.06, 1.12); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$u^{(k)}$', labelpad=-2)
tags(fig, axes)
k = np.array([2, 5, 30])
save(fig, HERE, 'figure', {'a': 'clip(kx,-1,1)', 'J_a': (2/(3*k)).tolist(), 'seminorm2_a': (2*k).tolist(), 'b': 'x^k', 'J_b': (1+1/(2*np.array([1,4,40])+1)).tolist()})
