from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Per-sample variance of importance sampling for I = P(X>4), X ~ Exp(1), proposal q = Exp(lam):
# v(lam) = e^{-4(2-lam)}/(lam(2-lam)) - I^2 for 0<lam<2, infinite for lam >= 2.
# lam = 1 is plain Monte Carlo; the minimiser solves 4 lam^2 - 10 lam + 2 = 0.
I = math.exp(-4)
v = lambda l: np.exp(-4*(2-l))/(l*(2-l)) - I*I
lam = np.linspace(0.03, 1.985, 800)
ls = (10-math.sqrt(68))/8
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
ax.plot(lam, v(lam), color=BLUE, lw=1.4)
ax.axvline(2, color=STROKE, lw=.85, ls=DASH)
ax.set_yscale('log'); ax.set_xlim(0, 2.3); ax.set_ylim(3e-4, 10); logticks(ax, [-3, -2, -1, 0, 1])
ax.set_xticks([0, .5, 1, 1.5, 2])
dot(ax, 1, v(1), color=BLUE); lab(ax, 1.04, v(1)*.45, '直接平均', BLUE)
dot(ax, ls, v(ls)); lab(ax, .02, 5.5e-4, r'$\lambda^{*}\approx 0.219$', RED)
dot(ax, .25, v(.25), color=GREEN, ms=3.4); lab(ax, .36, 1.05e-3, r'$\lambda=1/4$', GREEN)
lab(ax, 2.05, 1.5, r'$\infty$', RED, fontsize=8)
axlab(ax, r'$\lambda$', '单样本方差')
save(fig, HERE, 'figure', {'lam_star': ls, 'v_star': float(v(ls)), 'v_quarter': float(v(.25)), 'v_plain': float(v(1)),
     'v_1.5': float(v(1.5)), 'v_1.9': float(v(1.9))})
