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

# f=0.5(x1+x2-2)^2+0.5 gamma ||x||^2，gamma=0 与 0.5 的下水平集 {f<=1}。
fig, axes = figure(width_mm=112, height_mm=62, ncols=2, sharey=True)
panel(fig, .07, .985, .975, .205, .08)
X,Y=np.meshgrid(np.linspace(-3.2,5.2,500),np.linspace(-3.2,5.2,500))
for ax,g in zip(axes,(0,.5)):
    F=.5*(X+Y-2)**2+.5*g*(X**2+Y**2)
    ax.contourf(X,Y,F,levels=[-1,1],colors=[BLUE_FILL])
    ax.contour(X,Y,F,levels=[1],colors=[BLUE],linewidths=1.2)
    ax.contour(X,Y,F,levels=[2.25,4,6.25,9],colors=[BLUE],linewidths=.7)
    ax.set_xlim(-3,5); ax.set_ylim(-3,5); ax.set_aspect('equal'); ax.set_xticks([-2,0,2,4]); ax.set_yticks([-2,0,2,4]); ax.set_xlabel('$x_1$',labelpad=1)
axes[0].set_ylabel('$x_2$',labelpad=2)
s=np.array([-3,5.0]); axes[0].plot(s,2-s,color=RED,lw=1.6,zorder=4)
axes[1].plot([.8],[.8],'o',ms=5,color=RED,mew=0,zorder=4)
tags(fig, axes)
save(fig, HERE, 'figure', {'f':'0.5(x1+x2-2)^2+0.5*gamma*||x||^2','gamma':[0,.5],'sublevel':1,'xstar_gamma_.5':[.8,.8]})
