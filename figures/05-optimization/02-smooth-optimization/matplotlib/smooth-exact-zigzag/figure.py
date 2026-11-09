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

fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, .08, .985, .975, .175)
X,Y = np.meshgrid(np.linspace(-.8,10.2,800),np.linspace(-2.2,2.2,500))
P=[x0.copy()]
for t in range(12):
    g=grad(P[-1]); P.append(P[-1]-(g@g)/(g@H@g)*g)
P=np.array(P)
ax.contour(X,Y,f2(X,Y),levels=sorted(fv(p) for p in P[:7]),colors=[BLUE],linewidths=.7)
ax.plot(P[:,0],P[:,1],'-o',color=YELLOW,lw=1.3,ms=3.8,mew=0,zorder=4); ax.plot(0,0,'o',ms=4.8,color=RED,mew=0,zorder=5)
ax.text(9.15,1.1,'$x^{(0)}$',ha='left',va='bottom'); ax.text(7.2,-1.0,'$x^{(1)}$',ha='center',va='top'); ax.text(5.76,.86,'$x^{(2)}$',ha='center',va='bottom')
ax.set_xlim(-.8,10.2); ax.set_ylim(-2.2,2.2); ax.set_aspect('equal'); ax.set_xticks([0,5,10]); ax.set_yticks([-2,0,2]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=0)
save(fig, HERE, 'figure', {'P':P.tolist()})
