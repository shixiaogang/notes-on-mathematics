# Target: same flow v=x, tent centred at 1, t=ln 2: transported value vs conserved density; quantities along x0=1.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b,c)=figure(112,52,ncols=3)
L=np.log(2); x=np.linspace(0,4.4,1201)
a.fill_between(x,0,tent(x/2),color=BLUE_FILL,lw=0); a.plot(x,tent(x),color=RED,lw=1.4); a.plot(x,tent(x/2),color=BLUE,lw=1.4)
a.plot([3],[.5],'o',color=BLUE,ms=4); a.plot([1.5],[.5],'o',color=RED,ms=4)
a.set_xlim(0,4.4); a.set_ylim(0,1.15); a.set_xticks([0,2,4]); tail(a,'$x$','(a)','$u$')
b.fill_between(x,0,.5*tent(x/2),color=BLUE_FILL,lw=0); b.plot(x,tent(x),color=RED,lw=1.4); b.plot(x,.5*tent(x/2),color=BLUE,lw=1.4)
b.plot([3],[.25],'o',color=BLUE,ms=4); b.plot([1.5],[.5],'o',color=RED,ms=4)
b.set_xlim(0,4.4); b.set_ylim(0,1.15); b.set_xticks([0,2,4]); tail(b,'$x$','(b)','$\\rho$')
t=np.linspace(0,1.1,200)
c.plot(t,1+0*t,color=BLUE,lw=1.4); c.plot(t,np.exp(-t),color=YELLOW,lw=1.7); c.plot(t,np.exp(t),color=PURPLE,lw=1.4); c.plot(t,1+0*t,color=CHAR,lw=1.1,ls=(0,(3,3)))
c.text(.84,2.72,'$J$',color=PURPLE,ha='right'); c.text(1.08,.42,'$\\rho$',color=YELLOW,ha='right'); c.text(.5,1.1,'$u=\\rho J$',ha='center',fontsize=7.5)
c.set_xlim(0,1.1); c.set_ylim(0,3.1); c.set_xticks([0,L,1],['$0$','$\\ln 2$','$1$']); tail(c,'$t$','(c)')
save(fig,Path(__file__).resolve().parent,'figure',{'u':'u0(x e^-t)','rho':'e^-t u0(x e^-t)','area':'2 vs 1'})
