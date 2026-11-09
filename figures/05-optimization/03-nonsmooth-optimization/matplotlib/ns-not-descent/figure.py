from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# f(x)=|x1|+2|x2|，x=(1,0)，g=(1,2)，alpha=0.2：目标上升，距离下降。
fig,A=figure(width_mm=84,height_mm=62)
panel(fig,.09,.98,.98,.13)
X,Y=np.meshgrid(np.linspace(-1.6,1.6,801),np.linspace(-1.1,1.1,801))
A.contour(X,Y,abs(X)+2*abs(Y),levels=[.5,1,1.6],colors=[BLUE],linewidths=.8)
th=np.linspace(0,2*np.pi,400);r=1.;r2=np.sqrt(.8)
A.plot(r*np.cos(th),r*np.sin(th),color=MUTED,lw=.85,ls=':');A.plot(r2*np.cos(th),r2*np.sin(th),color=MUTED,lw=.85,ls=':')
a=.2;P=np.array([1,0.]);Q=P-a*np.array([1,2.])
A.annotate('',xy=Q,xytext=P,arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.4,shrinkA=0,shrinkB=0,mutation_scale=9))
A.plot(*P,'o',color=GREEN,ms=4.4,mew=0,zorder=6);A.plot(*Q,'o',color=GREEN,ms=4.4,mew=0,zorder=6)
opt(A)
A.text(1.04,.06,'$x$',color=INK);A.text(.83,-.53,'$x^{+}$',color=INK);A.text(-.2,.1,'$x^{*}$',color=INK)

A.set_xlim(-1.6,1.6);A.set_ylim(-1.1,1.1);A.set_aspect('equal');A.set_xticks([-1,0,1]);A.set_yticks([-1,0,1]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=0)
save(fig,HERE,'figure',{'f':'|x1|+2|x2|','x':[1,0],'g':[1,2],'alpha':.2})
