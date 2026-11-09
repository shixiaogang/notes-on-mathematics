from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# 束方法：f=max{-x,x/2,2x-3}，y0=4，tau=2，beta=1/2；读取程序在 x=0 返回 1/2。
f=lambda x:np.maximum.reduce([-x,x/2,2*x-3])
X=np.linspace(-2.5,5,1501)
def line(c,x):return f(np.array(c[0]))+c[1]*(x-c[0])
def model(C,x):return np.maximum.reduce([line(c,x) for c in C])
rounds=[([(4.,2.)],4.,0.),([(4.,2.),(0.,.5)],0.,-1.),([(4.,2.),(0.,.5),(-1.,-1.)],0.,0.)]
fig,axs=figure(width_mm=112,height_mm=52,ncols=3)
panel(fig,.05,.98,.98,.26,wspace=.14)
tau=2.
for ax,(C,ctr,cand) in zip(axs,rounds):
    ax.plot(X,f(X),color=BLUE,lw=1.4);M=model(C,X);ax.plot(X,M,color=PURPLE,lw=1.3);ax.plot(X,M+(X-ctr)**2/(2*tau),color=PURPLE,lw=.95,ls='--')
    ax.plot([ctr],[f(np.array(ctr))],'s',color=INK,ms=3.8,mew=0,zorder=7)
    mc=float(model(C,np.array(cand)));ax.plot([cand],[mc],'x',color=RED,ms=4.4,mew=1.1,zorder=8);ax.plot([cand],[f(np.array(cand))],'o',color=GREEN,ms=4.2,mew=0,zorder=7)
    ax.plot([cand,cand],[mc,f(np.array(cand))],color=MUTED,lw=.85,ls=':')
    ax.set_xlim(-2.5,5);ax.set_ylim(-4,7);ax.set_xticks([-2,0,2,4]);ax.set_yticks([-4,0,4]);ax.set_xlabel('$x$',labelpad=1)
fig.canvas.draw()
for ax,s in zip(axs,('(a)','(b)','(c)')):tag(fig,ax,s,y=.055)
save(fig,HERE,'figure',{'tau':tau,'beta':.5,'rounds':[[4,0],[0,-1],[0,0]]})
