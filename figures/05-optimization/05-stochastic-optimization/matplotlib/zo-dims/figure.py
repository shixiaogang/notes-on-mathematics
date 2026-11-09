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
# n=20 的二次目标 H=diag(linspace(1,9,20))，x0=3*1；每条曲线为 30 次运行平均，横轴是函数读数次数。
fig,A=panels(112,56,2,left=.115,right=.965,bottom=.26,wspace=.26)
n=20; H=np.linspace(1,9,n); F=lambda x:.5*(H*x**2).sum(-1); L=9.
def run(kind,m,sig,Qmax,d=.1,R=30,seed=0):
    rng=np.random.default_rng(seed); x=3*np.ones((R,n)); Q=[0]; V=[F(x).mean()]; q=0
    if kind=='coord': a=1/L; per=2*n
    else: a=1/(L*(1+(n-1)/m)); per=2*m
    while q<Qmax:
        if kind=='coord':
            gh=H*x+sig/(2**.5*d)*rng.standard_normal((R,n))
        else:
            u=rng.standard_normal((R,m,n)); u/=np.linalg.norm(u,axis=2,keepdims=True)
            D=((H*x)[:,None,:]*u).sum(2)+sig/(2**.5*d)*rng.standard_normal((R,m))
            gh=n*(D[:,:,None]*u).mean(1)
        x=x-a*gh; q+=per; Q.append(q); V.append(F(x).mean())
    return np.array(Q),np.array(V)
for ax,sig,Qm in zip(A,(0,.1),(6000,6000)):
    for kind,m,c,lw in (('coord',0,YELLOW,1.7),('sph',1,GREEN,1.3),('sph',5,PURPLE,1.3)):
        Q,V=run(kind,m,sig,Qm); ax.semilogy(Q,V,color=c,lw=lw)
    ax.set_xlim(0,Qm); ax.set_xticks([0,3000,6000]); ax.set_xlabel('函数读数次数',labelpad=0)
A[0].set_ylabel('平均目标差',labelpad=1)
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'n':n,'runs':30,'delta':.1,'sigma':[0,.1]})
