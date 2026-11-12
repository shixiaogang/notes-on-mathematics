from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Z ~ N(0,1): moment bound E|Z|^p / t^p as a function of the order p, for t=2 and t=3; dashed lines are exact P(|Z|>=t).
ps = np.arange(1, 15)
fig, ax = figure(width_mm=96, height_mm=54)
for t, c in ((2, BLUE), (3, GREEN)):
    b = np.array([normal_abs_moment(p)/t**p for p in ps])
    ax.semilogy(ps, b, '-o', color=c, lw=1.2, ms=3.2, mew=0)
    j = int(np.argmin(b)); ax.plot([ps[j]], [b[j]], 'o', ms=5, mfc='none', mec=RED, mew=1.1)
    ax.axhline(2*Q(t), color=c, lw=.9, ls=DASH)
lab(ax, 13.8, 6.5, '$t=2$', BLUE, ha='right'); lab(ax, 13.8, .021, '$t=3$', GREEN, ha='right', va='top')
ax.set_xlim(.5, 14.5); ax.set_ylim(1e-3, 20); logticks(ax, [1, 0, -1, -2, -3]); ax.set_xticks([1, 2, 4, 6, 8, 10, 12, 14])
axlab(ax, '$p$', r'$\mathbb{E}|Z|^p/t^p$'.replace(r'\mathbb{E}', '\U0001D53C') if False else '矩上界')
save(fig, HERE, 'figure', {'t2_best_p': 4, 't2_best': normal_abs_moment(4)/16, 't3_best_p': 9, 't3_best': normal_abs_moment(9)/3**9})
