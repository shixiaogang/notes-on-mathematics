"""Mixture vs average: 0.5N(-1.5,1)+0.5N(1.5,1) (var 3.25) vs (Y1+Y2)/2 ~ N(0,0.5); histogram of 5000 mixture samples, seed 716."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 5000
K = rng.random(n) < 0.5
xs = np.where(K, -1.5, 1.5)+rng.standard_normal(n)
x = np.linspace(-5, 5, 900)
fig, ax = figure(width_mm=96, height_mm=46)
ax.hist(xs, bins=np.arange(-5, 5.01, 0.25), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=0.5)
ax.plot(x, 0.5*phi(x+1.5)+0.5*phi(x-1.5), color=BLUE, lw=1.4)
ax.plot(x, phi(x/np.sqrt(0.5))/np.sqrt(0.5), color=YELLOW, lw=1.5)
ax.text(-3.4, 0.22, '混合', color=BLUE, fontsize=7.5, ha='center')
ax.text(0.75, 0.5, r'$\frac{1}{2}Y_1+\frac{1}{2}Y_2$', color=YELLOW, fontsize=7.5)
ax.set_xlim(-5, 5); ax.set_ylim(0, 0.6); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('密度')
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'sample_var': float(xs.var()), 'mixture_var': 3.25, 'avg_var': 0.5})
