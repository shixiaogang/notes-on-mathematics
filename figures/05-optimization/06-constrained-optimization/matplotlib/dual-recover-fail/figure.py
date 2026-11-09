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

# min -x, x in [0,1] 为定义域，乘子对应 x<=1/2；q(lam)=min(-lam/2,lam/2-1)。
fig,(A,B)=figure(width_mm=104,height_mm=48,ncols=2)
panel(fig,.075,.98,.965,.25,wspace=.25)
L=np.linspace(0,3,300);A.plot(L,np.minimum(-L/2,L/2-1),color=PURPLE,lw=1.5);A.axhline(-.5,color=BLUE,lw=.95,ls='--');opt(A,1,-.5)
A.text(2.95,-.43,r'$f^\star=-1/2$',ha='right',fontsize=7.5);A.text(.1,-.65,r'$\lambda<1$',fontsize=7.5,va='top') if 0 else None
A.set_xlim(0,3);A.set_ylim(-1.7,0);A.set_xticks([0,1,2,3]);A.set_yticks([-1.5,-1,-.5,0]);A.set_xlabel(r'$\lambda$',labelpad=1);A.text(2.0,-1.2,r'$q(\lambda)$',color=INK,ha='center')
B.plot([0,1],[1,1],color=PURPLE,lw=1.6);B.plot([1,3],[0,0],color=PURPLE,lw=1.6,zorder=3);B.plot([1,1],[0,1],color=PURPLE,lw=1.1,ls='--')
B.plot([0,3],[.5,.5],color=STROKE,lw=1.4);B.text(2.95,.56,r'$x\leq\frac{1}{2}$',fontsize=7.5,ha='right')
opt(B,1,.5);B.text(1.1,.38,r'$x^\star$',fontsize=8,va='top')
B.set_xlim(0,3);B.set_ylim(-.15,1.2);B.set_xticks([0,1,2,3]);B.set_yticks([0,.5,1]);B.set_xlabel(r'$\lambda$',labelpad=1);B.text(.5,.86,r'$x(\lambda)$',ha='center',color=INK)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s,y=.035)
save(fig,HERE,'figure',{'q':'min(-lam/2,lam/2-1)','lam_star':1,'x_star':.5})
