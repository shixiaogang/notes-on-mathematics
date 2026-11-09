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

# f(x)=x^2，f*(y)=y^2/4；y=2 的切线 2x-1。
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.06,.985,.97,.22,wspace=.2)
X=np.linspace(-1.5,2.2,300)
A.plot(X,X**2,color=BLUE,lw=1.5);A.plot(X,2*X,color=MUTED,lw=.9,ls=':');A.plot(X,2*X-1,color=PURPLE,lw=1.4)
A.plot([1,1],[1,2],color=RED,lw=1.6,solid_capstyle='butt');dot(A,1,1,BLUE,ms=4.2);dot(A,0,-1,PURPLE,ms=4.4)
A.text(.42,2.75,r'$f^*(2)=1$',va='center',ha='center',fontsize=7.5);A.plot([.55,1],[2.55,1.6],color=MUTED,lw=.6);A.text(.1,-1.25,r'$-f^*(2)$',va='center',fontsize=7.5);A.text(-1.42,2.4,'$f=x^2$',fontsize=8);A.text(1.42,3.15,'$2x$',fontsize=7.5,color=MUTED,ha='right');A.text(2.18,1.75,'$2x-1$',fontsize=7.5,ha='right')
A.axhline(0,color=MUTED,lw=.45,zorder=0);A.axvline(0,color=MUTED,lw=.45,zorder=0)
A.set_xlim(-1.5,2.2);A.set_ylim(-1.6,4.1);A.set_xticks([-1,0,1,2]);A.set_yticks([-1,0,1,2,3,4]);A.set_xlabel('$x$',labelpad=1)
Y=np.linspace(-3.5,3.5,300);B.plot(Y,Y**2/4,color=PURPLE,lw=1.5);dot(B,2,1,PURPLE,ms=4.4);B.text(2.08,.82,'$(2,1)$',fontsize=7.5,va='top')
B.text(-3.3,2.65,r'$f^*(y)=y^2/4$',fontsize=8)
B.set_xlim(-3.5,3.5);B.set_ylim(-.15,3.4);B.set_xticks([-2,0,2]);B.set_yticks([0,1,2,3]);B.set_xlabel('$y$',labelpad=1)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'f':'x^2','conj':'y^2/4'})
