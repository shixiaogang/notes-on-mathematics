from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Ridge: A=[[1,1],[1,0]], b=(2,0). H(gamma)=A'A+gamma I, x(gamma)=H^{-1}A'b. Contours at gamma=1, path, tangent, finite jump to gamma=3.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
A = np.array([[1., 1], [1, 0]]); b = np.array([2., 0])
def sol(g): return np.linalg.solve(A.T@A+g*np.eye(2), A.T@b)
ax = axs[0]
x0 = sol(1.); H = A.T@A+np.eye(2)
d = -np.linalg.solve(H, x0)
X, Y = np.meshgrid(np.linspace(-.5, 1.3, 200), np.linspace(-.3, 2.2, 200))
Z = .5*((X+Y-2)**2+(X)**2)+.5*(X**2+Y**2)
ax.contour(X, Y, Z, levels=[Z.min()+s for s in (.12, .4, .8, 1.3, 2.0, 2.8)], colors=BLUE, linewidths=.7)
G = np.geomspace(.02, 40, 300); P = np.array([sol(g) for g in G])
ax.plot(P[:, 0], P[:, 1], color=GREEN, lw=1.5, zorder=4)
x3 = sol(3.); pred = x0+2*d
ax.annotate('', xy=pred, xytext=x0, arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=1.3, mutation_scale=8, shrinkA=0, shrinkB=0), zorder=5)
opt_point(ax, x0); ax.plot(*x3, 'o', color=GREEN, ms=3.8, zorder=7)
ax.text(.45, .85, r'$\gamma=1$', fontsize=7.5)
ax.text(.24, .36, r'$\gamma=3$', fontsize=7.5, ha='right')
ax.text(.47, .03, '线性预测', fontsize=7.5, color=YELLOW, va='center')
ax.set_aspect('equal'); clean(ax, (-.5, 1.3), (-.3, 2.2), xlabel='$x_1$', ylabel='$x_2$', sub='(a)')
ax.set_xticks([0, 1]); ax.set_yticks([0, 1, 2])
ax = axs[1]
G2 = np.linspace(0, 4, 201); P2 = np.array([sol(max(g, 1e-9)) for g in G2])
ax.plot(G2, P2[:, 1], color=GREEN, lw=1.5, zorder=3)
ax.plot(G2, x0[1]+(G2-1)*d[1], color=YELLOW, lw=1.3, zorder=2)
opt_point(ax, (1, x0[1]))
ax.plot([3, 3], [pred[1], x3[1]], color=RED, lw=1.2, zorder=4)
ax.plot([3], [x3[1]], 'o', color=GREEN, ms=3.8, zorder=6)
ax.plot([3], [pred[1]], 'o', color=YELLOW, ms=3.8, zorder=6)
ax.text(1.12, 1.03, r'$x_2(\gamma)$', fontsize=8, color=GREEN)
clean(ax, (0, 4), (-.25, 2.1), xlabel=r'$\gamma$', sub='(b)', ylabel='$x_2$')
ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2])
save(fig, Path(__file__).resolve().parent, 'figure', {'x(1)': list(x0), 'dx': list(d), 'x(3)': list(x3), 'pred': list(pred)})
print(x0, d, x3, pred)
