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

fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .09, .985, .96, .27, .3)
a = axes[0]; x = np.linspace(-.25,2.2,400); a.plot(x,x**2,color=BLUE,lw=1.4)
P = 1+2.**(-np.arange(0,9)); a.plot(P,P**2,'-o',color=GREEN,lw=1.0,ms=3.6,mew=0,zorder=4)
a.plot([1],[1],'o',ms=5,mfc='white',mec=RED,mew=1.1,zorder=5); a.plot([0],[0],'o',ms=4.8,color=RED,mew=0,zorder=5)
a.text(1.0,.62,'$x=1$',ha='center',va='top'); a.text(.05,.25,'$x^*$',ha='left',va='bottom'); a.text(1.82,3.95,'$x^{(0)}$',ha='right',va='center')
a.set_xlim(-.25,2.2); a.set_ylim(-.2,4.6); a.set_xticks([0,1,2]); a.set_yticks([0,2,4]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f(x)=x^2$',labelpad=1)
b = axes[1]; t = np.arange(0,11); r = (2+2.**(-t))/(2+2.**(1-t))
b.axhline(.9,color=STROKE,lw=.95,ls=(0,(3,1.6))); b.text(10,.885,'$c_2=0.9$',ha='right',va='top')
b.plot(t[r<=.9+1e-12],r[r<=.9+1e-12],'o',ms=4,color=GREEN,mew=0,zorder=5); b.plot(t[r>.9+1e-12],r[r>.9+1e-12],'o',ms=4,color=RED,mew=0,zorder=5); b.plot(t,r,color=MUTED,lw=.85)
b.set_xlim(-.4,10.4); b.set_ylim(.7,1.03); b.set_xticks([0,2,4,6,8,10]); b.set_yticks([.7,.8,.9,1]); b.set_yticklabels(['0.7','0.8','0.9','1']); b.set_xlabel('$t$',labelpad=1); b.set_ylabel('新旧方向导数之比',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'x_t':'1+2^-t','ratio':'(2+2^-t)/(2+2^(1-t))'})
