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
# 四种差分的查询点，贯穿例 f=(x1^2+9x2^2)/2 在 (9,1) 附近；为便于观察取 h=0.4。
fig,A=panels(112,38,4,left=.015,right=.985,top=.98,bottom=.14,wspace=.08)
x=X0; h=.4
X,Y=np.meshgrid(np.linspace(8.1,9.9,300),np.linspace(.1,1.9,300))
def pts(a,P,cen):
    for p in P:
        a.plot([x[0],p[0]],[x[1],p[1]],color=GREEN,lw=.85,ls=(0,(3,2)),zorder=3)
        a.plot([p[0]],[p[1]],'o',color=GREEN,ms=4.2,mew=0,zorder=5)
    if cen: a.plot([x[0]],[x[1]],'o',color=GREEN,ms=4.2,mew=0,zorder=5)
    else: a.plot([x[0]],[x[1]],'o',mfc='white',mec=GREEN,ms=4.2,mew=.9,zorder=5)
e1=np.array([1.,0]);e2=np.array([0,1.]);u=np.array([.6,.8]);d=np.array([1.,-1.])
S=[([x+h*e1,x+h*e2],True),([x+h*e1,x-h*e1,x+h*e2,x-h*e2],False),([x+h*u,x-h*u],False),([x+h*d,x-h*d],False)]
for a,(P,c),t in zip(A,S,'abcd'):
    a.contour(X,Y,.5*(X**2+9*Y**2),levels=[37,41,45,49,53],colors=[BLUE],linewidths=.65); pts(a,P,c)
    a.set_xlim(8.1,9.9); a.set_ylim(.1,1.9); a.set_aspect('equal'); a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values(): s.set_visible(False)
    tag(fig,a,f'({t})',.02)
save(fig,HERE,'figure',{'x':[9,1],'h':h,'u':[.6,.8],'Delta':[1,-1]})
