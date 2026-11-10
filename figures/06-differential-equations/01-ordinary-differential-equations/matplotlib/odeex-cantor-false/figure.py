from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# The Cantor function: zero derivative a.e. but not a solution of x'=0.
fig,ax=figure(width_mm=86,height_mm=48)
panel(fig,.12,.97,.97,.17)
def cantor(x,depth=30):
    r=0.;w=.5
    for _ in range(depth):
        x*=3
        if x>=2: r+=w; x-=2
        elif x>=1: return r+w
        w/=2
    return r
t=np.linspace(0,1,6561); y=[cantor(float(s)) for s in t]
ax.plot(t,y,color=RED,lw=1.3,zorder=3); ax.plot([0,1],[0,0],color=BLUE,lw=1.6,zorder=4); dot(ax,0,0)
ax.text(.45,.56,'Cantor函数',color=RED,fontsize=7.5,ha='right',va='bottom'); ax.text(.97,.03,'唯一解 x≡0',color=BLUE,fontsize=7.5,ha='right',va='bottom')
ax.set_xlim(0,1.0); ax.set_ylim(-.04,1.04); ax.set_xticks([0,1/3,2/3,1]); ax.set_xticklabels(['0','1/3','2/3','1']); ax.set_yticks([0,.5,1]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('x',labelpad=1)
save(fig,HERE,'figure',{'levels':'Cantor'})
