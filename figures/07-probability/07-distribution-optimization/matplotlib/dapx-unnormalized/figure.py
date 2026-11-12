from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Quartic target pi~(x)=exp(-x^4/4), Z=2*4^{1/4}*Gamma(5/4)=2.5637, ln Z=0.9414.
# (a) pi~ (purple dashed) and pi=pi~/Z (blue).
# (b) candidates Q_s=N(0,s^2): J(s)=-ln s - C + 3 s^4/4 (green) and D(Q_s||Pi)=J+ln Z (blue);
#     common minimiser s*=3^{-1/4}=0.7598, D*=0.0472, J*=-0.8943.
Z = math.exp(LNZ4)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.3)
ax = axs[0]
x = np.linspace(-3, 3, 1201)
pt = np.exp(-x**4/4)
ax.plot(x, pt, color=PURPLE, lw=1.2, ls=DASH)
ax.plot(x, pt/Z, color=BLUE, lw=1.4)
lab(ax, .9, .93, r'$\widetilde{\pi}$', PURPLE)
lab(ax, 1.5, .42, r'$\pi=\widetilde{\pi}/Z$', BLUE)
ax.set_xlim(-3, 3); ax.set_ylim(0, 1.08)
axlab(ax, '$x$', None)
ax = axs[1]
s = np.linspace(.35, 1.3, 400)
J = quartic_J(0, s); D = J+LNZ4
ax.plot(s, D, color=BLUE, lw=1.4)
ax.plot(s, J, color=GREEN, lw=1.4)
ax.axhline(0, color=STROKE, lw=.85)
ss = 3**-0.25
for v in (quartic_J(0, ss)+LNZ4, quartic_J(0, ss)):
    dot(ax, ss, v, RED, ms=4)
ax.plot([ss, ss], [quartic_J(0, ss), quartic_J(0, ss)+LNZ4], color=PURPLE, lw=.85, ls=DOT)
lab(ax, ss+.03, -.45, r'$\ln Z\approx0.941$', PURPLE, fontsize=7)
lab(ax, 1.0, .55, r'$D_{\mathrm{KL}}(Q_s\Vert\Pi)$', BLUE)
lab(ax, 1.0, -.88, r'$J(Q_s)$', GREEN)
ax.set_xlim(.35, 1.3); ax.set_ylim(-1.0, 1.0)
axlab(ax, '$s$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'Z': Z, 'lnZ': LNZ4, 's_star': ss, 'D_star': float(quartic_J(0, ss)+LNZ4), 'J_star': float(quartic_J(0, ss))})
