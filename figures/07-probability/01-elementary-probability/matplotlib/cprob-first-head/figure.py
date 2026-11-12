"""Toss a fair coin until the first head. (a) P(first head at toss k) = 2^{-k};
(b) partial sums 1 - 2^{-k}, approaching 1 but never reached by finitely many outcomes."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tidy(ax):
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(0.95)

k = np.arange(1, 11)
p = 0.5 ** k
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
ax = axes[0]
ax.bar(k, p, width=0.6, color=BLUE_FILL, edgecolor=BLUE, linewidth=0.8)
ax.set_xticks(k); ax.set_xlabel('首次正面出现在第 k 次'); ax.set_ylabel('概率')
ax.set_ylim(0, 0.55)
ax = axes[1]
ax.step(k, np.cumsum(p), where='post', color=BLUE, lw=1.4)
ax.plot(k, np.cumsum(p), 'o', color=BLUE, ms=2.6)
ax.axhline(1, color=PURPLE, lw=1.0, ls=(0, (4, 2)))
ax.set_xticks(k); ax.set_xlabel('k'); ax.set_ylabel('前 k 项之和')
ax.set_ylim(0, 1.08)
for a_, tag in zip(axes, ('(a)', '(b)')):
    tidy(a_)
    a_.text(0.5, -0.42, tag, transform=a_.transAxes, ha='center', va='top', fontsize=8)
save(fig, Path(__file__).resolve().parent, 'figure', {'pmf': '2^-k', 'partial_sum_10': float(np.cumsum(p)[-1])})
