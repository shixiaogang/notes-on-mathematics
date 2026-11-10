from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: -u''=f on (0,1), f=4 on (1/4,3/4), u(0)=u(1)=0.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
X=np.linspace(0,1,801)
f=lambda x:4.0*((x>.25)&(x<.75))
up=lambda x:np.where(x<.25,1.0,np.where(x>.75,-1.0,-4*(x-.5)))
u=lambda x:np.where(x<.25,x,np.where(x>.75,1-x,.375-2*(x-.5)**2))
ax=axs[0]; ax.plot([0,.25],[0,0],color=RED,lw=1.6); ax.plot([.25,.75],[4,4],color=RED,lw=1.6); ax.plot([.75,1],[0,0],color=RED,lw=1.6)
ax.plot([.25,.25],[0,4],color=RED,lw=.85,ls=':'); ax.plot([.75,.75],[0,4],color=RED,lw=.85,ls=':')
ax.set_ylim(-.2,4.6); ax.set_ylabel('$f$'); sub(ax,'a','$x$')
ax=axs[1]; ax.axhline(0,color=GRID,lw=.85); ax.plot(X,up(X),color=BLUE,lw=1.4); ax.set_ylim(-1.2,1.2); ax.set_ylabel("$u'$"); sub(ax,'b','$x$')
ax=axs[2]; ax.plot(X,u(X),color=BLUE,lw=1.4); ax.plot([.25,.75],[.25,.25],'o',ms=3,color=PURPLE); ax.set_ylim(0,.42); ax.set_ylabel('$u$'); sub(ax,'c','$x$')
for ax in axs: style(ax); ax.set_xlim(0,1); ax.set_xticks([0,.25,.75,1]); ax.set_xticklabels(['0','1/4','3/4','1'])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'piecewise solution, u(1/2)=3/8'})
