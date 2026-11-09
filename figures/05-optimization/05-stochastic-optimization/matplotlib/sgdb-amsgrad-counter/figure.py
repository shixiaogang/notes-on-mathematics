from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# Adam 与 AMSGrad 在周期线性目标上的对比（Reddi 等的构造），可行集 [-1,1]，最优解 -1。
C=3.; b2=1/(1+C*C); al0=.1
def run(ams,T=3000):
    x=1.0 if 0 else 0.0; v=0.; vh=0.; X=[];V=[]
    for t in range(1,T+1):
        g=C if t%3==1 else -1.
        v=b2*v+(1-b2)*g*g
        vh=max(vh,v); den=vh if ams else v
        X.append(x);V.append(den)
        x=np.clip(x-al0/np.sqrt(t)*g/np.sqrt(den),-1,1)
    return np.array(X),np.array(V)
XA,VA=run(False);XM,VM=run(True)
print('adam x',XA[[0,100,1000,2999]],'ams',XM[[0,100,1000,2999]],'adam v last',VA[-6:],'ams',VM[-3:])
print('b2',b2, 'al0<sqrt(1-b2)?',np.sqrt(1-b2))
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.12,.965,.97,.27,wspace=.3)
a.plot(XA,color=YELLOW,lw=1.4); a.plot(XM,color=GREEN,lw=1.4); a.axhline(-1,color=RED,lw=1,ls='--'); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('$x^{(t)}$',labelpad=1); a.set_xlim(0,3000); a.set_ylim(-1.15,1.15)
a.text(1500,.8,'Adam',fontsize=7.5); a.text(1400,-.7,'AMSGrad',fontsize=7.5)
b.plot(np.arange(1,31),VA[:30],color=YELLOW,lw=1.4,marker='o',ms=2.2,mew=0); b.plot(np.arange(1,31),VM[:30],color=GREEN,lw=1.4)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel('分母平方统计',labelpad=1); b.set_xlim(1,30)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'C':C,'beta2':b2,'alpha0':al0})
