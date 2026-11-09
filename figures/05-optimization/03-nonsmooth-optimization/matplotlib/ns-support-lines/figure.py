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
# (a) f(x)=|x| 在 0 处的支撑直线；(b) f(x)=max{-x,x/2,2x-3} 在两个折点处的支撑直线。
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.08,.99,.98,.26,wspace=.16)
X=np.linspace(-2,2,401)
A.plot(X,abs(X),color=BLUE,lw=1.4)
for s in (-1,-.5,0,.5,1):
    A.plot(X,s*X,color=PURPLE,lw=.85,ls='--',zorder=2)
opt(A)
A.set_xlim(-2,2);A.set_ylim(-1,2);A.set_xticks([-2,-1,0,1,2]);A.set_yticks([-1,0,1,2])
A.text(1.32,1.72,'$|x|$',color=INK);A.text(1.1,.73,'$s=\\frac{1}{2}$',color=INK,fontsize=7.5,ha='left');A.text(1.25,.14,'$s=0$',color=INK,fontsize=7.5)
A.set_xlabel('$x$',labelpad=1)
X=np.linspace(-2,4,601); f=lambda x:np.maximum.reduce([-x,x/2,2*x-3])
B.plot(X,f(X),color=BLUE,lw=1.4)
for s in (-1,-.25,.5):
    B.plot(X,s*X,color=PURPLE,lw=.85,ls='--',zorder=2)
for s in (1.1,2):
    B.plot(X,1+s*(X-2),color=PURPLE,lw=.85,ls='--',zorder=2)
opt(B); B.plot([2],[1],'o',color=BLUE,ms=4,mew=0,zorder=6)
B.set_xlim(-2,4);B.set_ylim(-1.2,5);B.set_xticks([-2,0,2,4]);B.set_yticks([0,2,4])
B.text(3.15,4.3,'$f$',color=INK);B.set_xlabel('$x$',labelpad=1)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'a':'|x|, slopes -1,-1/2,0,1/2,1','b':'max{-x,x/2,2x-3}, slopes at 0 and 2'})
