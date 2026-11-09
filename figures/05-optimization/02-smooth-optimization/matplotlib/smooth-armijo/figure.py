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
panel(fig, .1, .985, .975, .155)
A = np.linspace(0,.58,500); phi = 45-162*A+405*A**2; tan_ = 45-162*A; arm = 45-16.2*A
ax.plot(A,tan_,color=MUTED,lw=.85,ls=':'); ax.plot(A,arm,color=STROKE,lw=1.0,ls=(0,(3,1.6))); ax.plot(A,phi,color=BLUE,lw=1.4)
ax.plot([0,.36],[3,3],color=GREEN,lw=2.8,solid_capstyle='butt',zorder=4); ax.text(.09,5,'可接受步长',ha='center',va='bottom')
ax.plot([.5],[65.25],'o',ms=4.6,mfc='white',mec=YELLOW,mew=1.1,zorder=5); ax.text(.51,62,'$0.5$',ha='left',va='top',fontsize=7.5)
ax.plot([.25],[29.8125],'o',ms=4.8,color=GREEN,mew=0,zorder=6); ax.text(.26,27.5,'$0.25$',ha='left',va='top',fontsize=7.5)
ax.plot([.36],[39.168],'o',ms=3.8,color=STROKE,mew=0,zorder=5); ax.text(.355,42,'$0.36$',ha='right',va='bottom',fontsize=7.5)
ax.text(.52,33.3,r'$\phi(0)+c_1\alpha\phi^{\prime}(0)$',ha='right',va='top',fontsize=7.5); ax.text(.215,6.5,r'',ha='left'); ax.text(.13,17,r'切线',ha='right',va='top',fontsize=7.5); ax.text(.45,71,r'$\phi(\alpha)$',ha='right',va='center')
ax.set_xlim(0,.58); ax.set_ylim(0,78); ax.set_xticks([0,.1,.2,.3,.4,.5]); ax.set_xticklabels(['0','0.1','0.2','0.3','0.4','0.5']); ax.set_yticks([0,20,40,60]); ax.set_xlabel(r'步长',labelpad=1); ax.set_ylabel('目标',labelpad=1)
save(fig, HERE, 'figure', {'phi':'45-162a+405a^2','c1':.1,'accept':'a<=0.36','trials':[1,.5,.25]})
