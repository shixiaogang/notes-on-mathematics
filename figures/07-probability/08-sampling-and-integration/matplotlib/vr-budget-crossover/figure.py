from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Target I = P(X>4), X ~ Exp(1).  Plain Monte Carlo: per-sample variance v0 = I(1-I), unit cost 1.
# Importance sampling with q = Exp(1/4): v1 = e^{-7}/(0.25*1.75) - I^2, unit cost 1.5, fixed set-up cost C0 = 2000.
# Relative RMSE after budget C: sqrt(v c/(C - C0))/I.  Crossover where the two are equal.
I = math.exp(-4); v0 = I*(1-I); v1 = math.exp(-7)/(0.25*1.75) - I*I; c1 = 1.5; C0 = 2000
C = np.logspace(np.log10(2050), 6, 400)
r0 = np.sqrt(v0/C)/I; r1 = np.sqrt(v1*c1/(C-C0))/I
Cx = v0*C0/(v0 - v1*c1)
fig, ax = figure(width_mm=96, height_mm=50)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
ax.plot(C, r0, color=BLUE, lw=1.4); ax.plot(C, r1, color=GREEN, lw=1.4)
ax.axvline(C0, color=STROKE, lw=.85, ls=DASH)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(1800, 1e6); ax.set_ylim(5e-3, 3)
logticks(ax, [-2, -1, 0]); logticks(ax, [4, 5, 6], 'x')
dot(ax, Cx, math.sqrt(v0/Cx)/I)
lab(ax, Cx*1.15, math.sqrt(v0/Cx)/I*1.25, r'$C\approx %d$' % round(Cx), RED)
lab(ax, 2.2e5, math.sqrt(v0/2.2e5)/I*1.25, '直接平均', BLUE)
lab(ax, 1.0e4, 0.0105, '重要性采样', GREEN)
lab(ax, C0*1.08, 1.8, r'$C_0$', STROKE)
axlab(ax, '总预算', '相对均方根误差')
save(fig, HERE, 'figure', {'I': I, 'v_plain': v0, 'v_is': v1, 'c_is': c1, 'C0': C0, 'crossover': Cx,
     'relrmse_plain_1e5': math.sqrt(v0/1e5)/I, 'relrmse_is_1e5': math.sqrt(v1*c1/(1e5-C0))/I})
