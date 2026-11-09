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
# Adam 的零初始化修正：常数读数 g=1 下未修正和修正后的方向系数。
b1,b2=.9,.999; T=np.arange(1,61)
m=1-b1**T; v=1-b2**T
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.12,.965,.97,.27,wspace=.3)
s=np.arange(0,31); w=(1-b1)*b1**(s)
a.bar(s,w,.72,color=BLUE); a.set_xlabel('读数的年龄',labelpad=1); a.set_ylabel('权重',labelpad=1); a.set_ylim(0,.108)
b.plot(T,m/np.sqrt(v),color=YELLOW,lw=1.5); b.axhline(1,color=GREEN,lw=1.4); b.set_xlabel('$t+1$',labelpad=1); b.set_ylabel('一步位移系数',labelpad=1); b.set_xlim(1,60); b.set_ylim(0,7.5)
b.text(32,5.6,'未修正',fontsize=7.5); b.text(4,1.12,'修正后',fontsize=7.5)
print('uncorrected',(m/np.sqrt(v))[[0,1,9,29,59]])
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'b1':b1,'b2':b2})
