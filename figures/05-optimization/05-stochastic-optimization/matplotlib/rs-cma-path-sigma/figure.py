from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 累计路径的两种情形（给定位移序列）与 CMA-ES 在五维球面 f=|x|^2/2 上的 sigma 轨迹
A=[(1.0,.15),(.8,.75),(1.15,-.05),(.75,.7)]; B=[(1.2,.75),(-.65,.95),(-1.15,-.8),(.75,-.7)]
fig,axes=figure(width_mm=112,height_mm=52,ncols=3,gridspec_kw={'width_ratios':[1.05,1.05,1.3]}); panel(fig,.06,.975,.97,.26,.3)
def draw(ax,seq):
    p=np.zeros(2)
    for s in seq:
        q=p+s; ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.3,mutation_scale=7,shrinkA=0,shrinkB=0)); p=q
    ax.annotate('',xy=p,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=YELLOW,lw=1.5,mutation_scale=8,shrinkA=0,shrinkB=0)); ax.plot([0],[0],'o',ms=3.4,color=INK,mew=0,zorder=6)
    ax.set_xlim(-.9,4.0); ax.set_ylim(-.9,3.0); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False); return float(np.hypot(*p))
l1=draw(axes[0],A); l2=draw(axes[1],B); print(l1,l2)
def cma(s,G,seed,n=5,lam=10):
    r=np.random.default_rng(seed); m=np.full(n,3.); mu=lam//2; w=np.log(mu+.5)-np.log(np.arange(1,mu+1)); w/=w.sum(); me=1/(w**2).sum(); cs=(me+2)/(n+me+5); ds=1+2*max(0,np.sqrt((me-1)/(n+1))-1)+cs; chi=np.sqrt(n)*(1-1/(4*n)+1/(21*n*n)); ps=np.zeros(n); S=[s]
    for g in range(G):
        z=r.standard_normal((lam,n)); x=m+s*z; o=np.argsort((x**2).sum(1))[:mu]; zw=w@z[o]; m=m+s*zw; ps=(1-cs)*ps+np.sqrt(cs*(2-cs)*me)*zw; s*=np.exp(cs/ds*(np.linalg.norm(ps)/chi-1)); S.append(s)
    return S,float((m**2).sum()/2)
c=axes[2]; a,fa=cma(1e-3,160,1); b,fb=cma(10.,160,2); c.plot(a,color=GREEN,lw=1.5); c.plot(b,color=YELLOW,lw=1.5); c.set_yscale('log'); c.set_xlim(0,160); c.set_ylim(1e-6,30); c.set_xticks([0,80,160]); c.set_yticks([1e-5,1e-3,1e-1,10]); c.minorticks_off(); c.set_xlabel('代数',labelpad=1); c.set_ylabel(r'$\sigma$',labelpad=1)
print(max(a),fa,fb); tags(fig,axes); save(fig,HERE,'figure',{'aligned_len':l1,'cancelled_len':l2,'peak_sigma_from_small':max(a)})
