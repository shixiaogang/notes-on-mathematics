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
    H=fig.get_figheight()*25.4
    if len(fig.axes)>1: bottom=15.5/H
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tag(fig, ax, s, y=None):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, 1.0/(fig.get_figheight()*25.4), s, ha='center', va='bottom')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
def dot(ax, x, y, c=GREEN, ms=4.2, z=6, m='o'): ax.plot([x],[y],m,ms=ms,color=c,mew=0,zorder=z)
def hollow(ax, x, y, c=BLUE, ms=4.4, z=7): ax.plot([x],[y],'o',ms=ms,mfc='white',mec=c,mew=1.0,zorder=z)

# min -x^2, -1<=x<=1：KKT 点 0 与 ±1；L(x,2,0)=-(x-1)^2-1 在 x=1 处是最大点。
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.065,.985,.97,.22,wspace=.22)
X=np.linspace(-1.6,1.6,300);A.axvspan(-1,1,color=BLUE_FILL,lw=0,zorder=0);A.plot(X,-X**2,color=BLUE,lw=1.5)
for s in (-1,1): A.plot([s,s],[-2.8,.5],color=STROKE,lw=1.4);opt(A,s,-1)
dot(A,0,0,GREEN,ms=4.8);A.text(.0,.13,'$x=0$',ha='center',fontsize=7.5)
A.set_xlim(-1.6,1.6);A.set_ylim(-2.8,.5);A.set_xticks([-1,0,1]);A.set_yticks([-2,-1,0]);A.set_xlabel('$x$',labelpad=1)
X=np.linspace(-1.6,3,300);B.axvspan(-1,1,color=BLUE_FILL,lw=0,zorder=0)
B.plot(X,-X**2,color=BLUE,lw=1.5);B.plot(X,-(X-1)**2-1,color=PURPLE,lw=1.5,ls='--');opt(B,1,-1)
B.text(2.9,-3.6,r'$\mathcal{L}(x,2,0)$'.replace(r'\mathcal{L}','L'),fontsize=7.5,ha='right',va='bottom') if 0 else None
B.text(-.2,-.7,'$f$',fontsize=8);B.text(2.05,-3.0,r'$\mathcal{L}$',fontsize=8)
B.set_xlim(-1.6,3);B.set_ylim(-7,.5);B.set_xticks([-1,0,1,2,3]);B.set_yticks([-6,-4,-2,0]);B.set_xlabel('$x$',labelpad=1)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'f':'-x^2','L':'-(x-1)^2-1'})
