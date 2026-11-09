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

fig, ax = figure(width_mm=104, height_mm=58)
panel(fig, .085, .985, .98, .16)
X,Y = np.meshgrid(np.linspace(-11,11,900),np.linspace(-4.2,4.2,700))
ax.contour(X,Y,f2(X,Y),levels=[2,8,18,32,45],colors=[BLUE],linewidths=[.75,.75,.75,.75,1.3])
c = np.array([8.,0.]); r = np.sqrt(2.)
th = np.linspace(0,2*np.pi,300); ax.fill(c[0]+r*np.cos(th),c[1]+r*np.sin(th),color=YELLOW_FILL,lw=0,zorder=1); ax.plot(c[0]+r*np.cos(th),c[1]+r*np.sin(th),color=YELLOW,lw=1.4,zorder=3)
ax.annotate('',xy=c,xytext=x0,arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.3,shrinkA=2,shrinkB=2,mutation_scale=8),zorder=4)
ax.plot(*x0,'o',ms=4.8,color=GREEN,mew=0,zorder=5); ax.plot(*c,'o',ms=4.8,color=GREEN,mew=0,zorder=5); ax.plot(0,0,'o',ms=4.8,color=RED,mew=0,zorder=5)
ax.text(9.25,1.15,'$x^{(0)}$',ha='left',va='bottom'); ax.text(8.15,-.12,'$x^{(1)}$',ha='left',va='top'); ax.text(.25,.15,'$x^*$',ha='left',va='bottom')
ax.set_xlim(-11,11); ax.set_ylim(-4.2,4.2); ax.set_aspect('equal'); ax.set_xticks([-10,-5,0,5,10]); ax.set_yticks([-4,0,4]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=0)
save(fig, HERE, 'figure', {'f':'(x1^2+9x2^2)/2','x0':[9,1],'L':9,'circle_center':[8,0],'radius':float(r)})
