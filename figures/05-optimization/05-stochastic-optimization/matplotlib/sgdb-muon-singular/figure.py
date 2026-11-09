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
# Muon 的奇异值映射：理想极因子 sigma->1，经典 Newton-Schulz 与五次多项式有限次迭代。
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2,sharey=True)
panel(fig,.125,.965,.97,.26,wspace=.1)
s=np.linspace(0,1,801)
def iter3(x,k):
    for _ in range(k): x=1.5*x-.5*x**3
    return x
A,B,C=3.4445,-4.7750,2.0315
def iter5(x,k):
    for _ in range(k): x=A*x+B*x**3+C*x**5
    return x
for ax in (a,b):
    ax.axhline(1,color=RED,lw=1.1,ls='--')
    ax.set_xlim(0,1); ax.set_ylim(0,1.42); ax.set_xlabel(r'$\sigma$',labelpad=1)
a.plot(s,iter3(s,1),color=YELLOW,lw=1.3); a.plot(s,iter3(s,3),color=PURPLE,lw=1.3); a.plot(s,iter3(s,5),color=GREEN,lw=1.4)
a.text(.60,.62,'$k=1$',fontsize=7.5,color=INK); a.text(.205,.62,'$k=3$',fontsize=7.5,color=INK); a.text(.07,1.10,'$k=5$',fontsize=7.5,color=INK)
a.set_ylabel('变换后的奇异值',labelpad=2)
v=iter5(s[s>=.02],5); b.fill_between(s,v.min(),v.max(),color=GREEN_FILL,lw=0)
b.plot(s,iter5(s,5),color=GREEN,lw=1.2)
print('min on [0.02,1]',iter5(s[s>=.02],5).min(),iter5(s[s>=.02],5).max(),'p(1)',A+B+C)
print('classic k=5 at .05,.1,.2',iter3(np.array([.05,.1,.2]),5))
print('fifth k=5 at .05,.1,.2,.5,1',iter5(np.array([.05,.1,.2,.5,1.]),5))
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'classic':'p(s)=1.5s-.5s^3','fifth':[A,B,C]})
