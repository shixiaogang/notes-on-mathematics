from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: H=|p|, u(x,t)=min_{|y-x|<=t}u0(y) with u0=dist(x,{-1.5,1}). (a) profiles; (b) fronts in (x,t), meeting at (-.25,1.25).
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
X=np.linspace(-3.5,3,1301); d=np.minimum(np.abs(X+1.5),np.abs(X-1))
ax=axs[0]; style(ax); ax.plot(X,d,color=RED,lw=1.3)
for t,c in ((.5,SHADES[1]),(1,SHADES[3])): ax.plot(X,np.maximum(d-t,0),color=c,lw=1.4)
ax.set_xlim(-3.5,3); ax.set_ylim(-.05,2); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.fill_between(X,0,d,color=BLUE_FILL,lw=0)
ax.plot(X,d,color=LINE,lw=1.5); ax.plot([-1.5,1],[0,0],'o',ms=4.4,color=RED,zorder=6,clip_on=False)
ax.plot([-.25],[1.25],'o',ms=4.2,color=INK,zorder=6)
ax.set_xlim(-3.5,3); ax.set_ylim(0,2); ax.set_ylabel('$t$'); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'u=(d-t)^+; d=dist to {-1.5,1}'})
