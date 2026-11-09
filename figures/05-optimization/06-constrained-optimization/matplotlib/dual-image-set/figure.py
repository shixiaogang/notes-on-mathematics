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

# 一元例在 (u,t)=(g(x),f(x)) 平面的像 t=(u-1)^2/2；支撑线 t=q(lam)-lam*u。
fig,A=figure(width_mm=92,height_mm=60)
panel(fig,.08,.97,.97,.13)
U=np.linspace(-2.2,3,400)
A.axvspan(-2.2,0,color=BLUE_FILL,lw=0,zorder=0)
A.plot(U,.5*(U-1)**2,color=BLUE,lw=1.5,zorder=4)
A.plot([0,0],[-1.2,4],color=STROKE,lw=1.5,zorder=2)
for lam,ls,yt in ((.5,':',None),(1,'--',None),(2,'-',None)):
    q=lam-.5*lam**2; A.plot(U,q-lam*U,color=PURPLE,lw=1.25,ls=ls,zorder=3); dot(A,0,q,PURPLE,ms=4.0,z=6)
    dot(A,1-lam,.5*lam**2,BLUE,ms=3.4,z=5)
opt(A,0,.5)
A.text(.07,.56,r'$(0,f^\star)$',fontsize=7.5)
A.text(-.07,-.18,r'$q(2)=0$',fontsize=7.5,ha='right')
A.text(2.1,1.28,r'$G$',color=INK); A.text(-2.05,.15,r'$u\leq0$',color=INK)
A.text(2.32,-.86,r'$\lambda=.5$'.replace('.5','0.5'),fontsize=7.5,ha='left') if 0 else None
A.text(-1.2,3.65,r'$\lambda=2$',fontsize=7.5); A.text(1.15,-.95,r'$\lambda=1$',fontsize=7.5,ha='right'); A.text(2.25,-.42,r'$\lambda=0.5$',fontsize=7.5,ha='left')
A.set_xlim(-2.2,3);A.set_ylim(-1.2,4);A.set_xticks([-2,-1,0,1,2,3]);A.set_yticks([0,1,2,3,4]);A.set_xlabel('$u$',labelpad=1);A.set_ylabel('$t$',labelpad=1)
save(fig,HERE,'figure',{'G':'t=(u-1)^2/2','lines':'t=q(lam)-lam*u'})
