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

def fixed(a, n=120):
    x=x0.copy(); E=[fv(x)]; C=[1]
    for t in range(n):
        x=x-a*grad(x); E.append(fv(x)); C.append(C[-1]+1)
    return E,C
def exact(n=120):
    x=x0.copy(); E=[fv(x)]; C=[1]
    for t in range(n):
        g=grad(x); x=x-(g@g)/(g@H@g)*g; E.append(fv(x)); C.append(C[-1]+2)
    return E,C
def bt(n=120):
    x=x0.copy(); E=[fv(x)]; C=[2]
    for t in range(n):
        g=grad(x); a=1.; fx=fv(x); k=0
        while True:
            k+=1; y=x-a*g
            if fv(y)<=fx-.1*a*g@g: break
            a*=.5
        x=y; E.append(fv(x)); C.append(C[-1]+k+1)
    return E,C
S=[(fixed(1/9),YELLOW,'-'),(fixed(.2),PURPLE,'-'),(exact(),STROKE,(0,(3,1.6))),(bt(),GREEN,'-')]
fig, axes = figure(width_mm=112, height_mm=58, ncols=2, sharey=True)
panel(fig, .105, .985, .965, .25, .09)
xr=[85,170]
for ax,use_c in zip(axes,(False,True)):
    for (E,C),c,ls in S:
        xx=C if use_c else range(len(E))
        ax.semilogy(xx,E,color=c,lw=1.4 if c!=STROKE else 1.0,ls=ls)
    ax.axhline(1e-6,color=MUTED,lw=.85,ls=':')
    ax.set_ylim(1e-7,1e2); ax.set_yticks([1e-6,1e-3,1])
axes[0].set_xlim(0,85); axes[1].set_xlim(0,130)
axes[0].set_xlabel('外层迭代数',labelpad=1); axes[1].set_xlabel('函数、梯度与矩阵向量积总次数',labelpad=1); axes[0].set_ylabel('目标差',labelpad=1)
from matplotlib.lines import Line2D
axes[0].legend(handles=[Line2D([],[],color=GREEN,lw=1.4,label='回溯'),Line2D([],[],color=YELLOW,lw=1.4,label='固定 1/L'),Line2D([],[],color=PURPLE,lw=1.4,label='固定 0.2'),Line2D([],[],color=STROKE,lw=1.0,ls=(0,(3,1.6)),label='精确线搜索')],loc='upper right',handlelength=1.8,labelspacing=.25,borderaxespad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'cost':'N_f+N_g+N_Hd; fixed no f; exact one Hd per iteration'})
