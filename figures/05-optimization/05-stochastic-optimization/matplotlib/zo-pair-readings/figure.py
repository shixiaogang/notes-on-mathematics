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
# 成对读数：f(s)=s^2/2，中心 s=1，半径 0.4；(a) 独立噪声 +0.3,-0.3；(b) 共享噪声 +0.3。
fig,A=panels(104,52,2,left=.09,bottom=.28,wspace=.16)
s=np.linspace(.2,1.8,200); h=.4; c=1
T=lambda v:.5+v*1.0
for k,a in enumerate(A):
    a.plot(s,.5*s**2,color=BLUE,lw=1.4)
    a.plot(s,T(s-1),color=INK,lw=.85,ls=(0,(4,2)))
    a.set_xlim(.2,1.8); a.set_ylim(-.15,1.75); a.set_xticks([.6,1,1.4]); a.set_yticks([0,.5,1,1.5]); a.set_xlabel('$s$',labelpad=0)
yp=.5*1.4**2+.3; ym=.5*.6**2-.3
A[0].plot([.6,1.4],[ym,yp],'-o',color=GREEN,lw=1.3,ms=4,mew=0); A[0].plot([.6,1.4],[.18,.98],'o',color=BLUE,ms=3.2,mew=0)
A[0].text(1.0,1.42,r'$D=1.75$',fontsize=7.5,color=INK,ha='right')
yp=.5*1.4**2+.3; ym=.5*.6**2+.3
A[1].plot(s,.5*s**2+.3,color=MUTED,lw=.85)
A[1].plot([.6,1.4],[ym,yp],'-o',color=GREEN,lw=1.3,ms=4,mew=0); A[1].plot([.6,1.4],[.18,.98],'o',color=BLUE,ms=3.2,mew=0)
A[1].text(1.0,1.42,r'$D=1$',fontsize=7.5,color=INK,ha='right')
A[0].set_ylabel('$y$',labelpad=0); A[1].set_yticklabels([])
for a,t in zip(A,'ab'): tag(fig,a,f'({t})',.02)
save(fig,HERE,'figure',{'f':'s^2/2','center':1,'radius':.4,'independent':[.3,-.3],'shared':.3})
