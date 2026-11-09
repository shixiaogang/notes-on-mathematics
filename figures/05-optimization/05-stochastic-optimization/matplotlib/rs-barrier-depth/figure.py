from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 双谷代价的能垒：从 x=2 到更低状态需爬升 4，单步代价差 2
fig, ax = figure(width_mm=84, height_mm=54)
s=np.arange(1,8); f=np.array([3,1,3,5,2,0,2.])
ax.plot(s,f,color=BLUE,lw=1.4,marker='o',ms=3.6,mew=0)
ax.plot([2],[1],'o',ms=5,color=GREEN,mew=0,zorder=5); ax.plot([6],[0],'o',ms=5.2,color=RED,mew=0,zorder=5); ax.plot([4],[5],'o',ms=4.6,mfc='white',mec=RED,mew=1,zorder=5)
ax.plot([2,4],[5,5],color=MUTED,lw=.85,ls=(0,(3,2))); ax.plot([2,2],[1,5],color=MUTED,lw=.0)
ax.annotate('',xy=(1.8,5),xytext=(1.8,1),arrowprops=dict(arrowstyle='<|-|>',color=RED,lw=1.1,mutation_scale=7,shrinkA=0,shrinkB=0)); ax.text(1.68,4.2,'能垒 4',ha='right',va='center',fontsize=7.5)
ax.plot([2,3],[3,3],color=MUTED,lw=.85,ls=(0,(3,2)))
ax.annotate('',xy=(2.55,3),xytext=(2.55,1.05),arrowprops=dict(arrowstyle='<|-|>',color=YELLOW,lw=1.1,mutation_scale=7,shrinkA=0,shrinkB=0)); ax.text(2.63,1.75,'单步差 2',ha='left',va='center',fontsize=7.5)
ax.text(4.12,5.1,'垒顶',ha='left',va='bottom',fontsize=7.5)
ax.set_xlim(.6,7.4); ax.set_ylim(-.5,5.9); ax.set_xticks(s); ax.set_yticks([0,1,2,3,4,5]); ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel('$f(x)$',labelpad=1)
save(fig,HERE,'figure',{'f':[3,1,3,5,2,0,2],'depth_of_state_2':4,'gap':2})
