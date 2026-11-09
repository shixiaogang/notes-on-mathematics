from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
# (a) periodic extension of x (period 1); (b) even reflection then period 2 of x (triangle wave); (c) periodic extension of x(1-x).
fig, axes = figure(width_mm=112, height_mm=34, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.26, wspace=.22)
ax=axes[0]
for n in range(-1,2):
    ax.plot([n,n+1],[0,1],color=BLUE if n==0 else GREEN,lw=1.4)
for n in (0,1): ax.plot([n,n],[0,1],color=RED,lw=.9,dashes=(2,1.5))
ax.set_xlim(-1,2); ax.set_ylim(-.1,1.25); ax.set_xticks([-1,0,1,2]); ax.set_yticks([0,1])
ax=axes[1]
x=np.linspace(-1,2,601); y=np.abs(((x+1)%2)-1)
ax.plot(x,y,color=GREEN,lw=1.4); m=(x>=0)&(x<=1); ax.plot(x[m],y[m],color=BLUE,lw=1.4)
ax.set_xlim(-1,2); ax.set_ylim(-.1,1.25); ax.set_xticks([-1,0,1,2]); ax.set_yticks([0,1])
ax=axes[2]
x=np.linspace(-1,2,601); u=x-np.floor(x); y=u*(1-u)
ax.plot(x,y,color=GREEN,lw=1.4); m=(x>=0)&(x<=1); ax.plot(x[m],y[m],color=BLUE,lw=1.4)
ax.set_xlim(-1,2); ax.set_ylim(-.03,.34); ax.set_xticks([-1,0,1,2]); ax.set_yticks([0,.25]); ax.set_yticklabels(['0','1/4'])
for ax,s in zip(axes,'abc'):
    ax.tick_params(labelsize=7,length=2,pad=1.5)
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'periodic extension of x, even reflection of x with period 2, periodic extension of x(1-x)'})
