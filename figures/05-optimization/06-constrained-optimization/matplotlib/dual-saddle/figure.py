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

# L(x,lam)=(x-2)^2/2+lam(x-1)，鞍点 (1,1)，值 1/2。
fig,(A,B,C)=figure(width_mm=112,height_mm=52,ncols=3,gridspec_kw={'width_ratios':[1.25,1,1]})
panel(fig,.075,.985,.97,.23,wspace=.3)
x=np.linspace(-.3,3,300);l=np.linspace(0,2.5,300);X,Y=np.meshgrid(x,l)
A.contour(X,Y,.5*(X-2)**2+Y*(X-1),levels=[-1.5,-.5,0,.5,1,2,3,4],colors=BLUE,linewidths=.8)
A.plot([1,1],[0,2.5],color=PURPLE,lw=1.05,ls='--');A.plot([-.3,3],[1,1],color=GREEN,lw=1.05,ls='--');opt(A,1,1)
A.set_xlim(-.3,3);A.set_ylim(0,2.5);A.set_xticks([0,1,2,3]);A.set_yticks([0,1,2]);A.set_xlabel('$x$',labelpad=1);A.set_ylabel(r'$\lambda$',labelpad=1)
L=np.linspace(0,2.5,50)
B.plot(L,2-L,color=BLUE,lw=1.2);B.plot(L,.5+0*L,color=PURPLE,lw=1.5,ls='--');B.plot(L,.125+.5*L,color=YELLOW,lw=1.5)
B.text(2.45,-.3,'$x=0$',fontsize=7.5,ha='right',va='top') if 0 else None
B.text(.1,1.85,'$x=0$',fontsize=7.5);B.text(2.4,.32,'$x=1$',fontsize=7.5,ha='right');B.text(2.45,1.45,'$x=1.5$',fontsize=7.5,ha='right')
opt(B,1,.5)
B.set_xlim(0,2.5);B.set_ylim(-.6,2.2);B.set_xticks([0,1,2]);B.set_yticks([0,1,2]);B.set_xlabel(r'$\lambda$',labelpad=1)
X=np.linspace(-.3,3,200);C.plot(X,.5*(X-2)**2+X-1,color=GREEN,lw=1.5,ls='--');opt(C,1,.5);C.text(.45,1.45,r'$\lambda=1$',fontsize=7.5,ha='center') if 0 else None
C.set_xlim(-.3,3);C.set_ylim(0,2.2);C.set_xticks([0,1,2,3]);C.set_yticks([0,1,2]);C.set_xlabel('$x$',labelpad=1)
for a_,s in zip((A,B,C),('(a)','(b)','(c)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'L':'(x-2)^2/2+lam(x-1)','saddle':[1,1,.5]})
