from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Three ways a maximal solution ends at omega=1.
fig,axes=figure(width_mm=112,height_mm=50,ncols=3)
panel(fig,.06,.98,.965,.25,.22)
ax=axes[0]; t=np.linspace(-.3,.93,400); ax.plot(t,1/(1-t),color=RED,lw=1.5); ax.plot(t[t<.72],1/(1-t[t<.72]),color=BLUE,lw=1.5); ax.axvline(1,color=MUTED,lw=.85,ls=(0,(2,2))); dot(ax,0,1,color=INK,ms=0)
dot(ax,0,1); ax.set_xlim(-.3,1.1); ax.set_ylim(0,14); ax.set_xticks([0,1]); ax.set_yticks([0,5,10]); ax.set_xlabel('t',labelpad=1)
ax=axes[1]; t=np.linspace(-.3,1,600); ax.plot(t,np.sqrt(1-t),color=BLUE,lw=1.5); ax.axhline(0,color=STROKE,lw=1.8,zorder=2); ax.axvline(1,color=MUTED,lw=.85,ls=(0,(2,2))); dot(ax,0,1); dot(ax,1,0,color=RED,ms=3.6)
ax.set_xlim(-.3,1.1); ax.set_ylim(-.1,1.25); ax.set_xticks([0,1]); ax.set_yticks([0,1]); ax.set_xlabel('t',labelpad=1)
ax=axes[2]; t=1-np.geomspace(1.3,.004,6000); ax.plot(t,np.sin(1/(1-t)),color=BLUE,lw=.95); ax.axvline(1,color=STROKE,lw=1.8,zorder=2); dot(ax,0,np.sin(1))
ax.set_xlim(-.3,1.1); ax.set_ylim(-1.25,1.25); ax.set_xticks([0,1]); ax.set_yticks([-1,0,1]); ax.set_xlabel('t',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'cases':['1/(1-t)','sqrt(1-t) on x>0','sin(1/(1-t)) on t<1']})
