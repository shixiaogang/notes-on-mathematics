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
# 差商方差与尺度 h 的关系（Monte Carlo，每点 4e6 次）：x=0.5，f=x^2/2。
# 独立噪声 std 0.1；共享 Lipschitz 样本 F=f+xi*x，xi~N(0,0.09)；共享指示样本 F=1{x>xi}，xi~N(0,1)。
fig,ax=figure(width_mm=96,height_mm=60)
rng=np.random.default_rng(11); H=np.logspace(-3,-.3,10); N=4000000; x=.5
V1=[];V2=[];V3=[]
for h in H:
    z=.1*rng.standard_normal((N,2)); V1.append(((z[:,0]-z[:,1])/(2*h)).var())
    xi=.3*rng.standard_normal(N); V2.append((xi).var()*(1.0)) # 差商的随机部分恒为 xi
    xi=rng.standard_normal(N); D=((x+h>xi).astype(float)-(x-h>xi).astype(float))/(2*h); V3.append(D.var())
ax.loglog(H,V1,'-o',color=YELLOW,lw=1.6,ms=3.4,mew=0); ax.loglog(H,V3,'-o',color=PURPLE,lw=1.4,ms=3.4,mew=0); ax.loglog(H,V2,'-o',color=GREEN,lw=1.4,ms=3.4,mew=0)
ax.set_xlabel('$h$',labelpad=1); ax.set_ylabel('差商方差',labelpad=1)
ax.text(6e-3,3.5e2,'独立噪声',fontsize=7.5,color=INK); ax.text(1.6e-3,13,'共享指示样本',fontsize=7.5,color=INK); ax.text(1.6e-3,.15,'共享光滑样本',fontsize=7.5,color=INK)
save(fig,HERE,'figure',{'x':x,'N':N,'seed':11})
