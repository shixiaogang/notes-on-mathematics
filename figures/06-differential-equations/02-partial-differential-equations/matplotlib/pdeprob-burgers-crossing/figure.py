from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: Burgers particle paths cross at (x,t)=(1,1) for the ramp datum; profile steepens.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
u0=lambda x:np.where(x<0,1.0,np.where(x>1,0.0,1-x))
ax=axs[0]; style(ax)
t=np.array([0,1.45])
for x0 in np.concatenate([np.arange(-1.5,0,.5),np.arange(0,1.01,.2),np.arange(1.5,3,.5)]):
    v=float(u0(np.array(x0)))
    ax.plot([x0,x0+v*1],[0,1],color=LINE,lw=.85); ax.plot([x0+v,x0+v*1.45],[1,1.45],color=LINE,lw=.85,ls=':')
ax.plot([1],[1],'o',ms=4,color=RED)
ax.plot([-1.5,3],[0,0],color=RED,lw=2,clip_on=False)
ax.set_xlim(-1.5,3); ax.set_ylim(0,1.45); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
X=np.linspace(-1,3,1000)
def prof(t): 
    return np.where(X<t,1.0,np.where(X>1,0.0,(1-X)/(1-t)))
ax.plot(X,prof(0),color=RED,lw=1.5)
for t,c in zip((.5,.9),SHADES[1:]): ax.plot(X,prof(t),color=c,lw=1.4)
ax.set_xlim(-1,3); ax.set_ylim(0,1.15); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'ramp u0; u=(1-x)/(1-t) for t<x<1'})
