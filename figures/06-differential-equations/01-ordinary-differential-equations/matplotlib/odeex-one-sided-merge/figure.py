from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# x'=-2 sgn(x) sqrt|x|: solutions reach 0 in finite time and merge.
fig,ax=figure(width_mm=88,height_mm=50)
panel(fig,.09,.97,.97,.16)
ax.set_xlim(0,2.2); ax.set_ylim(-1.65,1.65)
field(ax,lambda t,x:-2*np.sign(x)*np.sqrt(abs(x)),nt=17,nx=11)
t=np.linspace(0,2.2,800)
for x0 in (1.44,.81,.36,.09,-.16,-.64,-1.21):
    s=np.sqrt(abs(x0)); ax.plot(t,np.sign(x0)*np.clip(s-t,0,None)**2,color=BLUE,lw=1.35,zorder=3); dot(ax,0,x0,ms=3.6)
ax.plot([0,2.2],[0,0],color=BLUE,lw=1.5,zorder=3)
ax.set_xticks([0,1,2]); ax.set_yticks([-1,0,1]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
save(fig,HERE,'figure',{'ode':'x\'=-2sgn(x)sqrt|x|'})
