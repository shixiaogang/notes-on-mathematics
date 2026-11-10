from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: a rod temperature field and its samples on two grids.
fig, axs = figure(width_mm=112, height_mm=44, ncols=2, sharey=True)
u = lambda x: np.sin(np.pi*x)+.4*np.sin(3*np.pi*x)
X = np.linspace(0,1,400)
for ax,N,l in zip(axs,(5,20),'ab'):
    style(ax); ax.plot(X,u(X),color=BLUE,lw=1.4)
    xs = np.arange(1,N)/N
    ax.vlines(xs,0,u(xs),color=GREEN,lw=.85)
    ax.plot(xs,u(xs),'o',ms=3.2 if N==5 else 2.4,color=GREEN)
    ax.plot([0,1],[0,0],'o',ms=3.6,color=RED)
    ax.set_xlim(-.02,1.02); ax.set_ylim(0,1.25); ax.set_xticks([0,.5,1])
    sub(ax,l,'$x$')
axs[0].set_ylabel('$u$')
axs[0].text(.5,1.08,'$h=1/5$',ha='center',color=MUTED,fontsize=7.5)
axs[1].text(.5,1.08,'$h=1/20$',ha='center',color=MUTED,fontsize=7.5)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'u=sin(pi x)+0.4 sin(3 pi x); samples at x_j=j h'})
