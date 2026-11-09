from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panels(w,h,n,left=.07,right=.99,top=.97,bottom=.22,wspace=.25,rows=1,**k):
    fig=figure(width_mm=w,height_mm=h)[0]; fig.clf(); fig.set_layout_engine(None)
    A=[fig.add_subplot(rows,n,i+1,**k) for i in range(n*rows)]
    fig.subplots_adjust(left=left,right=right,top=top,bottom=bottom,wspace=wspace)
    return fig,A
def tag(fig,ax,s,y):
    p=ax.get_position(); fig.text((p.x0+p.x1)/2,y,s,ha='center',va='bottom')
H2=np.array([1.,9.]); X0=np.array([9.,1.])
def f2(x): return .5*(H2*np.asarray(x,float)**2).sum(-1)
def g2(x): return H2*np.asarray(x,float)
def sphere(rng,k,n=2):
    u=rng.standard_normal((k,n)); return u/np.linalg.norm(u,axis=1,keepdims=True)
# 约束下的查询：C=[1,9]x[-1,1]（只画左端），delta=0.2，tau=delta/sqrt(2)。
fig,A=panels(112,46,3,left=.015,right=.985,top=.98,bottom=.11,wspace=.06)
from matplotlib.patches import Rectangle
rng=np.random.default_rng(12); d=.2; t=d/2**.5
for a in A:
    a.add_patch(Rectangle((1,-1),3,2,fc=BLUE_FILL,ec=BLUE,lw=1.1,zorder=1))
    a.plot([1],[0],'o',color=RED,ms=4.8,mew=0,zorder=6)
    a.set_xlim(.55,2.2); a.set_ylim(-1.05,1.05); a.set_aspect('equal'); a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values(): s.set_visible(False)
def q(a,x,P):
    a.plot([x[0]],[x[1]],'o',color=GREEN,ms=4.2,mew=0,zorder=7)
    for p in P:
        inC=p[0]>=1 and abs(p[1])<=1
        a.plot([p[0]],[p[1]],'o' if inC else 'x',color=GREEN if inC else RED,ms=3.2 if inC else 4,mew=0 if inC else 1.1,zorder=5)
x=np.array([1.,.4]); u=np.array([.6,.8]); th=np.linspace(0,2*np.pi,200)
A[0].plot(x[0]+d*np.cos(th),x[1]+d*np.sin(th),color=GREEN,lw=.85,ls=(0,(3,2)),zorder=4)
q(A[0],x,[x+d*u,x-d*u])
A[1].add_patch(Rectangle((1.2,-.8),3,1.6,fc='none',ec=STROKE,lw=1.0,ls=(0,(4,2)),zorder=2))
x=np.array([1.2,.4]); A[1].plot(x[0]+d*np.cos(th),x[1]+d*np.sin(th),color=GREEN,lw=.85,ls=(0,(3,2)),zorder=4); q(A[1],x,[x+d*u,x-d*u])
A[2].add_patch(Rectangle((1.2,-.8),3,1.6,fc='none',ec=STROKE,lw=1.0,ls=(0,(4,2)),zorder=2))
q(A[2],x,x+t*rng.standard_normal((70,2)))
for a,tg in zip(A,'abc'): tag(fig,a,f'({tg})',.015)
save(fig,HERE,'figure',{'C':'[1,9]x[-1,1]','delta':d,'tau':t,'seed':12})
