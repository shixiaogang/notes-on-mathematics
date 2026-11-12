"""Two fair coins tossed repeatedly (n = 2000 rounds, seed 3). Running relative
frequency of (a) two heads and (b) one head one tail, against the classical values
1/4 and 1/2 (four equally likely ordered outcomes) and the value 1/3 obtained by
wrongly treating {two heads, two tails, one each} as equally likely."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

rng = np.random.default_rng(3)
n = 2000
c = rng.integers(0, 2, size=(n, 2))  # 1 = heads
heads = c.sum(axis=1)
k = np.arange(1, n + 1)
f2 = np.cumsum(heads == 2) / k
f1 = np.cumsum(heads == 1) / k

fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
for ax, f, true, tag in ((axes[0], f2, 0.25, '(a)'), (axes[1], f1, 0.5, '(b)')):
    ax.plot(k, f, color=GREEN, lw=1.1)
    ax.axhline(true, color=BLUE, lw=1.4)
    ax.axhline(1/3, color=YELLOW, lw=1.4, ls=(0, (4, 2)))
    ax.set_xscale('log')
    ax.set_xlim(1, n)
    ax.set_ylim(0, 1)
    ax.set_xlabel('轮数')
    for sp in ('left', 'bottom'):
        ax.spines[sp].set_linewidth(0.95)
    ax.text(0.5, -0.42, tag, transform=ax.transAxes, ha='center', va='top', fontsize=8)
    below = true < 1/3
    ax.text(n * 0.9, true + (-0.035 if below else 0.035), '1/4' if true == 0.25 else '1/2', color=BLUE, ha='right', va='top' if below else 'bottom', fontsize=7.5)
    ax.text(n * 0.9, 1/3 + (0.035 if below else -0.035), '1/3', color=YELLOW, ha='right', va='bottom' if below else 'top', fontsize=7.5)
    ax.set_xticks([1, 10, 100, 1000]); ax.set_xticklabels(['1', '10', '100', '1000'])
axes[0].set_ylabel('相对频率')
save(fig, Path(__file__).resolve().parent, 'figure',
     {'n': n, 'seed': 3, 'final_freq_two_heads': float(f2[-1]), 'final_freq_one_each': float(f1[-1])})
print(f2[-1], f1[-1])
