from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panels(w,h,n,left=.07,right=.99,top=.97,bottom=.22,wspace=.25,rows=1,**k):
    fig=figure(width_mm=w,height_mm=h)[0]; fig.clf(); fig.set_layout_engine(None)
    A=[fig.add_subplot(rows,n,i+1,**k) for i in range(n*rows)]
    fig.subplots_adjust(left=left,right=right,top=top,bottom=bottom,wspace=wspace)
    return fig,A
def tag(fig,ax,s,y):
    p=ax.get_position(); fig.text((p.x0+p.x1)/2,y,s,ha='center',va='bottom')
H2=np.array([1.,9.]); X0=np.array([9.,1.])
def f2(x): return .5*(H2*np.asarray(x,float)**2).sum(-1)
def g2(x): return H2*np.asarray(x,float)
def sphere(rng,k,n=2):
    u=rng.standard_normal((k,n)); return u/np.linalg.norm(u,axis=1,keepdims=True)
# 单点估计的散布：贯穿例 (9,1)，delta=0.1；(a) 原函数值 (b) 减去常数 45 后。
fig,A=panels(112,60,2,left=.125,right=.985,bottom=.25,wspace=.32)
rng=np.random.default_rng(8); U=sphere(rng,60); d=.1; x=X0; n=2
Y=f2(x+d*U)
E1=(n/d)*Y[:,None]*U; E2=(n/d)*(Y-45)[:,None]*U
g=np.array([9.,9.])
A[0].plot(E1[:,0],E1[:,1],'o',color=GREEN,ms=3,mew=0); A[1].plot(E2[:,0],E2[:,1],'o',color=GREEN,ms=3,mew=0)
for a,L in zip(A,(1120,24)):
    a.annotate('',xy=g,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.4,shrinkA=0,shrinkB=0),zorder=5)
    a.plot([g[0]],[g[1]],'o',mfc='white',mec=INK,ms=4,mew=.8,zorder=6)
    a.set_aspect('equal'); a.set_xlabel(r'$\hat g_1$',labelpad=0); a.set_ylabel(r'$\hat g_2$',labelpad=0)
A[0].set_xlim(-1120,1120); A[0].set_ylim(-1120,1120); A[0].set_xticks([-900,0,900]); A[0].set_yticks([-900,0,900])
A[1].set_xlim(-11,29); A[1].set_ylim(-11,29); A[1].set_xticks([0,9,18]); A[1].set_yticks([0,9,18])
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'x':[9,1],'delta':d,'seed':8,'mean_norm_a':float(np.linalg.norm(E1,axis=1).mean())})
