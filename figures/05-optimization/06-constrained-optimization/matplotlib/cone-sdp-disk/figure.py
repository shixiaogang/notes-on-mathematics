from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Trace-one 2x2 symmetric matrices X=[[a,b],[b,1-a]], W=[[2,1],[1,2]], <W,X>=2+2b.
fig, ax = figure(width_mm=78, height_mm=70)
xl, yl = (-.28, 1.28), (-.72, .98)
th = np.linspace(0, 2*np.pi, 300)
ax.fill(.5+.5*np.cos(th), .5*np.sin(th), facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.0, zorder=1)
ax.plot([0, 0, 1, 1], [.92, 0, 0, .92], color=YELLOW, lw=1.5, zorder=3)
for lev in (-.5, -.2, .1):
    ax.plot(xl, [lev, lev], color=BLUE, lw=.7, ls=(0, (4, 2)), zorder=2)
dot(ax, (.5, -.5)); dot(ax, (.5, .75), RED, ms=4.5); hollow(ax, (.5, -.3), PURPLE)
ax.plot([.5], [.75], 's', color=RED, ms=4.2, mew=0, zorder=7)
setup(ax, xl, yl, [0, .5, 1], [-.5, 0, .5], xl='$a$', yl='$b$')
ax.text(.56, .79, '$(0.5,0.75)$', fontsize=7.5)
ax.text(.5, -.4, '$(0.5,-0.3)$', fontsize=7.5, va='center', ha='center')
ax.text(.5, -.62, '$X^*$', color=RED, fontsize=8, ha='center')
ax.text(.5, .12, '半正定', color=BLUE, fontsize=7.5, ha='center')
ax.text(1.03, .55, '元素非负', color=YELLOW, fontsize=7.5, rotation=90, va='center')
save(fig, HERE, 'figure', {'disk': '(a-1/2)^2+b^2<=1/4', 'objective': '2+2b', 'X*': [[.5, -.5], [-.5, .5]]})
