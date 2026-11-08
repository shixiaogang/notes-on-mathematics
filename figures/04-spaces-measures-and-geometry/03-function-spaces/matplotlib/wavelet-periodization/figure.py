from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

SQ3 = np.sqrt(3.0)
H = np.array([1+SQ3, 3+SQ3, 3-SQ3, 1-SQ3])/(4*np.sqrt(2.0))

def cascade(levels=11):
    """D4 scaling function on [0,3]: exact integer values (eigenvector of the refinement matrix), then dyadic refinement phi(x)=sqrt2*sum h_k phi(2x-k)."""
    phi_int = {0: 0.0, 1: (1+SQ3)/2, 2: (1-SQ3)/2, 3: 0.0}
    n = 3*2**levels
    v = np.zeros(n+1); step = 2**levels
    for i, y in phi_int.items():
        v[i*step] = y
    for lev in range(1, levels+1):
        s = 2**(levels-lev)
        for i in range(s, n, 2*s):
            total = 0.0
            for k, hk in enumerate(H):
                idx = 2*i-k*2**levels
                if 0 <= idx <= n:
                    total += hk*v[idx]
            v[i] = np.sqrt(2.0)*total
    return np.linspace(0, 3, n+1), v

def phi_at(x, xs, v):
    return np.interp(x, xs, v, left=0.0, right=0.0)

def psi_at(x, xs, v):
    """psi(x)=sqrt2*sum g_k phi(2x-k), g_k=(-1)^k h_{1-k}; support [-1,2]."""
    y = np.zeros_like(x, dtype=float)
    for k in (-2, -1, 0, 1):
        y += np.sqrt(2.0)*(-1)**abs(k)*H[1-k]*phi_at(2*x-k, xs, v)
    return y
# D4 psi_{2,3}(x)=2 psi(4x-3), support [1/2,5/4]; (a) on the line, (b) Per on [0,1): the part beyond 1 moves to [0,1/4].
xs, v = cascade()
fig, axes = figure(width_mm=112, height_mm=40, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.2, wspace=.16)
p=lambda x:2*psi_at(4*x-3,xs,v)
ax=axes[0]
x=np.linspace(.3,1.35,2000); y=p(x)
ax.axvspan(1,1.35,color=YELLOW_FILL,lw=0,zorder=0)
ax.plot(x[x<=1],y[x<=1],color=BLUE,lw=1.4); ax.plot(x[x>=1],y[x>=1],color=RED,lw=1.4)
ax.axvline(1,color=MUTED,lw=.75,dashes=(3,2)); ax.axhline(0,color=MUTED,lw=.6)
ax.set_xlim(.3,1.35); ax.set_ylim(-3.4,4.2); ax.set_xticks([.5,1,1.25]); ax.set_xticklabels(['1/2','1','5/4']); ax.set_yticks([-2,0,2])
ax.text(.03,.98,r'$\psi_{2,3}$',transform=ax.transAxes,ha='left',va='top')
ax=axes[1]
x=np.linspace(0,1,2400); y1=p(x); y2=p(x+1)
ax.plot(x,y1+y2,color=BLUE,lw=1.4,label='per')
mask=x<=.25
ax.plot(x[mask],y2[mask],color=RED,lw=1.1,dashes=(3,1.5))
ax.axhline(0,color=MUTED,lw=.6); ax.set_xlim(0,1); ax.set_ylim(-3.4,4.2); ax.set_xticks([0,.25,.5,1]); ax.set_xticklabels(['0','1/4','1/2','1']); ax.set_yticks([-2,0,2])
ax.text(.42,.98,r'$\psi^{\mathrm{per}}_{2,3}$',transform=ax.transAxes,ha='center',va='top')
for ax,s in zip(axes,'ab'):
    ax.tick_params(labelsize=7,length=2,pad=1.5)
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'psi_{2,3}=2 psi(4x-3), D4, support [1/2,5/4]; Per wraps [1,5/4] to [0,1/4]'})
