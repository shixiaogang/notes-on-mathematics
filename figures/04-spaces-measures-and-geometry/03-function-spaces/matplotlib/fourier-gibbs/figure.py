from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# 方波部分和 S_N（N=2n-1），第一个峰在 x=pi/(2n)，极限高度 (2/pi)Si(pi)=1.17898。
def S(N, x):
    return 4/np.pi*sum(np.sin(k*x)/k for k in range(1, N+1, 2))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.15]})
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.96, bottom=.26, wspace=.22)
ax = axes[0]
x = np.linspace(-np.pi, np.pi, 3001)
ax.plot([-np.pi, 0], [-1, -1], color=BLUE, lw=1.4); ax.plot([0, np.pi], [1, 1], color=BLUE, lw=1.4)
ax.plot(x, S(9, x), color=YELLOW, lw=1.4)
ax.plot([0], [0], 'o', ms=3.6, color=INK, mew=0)
ax.set_xlim(-np.pi, np.pi); ax.set_ylim(-1.45, 1.45)
ax.set_xticks([-np.pi, 0, np.pi]); ax.set_xticklabels([r'$-\pi$', '$0$', r'$\pi$']); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
x = np.linspace(0, .78, 6001)
ax.plot([0, .78], [1, 1], color=BLUE, lw=1.4)
ax.axhline(1.17898, color=MUTED, lw=.85, ls=(0, (3, 2)))
for N, c in ((9, YELLOW), (25, GREEN), (81, PURPLE)):
    ax.plot(x, S(N, x), color=c, lw=1.2)
    n = (N+1)//2; p = np.pi/(2*n)
    ax.plot([p], [S(N, np.array([p]))[0]], 'o', ms=3.2, color=c, mew=0)
ax.text(.314, 1.205, '$N=9$', ha='center', va='bottom', color=INK)
ax.text(.121, 1.205, '$25$', ha='center', va='bottom', color=INK)
ax.text(.038, 1.205, '$81$', ha='center', va='bottom', color=INK)
ax.text(.77, 1.195, '$1.179$', ha='right', va='bottom', color=MUTED)
ax.set_xlim(0, .78); ax.set_ylim(.7, 1.32); ax.set_xticks([0, .25, .5, .75]); ax.set_yticks([.8, 1, 1.2]); ax.set_xlabel('$x$', labelpad=0)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'S_N of square wave, N=9,25,81; limit of first peak (2/pi)Si(pi)=1.17898'})
