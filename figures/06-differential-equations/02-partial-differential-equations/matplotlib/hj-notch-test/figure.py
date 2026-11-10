from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: evaluate q+p^2/2 on the admissible test pairs at the two kinds of kink in the notch.
# Bottom kink: (q,p)=(-1/2,p), |p|<=1 (touch from below; supersolution needs >=0).
# Ridge x=t/2: (q,p)=(-s/2,s), 0<=s<=1 (touch from above; subsolution needs <=0).
fig, axs = figure(width_mm=100, height_mm=46, ncols=2)
ax=axs[0]; style(ax); P=np.linspace(-1,1,201); Y=-.5+P**2/2
ax.plot(P,Y,color=RED,lw=1.5); ax.fill_between(P,Y,0,color=RED_FILL,lw=0); ax.axhline(0,color=MUTED,lw=.85,ls=':')
ax.set_xlim(-1,1); ax.set_ylim(-.6,.2); ax.set_xticks([-1,0,1]); ax.set_ylabel('$q+p^2/2$'); sub(ax,'a','$p$')
ax=axs[1]; style(ax); S=np.linspace(0,1,201); Y=-S/2+S**2/2
ax.plot(S,Y,color=BLUE,lw=1.5); ax.fill_between(S,Y,0,color=BLUE_FILL,lw=0); ax.axhline(0,color=MUTED,lw=.85,ls=':')
ax.set_xlim(0,1); ax.set_ylim(-.6,.2); ax.set_xticks([0,.5,1]); sub(ax,'b','$s$')
save(fig,HERE,'figure',{'formula':'(a) -1/2+p^2/2; (b) -s/2+s^2/2'})
