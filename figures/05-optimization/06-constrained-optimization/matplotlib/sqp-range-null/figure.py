from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
x0=np.array([1.5,.5]); a0=cA(x0)[0]; h0=ch(x0)[0]; B=2*np.eye(2)
pY=-a0*h0/(a0@a0); Z=np.array([1.,-3.]); pz=-Z@(cg(x0)+B@pY)/(Z@B@Z); pZ=Z*pz; p=pY+pZ
fig,ax=figure(width_mm=78,height_mm=68); 
U,V=np.meshgrid(np.linspace(1.,1.8,300),np.linspace(.2,1.0,300))
q=-(U-x0[0])-(V-x0[1])+(U-x0[0])**2+(V-x0[1])**2; qs=cg(x0)@p+.5*p@B@p
ax.contour(U,V,q,levels=[qs+d for d in (-.06,0,.1,.24,.42)],colors=BLUE,linewidths=.7,linestyles="solid",zorder=1)
circle(ax); linline(ax,x0,a0,h0,span=.5)
ax.plot([x0[0]-.5*Z[0]/3.162+0,x0[0]+.2],[0,0],alpha=0)
arrow(ax,x0,x0+pY,color=PURPLE); arrow(ax,x0+pY,x0+p,color=YELLOW); arrow(ax,x0,x0+p,color=GREEN,lw=1.4)
dot(ax,x0,GREEN); dot(ax,x0+p,GREEN)
ax.text(1.52,.45,'$\\mathbf{x}^{(0)}$',fontsize=8); ax.text(1.42,.42,'$\\mathbf{d}_Y$',color=PURPLE,fontsize=8,ha='right')
ax.text(1.255,.56,'$\\mathbf{Z}\\mathbf{d}_Z$',color=MUTED,fontsize=8,ha='right'); ax.text(1.40,.70,'$\\mathbf{d}$',color=GREEN,fontsize=8)
ax.text(1.27,.78,'$\\mathbf{x}^{(0)}+\\mathbf{d}$',fontsize=8,ha='left',va='bottom')
ax.text(1.64,.1+.14,'',fontsize=7.5)
setup(ax,(1.,1.8),(.2,1.0),xt=(1.2,1.5,1.8),yt=(.4,.6,.8,1))
save(fig,HERE,'figure',{'pY':pY.tolist(),'pZ':pZ.tolist(),'p':p.tolist(),'pz':float(pz)})
