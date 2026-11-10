# Target: area of a square carried by rotation, saddle and uniform expansion.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,axs=figure(112,48,ncols=3)
def square(a,b,n=60):
    s=np.linspace(0,1,n,endpoint=False)
    return np.concatenate([np.c_[a[0]+s*(a[1]-a[0]),a[2]+0*s],np.c_[a[1]+0*s,a[2]+s*(a[3]-a[2])],np.c_[a[1]-s*(a[1]-a[0]),a[3]+0*s],np.c_[a[0]+0*s,a[3]-s*(a[3]-a[2])]],0)
def area(p): x,y=p[:,0],p[:,1]; return .5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))
L=np.log(2); S=square((1,2,-.5,.5),None); S2=square((.5,1,.5,1),None); S3=square((.5,1,.5,1),None)
R=lambda p:np.c_[-p[:,1],p[:,0]]
Sd=lambda p:np.c_[p[:,0]*2,p[:,1]/2]
Ex=lambda p:p*2
for A,p,F,lim,tag in zip(axs,(S,S2,S3),(R,Sd,Ex),((-.7,2.3,-.7,2.3),(-.7,2.3,-.7,2.3),(-.7,2.3,-.7,2.3)),('(a)','(b)','(c)')):
    q=F(p); print(tag,area(p),area(q))
    A.fill(q[:,0],q[:,1],color=BLUE_FILL,ec=BLUE,lw=1.2); A.fill(p[:,0],p[:,1],fc='none',ec=RED,lw=1.4)
    A.set_xlim(lim[0],lim[1]); A.set_ylim(lim[2],lim[3]); A.set_aspect('equal'); tail(A,'$x_1$',tag,'$x_2$')
save(fig,Path(__file__).resolve().parent,'figure',{'rotation':'t=pi/2','saddle':'t=ln2','expansion':'t=ln2'})
