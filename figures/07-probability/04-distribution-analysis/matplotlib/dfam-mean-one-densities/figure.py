"""Densities on (0,inf) with mean 1: Exp(1), Gamma(2,2), Unif(0,2), Unif(1-a,1+a) a=0.3; point mass delta_1 as arrow."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dfam-common'))
from common import *

x = np.linspace(0.0005, 3.2, 1200)
fig, ax = figure(width_mm=96, height_mm=46)
ax.plot(x, np.exp(-x), color=BLUE, lw=1.4)
ax.plot(x, 4*x*np.exp(-2*x), color=YELLOW, lw=1.5)
ax.plot([0, 2, 2], [0.5, 0.5, 0], color=PURPLE, lw=1.3)
ax.plot([0, 0], [0, 0.5], color=PURPLE, lw=1.3)
a = 0.3
ax.plot([0.7, 0.7, 1.3, 1.3], [0, 1/(2*a), 1/(2*a), 0], color=GREEN, lw=1.3)
ax.axvline(1, color=STROKE, lw=0.85, ls='--', zorder=0)
ax.annotate('', xy=(1, 2.05), xytext=(1, 0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.6, mutation_scale=9))
ax.text(1.06, 1.98, r'$\delta_1$', color=RED, fontsize=8)
ax.text(0.12, 0.93, r'$\mathrm{Exp}(1)$', color=BLUE, fontsize=7.5)
ax.annotate(r'$\mathrm{Gamma}(2,2)$', xy=(1.75, 4*1.75*np.exp(-3.5)), xytext=(2.15, 0.95), color=YELLOW, fontsize=7.5, arrowprops=dict(arrowstyle='-', color=YELLOW, lw=0.85))
ax.text(2.05, 0.53, r'$\mathrm{Unif}(0,2)$', color=PURPLE, fontsize=7.5)
ax.text(1.36, 1.55, r'$\mathrm{Unif}(0.7,1.3)$', color=GREEN, fontsize=7.5)
ax.set_xlim(0, 3.2); ax.set_ylim(0, 2.2)
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f(x)$')
ax.set_xticks([0, 1, 2, 3])
means = {'exp': 1.0, 'gamma22': float(np.trapezoid(x*4*x*np.exp(-2*x), x)), 'unif02': 1.0, 'unif_a': 1.0}
save(fig, HERE, 'figure', {'target': 'mean-one densities', 'means_numeric': means})
