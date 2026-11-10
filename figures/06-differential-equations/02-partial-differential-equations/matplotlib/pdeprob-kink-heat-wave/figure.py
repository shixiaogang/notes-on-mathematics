from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: a hat initial profile under the heat and the wave equation on (0,1), zero end values.
fig, axs = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
X=np.linspace(0,1,801)
hat=lambda x:np.minimum(x,1-x)
K=np.arange(1,601); b=4*np.sin(K*np.pi/2)/(K*np.pi)**2
S=np.sin(np.outer(K,X)*np.pi)
heat=lambda t:(b*np.exp(-(K*np.pi)**2*t))@S
def ext(y):
    y=np.mod(y,2.0)
    return np.where(y<=1,hat(y),-hat(y-1))
wave=lambda t:.5*(ext(X-t)+ext(X+t))
ax=axs[0]; style(ax); ax.plot(X,hat(X),color=RED,lw=1.5)
for t,c in zip((.004,.02,.08),SHADES[1:]+[SHADES[-1]]): ax.plot(X,heat(t),color=c,lw=1.4)
sub(ax,'a','$x$'); ax.set_ylabel('$u$')
ax=axs[1]; style(ax); ax.plot(X,hat(X),color=RED,lw=1.5)
for t,c in zip((.1,.25),SHADES[1:]): ax.plot(X,wave(t),color=c,lw=1.4)
sub(ax,'b','$x$')
for ax in axs: ax.set_xlim(0,1); ax.set_xticks([0,.5,1]); ax.set_ylim(0,.56)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'hat=min(x,1-x); heat sine series 600 terms t=.004,.02,.08; wave odd periodic dAlembert t=.1,.25'})
