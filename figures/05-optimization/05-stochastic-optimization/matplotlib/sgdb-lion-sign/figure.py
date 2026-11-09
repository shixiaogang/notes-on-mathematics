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
# Lion：(a) 同向不同幅读数的候选方向与符号；(b) 精确梯度下固定步长在二次目标上的残差平台。
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.125,.965,.97,.26,wspace=.32)
c=np.array([.1,3.]); w=.36; t=np.array([0,1])
a.bar(t-w/2,c,w,color=YELLOW); a.bar(t+w/2,np.sign(c),w,color=GREEN)
a.set_xticks(t); a.set_xticklabels(['$x_1$','$x_2$']); a.set_ylabel('方向分量',labelpad=1); a.set_ylim(0,3.4)
a.text(1-w/2,3.08,'$3$',ha='center',fontsize=7.5); a.text(-w/2,.18,'$0.1$',ha='center',fontsize=7.5); a.text(w/2,1.08,'$1$',ha='center',fontsize=7.5); a.text(1+w/2,1.08,'$1$',ha='center',fontsize=7.5)
H=np.array([1.,9.])
def run(al,T=200,b1=.9,b2=.99):
    x=np.array([9.,1.]); m=np.zeros(2); out=[]
    for k in range(T):
        out.append(.5*(H*x*x).sum())
        g=H*x; d=np.sign(b1*m+(1-b1)*g); x=x-al*d; m=b2*m+(1-b2)*g
    return np.array(out)
for al,col,lab in ((.1,GREEN,r'$\alpha=0.1$'),(.02,YELLOW,r'$\alpha=0.02$')):
    y=run(al,1200); print(al,y[-200:].max()); ym=np.array([y[max(0,k-19):k+1].max() for k in range(len(y))]); b.semilogy(ym,color=col,lw=1.25)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel('$f$',labelpad=1); b.set_xlim(0,1200); b.set_ylim(5e-4,100)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'H':'diag(1,9)','x0':[9,1],'beta1':.9,'beta2':.99})
