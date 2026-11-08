from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
# (a) |d_{j,k}| of f=1_[1/3,1): -2^{-j/2}/3 on the interval containing 1/3; (b) of g=sin(2 pi x): d=-2^{j/2}(2/pi)cos(2 pi m)sin^2(pi 2^{-j-1}); (c) Fourier |c_n|=|sin(pi n/3)|/(pi n) of f.
# Tile shade: log10|d| linearly from -3 (white) to 0 (BLUE).
import matplotlib.colors as mc
from matplotlib.patches import Rectangle
fig, axes = figure(width_mm=112, height_mm=50, ncols=3, gridspec_kw={'width_ratios':[1,1,.95]})
fig.set_layout_engine(None)
fig.subplots_adjust(left=.055, right=.985, top=.95, bottom=.26, wspace=.27)
c0=np.array(mc.to_rgb('#FFFFFF')); c1=np.array(mc.to_rgb(BLUE))
def shade(a):
    if a<1e-12: return (1,1,1)
    t=np.clip((np.log10(a)+3)/3,0,1)
    return tuple(c0+(c1-c0)*t)
Jmax=6
def tiles(ax,fun):
    for j in range(Jmax):
        n=2**j
        for k in range(n):
            ax.add_patch(Rectangle((k/n,j),1/n,1,facecolor=shade(abs(fun(j,k))),edgecolor=GRID,lw=.55))
    ax.set_xlim(0,1); ax.set_ylim(Jmax,0); ax.set_xticks([0,1]); ax.set_yticks(np.arange(Jmax)+.5); ax.set_yticklabels([str(j) for j in range(Jmax)])
    ax.tick_params(length=0,labelsize=7,pad=2); ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False)
def fd(j,k):
    n=2**j; T=1/3
    return -2**(-j/2)/3 if k/n<=T<(k+1)/n else 0.0
def gd(j,k):
    n=2**j; m=(k+.5)/n
    return -2**(j/2)*(2/np.pi)*np.cos(2*np.pi*m)*np.sin(np.pi/(2*n))**2
tiles(axes[0],fd); tiles(axes[1],gd)
axes[0].axvline(1/3,color=RED,lw=.9,dashes=(2.4,1.6))
ax=axes[2]
n=np.arange(1,25); a=np.abs(np.sin(np.pi*n/3))/(np.pi*n)
nz=a>1e-10
ax.vlines(n[nz],0,a[nz],color=BLUE,lw=1.2); ax.plot(n[nz],a[nz],'o',ms=2.8,color=BLUE,mew=0)
ax.plot(n[~nz],0*n[~nz],'o',ms=2.2,color=MUTED,mew=0)
ax.set_xlim(0,25); ax.set_ylim(0,.32); ax.set_xticks([1,12,24]); ax.set_yticks([0,.1,.2,.3])
ax.set_xlabel('$n$',labelpad=0); ax.text(.97,.98,r'$|\hat f(n)|$',transform=ax.transAxes,ha='right',va='top')
ax.tick_params(labelsize=7,length=2,pad=1.5)
for ax,s in zip(axes,'abc'):
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Haar coefficient magnitude on dyadic tiles j<6 for f=1_[1/3,1) and g=sin(2 pi x); log10 shade from -3 to 0; Fourier |hat f(n)|'})
