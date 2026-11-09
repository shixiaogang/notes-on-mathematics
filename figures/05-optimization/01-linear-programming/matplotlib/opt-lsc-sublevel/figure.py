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

# 两个函数只在 x=0 处的取值不同，下水平集 {f<=0.6}。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
panel(fig, .095, .985, .955, .26, .1)
for ax,val in zip(axes,(0.4,1.0)):
    x=np.linspace(-1,-1e-3,10); ax.plot(x,np.ones_like(x),color=BLUE,lw=1.4)
    x=np.linspace(1e-3,1.5,100); ax.plot(x,.4+.5*x,color=BLUE,lw=1.4)
    other = 1.0 if val==.4 else .4
    ax.plot([0],[other],'o',ms=4.2,mfc='white',mec=BLUE,mew=1,zorder=4)
    ax.plot([0],[val],'o',ms=4.4,color=BLUE,mew=0,zorder=5)
    ax.axhline(.6,color=MUTED,lw=.85,ls=(0,(2,2)))
    ax.text(1.5,.63,'$a=0.6$',ha='right',va='bottom',color=MUTED,fontsize=7.5)
    ax.plot([0,.4],[0,0],color=GREEN,lw=2.4,solid_capstyle='butt',zorder=3)
    ax.plot([.4],[0],'o',ms=4.2,color=GREEN,mew=0,zorder=4)
    if val==.4: ax.plot([0],[0],'o',ms=4.2,color=GREEN,mew=0,zorder=4)
    else: ax.plot([0],[0],'o',ms=4.2,mfc='white',mec=GREEN,mew=1,zorder=4)
    ax.vlines(.4,0,.6,color=MUTED,lw=.7,ls=':')
    ax.set_xlim(-1,1.55); ax.set_ylim(-.08,1.25); ax.set_xticks([-1,0,.4,1]); ax.set_xticklabels(['$-1$','0','0.4','1']); ax.set_yticks([0,.4,1]); ax.set_yticklabels(['0','0.4','1']); ax.set_xlabel('$x$',labelpad=1)
axes[0].set_ylabel('$f$',labelpad=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'f':'1 for x<0; .4+.5x for x>0; f(0)=.4 or 1','level':.6})
