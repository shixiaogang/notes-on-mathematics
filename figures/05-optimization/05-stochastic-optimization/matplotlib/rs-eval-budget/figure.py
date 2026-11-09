from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 五维 Rastrigin，[-5.12,5.12]^5，统一预算 10000 次评价，每种方法 41 次独立运行（种子固定）
n=5; Bd=10000; lo,hi=-5.12,5.12; 
def F(x): x=np.atleast_2d(x); return 10*n+(x**2-10*np.cos(2*np.pi*x)).sum(1)
def rs_(r):
    y=F(r.uniform(lo,hi,(Bd,n))); return y
def sa(r):
    x=r.uniform(lo,hi,n); fx=F(x)[0]; o=[fx]
    for t in range(Bd-1):
        T=30*(.01/30)**(t/(Bd-2)); y=x+.4*r.standard_normal(n); y=np.where((y<lo)|(y>hi),x,y); fy=F(y)[0]
        if fy<=fx or r.random()<np.exp(-(fy-fx)/T): x,fx=y,fy
        o.append(fx)
    return np.array(o)
def ga(r,N=50):
    P=r.uniform(lo,hi,(N,n)); c=F(P); o=list(c)
    while len(o)<Bd:
        Q=[P[np.argmin(c)].copy()]
        while len(Q)<N:
            i=r.integers(N,size=(2,2)); a=P[i[0][np.argmin(c[i[0]])]]; b=P[i[1][np.argmin(c[i[1]])]]; u=r.uniform(-.25,1.25,n); ch=a+u*(b-a); m=r.random(n)<.2; ch=ch+m*.3*r.standard_normal(n); Q.append(np.clip(ch,lo,hi))
        P=np.array(Q); c2=F(P[1:]); c=np.r_[c[np.argmin(c)],c2]; o+=list(c2)
    return np.array(o[:Bd])
def pso(r,N=40):
    x=r.uniform(lo,hi,(N,n)); v=r.uniform(-1,1,(N,n)); p=x.copy(); fp=F(x); o=list(fp)
    while len(o)<Bd:
        G=p[np.argmin(fp)]; v=.7298*v+1.496*r.random((N,n))*(p-x)+1.496*r.random((N,n))*(G-x); v=np.clip(v,-2,2); nx=np.clip(x+v,lo,hi); v=nx-x; x=nx; fx=F(x); m=fx<fp; p[m]=x[m]; fp[m]=fx[m]; o+=list(fx)
    return np.array(o[:Bd])
def cma(r,lam=20):
    m=r.uniform(lo,hi,n); s=2.5; mu=lam//2; w=np.log(mu+.5)-np.log(np.arange(1,mu+1)); w/=w.sum(); me=1/(w**2).sum(); cs=(me+2)/(n+me+5); ds=1+2*max(0,np.sqrt((me-1)/(n+1))-1)+cs; cc=(4+me/n)/(n+4+2*me/n); c1=2/((n+1.3)**2+me); cm=min(1-c1,2*(me-2+1/me)/((n+2)**2+me)); chi=np.sqrt(n)*(1-1/(4*n)+1/(21*n*n)); C=np.eye(n); ps=np.zeros(n); pc=np.zeros(n); o=[]; g=0
    while len(o)<Bd:
        g+=1; d,B=np.linalg.eigh(C); d=np.sqrt(np.maximum(d,1e-20)); z=r.standard_normal((lam,n)); y=((B*d)@z.T).T; x=m+s*y; fx=F(x); o+=list(fx); idx=np.argsort(fx)[:mu]; yw=w@y[idx]; m=m+s*yw; ps=(1-cs)*ps+np.sqrt(cs*(2-cs)*me)*(B@((B.T@yw)/d)); hs=np.linalg.norm(ps)/np.sqrt(1-(1-cs)**(2*g))/chi<1.4+2/(n+1); pc=(1-cc)*pc+hs*np.sqrt(cc*(2-cc)*me)*yw; C=(1-c1-cm+c1*(1-hs)*cc*(2-cc))*C+c1*np.outer(pc,pc)+cm*(y[idx].T*w)@y[idx]; C=(C+C.T)/2; s*=np.exp(cs/ds*(np.linalg.norm(ps)/chi-1))
    return np.array(o[:Bd])
Al=[('rs',rs_,MUTED,(0,(4,2))),('sa',sa,YELLOW,'-'),('ga',ga,PURPLE,'-'),('pso',pso,BLUE,'-'),('cma',cma,GREEN,'-')]
R=41; H={}
for k,(nm,fn,_,_) in enumerate(Al): H[nm]=np.array([np.minimum.accumulate(fn(np.random.default_rng(1000*k+s))) for s in range(R)])
x=np.arange(1,Bd+1); tgt=3.0; out={}
fig,axes=figure(width_mm=112,height_mm=58,ncols=3); panel(fig,.11,.975,.97,.25,.5)
idx=np.unique(np.round(np.logspace(0,4,200)).astype(int))-1
for nm,_,c,ls in Al:
    h=H[nm]; axes[0].plot(x[idx],np.median(h,axis=0)[idx]+1e-3*0,color=c,lw=1.4,ls=ls)
    hit=(h<=tgt).mean(0); axes[1].plot(x[idx],hit[idx],color=c,lw=1.4,ls=ls); out[nm]=dict(median=float(np.median(h[:,-1])),q25=float(np.quantile(h[:,-1],.25)),q75=float(np.quantile(h[:,-1],.75)),best=float(h[:,-1].min()),success=float(hit[-1]))
print(out)
for ax in axes[:2]: ax.set_xscale('log'); ax.set_xlim(10,1e4); ax.set_xticks([10,1000]) ; ax.minorticks_off(); ax.set_xlabel('评价次数',labelpad=1)
axes[0].set_yscale('log'); axes[0].set_ylim(.5,120); axes[0].set_yticks([1,10,100]); axes[0].set_yticklabels(['1','10','100']); axes[0].set_ylabel('最好值',labelpad=1)
axes[1].set_ylim(0,1.02); axes[1].set_yticks([0,.5,1]); axes[1].set_yticklabels(['0','0.5','1']); axes[1].set_ylabel('达标比例',labelpad=1)
h=H['ga']; bestg=(0,0,0)
for j_,r_ in enumerate(h):
    ch_=np.flatnonzero(np.diff(r_)<0)
    for g_ in range(len(ch_)-1):
        drop=r_[ch_[g_]+1]-r_[ch_[g_+1]+1]
        if drop>=.8 and ch_[g_+1]-ch_[g_]>bestg[0]: bestg=(int(ch_[g_+1]-ch_[g_]),j_,g_)
_,j,g=bestg; r=h[j]; ch=np.flatnonzero(np.diff(r)<0); print(j,ch[g],ch[g+1],r[ch[g]+1],r[ch[g+1]+1],r[-1])
c=axes[2]; c.plot(x,r,color=PURPLE,lw=1.4); c.set_xscale('log'); c.set_xlim(50,Bd); c.set_ylim(0,20); c.set_xticks([100,1000,10000]); c.minorticks_off(); c.set_yticks([0,10,20]); c.set_xlabel('评价次数',labelpad=1); c.set_ylabel('最好值',labelpad=1); c.axvspan(ch[g],ch[g+1],facecolor=YELLOW_FILL,edgecolor='none',zorder=0)
tags(fig,axes); save(fig,HERE,'figure',{'n':n,'budget':Bd,'runs':R,'target':tgt,'summary':out,'plateau':[int(ch[g]),int(ch[g+1])]})
