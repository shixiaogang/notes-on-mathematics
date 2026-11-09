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

fig, ax = figure(width_mm=92, height_mm=54)
panel(fig, .125, .97, .97, .165)
x = np.linspace(.2,2.5,400); ax.plot(x,np.sin(x),color=BLUE,lw=1.4)
for xn,c in ((1.6,YELLOW),(.7,GREEN)):
    ax.plot([2,xn],[np.sin(2),np.sin(xn)],color=c,lw=1.3,zorder=4); ax.plot([xn],[np.sin(xn)],'o',ms=4.6,color=c,mew=0,zorder=5)
ax.plot([2],[np.sin(2)],'o',ms=4.8,color=STROKE,mew=0,zorder=5)
ax.text(2.04,.95,'$x$',ha='left',va='bottom'); ax.text(1.6,1.035,r'$x_{\mathrm{A}}$',ha='center',va='bottom'); ax.text(.74,.57,r'$x_{\mathrm{W}}$',ha='left',va='top')
ax.set_xlim(.2,2.5); ax.set_ylim(.3,1.15); ax.set_xticks([.5,1,1.5,2,2.5]); ax.set_xticklabels(['0.5','1','1.5','2','2.5']); ax.set_yticks([.4,.6,.8,1]); ax.set_yticklabels(['0.4','0.6','0.8','1']); ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel("$f'(x)=\\sin x$",labelpad=1)
save(fig, HERE, 'figure', {'x':2,'x_A':1.6,'x_W':.7})
