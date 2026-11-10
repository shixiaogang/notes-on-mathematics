from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: initial value 1 with boundary value 0: heat equation versus transport with v=1.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
x=np.linspace(0,1,301); t=np.linspace(0,.25,301)
K=np.arange(1,2001,2)
# heat: sum 4/(k pi) sin(k pi x) exp(-(k pi)^2 t), odd k
U=np.zeros((t.size,x.size))
S=np.sin(np.outer(K,x)*np.pi)
for i,tt in enumerate(t):
    U[i]=(4/(K*np.pi)*np.exp(-(K*np.pi)**2*tt))@S
U=np.clip(U,0,1)
ax=axs[0]; im=ax.imshow(U,origin='lower',extent=[0,1,0,.25],aspect='auto',cmap=FIELD,vmin=0,vmax=1,interpolation='bilinear')
ax.plot([0,1],[0,0],color=RED,lw=2.4,clip_on=False)
ax.plot([0,0],[0,.25],color=LINE,lw=2.0,clip_on=False); ax.plot([1,1],[0,.25],color=LINE,lw=2.0,clip_on=False)
ax.set_yticks([0,.1,.2]); sub(ax,'a','$x$'); ax.set_ylabel('$t$')
ax=axs[1]; tt=np.linspace(0,1,301); XX,TT=np.meshgrid(x,tt); V=(XX>TT).astype(float)
ax.imshow(V,origin='lower',extent=[0,1,0,1],aspect='auto',cmap=FIELD,vmin=0,vmax=1,interpolation='nearest')
ax.plot([0,1],[0,1],color=LINE,lw=1.8)
ax.plot([0,1],[0,0],color=RED,lw=2.4,clip_on=False); ax.plot([0,0],[0,1],color=LINE,lw=2.0,clip_on=False)
ax.set_yticks([0,.5,1]); sub(ax,'b','$x$')
for ax in axs: style(ax); ax.set_xticks([0,.5,1])
cb=fig.colorbar(im,ax=axs,shrink=.8,aspect=18,pad=.02); cb.set_ticks([0,.5,1]); cb.outline.set_linewidth(.6); cb.ax.tick_params(width=.6,length=2); cb.set_label('$u$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'heat sine series odd k<2001; transport u=1 for x>t else 0'})
