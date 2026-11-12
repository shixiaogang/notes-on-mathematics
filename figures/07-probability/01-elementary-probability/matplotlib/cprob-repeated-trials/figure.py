"""Probability of at least one success in n independent repetitions,
1 - (1-p)^n, for p = 1/6 (a six with one die) and p = 1/36 (double six with two dice)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tidy(ax):
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(0.95)

n = np.arange(1, 41)
a = 1 - (5/6) ** n
b = 1 - (35/36) ** n
fig, ax = figure(width_mm=96, height_mm=50)
ax.plot(n, a, '-o', color=BLUE, lw=1.4, ms=2.4, label='p=1/6')
ax.plot(n, b, '-o', color=YELLOW, lw=1.4, ms=2.4, label='p=1/36')
ax.axhline(0.5, color='#4C4D4F', lw=0.85, ls=(0, (2, 2)))
ax.plot([4], [a[3]], 'o', color=RED, ms=4.5, zorder=4)
ax.plot([24], [b[23]], 'o', color=RED, ms=4.5, zorder=4)
ax.text(5, a[3] - 0.04, f'n=4，{a[3]:.4f}', fontsize=7.5, va='top')
ax.text(24.5, b[23] - 0.04, f'n=24，{b[23]:.4f}', fontsize=7.5, va='top')
ax.set_xlim(0, 40.5); ax.set_ylim(0, 1.02)
ax.set_xlabel('重复次数 n'); ax.set_ylabel('至少成功一次的概率')
ax.legend(loc='lower right', handlelength=1.8)
tidy(ax)
save(fig, Path(__file__).resolve().parent, 'figure', {'p1_n4': float(a[3]), 'p2_n24': float(b[23]), 'p2_n25': float(b[24])})
print(a[3], b[23], b[24])
