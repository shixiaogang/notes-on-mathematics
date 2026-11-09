from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 五个城市、曼哈顿距离的开放路径；A(1,4),B(2,4),C(3,5),D(2,5),E(5,0)
P={'A':(1,4),'B':(2,4),'C':(3,5),'D':(2,5),'E':(5,0)}
def L(o): return sum(abs(P[a][0]-P[b][0])+abs(P[a][1]-P[b][1]) for a,b in zip(o,o[1:]))
fig, axes = figure(width_mm=96, height_mm=60, ncols=2)
panel(fig, .07, .985, .975, .21, .2)
off={'A':(-.22,-.05),'B':(.05,-.42),'C':(.22,.05),'D':(-.05,.22),'E':(.25,.05)}
for ax,o in zip(axes,('ABECD','ABDCE')):
    for u,v in zip(o,o[1:]):
        (x0,y0),(x1,y1)=P[u],P[v]; ax.plot([x0,x1,x1],[y0,y0,y1],color=GREEN,lw=1.4,solid_joinstyle='miter')
    for k,(x,y) in P.items():
        ax.plot([x],[y],'o',ms=4.4,color=BLUE if k!='E' else BLUE,mew=0,zorder=5); ax.text(x+off[k][0],y+off[k][1],k,ha='center',va='center',fontsize=8)
    ax.set_xlim(.2,5.8); ax.set_ylim(-.6,5.9); ax.set_aspect('equal'); ax.set_xticks(range(1,6)); ax.set_yticks(range(0,6)); ax.set_xlabel('$u$',labelpad=1)
axes[0].set_ylabel('$v$',labelpad=0); tags(fig,axes); print(L('ABECD'),L('ABDCE'))
save(fig,HERE,'figure',{'cities':P,'orders':['ABECD','ABDCE'],'lengths':[L('ABECD'),L('ABDCE')]})
