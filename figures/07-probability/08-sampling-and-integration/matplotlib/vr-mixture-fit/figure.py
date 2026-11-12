from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Target p = N(0,1), f = 1{x<-2.5} + 1{x>3}.  Trial run: m = 30 points from q0 = N(0, 3^2), seed 3.
# Contribution c_j = f(y_j) p(y_j)/q0(y_j).  Fit pi_k = share of contributions, m_k = contribution-weighted mean
# on each side, unit variances, defensive weight alpha = 0.2:
# q = 0.2 q0 + 0.8 [pi_L N(m_L,1) + pi_R N(m_R,1)].  Ideal q* = f p / I.  Per-sample variances by quadrature.
rng = np.random.default_rng(3); m = 30; y = rng.normal(0, 3, m)
f = lambda t: ((t < -2.5) | (t > 3)).astype(float)
c = f(y)*phi(y)/phi(y, 0, 3)
comps = []
for side in (y < 0, y > 0):
    cc = c*side; comps.append((cc.sum()/c.sum(), (cc*y).sum()/cc.sum()))
alpha = .2
xs = np.linspace(-15, 15, 600001); d = xs[1]-xs[0]
I = Phi(-2.5) + 1 - Phi(3)
q = lambda t: alpha*phi(t, 0, 3) + (1-alpha)*sum(pk*phi(t, mk, 1) for pk, mk in comps)
v_fit = float(np.sum(f(xs)*phi(xs)**2/q(xs))*d - I*I)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, bottom=.27, top=.95, wspace=.24)
a, b = axs
tr = a.get_xaxis_transform()
for t, cj in zip(y, c):
    if cj > 1e-3:
        a.plot([t, t], [0, cj], color=GREEN, lw=1.4); dot(a, t, cj, color=GREEN, ms=3.2)
    else:
        a.plot([t, t], [0, .045], color=MUTED, lw=.9, transform=tr)
for t0 in (-2.5, 3):
    a.axvline(t0, color=RED, lw=.85, ls=DASH)
a.set_xlim(-10, 10); a.set_ylim(0, .18); a.set_xticks([-8, -4, 0, 4, 8]); a.set_yticks([0, .05, .1, .15])
axlab(a, '$y$', r'$c_j$')
x = np.linspace(-6, 6, 1201)
qs = f(x)*phi(x)/I
b.fill_between(x, 0, qs, color=BLUE_FILL, lw=0, step=None)
b.plot(x, qs, color=BLUE, lw=1.0)
b.plot(x, q(x), color=YELLOW, lw=1.6)
for t0 in (-2.5, 3):
    b.axvline(t0, color=RED, lw=1.0)
b.set_xlim(-6, 6); b.set_ylim(0, 2.5); b.set_xticks([-6, -3, 0, 3, 6]); b.set_yticks([0, 1, 2])
lab(b, -4.6, 1.9, r'$q^{*}$', BLUE); lab(b, -1.9, .42, r'$q$', YELLOW)
axlab(b, '$x$')
tags(fig, axs)
save(fig, HERE, 'figure', {'trial_points': [float(t) for t in y], 'contrib': [float(v) for v in c],
     'components': [[float(u) for u in cmp] for cmp in comps], 'alpha': alpha, 'I': I,
     'var_fit': v_fit, 'var_plain': I*(1-I), 'ratio': I*(1-I)/v_fit, 'Ihat_trial': float(c.mean())})
