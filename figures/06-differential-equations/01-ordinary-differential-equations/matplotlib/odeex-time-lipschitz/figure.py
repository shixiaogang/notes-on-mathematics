from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# f(t,x)=2 clip(x,0,t^2)/t: Lipschitz in x with constant 2/t, solutions c t^2.
fig,axes=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.075,.965,.965,.25,.22)
ax=axes[0]; t=np.linspace(0,1,200)
ax.fill_between(t,0,t**2,fc=BLUE_FILL,ec='none',zorder=0)
for c,col in ((0,BLUE),(1,BLUE),(.25,YELLOW),(.5,YELLOW),(.75,YELLOW)):
    ax.plot(t,c*t**2,color=col,lw=1.45,zorder=3)
    ax.text(1.015,c,f'$c={c:g}$',fontsize=7.5,va='center')
dot(ax,0,0); ax.set_xlim(0,1.2); ax.set_ylim(-.05,1.1); ax.set_xticks([0,.5,1]); ax.set_yticks([0,.5,1]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
ax=axes[1]; t=np.linspace(.02,1,400); ax.plot(t,2/t,color=RED,lw=1.5); ax.set_xlim(0,1); ax.set_ylim(0,20); ax.set_xticks([0,.5,1]); ax.set_yticks([0,10,20]); ax.set_xlabel('$t$',labelpad=1)
ax.text(.2,14,'Lipschitz常数 2/t',color=RED,fontsize=7.5,ha='left',va='center')
tags(fig,axes)
save(fig,HERE,'figure',{'solutions':'c t^2, c in [0,1]'})
