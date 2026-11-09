from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# min -x1-x2, g1=x1^2+x2^2-2<=0, g2=x2-1.2<=0, g3=-x1<=0, x0=(.5,1.7), lam0=(1,0,0).
L=ineq_sqp([.5,1.7],[1.,0,0],T=7)
P=np.array([l['x'] for l in L])
fig,axes=figure(width_mm=112,height_mm=62,ncols=2); panels(fig,.08,.995,.985,.19,.2); a,b=axes
def region(ax):
    th=np.linspace(0,np.pi/2,300); xx=np.sqrt(2)*np.cos(th); yy=np.sqrt(2)*np.sin(th); keep=yy<=1.2
    px=np.r_[0,xx[keep],np.sqrt(2-1.44),0]; py=np.r_[0,yy[keep],1.2,1.2]
    ax.fill(px,py,facecolor=BLUE_FILL,edgecolor=BLUE,lw=.9,zorder=1)
    t=np.linspace(-.45,1.3,200); ax.plot(np.sqrt(2)*np.cos(t),np.sqrt(2)*np.sin(t),color=EDGE,lw=1.8,zorder=3)
    ax.plot([-.1,2.3],[1.2,1.2],color=EDGE,lw=1.8,zorder=3)
region(a); x0=P[0]; x1=P[1]
a0=DG[0](x0); linline(a,x0,a0,GS[0](x0),span=1.6); arrow(a,x0,x1); dot(a,x0,GREEN); dot(a,x1,GREEN); dot(a,(1,1))
a.text(.58,1.72,'$\\mathbf{x}^{(0)}$',fontsize=8); a.text(1.06,1.25,'$\\mathbf{x}^{(1)}$',fontsize=8); a.text(.9,.92,'$\\mathbf{x}^*$',fontsize=8,ha='right',va='top')
a.text(1.75,1.27,'$g_2=0$',color=EDGE,fontsize=7.5); a.text(1.42,-.2,'$g_1=0$',color=EDGE,fontsize=7.5); a.text(-.05,.9,'',fontsize=7)
setup(a,(-.1,2.3),(-.45,2.05),xt=(0,1,2),yt=(0,1,2))
region(b); b.plot(P[:6,0],P[:6,1],color=GREEN,lw=1.4,marker='o',ms=3.6,mew=0,zorder=5); dot(b,(1,1))
for i,(dx,dy,ha) in {0:(.08,.03,'left'),1:(.07,.05,'left'),2:(.07,-.02,'left'),3:(.08,.04,'left')}.items():
    b.text(P[i,0]+dx,P[i,1]+dy,'$\\mathbf{x}^{(%d)}$'%i,fontsize=8,ha=ha)
setup(b,(-.1,2.3),(-.45,2.05),xt=(0,1,2),yt=(0,1,2))
tags(fig,axes)
save(fig,HERE,'figure',{'iterates':P.tolist(),'W':[l.get('S') for l in L],'lam':[l['lam'].tolist() for l in L[:-1]]})
