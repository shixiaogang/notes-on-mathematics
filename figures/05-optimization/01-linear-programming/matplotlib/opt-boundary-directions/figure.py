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

# 资源分配的最优点 (2,2)：梯度 (-3,-2)，可行方向锥由 (-1,1) 与 (1,-2) 张成。
fig, ax = figure(width_mm=88, height_mm=66)
poly=np.array([[0.5,0.5],[2.75,.5],[2,2],[.5,3.5]])
ax.fill(poly[:,0],poly[:,1],facecolor=BLUE_FILL,edgecolor='none',zorder=0)
ax.plot([.5,2],[3.5,2],color=STROKE,lw=1.6,zorder=2); ax.plot([2.75,2],[.5,2],color=STROKE,lw=1.6,zorder=2)
s=np.array([2,2.9]); ax.plot(s,4-s,color=STROKE,lw=.85,ls=(0,(3,2)),zorder=1); s=np.array([1.55,2]); ax.plot(s,6-2*s,color=STROKE,lw=.85,ls=(0,(3,2)),zorder=1)
for c in (10,):
    x=np.array([1.75,3.0]); ax.plot(x,(c-3*x)/2,color=BLUE,lw=.95,ls=(0,(4,2.2)),zorder=1)
arr=lambda p,q,c,lw=1.15:ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color=c,lw=lw,mutation_scale=8,shrinkA=0,shrinkB=0),zorder=5)
arr((2,2),(2+.42*-1.8/1.8*1.8,2+.42*1.8),GREEN) if 0 else None
arr((2,2),(1.2,2.8),GREEN); arr((2,2),(2.55,.9),GREEN); arr((2,2),(1.2,1.5),GREEN)
arr((2,2),(2+3*.27,2+2*.27),INK)
ax.plot([2],[2],'o',ms=5,color=RED,mew=0,zorder=6)
ax.text(1.32,2.92,'$d_1$',ha='left',va='bottom'); ax.text(2.68,1.0,'$d_2$',ha='left',va='center'); ax.text(1.14,1.46,'$d_3$',ha='right',va='top')
ax.text(2.86,2.56,r'$-\nabla f$',ha='left',va='bottom')
ax.text(.75,.82,'可行域',color=INK)
ax.set_xlim(.5,3.6); ax.set_ylim(.5,3.5); ax.set_aspect('equal'); ax.set_xticks([1,2,3]); ax.set_yticks([1,2,3]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=2)
save(fig, HERE, 'figure', {'xstar':[2,2],'grad':[-3,-2],'cone':[[-1,1],[1,-2]],'d3':[-.8,-.5]})
