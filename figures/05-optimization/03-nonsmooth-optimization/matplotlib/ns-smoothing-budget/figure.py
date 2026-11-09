from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# f(x)=max_i(a_i^T x+b_i)，R^2，7 个单位方向，b 固定；对熵平滑做 Nesterov 加速。
import math, itertools
th_=2*np.pi*np.arange(7)/7;Aa=np.c_[np.cos(th_),np.sin(th_)];bb_=np.array([0,.3,-.2,.5,.1,-.4,.2]);m=7
f=lambda x:np.max(Aa@x+bb_)
best=1e9
for i,j,k in itertools.combinations(range(m),3):
    M=np.c_[Aa[[i,j,k]],-np.ones(3)]
    if abs(np.linalg.det(M))<1e-10: continue
    s=np.linalg.solve(M,-bb_[[i,j,k]]);best=min(best,f(s[:2])) if abs(f(s[:2])-s[2])<1e-9 else best
fs=best
def gm(x,mu):
    l=Aa@x+bb_;z=(l-l.max())/mu;w=np.exp(z);w/=w.sum();return Aa.T@w
def nag(mu,T,x0=(3.,2.)):
    x=np.array(x0);y=x.copy();th=1.;V=[f(x)];a=mu
    for t in range(T):
        xn=y-a*gm(y,mu);thn=(1+math.sqrt(1+4*th*th))/2;y=xn+(th-1)/thn*(xn-x);x=xn;th=thn;V.append(f(x))
    return np.array(V),x
def sub(al,T):
    x=np.array([3.,2.]);b=f(x);B=[b]
    for t in range(T):
        i=np.argmax(Aa@x+bb_);x=x-al*Aa[i];b=min(b,f(x));B.append(b)
    return np.array(B)
def cont(eps_end,T):
    mu=1.;x=np.array([3.,2.]);V=[f(x)];used=0
    while used<T:
        n=int(8/mu**.5)+10;n=min(n,T-used)
        v,x=nag(mu,n,x0=x);V+=list(v[1:]);used+=n;mu=max(mu/2,eps_end)
    return np.array(V)
T=4000
fig,(A,B)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.09,.97,.98,.26,wspace=.26)
tt=np.arange(1,T+1);pl=[]
for mu,ls in ((1.,'-'),(.1,'--'),(.01,':')):
    V,_=nag(mu,T);pl.append((mu,float(V[-1]-fs)));A.loglog(tt,V[1:]-fs,color=GREEN,lw=1.4,ls=ls);A.axhline(mu*math.log(m),color=MUTED,lw=.7,ls=':')
A.set_xlim(1,T);A.set_ylim(1e-4,6);A.set_xlabel('$t$',labelpad=1);A.set_ylabel('原目标差',labelpad=1)
eps=.02;mu=eps/(2*math.log(m));V,_=nag(mu,T)
Bs=sub(eps,T);Vb=np.minimum.accumulate(V);C=np.minimum.accumulate(cont(mu,T))
B.loglog(tt,Bs[1:]-fs,color=YELLOW,lw=1.4);B.loglog(tt,Vb[1:]-fs,color=GREEN,lw=1.4);B.loglog(tt,C[1:]-fs,color=PURPLE,lw=1.3,ls='--')
B.axhline(eps,color=MUTED,lw=.8,ls=':')
B.set_xlim(1,T);B.set_ylim(1e-4,6);B.set_xlabel('$t$',labelpad=1)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
print('fs',fs,'plateaus',pl,'end',float(Bs[-1]-fs),float(Vb[-1]-fs),float(C[-1]-fs),'hit',[int(np.argmax(v-fs<=eps)) for v in (Bs,Vb,C)])
save(fig,HERE,'figure',{'fstar':float(fs),'b':bb_.tolist(),'eps':eps,'mu':mu})
