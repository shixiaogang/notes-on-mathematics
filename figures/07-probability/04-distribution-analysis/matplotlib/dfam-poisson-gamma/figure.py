"""Poisson-Gamma mixture: Lambda~Gamma(2,1) gives P(X=k)=(k+1)/2^(k+2); compared with Poisson(2)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

import math
k = np.arange(0, 11)
nb = (k+1)/2.0**(k+2)
lam = np.linspace(1e-9, 80, 400001)
num = [float(np.trapezoid(np.exp(-lam)*lam**kk/math.factorial(kk)*lam*np.exp(-lam), lam)) for kk in range(5)]
po = np.array([math.exp(-2)*2**kk/math.factorial(kk) for kk in k])
fig, ax = figure(width_mm=96, height_mm=44)
ax.bar(k, nb, width=0.7, color=BLUE_FILL, edgecolor=BLUE, lw=0.8)
ax.scatter(k, po, s=16, facecolors='white', edgecolors=YELLOW, linewidths=1.3, zorder=4)
ax.text(6.3, 0.17, r'$\mathrm{Poisson}(2)$', color=YELLOW, fontsize=7.5)
ax.text(6.3, 0.22, '负二项', color=BLUE, fontsize=7.5)
ax.set_xticks(k); ax.set_xlim(-0.6, 10.6); ax.set_ylim(0, 0.3); ax.set_xlabel('$k$', labelpad=1); ax.set_ylabel(r'$\mathrm{P}(X=k)$')
mean = float((k*nb).sum()); var = float((k*k*nb).sum()-mean**2)
save(fig, HERE, 'figure', {'nb_first': [float(v) for v in nb[:4]], 'numeric_mixture_first5': num, 'poisson0': float(po[0]),
     'nb_mean_trunc10': mean, 'nb_var_trunc10': var})
