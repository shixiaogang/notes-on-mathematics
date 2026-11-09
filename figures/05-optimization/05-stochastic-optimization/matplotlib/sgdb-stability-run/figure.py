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
# 样本替换的有限步响应：逐项 ridge 最小二乘，耦合相同下标路径。
rng=np.random.default_rng(29)
N,d=100,5; A=rng.standard_normal((N,d)); xt=np.ones(d); b0=A@xt+.3*rng.standard_normal(N); gam=.2
k=0; Anew=rng.standard_normal(d)*1.; bnew=Anew@xt+.3*rng.standard_normal()
Li=(A*A).sum(1)+gam; Lm=max(Li.max(),Anew@Anew+gam); al=1./Lm; mu=gam
def gi(x,i,alt): 
    a,b=(Anew,bnew) if (alt and i==k) else (A[i],b0[i])
    return (a@x-b)*a+gam*x
def pair(T,path):
    x=np.zeros(d);y=np.zeros(d);D=[0.];G=0.
    for i in path:
        if i==k: G=max(G,np.linalg.norm(gi(x,i,False)),np.linalg.norm(gi(y,i,True)))
        x=x-al*gi(x,i,False);y=y-al*gi(y,i,True);D.append(np.linalg.norm(x-y))
    return np.array(D),G
T=400;R=1500;all_=[];Gmax=0
for r in range(R):
    path=rng.integers(0,N,T); D,G=pair(T,path); all_.append(D); Gmax=max(Gmax,G)
all_=np.array(all_); mean=all_.mean(0)
single_path=rng.integers(0,N,T); s,_=pair(T,single_path)
print('Lm',Lm,'al',al,'Gmax',Gmax,'mean at 100,400',mean[[100,400]],'non-exp bound',2*Gmax/N*al*400,'contract limit',2*Gmax/(N*mu))
ts=np.arange(T+1)
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.125,.965,.97,.26,wspace=.32)
a.plot(ts,s,color=GREEN,lw=1.1); a.set_xlim(0,400); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('$\\delta^{(t)}$',labelpad=1); a.set_ylim(bottom=0)
b.semilogy(ts,mean+1e-9,color=GREEN,lw=1.4); b.semilogy(ts,2*Gmax/N*al*ts+1e-9,color=PURPLE,lw=1.2)
limit=[0.]
for t in range(T): limit.append((1-al*mu)*limit[-1]+2*al*Gmax/N)
b.semilogy(ts,np.array(limit)+1e-9,color=YELLOW,lw=1.3,ls='--')
b.set_xlim(1,400); b.set_ylim(1e-3,2); b.set_xlabel('$t$',labelpad=1); b.set_ylabel('平均距离与上界',labelpad=1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'N':N,'d':d,'seed':29,'gamma':gam})
