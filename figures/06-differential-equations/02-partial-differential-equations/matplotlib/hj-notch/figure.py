from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: u0=0, H=p^2/2. Notch w=0 for |x|>=t/2, w=|x|-t/2 for |x|<=t/2 satisfies the equation a.e.; (b) w_x.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
X=np.linspace(-1.5,1.5,1201)
w=lambda x,t:np.minimum(np.abs(x)-t/2,0)
ax=axs[0]; style(ax)
ax.plot(X,0*X,color=BLUE,lw=1.5)
for t,col in zip((.5,1,2),('#CDBF98',YELLOW,'#8E7D4E')): ax.plot(X,w(X,t),color=col,lw=1.5)
ax.plot([0],[-1],'o',ms=4.2,color=RED,zorder=6)
ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.2,.25); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
ax.plot([-1.5,-.5],[0,0],color=YELLOW,lw=1.6); ax.plot([-.5,-.5],[0,-1],color=LINE,lw=1.5,ls='--')
ax.plot([-.5,0],[-1,-1],color=YELLOW,lw=1.6); ax.plot([0,0],[-1,1],color=RED,lw=1.5)
ax.plot([0,.5],[1,1],color=YELLOW,lw=1.6); ax.plot([.5,.5],[1,0],color=LINE,lw=1.5,ls='--'); ax.plot([.5,1.5],[0,0],color=YELLOW,lw=1.6)
ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.3,1.3); ax.set_ylabel(r'$\partial_x u$'); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'w=min(|x|-t/2,0); (b) at t=1'})
