from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: Rankine-Hugoniot speed is the chord slope of the flux between the two states.
fig, ax = figure(width_mm=86, height_mm=52); style(ax)
u=np.linspace(-.5,1.5,300); ax.plot(u,u**2/2,color=BLUE,lw=1.4)
ax.plot([0,1],[0,.5],color=LINE,lw=2)
ax.plot([-.5,1.5],[0,0],color=PURPLE,lw=1.1,ls='--'); ax.plot([.5,1.5],[0,1],color=PURPLE,lw=1.1,ls='--')
ax.plot([0,1],[0,.5],'o',ms=4.5,color=RED,zorder=5)
ax.text(.47,.33,'$s=1/2$',ha='right'); ax.text(1.27,.4,"$F'(1)=1$",color=PURPLE,ha='left',va='top'); ax.text(-.47,-.1,"$F'(0)=0$",color=PURPLE)
ax.text(1.03,.56,'$(u_-,F(u_-))$',ha='right',va='bottom'); ax.text(.03,-.03,'$(u_+,F(u_+))$',va='top')
ax.set_xlim(-.5,1.5); ax.set_ylim(-.17,1.15); ax.set_xlabel('$u$'); ax.set_ylabel('$F(u)$')
save(fig, HERE(__file__), 'figure', {'formula':'F=u^2/2, chord between u=0 and u=1'})
