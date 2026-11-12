"""Inspection of k items from N = 20 containing D = 4 defectives.
P(no defective) without replacement C(16,k)/C(20,k) versus with replacement 0.8^k."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tidy(ax):
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(0.95)

from math import comb
k = np.arange(0, 21)
wo = np.array([comb(16, int(m)) / comb(20, int(m)) for m in k])
wr = 0.8 ** k
fig, ax = figure(width_mm=96, height_mm=50)
ax.plot(k, wr, '-o', color=YELLOW, lw=1.4, ms=2.6, label='放回')
ax.plot(k, wo, '-o', color=BLUE, lw=1.4, ms=2.6, label='不放回')
ax.plot([5, 5], [wo[5], wr[5]], 'o', color=RED, ms=4.5, zorder=4)
ax.text(5.6, wr[5] + 0.02, f'{wr[5]:.3f}', fontsize=7.5, color=INK, va='bottom')
ax.text(4.4, wo[5] - 0.02, f'{wo[5]:.3f}', fontsize=7.5, color=INK, va='top', ha='right')
ax.set_xlim(-0.5, 20.5); ax.set_ylim(0, 1.03)
ax.set_xticks(range(0, 21, 4))
ax.set_xlabel('抽取件数 k'); ax.set_ylabel('样本中没有次品的概率')
ax.legend(loc='upper right', handlelength=1.8)
tidy(ax)
save(fig, Path(__file__).resolve().parent, 'figure', {'N': 20, 'D': 4, 'k5_without': float(wo[5]), 'k5_with': float(wr[5])})
print(wo[5], wr[5], wo[16], wo[17])
