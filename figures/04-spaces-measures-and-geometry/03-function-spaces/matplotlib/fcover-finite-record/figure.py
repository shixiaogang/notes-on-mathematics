from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f=x^2/2-1/4, g=x/2-0.35；节点 j/4；取值块 (-1,-.5],(-.5,0],(0,.5],(.5,1]；记录 2,2,2,3,3。
def f(x): return x**2/2-.25
def g(x): return x/2-.35
fig, ax = figure(width_mm=92, height_mm=56)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.1, right=.97, top=.97, bottom=.1)
nodes=np.arange(5)/4
for v in nodes:
    b=int(np.ceil((f(v)+1)/.5)); lo=-1+.5*(b-1)
    ax.fill_between([v-.045,v+.045],lo,lo+.5,color=YELLOW_FILL,lw=0)
    ax.plot([v,v],[-1,1],color=MUTED,lw=.85,ls=(0,(2,1.5)),zorder=1)
for y in [-1,-.5,0,.5,1]: ax.plot([-.03,1.03],[y,y],color=MUTED,lw=.85,zorder=1)
x=np.linspace(0,1,400)
ax.plot(x,f(x),color=BLUE,lw=1.4,zorder=3); ax.plot(x,g(x),color=GREEN,lw=1.4,zorder=3)
ax.plot(nodes,f(nodes),'o',ms=3.4,color=BLUE,mew=0,zorder=4); ax.plot(nodes,g(nodes),'o',ms=3.4,color=GREEN,mew=0,zorder=4)
ax.text(1.035,.27,'$f$',color=BLUE,ha='left',va='center'); ax.text(1.035,.13,'$g$',color=GREEN,ha='left',va='center')
ax.set_xlim(-.06,1.1); ax.set_ylim(-1,1)
ax.set_xticks(nodes); ax.set_xticklabels(['$x_1=0$','$x_2=1/4$','$x_3=1/2$','$x_4=3/4$','$x_5=1$'])
ax.set_yticks([-.75,-.25,.25,.75]); ax.set_yticklabels(['块1','块2','块3','块4']); ax.tick_params(axis='y',length=0)
for s in ('left','bottom'): ax.spines[s].set_visible(False)
ax.tick_params(axis='x',length=0)
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'f=x^2/2-1/4, g=x/2-.35, nodes j/4, blocks of length 1/2'})
