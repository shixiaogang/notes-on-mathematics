from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) 1_[0,.3] 与 1_[0,.7]；(b) 差的绝对值：面积 0.4（L1 距离），高度 1（一致距离）。
fig, axes = figure(width_mm=100, height_mm=42, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.26, wspace=.2)
a,b=axes
s,t=.3,.7
a.plot([0,s],[1.02,1.02],color=BLUE,lw=1.4); a.plot([s,1],[0,0],color=BLUE,lw=1.4,clip_on=False)
a.plot([0,t],[.98,.98],color=GREEN,lw=1.4); a.plot([t,1],[-.0,-.0],color=GREEN,lw=1.4,clip_on=False)
a.plot([s,s],[0,1.02],color=BLUE,lw=.85,ls=(0,(2,1.5))); a.plot([t,t],[0,.98],color=GREEN,lw=.85,ls=(0,(2,1.5)))
a.text(.15,1.06,r'$\mathbf{1}_{[0,0.3]}$',color=BLUE,ha='center',va='bottom')
a.text(.53,1.06,r'$\mathbf{1}_{[0,0.7]}$',color=GREEN,ha='center',va='bottom')
b.fill_between([s,t],0,1,color=RED_FILL,lw=0)
b.plot([0,s],[0,0],color=RED,lw=1.4); b.plot([s,s],[0,1],color=RED,lw=.85); b.plot([s,t],[1,1],color=RED,lw=1.4); b.plot([t,t],[0,1],color=RED,lw=.85); b.plot([t,1],[0,0],color=RED,lw=1.4)
b.text(.5,.5,'面积=0.4',ha='center',va='center')
b.annotate('',xy=(.82,1),xytext=(.82,0),arrowprops=dict(arrowstyle='<->',color=INK,lw=.85,shrinkA=0,shrinkB=0))
b.text(.85,.5,'高度=1',ha='left',va='center')
for ax in axes:
    ax.set_xlim(0,1.04); ax.set_ylim(0,1.3); ax.set_xticks([0,.3,.7,1]); ax.set_xticklabels(['0','0.3','0.7','1']); ax.set_yticks([0,1])
for ax,s_ in zip(axes,['(a)','(b)']):
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,s_,ha='center',va='bottom')
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'indicators of [0,.3],[0,.7]; |difference| has L1 norm .4 and sup norm 1'})
