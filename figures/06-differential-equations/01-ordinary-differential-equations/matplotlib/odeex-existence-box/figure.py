from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# xdot=x^2, x(0)=1 in the box |t|<=a, |x-1|<=b; M=(1+b)^2, delta=min(a,b/M).
fig,axes=figure(width_mm=112,height_mm=56,ncols=2,sharey=True)
panel(fig,.1,.985,.965,.235,.1)
for ax,(a,b) in zip(axes,((.5,1.),(.15,1.))):
    M=(1+b)**2; d=min(a,b/M)
    ax.add_patch(Rectangle((-a,1-b),2*a,2*b,fc=BLUE_FILL,ec=BLUE,lw=.95,zorder=1))
    t=np.linspace(-.62,.62,5)
    ax.plot(t,1+M*t,color=PURPLE,lw=.95,ls=(0,(3,2)),zorder=2); ax.plot(t,1-M*t,color=PURPLE,lw=.95,ls=(0,(3,2)),zorder=2)
    t=np.linspace(-.62,.62,300); ax.plot(t,1/(1-t),color=BLUE,lw=.85,ls=(0,(1.5,1.5)),zorder=3)
    t=np.linspace(-d,d,100); ax.plot(t,1/(1-t),color=BLUE,lw=1.8,zorder=4)
    for s in (-d,d): ax.vlines(s,-.22,2.5,color=STROKE,lw=.85,ls=':',zorder=2)
    dot(ax,0,1)
    ax.set_xlim(-.62,.62); ax.set_ylim(-.22,2.5); ax.set_xticks([-a,-d,0,d,a] if a!=d else [-a,0,a])
    ax.set_xlabel('$t$',labelpad=1)
axes[0].set_xticklabels(['$-a$','$-\\delta$','0','$\\delta$','$a$'])
axes[1].set_xticks([-.15,0,.15]); axes[1].set_xticklabels(['$-a=-\\delta$','0','$a=\\delta$'])
axes[0].set_yticks([0,1,2]); axes[0].set_yticklabels(['$x_0-b$','$x_0$','$x_0+b$']); axes[0].set_ylabel('$x$',labelpad=0)
axes[0].text(0,2.3,'斜率 M',color=PURPLE,fontsize=7.5,ha='center',va='center')
tags(fig,axes)
save(fig,HERE,'figure',{'ode':'x\'=x^2,x(0)=1','boxes':'a=.5,b=1 and a=.15,b=1','M':4})
