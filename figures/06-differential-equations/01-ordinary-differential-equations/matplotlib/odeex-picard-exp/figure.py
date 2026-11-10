from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Picard iterates of x'=x,x(0)=1 on [0,1]: partial sums of e^t.
from math import factorial
fig,axes=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.075,.985,.965,.25,.24)
t=np.linspace(0,1,300); ax=axes[0]
S=np.zeros_like(t); err=[]
for k in range(0,5):
    S=S+t**k/factorial(k)
    ax.plot(t,S,color=GREEN,lw=1.15,zorder=3); ax.text(1.012,S[-1]+{3:-.09,4:.1}.get(k,0),f'$k={k}$',fontsize=7.5,va='center')
ax.plot(t,np.exp(t),color=BLUE,lw=1.6,zorder=4); dot(ax,0,1)
ax.text(.72,2.28,'$\\mathrm{e}^t$',color=BLUE,fontsize=8,ha='right',va='center')
ax.set_xlim(0,1.18); ax.set_ylim(.9,2.9); ax.set_xticks([0,.5,1]); ax.set_yticks([1,2]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
ax=axes[1]; ks=np.arange(0,11); errs=[]
for k in ks:
    errs.append(np.e-sum(1/factorial(j) for j in range(k+1)))
bound=[np.e/factorial(k+1) for k in ks]
ax.semilogy(ks,bound,color=PURPLE,lw=1.,ls=(0,(3,2)),marker='o',ms=2.6,mew=0)
ax.semilogy(ks,errs,color=GREEN,lw=1.3,marker='o',ms=3,mew=0)
ax.semilogy(ks,[1.0]*len(ks),alpha=0)
ax.text(5.2,2e-2,'$\\mathrm{e}/(k+1)!$',color=PURPLE,fontsize=7.5,ha='left',va='center'); ax.text(3,3e-4,'一致误差',color=GREEN,fontsize=7.5,ha='left',va='center')
ax.set_xlim(0,10.3); ax.set_xticks([0,5,10]); ax.set_xlabel('迭代次数 k',labelpad=1); ax.minorticks_off(); ax.set_yticks([1,1e-3,1e-6]); ax.set_yticklabels(['$1$','$10^{-3}$','$10^{-6}$'])
tags(fig,axes)
save(fig,HERE,'figure',{'errors':[float(e) for e in errs[:6]]})
