from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Restarting x'=x^2 from t_k=1-(3/4)^k with b=x_k, delta_k=1/(4 x_k)=(1-t_k)/4.
fig,axes=figure(width_mm=112,height_mm=54,ncols=2,gridspec_kw={'width_ratios':[1.5,1]})
panel(fig,.07,.975,.965,.25,.22)
ax=axes[0]; K=6; tk=[1-.75**k for k in range(K+1)]; xk=[1/(1-s) for s in tk]; dk=[(1-s)/4 for s in tk]
for k in range(K-1,-1,-1):
    ax.add_patch(Rectangle((tk[k],0),dk[k],2*xk[k],fc='none',ec=BLUE,lw=.85,zorder=2))
t=np.linspace(0,.965,400); ax.plot(t,1/(1-t),color=BLUE,lw=1.6,zorder=4)
for k in range(K): dot(ax,tk[k],xk[k],ms=3.8)
ax.axvline(1,color=STROKE,lw=1.1,zorder=1)
ax.set_xlim(0,1.04); ax.set_ylim(0,9.5); ax.set_xticks([0,.25,.5,.75,1]); ax.set_xticklabels(['0','1/4','1/2','3/4','1']); ax.set_yticks([0,4,8]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('x',labelpad=1)
ax=axes[1]; k=np.arange(0,13); ax.bar(k,.25*.75**k,width=.62,color=BLUE_FILL,edgecolor=BLUE,lw=.75)
ax.set_xticks([0,4,8,12]); ax.set_yticks([0,.1,.2]); ax.set_xlabel('重启次数 k',labelpad=1); ax.set_ylabel('窗长',labelpad=1); ax.set_xlim(-.7,12.7)
tags(fig,axes)
save(fig,HERE,'figure',{'t_k':[float(x) for x in tk],'x_k':[float(x) for x in xk],'delta_k':[float(x) for x in dk]})
