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
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# 有限和最小二乘：同一实验按更新次数与样本读取量计时。N=200,d=10,gamma=0.1。
rng=np.random.default_rng(17)
N,d=200,10; A=rng.standard_normal((N,d))*(np.linspace(3,.3,d)); xt=rng.standard_normal(d); b0=A@xt+.3*rng.standard_normal(N); gam=.1
Li=(A*A).sum(1)+gam; Lm=Li.max(); H=A.T@A/N+gam*np.eye(d); xs=np.linalg.solve(H,A.T@b0/N); F=lambda x:.5*((A@x-b0)**2).mean()+.5*gam*(x@x); Fs=F(xs); Lg=np.linalg.eigvalsh(H).max()
print('L',Lg,'Lmax',Lm,'mu',np.linalg.eigvalsh(H).min())
gi=lambda x,i:(A[i]@x-b0[i])*A[i]+gam*x; full=lambda x:H@x-A.T@b0/N
def gd(steps):
    x=np.zeros(d); y=[];
    for k in range(steps): y.append((k*N,k,F(x)-Fs)); x=x-full(x)/Lg
    return np.array(y)
def sgd(reads,al,bs=1):
    x=np.zeros(d);y=[];k=0
    while k*bs<reads:
        if k%max(1,int(N/20/bs))==0: y.append((k*bs,k,F(x)-Fs))
        I=rng.integers(0,N,bs); g=np.mean([gi(x,i) for i in I],0); x=x-al*g; k+=1
    return np.array(y)
def svrg(reads,al):
    x=np.zeros(d);y=[];r=0;u=0
    while r<reads:
        y.append((r,u,F(x)-Fs))
        xh=x.copy(); gh=full(xh); r+=N
        for m in range(N):
            i=rng.integers(0,N); x=x-al*(gi(x,i)-gi(xh,i)+gh); r+=2; u+=1
            if m%20==19: y.append((r,u,F(x)-Fs))
    return np.array(y)
def saga(reads,al):
    x=np.zeros(d); T=np.array([gi(x,i) for i in range(N)]); av=T.mean(0); y=[]; r=N;u=0
    while r<reads:
        if u%20==0: y.append((r,u,F(x)-Fs))
        i=rng.integers(0,N); g=gi(x,i); x=x-al*(g-T[i]+av); av=av+(g-T[i])/N; T[i]=g; r+=1;u+=1
    return np.array(y)
RMAX=N*40
G=gd(40);S=sgd(RMAX,.2/Lm);S2=sgd(RMAX,1./Lm/10,bs=20);V=svrg(RMAX,.25/Lm);A2=saga(RMAX,1/(3*Lm))
print('finals gd',G[-1],'sgd',S[-1],'sgdb',S2[-1],'svrg',V[-1],'saga',A2[-1])
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2,sharey=True)
panel(fig,.125,.965,.97,.25,wspace=.1)
for arr,c,ls,lw in ((G,BLUE,'-',1.4),(S,YELLOW,'-',1.3),(V,GREEN,'-',1.4),(A2,PURPLE,'--',1.3)):
    a.semilogy(arr[:,1],arr[:,2],color=c,lw=lw,ls=ls); b.semilogy(arr[:,0]/N,arr[:,2],color=c,lw=lw,ls=ls)
a.set_xlim(0,400); a.set_xlabel('更新次数',labelpad=1); b.set_xlim(0,40); b.set_xlabel('读取量 / N',labelpad=1); a.set_ylabel('目标差',labelpad=1)
a.set_ylim(1e-5,3e2)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'N':N,'d':d,'seed':17})
