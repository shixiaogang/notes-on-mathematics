from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# (a) 软阈值 t=1；(b) f=max{-x,x/2,2x-3} 的邻近映射 alpha=1。
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.09,.99,.98,.26,wspace=.2)
X=np.linspace(-3,3,601);A.plot(X,X,color=MUTED,lw=.85,ls=':');A.plot(X,np.sign(X)*np.maximum(abs(X)-1,0),color=BLUE,lw=1.4)
A.set_xlim(-3,3);A.set_ylim(-3,3);A.set_xticks([-3,-1,0,1,3]);A.set_yticks([-2,0,2]);A.set_xlabel('$x$',labelpad=1);A.text(1.55,.1,'$S_1(x)$',color=INK);A.text(1.9,2.45,'$y=x$',color=INK,fontsize=7.5)
A.plot([-1,1],[0,0],color=STROKE,lw=2.2,solid_capstyle='butt')
def prox(x,a=1.):
    if x<-a: return x+a
    if x<=a/2: return 0.
    if x<2+a/2: return x-a/2
    if x<=2+2*a: return 2.
    return x-2*a
X=np.linspace(-3,7,1001);B.plot(X,X,color=MUTED,lw=.85,ls=':');B.plot(X,[prox(x) for x in X],color=BLUE,lw=1.4)
B.plot([-1,.5],[0,0],color=STROKE,lw=2.2,solid_capstyle='butt');B.plot([2.5,4],[2,2],color=STROKE,lw=2.2,solid_capstyle='butt')
B.set_xlim(-3,7);B.set_ylim(-3,6);B.set_xticks([-3,-1,.5,2.5,4,7],['$-3$','$-1$','$\\frac{1}{2}$','$\\frac{5}{2}$','$4$','$7$']);B.set_yticks([0,2,4]);B.set_xlabel('$x$',labelpad=1)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'a':'soft threshold','b':'prox of max{-x,x/2,2x-3}, alpha=1'})
