from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# x'=sqrt(1+x^2) (global, sinh t) with its linear-growth barrier t e^t; x'=1+x^2 blows up.
fig,ax=figure(width_mm=88,height_mm=50)
panel(fig,.09,.97,.97,.16)
t=np.linspace(0,2.3,300); ax.plot(t,t*np.exp(t),color=PURPLE,lw=1.15,ls=(0,(3,2))); ax.plot(t,np.sinh(t),color=BLUE,lw=1.6)
tt=np.linspace(0,1.53,300); y=np.tan(tt); m=y<12; ax.plot(tt[m],y[m],color=RED,lw=1.5); ax.axvline(np.pi/2,color=MUTED,lw=.85,ls=':')
dot(ax,0,0); ax.set_xlim(0,2.3); ax.set_ylim(0,12); ax.set_xticks([0,.5,1,1.5,2]); ax.set_yticks([0,4,8,12]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('x',labelpad=1)
ax.text(1.62,11,'$\\tan t$',color=RED,fontsize=7.5,ha='left'); ax.text(1.88,9.4,'$t\\mathrm{e}^t$',color=PURPLE,fontsize=7.5,ha='right'); ax.text(2.05,2.1,'$\\sinh t$',color=BLUE,fontsize=7.5,ha='right')
save(fig,HERE,'figure',{'sinh1':float(np.sinh(1)),'bound1':float(np.e)})
