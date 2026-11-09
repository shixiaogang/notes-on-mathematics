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

# min x^2, x-1<=0：f*=0；q 公式对 lam<0 也能算，lam=-2 时值为 1>f*。
fig,A=figure(width_mm=88,height_mm=46)
panel(fig,.09,.97,.96,.17)
A.axvspan(-5,0,color=RED_FILL,lw=0,zorder=0)
L1=np.linspace(0,2,100);L2=np.linspace(-5,0,300)
A.plot(L1,-L1**2/4-L1,color=PURPLE,lw=1.5);A.plot(L2,-L2**2/4-L2,color=RED,lw=1.5,ls='--')
A.axhline(0,color=BLUE,lw=.95,ls='--');A.text(1.95,.09,r'$f^\star=0$',ha='right',fontsize=7.5)
dot(A,-2,1,RED,ms=4.6);A.text(-2,1.14,r'$\lambda=-2$',ha='center',fontsize=7.5)
dot(A,0,0,PURPLE,ms=4.4)
A.set_xlim(-5,2);A.set_ylim(-3.2,1.7);A.set_xticks([-4,-2,0,2]);A.set_yticks([-3,-2,-1,0,1]);A.set_xlabel(r'$\lambda$',labelpad=1)
save(fig,HERE,'figure',{'q':'-lam^2/4-lam'})
