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
# f(x)=|x1|+2|x2| 的等高线（a）与三个点处的次微分（b）。
fig,(A,B)=figure(width_mm=112,height_mm=58,ncols=2)
panel(fig,.09,.99,.98,.26,wspace=.2)
X,Y=np.meshgrid(np.linspace(-2,2,801),np.linspace(-1.4,1.4,801))
A.contour(X,Y,abs(X)+2*abs(Y),levels=[.5,1,1.5,2,3],colors=[BLUE],linewidths=.7)
opt(A)
A.plot([1],[0],'s',color=GREEN,ms=4,mew=0,zorder=6);A.plot([.5],[.5],'^',color=GREEN,ms=4.6,mew=0,zorder=6)
A.text(1.08,.08,'$a$',color=INK);A.text(.56,.56,'$b$',color=INK);A.text(-.28,.1,'$0$',color=INK)
A.set_xlim(-2,2);A.set_ylim(-1.4,1.4);A.set_aspect('equal');A.set_xticks([-2,-1,0,1,2]);A.set_yticks([-1,0,1]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=0)
B.fill([-1,1,1,-1],[-2,-2,2,2],facecolor=PURPLE_FILL,edgecolor=PURPLE,lw=1.1,zorder=2)
B.plot([1,1],[-2,2],color=GREEN,lw=2.4,zorder=3,solid_capstyle='butt')
B.plot([1],[2],'^',color=GREEN,ms=5,mew=0,zorder=6);B.plot([0],[0],'o',color=RED,ms=4.4,mew=0,zorder=6)
B.axhline(0,color=MUTED,lw=.7,ls=':',zorder=1);B.axvline(0,color=MUTED,lw=.7,ls=':',zorder=1)
B.text(-.95,-1.6,'$\\partial f(0)$',color=INK);B.text(1.12,-.25,'$\\partial f(a)$',color=INK);B.text(1.12,2.02,'$\\partial f(b)$',color=INK,va='center')
B.set_xlim(-2,2.6);B.set_ylim(-2.6,2.6);B.set_aspect('equal');B.set_xticks([-1,0,1]);B.set_yticks([-2,0,2]);B.set_xlabel('$s_1$',labelpad=1);B.set_ylabel('$s_2$',labelpad=0)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'f':'|x1|+2|x2|'})
