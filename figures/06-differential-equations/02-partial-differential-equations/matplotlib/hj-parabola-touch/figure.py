from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: Hopf-Lax at t=pi/2 for u0=cos: the downward parabola c-(x-y)^2/(2t) rises until it touches u0.
fig, axs = figure(width_mm=112, height_mm=52, ncols=2, sharey=True)
t=np.pi/2; Y=np.linspace(-np.pi,np.pi,801); ys=np.linspace(-9,9,72001)
for ax,x0,l in zip(axs,(.6,0.),'ab'):
    style(ax); ax.plot(Y,np.cos(Y),color=BLUE,lw=1.4)
    F=np.cos(ys)+(x0-ys)**2/(2*t); c=F.min()
    ax.plot(Y,c-(x0-Y)**2/(2*t),color=PURPLE,lw=1.2)
    ax.plot([x0],[c],'o',ms=4.4,color=GREEN,zorder=6)
    touch=ys[(F-c)<1e-8]
    groups=np.split(touch,np.where(np.diff(touch)>.1)[0]+1); T=[g.mean() for g in groups]; print(x0,c,T)
    ax.plot(T,np.cos(T),'o',ms=4.4,color=RED,zorder=6)
    ax.set_xlim(-np.pi,np.pi); ax.set_ylim(-1.4,1.25); ax.set_xticks([-3,-2,-1,0,1,2,3]); sub(ax,l,'$y$')
axs[0].set_ylabel('$u_0(y)$')
save(fig,HERE,'figure',{'formula':'t=pi/2; x=.6 and x=0; c=min F'})
