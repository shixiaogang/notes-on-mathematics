from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# B*B=Lambda：x=0.4 时重叠长度 0.6；频域 sinc 与 sinc^2。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.28, wspace=.22)
ax = axes[0]; x0 = .4
ax.fill_between([x0-.5, .5], 0, 1, color=BLUE_FILL, lw=0)
ax.plot([-1.2, -.5, -.5, .5, .5, 1.2], [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.4)
ax.plot([-1.2, x0-.5, x0-.5, x0+.5, x0+.5, 1.2], [0, 0, 1, 1, 0, 0], color=PURPLE, lw=1.2, ls=(0, (3, 2)))
ax.annotate('', xy=(x0-.5, .5), xytext=(.5, .5), arrowprops=dict(arrowstyle='<->', lw=.85, color=INK, shrinkA=0, shrinkB=0))
ax.text(.2, .57, '$0.6$', ha='center', va='bottom')
ax.set_xlim(-1.2, 1.2); ax.set_ylim(-.05, 1.25); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$y$', labelpad=0)
ax = axes[1]
x = np.linspace(-1.5, 1.5, 601)
ax.plot(x, np.maximum(0, 1-np.abs(x)), color=BLUE, lw=1.4)
ax.plot([x0], [1-x0], 'o', ms=3.6, color=INK, mew=0)
ax.text(.47, .64, r'$\Lambda(0.4)=0.6$', ha='left', va='bottom')
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-.05, 1.25); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[2]
xi = np.linspace(-3.5, 3.5, 1500)
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(xi, np.sinc(xi), color=GREEN, lw=1.2, ls=(0, (3, 2)))
ax.plot(xi, np.sinc(xi)**2, color=GREEN, lw=1.4)
ax.set_xlim(-3.5, 3.5); ax.set_ylim(-.3, 1.12); ax.set_xticks([-3, 0, 3]); ax.set_yticks([0, 1]); ax.set_xlabel(r'$\xi$', labelpad=0)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '(B*B)(x)=max(0,1-|x|), Fourier sinc^2'})
