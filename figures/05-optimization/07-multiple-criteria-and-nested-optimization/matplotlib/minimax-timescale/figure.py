from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# f=-x^2/2+2xy-y^2/2: step ratio r=beta/alpha decides whether y tracks 2x.
J = lambda r: np.array([[-1., 2.], [-2*r, r]])
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .975, .235, .3)
a = .1; T = 40; R1 = gda(J(1), a, T, (1, 0)); R4 = gda(J(4), a, T, (1, 0))
g = np.linspace(-2.2, 2.2, 300); X, Y = np.meshgrid(g, g)
ax = axes[0]; setup(ax, (-1.8, 1.8), (-2.2, 2.2), (-1, 0, 1), (-2, -1, 0, 1, 2), equal=False)
ax.contour(X, Y, -.5*X**2+2*X*Y-.5*Y**2, levels=[-3, -1.5, -.5, .5, 1.5, 3], colors=BLUE, linewidths=.7, linestyles='solid')
s = np.array([-1.1, 1.1]); ax.plot(s, 2*s, color=PURPLE, lw=1.2, zorder=3)
ax.plot(R1[:, 0], R1[:, 1], color=YELLOW, lw=1.4, zorder=4); ax.plot(R4[:, 0], R4[:, 1], color=GREEN, lw=1.4, zorder=5); dot(ax, (0, 0))
ax = axes[1]; t = np.arange(T+1); setup(ax, (0, T), (1e-2, 8), range(0, T+1, 10), xl='$t$', yl=r'$\Vert\bm{z}^{(t)}\Vert_2$'.replace(r'\bm{z}', 'z').replace(r'\Vert', '|').replace('_2', ''))
ax.set_yscale('log'); ax.semilogy(t, np.linalg.norm(R1, axis=1), color=YELLOW, lw=1.6); ax.semilogy(t, np.linalg.norm(R4, axis=1), color=GREEN, lw=1.4)
ax.text(30, 2.8, '$r=1$', color=INK, fontsize=7.5); ax.text(26, .012*2.5, '$r=4$', color=INK, fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '-x^2/2+2xy-y^2/2', 'alpha': a, 'r': [1, 4]})
print(R1[:4], R4[:4], R1[-1], R4[-1])
