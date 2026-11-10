from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# x'=2 sqrt|x|, x(0)=0: x=0 and x_c=(t-c)^2 for t>=c.
fig,ax=figure(width_mm=92,height_mm=56)
panel(fig,.085,.975,.97,.15)
ax.set_xlim(-.05,2.1); ax.set_ylim(-.5,2.5)
field(ax,lambda t,x:2*np.sqrt(abs(x)),nt=19,nx=13)
ax.plot([0,2.1],[0,0],color=BLUE,lw=1.6,zorder=4)
t=np.linspace(0,2.1,300); ax.plot(t,t**2,color=BLUE,lw=1.6,zorder=4)
for c in (.5,1.,1.5):
    t=np.linspace(c,2.1,200); ax.plot(t,(t-c)**2,color=YELLOW,lw=1.4,zorder=3)
    ax.text(c+.02,-.13,f'$c={c:g}$',color=INK,fontsize=7.5,ha='center',va='top')
ax.text(1.48,2.27,'$x=t^2$',color=BLUE,fontsize=7.5,ha='right',va='center')
ax.text(.2,.09,'$x\\equiv0$',color=BLUE,fontsize=7.5,ha='center',va='bottom')
dot(ax,0,0)
ax.set_xticks([0,.5,1,1.5,2]); ax.set_yticks([0,1,2]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
save(fig,HERE,'figure',{'ode':'x\'=2sqrt|x|','c':[.5,1,1.5]})
