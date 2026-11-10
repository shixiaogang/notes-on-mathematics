from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: H=p^2/2, u0=cos x: characteristics x=y-t sin y. (a) all lines, envelope x=y-tan y, t=1/cos y.
# (b) lines stopped at the kink x=0, which they reach at t=y/sin y.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2, sharey=True)
Tm=2.2; ys=np.linspace(-3,3,25)
ax=axs[0]; style(ax)
t=np.linspace(0,Tm,50)
for y in ys: ax.plot(y-t*np.sin(y),t,color=BLUE,lw=.85)
th=np.linspace(-np.arccos(1/Tm),np.arccos(1/Tm),301)
ax.plot(th-np.tan(th),1/np.cos(th),color=LINE,lw=1.5)
ax.plot([0],[1],'o',ms=4.4,color=RED,zorder=6)
ax.set_xlim(-np.pi,np.pi); ax.set_ylim(0,Tm); ax.set_xticks([-3,-2,-1,0,1,2,3]); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
for y in ys:
    if abs(y)<1e-9: end=Tm
    else: end=min(Tm,y/np.sin(y))
    t=np.linspace(0,end,50); ax.plot(y-t*np.sin(y),t,color=BLUE,lw=.85)
ax.plot([0,0],[1,Tm],color=LINE,lw=1.7)
ax.plot([0],[1],'o',ms=4.4,color=RED,zorder=6)
ax.set_xlim(-np.pi,np.pi); ax.set_xticks([-3,-2,-1,0,1,2,3]); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'x=y-t sin y; envelope x=y-tan y, t=1/cos y; kink x=0, t>=1'})
