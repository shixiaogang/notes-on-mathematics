from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# U ~ Unif(0,1), g(theta,u) = 2 theta^3 u / (u^2+theta^2)^2, g(0,u) = 0.
# J(theta) = theta/(1+theta^2), J'(0) = 1, but d/dtheta g(0,u) = 0 for every u in (0,1).
# (a) g(theta,.) for theta = 0.4, 0.2, 0.1 (spike moves to u=0, area ~ theta).
# peak height 9/(8 sqrt 3) ~ 0.65 for every theta.
# (b) J(theta) (blue), tangent of slope 1 at 0 (red dashed), the exchanged value E[d g/d theta](0)=0 (green).
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.28)
a, b = axs
u = np.linspace(1e-4, 1, 2000)
facts = {}
for th, c, lx, ly in [(0.4, BLUE, .62, .72), (0.15, YELLOW, .24, .74), (0.05, PURPLE, .005, .78)]:
    g = 2*th**3*u/(u*u+th*th)**2
    a.plot(u, g, color=c, lw=1.3)
    um = th/math.sqrt(3); gm = 2*th**3*um/(um*um+th*th)**2
    lab(a, lx, ly, rf'$\theta={th}$', c, va='bottom')
    facts[f'area_{th}'] = th/(1+th*th)
a.set_xlim(0, 1); a.set_ylim(0, .9); a.set_xticks([0, .5, 1]); a.set_yticks([0, .3, .6])
axlab(a, r'$u$')
t = np.linspace(-1, 1, 300)
b.plot(t, t/(1+t*t), color=BLUE, lw=1.4)
b.plot(t, t, color=RED, lw=.9, ls=DASH)
b.plot(t, 0*t, color=GREEN, lw=1.3)
dot(b, 0, 0)
lab(b, .22, .68, '斜率 1', RED); lab(b, .1, -.17, '交换后斜率 0', GREEN); lab(b, -.95, -.32, r'$J(\theta)$', BLUE)
b.set_xlim(-1, 1); b.set_ylim(-.8, .8); b.set_xticks([-1, 0, 1]); b.set_yticks([-.5, 0, .5])
axlab(b, r'$\theta$')
tags(fig, axs)
save(fig, HERE, 'figure', facts)
