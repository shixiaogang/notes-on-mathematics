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
# 保留亲代与整代替换，固定 sigma。(a) f=(x1^2+9x2^2)/2，sigma=0.5，lambda=5；(b) 二维 Rastrigin，sigma=0.45，lambda=5
quad=lambda x:(x[...,0]**2+9*x[...,1]**2)/2
ras=lambda x:rastrigin(x[...,0],x[...,1])
def run(F,x0,sig,G,plus,seed,lam=5):
    rng=np.random.default_rng(seed); x=np.array(x0,float); fx=float(F(x)); tr=[fx]
    for g in range(G):
        y=x+sig*rng.standard_normal((lam,2)); fy=F(y); i=int(np.argmin(fy))
        if (not plus) or fy[i]<=fx: x,fx=y[i],float(fy[i])
        tr.append(fx)
    return np.array(tr)
fig,axes=figure(width_mm=112,height_mm=58,ncols=2); panel(fig,.105,.97,.96,.25,.3)
a=axes[0]; p=run(quad,(9,1),.5,80,True,3); c=run(quad,(9,1),.5,80,False,3); c2=np.minimum.accumulate(c)
a.plot(c,color=YELLOW,lw=1.2); a.plot(c2,color=YELLOW,lw=.9,ls=(0,(3,2))); a.plot(p,color=GREEN,lw=1.5); a.set_yscale('log'); a.set_xlim(0,80); a.set_ylim(1e-3,70); a.set_xticks([0,40,80]); a.set_yticks([.001,.1,10]); a.set_yticklabels(['0.001','0.1','10']); a.minorticks_off(); a.set_xlabel('代数',labelpad=1); a.set_ylabel('$f$',labelpad=1)
b=axes[1]; P=[run(ras,(2,2),.45,200,True,s) for s in range(101,141)]; C=[run(ras,(2,2),.45,200,False,s) for s in range(101,141)]
pb=np.median(P,axis=0); cb=np.median([np.minimum.accumulate(x) for x in C],axis=0); cu=np.median(C,axis=0)
b.plot(cu,color=YELLOW,lw=1.2); b.plot(cb,color=YELLOW,lw=.9,ls=(0,(3,2))); b.plot(pb,color=GREEN,lw=1.5); b.set_xlim(0,200); b.set_ylim(0,20); b.set_xticks([0,100,200]); b.set_yticks([0,5,10,15,20]); b.set_xlabel('代数',labelpad=1); b.set_ylabel('$f$ 的中位数'.replace(' 的中位数',''),labelpad=1)
print(pb[-1],cb[-1],cu[-1],p[-1],c[-1],c2[-1])
tags(fig,axes); save(fig,HERE,'figure',{'plus_final_quad':float(p[-1]),'comma_final_quad':float(c[-1]),'median_plus_ras':float(pb[-1]),'median_comma_best_ras':float(cb[-1])})
