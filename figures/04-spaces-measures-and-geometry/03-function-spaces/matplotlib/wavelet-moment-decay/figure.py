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
# (a,b) psi(x)*x, positive area blue, negative red: Haar integral -1/4, D4 integral 0.  (c) max_k |<psi_{j,k},x^2>| on [0,1): Haar -2^{j/2}(h^2/2)m, D4 exact -(sqrt3/8)2^{-5j/2}.
xs, v = cascade()
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.055, right=.985, top=.95, bottom=.27, wspace=.33)
ax=axes[0]
t=np.linspace(0,1,801); y=t*np.where(t<.5,1,-1)
ax.fill_between(t,0,y,where=y>=0,color=BLUE_FILL,lw=0,interpolate=True); ax.fill_between(t,0,y,where=y<=0,color=RED_FILL,lw=0,interpolate=True)
ax.plot(t[t<.5],y[t<.5],color=BLUE,lw=1.2); ax.plot(t[t>.5],y[t>.5],color=RED,lw=1.2)
ax.plot([.5,.5],[.5,-.5],color=MUTED,lw=.6)
ax.axhline(0,color=MUTED,lw=.6); ax.set_xlim(-.05,1.05); ax.set_ylim(-1.2,.75); ax.set_xticks([0,.5,1]); ax.set_xticklabels(['0','1/2','1']); ax.set_yticks([-1,0])
ax.text(.03,.98,r'Haar: $x\psi(x)$',transform=ax.transAxes,ha='left',va='top')
ax=axes[1]
t=np.linspace(-1,2,3001); y=t*psi_at(t,xs,v)
print('D4 integral x psi', np.trapezoid(y,t), 'x^2', np.trapezoid(t**2*psi_at(t,xs,v),t))
ax.fill_between(t,0,y,where=y>=0,color=BLUE_FILL,lw=0,interpolate=True); ax.fill_between(t,0,y,where=y<=0,color=RED_FILL,lw=0,interpolate=True)
ax.plot(t,y,color=BLUE,lw=1.1)
ax.axhline(0,color=MUTED,lw=.6); ax.set_xlim(-1.1,2.1); ax.set_ylim(-1.6,2.6); ax.set_xticks([-1,0,1,2]); ax.set_yticks([-1,0,1,2])
ax.text(.97,.98,r'D4: $x\psi(x)$',transform=ax.transAxes,ha='right',va='top')
ax=axes[2]
J=np.arange(0,11)
hv=[max(abs(2**(j/2)*(2.0**-j)**2/2*((k+.5)*2.0**-j)) for k in range(2**j)) for j in J]
dv=SQ3/8*2.0**(-2.5*J)
ax.plot(J,np.log2(hv),'-o',ms=2.8,color=YELLOW,lw=1.3,label='Haar')
ax.plot(J,np.log2(dv),'-s',ms=2.6,color=BLUE,lw=1.3,label='D4')
ax.set_xlim(-.4,10.4); ax.set_ylim(-29,0); ax.set_xticks([0,5,10]); ax.set_yticks([-25,-15,-5])
ax.set_xlabel('$j$',labelpad=0); ax.text(.03,.03,r'$\log_2\max_k|d_{j,k}|$',transform=ax.transAxes,ha='left',va='bottom')
ax.text(10.3,np.log2(hv[-1])+4.2,'Haar',ha='right',color=INK,fontsize=7.5)
ax.text(5.1,np.log2(dv[5])-3.6,'D4',ha='right',color=INK,fontsize=7.5)
for ax,s in zip(axes,'abc'):
    ax.tick_params(labelsize=7,length=2,pad=1.5)
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x psi(x): Haar integral -1/4, D4 integral 0; decay of |<psi_{j,k},x^2>|: Haar 2^{-3j/2}-order, D4 (sqrt3/8)2^{-5j/2}'})
