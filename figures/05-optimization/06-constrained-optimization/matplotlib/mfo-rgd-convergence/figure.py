from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Convergence of Riemannian gradient descent on the running example; L=9/2 sufficient constant.
T=60
def run(step):
    x=X0.copy(); F=[];G=[]
    for t in range(T+1):
        g=grad3(x); F.append(f3(x)-.5); G.append(np.linalg.norm(g)); x=retr(x,-step(x,g)*g)
    return np.array(F),np.array(G)
def bt(x,g):
    a=1.
    while f3(retr(x,-a*g))>f3(x)-.25*a*g@g: a/=2
    return a
F1,G1=run(lambda x,g:2/9); F2,G2=run(bt)
fig,axs=figure(width_mm=112,height_mm=48,ncols=2)
ax=axs[0]
ax.semilogy(F2+1e-18,color=GREEN,lw=1.5,label='回溯'); ax.semilogy(F1+1e-18,color=YELLOW,lw=1.5,label=r'$\alpha=2/9$')
ax.set_xlabel(r'$t$'+'\n(a)'); ax.set_ylabel(r'$f(\mathbf{x}^{(t)})-f^{*}$'); ax.legend(handlelength=1.8); ax.set_ylim(1e-16,2)
ax=axs[1]
t=np.arange(1,T+1); L=4.5; bound=np.sqrt(2*L*(F1[0])/t)
ax.semilogy(t,np.minimum.accumulate(G1)[:-1],color=YELLOW,lw=1.5,label=r'$\alpha=2/9$')
ax.semilogy(t,bound,color=GRAY,lw=1.1,ls='--',label='定理上界')
ax.set_xlabel(r'$T$'+'\n(b)'); ax.set_ylabel(r'$\min_{t<T}\Vert\mathbf{g}^{(t)}\Vert_2$'); ax.legend(handlelength=1.8,loc='lower left')
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'RGD on sphere, A=diag(1,2,4), x0=(2,2,1)/3; bound sqrt(2L(f0-f*)/T), L=9/2'})
