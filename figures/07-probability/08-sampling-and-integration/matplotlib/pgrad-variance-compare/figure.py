from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# Single-sample variances for X ~ N(theta,1), derivative in theta.
# (a) f = x^2: reparameterization 2X: 4 (blue); score f s: theta^4 + 14 theta^2 + 15 (yellow);
#     score with baseline J = theta^2+1: 8 theta^2 + 10 (green); optimal constant baseline theta^2+3: 8 theta^2 + 6 (green dashed).
# (b) f = sin(omega x) at theta = 0: reparameterization omega cos(omega X) vs score sin(omega X) X, closed forms:
#     Var_rep = omega^2 (1 + e^{-2 omega^2})/2 - omega^2 e^{-omega^2},
#     Var_sf  = (1 - (1 - 4 omega^2) e^{-2 omega^2})/2 - omega^2 e^{-omega^2}.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.28)
a, b = axs
t = np.linspace(-2, 2, 300)
a.plot(t, 4+0*t, color=BLUE, lw=1.4)
a.plot(t, t**4+14*t**2+15, color=YELLOW, lw=1.5)
a.plot(t, 8*t**2+10, color=GREEN, lw=1.3)
a.plot(t, 8*t**2+6, color=GREEN, lw=1.1, ls=DASH)
a.set_yscale('log'); a.set_xlim(-2, 2); a.set_ylim(2, 150); a.set_xticks([-2, -1, 0, 1, 2])
a.set_yticks([3, 10, 30, 100]); a.set_yticklabels(['3', '10', '30', '100'])
lab(a, -.55, 2.6, '重参数化', BLUE); lab(a, -1.95, 95, '得分', YELLOW)
axlab(a, r'$\theta$')
w = np.linspace(.2, 4, 300)
vr = w**2*(1+np.exp(-2*w**2))/2 - w**2*np.exp(-w**2)
vs = (1-(1-4*w**2)*np.exp(-2*w**2))/2 - w**2*np.exp(-w**2)
b.plot(w, vr, color=BLUE, lw=1.4); b.plot(w, vs, color=YELLOW, lw=1.5)
b.set_yscale('log'); b.set_xlim(0, 4); b.set_ylim(1e-3, 20); b.set_xticks([0, 1, 2, 3, 4])
lab(b, 2.6, 3.5, '重参数化', BLUE); lab(b, 2.6, .18, '得分', YELLOW)
cross = float(w[np.argmin(np.abs(vr-vs)[w > .5])+np.sum(w <= .5)])
b.axvline(cross, color=STROKE, lw=.6, ls=DOT)
axlab(b, r'$\omega$')
tags(fig, axs)
save(fig, HERE, 'figure', {'crossover_omega': cross, 'theta1': {'rep': 4, 'sf': 30, 'sfJ': 18, 'sfopt': 14}})
