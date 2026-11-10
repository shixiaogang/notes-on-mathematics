from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: heat mode amplification forward/backward, and a reconstruction with a tiny perturbation.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
T=.1; k=np.arange(1,9)
ax=axs[0]; style(ax)
ax.semilogy(k,np.exp(-(k*np.pi)**2*T),'o-',ms=3,lw=1.4,color=BLUE)
ax.semilogy(k,np.exp((k*np.pi)**2*T),'o-',ms=3,lw=1.4,color=RED)
ax.axhline(1,color=GRID,lw=.85); ax.text(5.1,3e-22,'正向',color=BLUE); ax.text(5.2,1e19,'反向',color=RED)
ax.set_xticks([1,3,5,7]); ax.set_ylabel('放大倍数'); sub(ax,'a','$k$')
ax=axs[1]; style(ax); X=np.linspace(0,1,800); eps=1e-10
true=np.sin(np.pi*X); rec=true+eps*np.exp((5*np.pi)**2*T)*np.sin(5*np.pi*X)
ax.axhline(0,color=GRID,lw=.85)
ax.plot(X,rec,color=RED,lw=1.2); ax.plot(X,true,color=BLUE,lw=1.4)
ax.set_xlim(0,1); ax.set_xticks([0,.5,1]); ax.set_ylabel('$u(x,0)$'); sub(ax,'b','$x$')
A=float(eps*np.exp((5*np.pi)**2*T))
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'T=.1; eps=1e-10 at mode 5','amplitude':A}); print(A)
