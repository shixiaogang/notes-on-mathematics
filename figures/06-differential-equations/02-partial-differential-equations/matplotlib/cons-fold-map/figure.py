from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: the map x0 -> x0+t u0(x0) is increasing before T*, has a flat point at T*, and folds after T*.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
s=np.linspace(-2.5,5.5,1000)
for ax,t,l in zip(axs,(.8,TSTAR,3),'abc'):
    style(ax); X=s+t*bump(s); ax.plot(s,X,color=BLUE,lw=1.4)
    ax.set_xlim(-2.5,5.5); ax.set_ylim(-2,7); sub(ax,l,'$x_0$')
axs[0].set_ylabel('$x$')
x0=1/np.sqrt(3); axs[1].plot([x0],[XSTAR],'o',ms=4,color=RED,zorder=4)
ax=axs[2]; y=2.55; ax.axhline(y,color=LINE,lw=.85,ls='--')
X=s+3*bump(s); sg=np.where(np.diff(np.sign(X-y)))[0]
for i in sg:
    ax.plot([s[i]],[y],'o',ms=3.5,color=RED,zorder=4)
axs[0].text(-2.1,5.6,'$t=0.8$'); axs[1].text(-2.1,5.6,'$t=T^{*}$'); axs[2].text(-2.1,5.6,'$t=3$')
save(fig, HERE(__file__), 'figure', {'formula':'X_t(x0)=x0+t/(1+x0^2), t=0.8,T*,3'})
