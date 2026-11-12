"""Normal scale mixture with W~Exp(1). (a) ln density: Laplace(0,1/sqrt2) vs N(0,1); (b) common scale sqrt(W)(Z1,Z2); (c) independent scales. 2000 samples, seed 716.
Also numerically checks that int e^{-w} N(x;0,w) dw equals the Laplace density."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 3000
fig, (a, b, c) = figure(width_mm=112, height_mm=46, ncols=3)
x = np.linspace(-5, 5, 801)
lap = np.exp(-np.sqrt(2)*np.abs(x))/np.sqrt(2)
w = np.linspace(1e-6, 60, 200001)
check = [float(np.trapezoid(np.exp(-w)*np.exp(-xx*xx/(2*w))/np.sqrt(2*np.pi*w), w)) for xx in (0.5, 1.0, 2.0)]
a.plot(x, np.log(lap), color=BLUE, lw=1.4)
a.plot(x, np.log(phi(x)), color=YELLOW, lw=1.5)
a.text(0.0, -6.4, r'$\mathcal{N}(0,1)$', color=YELLOW, fontsize=7.5, ha='center')
a.text(3.4, -2.5, 'Laplace', color=BLUE, fontsize=7.5, ha='center')
a.set_xlim(-5, 5); a.set_ylim(-8, 0.5); a.set_xlabel('$x$', labelpad=1); a.set_ylabel(r'$\ln f(x)$', labelpad=1)
W = rng.exponential(1.0, n); Z = rng.standard_normal((n, 2))
Xc = np.sqrt(W)[:, None]*Z
W2 = rng.exponential(1.0, (n, 2)); Z2 = rng.standard_normal((n, 2))
Xi = np.sqrt(W2)*Z2
for ax_, X in ((b, Xc), (c, Xi)):
    far = np.hypot(X[:, 0], X[:, 1]) > 3
    ax_.scatter(X[~far, 0], X[~far, 1], s=1.0, color=GREEN, linewidths=0)
    ax_.scatter(X[far, 0], X[far, 1], s=2.2, color=RED, linewidths=0)
    tt = np.linspace(0, 2*np.pi, 200)
    ax_.plot(3*np.cos(tt), 3*np.sin(tt), color=STROKE, lw=0.6, ls='--')
    ax_.set_xlim(-6, 6); ax_.set_ylim(-6, 6); ax_.set_xticks([-5, 0, 5]); ax_.set_yticks([-5, 0, 5])
    ax_.set_xlabel('$x_1$', labelpad=1)
b.set_ylabel('$x_2$', labelpad=0)
for ax_ in (a, b, c):
    ax_.set_box_aspect(1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30); tag(c, '(c)', y=-0.30)
def csq(X):
    return float(np.cov(X[:, 0]**2, X[:, 1]**2)[0, 1])
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'mixture_integral_at_0.5_1_2': check,
     'laplace_at_0.5_1_2': [float(np.exp(-np.sqrt(2)*t)/np.sqrt(2)) for t in (0.5, 1.0, 2.0)],
     'cov_sq_common': csq(Xc), 'cov_sq_indep': csq(Xi), 'corr_common': float(np.corrcoef(Xc.T)[0, 1])})
