from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
rng = np.random.default_rng(21)
def noise():
    u = rng.normal(size=3); u -= u.mean(); return u/np.linalg.norm(u)
def run(eps, a, T=70):
    x = X0.copy(); d = []; G = []
    for t in range(T):
        z = x-a*grad(x); p = proj(z)[0]; q = p+eps*noise(); G.append(np.linalg.norm(x-q)/a); d.append(np.linalg.norm(x-XS)); x = q
    return np.array(d), np.array(G)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax = axs[0]; rho = np.sqrt(1-1/L)
for eps, c in ((0., GREEN), (1e-4, YELLOW), (1e-2, PURPLE)):
    d, _ = run(eps, 1/L); ax.semilogy(np.arange(len(d)), np.maximum(d, 1e-9), color=c, lw=1.4)
    if eps: ax.axhline(eps/(1-rho), color=c, lw=.85, ls=(0, (3, 2)))
setup(ax, (0, 40), (1e-7, 2), [0, 20, 40], [1e-6, 1e-3, 1], xl='$t$', yl='$\\Vert x^{(t)}-x^*\\Vert_2$')
ax = axs[1]; eps = 1e-3
for a, c in ((1/L, GREEN), (1/(10*L), YELLOW)):
    d, G = run(eps, a, T=600); ax.semilogy(np.arange(len(G)), G, color=c, lw=1.1)
    ax.axhline(eps/a, color=c, lw=.85, ls=(0, (3, 2)))
setup(ax, (0, 300), (1e-4, 3), [0, 150, 300], [1e-3, 1e-1], xl='$t$', yl='$\\Vert \\tilde G_\\alpha\\Vert_2$')
panels(fig, .1, .985, .98, .22, .33); tags(fig, axs)
save(fig, HERE, 'figure', {'seed': 21, 'noise': 'projection output perturbed in the plane sum=0, norm eps', 'rho': float(rho)})
