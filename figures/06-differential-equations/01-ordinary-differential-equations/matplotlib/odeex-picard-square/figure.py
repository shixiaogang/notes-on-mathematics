from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Picard iterates of x'=x^2,x(0)=1 with exact polynomial integration.
from numpy.polynomial import polynomial as P
fig,axes=figure(width_mm=112,height_mm=52,ncols=2,gridspec_kw={'width_ratios':[1.25,1]})
panel(fig,.07,.985,.965,.26,.23)
ps=[np.array([1.])]
for k in range(6):
    q=P.polyint(P.polymul(ps[-1],ps[-1])); q[0]=1.; ps.append(q)
ax=axes[0]; d=.125
ax.axvspan(-d,d,fc=BLUE_FILL,ec='none',zorder=0)
for k,p in enumerate(ps[:5]):
    t=np.linspace(-.2,.72,400); y=P.polyval(t,p); ax.plot(t,y,color=GREEN,lw=1.1,zorder=3)
    tt=.72; ax.text(.725,min(P.polyval(tt,p),3.9),f'$k={k}$',fontsize=7.5,va='center') if P.polyval(tt,p)<3.8 else None
t=np.linspace(-.2,.72,300); ax.plot(t,1/(1-t),color=BLUE,lw=1.6,zorder=4); dot(ax,0,1)
ax.text(.595,3.45,'$1/(1-t)$',color=BLUE,fontsize=7.5,ha='right',va='center')
ax.set_xlim(-.2,.84); ax.set_ylim(.7,4); ax.set_xticks([-.125,0,.125,.5]); ax.set_xticklabels(['$-1/8$','0','$1/8$','1/2']); ax.set_yticks([1,2,3,4]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
ax=axes[1]; t=np.linspace(-d,d,4001); ex=1/(1-t); errs=[float(np.max(abs(P.polyval(t,p)-ex))) for p in ps]
ks=np.arange(len(ps)); bound=[2*.5**k*d for k in ks]
ax.semilogy(ks,bound,color=PURPLE,lw=1.,ls=(0,(3,2)),marker='o',ms=2.6,mew=0); ax.semilogy(ks,errs,color=GREEN,lw=1.3,marker='o',ms=3,mew=0)
ax.text(2.5,.19,'先验界',color=PURPLE,fontsize=7.5,ha='left',va='center'); ax.text(2.55,5e-3,'一致误差',color=GREEN,fontsize=7.5,ha='left',va='center')
ax.set_xticks(ks); ax.set_xlabel('迭代次数 k',labelpad=1); ax.minorticks_off(); ax.set_yticks([1,1e-2,1e-4,1e-6]); ax.set_yticklabels(['$1$','$10^{-2}$','$10^{-4}$','$10^{-6}$'])
tags(fig,axes)
r=save(fig,HERE,'figure',{'errors':errs,'bound':bound,'x3':[float(c) for c in ps[3]]})
print(r['facts'])
