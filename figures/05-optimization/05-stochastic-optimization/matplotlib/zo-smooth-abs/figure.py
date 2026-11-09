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
# |x| 的平滑：球平滑 delta=1（一维区间），高斯平滑 tau=1/sqrt(3)（方差与区间扰动相同）。
import math
fig,A=panels(112,50,2,left=.09,right=.985,bottom=.29,wspace=.22)
x=np.linspace(-2.5,2.5,801); d=1.; t=1/3**.5
ball=np.where(np.abs(x)<=d,(x**2+d**2)/(2*d),np.abs(x))
erf=np.vectorize(math.erf)
gs=t*(2/np.pi)**.5*np.exp(-x**2/(2*t**2))+x*erf(x/(2**.5*t))
A[0].plot(x,np.abs(x),color=BLUE,lw=1.4); A[0].plot(x,ball,color=GREEN,lw=1.4); A[0].plot(x,gs,color=YELLOW,lw=1.6,ls=(0,(5,2)))
A[0].set_xlim(-2.5,2.5); A[0].set_ylim(-.1,2.6); A[0].set_xticks([-2,-1,0,1,2]); A[0].set_yticks([0,1,2]); A[0].set_xlabel('$x$',labelpad=0); A[0].set_ylabel('函数值',labelpad=1)
xm=np.concatenate([x[x<0],[np.nan],x[x>0]]); ym=np.concatenate([-np.ones((x<0).sum()),[np.nan],np.ones((x>0).sum())])
A[1].plot(xm,ym,color=BLUE,lw=1.4); A[1].plot(x,np.clip(x/d,-1,1),color=GREEN,lw=1.4); A[1].plot(x,erf(x/(2**.5*t)),color=YELLOW,lw=1.6,ls=(0,(5,2)))
A[1].set_xlim(-2.5,2.5); A[1].set_ylim(-1.25,1.25); A[1].set_xticks([-2,-1,0,1,2]); A[1].set_yticks([-1,0,1]); A[1].set_xlabel('$x$',labelpad=0); A[1].set_ylabel('导数',labelpad=1)
A[0].text(.02,.27,'',fontsize=7.5)
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'f':'|x|','delta':d,'tau':t})
