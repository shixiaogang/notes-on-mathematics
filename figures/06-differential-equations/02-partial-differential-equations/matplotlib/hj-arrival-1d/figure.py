from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: 1D arrival time T(x)=int_0^x ds/c(s) for a piecewise-constant speed; slope of T is 1/c.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
def c(x): return np.where(x<1,1.0,np.where(x<2,0.4,1.5))
def T(x): return np.where(x<1,x,np.where(x<2,1+(x-1)/0.4,3.5+(x-2)/1.5))
X=np.linspace(0,3,1201)
ax=axs[0]; style(ax)
for a,b in [(0,1),(1,2),(2,3)]:
    Y=np.array([c(np.array((a+b)/2))]*2); ax.plot([a,b],Y,color=BLUE,lw=1.4)
    ax.fill_between([a,b],0,Y,color=BLUE_FILL,lw=0)
ax.set_xlim(0,3); ax.set_ylim(0,1.75); ax.set_xticks([0,1,2,3]); ax.set_ylabel('$c(x)$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
ax.plot(X,T(X),color=BLUE,lw=1.4)
ax.plot([0],[0],'o',ms=4,color=RED,clip_on=False,zorder=5)
for x0 in (1,2,3):
    ax.plot([x0,x0],[0,float(T(np.array(x0)))],color=MUTED,lw=.85,ls=':')
    ax.plot([0,x0],[float(T(np.array(x0)))]*2,color=MUTED,lw=.85,ls=':')
ax.set_xlim(0,3.05); ax.set_ylim(0,4.6); ax.set_xticks([0,1,2,3]); ax.set_yticks([0,1,3.5,4.17],['0','1','3.5','4.17']); ax.set_ylabel('$T(x)$'); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'c=1,0.4,1.5 on [0,1),[1,2),[2,3]; T=int ds/c'})
