from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# (a) p(k)=1/(k(k+1)): partial sums of k p(k) = sum_{k<=n} 1/(k+1) grow like ln n.
# (b) symmetric density f(x)=1/(2x^2), |x|>=1: truncated first moment over [-a,b]
#     equals (ln b - ln a)/2 and depends on how the truncation grows.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.09, right=.98, bottom=.3, wspace=.32)
ax = axes[0]
n = np.arange(1, 10001)
S = np.cumsum(1/(n+1))
ax.plot(n, S, color=BLUE, lw=1.4)
ax.plot(n, np.log(n+1)-1+np.euler_gamma, color=PURPLE, lw=.9, ls=DASH)
ax.set_xscale('log'); ax.set_xlim(1, 1e4); ax.set_ylim(0, 9.5)
ax.set_xticks([1, 10, 100, 1000, 10000]); ax.set_xticklabels(['1', '10', '$10^2$', '$10^3$', '$10^4$'])
lab(ax, 250, 3.3, r'$\ln(n+1)-0.42$', PURPLE, ha='left'); lab(ax, 700, 4.7, '', BLUE)
lab(ax, 3, 2.8, r'$\sum_{k\leq n}k\,p(k)$', BLUE, ha='left')
axlab(ax, '$n$', '部分和')
ax = axes[1]
a = np.linspace(1, 60, 400)
ax.plot(a, 0*a, color=BLUE, lw=1.4)
ax.plot(a, 0*a+np.log(2)/2, color=YELLOW, lw=1.6)
ax.plot(a, np.log(a)/2, color=PURPLE, lw=1.4)
lab(ax, 60, .07, '$[-a,a]$', BLUE, ha='right', va='bottom')
lab(ax, 60, np.log(2)/2+.07, '$[-a,2a]$', YELLOW, ha='right', va='bottom')
lab(ax, 60, np.log(60)/2-.1, '$[-a,a^2]$', PURPLE, ha='right', va='top')
ax.set_xlim(1, 60); ax.set_ylim(-.25, 2.3); ax.set_xticks([1, 20, 40, 60]); ax.set_yticks([0, np.log(2)/2, 1, 2]); ax.set_yticklabels(['0', '0.35', '1', '2'])
axlab(ax, '$a$', '截断均值')
tags(fig, axes)
save(fig, HERE, 'figure', {'S_10000': float(S[-1]), 'ln2/2': float(np.log(2)/2)})
