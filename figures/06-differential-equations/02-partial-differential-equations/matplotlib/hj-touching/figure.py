from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: which smooth test graphs can touch a function: smooth point, concave kink, convex kink.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3, sharey=True)
X=np.linspace(-1,1,401)
ax=axs[0]; style(ax); u=.6-.5*X**2
ax.plot(X,u,color=BLUE,lw=1.4)
ax.plot(X,.6-.5*X**2+.5*X**2*1.6,color=PURPLE,lw=1.1); ax.plot(X,.6-.5*X**2-.9*X**2,color=PURPLE,lw=1.1)
ax.plot([0],[.6],'o',ms=4.2,color=RED,zorder=6); sub(ax,'a','$x$'); ax.set_ylabel('$u,\\ \\varphi$')
ax=axs[1]; style(ax); u=.6-np.abs(X)*.6
ax.plot(X,u,color=BLUE,lw=1.4)
for s in (-.35,0,.35): ax.plot(X,.6+s*X+.25*X**2,color=PURPLE,lw=1.1)
ax.plot([0],[.6],'o',ms=4.2,color=RED,zorder=6); sub(ax,'b','$x$')
ax=axs[2]; style(ax); u=.6*np.abs(X)
ax.plot(X,u,color=BLUE,lw=1.4)
for s in (-.35,0,.35): ax.plot(X,s*X-.25*X**2,color=PURPLE,lw=1.1)
ax.plot([0],[0],'o',ms=4.2,color=RED,zorder=6); sub(ax,'c','$x$')
for ax in axs: ax.set_xlim(-1,1); ax.set_ylim(-.65,1.1); ax.set_xticks([-1,0,1])
save(fig,HERE,'figure',{'formula':'smooth .6-.5x^2; kinks .6-.6|x|, .6|x|; test parabolas'})
