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

kappa=100.; eps=1e-6
Tgd=np.ceil(kappa/2*np.log(1/eps)); Tcg=np.ceil(np.sqrt(kappa)/4*np.log(4/eps))
n=np.logspace(1,5,300)
fig, ax = figure(width_mm=100, height_mm=58)
panel(fig, .125, .955, .975, .155)
ax.loglog(n,2*n**2*Tgd,color=YELLOW,lw=1.4); ax.loglog(n,2*n**2*Tcg,color=GREEN,lw=1.4); ax.loglog(n,n**3/3+2*n**2,color=BLUE,lw=1.4)
ax.text(40,2*40**2*Tgd*1.8,'梯度下降',ha='right',va='bottom'); ax.text(9e2,2*9e2**2*Tcg/4,'共轭梯度',ha='left',va='top'); ax.text(5e3,5e3**3/3*4,'Cholesky',ha='right',va='bottom')
for x,c in ((3*2*Tgd,YELLOW),(3*2*Tcg,GREEN)):
    ax.plot([x],[x**3/3+2*x**2],'o',ms=4.4,color=c,mew=0,zorder=5)
ax.set_xlim(10,1e5); ax.set_ylim(1e3,1e14); ax.set_xlabel('维数',labelpad=1); ax.set_ylabel('浮点运算次数',labelpad=1); ax.set_xticks([1e1,1e2,1e3,1e4,1e5]); ax.set_yticks([1e4,1e8,1e12]); ax.minorticks_off()
save(fig, HERE, 'figure', {'kappa':kappa,'eps':eps,'T_gd':Tgd,'T_cg':Tcg,'per_iter':'2 n^2','cholesky':'n^3/3+2n^2'})
