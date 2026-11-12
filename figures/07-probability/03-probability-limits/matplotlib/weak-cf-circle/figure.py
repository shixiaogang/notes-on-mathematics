from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Fair die X in {1..6}: phi(t) = mean_k e^{itk} is the centroid of points e^{itk} on the unit circle.
k = np.arange(1, 7)
phi = lambda t: np.exp(1j*np.outer(np.atleast_1d(t), k)).mean(axis=1)
fig = None
import matplotlib.pyplot as plt
fig, axes = figure(width_mm=112, height_mm=46, ncols=3, gridspec_kw={'width_ratios': [1, 1, 1.5]})
fig.set_layout_engine(None); fig.subplots_adjust(left=.03, right=.98, top=.97, bottom=.3, wspace=.28)
th = np.linspace(0, 2*np.pi, 300)
for ax, t in zip(axes[:2], (0.5, np.pi/3)):
    ax.plot(np.cos(th), np.sin(th), color=STROKE, lw=.7)
    ax.axhline(0, color=GRID, lw=.6, zorder=0); ax.axvline(0, color=GRID, lw=.6, zorder=0)
    z = np.exp(1j*t*k)
    for zz in z: ax.plot([0, zz.real], [0, zz.imag], color=GREEN_FILL, lw=.7, zorder=1)
    ax.plot(z.real, z.imag, 'o', ms=3.6, color=GREEN, mew=0, zorder=4)
    c = phi(t)[0]; dot(ax, c.real, c.imag, RED, ms=4.6)
    ax.set_aspect('equal'); ax.set_xlim(-1.18, 1.18); ax.set_ylim(-1.18, 1.18); ax.axis('off')
    ps = ax.get_position(); ax.set_position([ps.x0, .13, ps.width, ps.y1-.13]); ax.set_anchor('S')
ax = axes[0]; z = np.exp(1j*.5*k)
for kk, zz in zip(k, z): lab(ax, 1.17*zz.real, 1.17*zz.imag, str(kk), GREEN, ha='center', va='center', fontsize=7)
ax = axes[2]; t = np.linspace(0, 2*np.pi, 800); ax.plot(t, np.abs(phi(t)), color=BLUE, lw=1.4)
dot(ax, .5, abs(phi(.5)[0]), RED, ms=3.8); dot(ax, np.pi/3, 0, RED, ms=3.8)
ax.set_xlim(0, 2*np.pi); ax.set_ylim(0, 1.05)
ax.set_xticks([0, np.pi/3, np.pi, 2*np.pi]); ax.set_xticklabels(['$0$', r'$\pi/3$', r'$\pi$', r'$2\pi$']); ax.set_yticks([0, .5, 1])
ax.set_xlabel(r'$t$', labelpad=3)
tags(fig, axes)
save(fig, HERE, 'figure', {'phi(0.5)': [float(phi(.5)[0].real), float(phi(.5)[0].imag)], 'abs': float(abs(phi(.5)[0])), 'phi(pi/3)': float(abs(phi(np.pi/3)[0]))})
