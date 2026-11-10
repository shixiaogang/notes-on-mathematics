from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: eigenvalues of the second-difference matrix on (0,1) with zero end values.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
def ev(N):
    h=1/(N+1); A=(np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1))/h**2
    return np.sort(-np.linalg.eigvalsh(A))
ax=axs[0]; style(ax)
k=np.arange(1,16)
ax.semilogy(k,(k*np.pi)**2,'-',color=BLUE,lw=1.4)
ax.semilogy(k,ev(15),'o',ms=3,color=YELLOW)
ax.semilogy(np.arange(1,4),ev(3),'o',ms=3.6,color=GREEN)
ax.text(10.2,2900,r'$k^2\pi^2$',color=BLUE); ax.text(11.5,380,'$N=15$',color=YELLOW); ax.text(3.6,28,'$N=3$',color=GREEN)
ax.set_xticks([1,5,10,15]); ax.set_ylabel(r'$|\lambda_k|$'); sub(ax,'a','$k$')
ax=axs[1]; style(ax)
Ns=np.array([3,7,15,31,63,127,255]); m=[ev(n)[-1] for n in Ns]
ax.loglog(Ns,m,'o-',ms=3,lw=1.4,color=GREEN)
ax.loglog(Ns,4*(Ns+1.0)**2,'--',lw=.95,color=PURPLE)
ax.text(19,7500,'$4/h^2$',color=PURPLE)
ax.set_ylabel(r'$\max_k|\lambda_k|$'); sub(ax,'b','$N$')
save(fig, Path(__file__).resolve().parent, 'figure', {'N3_eigs':[float(x) for x in ev(3)],'formula':'tridiag(1,-2,1)/h^2, h=1/(N+1)'})
print(ev(3))
