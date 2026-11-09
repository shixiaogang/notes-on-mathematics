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
# Metropolis 接受概率与 Gibbs 权重，f=(3,1,3,5,2,0,2)
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .1, .985, .95, .265, .3)
a=axes[0]; d=np.linspace(-2,6,500)
for T,c,ls in ((.5,PURPLE,'-'),(1,GREEN,'-'),(2,YELLOW,'-')):
    a.plot(d,np.minimum(1,np.exp(-d/T)),color=c,lw=1.5)
a.text(.62,.1,'$T=0.5$',fontsize=7.5,ha='right',color=INK); a.text(2.9,.125,'$T=1$',fontsize=7.5,color=INK,ha='center',va='center'); a.text(3.2,.38,'$T=2$',fontsize=7.5,ha='left',va='bottom',color=INK)
a.set_xlim(-2,6); a.set_ylim(0,1.06); a.set_xticks([-2,0,2,4,6]); a.set_yticks([0,.5,1]); a.set_yticklabels(['0','0.5','1']); a.set_xlabel(r'$f(y)-f(x)$',labelpad=1); a.set_ylabel('接受概率',labelpad=4)
b=axes[1]; f=np.array([3,1,3,5,2,0,2.]); s=np.arange(1,8); w=.38
out={}
for T,c,o in ((2,YELLOW,-w/2),(.5,GREEN,w/2)):
    p=np.exp(-f/T); p/=p.sum(); b.bar(s+o,p,w,color=c,edgecolor='none'); out[T]=p.tolist()
b.set_xticks(s); b.set_xlim(.4,7.6); b.set_ylim(0,.95); b.set_yticks([0,.25,.5,.75]); b.set_yticklabels(['0','0.25','0.5','0.75']); b.set_xlabel('$x$',labelpad=1); b.set_ylabel(r'$\pi_T(x)$',labelpad=1)
b.annotate('$T=0.5$',xy=(6.19,.85),xytext=(4.6,.84),fontsize=7.5,ha='center',va='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1)); b.annotate('$T=2$',xy=(5.81,.35),xytext=(4.1,.45),fontsize=7.5,ha='center',va='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
tags(fig,axes); save(fig,HERE,'figure',{'gibbs':out})
