from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# L=1, k=4, h=1/4；g_s, s=(+,-,+,+) 与 g_s', s'=(+,-,-,+)，在第三格中心相差 Lh=1/4。
h=.25; L=1
def bump(x,c): return np.maximum(0,L*h/2-L*np.abs(x-c))
C=np.array([.125,.375,.625,.875])
def gs(x,s): return sum(si*bump(x,c) for si,c in zip(s,C))
s1=[1,-1,1,1]; s2=[1,-1,-1,1]
fig, ax = figure(width_mm=96, height_mm=46)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.1, right=.97, top=.97, bottom=.14)
x=np.linspace(0,1,1601)
for v in [0,.25,.5,.75,1]: ax.plot([v,v],[-.17,.17],color=MUTED,lw=.85,ls=(0,(2,1.5)),zorder=0)
ax.plot(x,gs(x,s1),color=BLUE,lw=1.4,zorder=3)
ax.plot(x,gs(x,s2),color=GREEN,lw=1.4,zorder=2)
ax.annotate('',xy=(.625,.125),xytext=(.625,-.125),arrowprops=dict(arrowstyle='<->',color=RED,lw=1.1,shrinkA=0,shrinkB=0),zorder=4)
ax.text(.635,0,'$1/4$',color=INK,ha='left',va='center')
ax.text(.555,.095,'$g_s$',color=BLUE,ha='right',va='bottom'); ax.text(.555,-.095,r"$g_{s'}$",color=GREEN,ha='right',va='top')
ax.set_xlim(0,1); ax.set_ylim(-.17,.17); ax.set_xticks([0,.25,.5,.75,1]); ax.set_xticklabels(['0','1/4','1/2','3/4','1']); ax.set_yticks([-.125,0,.125]); ax.set_yticklabels(['-1/8','0','1/8'])
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'L=1,k=4,h=1/4,bump max(0,1/8-|x-c|); s=(+,-,+,+), s\'=(+,-,-,+)'})
