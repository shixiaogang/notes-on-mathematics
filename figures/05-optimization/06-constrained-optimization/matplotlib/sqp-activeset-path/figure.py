from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# min .5||x-c||^2, c=(4,2), x1+x2<=3, -x1<=0, -x2<=0, x1+2x2<=4
c=np.array([4.,2.]); poly=np.array([[0,0],[3,0],[2,1],[0,2]],float)
fig,ax=figure(width_mm=96,height_mm=62)
X,Y=np.meshgrid(np.linspace(-.5,5,400),np.linspace(-.6,3.2,400))
ax.fill(poly[:,0],poly[:,1],facecolor=BLUE_FILL,edgecolor=BLUE,lw=.9,zorder=1)
ax.contour(X,Y,.5*((X-4)**2+(Y-2)**2),levels=[.5,1.25,2.5,4.25,6.5,9.25],colors=BLUE,linewidths=.7,linestyles="solid",zorder=2)
P=np.array([[0,0],[3,0],[2.5,.5]])
ax.plot(P[:,0],P[:,1],color=GREEN,lw=1.6,zorder=5)
ax.plot([3,4],[0,0],color=YELLOW,lw=1.4,ls=(0,(4,2)),zorder=4); arrow(ax,(3.6,0),(4,0),color=YELLOW,lw=1.2)
for q in P[:2]: dot(ax,q,GREEN)
dot(ax,P[2]); dot(ax,c,BLUE,ms=3.6)
ax.text(-.1,-.33,'$\\mathbf{x}^{(0)}=\\mathbf{x}^{(1)}$',fontsize=8,ha='left',va='center'); ax.text(3.0,-.33,'$\\mathbf{x}^{(2)}=\\mathbf{x}^{(3)}$',fontsize=8,ha='center',va='center'); ax.text(2.62,.6,'$\\mathbf{x}^{(4)}=\\mathbf{x}^*$',fontsize=8,ha='left')
ax.text(4.1,2.05,'$\\mathbf{c}$',fontsize=8,color=BLUE); ax.text(4.0,.12,'全步终点',fontsize=7.5,color=MUTED,ha='center')
ax.text(1.5,.14,'$g_3$',color=EDGE,fontsize=7.5,ha='center'); ax.text(.4,1.0,'$g_2$',color=EDGE,fontsize=7.5); ax.text(2.88,.28,'$g_1$',color=EDGE,fontsize=7.5); ax.text(1.0,1.62,'$g_4$',color=EDGE,fontsize=7.5)
setup(ax,(-.4,4.9),(-.55,2.9),xt=(0,1,2,3,4),yt=(0,1,2))
save(fig,HERE,'figure',{'c':c.tolist(),'iterates':P.tolist()})
