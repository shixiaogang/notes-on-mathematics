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

xs=[3.]
for t in range(9): xs.append(xs[-1]-np.sin(xs[-1]))
xs=np.array(xs); fs=1-np.cos(xs); gs=np.abs(np.sin(xs))
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, .09, .985, .96, .27, .26)
a=axes[0]; x=np.linspace(-.5,3.6,400); a.plot(x,1-np.cos(x),color=BLUE,lw=1.4); a.plot(xs,fs,'o',ms=3.8,color=GREEN,mew=0,zorder=4); a.plot(xs,fs,color=GREEN,lw=.85)
a.plot([0],[0],'o',ms=4.6,color=RED,mew=0,zorder=5); a.text(3.02,2.1,'$x^{(0)}$',ha='center',va='bottom')
a.set_xlim(-.5,3.6); a.set_ylim(-.2,2.5); a.set_xticks([0,1,2,3]); a.set_yticks([0,1,2]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f(x)=1-\\cos x$',labelpad=1)
b=axes[1]; t=np.arange(len(xs))
b.plot(t,fs,'-o',color=BLUE,lw=1.3,ms=3.2,mew=0); b.plot(t,gs,'-o',color=GREEN,lw=1.3,ms=3.2,mew=0)
b.text(1.0,2.1,'$f$',ha='center',va='bottom'); b.text(2.8,.45,r'$\vert f^{\prime}\vert$',ha='right',va='top')
b.set_xlim(-.4,9.4); b.set_ylim(-.1,2.45); b.set_xticks([0,3,6,9]); b.set_yticks([0,1,2]); b.set_xlabel('迭代',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'x0':3,'alpha':1,'x':xs.tolist(),'f':fs.tolist(),'g':gs.tolist()})
