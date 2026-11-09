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
# prox of |y| with alpha=1: x=2 -> p=1；x=0.6 -> p=0。
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.08,.99,.98,.26,wspace=.16)
Y=np.linspace(-2,4,901)
for ax,x,p,yl in ((A,2.,1.,(-.2,5)),(B,.6,0.,(-.2,5))):
    ax.plot(Y,abs(Y),color=BLUE,lw=1.1)
    ax.plot(Y,.5*(Y-x)**2,color=PURPLE,lw=.95,ls='--')
    ax.plot(Y,abs(Y)+.5*(Y-x)**2,color=GREEN,lw=1.4)
    ax.plot([x],[0],'o',ms=4.2,mfc='white',mec=INK,mew=.8,zorder=6,clip_on=False)
    v=abs(p)+.5*(p-x)**2;ax.plot([p],[v],'o',color=GREEN,ms=4.6,mew=0,zorder=7)
    ax.plot([p,p],[0,v],color=MUTED,lw=.85,ls=':')
    ax.set_xlim(-2,4);ax.set_ylim(*yl);ax.set_xticks([-2,0,2,4]);ax.set_yticks([0,2,4]);ax.set_xlabel('$y$',labelpad=1)
A.text(2.05,.18,'$x$',color=INK);A.text(1.08,.08,'$p$',color=INK)
A.text(3.05,3.4,'$|y|$',color=INK,fontsize=7.5,ha='left');A.text(-1.95,3.05,'$\\frac{1}{2}(y-x)^2$',color=INK,fontsize=7.5);A.text(2.7,4.5,'和',color=INK,fontsize=7.5)
B.text(.68,.18,'$x$',color=INK);B.text(-.42,.1,'$p$',color=INK)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'alpha':1,'cases':[[2,1],[.6,0]]})
