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
# 取整前向的直通更新：w0=0.3，a=1 时步长 0.4 到 0.7，损失下降；a=0.3 时步长 4/3 到 0.7，损失上升。
fig,a=figure(width_mm=96,height_mm=52)
fig.set_layout_engine(None); fig.subplots_adjust(left=.11,right=.96,top=.97,bottom=.19)
Q=lambda w: np.floor(w+.5)
w=np.linspace(-.5,1.5,2001)
for av,col in ((1.,BLUE),(.3,GREEN)):
    F=.5*(Q(w)-av)**2; F2=F.copy(); F2[np.abs(np.diff(F,prepend=F[0]))>1e-6]=np.nan
    a.plot(w,F2,color=col,lw=1.5)
a.axvline(.5,color=MUTED,lw=.75,ls=':')
pts=[(.3,.5,BLUE,'o'),(.7,0,BLUE,'s'),(.3,.045,GREEN,'o'),(.7,.245,GREEN,'s')]
for x,y,c,m in pts: a.plot([x],[y],m,color=c,ms=4.6,mew=0,zorder=5)
a.set_xlim(-.5,1.5); a.set_ylim(-.04,.58); a.set_xlabel('$w$',labelpad=1); a.set_ylabel('$F(w)$',labelpad=1)
a.text(.72,.03,'下降',fontsize=7.5); a.text(.72,.265,'上升',fontsize=7.5)
a.text(.51,.53,'阈值',fontsize=7.5,color=MUTED)
save(fig,HERE,'figure',{'w0':.3})
