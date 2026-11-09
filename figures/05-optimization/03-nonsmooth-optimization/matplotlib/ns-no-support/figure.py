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
# (a) -sqrt(x) 在 0 没有支撑直线；(b) -|x| 的非凸折点。
fig,(A,B)=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.09,.99,.98,.26,wspace=.2)
X=np.linspace(0,2,801)
A.plot(X,-np.sqrt(X),color=BLUE,lw=1.4)
for s in (-1,-3):
    A.plot(X,s*X,color=PURPLE,lw=.85,ls='--')
A.plot([0],[0],'o',color=BLUE,ms=4,mew=0,zorder=6)
A.set_xlim(-.1,2);A.set_ylim(-2,.2);A.set_xticks([0,1,2]);A.set_yticks([-2,-1,0]);A.set_xlabel('$x$',labelpad=1)
A.text(1.5,-1.1,'$-\\sqrt{x}$',color=INK);A.text(1.08,-.86,'$s=-1$',color=INK,fontsize=7.5);A.text(.68,-1.92,'$s=-3$',color=INK,fontsize=7.5)
X=np.linspace(-2,2,401)
B.plot(X,-abs(X),color=BLUE,lw=1.4)
for s in (-1,0,1):
    B.plot(X,s*X,color=PURPLE,lw=.85,ls='--')
B.plot([0],[0],'o',color=RED,ms=4.8,mew=0,zorder=6,mfc='white',mec=RED) if 0 else B.plot([0],[0],'o',color=BLUE,ms=4,mew=0,zorder=6)
B.set_xlim(-2,2);B.set_ylim(-2,2);B.set_xticks([-2,0,2]);B.set_yticks([-2,0,2]);B.set_xlabel('$x$',labelpad=1)
B.text(1.05,-1.65,'$-|x|$',color=INK);B.text(1.1,.2,'$s=0$',color=INK,fontsize=7.5)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'a':'-sqrt(x)','b':'-|x|'})
