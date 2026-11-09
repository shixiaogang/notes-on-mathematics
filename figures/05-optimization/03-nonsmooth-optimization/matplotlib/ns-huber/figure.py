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
# Huber h_mu 与其一阶、二阶导数；mu=1,1/2。
h=lambda x,m:np.where(abs(x)<=m,x*x/(2*m),abs(x)-m/2)
d=lambda x,m:np.clip(x/m,-1,1)
fig,(A,B,C)=figure(width_mm=112,height_mm=48,ncols=3)
panel(fig,.05,.99,.98,.28,wspace=.26)
X=np.linspace(-2.5,2.5,1001)
A.plot(X,abs(X),color=BLUE,lw=1.4);A.plot(X,h(X,1.),color=GREEN,lw=1.3);A.plot(X,h(X,.5),color=GREEN,lw=1.3,ls='--')
A.set_xlim(-2.5,2.5);A.set_ylim(-.15,2.6);A.set_xticks([-2,0,2]);A.set_yticks([0,1,2]);A.set_xlabel('$x$',labelpad=1)
A.text(1.05,2.1,'$|x|$',color=INK)
B.plot([-2.5,0,0,2.5],[-1,-1,1,1],color=BLUE,lw=1.2);B.plot(X,d(X,1.),color=GREEN,lw=1.3);B.plot(X,d(X,.5),color=GREEN,lw=1.3,ls='--')
B.set_xlim(-2.5,2.5);B.set_ylim(-1.25,1.25);B.set_xticks([-2,0,2]);B.set_yticks([-1,0,1]);B.set_xlabel('$x$',labelpad=1)
C.plot([-2.5,-1],[0,0],color=GREEN,lw=1.3);C.plot([-1,1],[1,1],color=GREEN,lw=1.3);C.plot([1,2.5],[0,0],color=GREEN,lw=1.3)
C.plot([-2.5,-.5],[.0,.0],color=GREEN,lw=1.3,ls='--');C.plot([-.5,.5],[2,2],color=GREEN,lw=1.3,ls='--');C.plot([.5,2.5],[0,0],color=GREEN,lw=1.3,ls='--')
for x,y0,y1,cc in ((-1,0,1,GREEN),(1,0,1,GREEN),(-.5,0,2,GREEN),(.5,0,2,GREEN)):
    C.plot([x,x],[y0,y1],color=MUTED,lw=.7,ls=':')
C.set_xlim(-2.5,2.5);C.set_ylim(-.2,2.4);C.set_xticks([-2,0,2]);C.set_yticks([0,1,2]);C.set_xlabel('$x$',labelpad=1)
fig.canvas.draw()
for ax,s in zip((A,B,C),('(a)','(b)','(c)')):tag(fig,ax,s,y=.055)
save(fig,HERE,'figure',{'mu':[1,.5]})
