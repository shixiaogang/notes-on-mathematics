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
# 贯穿例 sigma=1，x0=(9,1)，300 次独立运行的平均目标差。(a) alpha=0.02, delta=0.1,0.5,2；(b) delta=0.5：固定步长与递减步长，以及尺度也递减。
fig,A=panels(112,54,2,left=.115,right=.965,bottom=.27,wspace=.24)
def run(af,df,T,R=300,seed=1):
    rng=np.random.default_rng(seed); x=np.tile(X0,(R,1)); out=[f2(x).mean()]
    for t in range(T):
        u=sphere(rng,R); z=rng.standard_normal((R,2)); d=df(t)
        D=(f2(x+d*u)+z[:,0]-f2(x-d*u)-z[:,1])/(2*d); x=x-af(t)*2*D[:,None]*u; out.append(f2(x).mean())
    return np.array(out)
T=3000; t=np.arange(T+1)
for d,c,lw in ((.1,PURPLE,1.3),(.5,GREEN,1.3),(2.,YELLOW,1.6)):
    A[0].semilogy(t,run(lambda k:.02,lambda k:d,T),color=c,lw=lw)
A[1].semilogy(t,run(lambda k:.02,lambda k:.5,T),color=GREEN,lw=1.3)
A[1].semilogy(t,run(lambda k:.02/(1+k/100),lambda k:.5,T),color=YELLOW,lw=1.6)
A[1].semilogy(t,run(lambda k:.02/(1+k/100)**.75,lambda k:.5/(1+k/100)**.1,T),color=PURPLE,lw=1.4)
for a,tg in zip(A,'ab'):
    a.set_xlim(0,T); a.set_ylim(1e-3,1e2); a.set_xticks([0,1500,3000]); a.set_xlabel('$t$',labelpad=0); tag(fig,a,f'({tg})',.02)
A[0].set_ylabel('平均目标差',labelpad=1)
A[0].text(1500,2.3,r'$\delta=0.1$',fontsize=7.5,color=INK); A[0].text(1500,.1,r'$\delta=0.5$',fontsize=7.5,color=INK); A[0].text(1500,.0065,r'$\delta=2$',fontsize=7.5,color=INK)
save(fig,HERE,'figure',{'sigma':1,'runs':300})
