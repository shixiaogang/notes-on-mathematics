from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: stationary problems. (a) |u'|=2|x| on (-1,1) with zero data: two classical solutions.
# (b) |u'|=1 on (0,1), u(0)=0, u(1)=2: the viscosity solution loses the right boundary value.
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
X=np.linspace(-1,1,401); ax=axs[0]; style(ax)
ax.plot(X,1-X**2,color=BLUE,lw=1.4); ax.plot(X,X**2-1,color=YELLOW,lw=1.6)
ax.plot([-1,1],[0,0],'o',ms=4.2,color=RED,zorder=6,clip_on=False)
ax.set_xlim(-1,1); ax.set_ylim(-1.2,1.2); ax.set_xticks([-1,0,1]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
X=np.linspace(0,1,201); ax=axs[1]; style(ax)
ax.plot(X,X,color=BLUE,lw=1.4); ax.plot([0],[0],'o',ms=4.2,color=RED,zorder=6,clip_on=False); ax.plot([1],[2],'o',ms=4.2,color=RED,zorder=6,clip_on=False)
ax.plot([1],[1],'o',ms=4.2,mfc='white',mec=BLUE,zorder=6,clip_on=False); ax.plot([1,1],[1,2],color=RED,lw=1,ls=':')
ax.set_xlim(0,1.02); ax.set_ylim(0,2.2); ax.set_xticks([0,.5,1]); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'(a) +-(1-x^2); (b) min(x,3-x)=x'})
