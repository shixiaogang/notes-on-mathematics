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

# f(x)=(x-2)^2，约束 x<=1。约束指标函数、普通指示函数、有限惩罚。
f = lambda x: (x-2)**2
fig, axes = figure(width_mm=112, height_mm=48, ncols=3, sharey=True)
panel(fig, .07, .985, .955, .25, .13)
L=-.5; R=3
for ax in axes:
    ax.axvspan(1,R,facecolor=RED_FILL,edgecolor='none',zorder=0)
    ax.set_xlim(L,R); ax.set_ylim(-.3,5); ax.set_xticks([0,1,2,3]); ax.set_xlabel('$x$',labelpad=1)
a=axes[0]; x=np.linspace(L,1,200); a.plot(x,f(x),color=BLUE,lw=1.4)
a.plot([1],[1],'o',ms=5,color=RED,mew=0,zorder=4); a.text(2,2.6,r'$+\infty$',ha='center',va='center')
a.set_ylabel('目标',labelpad=2)
a.set_yticks([0,1,2,3,4])
b=axes[1]; x=np.linspace(L,1,200); b.plot(x,f(x)+1,color=BLUE,lw=1.4)
x=np.linspace(1.0001,R,200); b.plot(x,f(x),color=BLUE,lw=1.4)
b.plot([1],[2],'o',ms=3.6,color=BLUE,mew=0,zorder=4); b.plot([1],[1],'o',ms=3.6,mfc='white',mec=BLUE,mew=1,zorder=4)
b.plot([2],[0],'o',ms=5,color=RED,mew=0,zorder=4)
c=axes[2]; x=np.linspace(L,R,400)
c.plot(x,f(x),color=MUTED,lw=.85,ls=(0,(2,2)))
c.plot(x,f(x)+np.maximum(0,x-1),color=BLUE,lw=1.4)
c.plot([1.5],[.75],'o',ms=5,color=RED,mew=0,zorder=4)
tags(fig, axes)
save(fig, HERE, 'figure', {'f':'(x-2)^2','C':'x<=1','penalty':'max(0,x-1)','minimizers':{'a':1,'b':2,'c':1.5}})
