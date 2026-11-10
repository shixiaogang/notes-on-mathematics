from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: modal response a(t) for L=1,c=1,f=sin(pi x)cos(Omega t), resonance vs non-resonance vs heat-mode.
fig, ax = figure(width_mm=112, height_mm=44); style(ax)
t = np.linspace(0, 12, 3001)
ax.axhline(0, color=GRID, lw=.85)
ax.plot(t, t/(2*np.pi), color=RED, lw=.95, ls=(0, (3, 2))); ax.plot(t, -t/(2*np.pi), color=RED, lw=.95, ls=(0, (3, 2)))
ax.plot(t, (np.cos(2*t)-np.cos(np.pi*t))/(np.pi**2-4), color=YELLOW, lw=1.6)
ax.plot(t, t*np.sin(np.pi*t)/(2*np.pi), color=BLUE, lw=1.4)
lam = np.pi**2; W = np.pi
H = (lam*np.cos(W*t)+W*np.sin(W*t)-lam*np.exp(-lam*t))/(lam**2+W**2)
ax.plot(t, H, color=PURPLE, lw=1.3)
ax.set_xlim(0, 12); ax.set_ylim(-2.1, 2.1); ax.set_ylabel('$a_1(t)$'); ax.set_xlabel('$t$')
save(fig, HERE(__file__), 'figure', {'formula': 'a=t sin(pi t)/(2 pi); (cos 2t - cos pi t)/(pi^2-4); heat mode with lambda=pi^2'})
