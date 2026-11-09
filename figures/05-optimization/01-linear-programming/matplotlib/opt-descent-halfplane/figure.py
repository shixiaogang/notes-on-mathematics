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

# 目标 f=0.5(x1+x2-2)^2+0.25||x||^2，x_bar=(2,0)，gradient=(1,0)。
fig, ax = figure(width_mm=90, height_mm=66)
X,Y=np.meshgrid(np.linspace(-1.5,4,500),np.linspace(-2.2,2.8,500))
F=.5*(X+Y-2)**2+.25*(X**2+Y**2)
ax.axvspan(-1.5,2,facecolor=GREEN_FILL,edgecolor='none',zorder=0)
ax.contour(X,Y,F,levels=[.5,1,1.5,2,3,4.5],colors=[BLUE],linewidths=.75,zorder=1)
ax.axvline(2,color=STROKE,lw=1.0,ls=(0,(4,2)),zorder=2)
arr=lambda p,q,c:ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color=c,lw=1.15,mutation_scale=8,shrinkA=0,shrinkB=0),zorder=5)
arr((2,0),(3,0),INK); arr((2,0),(1,0),GREEN); arr((2,0),(1,1),GREEN)
ax.plot([2],[0],'o',ms=4.4,color=INK,mew=0,zorder=6)
ax.plot([.8],[.8],'o',ms=5,color=RED,mew=0,zorder=6)
ax.text(3.03,.1,r'$\nabla f$',ha='left',va='bottom')
ax.text(.98,-.1,r'$-\nabla f$',ha='right',va='top',color=INK)
ax.text(.96,1.06,r'$d$',ha='right',va='bottom',color=INK)
ax.text(2.08,-.32,r'$\bar{x}$',ha='left',va='top')
ax.text(-1.25,-1.85,'下降方向',color=INK,fontsize=7.5)
ax.set_xlim(-1.5,4); ax.set_ylim(-2.2,2.8); ax.set_aspect('equal'); ax.set_xticks([-1,0,1,2,3,4]); ax.set_yticks([-2,-1,0,1,2]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=2)
save(fig, HERE, 'figure', {'f':'0.5(x1+x2-2)^2+0.25||x||^2','x_bar':[2,0],'grad':[1,0]})
