from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
# f(x)=x. Top row: P_j f (interval means), j=0,1,2. Bottom row: P_{j+1}f-P_j f, equal to -/+ 2^{-j-2} on the two halves of each level-j interval.
fig, axes = figure(width_mm=112, height_mm=56, nrows=2, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.98, top=.965, bottom=.125, wspace=.3, hspace=.58)
x = np.linspace(0,1,2)
for c, j in enumerate((0,1,2)):
    ax = axes[0][c]
    n = 2**j; e = np.arange(n+1)/n; m = (e[:-1]+e[1:])/2
    ax.plot(x,x,color=BLUE,lw=1.4,label='$f$')
    ax.step(e,list(m)+[m[-1]],where='post',color=GREEN,lw=1.4,solid_joinstyle='miter')
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xticks([0,1]); ax.set_yticks([0,1])
    ax.tick_params(labelsize=7, length=2, pad=1.5)
    ax.text(.04,.98,r'$P_{%d}f$'%j,transform=ax.transAxes,ha='left',va='top',color=INK)
    ax2 = axes[1][c]
    n2 = 2**(j+1); e2 = np.arange(n2+1)/n2; m2 = (e2[:-1]+e2[1:])/2
    # value of the level-j mean on each child interval
    pj = np.array([m[int(np.floor(t*n))] for t in m2])
    dv = m2-pj
    ax2.step(e2,list(dv)+[dv[-1]],where='post',color=YELLOW,lw=1.4,solid_joinstyle='miter')
    ax2.axhline(0,color=MUTED,lw=.6)
    ax2.set_xlim(0,1); ax2.set_ylim(-.32,.62); ax2.set_xticks([0,1]); ax2.set_yticks([-.25,0,.25]); ax2.set_yticklabels(['$-1/4$','0','$1/4$'])
    ax2.tick_params(labelsize=7, length=2, pad=1.5)
    ax2.text(.5,.98,r'$P_{%d}f-P_{%d}f$'%(j+1,j),transform=ax2.transAxes,ha='center',va='top',color=INK)
    ax2.set_xlabel('')
for r, s in enumerate('ab'):
    fig.text(.5,{0:.535,1:.015}[r],'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(x)=x; P_jf=interval means; detail P_{j+1}f-P_jf = -/+2^{-j-2}'})
