from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# 贯穿本章的例子：f(x)=(x1^2+9x2^2)/2，x0=(9,1)，L=9，mu=1。
H = np.diag([1., 9.])
def f2(X, Y): return .5*(X**2 + 9*Y**2)
def grad(x): return H@x
def fv(x): return .5*x@H@x
x0 = np.array([9., 1.])

fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, .07, .99, .98, .29, .1)
X,Y = np.meshgrid(np.linspace(-1.5,10.5,600),np.linspace(-4.2,4.2,500))
for a,alpha in zip(axes,(1/9,1/5,1/4)):
    a.contour(X,Y,f2(X,Y),levels=[1,4,12,25,45],colors=[BLUE],linewidths=.7)
    P=[x0.copy()]
    for t in range(14 if alpha<.24 else 7): P.append(P[-1]-alpha*grad(P[-1]))
    P=np.array(P); a.plot(P[:,0],P[:,1],'-o',color=GREEN,lw=1.1,ms=2.6,mew=0,zorder=4,clip_on=True)
    a.plot(0,0,'o',ms=4.4,color=RED,mew=0,zorder=5)
    a.set_xlim(-1.5,10.5); a.set_ylim(-4.2,4.2); a.set_aspect('equal'); a.set_xticks([0,5,10]); a.set_yticks([-4,0,4]); a.set_xlabel('$x_1$',labelpad=1)
axes[0].set_ylabel('$x_2$',labelpad=0); axes[1].set_yticklabels([]); axes[2].set_yticklabels([])
tags(fig, axes)
save(fig, HERE, 'figure', {'alphas':[1/9,1/5,1/4],'x0':[9,1]})
