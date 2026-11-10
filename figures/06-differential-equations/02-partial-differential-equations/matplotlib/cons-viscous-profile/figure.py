from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: exact viscous travelling wave of Burgers tends to the jump as nu->0.
fig, ax = figure(width_mm=92, height_mm=46); style(ax)
xi=np.linspace(-3,3,2000)
for nu,c,lab,tx,ty in ((.3,SHADES[0],'$\\nu=0.3$',-2.4,.5),(.1,SHADES[1],'$\\nu=0.1$',-1.2,.62),(.02,SHADES[3],'$\\nu=0.02$',.25,.9)):
    ax.plot(xi,.5-.5*np.tanh(xi/(4*nu)),color=c,lw=1.4); ax.text(tx,ty,lab,color=c)
ax.plot([-3,0,0,3],[1,1,0,0],color=LINE,lw=1.9,ls=(0,(1.5,2)))
ax.set_xlim(-3,3); ax.set_ylim(0,1.12); ax.set_xlabel('$\\xi=x-st$'); ax.set_ylabel('$U(\\xi)$')
save(fig, HERE(__file__), 'figure', {'formula':'U=1/2-1/2 tanh(xi/(4 nu))'})
