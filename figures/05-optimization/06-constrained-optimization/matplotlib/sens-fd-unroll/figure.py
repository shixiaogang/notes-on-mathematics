from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# (a) Central finite difference of x2(theta) on the price example, inner solves by gradient descent to gradient tolerance eps.
# (b) Ridge gamma=1: unrolled GD derivative and implicit derivative evaluated at the iterate.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]
rng = np.random.default_rng(519)
def inner(th, tol, s0):
    # reduced variable s=x1, x2=2-th*s; v(s)=.5(s-1-th)^2+.5(1-th*s)^2; gradient descent from s0 until |g|<=tol
    s = s0; a = .5/(1+th**2)
    for _ in range(200000):
        g = (s-1-th)-th*(1-th*s)
        if abs(g) <= tol: break
        s -= a*g
    return 2-th*s
true = -1.0
H = np.geomspace(1e-6, .3, 45)
for tol, col in [(1e-4, YELLOW), (1e-8, GREEN)]:
    err = []
    for h in H:
        e = [abs((inner(1+h, tol, rng.uniform(0, 3))-inner(1-h, tol, rng.uniform(0, 3)))/(2*h)-true) for _ in range(40)]
        err.append(np.median(e))
    ax.loglog(H, err, color=col, lw=1.3)
ax.text(3e-5, 4, r'$\varepsilon=10^{-4}$', fontsize=7.5, color=YELLOW)
ax.text(1.5e-6, 6e-6, r'$\varepsilon=10^{-8}$', fontsize=7.5, color=GREEN)
clean(ax, None, (1e-7, 60), xlabel='$h$', sub='(a)', ylabel='差分误差'); ax.minorticks_off(); ax.set_xticks([1e-6, 1e-4, 1e-2]); ax.set_yticks([1e-6, 1e-3, 1])
ax = axs[1]
A = np.array([[1., 1], [1, 0]]); b = np.array([2., 0]); g = 1.; H2 = A.T@A+g*np.eye(2); q = A.T@b
xs = np.linalg.solve(H2, q); ds = -np.linalg.solve(H2, xs)
L = np.linalg.eigvalsh(H2).max(); al = 1/L
x = np.zeros(2); D = np.zeros(2); eU, eI, eX = [], [], []
T = 41
for t in range(T):
    eU.append(np.linalg.norm(D-ds)); eI.append(np.linalg.norm(-np.linalg.solve(H2, x)-ds)); eX.append(np.linalg.norm(x-xs))
    grad = H2@x-q
    D = D-al*(H2@D+x); x = x-al*grad
ax.semilogy(range(T), eU, color=YELLOW, lw=1.4); ax.semilogy(range(T), eI, color=GREEN, lw=1.4)
ax.text(18, 2.1e-1, '展开', fontsize=7.5, color=YELLOW); ax.text(5, 1.4e-4, '隐式', fontsize=7.5, color=GREEN)
clean(ax, (0, 40), (1e-6, 3), xlabel='$t$', sub='(b)', ylabel='导数误差'); ax.minorticks_off(); ax.set_yticks([1e-5, 1e-3, 1e-1])
save(fig, Path(__file__).resolve().parent, 'figure', {'ridge_gamma': g, 'alpha': float(al), 'eU_last': eU[-1], 'eI_last': eI[-1]})
print(eU[0], eU[20], eU[-1], eI[0], eI[20], eI[-1])
