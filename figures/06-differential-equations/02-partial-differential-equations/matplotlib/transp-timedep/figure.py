# Target: time-dependent velocity: v=cos t (oscillating) and v=x t (accelerating).
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,52,ncols=2)
xl=(-2,3.6); tl=(0,2*np.pi)
x=np.linspace(*xl,801); t=np.linspace(*tl,601); X,T=np.meshgrid(x,t)
heat(a,tent(X-np.sin(T),0),xl,tl)
for x0 in np.arange(-3,3.6,.75):
    tt=np.linspace(*tl,300); a.plot(x0+np.sin(tt),tt,color=CHAR,lw=.75)
a.plot(xl,[0,0],color=RED,lw=3,clip_on=False)
a.set_xlim(*xl); a.set_ylim(*tl); a.set_yticks([0,np.pi,2*np.pi],['$0$','$\\pi$','$2\\pi$']); tail(a,'$x$','(a)','$t$')
xl=(0,6); tl=(0,1.6)
x=np.linspace(*xl,801); t=np.linspace(*tl,601); X,T=np.meshgrid(x,t)
heat(b,tent(X*np.exp(-T**2/2)),xl,tl)
for x0 in np.arange(.25,6,.25):
    tt=np.linspace(*tl,300); b.plot(x0*np.exp(tt**2/2),tt,color=CHAR,lw=.75)
b.plot(xl,[0,0],color=RED,lw=3,clip_on=False)
b.set_xlim(*xl); b.set_ylim(*tl); tail(b,'$x$','(b)','$t$')
save(fig,Path(__file__).resolve().parent,'figure',{'a':'x=x0+sin t','b':'x=x0 exp(t^2/2)'})
