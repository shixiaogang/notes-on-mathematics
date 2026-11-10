# Target: L^p growth of data errors under v=x: scalar field vs density.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,52,ncols=2,sharey=True)
t=np.linspace(0,2,200); xq=np.linspace(0,60,240001); dx=xq[1]-xq[0]
ps=[(1,BLUE),(2,YELLOW)]
def norm(f,p): return (np.max(np.abs(f)) if p==np.inf else ((np.abs(f)**p).sum()*dx)**(1/p))
e0=tent(xq,1,1); N={p:norm(e0,p) for p in (1,2,np.inf)}
pts=np.array([0,.5,1,1.5,2.])
for p,c in ps+[(np.inf,PURPLE)]:
    ex=0 if p==np.inf else 1/p
    a.plot(t,np.exp(ex*t),color=c,lw=1.7 if c==YELLOW else 1.4)
    a.plot(pts,[norm(tent(xq*np.exp(-s),1,1),p)/N[p] for s in pts],'o',color=GREEN,ms=3)
    exr=0 if p==1 else -(1-(0 if p==np.inf else 1/p))
    b.plot(t,np.exp(exr*t),color=c,lw=1.7 if c==YELLOW else 1.4)
    b.plot(pts,[norm(np.exp(-s)*tent(xq*np.exp(-s),1,1),p)/N[p] for s in pts],'o',color=GREEN,ms=3)
a.set_yscale('log',base=2); a.set_yticks([.125,.25,.5,1,2,4,8],['$1/8$','$1/4$','$1/2$','$1$','$2$','$4$','$8$']); a.minorticks_off()
a.text(1.5,6.2,'$p=1$',color=BLUE,ha='right',fontsize=7.5); a.text(1.5,2.75,'$p=2$',color=YELLOW,ha='right',fontsize=7.5); a.text(1.5,1.12,'$p=\\infty$',color=PURPLE,ha='right',fontsize=7.5)
b.text(1.5,1.12,'$p=1$',color=BLUE,ha='right',fontsize=7.5); b.text(1.5,.6,'$p=2$',color=YELLOW,ha='right',fontsize=7.5); b.text(1.0,.24,'$p=\\infty$',color=PURPLE,ha='right',fontsize=7.5)
a.set_xlim(0,2); b.set_xlim(0,2); a.set_ylim(.1,9)
tail(a,'$t$','(a)','$\\Vert e(\\cdot,t)\\Vert_p/\\Vert e_0\\Vert_p$'); tail(b,'$t$','(b)')
save(fig,Path(__file__).resolve().parent,'figure',{'u':'exp(t/p)','rho':'exp(-(1-1/p) t)'})
