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

# f=x1^2-x2^2 沿三个单位方向的一元限制。
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .07, .985, .955, .25, .27)
a=axes[0]
X,Y=np.meshgrid(np.linspace(-1.2,1.2,500),np.linspace(-1.2,1.2,500)); F=X**2-Y**2
a.contour(X,Y,F,levels=[.2,.5,.9],colors=[BLUE],linewidths=.75); a.contour(X,Y,F,levels=[-.9,-.5,-.2],colors=[BLUE],linewidths=.75,linestyles=[(0,(3,2))])
ds=[((1,0),STROKE),((1/np.sqrt(2),1/np.sqrt(2)),MUTED),((0,1),RED)]
for (d,c) in ds:
    a.annotate('',xy=(d[0],d[1]),xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=c,lw=1.25,mutation_scale=8,shrinkA=0,shrinkB=0),zorder=4)
a.text(1.03,.08,'$d_1$',ha='right',va='bottom'); a.text(.8,.8,'$d_2$',ha='left',va='bottom'); a.text(.07,1.03,'$d_3$',ha='left',va='top')
a.plot([0],[0],'o',ms=4.2,color=INK,mew=0,zorder=5)
a.set_xlim(-1.2,1.2); a.set_ylim(-1.2,1.2); a.set_aspect('equal'); a.set_xticks([-1,0,1]); a.set_yticks([-1,0,1]); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=1)
b=axes[1]; t=np.linspace(-1.2,1.2,200)
for (d,c),lab,ha,yy in zip(ds,('$d_1$','$d_2$','$d_3$'),('left','left','left'),(1.2,0.08,-1.2)):
    v=(t*d[0])**2-(t*d[1])**2
    b.plot(t,v,color=c,lw=1.4)
    b.text(.74 if lab=='$d_1$' or lab=='$d_3$' else .78,(1.0 if lab=='$d_1$' else (.07 if lab=='$d_2$' else -1.03)),lab,va='bottom',ha='right')
b.set_xlim(-1.25,1.25); b.set_ylim(-1.55,1.55); b.set_xticks([-1,0,1]); b.set_yticks([-1,0,1]); b.set_xlabel('$t$',labelpad=1); b.set_ylabel('$f(t\\,d)$',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'f':'x1^2-x2^2','H':'diag(2,-2)','d':[[1,0],[.7071,.7071],[0,1]]})
