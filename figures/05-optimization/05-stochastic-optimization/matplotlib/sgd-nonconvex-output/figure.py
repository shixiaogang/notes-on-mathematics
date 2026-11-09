from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿例：f_i(x)=a_i(x-b_i)^2/2，a=(1,2,3)，b=(-3,0,3)；f(x)=(x-1)^2+5，x*=1。
A = np.array([1., 2., 3.]); B = np.array([-3., 0., 3.])
def gi(x): return A*(x-B)
def panel(fig, left, right, top, bottom, wspace=.3, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')

# 非凸例：f_i(x)=1-cos x+c_i x，c=(-2,0,2)；f=1-cos x，L=1，sigma^2=8/3，f_inf=0。
rng=np.random.default_rng(34)
c=np.array([-2.,0,2]);al=.1;T=800;R=6000
X=np.zeros((R,T)); x=np.full(R,2.5)
for t in range(T):
    X[:,t]=x
    x=x-al*(np.sin(x)+c[rng.integers(3,size=R)])
g2=(np.sin(X)**2).mean(0); runavg=np.cumsum(g2)/np.arange(1,T+1)
D=1-np.cos(2.5); s2=8/3
tt=np.arange(1,T+1); bd=2*D/(al*tt)+al*s2
tau=rng.integers(T,size=R); out=X[np.arange(R),tau]
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.085,.985,.97,.25,wspace=.3)
xx=np.linspace(-5,11,500)
h,ed=np.histogram(out,bins=64,range=(-5,11),density=True)
a.bar(ed[:-1],h/h.max()*1.8,width=ed[1]-ed[0],align='edge',color=GREEN_FILL,edgecolor='none',zorder=1)
a.plot(xx,1-np.cos(xx),color=BLUE,lw=1.5,zorder=3)
a.plot([0,2*np.pi],[0,0],'o',ms=4.4,color=RED,mew=0,zorder=6,clip_on=False)
a.set_xlim(-5,11); a.set_ylim(0,2.3); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f(x)$',labelpad=1)
b.loglog(tt,bd,color=PURPLE,lw=1.2,ls=(0,(4,2))); b.loglog(tt,runavg,color=GREEN,lw=1.5)
b.text(50,1.5,'上界',fontsize=7.5); b.text(4,.25,'实际',fontsize=7.5)
b.set_xlabel('$T$',labelpad=1); b.set_ylabel('平均平方梯度',labelpad=1); b.set_xlim(1,T)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
print('runavg end',runavg[-1],'bd',bd[-1],'D',D,'near0or2pi',np.mean(np.abs(out)<1.5),np.mean(np.abs(out-2*np.pi)<1.5))
save(fig,HERE,'figure',{'seed':34,'runs':R,'runavg_end':float(runavg[-1]),'bound_end':float(bd[-1])})
