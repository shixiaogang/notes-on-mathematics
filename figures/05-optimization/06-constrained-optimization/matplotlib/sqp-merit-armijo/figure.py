from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
x=np.array([1.4,.2]); nu=np.array([.5]); rho=2.; p,nun=kkt_step(cg(x),cHL(x,nu),cA(x),ch(x)); D=cg(x)@p-rho*abs(ch(x)[0]); c=.1
phi=lambda y:cf(y)+rho*abs(ch(y)[0])
al=np.linspace(0,1.1,300); fig,ax=figure(width_mm=96,height_mm=52); panels(fig,.115,.99,.98,.16,0)
ax.plot(al,[phi(x+a*p) for a in al],color=BLUE,lw=1.4)
ax.plot(al,phi(x)+c*al*D,color=PURPLE,lw=1.2,ls=(0,(4,2))); ax.plot(al,phi(x)+al*D,color=MUTED,lw=.85)
for a,col in ((1.,RED),(.5,RED),(.25,GREEN)):
    ax.plot([a],[phi(x+a*p)],'o',color=col,ms=4.6,mew=0,zorder=6)
ax.text(1.09,-.84,'$\\phi_\\rho$',color=BLUE,fontsize=8,ha='right',va='bottom'); ax.text(1.08,-1.64,'充分下降线',color=PURPLE,fontsize=7.5,ha='right',va='bottom'); ax.text(.72,-2.08,'切线',color=MUTED,fontsize=7.5,ha='left')
setup(ax,(0,1.1),(-2.4,-.7),xt=(0,.25,.5,.75,1),yt=(-2,-1.5,-1),xl='$\\alpha$',yl='评价函数',equal=False)
save(fig,HERE,'figure',{'p':p.tolist(),'D':float(D),'phi0':float(phi(x)),'phi_trials':{a:float(phi(x+a*p)) for a in (1.,.5,.25)}})
