# Target: 2D Gaussian density carried by expansion, saddle and contraction.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
from matplotlib.colors import PowerNorm
fig,axs=figure(112,38,ncols=4,sharey=True)
xl=(-3,3); g=np.linspace(*xl,481); X,Y=np.meshgrid(g,g)
r0=lambda a,b:np.exp(-(a**2+b**2)/2)
fields=[(r0(X,Y),'(a)'),(np.exp(-1)*r0(X*np.exp(-.5),Y*np.exp(-.5)),'(b)'),(r0(X*np.exp(-.5),Y*np.exp(.5)),'(c)'),(np.exp(1)*r0(X*np.exp(.5),Y*np.exp(.5)),'(d)')]
for i,(A,(Z,tag)) in enumerate(zip(axs,fields)):
    A.imshow(Z,extent=[*xl,*xl],origin='lower',cmap=CMAP,norm=PowerNorm(.5,vmin=0,vmax=np.e),interpolation='bilinear')
    A.text(0,2.25,f'{Z.max():.2f}',ha='center',fontsize=7.5)
    A.set_xlim(*xl); A.set_ylim(*xl); A.set_aspect('equal'); A.set_xticks([-2,0,2]); A.set_yticks([-2,0,2]); tail(A,'$x_1$',tag,'$x_2$' if i==0 else None)
save(fig,Path(__file__).resolve().parent,'figure',{'t':1,'rates':'expansion div=1, saddle div=0, contraction div=-1'})
