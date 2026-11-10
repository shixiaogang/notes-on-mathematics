from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Switched input and an integrable singular input.
fig,axes=figure(width_mm=112,height_mm=48,ncols=3)
panel(fig,.075,.975,.965,.26,.3)
ax=axes[0]; ax.plot([0,1],[1,1],color=PURPLE,lw=1.5); ax.plot([1,3],[0,0],color=PURPLE,lw=1.5); ax.plot([1],[1],'o',ms=3.6,mfc='white',mec=PURPLE,mew=.9); ax.plot([1],[0],'o',ms=3.6,color=PURPLE,mew=0)
ax.set_xlim(0,3); ax.set_ylim(-.1,1.25); ax.set_xticks([0,1,2,3]); ax.set_yticks([0,1]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('g(t)',labelpad=1)
ax=axes[1]; t=np.linspace(0,3,500); x=np.where(t<=1,1-np.exp(-t),(1-np.exp(-1))*np.exp(-(t-1))); ax.plot(t,x,color=BLUE,lw=1.5,zorder=3)
x1=1-np.exp(-1); s=np.linspace(-.42,.42,3); ax.plot(1+s,x1+np.exp(-1)*s,color=PURPLE,lw=.95,ls=(0,(3,2))); ax.plot(1+s,x1-x1*s,color=PURPLE,lw=.95,ls=(0,(3,2)))
dot(ax,0,0); dot(ax,1,x1,ms=3.8)
ax.set_xlim(0,3); ax.set_ylim(-.05,.9); ax.set_xticks([0,1,2,3]); ax.set_yticks([0,.5]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('x(t)',labelpad=1)
ax=axes[2]; t=np.linspace(.01,1,400); ax.plot(t,1/np.sqrt(t),color=PURPLE,lw=1.5); ax.plot(t,2*np.sqrt(t),color=BLUE,lw=1.5); ax.plot([0,.01],[0,.2],color=BLUE,lw=1.5); dot(ax,0,0)
ax.text(.2,3.5,'$t^{-1/2}$',color=PURPLE,fontsize=7.5,ha='left'); ax.text(.5,1.95,'$2\\sqrt{t}$',color=BLUE,fontsize=7.5,ha='left')
ax.set_xlim(0,1); ax.set_ylim(0,5); ax.set_xticks([0,.5,1]); ax.set_yticks([0,2,4]); ax.set_xlabel('t',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'x(1)':float(x1),'left_slope':float(np.exp(-1)),'right_slope':float(-x1)})
