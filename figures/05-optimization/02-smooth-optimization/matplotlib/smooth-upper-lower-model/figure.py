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

fig, ax = figure(width_mm=100, height_mm=58)
panel(fig, .115, .985, .97, .15)
x = np.linspace(-1.2, 5.2, 700); x0_ = 2.; f0 = 1-np.cos(x0_); s = np.sin(x0_)
up = f0+s*(x-x0_)+.5*(x-x0_)**2; lo = f0+s*(x-x0_)-.5*(x-x0_)**2
ax.plot(x, up, color=YELLOW, lw=1.4); ax.plot(x, lo, color=PURPLE, lw=1.2, ls=(0,(3,1.6))); ax.plot(x, 1-np.cos(x), color=BLUE, lw=1.4)
x1 = x0_-s
ax.plot([x0_],[f0],'o',ms=4.8,color=GREEN,mew=0,zorder=6); ax.plot([x1],[f0-.5*s*s],'o',ms=4.6,mfc='white',mec=YELLOW,mew=1.0,zorder=6); ax.plot([x1],[1-np.cos(x1)],'o',ms=4.8,color=GREEN,mew=0,zorder=6)
ax.plot([x1,x1],[1-np.cos(x1),f0-.5*s*s],color=MUTED,lw=.85,ls=':')
ax.text(x0_,f0-.3,'$x^{(0)}$',ha='center',va='top'); ax.text(.84,.72,'$x^{(1)}$',ha='center',va='bottom')
ax.text(-.65,2.75,'上界',color=INK,ha='left'); ax.text(3.7,-2.3,'下界',color=INK,ha='left'); ax.text(4.0,1.72,'$f$',color=INK,ha='left')
ax.set_xlim(-1.2,5.2); ax.set_ylim(-3,3.4); ax.set_xticks([-1,0,1,2,3,4,5]); ax.set_yticks([-2,0,2]); ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel('目标',labelpad=1)
save(fig, HERE, 'figure', {'f':'1-cos x','L':1,'x0':2,'x1':x1})
