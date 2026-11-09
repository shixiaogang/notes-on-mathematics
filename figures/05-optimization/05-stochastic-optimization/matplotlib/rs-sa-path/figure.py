from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 二维 Rastrigin 上的模拟退火，高斯提议 sigma=0.8，几何降温 T: 25->0.05，3000 次
rng=np.random.default_rng(11)
F=lambda x: rastrigin(x[0],x[1])
x=np.array([3.2,-3.0]); fx=F(x); B=3000; T0,T1=25,.05; tr=[x.copy()]; cur=[fx]; best=[fx]; bx=x.copy(); bf=fx
for t in range(B-1):
    T=T0*(T1/T0)**(t/(B-2)); y=x+.8*rng.standard_normal(2); fy=F(y)
    if fy<=fx or rng.random()<np.exp(-(fy-fx)/T): x,fx=y,fy
    if fx<bf: bf,bx=fx,x.copy()
    tr.append(x.copy()); cur.append(fx); best.append(bf)
tr=np.array(tr); print(bf,bx,x,fx)
fig,axes=figure(width_mm=112,height_mm=60,ncols=2); panel(fig,.075,.96,.965,.245,.28)
a=axes[0]; g=np.linspace(-5,5,700); X,Y=np.meshgrid(g,g); a.contour(X,Y,rastrigin(X,Y),levels=[10,35,60],colors=[BLUE],linewidths=.5)
a.plot(tr[::18,0],tr[::18,1],color=YELLOW,lw=.7); a.plot([tr[0,0]],[tr[0,1]],'o',ms=3.6,mfc='white',mec=GREEN,mew=.9,zorder=5); a.plot([bx[0]],[bx[1]],'o',ms=4.4,color=GREEN,mew=0,zorder=6); a.plot([0],[0],'o',ms=4.4,color=RED,mew=0,zorder=7)
a.set_aspect('equal'); a.set_xlim(-5,5); a.set_ylim(-5,5); a.set_xticks([-4,0,4]); a.set_yticks([-4,0,4]); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0)
b=axes[1]; ts=np.arange(1,B+1); b.plot(ts,cur,color=YELLOW,lw=.8); b.plot(ts,best,color=GREEN,lw=1.5)
b.set_xlim(1,B); b.set_ylim(0,80); b.set_xticks([1,1500,3000]); b.set_yticks([0,40,80]); b.set_xlabel('评价次数',labelpad=1); b.set_ylabel('$f$',labelpad=1)
tags(fig,axes); save(fig,HERE,'figure',{'sigma':.8,'T':[T0,T1],'B':B,'seed':11,'best':float(bf),'best_x':bx.tolist(),'final':float(fx)})
