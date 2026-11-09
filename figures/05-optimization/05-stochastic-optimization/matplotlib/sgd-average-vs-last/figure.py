from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿例：f_i(x)=a_i(x-b_i)^2/2，a=(1,2,3)，b=(-3,0,3)；f(x)=(x-1)^2+5，x*=1。
A = np.array([1., 2., 3.]); B = np.array([-3., 0., 3.])
def gi(x): return A*(x-B)
def panel(fig, left, right, top, bottom, wspace=.3, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')

rng=np.random.default_rng(21)
al=.1;T=600;R=4000
X=np.zeros((R,T+1)); X[:,0]=5.
idx=rng.integers(3,size=(R,T))
for t in range(T):
    X[:,t+1]=X[:,t]-al*A[idx[:,t]]*(X[:,t]-B[idx[:,t]])
av=np.cumsum(X,axis=1)/np.arange(1,T+2)
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.085,.985,.97,.25,wspace=.3)
s=np.arange(T+1)
a.plot(s[:301],X[0,:301],color=GREEN,lw=.95); a.plot(s[:301],av[0,:301],color=YELLOW,lw=1.7)
a.axhline(1,color=RED,lw=.85); a.text(112,3.3,'$x^{(t)}$',fontsize=8); a.text(70,1.9,r'$\bar{x}^{(t)}$',fontsize=8)
a.set_xlabel('$t$',labelpad=1); a.set_xlim(0,300); a.set_ylim(-1.2,5.2)
g1=((X-1)**2).mean(0); g2=((av-1)**2).mean(0)
b.loglog(s[1:],g1[1:],color=GREEN,lw=1.4); b.loglog(s[1:],g2[1:],color=YELLOW,lw=1.7)
b.text(25,.9,'最后一点',fontsize=7.5); b.text(45,.033,'平均点',fontsize=7.5)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel(r'$\mathrm{E}[f-f^*]$',labelpad=1); b.set_xlim(1,600)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
print('last',g1[-1],'avg',g2[-1])
save(fig,HERE,'figure',{'seed':21,'runs':R,'alpha':al,'last':float(g1[-1]),'avg':float(g2[-1])})
