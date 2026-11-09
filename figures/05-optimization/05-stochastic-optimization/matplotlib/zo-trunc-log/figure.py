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
# 截断误差随扰动尺度变化：phi(s)=s^2/2+s^3/6 在 s0=1 处，导数精确值 1.5。
fig,ax=figure(width_mm=84,height_mm=56)
phi=lambda s:.5*s**2+s**3/6
h=np.logspace(-3,0,60); s0=1.
ef=np.abs((phi(s0+h)-phi(s0))/h-1.5); ec=np.abs((phi(s0+h)-phi(s0-h))/(2*h)-1.5)
ax.loglog(h,ef,color=YELLOW,lw=1.6); ax.loglog(h,ec,color=GREEN,lw=1.4)
ax.loglog(h,h,color=INK,lw=.85,ls=(0,(4,2))); ax.loglog(h,h**2/6,color=INK,lw=.85,ls=(0,(1,2)))
ax.set_xlabel('$h$',labelpad=1); ax.set_ylabel('差商误差',labelpad=1); ax.set_xlim(1e-3,1)
ax.text(.012,.032,'前向',fontsize=7.5,color=INK); ax.text(.1,3.0e-4,'中心',fontsize=7.5,color=INK)
save(fig,HERE,'figure',{'phi':'s^2/2+s^3/6','s0':1})
