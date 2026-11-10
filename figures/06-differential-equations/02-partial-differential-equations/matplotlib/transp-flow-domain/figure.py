# Target: v=x^2: characteristics, forward blow-up and region not reached from t=0.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,52,ncols=2)
T=np.linspace(1e-3,1.5,600); xl=(-3,3)
a.fill_between(-1/T,T,1.5,color=RED_FILL,lw=0,where=-1/T>=-3.2)
a.fill_betweenx(T,-3,-1/T,color=RED_FILL,lw=0)
a.plot(-1/T,T,color=CHAR,lw=1.5)
for x0 in [-3,-2,-1.3,-.8,-.4,0,.3,.6,.9,1,1.5,2.5]:
    tt=np.linspace(0,1.5,800); tt=tt[1-tt*x0>1e-3]; y=x0/(1-tt*x0); mask=np.abs(y)<=3.05
    a.plot(y[mask],tt[mask],color=BLUE if x0==1 else CHAR,lw=1.4 if x0==1 else .8)
a.plot(xl,[0,0],color=RED,lw=3,clip_on=False)
a.axhline(1,color=MUTED,lw=.85,ls=(0,(3,2)),xmin=0,xmax=1)
a.text(-2.85,1.2,'$x\\leq -1/t$',fontsize=7.5,va='bottom')
a.set_xlim(*xl); a.set_ylim(0,1.5); tail(a,'$x$','(a)','$t$')
xs=np.linspace(-4,.86,600)
b.plot(xs,xs/(1-xs),color=BLUE,lw=1.4)
b.axvline(1,color=RED,lw=1.1,ls=(0,(3,2))); b.axhline(-1,color=CHAR,lw=1.1,ls=(0,(3,2)))
b.set_xlim(-4,2); b.set_ylim(-2,6); tail(b,'$x$','(b)','$\\varphi_{1}(x)$')
b.text(1.12,4.6,'$x=1$',color=RED,fontsize=7.5); b.text(-3.9,-1.65,'$y=-1$',color=CHAR,fontsize=7.5)
save(fig,Path(__file__).resolve().parent,'figure',{'flow':'x/(1-t x)'})
