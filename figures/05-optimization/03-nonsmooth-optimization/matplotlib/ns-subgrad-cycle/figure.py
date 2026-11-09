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
# f(x)=|x1|+2|x2|，x0=(1,1)，固定步长 0.3；次梯度取 sign(0)=+1 的约定。
def sg(x): return np.array([1. if x[0]>=0 else -1., 2. if x[1]>=0 else -2.])
f=lambda x:abs(x[0])+2*abs(x[1])
P=[np.array([1.,1.])]
for t in range(14): P.append(P[-1]-.3*sg(P[-1]))
P=np.round(np.array(P),10);V=[f(x) for x in P]
fig,(A,B)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.09,.99,.98,.26,wspace=.22)
X,Y=np.meshgrid(np.linspace(-.6,1.3,801),np.linspace(-.6,1.2,801))
A.contour(X,Y,abs(X)+2*abs(Y),levels=[.3,.6,.9,1.5,3],colors=[BLUE],linewidths=.7)
A.plot(P[:6,0],P[:6,1],'-o',color=GREEN,lw=1.2,ms=3.4,mew=0,zorder=4);opt(A)
for i,(dx,dy) in zip(range(5),[(.05,.03),(.05,.02),(.04,-.09),(.05,.02),(-.2,-.1)]):
    A.text(P[i,0]+dx,P[i,1]+dy,f'{i}',color=INK,fontsize=7.5)
A.set_xlim(-.6,1.3);A.set_ylim(-.6,1.2);A.set_aspect('equal');A.set_xticks([-.5,0,.5,1],['$-0.5$','$0$','$0.5$','$1$']);A.set_yticks([-.5,0,.5,1],['$-0.5$','$0$','$0.5$','$1$']);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=0)
T=np.arange(len(V));B.plot(T,V,'-o',color=GREEN,lw=1.2,ms=3,mew=0);B.step(T,np.minimum.accumulate(V),where='post',color=PURPLE,lw=1.2,ls='--')
B.set_xlim(0,14);B.set_ylim(0,3.2);B.set_xticks([0,4,8,12]);B.set_yticks([0,1,2,3]);B.set_xlabel('$t$',labelpad=1)
B.text(8.3,1.08,'$f(x^{(t)})$',color=INK);B.text(9.4,.28,'目前最好值',color=INK,fontsize=7.5)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'f':'|x1|+2|x2|','alpha':.3,'x0':[1,1],'values':[float(v) for v in V]})
