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

# 一元目标 phi(a)=0.12(a-3)^2+0.35 cos(2.2 a)，沿线段的非凸例子；c1=0.1，c2=0.5。
phi = lambda a: .12*(a-3)**2+.35*np.cos(2.2*a)
dphi = lambda a: .24*(a-3)-.77*np.sin(2.2*a)
c1, c2 = .1, .5
A = np.linspace(0,6.2,3000); p0, s0 = phi(0.), dphi(0.)
arm = phi(A) <= p0+c1*A*s0
cur = dphi(A) >= c2*s0
stg = np.abs(dphi(A)) <= c2*abs(s0)
def runs(m):
    idx = np.where(m)[0]
    if len(idx)==0: return []
    sp = np.split(idx, np.where(np.diff(idx)>1)[0]+1)
    return [(A[s[0]],A[s[-1]]) for s in sp]
fig, axes = figure(width_mm=100, height_mm=88, nrows=3, sharex=True, gridspec_kw={'height_ratios':[1.5,1.2,.55]})
panel(fig, .1, .985, .985, .135, hspace=.1)
a=axes[0]; a.plot(A,p0+c1*A*s0,color=STROKE,lw=1.0,ls=(0,(3,1.6))); a.plot(A,phi(A),color=BLUE,lw=1.4); a.set_ylabel(r'$\phi(\alpha)$',labelpad=1); a.set_ylim(-.55,1.65); a.set_yticks([0,1])
a.plot([0],[p0],'o',ms=4.6,color=GREEN,mew=0,zorder=5)
b=axes[1]; b.axhline(c2*s0,color=STROKE,lw=1.0,ls=(0,(3,1.6))); b.axhline(-c2*s0,color=STROKE,lw=1.0,ls=(0,(1,1.6))); b.axhline(0,color=MUTED,lw=.6)
b.plot(A,dphi(A),color=BLUE,lw=1.4); b.set_ylabel(r"$\phi^{\prime}(\alpha)$",labelpad=1); b.set_ylim(-1.45,1.45); b.set_yticks([-1,0,1])
b.text(6.15,c2*s0-.07,r"$c_2\phi^{\prime}(0)$",ha='right',va='top',fontsize=7.5); b.text(.08,-c2*s0+.07,r"$-c_2\phi^{\prime}(0)$",ha='left',va='bottom',fontsize=7.5)
c=axes[2]; c.spines['left'].set_visible(False); c.set_yticks([]); c.set_ylim(-.6,2.6); c.set_xticks([0,1,2,3,4,5,6])
for y,m,col,s in ((2,arm,GREEN,'A'),(1,arm&cur,YELLOW,'W'),(0,arm&stg,PURPLE,'S')):
    for l,r in runs(m): c.plot([l,r],[y,y],color=col,lw=3,solid_capstyle='butt')
    c.text(-.05,y,s,ha='right',va='center',fontsize=7.5,clip_on=False)
c.axvline(0,color='none')
c.set_xlim(0,6.2); b.set_xlim(0,6.2); a.set_xlim(0,6.2)

fig.text(.54,.012,r'步长',ha='center',va='bottom')
save(fig, HERE, 'figure', {'phi':'0.12(a-3)^2+0.35cos(2.2a)','c1':c1,'c2':c2,'armijo':runs(arm),'wolfe':runs(arm&cur),'strong':runs(arm&stg)})
print(runs(arm),runs(arm&cur),runs(arm&stg))
