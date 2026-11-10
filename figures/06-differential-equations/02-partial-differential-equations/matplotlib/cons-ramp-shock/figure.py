from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: the ramp datum: characteristics focus at (1,1), then a shock x=(1+t)/2 absorbs them.
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
ax=axs[0]; style(ax); tm=3
for x0 in np.arange(-3,3.01,.25):
    v=float(ramp(np.array(x0)))
    if x0<0: T=(1-x0)*2/(2)  # hits x=(1+t)/2: x0+t=(1+t)/2
    if x0<0: T=1-2*x0
    elif x0<=1: T=1.0
    else: T=2*x0-1
    T=min(T,tm); ax.plot([x0,x0+v*T],[0,T],color=LINE,lw=.7)
ax.plot([1,1+(tm-1)/2],[1,tm],color=LINE,lw=2.2); ax.plot([1],[1],'o',ms=4.5,color=RED,zorder=5)
ax.plot([-2,3],[0,0],color=RED,lw=2,clip_on=False); ax.set_xlim(-2,3); ax.set_ylim(0,tm); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); x=np.linspace(-1,3.2,1500)
ax.plot(x,ramp(x),color=RED,lw=1.4)
ax.plot(x,np.where(x<.5,1.0,np.where(x>1,0.0,(1-x)/.5)),color=SHADES[0],lw=1.4)
ax.plot([-1,1,1,3.2],[1,1,0,0],color=SHADES[1],lw=1.4)
ax.plot([-1,1.5,1.5,3.2],[1,1,0,0],color=SHADES[2],lw=1.4)
ax.plot([-1,2.5,2.5,3.2],[1,1,0,0],color=SHADES[3],lw=1.4)
for xx,txt in ((0.12,'$0$'),(.82,'$0.5$'),(1.0,'$1$'),(1.5,'$2$'),(2.5,'$4$')):
    pass
ax.text(-.75,.55,'$t=0$',color=RED); ax.text(1.05,.86,'$1$',color=SHADES[1]); ax.text(1.55,.86,'$2$',color=SHADES[2]); ax.text(2.55,.86,'$4$',color=SHADES[3])
ax.set_xlim(-1,3.2); ax.set_ylim(0,1.15); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'ramp; shock x=(1+t)/2 for t>=1'})
