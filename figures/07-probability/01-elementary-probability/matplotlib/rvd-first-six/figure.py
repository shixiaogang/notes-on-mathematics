from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: N = number of throws of a fair die until the first six. p(k)=(5/6)^{k-1}/6, F(k)=1-(5/6)^k.
# Infinitely many values; the remaining mass beyond k=10 is (5/6)^10 ~ 0.1615.
K = 16
k = np.arange(1, K+1)
p = (5/6)**(k-1)/6
fig, axs = figure(width_mm=108, height_mm=46, ncols=2)
ax = axs[0]; style(ax)
bars(ax, k, p, width=.55)
ax.set_xlim(0, K+1); ax.set_ylim(0, .2); ax.set_xticks([1, 5, 10, 15]); ax.set_yticks([0, .1, 1/6]); ax.set_yticklabels(['0', '0.1', '1/6'])
ax.set_ylabel('$p_N(k)$')
sub(ax, 'a', '$k$')
ax = axs[1]; style(ax)
xs = np.r_[k, K+1.5]
cum = 1-(5/6)**k
step_cdf(ax, k, p, -.5, K+1.5, dots=False)
ax.plot(k, cum, 'o', ms=2.4, color=BLUE, zorder=4)
ax.axhline(1, color=LINE, lw=.85, ls=':')
ax.plot([10, 10], [cum[9], 1], color=RED, lw=2.0)
ax.text(9.5, (1+cum[9])/2, f'{(5/6)**10:.4f}', color=RED, fontsize=7.5, va='center', ha='right')
ax.set_xlim(-.5, K+1.5); ax.set_ylim(0, 1.08); ax.set_xticks([1, 5, 10, 15]); ax.set_yticks([0, .5, 1])
ax.set_ylabel('$F_N(x)$')
sub(ax, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'p1': 1/6, 'tail_after_10': (5/6)**10})
