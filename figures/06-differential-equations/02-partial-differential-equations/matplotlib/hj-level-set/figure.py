from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: level-set lift u(x,t)=T(x)-t of T(x)=|x|: the zero level of u is the wavefront at time t.
fig, ax = figure(width_mm=78, height_mm=46)
style(ax)
X=np.linspace(-2,2,801)
for t,col in zip((0,.5,1),SHADES[0:1]+SHADES[1:2]+SHADES[3:4]):
    ax.plot(X,np.abs(X)-t,color=col,lw=1.4)
    ax.plot([-t,t],[0,0],'o',ms=4,color=RED,clip_on=False,zorder=5)
ax.axhline(0,color=MUTED,lw=.85,ls=':')
ax.set_xlim(-2,2); ax.set_ylim(-1.15,2); ax.set_xticks([-2,-1,0,1,2]); ax.set_xlabel('$x$'); ax.set_ylabel('$u(x,t)$')
save(fig,HERE,'figure',{'formula':'u=|x|-t, t=0,0.5,1; zeros at +-t'})
