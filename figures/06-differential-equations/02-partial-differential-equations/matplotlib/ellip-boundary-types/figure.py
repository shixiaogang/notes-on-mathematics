from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# -u''=1 on (0,1), u(0)=0, three conditions at x=1.
fig, ax = figure(width_mm=80, height_mm=50)
panel(fig, left=.11, right=.97, top=.96, bottom=.17)
ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4)
ax.plot(X, X-X**2/2, color=YELLOW, lw=1.5)
ax.plot(X, .75*X-X**2/2, color=PURPLE, lw=1.4)
dot(ax, 0, 0); dot(ax, 1, 0)
lab(ax, .62, .375, r"$u'(1)=0$", YELLOW)
lab(ax, .58, .215, r"$u'(1)+u(1)=0$", PURPLE, ha='left')
lab(ax, .38, .07, r"$u(1)=0$", BLUE)
ax.set_xlim(-.02, 1.04); ax.set_ylim(-.02, .56); ax.set_xticks([0, 1]); ax.set_yticks([0, .25, .5])
hat01(ax, yl='$u$')
save(fig, HERE, 'figure', {'problem': "-u''=1, u(0)=0", 'u_D': 'x(1-x)/2', 'u_N': 'x-x^2/2', 'u_R': '3x/4-x^2/2'})
