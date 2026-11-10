from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: particle paths of three velocities on (0,1) and the boundary parts needing data.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3, sharey=True)
kw=dict(color=LINE,lw=.8)
T=np.linspace(0,1,200)
ax=axs[0]
for x0 in np.arange(0,1,.2): ax.plot(x0+T,T,**kw)
for t0 in np.arange(.2,1,.2): ax.plot(T,t0+T,**kw)
ax.plot([0,1],[0,0],color=RED,lw=2.4,clip_on=False); ax.plot([0,0],[0,1],color=RED,lw=2.4,clip_on=False)
sub(ax,'a','$x$'); ax.set_ylabel('$t$')
ax=axs[1]
for x0 in np.array([.04,.12,.22,.34,.44,.56,.66,.78,.88,.96]): ax.plot(.5+(x0-.5)*np.exp(T),T,**kw)
ax.plot([0,1],[0,0],color=RED,lw=2.4,clip_on=False); sub(ax,'b','$x$')
ax=axs[2]
for x0 in np.arange(.1,1,.2): ax.plot(.5+(x0-.5)*np.exp(-T),T,**kw)
for t0 in (.2,.45,.7):
    for e,s in ((0,1),(1,-1)):
        ax.plot(.5+(e-.5)*np.exp(-T),t0+T,**kw)
ax.plot([0,1],[0,0],color=RED,lw=2.4,clip_on=False); ax.plot([0,0],[0,1],color=RED,lw=2.4,clip_on=False); ax.plot([1,1],[0,1],color=RED,lw=2.4,clip_on=False)
sub(ax,'c','$x$')
for ax in axs:
    style(ax); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xticks([0,.5,1]); ax.set_yticks([0,.5,1])
    ax.spines['top'].set_visible(True); ax.spines['right'].set_visible(True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'dx/dt=v with v=1, v=x-1/2, v=1/2-x'})
