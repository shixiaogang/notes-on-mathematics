from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# Sphere-packing (Hamming) bound for single-error-correcting binary codes: M (1+n) <= 2^n, i.e. rate <= 1 - log2(1+n)/n.
# Purple: the bound as a function of n (drawn through integer n). Green: Hamming codes n = 2^m - 1, k = n - m (meet it).
# Yellow: the [5,2,3] code of the chapter (strictly below the bound at n = 5).
ns = np.arange(3, 64)
bd = 1-np.log2(1+ns)/ns
fig, ax = figure(width_mm=88, height_mm=54)
panel(fig, left=.14, right=.96, top=.96, bottom=.18)
ax.plot(ns, bd, color=PURPLE, lw=1.2)
hm = [(2**m-1, 2**m-1-m) for m in range(2, 7)]
for n, k in hm:
    ax.plot([n], [k/n], 'o', ms=4, color=GREEN, mew=0, zorder=5)
    if n == 3: lab(ax, .4, .24, r'$[3,1]$', GREEN)
    elif n == 63: lab(ax, n-1, k/n+.04, r'$[63,57]$', GREEN, ha='right')
    else: lab(ax, n+1.2, k/n-.06, r'$[%d,%d]$' % (n, k), GREEN)
ax.plot([5], [2/5], 's', ms=4, color=YELLOW, mew=0, zorder=5)
lab(ax, 6.0, .30, r'$[5,2]$', YELLOW)
lab(ax, 22, 1.0, '上界', PURPLE); lab(ax, 29, 1.0, r'$1-\log_2(1+n)/n$', PURPLE)
ax.set_xlim(0, 68); ax.set_ylim(0, 1.08); ax.set_xticks([3, 7, 15, 31, 63])
ax.set_xlabel(r'$n$', labelpad=1); ax.set_ylabel(r'$k/n$', labelpad=1)
save(fig, HERE, 'figure', {'hamming_codes': hm, 'bound_n5': float(1-np.log2(6)/5)})
