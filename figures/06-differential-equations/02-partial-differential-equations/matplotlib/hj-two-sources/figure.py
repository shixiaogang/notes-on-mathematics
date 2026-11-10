from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: arrival T=min(|x-a|,|x-b|), a=(-1,0), b=(1,0); (b) section x2=1 with other branches.
fig, axs = figure(width_mm=112, height_mm=54, ncols=2, width_ratios=[1.15,1])
ax=axs[0]; style(ax)
xs=np.linspace(-3,3,801); ys=np.linspace(-2.2,2.2,601); X,Y=np.meshgrid(xs,ys)
T1=np.hypot(X+1,Y); T2=np.hypot(X-1,Y); T=np.minimum(T1,T2)
ax.contour(X,Y,T,levels=[.5,1,1.5,2,2.5],colors=[BLUE],linewidths=1.1)
ax.plot([0,0],[-2.2,2.2],color=LINE,lw=1.7)
ax.plot([-1,1],[0,0],'o',ms=4.5,color=RED,zorder=6)
ax.set_aspect('equal'); ax.set_xlim(-3,3); ax.set_ylim(-2.2,2.2); ax.set_ylabel('$x_2$'); sub(ax,'a','$x_1$')
ax=axs[1]; style(ax)
x=np.linspace(-3,3,801); a=np.hypot(x+1,1); b=np.hypot(x-1,1)
ax.plot(x,a,color=YELLOW,lw=1.5); ax.plot(x,b,color=YELLOW,lw=1.5)
ax.plot(x,np.minimum(a,b),color=BLUE,lw=1.6)
ax.plot([0],[np.sqrt(2)],'o',ms=4.4,color=RED,zorder=6)
ax.set_xlim(-3,3); ax.set_ylim(.8,4.2); ax.set_ylabel('$T(x_1,1)$'); sub(ax,'b','$x_1$')
save(fig,HERE,'figure',{'formula':'T=min(|x-a|,|x-b|); section x2=1, kink value sqrt 2'})
