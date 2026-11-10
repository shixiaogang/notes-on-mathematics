from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: T_eps=-eps ln(K0(r1/eps)+K0(r2/eps)) solves |grad T|^2-eps Lap T=1 away from the sources; compare level sets with T=min(r1,r2).
fig, axs = figure(width_mm=112, height_mm=52, ncols=2, sharey=True)
xs=np.linspace(-3,3,361); ys=np.linspace(-2.2,2.2,265); X,Y=np.meshgrid(xs,ys)
s=np.linspace(0,8,1601); ds=s[1]-s[0]
def logK0(z):
    z=np.maximum(z,1e-6); I=np.exp(-z[...,None]*(np.cosh(s)-1)).sum(-1)*ds
    return np.log(I)-z
r1=np.hypot(X+1,Y); r2=np.hypot(X-1,Y); T=np.minimum(r1,r2)
for ax,e,l in zip(axs,(.3,.08),'ab'):
    style(ax); Te=-e*np.logaddexp(logK0(r1/e),logK0(r2/e))
    ax.contour(X,Y,T,levels=[1,1.5,2,2.5],colors=[BLUE],linewidths=1.1)
    ax.contour(X,Y,Te,levels=[1,1.5,2,2.5],colors=[YELLOW],linewidths=1.3)
    ax.plot([-1,1],[0,0],'o',ms=4.4,color=RED,zorder=6); ax.set_aspect('equal'); ax.set_xlim(-3,3); ax.set_ylim(-2.2,2.2); sub(ax,l,'$x_1$')
axs[0].set_ylabel('$x_2$')
save(fig,HERE,'figure',{'formula':'T_eps=-eps ln(K0(r1/eps)+K0(r2/eps)), eps=.3,.08'})
