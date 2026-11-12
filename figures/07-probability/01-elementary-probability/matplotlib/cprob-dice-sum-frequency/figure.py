"""Two fair dice: classical probability of each sum (count/36) versus the naive
assignment 1/11 per sum, and simulated relative frequencies (n = 3600, seed 7)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

sums = np.arange(2, 13)
counts = np.array([sum(1 for i in range(1, 7) for j in range(1, 7) if i + j == s) for s in sums])
p = counts / 36
rng = np.random.default_rng(7)
n = 3600
rolls = rng.integers(1, 7, size=(n, 2)).sum(axis=1)
freq = np.array([(rolls == s).mean() for s in sums])

fig, ax = figure(width_mm=100, height_mm=50)
ax.bar(sums, p, width=0.62, color=BLUE_FILL, edgecolor=BLUE, linewidth=0.8, label='计数比 k/36', zorder=2)
ax.plot(sums, freq, 'o', color=GREEN, ms=3.6, label=f'频率（n={n}）', zorder=3)
ax.axhline(1/11, color=YELLOW, lw=1.4, ls=(0, (4, 2)), label='错误赋值 1/11', zorder=1)
ax.set_xticks(sums)
ax.set_xlabel('两枚骰子的点数和')
ax.set_ylabel('概率')
ax.set_ylim(0, 0.21)
ax.set_xlim(1.4, 12.6)
ax.legend(loc='upper right', handlelength=1.6, borderaxespad=0.2)
for sp in ('left', 'bottom'):
    ax.spines[sp].set_linewidth(0.95)
save(fig, Path(__file__).resolve().parent, 'figure',
     {'formula': 'P(sum=s) = #{(i,j): i+j=s}/36', 'counts': counts.tolist(),
      'simulation': {'n': n, 'seed': 7, 'freq': [round(x, 4) for x in freq]}})
print(dict(zip(sums.tolist(), np.round(freq, 4).tolist())))
