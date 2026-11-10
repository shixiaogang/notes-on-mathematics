from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: the conics that give the three types their names.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
a=np.linspace(0,2*np.pi,300); s=np.linspace(-1.5,1.5,200)
ax=axs[0]; ax.plot(np.cos(a),np.sin(a),color=BLUE,lw=1.4); sub(ax,'a',r'$\xi$'); ax.set_ylabel(r'$\tau$')
ax=axs[1]; ax.plot(s,s**2,color=BLUE,lw=1.4); ax.set_ylim(-.25,2.25); sub(ax,'b',r'$\xi$')
ax=axs[2]; ch=np.cosh(s)
ax.plot(np.sinh(s),ch,color=BLUE,lw=1.4); ax.plot(np.sinh(s),-ch,color=BLUE,lw=1.4)
ax.plot([-2,2],[-2,2],color=LINE,lw=1.2); ax.plot([-2,2],[2,-2],color=LINE,lw=1.2); sub(ax,'c',r'$\xi$')
for ax,L in zip(axs,(1.5,1.5,2.2)):
    style(ax); ax.set_xlim(-L,L); ax.set_xticks([-1,0,1])
    if L!=1.5 or ax is axs[0]: ax.set_ylim(-L,L)
    ax.set_yticks([-1,0,1] if ax is not axs[1] else [0,1,2])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'tau^2+xi^2=1; tau=xi^2; tau^2-xi^2=1'})
