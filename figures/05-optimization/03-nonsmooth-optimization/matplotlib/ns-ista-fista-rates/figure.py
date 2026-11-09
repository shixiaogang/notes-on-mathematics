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
# 相关设计的 Lasso：A 为 100x200，列间 AR(1) 相关 rho=0.9，seed=7；lambda=0.005||A^Tb||_inf。
import math
rng=np.random.default_rng(7)
Z=rng.normal(size=(100,200));rho=.9;A_=Z.copy()
for j in range(1,200): A_[:,j]=rho*A_[:,j-1]+math.sqrt(1-rho*rho)*Z[:,j]
A_=A_/np.linalg.norm(A_,axis=0);xt=np.zeros(200);idx=rng.choice(200,10,replace=False);xt[idx]=rng.normal(size=10)*2
b=A_@xt+.02*rng.normal(size=100);lam=.005*np.max(abs(A_.T@b));L=np.linalg.norm(A_,2)**2
S=lambda x,t:np.sign(x)*np.maximum(abs(x)-t,0)
F=lambda x:.5*np.sum((A_@x-b)**2)+lam*np.sum(abs(x))
gr=lambda x:A_.T@(A_@x-b)
def fista(T,restart=False):
    x=np.zeros(200);y=x.copy();th=1.;fx=F(x);V=[fx]
    for t in range(T):
        xn=S(y-gr(y)/L,lam/L);fn=F(xn)
        if restart and fn>fx:
            th=1.;y=x.copy();xn=S(y-gr(y)/L,lam/L);fn=F(xn)
        thn=(1+math.sqrt(1+4*th*th))/2;y=xn+(th-1)/thn*(xn-x);x=xn;th=thn;fx=fn;V.append(fx)
    return np.array(V),x
def ista(T):
    x=np.zeros(200);V=[F(x)]
    for t in range(T):
        x=S(x-gr(x)/L,lam/L);V.append(F(x))
    return np.array(V),x
_,xs=fista(40000,True);Fs=F(xs);R2=np.sum(xs**2);T=4000
Vi,_=ista(T);Vf,_=fista(T);tt=np.arange(1,T+1)
fig,(a,bb)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.1,.97,.98,.26,wspace=.26)
a.loglog(tt,L*R2/(2*tt),color=GREEN,lw=.95,ls='--');a.loglog(tt,2*L*R2/(tt+1)**2,color=YELLOW,lw=.95,ls='--')
a.loglog(tt,Vi[1:]-Fs,color=GREEN,lw=1.4);a.loglog(tt,np.maximum(Vf[1:]-Fs,1e-14),color=YELLOW,lw=1.4)
a.set_xlim(1,T);a.set_ylim(1e-8,1e4);a.set_yticks([1e-8,1e-4,1,1e4]);a.set_xlabel('$T$',labelpad=1);a.set_ylabel('目标差',labelpad=1)
w=list(range(200,1200));bb.semilogy(w,Vf[w]-Fs,color=YELLOW,lw=1.3);bb.semilogy(w,Vi[w]-Fs,color=GREEN,lw=1.4)
bb.set_xlabel('$t$',labelpad=1);bb.set_xlim(200,1199);bb.set_xticks([200,600,1000])
fig.canvas.draw();tag(fig,a,'(a)',y=.055);tag(fig,bb,'(b)',y=.055)
rises=int(np.sum(np.diff(Vf)>0))
print({'L':L,'R2':R2,'gap_ista':[float(Vi[k]-Fs) for k in (10,100,1000,4000)],'gap_f':[float(Vf[k]-Fs) for k in (10,100,1000,4000)],'rises':rises})
save(fig,HERE,'figure',{'m':100,'n':200,'seed':7,'rho':.9,'lambda':float(lam),'L':float(L),'Fstar':float(Fs),'R2':float(R2),'fista_rises':rises})
