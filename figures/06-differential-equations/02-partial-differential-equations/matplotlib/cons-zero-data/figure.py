from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: zero initial data admits the nonzero weak solution with three jumps, b=1.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
ax=axs[0]; style(ax); ax.plot([0,0],[0,1.5],color=RED,lw=2.0); ax.plot([0,-.75],[0,1.5],color=LINE,lw=2.0); ax.plot([0,.75],[0,1.5],color=LINE,lw=2.0)
ax.plot([-1.5,1.5],[0,0],color=RED,lw=2,clip_on=False)
ax.text(-.32,1.05,'$-1$',ha='center'); ax.text(.33,1.05,'$+1$',ha='center'); ax.text(-1.05,.8,'$0$',ha='center'); ax.text(1.05,.8,'$0$',ha='center')
ax.set_xlim(-1.5,1.5); ax.set_ylim(0,1.5); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.axhline(0,color=MUTED,lw=.7)
ax.plot([-1.5,-.5,-.5,0,0,.5,.5,1.5],[0,0,-1,-1,1,1,0,0],color=BLUE,lw=1.4)
ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.3,1.3); ax.set_ylabel('$u(x,1)$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'0|-b|b|0 with b=1'})
