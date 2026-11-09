from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
fig,axes=figure(width_mm=112,height_mm=56,ncols=2); panels(fig,.02,.99,.99,.13,.05); a,b=axes
poly=np.array([[0,0],[3,0],[2,1],[0,2]],float); c=np.array([4.,2.])
for ax in axes: ax.fill(poly[:,0],poly[:,1],facecolor=BLUE_FILL,edgecolor=BLUE,lw=.9,zorder=1); ax.axis('off'); ax.set_aspect('equal')
# (a) at the origin, W={g2,g3}
a.plot([0,0],[0,2],color=EDGE,lw=2.0,zorder=3); a.plot([0,3],[0,0],color=EDGE,lw=2.0,zorder=3)
arrow(a,(0,0),(-1,0),color=PURPLE); arrow(a,(0,0),(0,-1),color=PURPLE); arrow(a,(0,0),(4/1.5,2/1.5),color=BLUE)
dot(a,(0,0),GREEN); a.text(-1.02,.15,'$\\nabla g_2$',color=PURPLE,fontsize=8); a.text(.1,-1.0,'$\\nabla g_3$',color=PURPLE,fontsize=8); a.text(2.75,1.33,'$-\\nabla q$',color=BLUE,fontsize=8)
a.set_xlim(-1.4,3.5); a.set_ylim(-1.25,2.3)
x=np.array([3.,0.]); gq=x-c
b.plot(poly[[1,2],0],poly[[1,2],1],color=EDGE,lw=2.0,zorder=3); b.plot([0,3],[0,0],color=EDGE,lw=2.0,zorder=3)
# -grad q=(1,2) = lam1*(1,1)+lam3*(0,-1) with lam1=1, lam3=-1
arrow(b,x,x+np.array([1,1]),color=PURPLE); arrow(b,x,x+np.array([0,1]),color=RED,ls=(0,(3,1.5))); arrow(b,x,x-gq,color=BLUE); arrow(b,x,x+np.array([-.9,.9]),color=GREEN)
dot(b,x,GREEN)
b.text(4.08,.92,'$\\nabla g_1$',color=PURPLE,fontsize=8); b.text(3.02,1.14,'$\\lambda_3\\nabla g_3$',color=RED,fontsize=8,ha='right',va='bottom'); b.text(4.0,2.05,'$-\\nabla q$',color=BLUE,fontsize=8,ha='center',va='bottom'); b.text(2.05,.98,'',fontsize=8)
b.text(2.08,.62,'',fontsize=8)
b.text(2.0,.55,'释放后',color=GREEN,fontsize=7.5,ha='right')
b.set_xlim(1.0,4.9); b.set_ylim(-.65,2.5)
tags(fig,axes)
save(fig,HERE,'figure',{'x':x.tolist(),'gradq':gq.tolist(),'lambda1':1,'lambda3':-1})
