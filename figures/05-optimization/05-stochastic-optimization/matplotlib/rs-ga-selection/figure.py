from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 五个候选 f=(-24,-20,-19,-15,-10) 的选中概率
N=5; x=np.arange(1,6); w=.2; c=np.array([-24,-20,-19,-15,-10.])
t2=[((N-r)**2-(N-r-1)**2)/N**2 for r in range(N)]; t3=[((N-r)**3-(N-r-1)**3)/N**3 for r in range(N)]; lin=[(.5+(N-1-r)/(N-1))/N for r in range(N)]; F=c.max()-c+1; pr=F/F.sum()
fig,ax=figure(width_mm=100,height_mm=52)
for o,y,col in ((-1.5,lin,YELLOW),(-.5,t2,GREEN),(.5,t3,PURPLE),(1.5,pr,BLUE)): ax.bar(x+o*w,y,w,color=col,edgecolor='none')
ax.set_xticks(x); ax.set_xticklabels(['-24','-20','-19','-15','-10']); ax.set_xlim(.45,5.55); ax.set_ylim(0,.53); ax.set_yticks([0,.25,.5]); ax.set_yticklabels(['0','0.25','0.5']); ax.set_xlabel('$f$',labelpad=1); ax.set_ylabel('选中概率',labelpad=1)
print(lin,t2,t3,pr); save(fig,HERE,'figure',{'costs':c.tolist(),'linear_rank_s1.5':lin,'tournament2':t2,'tournament3':t3,'proportional_F=fmax-f+1':pr.tolist()})
