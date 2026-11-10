from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: multiplying Burgers by u keeps smooth solutions but changes the conserved quantity and the jump speed.
fig, axs = figure(width_mm=112, height_mm=44, ncols=2)
ax=axs[0]; style(ax); ax.plot([0,1],[0,2],color=BLUE,lw=1.9); ax.plot([0,4/3],[0,2],color=YELLOW,lw=1.9)
ax.text(.62,1.5,'$s=1/2$',color=BLUE,ha='right'); ax.text(1.16,1.05,'$s=2/3$',color=YELLOW,ha='left')
ax.plot([-1.5,2],[0,0],color=RED,lw=2,clip_on=False); ax.set_xlim(-1.5,2); ax.set_ylim(0,2); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.plot([-1,1,1,2],[1,1,0,0],color=BLUE,lw=1.5); ax.plot([-1,4/3,4/3,2],[1,1,0,0],color=YELLOW,lw=1.5)
ax.set_xlim(-1,2); ax.set_ylim(0,1.2); ax.set_ylabel('$u(x,2)$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'jump speeds of u and u^2/2 conservation, step 1|0'})
