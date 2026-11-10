from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Amplification factors in the complex plane for advection schemes.
th = np.linspace(0, 2*PI, 721); C = np.exp(1j*th)
fig, axes = figure(width_mm=112, height_mm=52, ncols=3)
panel(fig, left=.02, right=.98, wspace=.08, bottom=.14, top=.98)
def base(ax):
    ax.fill(C.real, C.imag, color=BLUE_FILL, lw=0); ax.plot(C.real, C.imag, color=BLUE, lw=1.1)
    ax.axhline(0, color=STROKE, lw=.5); ax.axvline(0, color=STROKE, lw=.5)
    ax.set_xlim(-1.9, 1.5); ax.set_ylim(-1.6, 1.6); ax.set_aspect('equal'); ax.axis('off')
g = lambda L: 1-L*(1-np.exp(-1j*th))
base(axes[0]); z = g(.5); axes[0].plot(z.real, z.imag, color=GREEN, lw=1.4)
base(axes[1]); z = g(1.3); axes[1].plot(z.real, z.imag, color=RED, lw=1.4)
base(axes[2]); z = 1-.5j*np.sin(th); axes[2].plot(z.real, z.imag, color=RED, lw=2)
tags(fig, axes); save(fig, HERE, 'figure', {'upwind_0.5_max': float(abs(g(.5)).max()), 'upwind_1.3_max': float(abs(g(1.3)).max()), 'ftcs_0.5_max': float(abs(1-.5j*np.sin(th)).max())})
print(abs(g(.5)).max(), abs(g(1.3)).max(), abs(1-.5j*np.sin(th)).max())
