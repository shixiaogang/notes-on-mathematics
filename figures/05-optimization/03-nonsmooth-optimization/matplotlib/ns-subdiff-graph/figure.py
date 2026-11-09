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
# f(x)=max{-x,x/2,2x-3} 与其次微分的图像。
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.09,.99,.98,.26,wspace=.2)
X=np.linspace(-2,4,601); f=lambda x:np.maximum.reduce([-x,x/2,2*x-3])
A.plot(X,f(X),color=BLUE,lw=1.4);opt(A);A.plot([2],[1],'o',color=BLUE,ms=4,mew=0,zorder=6)
A.set_xlim(-2,4);A.set_ylim(-.3,5);A.set_xticks([-2,0,2,4]);A.set_yticks([0,2,4]);A.set_xlabel('$x$',labelpad=1)
A.text(3.2,3.95,'$f$',color=INK)
B.plot([-2,0],[-1,-1],color=BLUE,lw=1.4);B.plot([0,0],[-1,.5],color=BLUE,lw=1.4);B.plot([0,2],[.5,.5],color=BLUE,lw=1.4)
B.plot([2,2],[.5,2],color=BLUE,lw=1.4);B.plot([2,4],[2,2],color=BLUE,lw=1.4)
B.axhline(0,color=MUTED,lw=.85,ls=':',zorder=1)
opt(B)
B.set_xlim(-2,4);B.set_ylim(-1.4,2.4);B.set_xticks([-2,0,2,4]);B.set_yticks([-1,0,.5,1,2],['$-1$','$0$','$\\frac{1}{2}$','$1$','$2$']);B.set_xlabel('$x$',labelpad=1)
B.text(2.9,2.1,'$\\partial f(x)$',color=INK)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'f':'max{-x,x/2,2x-3}'})
