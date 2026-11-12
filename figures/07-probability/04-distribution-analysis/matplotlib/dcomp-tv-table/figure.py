from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Running example P=(0.6,0.3,0.1), Q=(0.3,0.3,0.4) on {0,1,2}.
# (a) the two probability tables; (b) the differences p_i - q_i; A*={p>q}={0}.
# d_TV = sum of positive parts = 0.3 = half the total absolute difference.
p, q, x = P_EX, Q_EX, X_EX
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.27, wspace=.3)
ax = axs[0]
bars(ax, x, p, BLUE, BLUE_FILL, width=.34, offset=-.18)
bars(ax, x, q, YELLOW, YELLOW_FILL, width=.34, offset=.18)
for xi, pi, qi in zip(x, p, q):
    lab(ax, xi-.18, pi+.02, f'{pi:.1f}', BLUE, ha='center', fontsize=7)
    lab(ax, xi+.18, qi+.02, f'{qi:.1f}', YELLOW, ha='center', fontsize=7)
lab(ax, 1.55, .58, '$P$', BLUE, ha='center', fontsize=8)
lab(ax, 1.95, .58, '$Q$', YELLOW, ha='center', fontsize=8)
ax.set_xticks(x); ax.set_ylim(0, .7); ax.set_xlim(-.6, 2.6)
ax.set_yticks([0, .2, .4, .6])
axlab(ax, '$x$', '概率')
ax = axs[1]
d = p-q
cols = [BLUE if v > 0 else RED for v in d]
fills = [BLUE_FILL if v > 0 else RED_FILL for v in d]
for xi, di, c, f in zip(x, d, cols, fills):
    if abs(di) > 1e-12:
        ax.bar([xi], [di], width=.5, color=f, edgecolor=c, linewidth=.8, zorder=2)
    lab(ax, xi, di+(.03 if di >= 0 else -.07), f'{di:+.1f}' if abs(di) > 1e-12 else '$0$', c if abs(di) > 1e-12 else INK, ha='center', fontsize=7)
ax.axhline(0, color=STROKE, lw=.85)
ax.set_xticks(x); ax.set_xlim(-.6, 2.6); ax.set_ylim(-.42, .42)
ax.set_yticks([-.3, 0, .3])
axlab(ax, '$x$', '$p_X(x)$ 之差')
ax.set_ylabel('$p(x)-q(x)$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'p': p.tolist(), 'q': q.tolist(), 'tv': float(.5*abs(d).sum())})
