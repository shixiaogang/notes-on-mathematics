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

# 资源分配：不可行点的目标值可以低于最优值。
fig, ax = figure(width_mm=88, height_mm=62)
poly=np.array([[1,1],[2.5,1],[2,2],[1,3]])
ax.fill(poly[:,0],poly[:,1],facecolor=BLUE_FILL,edgecolor='none',zorder=0)
s=np.array([1,2.0]); ax.plot(s,4-s,color=STROKE,lw=1.6,zorder=2); s=np.array([2.0,2.5]); ax.plot(s,6-2*s,color=STROKE,lw=1.6,zorder=2)
s=np.array([2,2.35]); ax.plot(s,4-s,color=STROKE,lw=.85,ls=(0,(3,2))); s=np.array([1.7,2]); ax.plot(s,6-2*s,color=STROKE,lw=.85,ls=(0,(3,2)))
for c,lab in ((8.5,'利润 8.5'),(10,'利润 10'),(10.3,'利润 10.3')):
    x=np.array([1,2.9]); ax.plot(x,(c-3*x)/2,color=BLUE,lw=.85,ls=(0,(4,2.2)),zorder=1)
ax.text(2.07,1.1,'8.5',ha='right',va='center',color=BLUE,fontsize=7.5,bbox=dict(fc=BLUE_FILL,ec='none',pad=.4))
ax.text(2.57,1.1,'10',ha='right',va='center',color=BLUE,fontsize=7.5,bbox=dict(fc='white',ec='none',pad=.4))
ax.text(2.74,1.1,'10.3',ha='left',va='center',color=BLUE,fontsize=7.5)
ax.plot([2],[2],'o',ms=5,color=RED,mew=0,zorder=6)
ax.plot([2.1],[2.0],'x',ms=5.2,color=RED,mew=1.4,zorder=6)
ax.plot([1.5],[2.0],'o',ms=4.4,color=GREEN,mew=0,zorder=6)
ax.text(1.94,1.93,r'$x^*$',ha='right',va='top'); ax.text(2.15,2.04,r'$\tilde{x}$',ha='left',va='bottom'); ax.text(1.5,1.86,r'$\hat{x}$',ha='center',va='top')
ax.set_xlim(1,3.2); ax.set_ylim(1,3); ax.set_aspect('equal'); ax.set_xticks([1,1.5,2,2.5,3]); ax.set_xticklabels(['1','1.5','2','2.5','3']); ax.set_yticks([1,2,3]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=2)
save(fig, HERE, 'figure', {'x_star':[2,2],'x_tilde':[2.1,2.0],'x_hat':[1.5,2.0]})
