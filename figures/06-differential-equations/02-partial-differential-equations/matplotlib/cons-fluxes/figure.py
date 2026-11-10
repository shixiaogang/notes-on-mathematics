from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: flux shapes and their slopes (speeds) for linear, Burgers and traffic fluxes.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
cases=[(np.linspace(-1,1,200),lambda u:.6*u,lambda u:.6+0*u,'a',(-1,1)),
       (np.linspace(-1,1,200),lambda u:u**2/2,lambda u:u,'b',(-1,1)),
       (np.linspace(0,1,200),lambda u:u*(1-u),lambda u:1-2*u,'c',(0,1))]
for ax,(u,F,dF,l,lim) in zip(axs,cases):
    style(ax); ax.axhline(0,color=MUTED,lw=.7)
    ax.plot(u,F(u),color=BLUE,lw=1.4); ax.plot(u,dF(u),color=PURPLE,lw=1.2,ls='--')
    ax.set_xlim(*lim); ax.set_ylim(-1.1,1.1); sub(ax,l,'$u$')
axs[0].text(-.95,-.75,'$F$',color=BLUE); axs[0].text(-.2,.72,"$F'$",color=PURPLE)
axs[1].text(-.92,.55,'$F$',color=BLUE); axs[1].text(.5,.72,"$F'$",color=PURPLE)
axs[2].text(.42,.36,'$F$',color=BLUE); axs[2].text(.04,.52,"$F'$",color=PURPLE)
save(fig, HERE(__file__), 'figure', {'formula':'F=0.6u, u^2/2, u(1-u) and F-prime'})
