from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# (a) Self-normalised IS for I = E[X], target unnormalised p~(x) = x^2 e^{-x} (Gamma(3,1), Z = 2, I = 3),
# proposal q = Exp(1/2), w = 2 x^2 e^{-x/2}.  R = 40000 replications per n (seed 5): |bias| and standard deviation.
# Reference lines: 0.527/n (bias coefficient -E_q[w^2(f-I)]/Z^2) and sqrt(3.687/n) (tau^2/Z^2).
# (b) Missed mode: p~ = 0.5 phi(x) + 0.5 phi(x-8), proposal N(0,1), n = 1000 (seed 6); true E[X] = 4.
rng = np.random.default_rng(5); R = 40000
ns = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
bias = []; sd = []
for n in ns:
    x = rng.exponential(2.0, (R, n)); w = 2*x**2*np.exp(-x/2)
    est = (w*x).sum(1)/w.sum(1)
    bias.append(abs(est.mean()-3)); sd.append(est.std())
t = np.linspace(1e-9, 150, 3000001); dt = t[1]-t[0]; qd = np.exp(-t/2)/2; W = t**2*np.exp(-t)/qd
tau2 = float(np.sum(W**2*(t-3)**2*qd)*dt); bc = float(-np.sum(W**2*(t-3)*qd)*dt/4)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.98, bottom=.27, top=.95, wspace=.26)
a, b = axs
a.plot(ns, sd, 'o-', color=GREEN, lw=1.2, ms=3)
a.plot(ns, bias, 'o-', color=RED, lw=1.2, ms=3)
a.plot(ns, np.sqrt(tau2/4/ns), color=PURPLE, lw=.9, ls=DASH)
a.plot(ns, abs(bc)/ns, color=PURPLE, lw=.9, ls=DASH)
a.set_xscale('log'); a.set_yscale('log'); a.set_xlim(1.6, 1300); a.set_ylim(3e-4, 3)
logticks(a, [-3, -2, -1, 0]); logticks(a, [1, 2, 3], 'x')
lab(a, 3, 1.4, '标准差', GREEN); lab(a, 2.2, 2e-3, '偏差', RED)
axlab(a, '$n$')
rng = np.random.default_rng(6); n = 1000
x = rng.normal(0, 1, n); w = (0.5*phi(x)+0.5*phi(x, 8))/phi(x)
est = float((w*x).sum()/w.sum()); ess = float(w.sum()**2/(w*w).sum())
xx = np.linspace(-4, 12, 1601)
b.plot(xx, 0.5*phi(xx)+0.5*phi(xx, 8), color=BLUE, lw=1.4)
b.plot(xx, phi(xx), color=YELLOW, lw=1.6)
tr = b.get_xaxis_transform()
for v in x[:200]:
    b.plot([v, v], [0, .05], color=GREEN, lw=.5, transform=tr)
b.axvline(4, color=RED, lw=1.0, ymax=.75); b.axvline(est, color=GREEN, lw=1.0, ls=DASH, ymax=.75)
b.set_xlim(-4, 12); b.set_ylim(0, .5); b.set_xticks([-4, 0, 4, 8, 12]); b.set_yticks([0, .2, .4])
lab(b, 8.3, .26, r'$\tilde{p}$', BLUE); lab(b, 1.2, .36, r'$q$', YELLOW); lab(b, 4.3, .36, r'$I=4$', RED)
axlab(b, '$x$')
tags(fig, axs)
save(fig, HERE, 'figure', {'ns': ns.tolist(), 'abs_bias': [float(v) for v in bias], 'sd': [float(v) for v in sd],
     'tau2_over_Z2': tau2/4, 'bias_coef': bc, 'missed_mode_estimate': est, 'missed_mode_ess': ess, 'n_b': n})
