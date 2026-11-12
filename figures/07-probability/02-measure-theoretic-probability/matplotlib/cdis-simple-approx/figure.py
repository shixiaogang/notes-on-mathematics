"""Simple-function approximation of int g dK(y,.), triangle model, y=0.4, g(x)=x^2.
g_n = 2^-n floor(2^n g); integrals of g_n under Unif(0.4,1) increase to 0.52."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
y0 = 0.4
def integral(n):
    s = 0.0
    for j in range(1, 2**n):
        c = math.sqrt(j/2**n)
        s += (1/2**n)*(min(1.0, (1 - c)/(1 - y0)) if c > y0 else 1.0)
    return s
fig, (a, b) = figure(width_mm=104, height_mm=46, ncols=2)
x = np.linspace(0, 1, 1200)
a.axvspan(y0, 1, ymin=0, ymax=0.04, color=BLUE_FILL, lw=0)
shades = {1: '#BACABF', 2: '#9EB3A5', 3: GREEN}
for n in (1, 2, 3):
    a.plot(x, np.floor(2**n*x**2)/2**n, color=shades[n], lw=1.1, drawstyle='steps-post')
a.plot(x, x**2, color=BLUE, lw=1.4)
a.set_xlim(0, 1); a.set_ylim(0, 1.05); a.set_xticks([0, 0.4, 1]); a.set_yticks([0, 0.5, 1])
a.set_xlabel('$x$', labelpad=1)
ns = np.arange(1, 9); vals = [integral(int(n)) for n in ns]
b.axhline(0.52, color=RED, lw=1.0, ls=DASH)
b.scatter(ns, vals, s=14, color=GREEN, zorder=3)
b.set_xlim(0.5, 8.5); b.set_ylim(0.2, 0.56); b.set_xticks(ns); b.set_yticks([0.2, 0.3, 0.4, 0.5])
b.set_xlabel('$n$', labelpad=1); b.set_ylabel('$\\int g_n\\,\\mathrm{d}K$')

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'y': y0, 'g': 'x^2', 'integrals': [round(v, 4) for v in vals], 'limit': (1 + y0 + y0**2)/3})
