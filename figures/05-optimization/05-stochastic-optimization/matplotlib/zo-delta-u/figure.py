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
# 扰动尺度的取舍：f=sum(exp(x_i)-x_i-1)，n=2，sigma=0.2，x0=(1,1)，alpha=0.02，T=3000，200 次运行，末 500 步平均的目标差。
fig,ax=figure(width_mm=92,height_mm=56)
rng=np.random.default_rng(31)
ff=lambda x:(np.exp(x)-x-1).sum(-1)
D=np.logspace(-1.7,.6,14); R=200; T=3000; O=[]
for d in D:
    x=np.ones((R,2)); acc=0.
    for t in range(T):
        u=sphere(rng,R); z=.2*rng.standard_normal((R,2)); Dq=(ff(x+d*u)+z[:,0]-ff(x-d*u)-z[:,1])/(2*d); x=x-.02*2*Dq[:,None]*u
        if t>=T-500: acc+=ff(x).mean()
    O.append(acc/500)
O=np.array(O); k=O.argmin()
ax.loglog(D,O,'-o',color=GREEN,lw=1.4,ms=3.6,mew=0); ax.plot([D[k]],[O[k]],'o',color=RED,ms=5,mew=0,zorder=6)
ax.set_xlabel(r'$\delta$',labelpad=1); ax.set_ylabel('平均目标差',labelpad=1)
save(fig,HERE,'figure',{'alpha':.02,'sigma':.2,'T':T,'runs':R,'best_delta':float(D[k]),'best':float(O[k]),'values':O.tolist()})
print(D,O)
