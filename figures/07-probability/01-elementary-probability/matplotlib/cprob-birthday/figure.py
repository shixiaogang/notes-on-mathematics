"""Birthday problem: P(at least two of n people share a birthday) with 365
equally likely days, exact 1 - P(365,n)/365^n, and the approximation
1 - exp(-n(n-1)/730)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tidy(ax):
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(0.95)

n = np.arange(1, 71)
exact = np.array([1 - np.prod([(365 - i) / 365 for i in range(m)]) for m in n])
approx = 1 - np.exp(-n * (n - 1) / 730)
fig, ax = figure(width_mm=96, height_mm=50)
ax.plot(n, exact, color=BLUE, lw=1.4, label='精确值')
ax.plot(n, approx, color=PURPLE, lw=1.1, ls=(0, (4, 2)), label='近似 1−exp(−n(n−1)/730)')
ax.axhline(0.5, color='#4C4D4F', lw=0.85, ls=(0, (2, 2)))
ax.plot([23], [exact[22]], 'o', color=RED, ms=4.5, zorder=4)
ax.annotate(f'n=23，{exact[22]:.3f}', (23, exact[22]), xytext=(30, 0.36), fontsize=7.5, color=INK,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
ax.set_xlim(0, 70); ax.set_ylim(0, 1.02)
ax.set_xlabel('人数 n'); ax.set_ylabel('至少两人同一天生日的概率')
ax.legend(loc='lower right', handlelength=1.8)
tidy(ax)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '1 - prod_{i<n}(365-i)/365', 'n23': float(exact[22]), 'n50': float(exact[49])})
print(exact[22], exact[49], approx[22])
