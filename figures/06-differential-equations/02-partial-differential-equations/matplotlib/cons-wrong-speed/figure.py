from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: for step (1,0) on [-1,1]x[0,1], the jump speed changes the mass ledger; only s=1/2 balances inflow 1/2.
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
for ax,s,l in zip(axs,(0,.5),'ab'):
    style(ax); x=np.array([-1,s,s,1]); u=np.array([1,1,0,0]); 
    if s>0: ax.fill_between([0,s],[0,0],[1,1],color=BLUE_FILL,lw=0)
    ax.plot([-1,0,0,1],[1,1,0,0],color=RED,lw=2.0 if s==0 else 1.4)
    ax.plot(x,u,color=BLUE,lw=1.4, ls=(0,(4,2)) if s==0 else '-')
    ax.set_xlim(-1,1); ax.set_ylim(0,1.3); sub(ax,l,'$x$')
axs[0].set_ylabel('$u$')
axs[1].text(.25,.48,'$1/2$',ha='center')
save(fig, HERE(__file__), 'figure', {'formula':'step 1|0, jump at x=st with s=0 and s=1/2 at t=1'})
