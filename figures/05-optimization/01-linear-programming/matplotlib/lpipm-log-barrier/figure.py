from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# One-variable barrier: -mu log x, and x - mu log x with minimizer x = mu.
x = np.linspace(.004, 3.2, 800)
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
styles = [(1., BLUE, '-'), (.3, BLUE, '--'), (.08, BLUE, ':')]
for mu, c, ls in styles:
    a.plot(x, -mu * np.log(x), color=c, ls=ls, lw=1.4)
    f = x - mu * np.log(x); b.plot(x, f, color=c, ls=ls, lw=1.4)
    b.plot([mu], [mu - mu * np.log(mu)], 'o', color=GREEN, ms=4, zorder=6)
for mu, xx, yy in [(1., .22, 2.15), (.3, .42, .62), (.08, 1.02, .16)]:
    a.text(xx, yy, f'$\\mu={mu:g}$', fontsize=7.5)
a.plot([0, 0], [-1.2, 3], color='#4C4D4F', lw=2)
a.set_xlim(-.05, 3.2); a.set_ylim(-1.2, 3)
b.plot([0, 0], [0, 3], color='#4C4D4F', lw=2)
b.plot([0], [0], 'o', color=RED, ms=5, zorder=7, clip_on=False)
b.plot(x, x, color=MUTED, lw=.85)
b.text(2.05, 2.5, '$f=x$', fontsize=7.5, color=MUTED, ha='right')
b.text(1.3, .62, '$\\mu=1$', fontsize=7.5); b.text(.62, 1.42, '$\\mu=0.3$', fontsize=7.5)
b.set_xlim(-.05, 3.2); b.set_ylim(0, 3)
xlab(a, '$x$', '(a) 障碍项'); xlab(b, '$x$', '(b) 目标加障碍项')
save(fig, OUT, 'figure', {'formula': '-mu log x; x-mu log x, minimizer x=mu', 'mu': [1, .3, .08]})
