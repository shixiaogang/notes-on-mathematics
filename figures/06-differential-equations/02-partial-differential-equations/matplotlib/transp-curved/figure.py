# Target: transport by v=x of a tent centred at 1: characteristics x=x0 e^t and profiles.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,52,ncols=2)
L=np.log(2)
x=np.linspace(0,5,1001); t=np.linspace(0,1.2,401); X,T=np.meshgrid(x,t)
heat(a,tent(X*np.exp(-T)),(0,5),(0,1.2))
for x0 in np.arange(.25,5,.25):
    tt=np.linspace(0,1.2,200); a.plot(x0*np.exp(tt),tt,color=CHAR,lw=.7)
a.plot([0,5],[0,0],color=RED,lw=3,clip_on=False)
tt=np.linspace(0,L,100); a.plot(1.5*np.exp(tt),tt,color=INK,lw=1.7)
a.plot([3],[L],'o',color=BLUE,ms=4.5,mec='white',mew=.4); a.plot([1.5],[0],'o',color=RED,ms=4.5,clip_on=False,mec='white',mew=.4)
B=dict(fc='white',ec='none',pad=.8)
a.text(3.14,L+.03,'$(3,\\ln 2)$',fontsize=7.5,bbox=B); a.text(1.62,.04,'$(1.5,0)$',fontsize=7.5,bbox=B)
a.set_xlim(0,5); a.set_ylim(0,1.2); tail(a,'$x$','(a)','$t$')
xx=np.linspace(0,4.6,1201)
cs=shades(2)
b.plot(xx,tent(xx),color=RED,lw=1.4)
b.plot(xx,tent(xx*np.exp(-L/2)),color=cs[0],lw=1.4)
b.plot(xx,tent(xx*np.exp(-L)),color=cs[1],lw=1.4)
b.plot([1.5,3],[.5,.5],color=MUTED,lw=.85,ls=(0,(3,2)))
b.plot([1.5],[.5],'o',color=RED,ms=4); b.plot([3],[.5],'o',color=BLUE,ms=4)
b.text(.45,1.04,'$t=0$',color=RED,fontsize=7.5); b.text(1.25,1.04,'$t=\\frac{1}{2}\\ln 2$',color=cs[0],fontsize=7.5); b.text(2.6,1.04,'$t=\\ln 2$',color=cs[1],fontsize=7.5)
b.set_xlim(0,4.6); b.set_ylim(0,1.25); tail(b,'$x$','(b)','$u$')
save(fig,Path(__file__).resolve().parent,'figure',{'flow':'x e^t','check':'u(3,ln2)=u0(1.5)=0.5'})
