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
# f=max{-x,x/2,2x-3} 的熵平滑：(a) 分支权重 mu=0.2；(b) 导数对比。
a=np.array([-1,.5,2.]);b=np.array([0,0,-3.])
def p(x,m):
    z=(np.outer(x,a)+b)/m;z=z-z.max(1,keepdims=True);w=np.exp(z);return w/w.sum(1,keepdims=True)
X=np.linspace(-2,4,1201)
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.07,.97,.98,.26,wspace=.22)
P=p(X,.2)
A.plot(X,P[:,0],color=BLUE,lw=1.4);A.plot(X,P[:,1],color=GREEN,lw=1.4);A.plot(X,P[:,2],color=YELLOW,lw=1.4)
A.set_xlim(-2,4);A.set_ylim(-.05,1.15);A.set_xticks([-2,0,2,4]);A.set_yticks([0,.5,1],['$0$','$0.5$','$1$']);A.set_xlabel('$x$',labelpad=1)
A.text(-1.5,1.04,'$u_1$',color=INK);A.text(.8,1.04,'$u_2$',color=INK);A.text(3.2,1.04,'$u_3$',color=INK)
B.plot([-2,0,0,2,2,4],[-1,-1,.5,.5,2,2],color=BLUE,lw=1.2)
B.plot(X,(p(X,.2)*a).sum(1),color=GREEN,lw=1.4,ls='--');B.plot(X,(p(X,1.)*a).sum(1),color=GREEN,lw=1.4)
B.set_xlim(-2,4);B.set_ylim(-1.3,2.3);B.set_xticks([-2,0,2,4]);B.set_yticks([-1,0,1,2]);B.set_xlabel('$x$',labelpad=1)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'mu':[.2,1.]})
