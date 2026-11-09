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

def run(mode):
    x = x0.copy(); a0 = 1.; tr = []
    while fv(x) > 1e-6:
        g = grad(x); a = a0; k = 0; fx = fv(x)
        while True:
            k += 1; y = x-a*g
            if fv(y) <= fx-.1*a*g@g: break
            a *= .5
        tr.append(k); x = y
        if mode == 'warm': a0 = 2*a
    return np.array(tr)
cold, warm = run('cold'), run('warm')
fig, axes = figure(width_mm=112, height_mm=44, ncols=2, sharey=True)
panel(fig, .08, .985, .965, .31, .1)
for a,tr,c in zip(axes,(cold,warm),(GREEN,YELLOW)):
    a.bar(range(len(tr)),tr,color=c,width=.72,lw=0); a.axhline(tr.mean(),color=STROKE,lw=.85,ls=(0,(3,1.6)))
    a.text(len(tr)-.5,4.45,f'平均 {tr.mean():.2f}',ha='right',va='bottom',fontsize=7.5)
    a.set_xlabel('外层迭代',labelpad=1); a.set_xlim(-1,len(tr)); a.set_xticks(range(0,len(tr),10))
axes[0].set_yticks([0,1,2,3,4]); axes[0].set_ylim(0,5); axes[0].set_ylabel('试探次数',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'cold':cold.tolist(),'warm':warm.tolist()})
