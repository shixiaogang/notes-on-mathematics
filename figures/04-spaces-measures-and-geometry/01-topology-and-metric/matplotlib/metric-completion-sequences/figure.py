from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
# q_n decimal truncations of sqrt2; y_{n+1}=(y_n+2/y_n)/2, y_1=1.
n = np.arange(1, 7)
q = np.floor(np.sqrt(2)*10.0**n)/10.0**n
y = [1.0]
for _ in range(5): y.append((y[-1]+2/y[-1])/2)
y = np.array(y)
fig, ax = figure(width_mm=92, height_mm=50)
ax.axhline(np.sqrt(2), color=RED, lw=.85, ls=(0, (3, 2)))
ax.plot(n, q, '-o', color=BLUE, lw=1.4, ms=3.2, mew=0)
ax.plot(n, y, '-s', color=GREEN, lw=1.4, ms=3, mew=0)
ax.set_xlim(.8, 6.9); ax.set_ylim(.95, 1.55)
ax.set_xticks(n); ax.set_yticks([1, 1.2, np.sqrt(2)]); ax.set_yticklabels(['1', '1.2', r'$\sqrt{2}$'])
ax.set_xlabel('$n$', labelpad=1)
ax.text(1.12, 1.455, '$q_n$', color=BLUE, ha='left', va='center')
ax.text(1.72, 1.525, '$y_n$', color=GREEN, ha='right', va='center')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'q_n=floor(sqrt2*10^n)/10^n; y_1=1, y_{n+1}=(y_n+2/y_n)/2'})
