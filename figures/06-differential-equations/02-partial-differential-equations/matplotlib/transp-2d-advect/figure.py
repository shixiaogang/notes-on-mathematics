# Target: advection of a 2D blob by rotation and saddle flow; field values unchanged.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,axs=figure(112,46,ncols=3,sharey=True)
xl=(-2.5,2.5); g=np.linspace(*xl,521); X,Y=np.meshgrid(g,g)
u0=lambda a,b:np.exp(-(((a-1.2)/.42)**2+((b+.1)/.7)**2))+.8*np.exp(-(((a-.8)/.3)**2+((b-.95)/.3)**2))
c=np.cos(np.pi/2); s=np.sin(np.pi/2)
L=.5
fields=[u0(X,Y), u0(c*X+s*Y,-s*X+c*Y), u0(X*np.exp(-L),Y*np.exp(L))]
q=np.linspace(-2,2,5); QX,QY=np.meshgrid(q,q)
V=[(0*QX,0*QX),(-QY,QX),(QX,-QY)]
for i,(A,Z,(vx,vy),tag) in enumerate(zip(axs,fields,V,'(a) (b) (c)'.split())):
    heat(A,Z,xl,xl,vmin=0,vmax=1.05)
    if i: A.quiver(QX,QY,vx,vy,color=MUTED,angles='xy',scale_units='xy',scale=5.2,width=.009,headwidth=4,headlength=5)
    A.set_xlim(*xl); A.set_ylim(*xl); A.set_aspect('equal'); A.set_xticks([-2,0,2]); A.set_yticks([-2,0,2]); tail(A,'$x_1$',tag,'$x_2$' if i==0 else None)
    print(i,float(Z.max()))
save(fig,Path(__file__).resolve().parent,'figure',{'rotation':'t=pi/2','saddle':'t=0.5'})
