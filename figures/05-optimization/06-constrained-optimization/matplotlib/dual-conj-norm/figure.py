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

# |x| 的共轭是 [-1,1] 的约束指标函数；C=[-1,2] 的支撑函数 max(2y,-y)。
fig,(A,B,C)=figure(width_mm=112,height_mm=48,ncols=3)
panel(fig,.05,.985,.97,.25,wspace=.24)
X=np.linspace(-2,2.2,10)
A.plot([-2,0,2.2],[2,0,2.2],color=BLUE,lw=1.5,zorder=4)
for s,ls in ((-.6,'-'),(.4,'-'),(1,'-')): A.plot(X,s*X,color=PURPLE,lw=1.05,zorder=3)
A.plot(X,1.5*X,color=RED,lw=1.2,ls=':',zorder=5);A.text(1.08,2.42,r'$y=1.5$',fontsize=7.5,ha='center')
A.axhline(0,color=MUTED,lw=.45,zorder=0)
A.set_xlim(-2,2.2);A.set_ylim(-1.6,2.8);A.set_xticks([-2,0,2]);A.set_yticks([-1,0,1,2]);A.set_xlabel('$x$',labelpad=1)
B.plot([-1,1],[0,0],color=PURPLE,lw=1.8,solid_capstyle='butt')
for s in (-1,1):
    B.annotate('',xy=(s,2.5),xytext=(s,0),arrowprops=dict(arrowstyle='-|>',color=PURPLE,lw=1.2,shrinkA=0,shrinkB=0))
    dot(B,s,0,PURPLE,ms=4)
B.text(0,1.05,'$+\\infty$ 在外',fontsize=7.5,ha='center') if 0 else None
B.text(-1.65,1.2,r'$+\infty$',fontsize=7.5,ha='center');B.text(1.65,1.2,r'$+\infty$',fontsize=7.5,ha='center');B.text(0,.14,'$0$',fontsize=7.5,ha='center')
B.set_xlim(-2.2,2.2);B.set_ylim(-.3,2.8);B.set_xticks([-1,0,1]);B.set_yticks([0,1,2]);B.set_xlabel('$y$',labelpad=1)
Y=np.linspace(-2,2,5)
Y=np.array([-2,0,2]);C.plot(Y,np.maximum(2*Y,-Y),color=PURPLE,lw=1.5)
C.text(1.15,3.05,r'$2y$',fontsize=7.5,ha='center');C.text(-1.2,1.6,r'$-y$',fontsize=7.5,ha='center')
C.set_xlim(-2,2);C.set_ylim(-.3,4.3);C.set_xticks([-2,0,2]);C.set_yticks([0,2,4]);C.set_xlabel('$y$',labelpad=1)
for a_,s in zip((A,B,C),('(a)','(b)','(c)')):tag(fig,a_,s,y=.04)
save(fig,HERE,'figure',{'abs_conj':'indicator [-1,1]','support':'sigma_[-1,2](y)=max(2y,-y)'})
