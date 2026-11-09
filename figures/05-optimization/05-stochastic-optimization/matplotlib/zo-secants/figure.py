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
# 差商的几何：phi(s)=s^2/2+s^3/6，s0=1，h=0.8；切线斜率 1.5，前向差商 2.4067，中心差商 1.6067。
fig,ax=figure(width_mm=84,height_mm=56)
phi=lambda s:.5*s**2+s**3/6
s=np.linspace(-.05,2.05,300); h=.8; s0=1.
ax.plot(s,phi(s),color=BLUE,lw=1.4)
ax.plot(s,phi(s0)+1.5*(s-s0),color=INK,lw=.95,ls=(0,(4,2)))
fw=(phi(s0+h)-phi(s0))/h; ce=(phi(s0+h)-phi(s0-h))/(2*h)
ax.plot(s,phi(s0)+fw*(s-s0),color=YELLOW,lw=1.3); ax.plot(s,phi(s0-h)+ce*(s-s0+h),color=GREEN,lw=1.3)
ax.plot([s0,s0+h],[phi(s0),phi(s0+h)],'o',color=YELLOW,ms=4,mew=0,zorder=5)
ax.plot([s0-h,s0+h],[phi(s0-h),phi(s0+h)],'o',color=GREEN,ms=4,mew=0,zorder=4)
ax.plot([s0],[phi(s0)],'o',color=BLUE,ms=4,mew=0,zorder=6)
ax.set_xlim(-.05,2.05); ax.set_ylim(-.3,3.4); ax.set_xticks([.2,1,1.8]); ax.set_xticklabels(['$s_0-h$','$s_0$','$s_0+h$']); ax.set_yticks([0,1,2,3]); ax.set_ylabel(r'$\varphi(s)$',labelpad=0)
ax.text(.93,.08,'前向',fontsize=7.5,color=INK); ax.text(.28,.72,'中心',fontsize=7.5,color=INK); ax.text(1.72,1.42,'切线',fontsize=7.5,color=INK)
save(fig,HERE,'figure',{'phi':'s^2/2+s^3/6','s0':1,'h':.8,'forward':fw,'central':ce,'tangent':1.5})
