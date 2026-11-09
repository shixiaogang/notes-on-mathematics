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
# (a) x=0.1，N(x,0.3^2) 提议在 [0,1] 上的三种处理；(b) 五状态、提议 +-1,+-2 截断到 {1..5}，f=(1,0,1,2,3)，T=1
from math import erf
Phi=lambda z:.5*(1+erf(z/np.sqrt(2)))
fig,axes=figure(width_mm=112,height_mm=58,ncols=2); panel(fig,.085,.975,.955,.25,.3)
a=axes[0]; x0,s=.1,.3; u=np.linspace(0,1,400); phi=lambda y:np.exp(-(y-x0)**2/(2*s*s))/(s*np.sqrt(2*np.pi))
ref=sum(phi(u+2*k)+phi(2*k-u) for k in range(-4,5))
a.plot(u,phi(u),color=YELLOW,lw=1.4,ls='-'); a.plot(u,ref,color=GREEN,lw=1.5)
pl=Phi((0-x0)/s); out=pl+1-Phi((1-x0)/s); a.plot([0,0],[0,pl*4],color=YELLOW,lw=1.6,clip_on=False); a.plot([0],[pl*4],'o',ms=4,color=YELLOW,mew=0,clip_on=False)
a.plot([x0,x0],[0,out*4],color=RED,lw=1.2,ls=(0,(2,1.6))); a.plot([x0],[out*4],'o',ms=3.8,mfc='white',mec=RED,mew=.9,zorder=5)
a.set_xlim(0,1); a.set_ylim(0,2.8); a.set_xticks([0,.5,1]); a.set_xticklabels(['0','0.5','1']); a.set_yticks([0,1,2]); a.set_xlabel('$y$',labelpad=1); a.set_ylabel('提议密度',labelpad=1)
f=np.array([1,0,1,2,3.]); T=1; n=5; M=np.zeros((5,5)); q=np.zeros((5,5))
for i in range(n):
    for d in (-2,-1,1,2):
        j=min(n-1,max(0,i+d)); q[i,j]+=.25
for i in range(n):
    for j in range(n):
        if i!=j: M[i,j]=q[i,j]*min(1,np.exp(-(f[j]-f[i])/T))
    M[i,i]=1-M[i].sum()
d=np.ones(5)/5
for _ in range(20000): d=d@M
g=np.exp(-f/T); g/=g.sum(); print(q,d,g)
b=axes[1]; xs=np.arange(1,6); b.bar(xs-.19,g,.38,color=GREEN,edgecolor='none'); b.bar(xs+.19,d,.38,color=YELLOW,edgecolor='none'); b.set_xlim(.4,5.6); b.set_xticks(xs); b.set_ylim(0,.5); b.set_yticks([0,.25,.5]); b.set_yticklabels(['0','0.25','0.5']); b.set_xlabel('状态',labelpad=1); b.set_ylabel('平稳概率',labelpad=1)
tags(fig,axes); save(fig,HERE,'figure',{'atom':pl,'stationary_clipped':d.tolist(),'gibbs':g.tolist()})
