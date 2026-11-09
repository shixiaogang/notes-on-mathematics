from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Spectral radius versus step size on two linear F.
J2 = np.array([[1., 2.], [-2., 1.]])
def og(J, a):
    I = np.eye(2); return rho(np.block([[I-2*a*J, a*J], [I, 0*I]]))
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .975, .235, .3)
for ax, J, xm, ym in ((axes[0], A, 1.2, (.6, 1.5)), (axes[1], J2, .8, (0, 1.5))):
    al = np.linspace(.002, xm, 800)
    setup(ax, (0, xm), ym, None, None, xl='步长', yl='谱半径')
    ax.axhline(1, color=MUTED, lw=.85, ls=(0, (3, 2)))
    ax.plot(al, [rho(np.eye(2)-a*J) for a in al], color=YELLOW, lw=1.6)
    ax.plot(al, [rho(np.eye(2)-a*J+a*a*J@J) for a in al], color=GREEN, lw=1.4)
    ax.plot(al, [og(J, a) for a in al], color=PURPLE, lw=1.3)
axes[0].text(1.02, 1.3, 'GDA', fontsize=7.5); axes[0].text(.9, .78, 'EG', fontsize=7.5); axes[0].text(.28, .72, 'OGDA', fontsize=7.5)
axes[1].text(.5, 1.3, 'GDA', fontsize=7.5); axes[1].text(.49, .14, 'EG', fontsize=7.5); axes[1].text(.33, 1.3, 'OGDA', fontsize=7.5, ha='right')
tags(fig, axes)
save(fig, HERE, 'figure', {'J': ['[[0,1],[-1,0]]', '[[1,2],[-2,1]]']})
