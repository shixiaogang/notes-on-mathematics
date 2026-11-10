from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: response to a unit point stimulus for Poisson, heat and wave equations.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
ax=axs[0]; style(ax); X=np.linspace(0,1,300)
ax.plot(X,np.minimum(X,1-X)/2,color=BLUE,lw=1.4); ax.plot([.5],[0],'o',ms=3.8,color=RED,clip_on=False)
ax.set_xlim(0,1); ax.set_ylim(0,.3); ax.set_xticks([0,.5,1]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); X=np.linspace(-1.5,1.5,800)
for t,c in zip((.01,.05,.2),SHADES[1:]): ax.plot(X,np.exp(-X**2/(4*t))/np.sqrt(4*np.pi*t),color=c,lw=1.4)
ax.plot([0],[0],'o',ms=3.8,color=RED,clip_on=False); ax.set_xlim(-1.5,1.5); ax.set_ylim(0,3); sub(ax,'b','$x$')
ax=axs[2]; style(ax)
for t,c in zip((.3,.7,1.1),SHADES[1:]):
    ax.plot([-1.5,-t,-t,t,t,1.5],[0,0,.5,.5,0,0],color=c,lw=1.4)
ax.plot([0],[0],'o',ms=3.8,color=RED,clip_on=False); ax.set_xlim(-1.5,1.5); ax.set_ylim(0,.72); sub(ax,'c','$x$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'min(x,1-x)/2; heat kernel t=.01,.05,.2; wave box 1/2 |x|<t, t=.3,.7,1.1'})
