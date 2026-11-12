"""A point chosen from n equally spaced positions k/n (k = 1..n) in (0,1].
(a) P(0.2 < X <= 0.5) = #{k: 0.2 < k/n <= 0.5}/n approaches the length 0.3.
(b) the probability 1/n of any single position tends to 0."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tidy(ax):
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(0.95)

from fractions import Fraction
n = np.arange(1, 61)
ratio = np.array([sum(1 for k in range(1, m + 1) if Fraction(1, 5) < Fraction(k, m) <= Fraction(1, 2)) / m for m in n])
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
ax = axes[0]
ax.plot(n, ratio, 'o', color=GREEN, ms=2.4)
ax.axhline(0.3, color=BLUE, lw=1.4)
ax.set_xlabel('格点数 n'); ax.set_ylabel('计数比'); ax.set_ylim(0, 0.6)
ax = axes[1]
ax.plot(n, 1 / n, 'o', color=GREEN, ms=2.4)
ax.axhline(0, color=BLUE, lw=1.4)
ax.set_xlabel('格点数 n'); ax.set_ylabel('单个格点的概率'); ax.set_ylim(-0.03, 1.05)
for a_, tag in zip(axes, ('(a)', '(b)')):
    tidy(a_); a_.set_xlim(0, 61)
    a_.text(0.5, -0.42, tag, transform=a_.transAxes, ha='center', va='top', fontsize=8)
save(fig, Path(__file__).resolve().parent, 'figure', {'event': '(0.2, 0.5]', 'ratios_n_4_10_60': [float(ratio[3]), float(ratio[9]), float(ratio[59])]})
print(ratio[3], ratio[9], ratio[6], ratio[59])
