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

fig, axes = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios':[1,1.35]})
panel(fig, .105, .985, .96, .27, .26)
a = axes[0]; A = np.linspace(0,.15,400)
a.plot(A,45-162*A+405*A**2,color=BLUE,lw=1.4); a.plot(A,45-1620*A+40500*A**2,color=BLUE,lw=1.4,ls=(0,(3,1.6)))
a.axvline(1/9,color=MUTED,lw=.85,ls=':'); a.plot([1/9],[32],'o',ms=4.4,color=GREEN,mew=0,zorder=5); a.plot([1/9],[365],'o',ms=4.4,color=RED,mew=0,zorder=5)
a.text(1/9-.004,395,'$1/L$',ha='right',va='bottom'); a.text(.015,60,r'$-g$',ha='left',va='bottom'); a.text(.125,300,r'$-10g$',ha='left',va='center')
a.set_xlim(0,.15); a.set_ylim(0,440); a.set_xticks([0,.05,.1,.15]); a.set_xticklabels(['0','0.05','0.1','0.15']); a.set_yticks([0,200,400]); a.set_xlabel(r'步长',labelpad=1); a.set_ylabel('目标',labelpad=1)
b = axes[1]; X,Y = np.meshgrid(np.linspace(-11,11,700),np.linspace(-9.5,3,500))
b.contour(X,Y,f2(X,Y),levels=[8,20,45,120],colors=[BLUE],linewidths=.7)
g = grad(x0)
for d,c in ((-g,GREEN),(-np.linalg.solve(H,g),YELLOW)):
    b.annotate('',xy=x0+d*min(1.,1.)*(1 if c==YELLOW else .4),xytext=x0,arrowprops=dict(arrowstyle='-',color=c,lw=.8,ls=(0,(3,1.6))),zorder=3)
    amax = 2*abs(g@d)/(9*d@d); e = x0+amax*d
    b.plot([x0[0],e[0]],[x0[1],e[1]],color=c,lw=2.6,solid_capstyle='butt',zorder=4)
b.plot(*x0,'o',ms=4.8,color=GREEN,mew=0,zorder=6); b.plot(0,0,'o',ms=4.8,color=RED,mew=0,zorder=5)
e=x0-.4*g; b.plot(*e,'o',ms=3.6,mfc='white',mec=GREEN,mew=.9,zorder=5); b.text(e[0]-.3,e[1]-.25,r'$\phi=\phi(0)$',ha='right',va='top',fontsize=7.5)
b.text(9.1,1.45,'$x^{(0)}$',ha='center',va='bottom'); b.text(.3,.3,'$x^*$',ha='left',va='bottom')
b.set_xlim(-11,11); b.set_ylim(-9.5,3); b.set_aspect('equal'); b.set_xticks([-10,0,10]); b.set_yticks([-8,-4,0]); b.set_xlabel('$x_1$',labelpad=1); b.set_ylabel('$x_2$',labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'x0':[9,1],'d1':'-g','d2':'-H^{-1}g','guaranteed':'alpha<2|g.d|/(L|d|^2)'})
