# Target: shifted velocity v=1 vs v=1+delta: smooth tent vs step data; sup and L^p errors against delta.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b,c)=figure(112,52,ncols=3)
t=1.5; d=.2; x=np.linspace(-1,3.5,2001); xq=np.linspace(-3,8,440001); dx=xq[1]-xq[0]
a.fill_between(x,tent(x-t,0),tent(x-t*(1+d),0),color=RED_FILL,lw=0)
a.plot(x,tent(x-t,0),color=BLUE,lw=1.4); a.plot(x,tent(x-t*(1+d),0),color=YELLOW,lw=1.7)
a.set_xlim(-1,3.5); a.set_ylim(0,1.15); a.set_xticks([0,1,2,3]); tail(a,'$x$','(a)','$u$')
H=lambda s:(s<0).astype(float)
b.fill_between(x,H(x-t),H(x-t*(1+d)),color=RED_FILL,lw=0,step='mid')
b.plot(x,H(x-t),color=BLUE,lw=1.4); b.plot(x,H(x-t*(1+d)),color=YELLOW,lw=1.7)
b.set_xlim(-1,3.5); b.set_ylim(0,1.15); b.set_xticks([0,1,2,3]); tail(b,'$x$','(b)')
ds=np.logspace(-3,-.2,12)
sup_t=[np.max(np.abs(tent(xq-t,0)-tent(xq-t*(1+s),0))) for s in ds]
sup_s=[np.max(np.abs(H(xq-t)-H(xq-t*(1+s)))) for s in ds]
l1_s=[np.abs(H(xq-t)-H(xq-t*(1+s))).sum()*dx for s in ds]
l2_s=[np.sqrt(((H(xq-t)-H(xq-t*(1+s)))**2).sum()*dx) for s in ds]
c.loglog(ds,sup_t,color=BLUE,lw=1.4); c.loglog(ds,l1_s,color=GREEN,lw=1.4,ls=(0,(3,2))); c.loglog(ds,l2_s,color=YELLOW,lw=1.7); c.loglog(ds,sup_s,color=RED,lw=1.4)
c.loglog(ds,2.2*ds**.5,color=PURPLE,lw=.85,ls=(0,(1.5,1.5)))
c.set_ylim(1e-3,4); tail(c,'$\\delta$','(c)')
print(sup_t[0],1.5e-3,l1_s[0],l2_s[0],np.sqrt(1.5e-3))
save(fig,Path(__file__).resolve().parent,'figure',{'t':1.5})
