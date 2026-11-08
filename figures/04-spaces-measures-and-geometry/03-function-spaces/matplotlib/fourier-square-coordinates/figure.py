from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# 方波 f=sgn(x) 在 (-pi,pi)；系数 |f^(k)|=2/(pi|k|)（k 奇），S_5 由 k=1,3,5 三项正弦组成。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.96, bottom=.26, wspace=.27)
ax = axes[0]
x = np.linspace(-np.pi, np.pi, 1400)
for k in (1, 3, 5):
    ax.plot(x, 4/(np.pi*k)*np.sin(k*x), color=MUTED, lw=.85)
S5 = sum(4/(np.pi*k)*np.sin(k*x) for k in (1, 3, 5))
ax.plot([-np.pi, 0], [-1, -1], color=BLUE, lw=1.4); ax.plot([0, np.pi], [1, 1], color=BLUE, lw=1.4)
ax.plot(x, S5, color=YELLOW, lw=1.4)
ax.set_xlim(-np.pi, np.pi); ax.set_ylim(-1.45, 1.62)
ax.set_xticks([-np.pi, 0, np.pi]); ax.set_xticklabels([r'$-\pi$', '$0$', r'$\pi$']); ax.set_yticks([-1, 0, 1])
ax.set_xlabel('$x$', labelpad=0)
ax.text(1.0, .84, '$f$', color=BLUE, ha='center', va='top')
ax.text(.62, 1.32, '$S_5f$', color=INK, ha='center', va='bottom')
ax = axes[1]
K = np.arange(-9, 10)
c = np.array([2/(np.pi*abs(k)) if k % 2 else 0. for k in K])
kept = np.abs(K) <= 5
ax.vlines(K[kept], 0, c[kept], color=GREEN, lw=1.2); ax.plot(K[kept], c[kept], 'o', ms=3.4, color=GREEN, mew=0)
ax.vlines(K[~kept], 0, c[~kept], color=RED, lw=1.2); ax.plot(K[~kept], c[~kept], 'o', ms=3.4, color=RED, mew=0)
ax.set_xlim(-10, 10); ax.set_ylim(0, .75); ax.set_xticks([-9, -5, -1, 1, 5, 9]); ax.set_yticks([0, .2, .4, .6])
ax.set_xlabel('$k$', labelpad=0); ax.set_ylabel(r'$|\widehat{f}(k)|$', labelpad=1)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'square wave, S_5=(4/pi)(sin x+sin 3x/3+sin 5x/5), |c_k|=2/(pi|k|) for odd k'})
