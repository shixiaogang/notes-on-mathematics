from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Blow-up time as the tail integral of 1/f, and four growth rates with x(0)=1.
fig,axes=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.095,.97,.965,.25,.22)
ax=axes[0]; x=np.linspace(1,6,300); ax.fill_between(x,0,1/x**2,fc=BLUE_FILL,ec='none',zorder=1)
ax.plot(x,1/x**2,color=BLUE,lw=1.5,zorder=3); ax.plot(x,1/x,color=YELLOW,lw=1.5,zorder=3)
ax.text(3.2,.075,'面积 1',color=BLUE,fontsize=7.5,ha='left',va='bottom') if 0 else None
ax.text(2.25,.53,'1/x',color=YELLOW,fontsize=8,ha='left',va='center'); ax.text(1.72,.17,'1/x²',color=BLUE,fontsize=8,ha='left',va='center') if 0 else ax.text(1.05,.13,'$1/x^2$',color=BLUE,fontsize=8,ha='left',va='center')
ax.set_xlim(1,6); ax.set_ylim(0,1.05); ax.set_xticks([1,2,4,6]); ax.set_yticks([0,.5,1]); ax.set_xlabel('状态 x',labelpad=1); ax.set_ylabel('1/f(x)',labelpad=1)
ax=axes[1]; t=np.linspace(0,2.6,500)
ax.plot(t,np.exp(t),color=BLUE,lw=1.5)
y=2.0**np.exp(t)-1; m=y<16; ax.plot(t[m],y[m],color=PURPLE,lw=1.5)
tt=np.linspace(0,.99,400); y=1/(1-tt); m=y<16; ax.plot(tt[m],y[m],color=RED,lw=1.5)
ax.axvline(1,color=MUTED,lw=.85,ls=':'); dot(ax,0,1)
ax.text(.73,12.5,'$p=2$',color=RED,fontsize=7.5,ha='right'); ax.text(2.58,7.3,'$p=1$',color=BLUE,fontsize=7.5,ha='right'); ax.text(1.42,9.6,'双重指数',color=PURPLE,fontsize=7.5,ha='left')
ax.set_xlim(0,2.6); ax.set_ylim(0,16); ax.set_xticks([0,1,2]); ax.set_yticks([0,5,10,15]); ax.set_xlabel('t',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'T':'1/(p-1)','double':'2^(exp t)-1'})
