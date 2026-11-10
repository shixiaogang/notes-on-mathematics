from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: boundary-driven half line u=g(t-x), g=sin^2(pi t) on [0,1], c=1, with injected energy.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
g = lambda r: np.where((r >= 0) & (r <= 1), np.sin(np.pi*np.clip(r, 0, 1))**2, 0.)
xs = np.linspace(0, 3, 601); ts = np.linspace(0, 3, 601); X, TT = np.meshgrid(xs, ts)
ax = axs[0]; style(ax); field(ax, g(TT-X), [0, 3, 0, 3], vmax=1.)
ax.plot([0, 3], [0, 3], color=LINE, lw=1.0); ax.plot([0, 2], [1, 3], color=LINE, lw=1.0)
ax.plot([0, 0], [0, 1], color=RED, lw=2.2, clip_on=False, zorder=5)
ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2, 3]); ax.set_ylabel('$t$'); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax); t = np.linspace(0, 2, 2001)
P = np.where(t <= 1, (np.pi*np.sin(2*np.pi*t))**2, 0.)
# Energy by direct spatial quadrature of (u_t^2+u_x^2)/2 at each time.
gp = lambda r: np.where((r >= 0) & (r <= 1), np.pi*np.sin(2*np.pi*r), 0.)
x = np.linspace(0, 2.2, 8801)
E = np.array([np.trapezoid(gp(tt-x)**2, x) if hasattr(np, 'trapezoid') else np.trapz(gp(tt-x)**2, x) for tt in t])
ax.plot(t, P, color=PURPLE, lw=1.3); ax.plot(t, E, color=BLUE, lw=1.5)
ax.axhline(np.pi**2/2, color=RED, lw=.95, ls=(0, (3, 2)))
ax.text(1.97, 5.3, r'$\pi^{2}/2$', color=RED, ha='right'); ax.text(1.3, 3.9, '$E(t)$', color=BLUE); ax.text(1.03, 8.6, '功率', color=PURPLE)
ax.set_xlim(0, 2); ax.set_ylim(0, 10.5); ax.set_xticks([0, 1, 2]); sub(ax, 'b', '$t$')
save(fig, HERE(__file__), 'figure', {'formula': 'u=g(t-x); P=g\'(t)^2; E by quadrature; final pi^2/2'})
