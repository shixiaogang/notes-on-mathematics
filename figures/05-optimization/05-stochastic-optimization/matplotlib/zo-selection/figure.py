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
# 选择偏差：K 个候选的真实值都为 1，读数噪声标准差 1。(a) K=12 的一次读数，(b) 最小读数与独立复评的均值随 K 变化（1e5 次）。
fig,A=panels(112,52,2,left=.085,right=.985,bottom=.28,wspace=.25)
rng=np.random.default_rng(2); y=1+rng.standard_normal(12); k=y.argmin(); a=A[0]
a.axhline(1,color=BLUE,lw=1.4); a.plot(range(1,13),y,'o',color=GREEN,ms=4,mew=0,zorder=4)
a.plot([k+1],[y[k]],'o',color=RED,ms=5.6,mew=0,zorder=5)
a.set_xlim(.3,12.7); a.set_ylim(-1.7,3.6); a.set_xticks([1,6,12]); a.set_yticks([-1,0,1,2,3]); a.set_xlabel('候选编号',labelpad=0); a.set_ylabel('读数',labelpad=1)
K=[1,2,4,8,16,32,64,128,256]; M=[];R=[]
for m in K:
    Z=rng.standard_normal((100000,m)); M.append(1+Z.min(1).mean()); R.append(1+rng.standard_normal(100000).mean())
b=A[1]; b.semilogx(K,M,'-o',color=RED,lw=1.4,ms=3.6,mew=0); b.semilogx(K,R,'-o',color=GREEN,lw=1.4,ms=3.6,mew=0); b.axhline(1,color=BLUE,lw=1.2,zorder=1)
b.set_xticks([1,4,16,64,256]); b.set_xticklabels(['1','4','16','64','256']); b.minorticks_off(); b.set_ylim(-2.1,1.5); b.set_yticks([-2,-1,0,1]); b.set_xlabel('候选数',labelpad=0); b.set_ylabel('均值',labelpad=1)
b.text(6,-.95,'最小读数',fontsize=7.5,color=INK,ha='right'); b.text(40,1.16,'独立复评',fontsize=7.5,color=INK,ha='center')
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'seed':2,'min_of':dict(zip(map(str,K),M))})
