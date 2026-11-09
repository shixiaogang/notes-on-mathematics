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
# AdaGrad 与 RMSProp 在同一读数序列（前 10 步幅度 10，其后幅度 1）上的有效系数。
g=np.r_[10*np.ones(10),np.ones(70)]; alpha=1.; rho=.9
va=vr=0.; A=[];R=[]
for x in g:
    va+=x*x; vr=rho*vr+(1-rho)*x*x; A.append(alpha/np.sqrt(va)); R.append(alpha/np.sqrt(vr))
A=np.array(A);R=np.array(R)
print('A',A[[0,9,10,30,79]],'R',R[[0,9,10,30,79]])
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.12,.965,.97,.27,wspace=.3)
a.step(range(80),g,where='post',color=BLUE,lw=1.2); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('读数幅度',labelpad=1); a.set_xlim(0,80); a.set_ylim(0,11)
b.semilogy(A,color=YELLOW,lw=1.5); b.semilogy(R,color=GREEN,lw=1.4); b.set_xlabel('$t$',labelpad=1); b.set_ylabel('有效系数',labelpad=1); b.set_xlim(0,80)
b.text(44,.031,'AdaGrad',fontsize=7.5); b.text(35,.72,'RMSProp',fontsize=7.5)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'rho':rho,'alpha':alpha})
