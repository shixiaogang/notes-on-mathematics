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
# 40 项背包（种子 2），种群 30，二元锦标赛，单点交叉，保留一个精英，超重按罚项计。比较变异率 0 与 1/40
rng0=np.random.default_rng(2); n=40; v=rng0.integers(10,60,n); w=rng0.integers(5,40,n); cap=int(.4*w.sum())
dp=np.zeros(cap+1,int)
for a,b in zip(v,w): dp[b:]=np.maximum(dp[b:],dp[:cap+1-b]+a)
opt=int(dp[cap])
def cost(P): return -(P@v)+50*np.maximum(0,P@w-cap)
def run(pm,seed,G=150,N=30):
    r=np.random.default_rng(seed); P=(r.random((N,n))<.4).astype(int); D=[];B=[]; bf=np.inf
    for g in range(G+1):
        c=cost(P); ok=(P@w<=cap)
        if ok.any(): bf=min(bf,c[ok].min())
        D.append(float(np.mean(2*P.mean(0)*(1-P.mean(0))))*N/(N-1)); B.append(bf)
        e=P[np.argmin(c)].copy(); Q=[]
        while len(Q)<N-1:
            i=r.integers(N,size=(2,2)); a=P[i[0][np.argmin(c[i[0]])]]; b=P[i[1][np.argmin(c[i[1]])]]; k=r.integers(1,n)
            for ch in (np.r_[a[:k],b[k:]],np.r_[b[:k],a[k:]]): Q.append(ch^(r.random(n)<pm))
        P=np.array(Q[:N-1]+[e])
    return D,B
fig,axes=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.115,.975,.96,.26,.34)
res={}
for pm,col in ((0,YELLOW),(1/40,GREEN)):
    R=[run(pm,s) for s in range(31)]; d=np.median([x[0] for x in R],axis=0); b=np.median([x[1] for x in R],axis=0); axes[0].plot(d,color=col,lw=1.5); axes[1].plot((b+opt)/opt,color=col,lw=1.5); res[pm]=(float(d[-1]),float((b[-1]+opt)/opt))
print(opt,res)
axes[0].set_xlim(0,150); axes[0].set_ylim(0,.52); axes[0].set_xticks([0,75,150]); axes[0].set_yticks([0,.25,.5]); axes[0].set_yticklabels(['0','0.25','0.5']); axes[0].set_xlabel('代数',labelpad=1); axes[0].set_ylabel('多样性',labelpad=1)
axes[1].set_xlim(0,150); axes[1].set_ylim(0,.25); axes[1].set_xticks([0,75,150]); axes[1].set_yticks([0,.1,.2]); axes[1].set_yticklabels(['0','0.1','0.2']); axes[1].set_xlabel('代数',labelpad=1); axes[1].set_ylabel('相对间隙',labelpad=1)
tags(fig,axes); save(fig,HERE,'figure',{'optimum':opt,'capacity':cap,'runs':31,'final':res})
