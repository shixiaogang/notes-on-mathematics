from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: jump and fan candidates for step (0,1) at t=1 hold the same mass; signed difference has zero integral.
fig, ax = figure(width_mm=90, height_mm=44); style(ax)
x=np.linspace(-.5,1.6,800); fan=np.clip(x,0,1); jump=(x>.5)*1.0
ax.fill_between(x,fan,jump,color=BLUE_FILL,lw=0)
ax.plot(x,fan,color=BLUE,lw=1.4); ax.plot([-.5,.5,.5,1.6],[0,0,1,1],color=YELLOW,lw=1.6)
ax.text(.33,.09,'$1/8$',ha='center'); ax.text(.67,.84,'$1/8$',ha='center')
ax.set_xlim(-.5,1.6); ax.set_ylim(0,1.15); ax.set_xlabel('$x$'); ax.set_ylabel('$u(x,1)$')
save(fig, HERE(__file__), 'figure', {'formula':'x clipped to [0,1] versus H(x-1/2)'})
