from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# 2D QP: q(p)=.5 p'Bp + c'p on the line p2=0 (A=(0,1)). Three B.
fig,axes=figure(width_mm=112,height_mm=45,ncols=3); panels(fig,.02,.99,.985,.15,.06)
Bs=[np.diag([1.,1.]),np.diag([1.,-1.]),np.diag([-1.,1.])]; c=np.array([-.6,.3])
X,Y=np.meshgrid(np.linspace(-2,2,400),np.linspace(-1.5,1.5,400))
for ax,B in zip(axes,Bs):
    Q=.5*(B[0,0]*X**2+B[1,1]*Y**2)+c[0]*X+c[1]*Y
    ax.contour(X,Y,Q,levels=[-1.5,-1,-.6,-.3,-.1,.15,.5,1,1.5,2.2],colors=BLUE,linewidths=.7,linestyles='solid',zorder=1)
    ax.plot([-2,2],[0,0],color=EDGE,lw=1.8,zorder=3)
    p=np.array([-c[0]/B[0,0],0]); 
    if B[0,0]>0: dot(ax,p)
    else: hollow(ax,p,RED)
    ax.set_xlim(-2,2); ax.set_ylim(-1.5,1.5); ax.set_aspect('equal'); ax.axis('off')
tags(fig,axes)
save(fig,HERE,'figure',{'B':[b.tolist() for b in Bs],'c':c.tolist(),'A':[0,1]})
