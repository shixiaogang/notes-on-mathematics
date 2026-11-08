from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# p_k=e^{-1}/k!, m_k=2^{-(k+1)}, h=p/m, k=0..5
from math import factorial, e
K = np.arange(6)
p = np.array([1/(e*factorial(int(k))) for k in K]); m = 2.0**(-(K+1)); h = p/m
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
a, b = axes
a.bar(K, m, width=.72, facecolor='none', edgecolor=GREEN, lw=.9, ls=(0, (3, 2)))
a.bar(K, p, width=.46, facecolor=BLUE_FILL, edgecolor=BLUE, lw=.75)
a.text(.72, .47, r'$m_k$', ha='left', va='center'); a.text(1.32, .33, r'$p_k$', ha='left', va='center')
a.set_ylim(0, .56); a.set_yticks([0, .25, .5]); a.set_yticklabels(['0', '0.25', '0.5'])
b.bar(K, h, width=.56, facecolor=BLUE_FILL, edgecolor=BLUE, lw=.75)
for k, v in zip(K, h): b.text(k, v+.04, f'{v:.2f}', ha='center', va='bottom', fontsize=7.5)
b.text(4.7, 1.18, r'$h(k)=p_k/m_k$', ha='center', va='center')
b.axhline(1, color=MUTED, lw=.85, ls=(0, (1.6, 1.4))); b.set_ylim(0, 1.75); b.set_yticks([0, 1])
for ax in axes:
    ax.set_xticks(K); ax.set_xlim(-.6, 5.6)
fig.set_layout_engine(None); fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.22, wspace=.22)
for ax, s in zip(axes, ['(a)', '(b)']):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p_k=e^-1/k!, m_k=2^-(k+1), h=p/m', 'h': [round(float(v), 4) for v in h]})
