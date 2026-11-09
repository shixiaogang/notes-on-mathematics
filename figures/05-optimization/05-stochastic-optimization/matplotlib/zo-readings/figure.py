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
# 精确读数、加性噪声读数与样本函数：phi(s)=s^2/2；噪声标准差 0.6；样本函数 s^2/2+xi*s。
fig,A=panels(112,46,3,left=.07,bottom=.31,wspace=.14)
s=np.linspace(-3,3,300); q=np.linspace(-2.7,2.7,10); rng=np.random.default_rng(14)
for a in A:
    a.plot(s,.5*s**2,color=BLUE,lw=1.4,zorder=3); a.set_xlim(-3,3); a.set_ylim(-1.8,5.2); a.set_xticks([-2,0,2]); a.set_yticks([0,2,4]); a.set_xlabel('$s$',labelpad=0)
A[0].plot(q,.5*q**2,'o',color=GREEN,ms=3.6,mew=0,zorder=4)
A[1].plot(q,.5*q**2+.6*rng.standard_normal(10),'o',color=GREEN,ms=3.6,mew=0,zorder=4)
for xi in (-.8,-.3,.4,.9):
    A[2].plot(s,.5*s**2+xi*s,color=MUTED,lw=.8,zorder=2)
    A[2].plot(q[[2,7]] if xi>0 else q[[1,5]],(.5*q**2+xi*q)[[2,7]] if xi>0 else (.5*q**2+xi*q)[[1,5]],'o',color=GREEN,ms=3.6,mew=0,zorder=4)
A[1].set_yticklabels([]); A[2].set_yticklabels([]); A[0].set_ylabel('$y$',labelpad=0)
for a,t in zip(A,'abc'): tag(fig,a,f'({t})',.02)
save(fig,HERE,'figure',{'phi':'s^2/2','noise_std':.6,'seed':14})
