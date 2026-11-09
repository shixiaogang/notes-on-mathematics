from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# Model on the linearised line at x0=(1.5,.5), h=.5 with nu=-1 (B=-2I), measured from the normal point, along unit tangent t.
x0=np.array([1.5,.5]); A=cA(x0); h=ch(x0); a=A[0]; pY=-a*h[0]/(a@a); t=np.array([-1.,3.])/np.sqrt(10); g=cg(x0)
def q(s,B): p=pY+s*t; return g@p+.5*B*(p@p)
s=np.linspace(-2.2,2.2,300)
fig,ax=figure(width_mm=100,height_mm=56); panels(fig,.095,.99,.98,.14,0)
b=-2; ax.plot(s,[q(u,-2) for u in s],color=RED,lw=1.4)
ax.plot(s,[q(u,1.) for u in s],color=GREEN,lw=1.4)
ax.plot(s,[q(u,2.) for u in s],color=YELLOW,lw=1.6,ls=(0,(4,2)))
D=1.0; ax.axvspan(-D,D,facecolor=BLUE_FILL,edgecolor='none',zorder=0)
sr=[q(u,-2) for u in (-D,D)]; i=int(np.argmin(sr)); dot(ax,((-D,D)[i],sr[i]),BLUE,ms=4.4)
smax=-(g+(-2)*pY)@t/(-2); hollow(ax,(smax,q(smax,-2)),RED)
for B,col in ((1.,GREEN),(2.,YELLOW)):
    sm=-(g+B*pY)@t/B; dot(ax,(sm,q(sm,B)),col,ms=4.4)
ax.text(-1.75,-3.6,'$\\mathbf{B}=-2\\mathbf{I}$',color=RED,fontsize=8,ha='center'); ax.text(2.17,.22,'$\\mathbf{B}=\\mathbf{I}$',color=GREEN,fontsize=8,ha='right'); ax.text(1.62,3.1,'$\\mathbf{B}=2\\mathbf{I}$',color=MUTED,fontsize=8,ha='right')
ax.text(0,4.1,'$|s|\\leq\\Delta$',color=BLUE,fontsize=8,ha='center')
ax.set_xlim(-2.2,2.2); ax.set_ylim(-4.8,4.8); ax.set_xticks([-2,-1,0,1,2]); ax.set_yticks([-4,-2,0,2,4]); ax.set_xlabel('$s$',labelpad=1); ax.set_ylabel('$q$',labelpad=1)
save(fig,HERE,'figure',{'pY':pY.tolist(),'t':t.tolist(),'smax':float(smax)})
