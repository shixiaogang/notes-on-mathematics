from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: characteristics enter a compressive jump and leave an expansive jump (both with s=1/2).
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
def arrow(ax,x0,y0,x1,y1):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),arrowprops=dict(arrowstyle='-|>',color=LINE,lw=.7,mutation_scale=6,shrinkA=0,shrinkB=0))
ax=axs[0]; style(ax); tm=2
for x0 in np.arange(-2,0,.4):
    T=min(1-2*x0-1+1 if 0 else -2*x0,tm); ax.plot([x0,x0+T],[0,T],color=LINE,lw=.75); arrow(ax,x0+.45*T,.45*T,x0+.55*T,.55*T)
for x0 in np.arange(.4,2.01,.4):
    T=min(2*x0,tm); ax.plot([x0,x0],[0,T],color=LINE,lw=.75); arrow(ax,x0,.45*T,x0,.55*T)
ax.plot([0,1],[0,2],color=LINE,lw=2.2); ax.plot([-2,2],[0,0],color=RED,lw=2,clip_on=False)
ax.set_xlim(-2,2); ax.set_ylim(0,tm); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
for x0 in np.arange(-2,-.01,.4):
    ax.plot([x0,x0],[0,tm],color=LINE,lw=.75); arrow(ax,x0,.9,x0,1.1)
ts=np.arange(.4,2.01,.4)
for x0 in np.arange(.4,2.01,.4):
    ax.plot([x0,x0+tm],[0,tm],color=LINE,lw=.75); arrow(ax,x0+.9,.9,x0+1.1,1.1)
for t0 in ts[:-1]:
    x0=t0/2; 
    ax.plot([x0,x0-0],[t0,tm],color=MUTED,lw=.75,ls=':')
    ax.plot([x0,x0+tm-t0],[t0,tm],color=MUTED,lw=.75,ls=':')
ax.plot([0,1],[0,2],color=RED,lw=2.2); ax.plot([-2,2],[0,0],color=RED,lw=2,clip_on=False)
ax.set_xlim(-2,2); ax.set_ylim(0,tm); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'characteristics near x=t/2 for steps 1|0 and 0|1'})
