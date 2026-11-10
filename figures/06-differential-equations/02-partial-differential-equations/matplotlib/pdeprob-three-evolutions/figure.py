from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: the same Gaussian bump under heat, transport and wave equations (exact solutions).
fig, axs = figure(width_mm=112, height_mm=46, ncols=3, sharey=True)
s0=.25; X=np.linspace(0,6,800); T=[0,.5,1,1.5]
g=lambda x:np.exp(-(x-3)**2/(2*s0**2))
sols=[lambda x,t:s0/np.sqrt(s0**2+2*.1*t)*np.exp(-(x-3)**2/(2*(s0**2+2*.1*t))),
      lambda x,t:g(x-t),
      lambda x,t:.5*(g(x-t)+g(x+t))]
for ax,f,l,n in zip(axs,sols,'abc',('热方程','输运方程','波动方程')):
    style(ax)
    for t,c in zip(T,[RED]+SHADES[1:]):
        ax.plot(X,f(X,t),color=c,lw=1.4)
    ax.set_xlim(0,6); ax.set_ylim(0,1.08); ax.set_xticks([0,3,6]); sub(ax,l,'$x$')
    ax.text(.03,.95,n,transform=ax.transAxes,color=MUTED,fontsize=7.5,va='top')
axs[0].set_ylabel('$u$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'exact solutions; kappa=0.1,b=1,c=1, sigma0=0.25, t=0,0.5,1,1.5'})
