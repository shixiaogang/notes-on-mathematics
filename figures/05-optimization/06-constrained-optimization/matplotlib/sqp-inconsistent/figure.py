from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# f=((x1-2)^2+x2^2)/2, h1=x2-x1^2, h2=x2-1; x0=(0,0), elastic step p=(2,0), alpha=1/2, then p=(0,1) to x*=(1,1).
fig,axes=figure(width_mm=112,height_mm=47,ncols=2); panels(fig,.075,.995,.985,.27,.2); a,b=axes
u=np.linspace(-1.6,2.3,300)
def base(ax):
    ax.plot(u,u**2,color=EDGE,lw=1.8,zorder=3); ax.plot([-1.6,2.6],[1,1],color=EDGE,lw=1.8,zorder=3)
    dot(ax,(1,1)); hollow(ax,(-1,1),RED)
    ax.contour(*np.meshgrid(np.linspace(-1.6,2.6,300),np.linspace(-.5,2,300)),.5*((np.meshgrid(np.linspace(-1.6,2.6,300),np.linspace(-.5,2,300))[0]-2)**2+np.meshgrid(np.linspace(-1.6,2.6,300),np.linspace(-.5,2,300))[1]**2),levels=[.5,1,2,3.5,5.5],colors=BLUE,linewidths=.6,linestyles='solid',zorder=1)
base(a); a.plot([-1.6,2.6],[0,0],color=EDGE,lw=1.1,ls=(0,(4,2)),zorder=4); dot(a,(0,0),GREEN)
arrow(a,(0,.04),(0,.96),color=RED,lw=1.1,ls=(0,(3,1.5)))
a.text(.3,-.3,'$\\mathbf{x}^{(0)}$',fontsize=8,ha='center'); a.text(1.58,1.08,'$h_2=0$',color=EDGE,fontsize=7.5,ha='left'); a.text(1.22,1.78,'$h_1=0$',color=EDGE,fontsize=7.5,ha='right')
setup(a,(-1.6,2.6),(-.5,2.0),xt=(-1,0,1,2),yt=(0,1,2))
base(b); P=np.array([[0,0],[1,0],[1,1]]); b.plot(P[:,0],P[:,1],color=GREEN,lw=1.5,zorder=5)
b.plot([1,2],[0,0],color=YELLOW,lw=1.5,ls=(0,(4,2)),zorder=4); hollow(b,(2,0),YELLOW)
for q in P[:2]: dot(b,q,GREEN)
b.text(0,-.3,'$\\mathbf{x}^{(0)}$',fontsize=8,ha='center'); b.text(1,-.3,'$\\mathbf{x}^{(1)}$',fontsize=8,ha='center'); b.text(2,-.3,'全步',fontsize=7.5,ha='center',color=MUTED); b.text(.9,1.14,'$\\mathbf{x}^{(2)}=\\mathbf{x}^*$',fontsize=8,ha='right')
setup(b,(-1.6,2.6),(-.5,2.0),xt=(-1,0,1,2),yt=(0,1,2))
tags(fig,axes)
save(fig,HERE,'figure',{'elastic_step':[2,0],'alpha':.5,'x1':[1,0],'x2':[1,1]})
