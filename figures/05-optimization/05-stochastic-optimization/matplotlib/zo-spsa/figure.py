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
# SPSA：n=2，四种符号向量；左图为扰动 h*Delta（h=1）与半径 h*sqrt(2) 的圆，右图为贯穿例 (9,1) 处的四个估计。
fig,A=panels(104,58,2,left=.1,right=.985,bottom=.25,wspace=.28)
a=A[0]; th=np.linspace(0,2*np.pi,300); r=2**.5
a.plot(r*np.cos(th),r*np.sin(th),color=MUTED,lw=.85)
for d,c in (((1,1),GREEN),((1,-1),YELLOW)):
    a.plot([d[0],-d[0]],[d[1],-d[1]],'-',color=c,lw=1.3,zorder=3); a.plot([d[0],-d[0]],[d[1],-d[1]],'o',color=c,ms=4.4,mew=0,zorder=4)
a.annotate('',xy=(1,0),xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=INK,lw=.9,shrinkA=0,shrinkB=0))
a.text(.5,.09,'$h$',fontsize=7.5,color=INK,ha='center')
a.text(-1.08,.25,r'$h\sqrt{2}$',fontsize=7.5,color=INK,ha='center')
a.plot([0,-1],[0,1],color=INK,lw=.85,ls=(0,(1,1.5)),zorder=5)
a.plot([0],[0],'o',mfc='white',mec=INK,ms=4,mew=.8,zorder=6)
a.set_xlim(-1.8,1.8); a.set_ylim(-1.8,1.8); a.set_aspect('equal'); a.set_xticks([-1,0,1]); a.set_yticks([-1,0,1]); a.set_xlabel(r'$h\Delta_1$',labelpad=0); a.set_ylabel(r'$h\Delta_2$',labelpad=0)
b=A[1]; g=np.array([9.,9.])
b.plot([18],[18],'o',color=GREEN,ms=5,mew=0,zorder=5); b.plot([0],[0],'o',color=YELLOW,ms=5,mew=0,zorder=5)
b.annotate('',xy=g,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.4,shrinkA=0,shrinkB=0),zorder=4)
b.plot([9],[9],'o',mfc='white',mec=INK,ms=4.8,mew=.9,zorder=6)
b.text(10.2,7.2,r'$\nabla f$',fontsize=8,color=INK); b.text(15.2,19.8,r'$\pm(1,1)$',fontsize=7.5,color=INK); b.text(1.2,-2.2,r'$\pm(1,-1)$',fontsize=7.5,color=INK)
b.set_xlim(-4,24); b.set_ylim(-4,24); b.set_aspect('equal'); b.set_xticks([0,9,18]); b.set_yticks([0,9,18]); b.set_xlabel(r'$\hat g_1$',labelpad=0); b.set_ylabel(r'$\hat g_2$',labelpad=0)
tag(fig,A[0],'(a)',.02); tag(fig,A[1],'(b)',.02)
save(fig,HERE,'figure',{'g':[9,9],'h':.1})
