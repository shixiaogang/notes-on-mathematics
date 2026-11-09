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
# F(x)=|x|+|x-1|+|x-5|，x0=3，二次代理（IRLS）；最优值 F*=5，x*=1。
y=np.array([0.,1,5]);F=lambda x:np.abs(np.subtract.outer(x,y)).sum(-1)
def Q(x,c):
    r=np.abs(c-y);return ((np.subtract.outer(x,y))**2/(2*r)+r/2).sum(-1)
def nx(c):
    w=1/np.abs(c-y);return (w*y).sum()/w.sum()
P=[3.]
for t in range(12):P.append(nx(P[-1]))
P=np.array(P);print(P[:6],F(P[:6]))
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.07,.97,.98,.26,wspace=.24)
X=np.linspace(-1.5,6.5,1201);A.plot(X,F(X),color=BLUE,lw=1.4)
for c,ls in ((P[0],'-'),(P[1],'--'),(P[2],':')):
    A.plot(X,Q(X,c),color=GREEN,lw=1.2,ls=ls);A.plot([c],[F(np.array(c))],'o',color=GREEN,ms=4,mew=0,zorder=6)
opt(A,1,5.)
A.set_xlim(-1.5,6.5);A.set_ylim(4,14);A.set_xticks([0,1,3,5]);A.set_yticks([6,10,14]);A.set_xlabel('$x$',labelpad=1)
A.text(5.45,10.3,'$F$',color=INK)
tt=np.arange(13);B.semilogy(tt,F(P)-5,'-o',color=GREEN,lw=1.3,ms=3,mew=0)
B.set_xlim(0,12);B.set_xticks([0,4,8,12]);B.set_xlabel('$t$',labelpad=1);B.set_ylabel('目标差',labelpad=1)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'y':y.tolist(),'x':P.tolist()})
