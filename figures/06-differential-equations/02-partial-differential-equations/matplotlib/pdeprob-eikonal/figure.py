from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: |u'|=1 on (-1,1), u(+-1)=0: many a.e. solutions; vanishing viscosity selects 1-|x|.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
X=np.linspace(-1,1,1601)
ax=axs[0]; style(ax)
tri=lambda n:(1/(2**n))*(1-np.abs(((X+1)*2**n)%2-1))
ax.plot(X,1-np.abs(X),color=BLUE,lw=1.4)
ax.plot(X,tri(1),color=YELLOW,lw=1.6)
ax.plot(X,-tri(2),color=PURPLE,lw=1.4)
ax.plot([-1,1],[0,0],'o',ms=3.8,color=RED,clip_on=False,zorder=5)
ax.set_xlim(-1,1); ax.set_ylim(-.35,1.08); ax.set_xticks([-1,0,1]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
ax.plot(X,1-np.abs(X),color=BLUE,lw=1.4)
lc=lambda z:np.logaddexp(z,-z)-np.log(2)
for e,c in zip((.3,.1,.03),(PURPLE,YELLOW,GREEN)):
    ax.plot(X,e*(lc(np.full_like(X,1/e))-lc(X/e)),color=c,lw=1.4)
ax.plot([-1,1],[0,0],'o',ms=3.8,color=RED,clip_on=False,zorder=5)
ax.set_xlim(-1,1); ax.set_xticks([-1,0,1]); sub(ax,'b','$x$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'u_eps=eps(ln cosh(1/eps)-ln cosh(x/eps)), eps=.3,.1,.03'})
