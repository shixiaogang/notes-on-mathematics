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

from itertools import permutations
C=A*(1-B)  # g_i=A_i*delta+C_i，delta=x-1
def maps(pi,al):
    a_,c_=1.,0.
    for i in pi:
        a_,c_=(1-al*A[i])*a_,(1-al*A[i])*c_-al*C[i]
    return a_,c_
def rr(al):
    P=[maps(p,al) for p in permutations(range(3))]
    ea=np.mean([p[0] for p in P]); ec=np.mean([p[1] for p in P]); m=ec/(1-ea)
    ea2=np.mean([p[0]**2 for p in P]); eac=np.mean([p[0]*p[1] for p in P]); ec2=np.mean([p[1]**2 for p in P])
    return (2*eac*m+ec2)/(1-ea2)
def cyc(al):
    a_,c_=maps((0,1,2),al); return (c_/(1-a_))**2
al=np.logspace(np.log10(.004),np.log10(.2),60)
fig,ax=figure(width_mm=92,height_mm=56)
ax.loglog(al,28*al/(6-7*al),color=GREEN,lw=1.5)
ax.loglog(al,[rr(a) for a in al],color=YELLOW,lw=1.7)
ax.loglog(al,[cyc(a) for a in al],color=PURPLE,lw=1.3,ls=(0,(4,2)))
ax.text(.03,.32,'有放回',fontsize=8); ax.text(.024,.00011,'随机重排',fontsize=8); ax.text(.0115,.0065,'固定循环',fontsize=8,ha='right')
ax.set_xlabel(r'$\alpha$',labelpad=1); ax.set_ylabel('一轮结束时的目标差',labelpad=1)
print('rr .1',rr(.1),'cyc .1',cyc(.1),'wr .1',28*.1/(6-.7), 'rr .01',rr(.01),'cyc .01',cyc(.01),'wr .01',.28/(6-.07))
save(fig,HERE,'figure',{'rr_0.1':rr(.1),'cyc_0.1':cyc(.1)})
