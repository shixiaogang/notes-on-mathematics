"""Blahut-Arimoto for Bern(0.3), Hamming, s=log2 9 (2^{-s}=1/9), start r=(1/2,1/2).
(a) output probability r^(t)(1) -> 0.25 (blue line). (b) J^(t)-F* (green), certified gap bound
max log2 c^(t) (yellow), and D(r*||r^(0))/t (purple dashed), log scale."""
from pathlib import Path
import sys
import math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

px = np.array([.7, .3]); d = np.array([[0, 1], [1, 0.]]); s = math.log2(9)
H = blahut_arimoto(px, d, s, r0=[.5, .5], iters=25)
Fstar = float(rd_binary(.1))+s*.1
rstar = np.array([.75, .25]); r0 = np.array([.5, .5])
kl0 = float(np.sum(rstar*np.log2(rstar/r0)))
t = np.array([h['t'] for h in H])
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.085, right=.985, top=.95, bottom=.28, wspace=.32)
ax = axs[0]
rs = [.5]+[h['r'][1] for h in H]
ax.plot(range(len(rs)), rs, 'o-', color=GREEN, ms=3, lw=1.0)
ax.axhline(.25, color=BLUE, lw=1.1, ls=DASH)
ax.set_xlim(-.5, 15.5); ax.set_ylim(.22, .52)
axlab(ax, '轮次', '$r^{(t)}(1)$')
ax = axs[1]
ax.semilogy(t, [h['J']-Fstar for h in H], 'o-', color=GREEN, ms=3, lw=1.0)
ax.semilogy(t, [h['gap'] for h in H], 's-', color=YELLOW, ms=3, lw=1.2)
ax.semilogy(t, kl0/t, color=PURPLE, lw=.9, ls=DASH)
lab(ax, 9, .14, '$D_{\\mathrm{KL}}(r^*\\Vert r^{(0)})/t$', PURPLE, ha='left')
lab(ax, 9.5, 4e-4, '最优性界', YELLOW, ha='left')
lab(ax, .8, 1e-6, '$J^{(t)}-F^*$', GREEN, ha='left')
ax.set_xlim(0, 20.5); ax.set_ylim(1e-8, 1.5)
axlab(ax, '轮次', 'bit')
tags(fig, axs)
save(fig, HERE, 'figure', {'Fstar': Fstar, 'kl0': kl0,
                          'rounds': [dict(t=h['t'], r1=float(h['r'][1]), J=h['J'], gap=h['gap'], I=h['I'], D=h['D']) for h in H[:8]]})
