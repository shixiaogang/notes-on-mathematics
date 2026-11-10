from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: energy growth under forcing and the bound sqrt(E)<=sqrt(E0)+int ||f||/sqrt 2.
fig, ax = figure(width_mm=112, height_mm=44); style(ax)
t = np.linspace(0, 12, 6001)
aR = t*np.sin(np.pi*t)/(2*np.pi); dR = np.sin(np.pi*t)/(2*np.pi)+t*np.cos(np.pi*t)/2
aN = (np.cos(2*t)-np.cos(np.pi*t))/(np.pi**2-4); dN = (-2*np.sin(2*t)+np.pi*np.sin(np.pi*t))/(np.pi**2-4)
ER = np.sqrt(.25*(dR**2+np.pi**2*aR**2)); EN = np.sqrt(.25*(dN**2+np.pi**2*aN**2))
def cumtrap(y):
    return np.concatenate([[0], np.cumsum(.5*(y[1:]+y[:-1])*np.diff(t))])
bR = .5*cumtrap(np.abs(np.cos(np.pi*t))); bN = .5*cumtrap(np.abs(np.cos(2*t)))
ax.plot(t, bR, color=RED, lw=1.1, ls=(0, (3, 2)))
ax.plot(t, ER, color=BLUE, lw=1.4)
ax.plot(t, EN, color=YELLOW, lw=1.6)
ax.set_xlim(0, 12); ax.set_ylim(0, 4.2); ax.set_xlabel('$t$'); ax.set_ylabel(r'$\sqrt{E(t)}$')
print('sqrtE(12)=', ER[-1], 'bound', bR[-1], 'max violation', (ER-bR).max(), (EN-bN).max())
save(fig, HERE(__file__), 'figure', {'formula': 'E=(a^2_t+pi^2 a^2)/4; bound (1/2) int |cos(Omega s)| ds'})
