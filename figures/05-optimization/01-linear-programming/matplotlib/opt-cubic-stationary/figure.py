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

# f=x^3-3x+y^2：(1,0) 局部极小，(-1,0) 鞍点，无下界。
fig, ax = figure(width_mm=92, height_mm=66)
X,Y=np.meshgrid(np.linspace(-2.6,2.3,600),np.linspace(-2.2,2.2,600))
F=X**3-3*X+Y**2
ax.contour(X,Y,F,levels=[-1.7,-1,0,1,2,3,4,6],colors=[BLUE],linewidths=.75)
ax.contour(X,Y,F,levels=[2],colors=[BLUE],linewidths=1.25)
ax.plot([1],[0],'o',ms=4.8,color=YELLOW,mew=0,zorder=5); ax.plot([-1],[0],'o',ms=4.4,mfc='white',mec=INK,mew=1,zorder=5)
ax.text(1.0,-.2,'局部极小',ha='center',va='top',bbox=dict(fc='white',ec='none',pad=.5)); ax.text(-1.0,-.2,'鞍点',ha='center',va='top',bbox=dict(fc='white',ec='none',pad=.5))
ax.annotate('',xy=(-2.55,1.72),xytext=(-1.75,1.72),arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.0,mutation_scale=8,shrinkA=0,shrinkB=0))
ax.text(-1.68,1.72,r'$f\to-\infty$',va='center',ha='left',color=INK,bbox=dict(fc='white',ec='none',pad=.6))
ax.set_xlim(-2.6,2.3); ax.set_ylim(-2.2,2.2); ax.set_aspect('equal'); ax.set_xticks([-2,-1,0,1,2]); ax.set_yticks([-2,-1,0,1,2]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=2)
save(fig, HERE, 'figure', {'f':'x1^3-3x1+x2^2','stationary':[[1,0],[-1,0]]})
