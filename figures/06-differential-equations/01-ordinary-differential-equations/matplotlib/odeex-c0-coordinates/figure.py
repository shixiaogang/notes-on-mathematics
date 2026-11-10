from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# c0 example: x_n'=2sqrt(x_n)+1/(n+1), x_n(0)=0. Coordinates stay above t^2.
fig,axes=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.08,.985,.965,.25,.24)
def sol(n,T,steps=4000):
    # integrate s=sqrt(x): s'=1+1/(2(n+1)s) is singular; use x with a tiny-step start
    f=lambda t,x:2*np.sqrt(max(x,0))+1/(n+1)
    return rk4(f,0.,0.,T,steps)
ax=axes[0]; ns=np.arange(1,41); t0=.5; vals=[sol(int(n),t0)[1][-1] for n in ns]
ax.plot(ns,vals,'o',ms=2.8,color=BLUE,mew=0)
ax.plot(ns,1/(ns+1),'o',ms=2.8,color=YELLOW,mew=0); ax.axhline(t0**2,color=RED,lw=1.4)
ax.text(40,.215,'$t^2=1/4$',color=RED,fontsize=7.5,ha='right',va='top'); ax.text(12,.115,'$1/(n+1)$',color=YELLOW,fontsize=7.5,ha='left',va='bottom'); ax.text(9,.42,'$x_n(1/2)$',color=BLUE,fontsize=7.5,ha='left',va='bottom')
ax.set_xlim(0,41); ax.set_ylim(0,.72); ax.set_xticks([1,10,20,30,40]); ax.set_yticks([0,.25,.5]); ax.set_xlabel('坐标序号 n',labelpad=1)
ax=axes[1]
ends={}
for n,c,ls in ((1,BLUE,'-'),(9,BLUE,(0,(4,2))),(99,BLUE,(0,(1.5,1.5)))):
    t,x=sol(n,1.); ax.plot(t,x,color=c,lw=1.3,ls=ls); ends[n]=float(x[-1])
    ax.text(1.01,x[-1],f'$n={n}$',fontsize=7.5,va='center')
t=np.linspace(0,1,100); ax.plot(t,t**2,color=RED,lw=1.4); ax.text(.72,.33,'$t^2$',color=RED,fontsize=7.5,ha='left',va='top')
dot(ax,0,0); ax.set_xlim(0,1.16); ax.set_ylim(0,1.6); ax.set_xticks([0,.5,1]); ax.set_yticks([0,.5,1,1.5]); ax.set_xlabel('$t$',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'x_n(1/2)':[float(v) for v in vals[:5]],'x_n(1)':ends})
