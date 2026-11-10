# Target: lookup via inverse flow: tent carried by v=x to t=ln 2.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
from matplotlib.patches import ConnectionPatch
fig,(a,b)=figure(100,62,nrows=2,sharex=True)
L=np.log(2); x=np.linspace(0,4.4,1201)
a.plot(x,tent(x),color=RED,lw=1.4); b.plot(x,tent(x/2),color=BLUE,lw=1.4)
for x0 in (.5,1,1.5):
    y=2*x0; h=float(tent(np.array(x0)))
    a.plot([x0],[h],'o',color=RED,ms=4); b.plot([y],[h],'o',color=BLUE,ms=4)
    a.plot([x0,x0],[0,h],color=MUTED,lw=.85,ls=(0,(3,2))); b.plot([y,y],[0,h],color=MUTED,lw=.85,ls=(0,(3,2)))
    fig.add_artist(ConnectionPatch(xyA=(x0,0),xyB=(y,h),coordsA=a.transData,coordsB=b.transData,color=CHAR,lw=.85,arrowstyle='-|>',mutation_scale=7,shrinkA=0,shrinkB=2))
a.set_xlim(0,4.4); a.set_ylim(0,1.2); b.set_ylim(0,1.2)
a.set_ylabel('$u_0$'); b.set_ylabel('$u(\\cdot,\\ln 2)$'); b.set_xlabel('$x$')
save(fig,Path(__file__).resolve().parent,'figure',{'flow':'y=2x0'})
