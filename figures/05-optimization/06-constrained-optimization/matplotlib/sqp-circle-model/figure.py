from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# min -x1-x2 s.t. x1^2+x2^2=2; first QP at x0=(1.5,.5), nu0=1, B=2I.
x0=np.array([1.5,.5]); B=2*np.eye(2); p,nu=kkt_step(cg(x0),B,cA(x0),ch(x0)); x1=x0+p
fig,axes=figure(width_mm=112,height_mm=60,ncols=2); panels(fig,.08,.995,.985,.22,.2); a,b=axes
X,Y=np.meshgrid(np.linspace(-.4,2.4,300),np.linspace(-.8,2.0,300))
a.contour(X,Y,-X-Y,levels=[-3.2,-2.6,-2,-1.4,-.8,-.2],colors=BLUE,linewidths=.7,linestyles="solid",zorder=1)
circle(a); linline(a,x0,cA(x0)[0],ch(x0)[0],span=1.05)
arrow(a,x0,x1); dot(a,x0,GREEN); dot(a,x1,GREEN); dot(a,(1,1))
a.text(1.58,.42,'$\\mathbf{x}^{(0)}$',fontsize=8); a.text(1.3,.8,'$\\mathbf{x}^{(1)}$',fontsize=8); a.text(.9,1.1,'$\\mathbf{x}^*$',fontsize=8,ha='right')
a.text(.02,1.5,'$h=0$',fontsize=8,color=EDGE); a.text(1.72,-.5,'线性化',fontsize=7.5,color=EDGE,ha='left')
setup(a,(-.3,2.3),(-.75,1.95),xt=(0,1,2),yt=(0,1))
# QP model contours in x-coordinates
U,V=np.meshgrid(np.linspace(.9,2.0,400),np.linspace(.1,1.2,400))
q=-(U-x0[0])-(V-x0[1])+(U-x0[0])**2+(V-x0[1])**2
qs=cg(x0)@p+.5*p@B@p
b.contour(U,V,q,levels=sorted([qs-.3,qs-.12,qs,qs+.2,qs+.45,qs+.8]),colors=BLUE,linewidths=.7,linestyles="solid",zorder=1)
circle(b); linline(b,x0,cA(x0)[0],ch(x0)[0],span=.75)
arrow(b,x0,x1); dot(b,x0,GREEN); dot(b,x1,GREEN); dot(b,(1,1)); dot(b,x0+np.array([.5,.5]),BLUE,ms=3.6)
b.text(1.53,.42,'$\\mathbf{x}^{(0)}$',fontsize=8); b.text(1.1,.72,'$\\mathbf{x}^{(1)}$',fontsize=8,ha='right'); b.text(1.04,1.07,'$\\mathbf{x}^*$',fontsize=8,ha='left')
b.text(2.03,1.0,'模型最低点',fontsize=7.5,color=BLUE,ha='right',va='bottom')
setup(b,(.9,2.05),(.1,1.25),xt=(1,1.5,2),yt=(.5,1))
tags(fig,axes)
save(fig,HERE,'figure',{'x0':x0.tolist(),'p':p.tolist(),'nu1':nu.tolist(),'x1':x1.tolist(),'h1':ch(x1).tolist()})
