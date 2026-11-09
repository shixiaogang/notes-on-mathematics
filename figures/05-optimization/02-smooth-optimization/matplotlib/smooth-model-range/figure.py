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
panel(fig, .105, .985, .96, .27, .28)
m = lambda x: 1+4*(x-1)+6*(x-1)**2
a = axes[0]; x = np.linspace(-3.8, 1.6, 700)
a.axvspan(-3,1,color=GREEN_FILL,lw=0); a.plot(x,m(x),color=YELLOW,lw=1.4); a.plot(x,x**4,color=BLUE,lw=1.4)
a.plot([1],[1],'o',ms=4.6,color=GREEN,mew=0,zorder=5); a.plot([-3],[81],'o',ms=4.2,color=RED,mew=0,zorder=5)
a.text(1.0,18,'$x^{(0)}$',ha='center',va='bottom'); a.text(-2.9,84,'$x=-3$',ha='left',va='bottom')
a.text(-.1,60,'上界',ha='left',va='center'); a.text(-3.72,155,'$f$',ha='left')
a.set_xlim(-3.8,1.6); a.set_ylim(-5,190); a.set_xticks([-3,-2,-1,0,1]); a.set_yticks([0,50,100,150]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('目标',labelpad=1)
b = axes[1]; x = np.linspace(.75, 1.25, 400)
b.axvspan(.75,1,color=GREEN_FILL,lw=0); b.axvspan(1,1.25,color=RED_FILL,lw=0)
b.plot(x,x**4,color=BLUE,lw=1.4); b.plot(x,m(x),color=YELLOW,lw=1.4,ls=(0,(3,1.6))); b.plot([1],[1],'o',ms=4.6,color=GREEN,mew=0,zorder=5)
b.text(.79,.95,'盖得住',ha='left',va='bottom'); b.text(1.04,.68,'盖不住',ha='left',va='bottom')
b.set_xlim(.75,1.25); b.set_ylim(.25,2.6); b.set_xticks([.8,1,1.2]); b.set_xticklabels(['0.8','1','1.2']); b.set_yticks([.5,1,1.5,2,2.5]); b.set_yticklabels(['0.5','1','1.5','2','2.5']); b.set_xlabel('$x$',labelpad=1); b.set_ylabel('目标',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'f':'x^4','x0':1,'L':12,'upper':'1+4(x-1)+6(x-1)^2','valid':'[-3,1]'})
