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
# (a) Haar two-scale relation; (b) D4 phi and pieces sqrt2 h_k phi(2x-k); (c) D4 psi by formula g_k=(-1)^k h_{1-k}.
xs, v = cascade()
fig, axes = figure(width_mm=112, height_mm=40, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.2, wspace=.24)
ax=axes[0]
ax.fill_between([0,.5],0,1,color=GREEN_FILL,lw=0); ax.fill_between([.5,1],0,1,color=YELLOW_FILL,lw=0)
ax.plot([.5,.5],[0,1],color=MUTED,lw=.75,dashes=(3,2))
ax.plot([-.25,0,0,1,1,1.25],[0,0,1,1,0,0],color=BLUE,lw=1.4,solid_joinstyle='miter')
ax.axhline(0,color=MUTED,lw=.6); ax.set_xlim(-.25,1.25); ax.set_ylim(-.35,1.5); ax.set_xticks([0,.5,1]); ax.set_xticklabels(['0','1/2','1']); ax.set_yticks([0,1])
ax.text(.03,.98,r'Haar $\varphi$',transform=ax.transAxes,ha='left',va='top')
x=np.linspace(-.3,3.3,2500)
ax=axes[1]
cols=[GREEN,YELLOW,RED,PURPLE]
for k in range(4):
    ax.plot(x,np.sqrt(2)*H[k]*phi_at(2*x-k,xs,v),color=cols[k],lw=.95)
ax.plot(x,phi_at(x,xs,v),color=BLUE,lw=1.4)
ax.axhline(0,color=MUTED,lw=.6); ax.set_xlim(-.3,3.3); ax.set_ylim(-.65,1.55); ax.set_xticks([0,1,2,3]); ax.set_yticks([0,1])
ax.text(.97,.98,r'D4 $\varphi$',transform=ax.transAxes,ha='right',va='top')
ax=axes[2]
x2=np.linspace(-1.3,2.3,2500)
ax.plot(x2,psi_at(x2,xs,v),color=BLUE,lw=1.4)
ax.axhline(0,color=MUTED,lw=.6); ax.set_xlim(-1.3,2.3); ax.set_ylim(-1.55,2.05); ax.set_xticks([-1,0,1,2]); ax.set_yticks([-1,0,1])
ax.text(.97,.98,r'D4 $\psi$',transform=ax.transAxes,ha='right',va='top')
for ax,s in zip(axes,'abc'):
    ax.tick_params(labelsize=7,length=2,pad=1.5)
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'phi=sqrt2 sum h_k phi(2x-k); D4 h=(1+sqrt3,3+sqrt3,3-sqrt3,1-sqrt3)/(4 sqrt2); dyadic refinement from exact integer values'})
