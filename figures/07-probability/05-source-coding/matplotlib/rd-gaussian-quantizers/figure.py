"""N(0,1), squared error. Blue: D(R)=2^{-2R}. Green: Lloyd-Max quantizers with N=2,4,8,16 levels at
fixed index length log2 N. Yellow: uniform (midtread) quantizer with centroid reconstruction and ideal
entropy coding of the index, rate H(index), steps from 3 down to 0.1. Purple dashed: D(R) shifted by
(1/2)log2(pi e/6)=0.2546 bit."""
from pathlib import Path
import sys
import math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

LM = {N: lloyd_max_gauss(N)[1] for N in (2, 4, 8, 16)}
steps = np.geomspace(3.0, .1, 50)
EC = np.array([ecsq_gauss(s) for s in steps])
gap = .5*math.log2(math.pi*math.e/6)
fig, ax = figure(width_mm=92, height_mm=54)
R = np.linspace(0, 4.4, 300)
ax.semilogy(R, 2.0**(-2*R), color=BLUE, lw=1.4, zorder=3)
ax.semilogy(R+gap, 2.0**(-2*R), color=PURPLE, lw=.9, ls=DASH, zorder=2)
ax.semilogy(EC[:, 0], EC[:, 1], color=YELLOW, lw=1.6, zorder=2)
for N, m in LM.items():
    dot(ax, math.log2(N), m, GREEN, ms=4.6)
    lab(ax, math.log2(N)+.07, m*1.12, f'$N={N}$', GREEN, ha='left')
lab(ax, .12, .1, '$D(R)=2^{-2R}$', BLUE, ha='left')
lab(ax, 2.3, .055, '均匀量化+熵编码', YELLOW, ha='left')
ax.set_xlim(0, 4.4); ax.set_ylim(2e-3, 1.2)
axlab(ax, '码率（bit/符号）', '均方误差')
save(fig, HERE, 'figure', {'lloyd_max_mse': LM, 'gap_bits': gap,
                          'ecsq_samples': {f'{s:.3f}': list(map(float, e)) for s, e in zip(steps[::10], EC[::10])}})
