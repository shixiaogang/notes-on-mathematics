from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) 六个坐标上的代表 g 与盒子 |x_k-g_k|<=eps；(b) 同一 g、f 在全部输入上，一致距离的闭球是图像周围的管道。
def g(x): return .5+.3*np.sin(2*np.pi*x)
def f(x): return g(x)+.1*np.cos(5*np.pi*x)
def h(x): return f(x)+.3*np.exp(-((x-.7)/.03)**2)
eps=.15
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.31, wspace=.2)
a,b=axes
K=np.arange(1,7); xk=K/7
for k,x in zip(K,xk):
    a.fill_between([k-.28,k+.28],g(x)-eps,g(x)+eps,color=GREEN_FILL,lw=0)
    a.plot([k-.28,k+.28],[g(x),g(x)],color=GREEN,lw=1.4,solid_capstyle='butt')
    a.plot([k],[f(x)],'o',ms=3.6,color=BLUE,mew=0)
a.set_xlim(.4,6.6); a.set_ylim(0,1.1); a.set_xticks(K); a.set_yticks([0,.5,1]); a.set_xlabel('坐标 k',labelpad=2)
x=np.linspace(0,1,1500)
b.fill_between(x,g(x)-eps,g(x)+eps,color=GREEN_FILL,lw=0)
b.plot(x,g(x),color=GREEN,lw=1.4)
b.plot(x,f(x),color=BLUE,lw=1.4)
b.plot(x,h(x),color=RED,lw=.95,zorder=1)
b.set_xlim(0,1); b.set_ylim(0,1.1); b.set_xticks([0,.5,1]); b.set_xticklabels(['0','1/2','1']); b.set_yticks([0,.5,1]); b.set_xlabel('输入 x',labelpad=2)
b.text(.28,.92,'$g$',color=GREEN,ha='center',va='bottom')
b.text(.39,.83,'$f$',color=BLUE,ha='center',va='bottom')
b.text(.72,.62,'$h$',color=RED,ha='left',va='bottom')
for ax,s in zip(axes,['(a)','(b)']):
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.02,s,ha='center',va='bottom')
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'g=.5+.3 sin(2 pi x), f=g+.1cos(5 pi x), h=f+.3exp(-((x-.7)/.03)^2), eps=.15; (a) samples at x=k/7'})
