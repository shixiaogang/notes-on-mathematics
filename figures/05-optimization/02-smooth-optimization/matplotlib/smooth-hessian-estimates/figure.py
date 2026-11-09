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
panel(fig, .03, .985, .95, .27, .24)
A = np.array([[2.,1,0],[1,3,1],[0,1,2]]); ev = np.linalg.eigvalsh(A)
a = axes[0]; a.axis('off'); a.set_xlim(.4,7.6); a.set_ylim(-1.5,2)
a.plot([.6,7.4],[0,0],color=STROKE,lw=.95)
for t in range(1,8): a.plot([t,t],[-.1,.1],color=STROKE,lw=.85); a.text(t,-.42,str(t),ha='center',va='center',fontsize=7.5)
a.plot(ev,0*ev,'o',ms=5,color=BLUE,mew=0,zorder=4)
a.text(2,.45,'特征值',ha='center',va='bottom')
for v,s,y in ((np.sqrt(21),r'$\Vert A\Vert_F$',1.2),(5,r'行和',.55),(7,r'迹',.55)):
    a.plot([v,v],[0,y-.05],color=PURPLE,lw=.85); a.plot([v],[0],'o',ms=4,color=PURPLE,mew=0,zorder=4); a.text(v,y,s,ha='center',va='bottom')
a.annotate('',xy=(4,-.75),xytext=(4,-1.25),arrowprops=dict(arrowstyle='-|>',color=RED,lw=1,mutation_scale=7)); a.text(4.25,-1.05,r'$L=4$',ha='left',va='center',fontsize=7.5)
b = axes[1]; v = np.ones(3); R = []
for k in range(9):
    R.append(v@A@v/(v@v)); v = A@v
b.axhline(4,color=RED,lw=.85,ls=(0,(3,1.6))); b.plot(range(9),R,'-o',color=GREEN,lw=1.3,ms=3.6,mew=0)
b.text(8,4.04,'$L=4$',ha='right',va='bottom')
b.set_xlim(-.4,8.4); b.set_ylim(3.55,4.25); b.set_xticks([0,2,4,6,8]); b.set_yticks([3.6,3.8,4,4.2]); b.set_yticklabels(['3.6','3.8','4','4.2']); b.set_xlabel('幂迭代步数',labelpad=1); b.set_ylabel('Rayleigh 商',labelpad=1)
p0 = a.get_position(); p1 = b.get_position()
fig.text((p0.x0+p0.x1)/2,.015,'(a)',ha='center',va='bottom'); fig.text((p1.x0+p1.x1)/2,.015,'(b)',ha='center',va='bottom')
save(fig, HERE, 'figure', {'A':A.tolist(),'eig':ev.tolist(),'rayleigh':R})
