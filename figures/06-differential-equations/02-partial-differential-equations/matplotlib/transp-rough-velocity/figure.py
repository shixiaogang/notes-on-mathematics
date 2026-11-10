# Target: discontinuous velocities: merging, gap, and non-unique signed weak solution with zero data.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b,c)=figure(112,52,ncols=3)
xl=(-1.5,1.5); tl=(0,1.3)
for x0 in np.arange(-1.4,1.5,.2):
    if abs(x0)<1e-9: continue
    s=np.sign(x0); r=abs(x0)
    a.plot([x0,x0-s*min(r,1.3)],[0,min(r,1.3)],color=CHAR,lw=.8)
a.plot([0,0],[0,1.3],color=RED,lw=2.8)
a.plot(xl,[0,0],color=RED,lw=2.8,clip_on=False)
for x0 in np.arange(-1.4,1.5,.2):
    if abs(x0)<1e-9: continue
    b.plot([x0,x0+np.sign(x0)*1.3],[0,1.3],color=CHAR,lw=.8)
b.fill([0,1.3,-1.3],[0,1.3,1.3],color=RED_FILL,lw=0)
b.plot(xl,[0,0],color=RED,lw=2.8,clip_on=False); b.plot([-1.3,0,1.3],[1.3,0,1.3],color=CHAR,lw=1.5)
x=np.linspace(-1.5,1.5,1201); t=np.linspace(0,1.3,801); X,T=np.meshgrid(x,t)
Z=np.where((X>0)&(X<T),T-X,0.0)+np.where((X<0)&(X>-T),-(T+X),0.0)
heat(c,Z,xl,tl,vmin=-1.3,vmax=1.3,cmap=DIV)
c.plot([-1.3,0,1.3],[1.3,0,1.3],color=CHAR,lw=1.1)
c.plot([0,0],[0,1.3],color=CHAR,lw=1.1,ls=(0,(3,2)))
for A,tag in ((a,'(a)'),(b,'(b)'),(c,'(c)')):
    A.set_xlim(*xl); A.set_ylim(*tl); A.set_xticks([-1,0,1]); tail(A,'$x$',tag,'$t$' if tag=='(a)' else None)
save(fig,Path(__file__).resolve().parent,'figure',{'c':'rho=t-x on 0<x<t, rho=-(t+x) on -t<x<0, v=sgn x, rho0=0'})
