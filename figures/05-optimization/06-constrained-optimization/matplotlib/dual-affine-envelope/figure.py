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

# L(x,lam)=(x-2)^2/2+lam(x-1)：固定x是lam的直线，q(lam)=lam-lam^2/2是下包络。
fig,A=figure(width_mm=92,height_mm=58)
panel(fig,.08,.84,.97,.13)
La=np.linspace(0,3,200)
xs=[(-.5,BLUE,'-'),(0,BLUE,'-'),(.5,BLUE,'-'),(1,BLUE,'-'),(1.5,YELLOW,'-'),(2,YELLOW,'-'),(3,YELLOW,'-')]
for x,c,ls in xs:
    A.plot(La,.5*(x-2)**2+La*(x-1),color=c,lw=1.6 if x==1 else 1.05,ls=ls,zorder=3)
    yr=.5*(x-2)**2+3*(x-1)
    if -2.15<=yr<=4.2: A.text(3.04,yr,f'$x={x:g}$',va='center',fontsize=7.5)
A.plot(La,La-.5*La**2,color=PURPLE,lw=1.9,zorder=5)
opt(A,1,.5); A.text(1.12,.03,r'$q(\lambda)$',color=INK)
A.set_xlim(0,3);A.set_ylim(-2.2,4.2);A.set_xticks([0,1,2,3]);A.set_yticks([-2,0,.5,2,4]);A.set_xlabel(r'$\lambda$',labelpad=1)
save(fig,HERE,'figure',{'L':'(x-2)^2/2+lam(x-1)','q':'lam-lam^2/2'})
