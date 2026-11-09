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
# AdamW 与 Adam+L2 的首步：x0=1，读数 g=-0.1，alpha=0.1，改变惩罚系数 gamma。
x0,g,al=1.,-.1,.1
ga=np.linspace(0,.5,1001)
x_w=(1-al*ga)*x0-al*np.sign(g)
x_l=x0-al*np.sign(g+ga*x0)
fig,a=figure(width_mm=82,height_mm=50)
fig.set_layout_engine(None); fig.subplots_adjust(left=.14,right=.96,top=.97,bottom=.2)
a.plot(ga,x_w,color=GREEN,lw=1.4)
m=ga<.1
a.plot(ga[m],x_l[m],color=YELLOW,lw=1.6); a.plot(ga[~m],x_l[~m],color=YELLOW,lw=1.6)
a.plot([.1,.1],[.9,1.1],color=YELLOW,lw=.8,ls=':')
a.axhline(x0,color=STROKE,lw=.8,ls='--')
a.set_xlabel(r'$\gamma$',labelpad=1); a.set_ylabel('$x^{(1)}$',labelpad=1); a.set_xlim(0,.5); a.set_ylim(.85,1.15)
a.text(.32,1.085,'AdamW',fontsize=7.5); a.text(.3,.915,'Adam + 平方惩罚梯度',fontsize=7.5); a.text(.015,1.01,'$x^{(0)}$',fontsize=7.5,color=MUTED)
print('gamma=.5',x_w[-1],x_l[-1])
save(fig,HERE,'figure',{'x0':x0,'g':g,'alpha':al})
