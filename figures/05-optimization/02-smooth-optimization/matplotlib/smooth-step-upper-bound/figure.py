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

fig, ax = figure(width_mm=100, height_mm=56)
panel(fig, .105, .985, .97, .155)
a = np.linspace(0,.47,500); phi = 45-162*a+405*a**2; up = 45-162*a+729*a**2
ax.axhline(45,color=MUTED,lw=.85,ls=':')
ax.plot(a,up,color=YELLOW,lw=1.4); ax.plot(a,phi,color=BLUE,lw=1.4)
for v,s in ((1/9,'$1/L$'),(2/9,'$2/L$')):
    ax.plot([v,v],[0,60],color=MUTED,lw=.85,ls=(0,(3,1.6))); ax.text(v,61,s,ha='center',va='bottom')
ax.plot([.4],[45],'o',ms=4.2,color=BLUE,mew=0,zorder=5); ax.plot([2/9],[45],'o',ms=4.2,color=YELLOW,mew=0,zorder=5)
ax.plot([1/9],[32],'o',ms=4.6,color=GREEN,mew=0,zorder=5); ax.plot([1/9],[36],'o',ms=4.4,mfc='white',mec=YELLOW,mew=1,zorder=5); ax.plot([.2],[28.8],'o',ms=4.6,color=RED,mew=0,zorder=5)
ax.text(.312,55,'上界',ha='left',va='center'); ax.text(.33,27,r'$\phi(\alpha)$',ha='left',va='center'); ax.text(.408,42,'$0.4$',ha='left',va='top',fontsize=7.5)
ax.text(.195,27.5,r'$\alpha_{\mathrm{e}}$',ha='right',va='top')
ax.set_xlim(0,.47); ax.set_ylim(20,74); ax.set_xticks([0,.1,.2,.3,.4]); ax.set_xticklabels(['0','0.1','0.2','0.3','0.4']); ax.set_yticks([20,30,40,50,60,70]); ax.set_xlabel(r'步长',labelpad=1); ax.set_ylabel('目标',labelpad=1)
save(fig, HERE, 'figure', {'phi':'45-162a+405a^2','upper':'45-162a+729a^2'})
