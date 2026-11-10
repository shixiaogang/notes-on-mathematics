from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Two curves u,v in the tube and their images Tu,Tv for x'=x^2, delta=1/8.
fig,axes=figure(width_mm=112,height_mm=50,ncols=2,sharey=True)
panel(fig,.075,.985,.965,.25,.08)
t=np.linspace(-.125,.125,4001); dt=t[1]-t[0]; i0=2000
u=1+.75*np.sin(70*t+.3); v=1+.15*np.cos(50*t)-.45*t/.125
def T(w):
    g=w**2; C=np.concatenate(([0],np.cumsum((g[1:]+g[:-1])/2*dt)));  return 1+C-C[i0]
Tu,Tv=T(u),T(v)
d0=np.max(abs(u-v)); d1=np.max(abs(Tu-Tv))
for ax in axes:
    ax.add_patch(Rectangle((-.125,0),.25,2,fc=BLUE_FILL,ec=BLUE,lw=.95,zorder=1)); ax.set_xlim(-.135,.135); ax.set_ylim(-.1,2.1); ax.set_xticks([-.125,0,.125]); ax.set_xticklabels(['$-1/8$','0','$1/8$']); ax.set_xlabel('$t$',labelpad=1); dot(ax,0,1)
axes[0].plot(t,u,color=YELLOW,lw=1.25,zorder=3); axes[0].plot(t,v,color=PURPLE,lw=1.25,zorder=3)
axes[1].plot(t,Tu,color=YELLOW,lw=1.4,zorder=3); axes[1].plot(t,Tv,color=PURPLE,lw=1.4,zorder=3)
axes[0].set_yticks([0,1,2]); axes[0].set_ylabel('$x$',labelpad=1)
axes[0].text(-.115,1.88,'$u$',color=YELLOW,fontsize=8,ha='left',va='center'); axes[0].text(.097,.46,'$v$',color=PURPLE,fontsize=8,ha='left',va='center')
axes[1].text(.082,1.28,'$\\mathcal{T}u$',color=YELLOW,fontsize=8,ha='left',va='bottom'); axes[1].text(.082,.87,'$\\mathcal{T}v$',color=PURPLE,fontsize=8,ha='left',va='top')
tags(fig,axes)
r=save(fig,HERE,'figure',{'d(u,v)':float(d0),'d(Tu,Tv)':float(d1),'ratio':float(d1/d0)})
print(r['facts'], u.min(),u.max(),v.min(),v.max())
