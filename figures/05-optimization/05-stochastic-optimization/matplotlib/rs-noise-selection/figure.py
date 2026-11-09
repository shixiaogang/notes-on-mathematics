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
# (a) N 个真实代价都为 0、噪声 N(0,1) 的候选，最低读数的均值及复核读数的均值；(b) 差为 Delta 的两候选，各读 n 次后选错的概率
from math import erfc
rng=np.random.default_rng(9); Ns=np.unique(np.round(np.logspace(0,3,40)).astype(int)); m=[]; re=[]
for n in Ns:
    z=rng.standard_normal((20000,int(n))); m.append(z.min(1).mean()); re.append(rng.standard_normal(20000).mean())
fig,axes=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.095,.975,.96,.26,.3)
a=axes[0]; a.axhline(0,color=RED,lw=.0); a.plot(Ns,m,color=YELLOW,lw=1.6); a.plot(Ns,re,color=GREEN,lw=1.6); a.set_xscale('log'); a.set_xlim(1,1000); a.set_ylim(-3.6,.5); a.set_xticks([1,10,100,1000]); a.set_xticklabels(['1','10','100','1000']); a.minorticks_off(); a.set_yticks([-3,-2,-1,0]); a.set_xlabel('候选数 $N$'.replace('候选数 ',''),labelpad=1); a.set_ylabel('读数均值',labelpad=1)
b=axes[1]; n=np.arange(1,101)
for r,c in ((.25,YELLOW),(.5,PURPLE),(1,GREEN)):
    p=[.5*erfc(r*np.sqrt(k/2)/np.sqrt(2)) for k in n]; b.plot(n,p,color=c,lw=1.5); print(r,p[0],p[3],p[15],p[99])
b.set_xlim(1,100); b.set_ylim(0,.5); b.set_xticks([1,50,100]); b.set_yticks([0,.25,.5]); b.set_yticklabels(['0','0.25','0.5']); b.set_xlabel('$n$',labelpad=1); b.set_ylabel('选错概率',labelpad=1)
b.text(55,.2,r'$\Delta/\sigma_\varepsilon=0.25$',fontsize=7.5); b.text(24,.075,r'$0.5$',fontsize=7.5); b.text(9,.05,r'$1$',fontsize=7.5)
print(m[0],m[-1]); tags(fig,axes); save(fig,HERE,'figure',{'seed':9,'N':Ns.tolist(),'mean_min':m})
