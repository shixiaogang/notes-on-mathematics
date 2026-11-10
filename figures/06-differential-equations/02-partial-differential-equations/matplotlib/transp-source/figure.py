# Target: transport by v=x with source f=x: solution vs source-free at t=ln 2, and accumulation along x0=1.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,52,ncols=2)
L=np.log(2); x=np.linspace(0,4.4,1201)
a.plot(x,tent(x),color=RED,lw=1.4)
a.plot(x,tent(x*np.exp(-L)),color=YELLOW,lw=1.7)
a.plot(x,tent(x*np.exp(-L))+x*(1-np.exp(-L)),color=BLUE,lw=1.4)
a.plot([2],[2],'o',color=BLUE,ms=4); a.plot([2],[1],'o',color=YELLOW,ms=4)
a.plot([2,2],[1,2],color=MUTED,lw=.85,ls=(0,(3,2)))
a.text(2.1,1.42,'$+1$',fontsize=7.5)
a.set_xlim(0,4.4); a.set_ylim(0,3); tail(a,'$x$','(a)','$u(x,\\ln 2)$')
t=np.linspace(0,1,300)
b.fill_between(t,1,np.exp(t),color=BLUE_FILL,lw=0)
b.plot(t,np.exp(t),color=BLUE,lw=1.4); b.axhline(1,color=YELLOW,lw=1.7)
b.plot([0],[1],'o',color=RED,ms=4.5,clip_on=False,zorder=5); b.plot([L],[2],'o',color=BLUE,ms=4.5)
b.axvline(L,color=MUTED,lw=.85,ls=(0,(3,2)))
b.set_xticks([0,L,1],['$0$','$\\ln 2$','$1$']); b.set_xlim(0,1); b.set_ylim(.8,2.8); tail(b,'$t$','(b)','$u(\\mathrm{e}^t,t)$')
save(fig,Path(__file__).resolve().parent,'figure',{'u':'u0(x e^-t)+x(1-e^-t)','check':'u(2,ln2)=2'})
