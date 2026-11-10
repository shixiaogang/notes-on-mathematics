from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# -Lap u=1 on unit square, sine series.
fig, axes = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [.9, 1]})
panel(fig, left=.05, wspace=.28, bottom=.25, right=.985)
g = np.linspace(0, 1, 241); Px, Py = np.meshgrid(g, g)
odd = np.arange(1, 80, 2); U = 0*Px
for m in odd:
    sm = np.sin(m*np.pi*Px)
    for n in odd:
        U += 16/(np.pi**4*m*n*(m**2+n**2))*sm*np.sin(n*np.pi*Py)
ax = axes[0]
ax.imshow(U, origin='lower', extent=[0, 1, 0, 1], cmap=FIELD, vmin=0, vmax=.08)
ax.contour(Px, Py, U, [.02, .04, .06], colors=INK, linewidths=.7)
ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=STROKE, lw=1.4); dot(ax, .5, .5, RED, 3.8)
ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); hat01(ax, '$x_1$'); ax.set_ylabel('$x_2$', labelpad=-3)
for s in ax.spines.values(): s.set_visible(False)
ax = axes[1]
Ns = np.arange(1, 22, 2); vals = []
for N in Ns:
    vals.append(sum(16/(np.pi**4*m*n*(m**2+n**2))*np.sin(m*np.pi/2)*np.sin(n*np.pi/2) for m in odd[odd <= N] for n in odd[odd <= N]))
ax.plot(Ns, vals, '-o', ms=3.2, lw=1.1, color=GREEN, mew=0); ax.axhline(U[120, 120], color=BLUE, lw=1.2)
lab(ax, 21, U[120, 120]+.0005, '%.4f' % U[120, 120], BLUE, ha='right')
ax.set_xlim(0, 22); ax.set_ylim(.070, .085); ax.set_yticks([.07, .08]); ax.set_xticks([1, 5, 11, 21]); hat01(ax, r'截断阶 N', r'$u(\frac{1}{2},\frac{1}{2})$')
tags(fig, axes)
save(fig, HERE, 'figure', {'center': float(U[120, 120]), 'first': vals[0], 'terms': 'm,n odd <80'})
print(U[120, 120], vals[:3])
