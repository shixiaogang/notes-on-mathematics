"""Variance as a function of the mean along several one-parameter families; red points at mean 2."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

fig, ax = figure(width_mm=100, height_mm=56)
style(ax)
m = np.linspace(0, 6, 601)
ax.plot(m[m <= 6], m[m <= 6]*(1-m[m <= 6]/10), color=BLUE, lw=1.4)                    # Bin(10,p): v=m(1-m/10)
mk = np.arange(0, 11)/2; ax.plot(mk[mk <= 6], (mk*(1-mk/10)*10/19)[mk <= 6], 'o', color=BLUE, ms=2.6, mfc='white', mew=.9)  # Hyp(20,K,10)
ax.plot(m, m, color=GREEN, lw=1.4)                                                     # Poisson: v=m
mg = m[m >= 1]; ax.plot(mg, mg**2-mg, color=YELLOW, lw=1.4, ls='--')                    # Geom: v=m^2-m
ax.plot(m, m**2, color=PURPLE, lw=1.4, ls='-.')                                          # Exp: v=m^2
for vv in (1.6, 0.8421, 2, 4):
    ax.plot([2], [vv], 'o', color=RED, ms=3.6, zorder=6)
lab(ax, 4.2, 2.85, 'Bin$(10,p)$', BLUE); lab(ax, 4.1, .45, 'Hyp$(20,K,10)$', BLUE)
lab(ax, 4.7, 5.3, 'Poisson', GREEN); lab(ax, 3.55, 8.2, 'Geom', YELLOW); lab(ax, 2.35, 7.8, 'Exp', PURPLE, ha='right')
ax.set_xlim(0, 6); ax.set_ylim(0, 10); ax.set_xticks([0, 1, 2, 3, 4, 5, 6]); ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.set_xlabel('均值', labelpad=1); ax.set_ylabel('方差', labelpad=1)
save(fig, here(__file__), 'figure', {'at_mean_2': {'Bin(10,0.2)': 1.6, 'Hyp(20,4,10)': 0.8421, 'Poisson(2)': 2, 'Geom(1/2)': 2, 'Exp(1/2)': 4}})
