"""Triangle model (density 2 on 0<=y<=x<=1): mean (2/3,1/3), Sigma=[[1/18,1/36],[1/36,1/18]].
(a) 800 simulated points (seed 1, as (max,min) of two uniforms), principal axes along (1,1) and (1,-1) with half-lengths
equal to the standard deviations sqrt(1/12), sqrt(1/36). (b) a^T Sigma a for a=(cos phi, sin phi) and sample variances of a^T X."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

rng = np.random.default_rng(1); n = 800
u = rng.random((2, n)); x = u.max(0); y = u.min(0)
S = np.array([[1/18, 1/36], [1/36, 1/18]]); mu = np.array([2/3, 1/3])
fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.25]})
a.plot([0, 1, 1, 0], [0, 0, 1, 0], color=BLUE, lw=1.1)
a.scatter(x, y, s=1.4, color=GREEN, linewidths=0)
for v, lam in ((np.array([1, 1])/np.sqrt(2), 1/12), (np.array([1, -1])/np.sqrt(2), 1/36)):
    d = np.sqrt(lam)*v
    a.annotate('', xy=mu+d, xytext=mu-d, arrowprops=dict(arrowstyle='<->', color=PURPLE, lw=1.3, shrinkA=0, shrinkB=0))
a.scatter([mu[0]], [mu[1]], s=16, color=RED, zorder=4)
a.set_aspect('equal'); a.set_xlim(-0.03, 1.05); a.set_ylim(-0.03, 1.05); a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 0.5, 1])
a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$y$', rotation=0)
phi = np.linspace(0, np.pi, 300)
b.plot(phi, 1/18 + np.sin(2*phi)/36, color=BLUE, lw=1.4)
ph = np.linspace(0, np.pi, 13)[:-1]
sv = [np.var(np.cos(p)*x + np.sin(p)*y) for p in ph]
b.scatter(ph, sv, s=10, color=GREEN, zorder=3)
b.scatter([np.pi/4, 3*np.pi/4], [1/12, 1/36], s=18, color=RED, zorder=4)
b.text(np.pi/4 - 0.12, 1/12, r'$\frac{1}{12}$', ha='right', va='center')
b.text(3*np.pi/4 + 0.12, 1/36 - 0.002, r'$\frac{1}{36}$', ha='left', va='top')
b.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]); b.set_xticklabels(['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])
b.set_ylim(0, 0.1); b.set_yticks([0, 0.05, 0.1]); b.set_xlabel(r'$\varphi$', labelpad=1)
b.set_ylabel(r'$v(\varphi)$')
tag(a, '(a)', y=-0.24); tag(b, '(b)', y=-0.24)
save(fig, Path(__file__).resolve().parent, 'figure', {'seed': 1, 'n': n, 'sample_cov': np.cov(x, y, bias=True).tolist(), 'Sigma': S.tolist()})
