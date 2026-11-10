# Target: logistic velocity: spacing of evenly seeded characteristics equals inverse density; Jacobian at t=ln 2.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,54,ncols=2)
phi=lambda x,t:x*np.exp(t)/(1-x+x*np.exp(t))
t=np.linspace(0,3,400)
for x0 in np.arange(.05,1,.05): a.plot(phi(x0,t),t,color=CHAR,lw=.8)
a.plot([0,0],[0,3],color=CHAR,lw=1.5,clip_on=False); a.plot([1,1],[0,3],color=CHAR,lw=1.5,clip_on=False)
a.plot([0,1],[0,0],color=RED,lw=3,clip_on=False)
a.axhline(np.log(2),color=MUTED,lw=.85,ls=(0,(3,2)))
a.set_xlim(0,1); a.set_ylim(0,3); a.set_yticks([0,np.log(2),1,2,3],['$0$','$\\ln 2$','$1$','$2$','$3$']); tail(a,'$x$','(a)','$t$')
L=np.log(2); x=np.linspace(0,1,300)
b.plot(x,2/(1+x)**2,color=BLUE,lw=1.4); b.axhline(1,color=MUTED,lw=.85,ls=(0,(3,2)))
pts=np.linspace(.05,.95,10); h=1e-5; fd=(phi(pts+h,L)-phi(pts-h,L))/(2*h)
b.plot(pts,fd,'o',color=GREEN,ms=3.5)
b.plot([1/3],[9/8],'o',color=RED,ms=4.5); b.text(.37,1.2,'$(1/3,\\,9/8)$',fontsize=7.5)
b.set_xlim(0,1); b.set_ylim(.4,2.1); tail(b,'$x_0$','(b)','$J_{0,\\ln 2}$')
print(max(abs(fd-2/(1+pts)**2)))
save(fig,Path(__file__).resolve().parent,'figure',{'J':'2/(1+x)^2 at t=ln 2'})
