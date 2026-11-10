from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: chord condition. For u_- > u_+ the graph must lie below the chord; for u_- < u_+ above; convex flux passes only the first.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
u=np.linspace(-.3,1.3,300); F=u**2/2; m=np.linspace(0,1,200)
for ax,col,l in zip(axs,(BLUE_FILL,RED_FILL),'ab'):
    style(ax); ax.fill_between(m,m**2/2,m/2,color=col,lw=0); ax.plot(u,F,color=BLUE,lw=1.4); ax.plot([0,1],[0,.5],color=LINE if l=='a' else RED,lw=2)
    ax.plot([0,1],[0,.5],'o',ms=4,color=RED,zorder=5); ax.set_xlim(-.3,1.3); ax.set_ylim(-.12,.9); sub(ax,l,'$u$')
axs[0].set_ylabel('$F(u)$')
axs[0].text(1.03,.53,'$u_-$',va='bottom',ha='left'); axs[0].text(.05,-.03,'$u_+$',va='top')
axs[1].text(1.03,.53,'$u_+$',va='bottom',ha='left'); axs[1].text(.05,-.03,'$u_-$',va='top')
save(fig, HERE(__file__), 'figure', {'formula':'F=u^2/2 with chord on [0,1]'})
