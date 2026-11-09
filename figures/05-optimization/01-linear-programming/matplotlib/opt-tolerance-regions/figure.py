from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')

# gamma=0.1 时三种容差集合：目标差、解距离、梯度都不超过 0.1（位移 d=x-x*）。
g=.1; H=np.array([[1+g,1],[1,1+g]]); eps=.1
fig, ax = figure(width_mm=86, height_mm=74)
X,Y=np.meshgrid(np.linspace(-1.35,1.35,900),np.linspace(-1.35,1.35,900))
P=np.stack([X,Y],-1)
Q=.5*(P[...,0]*(H[0,0]*X+H[0,1]*Y)+P[...,1]*(H[1,0]*X+H[1,1]*Y))
Gr=np.hypot(H[0,0]*X+H[0,1]*Y,H[1,0]*X+H[1,1]*Y); D=np.hypot(X,Y)
ax.contourf(X,Y,Q,levels=[-1,eps],colors=[BLUE_FILL])
ax.contour(X,Y,Q,levels=[eps],colors=[BLUE],linewidths=1.3)
ax.contour(X,Y,Gr,levels=[eps],colors=[GREEN],linewidths=1.3)
ax.contour(X,Y,D,levels=[eps],colors=[STROKE],linewidths=1.3)
ax.plot([0],[0],'o',ms=3,color=RED,mew=0,zorder=6)
ax.text(.86,-.40,'目标差',ha='left',va='center',color=INK)
ax.annotate('梯度',xy=(-.5,.53),xytext=(-1.1,1.0),color=INK,arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
ax.annotate('解距离',xy=(.06,.09),xytext=(.42,.82),color=INK,arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
ax.set_xlim(-1.35,1.35); ax.set_ylim(-1.35,1.35); ax.set_aspect('equal'); ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1])
ax.set_xlabel('$x_1-x_1^*$',labelpad=1); ax.set_ylabel('$x_2-x_2^*$',labelpad=1)
save(fig, HERE, 'figure', {'H':H.tolist(),'eps':eps,'gap_axes':[float(np.sqrt(2*eps/g)),float(np.sqrt(2*eps/(2+g)))],'grad_axes':[eps/g,eps/(2+g)]})
