from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# merit SQP on the circle, far start (.2,-1.6), nu0=1, rho=1, shifted to keep reduced curvature >= .5.
L=ls_merit_sqp([.2,-1.6],[1.],rho=1.,T=14,floor=.5)
P=np.array([l['x'] for l in L]); e=[np.linalg.norm(q-1) for q in P]; al=[l['alpha'] for l in L[:-1]]
fig,axes=figure(width_mm=112,height_mm=60,ncols=2); panels(fig,.08,.99,.985,.22,.36); a,b=axes
circle(a); X,Y=np.meshgrid(np.linspace(-2.2,2.2,200),np.linspace(-2.2,2.2,200)); a.contour(X,Y,-X-Y,levels=[-3,-1.5,0,1.5,3],colors=BLUE,linewidths=.6,linestyles='solid',zorder=1)
n=min(12,len(P)); a.plot(P[:n,0],P[:n,1],color=GREEN,lw=1.3,marker='o',ms=3,mew=0,zorder=5); dot(a,(1,1)); hollow(a,(-1,-1),PURPLE)
a.text(.3,-1.85,'$\\mathbf{x}^{(0)}$',fontsize=8); setup(a,(-2.2,2.2),(-2.2,2.2),xt=(-2,0,2),yt=(-2,0,2))
idx=[i for i,v in enumerate(e) if v>1e-15]
b.semilogy(idx,[e[i] for i in idx],color=GREEN,lw=1.4,marker='o',ms=3.2,mew=0)
for i,v in enumerate(al):
    if i in idx and v<1: b.axvspan(i-.5,i+.5,facecolor=YELLOW_FILL,edgecolor='none',zorder=0)
setup(b,(-.5,13.5),(1e-16,10),xt=(0,3,6,9,12),yt=[1e-15,1e-10,1e-5,1],xl='$t$',yl='到解的距离',equal=False); b.minorticks_off()
tags(fig,axes)
save(fig,HERE,'figure',{'iterates':P.tolist(),'alpha':al,'tau':[l['tau'] for l in L[:-1]],'dist':e})
