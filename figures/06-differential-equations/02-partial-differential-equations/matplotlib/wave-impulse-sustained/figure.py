from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: sustained forcing f=box(x) as a superposition of unit impulses; c=1.
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
x = np.linspace(-6, 6, 1201); T0 = 3.
s = np.linspace(0, T0, 3001)
def sustained(x, t):
    r = np.maximum(t-s, 0.)
    return np.trapezoid(wave_box(x[..., None], r), s, axis=-1) if hasattr(np, 'trapezoid') else np.trapz(wave_box(x[..., None], r), s, axis=-1)
ax = axs[0]; style(ax)
for s0, col in zip([2, 1, 0], SHADES[:3]):
    ax.plot(x, wave_box(x, T0-s0), color=col, lw=1.2)
ax.plot(x, sustained(x, T0), color=BLUE, lw=1.6)
ax.plot(x, box(x)*.0+0, color=GRID, lw=.1)
ax.set_xlim(-5.5, 5.5); ax.set_ylim(0, 2.75); ax.set_xticks([-4, 0, 4]); ax.set_ylabel('$u(x,3)$'); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax); t = np.linspace(0, 4, 801)
ax.plot(t, np.minimum(t, 1), color=YELLOW, lw=1.7)
ax.plot(t, np.where(t <= 1, t**2/2, t-.5), color=BLUE, lw=1.5)
ax.plot([1], [.5], 'o', ms=3.4, color=RED); ax.plot([1], [1], 'o', ms=3.4, color=RED)
ax.text(2.55, .5, '瞬时冲击', color=YELLOW); ax.text(.55, 2.5, '持续驱动', color=BLUE)
ax.set_xlim(0, 4); ax.set_ylim(0, 3.7); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_ylabel('$u(0,t)$'); sub(ax, 'b', '$t$')
save(fig, HERE(__file__), 'figure', {'formula': 'impulse min(t,1); sustained t^2/2 (t<=1), t-1/2 (t>=1) at x=0; profile at t=3 by quadrature'})
