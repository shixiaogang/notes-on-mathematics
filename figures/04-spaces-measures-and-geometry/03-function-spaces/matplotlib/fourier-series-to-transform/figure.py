from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# 方框 B 以 T 为周期延拓，T c_k 落在 B^ 的频率 k/T 上。
fig, axes = figure(width_mm=112, height_mm=44, ncols=3, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.99, top=.95, bottom=.3, wspace=.09)
xi = np.linspace(-4.3, 4.3, 1500)
for ax, T in zip(axes, (2, 4, 8)):
    ax.axhline(0, color=MUTED, lw=.85)
    ax.plot(xi, np.sinc(xi), color=GREEN, lw=1.4)
    k = np.arange(-4*T, 4*T+1); w = k/T; y = np.sinc(w)
    ax.vlines(w, 0, y, color=YELLOW, lw=.95); ax.plot(w, y, 'o', ms=2.6, color=YELLOW, mew=0)
    ax.set_xlim(-4.3, 4.3); ax.set_ylim(-.3, 1.12); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([0, .5, 1])
    ax.set_xlabel(r'$\xi$', labelpad=0)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'B^(xi)=sin(pi xi)/(pi xi); T c_k=B^(k/T), T=2,4,8'})
