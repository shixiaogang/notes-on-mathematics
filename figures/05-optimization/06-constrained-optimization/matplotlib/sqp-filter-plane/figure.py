from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# Teaching filter F={(0.8,-2.6),(0.3,-2.2),(0.05,-1.9)}, margins gamma=0.1.
F=[(.8,-2.6),(.3,-2.2),(.05,-1.9)]; g=.1
fig,ax=figure(width_mm=92,height_mm=62); panels(fig,.115,.985,.98,.15,0)
th=np.linspace(0,1.1,1200); fy=np.linspace(-3.1,-1.3,900); T,Y=np.meshgrid(th,fy)
forb=np.zeros_like(T,bool)
for t,f in F: forb|=(T>(1-g)*t)&(Y>f-g*t)
ax.contourf(T,Y,forb.astype(float),levels=[.5,1.5],colors=[RED_FILL],zorder=0)
# staircase of pure domination
for t,f in F:
    ax.plot([t,t],[f,-1.3],color=EDGE,lw=.95,zorder=2); ax.plot([t,1.1],[f,f],color=EDGE,lw=.95,zorder=2)
    ax.plot([t],[f],'o',color=BLUE,ms=4.6,mew=0,zorder=5)
C={'A':(.2,-2.4,GREEN),'B':(.4,-2.0,RED),'C':(.295,-2.205,RED)}
for k,(t,f,col) in C.items():
    ax.plot([t],[f],'o' if col==GREEN else 'X',color=col,ms=5,mew=0,zorder=6)
ax.text(.17,-2.43,'A',fontsize=8,ha='right',va='center'); ax.text(.42,-1.96,'B',fontsize=8); ax.text(.275,-2.285,'C',fontsize=8,ha='center',va='center')
setup(ax,(0,1.1),(-3.0,-1.5),xt=(0,.25,.5,.75,1),yt=(-3,-2.5,-2,-1.5),xl='$\\theta$',yl='$f$',equal=False)
save(fig,HERE,'figure',{'filter':F,'gamma':g,'candidates':{k:v[:2] for k,v in C.items()}})
