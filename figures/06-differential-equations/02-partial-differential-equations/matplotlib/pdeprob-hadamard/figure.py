from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: Cauchy data for the Laplace equation, u=sinh(ky) sin(kx)/k^2.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax=axs[0]; style(ax); X=np.linspace(0,2*np.pi,1000); ks=(2,5,20); cs=(BLUE,YELLOW,PURPLE)
for k,c in zip(ks,cs): ax.plot(X,np.sin(k*X)/k,color=c,lw=1.3)
ax.set_xlim(0,2*np.pi); ax.set_xticks([0,np.pi,2*np.pi]); ax.set_xticklabels(['0',r'$\pi$',r'$2\pi$']); ax.set_ylabel(r'$\partial_y u(x,0)$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); y=np.linspace(0.001,1,300)
for k,c in zip(ks,cs):
    ax.semilogy(y,np.sinh(k*y)/k**2,color=c,lw=1.4)
    ax.text(1.02,np.sinh(k)/k**2*{2:.3,5:3,20:1}[k],f'$k={k}$',color=c,va='center')
ax.set_xlim(0,1.22); ax.set_xticks([0,.5,1]); ax.set_ylabel(r'$\sup_x| u(x,y)|$'); sub(ax,'b','$y$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'u=sinh(k y) sin(k x)/k^2, k=2,5,20'})
