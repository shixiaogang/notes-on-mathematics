# Target: step data: test function across the discontinuity, mollified data, and weak residual vs front speed.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b,c)=figure(112,52,ncols=3)
def bump(r):
    out=np.zeros_like(r); m=np.abs(r)<1; out[m]=np.exp(1-1/(1-r[m]**2)); return out
psi=lambda x,t:bump((x-1)/1.5)*bump((t-1)/.95)
xl=(-1,3); tl=(0,2.2); x=np.linspace(*xl,601); t=np.linspace(*tl,601); X,T=np.meshgrid(x,t)
a.fill_between([xl[0],2.2],[0,2.2],[2.2,2.2],color='white',lw=0)
a.fill_between([-1,0,2.2],[0,0,2.2],2.2,color=BLUE_FILL,lw=0)
a.contour(X,T,psi(X,T),levels=[.1,.4,.8],colors=PURPLE,linewidths=.85)
a.plot([0,2.2],[0,2.2],color=CHAR,lw=1.7); a.plot([-1,0],[0,0],color=RED,lw=2.8,clip_on=False)
a.text(.05,1.55,'$u=1$',fontsize=7.5); a.text(2.0,.45,'$u=0$',fontsize=7.5)
a.set_xlim(*xl); a.set_ylim(*tl); tail(a,'$x$','(a)','$t$')
xx=np.linspace(-1,3,1201); cs=shades(3)
for e,col in zip((.5,.2,.06),cs):
    b.plot(xx,.5*(1-np.tanh((xx-1)/e*2)),color=col,lw=1.4)
b.plot([-1,1,1,3],[1,1,0,0],color=CHAR,lw=1.1,ls=(0,(3,2)))
b.set_xlim(-1,3); b.set_ylim(0,1.1); tail(b,'$x$','(b)','$u(x,1)$')
# Weak residual for u=1_{x<st}: numerical quadrature with analytic-free finite differences of psi
xq=np.linspace(-2,4,2401); tq=np.linspace(0,3,1601); Xq,Tq=np.meshgrid(xq,tq); dx=xq[1]-xq[0]; dt=tq[1]-tq[0]
P=psi(Xq,Tq); Pt=np.gradient(P,dt,axis=0); Px=np.gradient(P,dx,axis=1)
def res(s):
    U=(Xq<s*Tq).astype(float)
    return (U*(Pt+Px)).sum()*dx*dt+(np.where(xq<0,1.0,0)*P[0]).sum()*dx
ss=np.linspace(.2,1.8,9); R=[res(s) for s in ss]
fine=np.linspace(.2,1.8,200); tt=np.linspace(0,3,4001)
L=[(1-s)*np.trapezoid(psi(s*tt,tt),tt) for s in fine]
c.plot(fine,L,color=BLUE,lw=1.4); c.plot(ss,R,'o',color=GREEN,ms=3.5)
c.axhline(0,color=MUTED,lw=.85); c.plot([1],[0],'o',color=RED,ms=4.5)
c.set_xlim(.2,1.8); tail(c,'$s$','(c)','$R(s)$')
print('res',R)
save(fig,Path(__file__).resolve().parent,'figure',{'residual':'R(s)=(1-s) int psi(st,t) dt'})
