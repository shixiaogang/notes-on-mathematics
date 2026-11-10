from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: -u''=2, u(1)=0 with three left-end conditions.
fig, ax = figure(width_mm=92, height_mm=52); style(ax)
X=np.linspace(0,1,300)
ax.plot(X,X*(1-X),color=BLUE,lw=1.4)
ax.plot(X,1-X**2,color=YELLOW,lw=1.6)
ax.plot(X,.5+.5*X-X**2,color=PURPLE,lw=1.4)
ax.plot([0,0,0],[0,1,.5],'o',ms=3.8,color=RED); ax.plot([1],[0],'o',ms=3.8,color=RED)
ax.plot([0,.25],[1,1],'--',color=YELLOW,lw=.95); ax.plot([0,.22],[.5,.61],'--',color=PURPLE,lw=.95)
ax.text(.5,.3,'Dirichlet',color=BLUE,ha='center'); ax.text(.62,.72,'Neumann',color=YELLOW); ax.text(.1,.68,'Robin',color=PURPLE,ha='center')
ax.set_xlim(0,1.02); ax.set_ylim(0,1.08); ax.set_xticks([0,.5,1]); ax.set_xlabel('$x$'); ax.set_ylabel('$u$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':"x(1-x); 1-x^2; 1/2+x/2-x^2"})
