from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: Burgers speed equals height, so higher parts of the profile move further in time 1.
fig, ax = figure(width_mm=96, height_mm=46); style(ax)
x=np.linspace(-4,7,1500); ax.plot(x,bump(x),color=RED,lw=1.4)
X=x+1*bump(x); ax.plot(X,bump(x),color=BLUE,lw=1.4)
for x0 in (-2,-1,0,.6,1.2,2,3):
    u=bump(x0); ax.plot([x0],[u],'o',ms=3,color=RED,zorder=4)
    ax.annotate('',xy=(x0+u,u),xytext=(x0,u),arrowprops=dict(arrowstyle='-|>',color=LINE,lw=.9,mutation_scale=7,shrinkA=2,shrinkB=0))
ax.text(-2.7,.42,'$t=0$',color=RED); ax.text(2.45,.47,'$t=1$',color=BLUE)
ax.set_xlim(-4,6.5); ax.set_ylim(0,1.12); ax.set_xlabel('$x$'); ax.set_ylabel('$u$')
save(fig, HERE(__file__), 'figure', {'formula':'u0=1/(1+x^2); point (x0,u0) moves to (x0+u0,u0) at t=1'})
