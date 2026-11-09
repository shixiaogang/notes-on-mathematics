from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Quadratic model at x0 in the tangent basis (E1,E2), radius 1; pullback for comparison.
q=X0@A3@X0; g=np.array([2/9,-8/9]); H=np.array([[1,-10/9],[-10/9,2/3]])
u=np.linspace(-1.35,1.35,400); V1,V2=np.meshgrid(u,u)
M=g[0]*V1+g[1]*V2+.5*(H[0,0]*V1**2+2*H[0,1]*V1*V2+H[1,1]*V2**2)
Y=X0[None,None,:]+V1[...,None]*E1+V2[...,None]*E2
Y/=np.linalg.norm(Y,axis=-1,keepdims=True)
F=.5*(Y[...,0]**2+2*Y[...,1]**2+4*Y[...,2]**2)-f3(X0)
fig,ax=figure(width_mm=78,height_mm=72)
levels=[-.5,-.3,-.1,.1,.4]
ax.contour(V1,V2,M,levels=levels,colors=YELLOW,linewidths=1.1,linestyles='solid')
ax.contour(V1,V2,F,levels=levels,colors=BLUE,linewidths=.9,linestyles='solid')
th=np.linspace(0,2*np.pi,200); ax.plot(np.cos(th),np.sin(th),color=GRAY,lw=1.5)
vc=np.array([-.18378378,.73513514]); vt=np.array([0.,1.])
ax.plot([0,vc[0]],[0,vc[1]],color=GREEN,lw=1.5); ax.plot([vc[0],vt[0]],[vc[1],vt[1]],color=GREEN,lw=1.5)
ax.plot(0,0,'o',ms=4.4,color=GREEN); ax.plot(*vc,'o',ms=4.4,mfc='white',mec=YELLOW,mew=1.1); ax.plot(*vt,'o',ms=4.4,color=GREEN)
ax.text(.07,-.1,r'$\mathbf{0}$',fontsize=8); ax.text(vc[0]-.09,vc[1]-.03,r'$\mathbf{v}^{\mathrm{C}}$',ha='right',fontsize=8); ax.text(.07,1.05,r'$\mathbf{v}$',fontsize=8)
ax.set_aspect('equal'); ax.set_xlabel(r'$v_1$'); ax.set_ylabel(r'$v_2$'); ax.set_xlim(-1.35,1.35); ax.set_ylim(-1.35,1.35)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'m(v)=g.v+v.Hv/2, g=(2/9,-8/9), H=[[1,-10/9],[-10/9,2/3]]; pullback with normalization'})
