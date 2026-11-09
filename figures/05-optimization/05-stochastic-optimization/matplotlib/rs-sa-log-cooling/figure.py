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
# 双谷链精确计算：对数降温 T=c/log(t+2)，从 x=2 出发，P(X_t 在全局最小)
f=np.array([3,1,3,5,2,0,2.]); N=2000000
marks=np.unique(np.round(np.logspace(0,np.log10(N),160)).astype(int))
def step(d,T):
    up=.5*np.minimum(1,np.exp(-(f[1:]-f[:-1])/T)); dn=.5*np.minimum(1,np.exp(-(f[:-1]-f[1:])/T))
    out=np.zeros(7); out[1:]+=d[:-1]*up; out[:-1]+=d[1:]*dn
    stay=np.ones(7); stay[:-1]-=up; stay[1:]-=dn; return out+d*stay
fig,ax=figure(width_mm=100,height_mm=54)
res={}
for c,col,ls in ((1,YELLOW,'-'),(2,PURPLE,'-'),(4,GREEN,'-'),(8,MUTED,(0,(4,2)))):
    d=np.zeros(7); d[1]=1; ys=[]; j=0
    for t in range(N):
        d=step(d,c/np.log(t+2))
        if t+1==marks[j]:
            ys.append(d[5]); j+=1
    ax.plot(marks,ys,color=col,lw=1.5,ls=ls); res[c]=ys[-1]; ax.text(marks[-1]*1.25,ys[-1]+(.03 if c==1 else 0),f'$c={c}$',fontsize=7.5,va='center',ha='left')
print(res)
ax.set_xscale('log'); ax.set_xlim(1,N*8); ax.set_ylim(0,1.02); ax.set_yticks([0,.25,.5,.75,1]); ax.set_yticklabels(['0','0.25','0.5','0.75','1']); ax.set_xticks([1,1e2,1e4,1e6]); ax.minorticks_off(); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel(r"$P(x^{(t)}=6)$',labelpad=1)
save(fig,HERE,'figure',{'f':f.tolist(),'schedule':'c/log(t+2)','start':2,'final':res})
