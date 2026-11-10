from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: integral constraint for the Neumann problem.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
X=np.linspace(0,1,300)
ax=axs[0]; style(ax)
u=lambda t:t+.5*np.exp(-np.pi**2*t)*np.cos(np.pi*X)
ax.plot(X,u(0),color=RED,lw=1.5)
for t,c in zip((.1,.4,.8,1.2),SHADES): ax.plot(X,u(t),color=c,lw=1.4)
ax.set_xlim(0,1); ax.set_xticks([0,.5,1]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax)
for C,c in zip((0,.2,.4),(BLUE,YELLOW,PURPLE)): ax.plot(X,-X**2/2+X/2+C,color=c,lw=1.5)
ax.set_xlim(0,1); ax.set_xticks([0,.5,1]); ax.set_ylim(0,.72); sub(ax,'b','$x$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'(a) t+.5 exp(-pi^2 t) cos(pi x); (b) -x^2/2+x/2+C'})
