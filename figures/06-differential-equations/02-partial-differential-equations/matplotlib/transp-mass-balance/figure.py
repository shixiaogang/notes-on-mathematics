# Target: mass balance on (0,1) for inflow/outflow, outflow on both ends, and no-flux velocities.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
configure()
fig=plt.figure(figsize=(112/25.4,88/25.4),layout='constrained')
ax=fig.subplot_mosaic('abc;ddd',height_ratios=[1.25,1])
phi=lambda x,t:x*np.exp(t)/(1-x+x*np.exp(t))
tl=(0,2); x=np.linspace(0,1,401); t=np.linspace(*tl,401); X,T=np.meshgrid(x,t)
a,b,c,d=ax['a'],ax['b'],ax['c'],ax['d']
heat(a,np.where(X>T,1.0,0.0),(0,1),tl,vmax=2)
for x0 in np.arange(0,1,.2): a.plot([x0,1],[0,1-x0],color=CHAR,lw=.8)
for t0 in np.arange(.2,2,.2): a.plot([0,min(1,2-t0)],[t0,min(t0+1,2)],color=CHAR,lw=.8)
a.plot([0,0],[0,2],color=RED,lw=2.6,clip_on=False); a.plot([0,1],[0,0],color=RED,lw=2.6,clip_on=False)
heat(b,np.exp(-T),(0,1),tl,vmax=2)
for x0 in np.arange(.05,1,.1):
    tt=np.linspace(*tl,200); y=.5+(x0-.5)*np.exp(tt); m=(y>=0)&(y<=1); b.plot(y[m],tt[m],color=CHAR,lw=.8)
b.plot([0,1],[0,0],color=RED,lw=2.6,clip_on=False)
R=np.exp(-T)/(1-X+X*np.exp(-T))**2
heat(c,R,(0,1),tl,vmax=2)
for x0 in np.arange(.1,1,.1):
    tt=np.linspace(*tl,200); c.plot(phi(x0,tt),tt,color=CHAR,lw=.8)
c.plot([0,1],[0,0],color=RED,lw=2.6,clip_on=False)
c.plot([0,0],[0,2],color=CHAR,lw=1.6,clip_on=False); c.plot([1,1],[0,2],color=CHAR,lw=1.6,clip_on=False)
for A,tag in ((a,'(a)'),(b,'(b)'),(c,'(c)')):
    A.set_xlim(0,1); A.set_ylim(*tl); A.set_xticks([0,.5,1]); tail(A,'$x$',tag,'$t$' if tag=='(a)' else None)
tt=np.linspace(0,2,400)
# numerical mass by quadrature of the closed-form densities
xq=np.linspace(0,1,4001)
M1=[np.trapezoid(np.where(xq>s,1.0,0.0),xq) for s in tt]
M2=np.exp(-tt)
M3=[np.trapezoid(np.exp(-s)/(1-xq+xq*np.exp(-s))**2,xq) for s in tt]
d.plot(tt,M1,color=BLUE,lw=1.4); d.plot(tt,M2,color=YELLOW,lw=1.7); d.plot(tt,M3,color=PURPLE,lw=1.4)
d.text(1.12,.08,'(a)',color=BLUE,fontsize=7.5); d.text(1.25,.36,'(b)',color=YELLOW,fontsize=7.5); d.text(1.25,1.06,'(c)',color=PURPLE,fontsize=7.5)
d.set_xlim(0,2); d.set_ylim(0,1.2); tail(d,'$t$','(d)','$M(t)$')
print(M1[100],tt[100],M3[-1])
save(fig,Path(__file__).resolve().parent,'figure',{'a':'v=1,rho0=1,g=0','b':'v=x-1/2, rho0=1','c':'v=x(1-x), rho0=1'})
