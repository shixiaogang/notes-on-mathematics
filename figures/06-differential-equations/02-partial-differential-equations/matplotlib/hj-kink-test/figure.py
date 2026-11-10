from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: F(p)=|p|-1 at kinks. (a) 1-|x| touched above with |p|<=1; (b) |x|-1 touched below by slope 0; (c) F on [-1,1].
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
X=np.linspace(-1,1,401)
ax=axs[0]; style(ax); ax.plot(X,1-np.abs(X),color=BLUE,lw=1.4)
for s in (-.6,0,.6): ax.plot(X,1+s*X+.1*X**2,color=PURPLE,lw=1.1)
ax.plot([0],[1],'o',ms=4.2,color=RED,zorder=6); ax.plot([-1,1],[0,0],'o',ms=4,color=RED,clip_on=False,zorder=6)
ax.set_xlim(-1,1); ax.set_ylim(-.15,1.5); ax.set_xticks([-1,0,1]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.plot(X,np.abs(X)-1,color=YELLOW,lw=1.6)
ax.plot(X,0*X-1,color=RED,lw=1.2)
ax.plot([0],[-1],'o',ms=4.2,color=RED,zorder=6); ax.plot([-1,1],[0,0],'o',ms=4,color=RED,clip_on=False,zorder=6)
ax.set_xlim(-1,1); ax.set_ylim(-1.25,.15); ax.set_xticks([-1,0,1]); sub(ax,'b','$x$')
ax=axs[2]; style(ax); P=np.linspace(-1.4,1.4,281); ax.plot(P,np.abs(P)-1,color=BLUE,lw=1.4)
ax.fill_between([-1,1],-1.1,0,color=BLUE_FILL,lw=0); ax.axhline(0,color=MUTED,lw=.85,ls=':')
ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.1,.45); ax.set_xticks([-1,0,1]); ax.set_ylabel('$|p|-1$'); sub(ax,'c','$p$')
save(fig,HERE,'figure',{'formula':'|p|-1; u=1-|x| and |x|-1'})
