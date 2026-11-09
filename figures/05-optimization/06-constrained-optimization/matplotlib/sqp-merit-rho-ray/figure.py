from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# phi_rho(s,s)=-2s+rho|2s^2-2| along the ray x1=x2=s.
s=np.linspace(0,6,1200); fig,ax=figure(width_mm=100,height_mm=54); panels(fig,.1,.99,.98,.155,0)
for rho,col,ls in ((.1,RED,'-'),(1.,GREEN,'-'),(5.,YELLOW,(0,(4,2)))):
    ax.plot(s,-2*s+rho*np.abs(2*s**2-2),color=col,lw=1.5,ls=ls)
dot(ax,(1,-2)); hollow(ax,(5,-5.2),RED)
ax.text(5.2,-4.2,'$\\rho=0.1$',color=RED,fontsize=8,ha='center'); ax.text(2.8,4.6,'$\\rho=1$',color=GREEN,fontsize=8,ha='left'); ax.text(1.2,7.,'$\\rho=5$',color=MUTED,fontsize=8,ha='right'); ax.text(1.05,-3.1,'$\\mathbf{x}^*$',fontsize=8,ha='center')
setup(ax,(0,6),(-6.5,10),xt=(0,1,2,3,4,5,6),yt=(-5,0,5,10),xl='$s$',yl='$\\phi_\\rho(s,s)$',equal=False)
save(fig,HERE,'figure',{'phi':'-2s+rho|2s^2-2|'})
