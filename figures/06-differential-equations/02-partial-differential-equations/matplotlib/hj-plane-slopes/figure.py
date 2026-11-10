from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: H(p)=p^2/2; the plane solution u=p x-t H(p) falls at rate H(p), independent of position.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax=axs[0]; style(ax)
P=np.linspace(-2.2,2.2,401); ax.plot(P,P**2/2,color=BLUE,lw=1.4)
cols=[YELLOW,GREEN,PURPLE]; ps=[0,1,2]
for p,col in zip(ps,cols):
    ax.plot([p],[p*p/2],'o',ms=4.2,color=col,zorder=5,clip_on=False)
    ax.plot([p,p],[0,p*p/2],color=col,lw=.85,ls=':')
ax.set_xlim(-2.2,2.2); ax.set_ylim(0,2.5); ax.set_xticks([-2,-1,0,1,2]); ax.set_ylabel('$H(p)$'); sub(ax,'a','$p$')
ax=axs[1]; style(ax)
X=np.linspace(-.5,1.5,5)
for p,col in zip(ps,cols):
    ax.plot(X,p*X,color=col,lw=.95,ls='--')
    ax.plot(X,p*X-p*p/2,color=col,lw=1.5)
ax.set_xlim(-.5,1.5); ax.set_ylim(-3.2,3.2); ax.set_xticks([-.5,0,.5,1,1.5]); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'u=p x-t p^2/2, p=0,1,2; dashed t=0, solid t=1'})
