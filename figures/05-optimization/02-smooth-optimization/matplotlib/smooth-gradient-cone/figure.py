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

fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, .1, .985, .96, .27, .26)
a = axes[0]; x = np.linspace(-1.5, 5.5, 500); xb = 2.; yb = np.sin(xb)
a.fill_between(x, yb-np.abs(x-xb), yb+np.abs(x-xb), color=BLUE_FILL, lw=0)
a.plot(x, yb+np.abs(x-xb), color=MUTED, lw=.85, ls=(0,(3,1.6))); a.plot(x, yb-np.abs(x-xb), color=MUTED, lw=.85, ls=(0,(3,1.6)))
a.plot(x, np.sin(x), color=BLUE, lw=1.4); a.plot([xb],[yb],'o',ms=4.6,color=GREEN,mew=0,zorder=5)
a.text(xb+.05, yb+.22, r'$\bar{x}$', ha='left', va='bottom')
a.set_xlim(-1.5,5.5); a.set_ylim(-2.3,2.8); a.set_xticks([-1,0,2,4]); a.set_yticks([-2,0,2]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel("$f'(x)$",labelpad=1)
b = axes[1]; L = 3.; x = np.linspace(-1, 1, 1601); g = np.sign(x)*np.sqrt(np.abs(x))
b.fill_between(x, -L*np.abs(x), L*np.abs(x), color=BLUE_FILL, lw=0)
b.plot(x, L*np.abs(x), color=MUTED, lw=.85, ls=(0,(3,1.6))); b.plot(x, -L*np.abs(x), color=MUTED, lw=.85, ls=(0,(3,1.6)))
b.plot(x, g, color=BLUE, lw=1.4)
m = np.abs(x) < 1/L**2
b.plot(x[m], g[m], color=RED, lw=2.0, zorder=4); b.plot([0],[0],'o',ms=4.6,color=GREEN,mew=0,zorder=5)
b.annotate('曲线逃出', xy=(.06,.245), xytext=(.26,1.25), fontsize=7.5, color=INK, arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=2))
b.set_xlim(-1,1); b.set_ylim(-1.8,1.8); b.set_xticks([-1,0,1]); b.set_yticks([-1,0,1]); b.set_xlabel('$x$',labelpad=1); b.set_ylabel("$f'(x)$",labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'a':"f'=sin x, L=1, cone at x=2",'b':"f'=sign(x)|x|^(1/2), L=3 cone at 0, curve outside for |x|<1/9"})
