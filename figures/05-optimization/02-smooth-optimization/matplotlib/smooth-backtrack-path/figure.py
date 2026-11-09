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

fig, ax = figure(width_mm=100, height_mm=70)
panel(fig, .075, .985, .985, .135)
X,Y = np.meshgrid(np.linspace(-3,10.5,800),np.linspace(-8.8,4.2,800))
ax.contour(X,Y,f2(X,Y),levels=[2,6,14,24,45,80],colors=[BLUE],linewidths=.7)
x = x0.copy(); P=[x.copy()]; R=[]
for t in range(5):
    g = grad(x); a = 1.; fx = fv(x)
    while True:
        y = x-a*g
        if fv(y) <= fx-.1*a*g@g: break
        R.append(y.copy()); a *= .5
    x = y; P.append(x.copy())
P=np.array(P); R=np.array(R)
for r,(q) in zip(R,range(len(R))):
    pass
ax.scatter(R[:,0],R[:,1],s=15,facecolors='white',edgecolors=YELLOW,linewidths=1,zorder=4,clip_on=True)
ax.plot(P[:,0],P[:,1],'-o',color=GREEN,lw=1.2,ms=3.8,mew=0,zorder=5)
ax.plot(0,0,'o',ms=4.8,color=RED,mew=0,zorder=6)
ax.text(9.15,1.2,'$x^{(0)}$',ha='left',va='bottom'); ax.text(6.9,-1.5,'$x^{(1)}$',ha='left',va='top'); ax.text(5.1,1.8,'$x^{(2)}$',ha='center',va='bottom')
ax.set_xlim(-3,10.5); ax.set_ylim(-8.8,4.2); ax.set_aspect('equal'); ax.set_xticks([0,5,10]); ax.set_yticks([-8,-4,0,4]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=0)
save(fig, HERE, 'figure', {'c1':.1,'rho':.5,'a0':1,'P':P.tolist()})
