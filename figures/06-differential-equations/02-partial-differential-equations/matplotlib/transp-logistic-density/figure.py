# Target: uniform density on (0,1) under logistic velocity: density and cumulative mass; particle check.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,52,ncols=2)
rho=lambda y,t:np.exp(-t)/(1-y+y*np.exp(-t))**2
F=lambda y,t:y*np.exp(-t)/(1-y+y*np.exp(-t))
phi=lambda x,t:x*np.exp(t)/(1-x+x*np.exp(t))
y=np.linspace(0,1,500); ts=[np.log(2),np.log(4)]; cs=shades(2)
rng=np.random.default_rng(10); P=rng.uniform(0,1,40000)
H,e=np.histogram(phi(P,ts[1]),bins=25,range=(0,1),density=True)
a.bar(e[:-1],H,width=e[1]-e[0],align='edge',color=GREEN_FILL,ec=GREEN,lw=.5)
a.plot([0,1],[1,1],color=RED,lw=1.4)
for t,c in zip(ts,cs): a.plot(y,rho(y,t),color=c,lw=1.4)
a.plot([.5],[8/9],'o',color=BLUE,ms=4)
a.text(.05,1.1,'$t=0$',color=RED,fontsize=7.5); a.text(.06,.66,'$\\ln 2$',color=cs[0],fontsize=7.5); a.text(.72,2.2,'$\\ln 4$',color=cs[1],fontsize=7.5,ha='right')
a.set_xlim(0,1); a.set_ylim(0,4.2); tail(a,'$x$','(a)','$\\rho$')
b.plot(y,y,color=RED,lw=1.4)
for t,c in zip(ts,cs): b.plot(y,F(y,t),color=c,lw=1.4)
b.plot([.5,.5],[0,1/3],color=MUTED,lw=.85,ls=(0,(3,2))); b.plot([.5],[1/3],'o',color=BLUE,ms=4); b.text(.53,.275,'$1/3$',fontsize=7.5)
b.set_xlim(0,1); b.set_ylim(0,1); tail(b,'$y$','(b)','$\\int_0^y\\rho\\,\\mathrm{d}x$')
print(np.trapezoid(rho(y,ts[0]),y),np.trapezoid(rho(y,ts[1]),y))
save(fig,Path(__file__).resolve().parent,'figure',{'rho':'e^-t/(1-y+y e^-t)^2','seed':10})
