# Target: solution of the boundary-initial transport problem on (0,1), v=1/2, compatible and incompatible data.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b,c)=figure(112,50,ncols=3)
x=np.linspace(0,1,401); t=np.linspace(0,2,401); X,T=np.meshgrid(x,t)
u01=lambda s:.5*(1+np.cos(2*np.pi*s)); g1=lambda s:np.cos(np.pi*s/2)**2
def sol(u0,g,X,T):
    return np.where(X>=T/2,u0(np.maximum(X-T/2,0)),g(np.maximum(T-2*X,0)))
U1=sol(u01,g1,X,T); U2=sol(lambda s:0*s,lambda s:1+0*s,X,T)
for A,U in ((a,U1),(b,U2)):
    heat(A,U,(0,1),(0,2))
    for x0 in np.arange(.2,1,.2): A.plot([x0,1],[0,2*(1-x0)],color=CHAR,lw=.8)
    for t0 in np.arange(.4,2,.4): A.plot([0,min(1,(2-t0)/2)],[t0,min(t0+2,2)],color=CHAR,lw=.8)
    A.plot([0,1],[0,2],color=CHAR,lw=1.6)
    A.plot([0,1],[0,0],color=RED,lw=2.6,clip_on=False); A.plot([0,0],[0,2],color=RED,lw=2.6,clip_on=False)
    A.set_xlim(0,1); A.set_ylim(0,2); A.set_xticks([0,.5,1])
tail(a,'$x$','(a)','$t$'); tail(b,'$x$','(b)')
xx=np.linspace(0,1,801)
c.plot(xx,sol(u01,g1,xx,1+0*xx),color=BLUE,lw=1.4)
c.plot(xx,sol(lambda s:0*s,lambda s:1+0*s,xx,1+0*xx),color=YELLOW,lw=1.7)
c.axvline(.5,color=CHAR,lw=.85,ls=(0,(3,2)))
c.set_xlim(0,1); c.set_ylim(0,1.12); c.set_xticks([0,.5,1]); tail(c,'$x$','(c)','$u(x,1)$')
save(fig,Path(__file__).resolve().parent,'figure',{'v':.5,'a':'u0=.5(1+cos 2pi x), g=cos^2(pi t/2)','b':'u0=0,g=1'})
