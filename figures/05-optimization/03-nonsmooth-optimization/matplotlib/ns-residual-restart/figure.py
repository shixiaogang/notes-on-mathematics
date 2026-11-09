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
# 相关设计的 Lasso（同 ns-ista-fista-rates）：(a) FISTA 的目标差与映射残差；(b) 函数值重启。
import math
rng=np.random.default_rng(7)
Z=rng.normal(size=(100,200));rho=.9;A_=Z.copy()
for j in range(1,200): A_[:,j]=rho*A_[:,j-1]+math.sqrt(1-rho*rho)*Z[:,j]
A_=A_/np.linalg.norm(A_,axis=0);xt=np.zeros(200);idx=rng.choice(200,10,replace=False);xt[idx]=rng.normal(size=10)*2
b=A_@xt+.02*rng.normal(size=100);lam=.005*np.max(abs(A_.T@b));L=np.linalg.norm(A_,2)**2
S=lambda x,t:np.sign(x)*np.maximum(abs(x)-t,0)
F=lambda x:.5*np.sum((A_@x-b)**2)+lam*np.sum(abs(x))
gr=lambda x:A_.T@(A_@x-b)
Gm=lambda x:L*(x-S(x-gr(x)/L,lam/L))
def fista(T,restart=False,track=False):
    x=np.zeros(200);y=x.copy();th=1.;fx=F(x);V=[fx];R=[np.linalg.norm(Gm(x))] if track else [];ev=[]
    for t in range(T):
        xn=S(y-gr(y)/L,lam/L);fn=F(xn)
        if restart and fn>fx:
            th=1.;y=x.copy();ev.append(t);xn=S(y-gr(y)/L,lam/L);fn=F(xn)
        thn=(1+math.sqrt(1+4*th*th))/2;y=xn+(th-1)/thn*(xn-x);x=xn;th=thn;fx=fn;V.append(fx)
        if track:R.append(np.linalg.norm(Gm(x)))
    return np.array(V),np.array(R),x,ev
def ista(T):
    x=np.zeros(200);V=[F(x)]
    for t in range(T):
        x=S(x-gr(x)/L,lam/L);V.append(F(x))
    return np.array(V)
_,_,xs,_=fista(40000,True);Fs=F(xs);T=4000
V,R,_,_=fista(T,track=True);Vr,_,_,ev=fista(T,True);Vi=ista(T);tt=np.arange(T+1)
fig,(a,bb)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.08,.97,.98,.26,wspace=.26)
a.semilogy(tt,np.maximum(V-Fs,1e-15),color=YELLOW,lw=1.3);a.semilogy(tt,R,color=PURPLE,lw=1.1)
a.set_xlim(0,T);a.set_ylim(1e-10,1e2);a.set_xlabel('$t$',labelpad=1);a.set_yticks([1e-8,1e-4,1]);a.set_xticks([0,2000,4000])
bb.semilogy(tt,np.maximum(Vi-Fs,1e-15),color=GREEN,lw=1.3);bb.semilogy(tt,np.maximum(V-Fs,1e-15),color=YELLOW,lw=1.3);bb.semilogy(tt,np.maximum(Vr-Fs,1e-15),color=PURPLE,lw=1.3)
bb.set_xlim(0,T);bb.set_ylim(1e-10,1e2);bb.set_yticks([1e-8,1e-4,1]);bb.set_xlabel('$t$',labelpad=1);bb.set_xticks([0,2000,4000])
fig.canvas.draw();tag(fig,a,'(a)',y=.055);tag(fig,bb,'(b)',y=.055)
print({'restarts':len(ev),'first':ev[:6],'gap_end':[float(Vi[-1]-Fs),float(V[-1]-Fs),float(max(Vr[-1]-Fs,0))],'R_end':float(R[-1])})
save(fig,HERE,'figure',{'restarts':len(ev),'first':[int(e) for e in ev[:8]],'T':T})
