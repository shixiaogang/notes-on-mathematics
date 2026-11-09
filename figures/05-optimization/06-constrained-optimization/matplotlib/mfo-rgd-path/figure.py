from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Riemannian gradient descent with Armijo backtracking (c1=1/4, a0=1, shrink 1/2) and fixed step 2/9.
fig, ax = figure(width_mm=72, height_mm=68)
D=Disk(28,24); D.outline(ax)
ax.contour(D.U,D.V,D.rayleigh(),levels=[.56,.68,.85,1.0,1.2,1.45,1.7,1.9],colors=BLUE,linewidths=.75)
def path(step):
    x=X0.copy(); P=[x]
    for t in range(14):
        g=grad3(x); a=step(x,g); x=retr(x,-a*g); P.append(x)
    return P
def bt(x,g):
    a=1.
    while f3(retr(x,-a*g))>f3(x)-.25*a*g@g: a/=2
    return a
for P,c,lw,ms in [(path(lambda x,g:2/9),YELLOW,1.3,2.6),(path(bt),GREEN,1.5,3.2)]:
    for a,b in zip(P[:-1],P[1:]):
        ax.plot(*D.xy(arc(a,b)),color=c,lw=lw)
    for p in P:
        ax.plot(*D.xy(p),'o',ms=ms,color=c)
ax.plot(*D.xy(np.eye(3)[0]),'o',ms=4.8,color=RED,zorder=5)
ax.plot(*D.xy(X0),'o',ms=4.4,color=GREEN,zorder=5)
a,b=D.xy(X0); ax.text(a+.05,b+.12,r'$\mathbf{x}^{(0)}$',ha='center',fontsize=8)
a,b=D.xy(np.eye(3)[0]); ax.text(a-.13,b-.14,r'$\mathbf{e}_1$',ha='center',fontsize=8)
ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'RGD, normalization, Armijo c1=1/4 alpha0=1 shrink 1/2; fixed alpha=2/9'})
