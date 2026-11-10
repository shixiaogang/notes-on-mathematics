from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# u=x^2-y^2 on unit disc; mean value at p.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2, gridspec_kw={'width_ratios': [.8, 1]})
panel(fig, left=.03, wspace=.22, bottom=.25, right=.985)
ax = axes[0]
g = np.linspace(-1, 1, 501); P, Q = np.meshgrid(g, g); U = P**2-Q**2; U[P**2+Q**2 > 1] = np.nan
ax.contour(P, Q, U, [-.75, -.5, -.25, 0, .25, .5, .75], colors=BLUE, linewidths=.9, linestyles='solid')
t = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color=STROKE, lw=1.4)
p = (.3, .2); r = .5
ax.plot(p[0]+r*np.cos(t), p[1]+r*np.sin(t), color=YELLOW, lw=1.3); dot(ax, *p, RED, 4)
for s in (0, np.pi): dot(ax, np.cos(s), np.sin(s), RED, 4.2)
for s in (np.pi/2, 3*np.pi/2): dot(ax, np.cos(s), np.sin(s), PURPLE, 4.2)
ax.set_xlim(-1.08, 1.08); ax.set_ylim(-1.08, 1.08); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax = axes[1]
th = np.linspace(0, 2*np.pi, 721); up = (p[0]+r*np.cos(th))**2-(p[1]+r*np.sin(th))**2
ax.plot(th, up, color=YELLOW, lw=1.5); ax.axhline(p[0]**2-p[1]**2, color=RED, lw=1.2, ls=DASH)
m = float(np.trapezoid(up, th)/(2*np.pi))
lab(ax, 4.3, p[0]**2-p[1]**2+.05, r'$u(\mathbf{p})=0.05$', RED, ha='center')
ax.set_xlim(0, 2*np.pi); ax.set_xticks([0, np.pi, 2*np.pi]); ax.set_xticklabels(['0', r'$\pi$', r'$2\pi$']); ax.set_ylim(-.5, .75); ax.set_yticks([-.4, 0, .4]); hat01(ax, r'$\theta$', r'$u$')
tags(fig, axes)
print(m)
save(fig, HERE, 'figure', {'u': 'x^2-y^2', 'p': p, 'r': r, 'mean': m})
