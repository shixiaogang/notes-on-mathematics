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
# 球面与高斯方向：(a) n=2，delta=1 的球面点与 tau=1/sqrt(2) 的高斯点；(b) ||u||/sqrt(n) 的密度（解析式）。
import math
fig,A=panels(112,52,2,left=.08,right=.985,bottom=.28,wspace=.25)
rng=np.random.default_rng(5); a=A[0]; th=np.linspace(0,2*np.pi,300)
a.plot(np.cos(th),np.sin(th),color=GREEN,lw=1.4)
P=rng.standard_normal((90,2))/2**.5
a.plot(P[:,0],P[:,1],'o',color=YELLOW,ms=3,mew=0); a.plot([0],[0],'o',mfc='white',mec=INK,ms=4.4,mew=.9,zorder=6)
a.set_xlim(-2.4,2.4); a.set_ylim(-2.4,2.4); a.set_aspect('equal'); a.set_xticks([-2,0,2]); a.set_yticks([-2,0,2])
b=A[1]; s=np.linspace(.001,2.2,800)
for n,c,ls,l,xy in ((2,YELLOW,'-',r'$n=2$',(.43,.92)),(10,PURPLE,'-',r'$n=10$',(1.28,1.15)),(100,GREEN,'-',r'$n=100$',(1.1,3.7))):
    r=s*n**.5; logp=(1-n/2)*math.log(2)+(n-1)*np.log(r)-r**2/2-math.lgamma(n/2)
    b.plot(s,np.exp(logp)*n**.5,color=c,lw=1.5 if c==YELLOW else 1.4)
    b.text(xy[0],xy[1],l,fontsize=7.5,color=INK)
b.axvline(1,color=INK,lw=.85,ls=(0,(4,2))); b.set_xlim(0,2.2); b.set_ylim(0,4.4); b.set_xticks([0,1,2]); b.set_yticks([0,2,4]); b.set_xlabel(r'$\|u\|_2/\sqrt{n}$',labelpad=0); b.set_ylabel('密度',labelpad=1)
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'seed':5,'delta':1,'tau':2**-.5})
