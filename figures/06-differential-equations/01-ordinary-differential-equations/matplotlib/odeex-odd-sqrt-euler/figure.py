from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# x'=2 sgn(x) sqrt|x|; Euler polygons from x0=(-1)^N/N^2 on [0,1].
fig,ax=figure(width_mm=88,height_mm=52)
panel(fig,.1,.97,.97,.16)
f=lambda x:2*np.sign(x)*np.sqrt(abs(x))
d=1.
last={}
for N,ls in ((20,(0,(4,2))),(21,(0,(4,2))),(80,'-'),(81,'-')):
    h=d/N; x=[(-1)**N/N**2]
    for k in range(N): x.append(x[-1]+h*f(x[-1]))
    t=np.arange(N+1)*h; ax.plot(t,x,color=GREEN,lw=1.15,ls=ls,zorder=4); last[N]=x[-1]
t=np.linspace(0,1,100)
ax.plot(t,t**2,color=BLUE,lw=1.5,zorder=3); ax.plot(t,-t**2,color=BLUE,lw=1.5,zorder=3); ax.plot(t,0*t,color=BLUE,lw=1.5,zorder=3)
dot(ax,0,0)
ax.text(1.,1.03,'$x=t^2$',color=BLUE,fontsize=7.5,ha='right',va='bottom'); ax.text(1.,-1.03,'$x=-t^2$',color=BLUE,fontsize=7.5,ha='right',va='top'); ax.text(1.,.05,'$x\\equiv0$',color=BLUE,fontsize=7.5,ha='right',va='bottom')
ax.text(.53,.60,'N为偶数',color=GREEN,fontsize=7.5,ha='right'); ax.text(.53,-.66,'N为奇数',color=GREEN,fontsize=7.5,ha='right')
ax.set_xlim(0,1.02); ax.set_ylim(-1.25,1.25); ax.set_xticks([0,.5,1]); ax.set_yticks([-1,0,1]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
save(fig,HERE,'figure',{'x_end':last})
