from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Experiment on one random model: max c'x, Ax<=b, A,c uniform on (0,1), b=1, m=n; Dantzig tableau, 30 seeds.
def pivots(m,n,seed):
    r=np.random.default_rng(seed);A=r.uniform(size=(m,n));c=r.uniform(size=n);b=np.ones(m)
    T=np.hstack([A,np.eye(m),b[:,None]]);z=np.concatenate([-c,np.zeros(m+1)]);k=0
    while True:
        j=int(np.argmin(z[:-1]))
        if z[j]>-1e-10: return k
        col=T[:,j];mask=col>1e-10
        ratios=np.where(mask,T[:,-1]/np.where(mask,col,1),np.inf);i=int(np.argmin(ratios))
        T[i]/=T[i,j]
        T-=np.outer(T[:,j]*(np.arange(m)!=i),T[i]);z-=z[j]*T[i];k+=1
Ms=[10,20,40,80,160,320]
mean=[];lo=[];hi=[]
for m in Ms:
    v=[pivots(m,m,s) for s in range(30)];mean.append(np.mean(v));lo.append(np.min(v));hi.append(np.max(v))
fig,ax=figure(width_mm=92,height_mm=52)
ax.fill_between(Ms,lo,hi,facecolor=GREEN_FILL,edgecolor='none',zorder=1)
ax.plot(Ms,mean,'-o',color=GREEN,lw=1.4,ms=3.2,zorder=3)
ax.set_xscale('log',base=2);ax.set_yscale('log',base=2);ax.set_xticks(Ms);ax.set_xticklabels([str(m) for m in Ms]);ax.minorticks_off()
ax.set_xlabel('$m=n$',labelpad=1);ax.set_ylabel('换基次数',labelpad=1)
save(fig,Path(__file__).resolve().parent,'figure',{'model':'A,c~U(0,1), b=1, m=n','seeds':30,'mean':mean,'min':[int(v) for v in lo],'max':[int(v) for v in hi],})
print(mean,lo,hi)
