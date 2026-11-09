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
# 贯穿例上随机重球（alpha=0.1, beta=0.5）的读数、真梯度与 v(1-beta) 移动平均方向。固定种子 3。
a_=np.array([1.,2.,3.]); b_=np.array([-3.,0.,3.])
rng=np.random.default_rng(3)
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.125,.965,.97,.25,wspace=.32)
s=np.arange(0,16)
for bet,c in ((.5,YELLOW),(.9,GREEN)):
    a.plot(s,(1-bet)*bet**s,'-o',color=c,lw=1.2,ms=2.8,mew=0)
a.set_xlabel('读数的年龄 $s$'.replace(' $s$',''),labelpad=1); a.set_ylabel('权重',labelpad=1); a.set_xlim(0,15); a.set_ylim(0,.55)
a.text(1.6,.3,r'$\beta=0.5$',fontsize=7.5); a.text(6.8,.085,r'$\beta=0.9$',fontsize=7.5)
# 梯度从 +2 变为 -2 的固定读数，噪声用贯穿例 x=2 处读数的方差 (3 个值 5,4,-3)。
T=60; bet=.9
rd=np.where(np.arange(T)<30,2.,-2.)
pts=np.array([5.,4.,-3.]); noise=pts[rng.integers(0,3,T)]-2
g=rd+noise
m=0;M=[]
for k in range(T):
    m=bet*m+(1-bet)*g[k]; M.append(m/(1-bet**(k+1)))
b.plot(np.arange(T),g,'o',color=YELLOW,ms=2,mew=0)
b.step(np.arange(T+1),np.r_[rd,rd[-1]],where='post',color=BLUE,lw=1.1)
b.plot(np.arange(T),M,color=GREEN,lw=1.4)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel('方向',labelpad=1); b.set_xlim(0,T)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'seed':3,'beta':.9})
