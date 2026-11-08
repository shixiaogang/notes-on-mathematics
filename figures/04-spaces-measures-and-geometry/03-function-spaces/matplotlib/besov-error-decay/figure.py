from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f=1_[0,1/3): E_J=(sqrt2/3)2^{-J/2} at M=2^J; sigma_N=(2/3)2^{-N/2}; theorem bound N^{-1/4}||c||_{4/3}.
fig, ax = figure(width_mm=90, height_mm=56)
J = np.arange(0, 7); M = 2.0**J
E = np.sqrt(2)/3*2.0**(-J/2)
N = np.arange(1, 65); sig = 2/3*2.0**(-N/2)
tau = 4/3; ctau = (3.0**(-tau)*(1+1/(1-2**(-tau/2))))**(1/tau)
bd = N**(-.25)*ctau
ax.loglog(M, E, color=BLUE, lw=1.4, marker='o', ms=3.4, mew=0)
ax.loglog(N[:40], sig[:40], color=GREEN, lw=1.4)
ax.loglog(N, bd, color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.set_xlim(1, 64); ax.set_ylim(1e-6, 2)
ax.set_xticks([1, 2, 4, 8, 16, 32, 64]); ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64']); ax.minorticks_off()
ax.set_yticks([1e-5, 1e-3, 1e-1]); ax.set_yticklabels(['$10^{-5}$', '$10^{-3}$', '$10^{-1}$'])
ax.set_xlabel('项数', labelpad=0)
ax.text(20, .055, r'$E_J$', color=BLUE, ha='center', va='top')
ax.text(11, .0011, r'$\sigma_N$', color=GREEN, ha='left', va='center')
ax.text(30, .55, r'$N^{-1/4}\Vert c\Vert_{\ell^{4/3}}$', color=MUTED, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'E_J=(sqrt2/3)2^{-J/2}, M=2^J; sigma_N=(2/3)2^{-N/2}; bound N^{-1/4}*||c||_{4/3}', 'ctau': float(ctau)})
