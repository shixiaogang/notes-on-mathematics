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

# 三种不同的失败：原始不达到、对偶不达到、正间隙。
fig,(A,B,C)=figure(width_mm=112,height_mm=48,ncols=3)
panel(fig,.05,.985,.97,.25,wspace=.25)
X=np.linspace(-.6,5,300);A.axvspan(0,5,color=BLUE_FILL,lw=0,zorder=0);A.plot(X,np.exp(-X),color=BLUE,lw=1.5);A.axhline(0,color=PURPLE,lw=1.0,ls='--');A.plot([0,0],[-.2,1.9],color=STROKE,lw=1.4)
A.text(2.3,.15,r'$f^\star=d^\star=0$',fontsize=7.5)
A.set_xlim(-.6,5);A.set_ylim(-.2,1.9);A.set_xticks([0,2,4]);A.set_yticks([0,1]);A.set_xlabel('$x$',labelpad=1)
L=np.linspace(.06,6,400);B.plot(L,-1/(4*L),color=PURPLE,lw=1.5);B.axhline(0,color=BLUE,lw=1.0,ls='--');B.text(5.8,.12,r'$f^\star=0$',ha='right',fontsize=7.5)
B.set_xlim(0,6);B.set_ylim(-1.8,.5);B.set_xticks([0,2,4,6]);B.set_yticks([-1,0]);B.set_xlabel(r'$\lambda$',labelpad=1)
C.axvspan(-1,0,color=RED_FILL,lw=0,zorder=0);C.plot([0,2],[0,0],color=BLUE,lw=1.5,zorder=3);hollow(C,0,0);opt(C,0,1)
C.annotate('',xy=(.3,1),xytext=(.3,0),arrowprops=dict(arrowstyle='<|-|>',color=RED,lw=1.0,shrinkA=0,shrinkB=0));C.text(.42,.5,'间隙',fontsize=7.5,va='center')
C.text(.12,1.1,r'$v(0)=1$',fontsize=7.5);C.text(-.5,.5,'不可行',fontsize=7.5,ha='center')
C.set_xlim(-1,2);C.set_ylim(-.2,1.5);C.set_xticks([-1,0,1,2]);C.set_yticks([0,1]);C.set_xlabel('$u$',labelpad=1)
for a_,s in zip((A,B,C),('(a)','(b)','(c)')):tag(fig,a_,s,y=.04)
save(fig,HERE,'figure',{'a':'exp(-x),x>=0','b':'q=-1/(4lam)','c':'v(0)=1, v(u>0)=0'})
