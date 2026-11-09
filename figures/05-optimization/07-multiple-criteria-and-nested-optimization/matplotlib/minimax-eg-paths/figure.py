from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# GDA, EG, OGDA on xy (alpha=0.3) and on x^2/2+2xy-y^2/2 (alpha=0.1), counted by F evaluations.
J2 = np.array([[1., 2.], [-2., 1.]])
fig, axes = figure(width_mm=112, height_mm=47, ncols=3)
panels(fig, .06, .985, .975, .265, .42)
a = .3; T = 30; G = gda(A, a, T, (1, 0)); Ex = eg(A, a, T, (1, 0)); O = ogda(A, a, T, (1, 0))
ax = axes[0]; setup(ax, (-2.2, 2.2), (-2.2, 2.2), (-2, 0, 2), (-2, 0, 2), equal=True)
ax.plot(G[:, 0], G[:, 1], color=YELLOW, lw=1.5); ax.plot(Ex[:, 0], Ex[:, 1], color=GREEN, lw=1.3); ax.plot(O[:, 0], O[:, 1], color=PURPLE, lw=1.2); dot(ax, (0, 0))
def curves(ax, G, Ex, O, n):
    ax.semilogy(np.arange(len(G)), np.linalg.norm(G, axis=1), color=YELLOW, lw=1.6)
    ax.semilogy(2*np.arange(len(Ex)), np.linalg.norm(Ex, axis=1), color=GREEN, lw=1.4)
    ax.semilogy(np.arange(len(O)), np.linalg.norm(O, axis=1), color=PURPLE, lw=1.3)
ax = axes[1]; setup(ax, (0, 60), (.02, 10), (0, 30, 60), xl='读取次数', yl='距离'); ax.set_yscale('log'); curves(ax, gda(A, a, 60, (1, 0)), eg(A, a, 30, (1, 0)), ogda(A, a, 60, (1, 0)), 60)
a2 = .1; ax = axes[2]; setup(ax, (0, 60), (1e-4, 2), (0, 30, 60), xl='读取次数', yl='距离'); ax.set_yscale('log'); curves(ax, gda(J2, a2, 60, (1, 0)), eg(J2, a2, 30, (1, 0)), ogda(J2, a2, 60, (1, 0)), 60)
tags(fig, axes)
save(fig, HERE, 'figure', {'xy_alpha': a, 'sc_alpha': a2, 'z0': [1, 0]})
