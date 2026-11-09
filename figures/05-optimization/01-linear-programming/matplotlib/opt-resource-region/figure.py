from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')

# 资源分配：max 3x1+2x2, s.t. x1+x2<=4, 2x1+x2<=6, x>=0。最优点 (2,2)，利润 10。
fig, ax = figure(width_mm=88, height_mm=66)
poly = np.array([[0,0],[3,0],[2,2],[0,4]])
ax.fill(poly[:,0], poly[:,1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.9, zorder=1)
ax.plot([0,2],[4,2], color=STROKE, lw=1.7, zorder=3, solid_capstyle='round')
ax.plot([2,3],[2,0], color=STROKE, lw=1.7, zorder=3, solid_capstyle='round')
for c in (4, 8, 10):
    x = np.array([-.2, 4.0]); y = (c-3*x)/2
    ax.plot(x, y, color=BLUE, lw=.95, ls=(0,(4,2.2)), zorder=2)
for c,dx,fc in ((4,.05,BLUE_FILL),(8,.05,BLUE_FILL),(10,.07,'white')):
    y=.22; ax.text((c-2*y)/3+dx, y, f'{c}', color=BLUE, fontsize=7.5, va='center', ha='left', bbox=dict(fc=fc, ec='none', pad=.5), zorder=4)
ax.annotate('', xy=(4.32, 3.15), xytext=(3.6, 2.67), arrowprops=dict(arrowstyle='-|>', color=INK, lw=.85, mutation_scale=7, shrinkA=0, shrinkB=0))
ax.text(4.36, 3.2, '利润增大', fontsize=7.5, ha='right', va='bottom', color=MUTED)
ax.plot([2],[2],'o',ms=5,color=RED,mew=0,zorder=5)
ax.text(2.14, 2.1, '$(2,2)$', ha='left', va='bottom', color=INK)
ax.text(.42, 1.1, '可行域', color=INK)
ax.text(1.12, 3.2, r'$x_1+x_2=4$', fontsize=7.5, color=STROKE, ha='left', va='bottom')
ax.text(2.98, .98, r'$2x_1+x_2=6$', fontsize=7.5, color=STROKE, ha='left', va='center')
ax.set_xlim(-.2, 4.6); ax.set_ylim(-.2, 4.6)
ax.set_xticks([0,1,2,3,4]); ax.set_yticks([0,1,2,3,4])
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=2)
save(fig, HERE, 'figure', {'problem': 'max 3x1+2x2 s.t. x1+x2<=4, 2x1+x2<=6, x>=0', 'optimum': [2,2], 'value': 10})

