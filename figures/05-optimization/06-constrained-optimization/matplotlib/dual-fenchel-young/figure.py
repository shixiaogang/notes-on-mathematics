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

# Fenchel-Young 间隙：f=x^2, x0=0.5, y=2 差 0.25；|x| 在 0 处 y in [-1,1] 取等。
fig,(A,B)=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.06,.985,.97,.22,wspace=.2)
X=np.linspace(-1.2,2,300)
A.plot(X,X**2,color=BLUE,lw=1.5);A.plot(X,2*X-1,color=PURPLE,lw=1.3)
A.plot([.5,.5],[0,.25],color=RED,lw=1.8,solid_capstyle='butt');dot(A,.5,.25,BLUE,ms=4);dot(A,.5,0,PURPLE,ms=4);dot(A,1,1,RED,ms=4.6)
A.text(.42,.16,'间隙',fontsize=7.5,ha='right',color=INK);A.text(1.08,.84,'切点处取等',fontsize=7.5,va='top')
A.text(1.5,2.9,'$f$',fontsize=8,ha='right',va='bottom');A.text(1.97,1.95,'$2x-1$',fontsize=7.5,ha='right',va='top')
A.axhline(0,color=MUTED,lw=.45,zorder=0)
A.set_xlim(-1.2,2);A.set_ylim(-1.1,3.6);A.set_xticks([-1,0,.5,1,2]);A.set_xticklabels(['$-1$','$0$','$0.5$','$1$','$2$']);A.set_yticks([-1,0,1,2,3]);A.set_xlabel('$x$',labelpad=1)
X=np.linspace(-2,2,5);B.plot([-2,0,2],[2,0,2],color=BLUE,lw=1.5,zorder=4)
for s in (-.7,.3,1): B.plot(X,s*X,color=PURPLE,lw=1.05,zorder=3);B.text(2.02,s*2,f'$y={s:g}$',fontsize=7.5,va='center')
opt(B,0,0)
B.set_xlim(-2,2.75);B.set_ylim(-1.7,2.4);B.set_xticks([-2,0,2]);B.set_yticks([-1,0,1,2]);B.set_xlabel('$x$',labelpad=1)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'gap':.25})
