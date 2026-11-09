from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# From x0=(4,0): objective values under MGDA vs gradient descent on the fixed sum w=(1/2,1/2); residual of MGDA.
def wgd(x0, T, w=.5):
    H = np.diag([w+(1-w), 9*w+(1-w)]); x = np.array(x0, float); P = [x.copy()]; a = 1/np.max(np.diag(H))
    for _ in range(T):
        g1, g2 = gm(x); x = x-a*(w*g1+(1-w)*g2); P.append(x.copy())
    return np.array(P)
T = 40; P, R, A_, _ = mgda((4, 0), T); Q = wgd((4, 0), T); V = fm(P).T; W = fm(Q).T; t = np.arange(T+1)
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .985, .22, .28)
ax = axes[0]; setup(ax, (0, 40), (2, 9), range(0, 41, 10), range(2, 10, 2), '$t$', '目标值')
ax.plot(t, V[:, 0], color=GREEN, lw=1.4); ax.plot(t, V[:, 1], color=GREEN, lw=1.4, ls=(0, (3, 2)))
ax.plot(t, W[:, 0], color=YELLOW, lw=1.7); ax.plot(t, W[:, 1], color=YELLOW, lw=1.7, ls=(0, (3, 2)))
ax.text(31, 7.3, '$f_1$', color=INK); ax.text(31, 3.5, '$f_2$', color=INK)
ax = axes[1]; setup(ax, (0, 40), (1e-4, 8), range(0, 41, 10), None, '$t$', r'$\Vert\bar g^{(t)}\Vert_2$')
ax.semilogy(t[:-1], R, color=GREEN, lw=1.4); ax.tick_params(axis='y', which='minor', length=0)
ax.set_ylim(1e-4, 8); tags(fig, axes)
save(fig, HERE, 'figure', {'mgda_end': V[-1].tolist(), 'wgd_end': W[-1].tolist()}); print(V[0], V[-1], W[-1], W[:,1].max(), R[-1])
