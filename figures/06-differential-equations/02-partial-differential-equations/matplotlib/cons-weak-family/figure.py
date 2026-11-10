from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: a one-parameter family of weak solutions for the step (0,1), alpha=1, 1/2, 0.
fig, axs = figure(width_mm=112, height_mm=76, nrows=2, ncols=3, sharex=True, gridspec_kw={'height_ratios':[1.5,1]})
x=np.linspace(-.6,1.5,1200)
def prof(x,a):
    return np.where(x<a/2,0.0,np.where(x<a,a,np.where(x<1,x,1.0)))
for j,(a,l) in enumerate(zip((1,.5,0),'abc')):
    ax=axs[0,j]; style(ax)
    if a>0: ax.plot([0,a/2],[0,1],color=RED,lw=2.0)
    for k in np.linspace(a,1,6 if a<1 else 1):
        if k>a or a==0: ax.plot([0,k],[0,1],color=LINE,lw=.75)
    if a==0: ax.plot([0,0],[0,1],color=LINE,lw=.75)
    ax.set_xlim(-.6,1.5); ax.set_ylim(0,1); ax.tick_params(labelbottom=False)
    ax=axs[1,j]; style(ax); u=prof(x,a)
    # draw jumps vertically
    pts=np.r_[x]; ax.plot(pts,u,color=BLUE,lw=1.4)
    ax.set_xlim(-.6,1.5); ax.set_ylim(0,1.2); sub(ax,l,'$x$')
axs[0,0].set_ylabel('$t$'); axs[1,0].set_ylabel('$u(x,1)$')
save(fig, HERE(__file__), 'figure', {'formula':'u=0|a|x/t|1 with jump x=a t/2'})
