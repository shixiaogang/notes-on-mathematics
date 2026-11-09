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
# 贯穿例 (9,1) 处 g=(9,9) 的单方向估计 2<g,u>u 落在以 g 为圆心、过原点的圆上；右图为 m 方向平均的均方误差。
fig,A=panels(112,60,2,left=.1,right=.985,bottom=.25,wspace=.28)
rng=np.random.default_rng(3); g=np.array([9.,9.]); a=A[0]
th=np.linspace(0,2*np.pi,400); r=np.linalg.norm(g)
a.plot(g[0]+r*np.cos(th),g[1]+r*np.sin(th),color=MUTED,lw=.85)
U=sphere(rng,18); E=2*(U@g)[:,None]*U
a.plot(E[:,0],E[:,1],'o',color=GREEN,ms=3.4,mew=0,zorder=4)
a.annotate('',xy=g,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.4,shrinkA=0,shrinkB=0),zorder=5)
a.plot([g[0]],[g[1]],'o',mfc='white',mec=INK,ms=4.8,mew=.9,zorder=6)
a.text(10,6.4,r'$\nabla f$',fontsize=8,color=INK)
a.set_xlim(-6.5,24.5); a.set_ylim(-6.5,24.5); a.set_aspect('equal'); a.set_xticks([0,9,18]); a.set_yticks([0,9,18]); a.set_xlabel('$\\hat g_1$',labelpad=0); a.set_ylabel('$\\hat g_2$',labelpad=0)
b=A[1]; rng=np.random.default_rng(4); M=[1,2,4,8,16,32,64]; R=[]
for m in M:
    U=sphere(rng,40000*m); E=2*(U@g)[:,None]*U; E=E.reshape(40000,m,2).mean(1); R.append(((E-g)**2).sum(1).mean())
b.loglog(M,162/np.array(M),color=INK,lw=.85,ls=(0,(4,2))); b.loglog(M,R,'o',color=GREEN,ms=4,mew=0)
b.set_xlabel('方向数',labelpad=0); b.set_ylabel(r'均方误差',labelpad=1); b.set_xticks([1,4,16,64]); b.set_xticklabels(['1','4','16','64']); b.minorticks_off()
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'g':[9,9],'n':2,'theory':'162/m','seed':[3,4]})
