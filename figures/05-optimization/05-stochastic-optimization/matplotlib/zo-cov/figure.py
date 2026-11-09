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
# 坐标差分的噪声协方差：n=2，sigma=h=0.1。(a) 前向共用中心读数 Cov=[[2,1],[1,2]]；(b) 中心差分 Cov=0.5 I。
fig,A=panels(104,58,2,left=.1,right=.985,bottom=.25,wspace=.22)
rng=np.random.default_rng(21); N=350; s=.1; h=.1
z=s*rng.standard_normal((N,3)); F=np.c_[(z[:,1]-z[:,0])/h,(z[:,2]-z[:,0])/h]
z=s*rng.standard_normal((N,4)); C=np.c_[(z[:,0]-z[:,1])/(2*h),(z[:,2]-z[:,3])/(2*h)]
th=np.linspace(0,2*np.pi,300)
def ell(a,S):
    w,V=np.linalg.eigh(S); E=2*V@np.diag(w**.5)@np.c_[np.cos(th),np.sin(th)].T; a.plot(E[0],E[1],color=INK,lw=1.1,zorder=5)
for a,P,S,t in zip(A,(F,C),(np.array([[2,1],[1,2.]]),.5*np.eye(2)),'ab'):
    a.plot(P[:,0],P[:,1],'o',color=RED,ms=2.4,mew=0); ell(a,S)
    a.set_xlim(-6,6); a.set_ylim(-6,6); a.set_aspect('equal'); a.set_xticks([-4,0,4]); a.set_yticks([-4,0,4]); a.set_xlabel('第一分量误差',labelpad=0); tag(fig,a,f'({t})',.02)
A[0].set_ylabel('第二分量误差',labelpad=0)
save(fig,HERE,'figure',{'sigma':s,'h':h,'seed':21})
