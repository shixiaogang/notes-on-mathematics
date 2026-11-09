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
# 平滑对解的影响：(a) f=max(x,-2x) 与 delta=1 的区间平滑；(b) f=-|x| 与 delta=1 的区间平滑。
fig,A=panels(112,50,2,left=.09,right=.985,bottom=.29,wspace=.22)
x=np.linspace(-2.2,2.2,1601); d=1.
v=(np.linspace(-1,1,2001)[:,None]); 
f=lambda y:np.maximum(y,-2*y)
A[0].plot(x,f(x),color=BLUE,lw=1.4); Fd=f(x[:,None]+d*v.T).mean(1); A[0].plot(x,Fd,color=GREEN,lw=1.4)
A[0].plot([0],[0],'o',color=RED,ms=4.8,mew=0,zorder=6); k=Fd.argmin(); A[0].plot([x[k]],[Fd[k]],'o',mfc='white',mec=GREEN,ms=4.8,mew=1,zorder=6)
A[0].set_xlim(-2.2,2.2); A[0].set_ylim(-.2,3.0); A[0].set_xticks([-2,-1,0,1,2]); A[0].set_yticks([0,1,2,3]); A[0].set_xlabel('$x$',labelpad=0); A[0].set_ylabel('函数值',labelpad=1)
g=lambda y:-np.abs(y); Gd=g(x[:,None]+d*v.T).mean(1)
A[1].plot(x,g(x),color=BLUE,lw=1.4); A[1].plot(x,Gd,color=GREEN,lw=1.4); A[1].plot([0],[-.5],'o',mfc='white',mec=GREEN,ms=4.8,mew=1,zorder=6)
A[1].set_xlim(-2.2,2.2); A[1].set_ylim(-2.4,.3); A[1].set_xticks([-2,-1,0,1,2]); A[1].set_yticks([-2,-1,0]); A[1].set_xlabel('$x$',labelpad=0)
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'delta':d,'argmin_smoothed':float(x[k])})
print(x[k],Fd[k])
