"""Reverse water-filling for independent Gaussian components with variances (4,1,0.25).
(a) total distortion D=1.5 -> level theta=0.625; D_k=min(theta, sigma_k^2) (blue fill), rates
    (1/2)log2(sigma_k^2/D_k)=1.339, 0.339, 0 bit.
(b) total R(D) in bits per vector; red dots where components drop out (D=0.75, 2.25), green: example."""
from pathlib import Path
import sys
import math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

sig = np.array([4., 1., .25])


def level(D):
    lo, hi = 0., sig.max()
    for _ in range(200):
        t = (lo+hi)/2
        if np.minimum(t, sig).sum() < D: lo = t
        else: hi = t
    return (lo+hi)/2


def Rtot(D):
    if D >= sig.sum(): return 0.
    t = level(D); Dk = np.minimum(t, sig)
    return float(np.sum(.5*np.log2(sig/Dk)))


th = level(1.5); Dk = np.minimum(th, sig); Rk = .5*np.log2(sig/Dk)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, right=.985, top=.95, bottom=.27, wspace=.3)
ax = axs[0]
for k, s in enumerate(sig):
    ax.bar(k, s, width=.6, color='white', edgecolor=BLUE, lw=.9, zorder=2)
    ax.bar(k, Dk[k], width=.6, color=BLUE_FILL, edgecolor=BLUE, lw=.9, zorder=3)
    lab(ax, k, max(s, th+.3)+.12, f'$R_{k+1}={Rk[k]:.3f}$', INK, ha='center')
ax.axhline(th, color=RED, lw=1.1, zorder=4)
lab(ax, 2.95, th+.1, '$\\theta=0.625$', RED, ha='right')
ax.set_xticks([0, 1, 2]); ax.set_xticklabels(['$\\sigma_1^2=4$', '$\\sigma_2^2=1$', '$\\sigma_3^2=0.25$'])
ax.set_ylim(0, 4.7); ax.set_xlim(-.5, 3.0)
ax.set_ylabel('方差与失真', labelpad=1)
ax = axs[1]
D = np.linspace(.05, 5.6, 400)
ax.plot(D, [Rtot(x) for x in D], color=BLUE, lw=1.4)
for x in (.75, 2.25):
    dot(ax, x, Rtot(x), RED)
dot(ax, 1.5, Rtot(1.5), GREEN, ms=4.6)
lab(ax, 1.62, Rtot(1.5)+.15, f'$({1.5},\\,{Rtot(1.5):.3f})$', GREEN, ha='left')
ax.set_xlim(0, 5.6); ax.set_ylim(0, 5)
axlab(ax, '总失真', '码率（bit/向量）')
tags(fig, axs)
save(fig, HERE, 'figure', {'theta': th, 'Dk': Dk.tolist(), 'Rk': Rk.tolist(), 'R_total': float(Rk.sum()),
                          'R_at_0.75': Rtot(.75), 'R_at_2.25': Rtot(2.25)})
