"""Coordinate records of curves on the circle, and a smooth parametrization whose image has a cusp."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 104, 48
fig, ax = canvas(W, H)
def inset(x, y, w, h):
    a = fig.add_axes([x/W, y/H, w/W, h/H])
    a.spines[['top', 'right']].set_visible(False)
    a.tick_params(length=2, width=.75, pad=1.5)
    return a
a = inset(10, 13, 38, 32)
t = np.linspace(-1.35, 1.35, 401)
for f, c in ((t, BLUE), (2*t, GREEN), (t**3, YELLOW)):
    a.plot(t, f, color=c, lw=1.4)
a.set_xlim(-1.4, 1.4); a.set_ylim(-2.75, 2.75); a.set_xticks([-1, 0, 1]); a.set_yticks([-2, 0, 2])
a.set_xlabel('$t$', labelpad=.5); a.set_ylabel(r'$\theta$', labelpad=.5, rotation=0)
a.text(1.03, 2.5, r'$2t$', color=GREEN, fontsize=8); a.text(1.18, .78, '$t$', color=BLUE, fontsize=8); a.text(1.15, 2.38-.0, '', fontsize=8)
a.text(.66, -.55, '$t^3$', color=YELLOW, fontsize=8)
b = inset(62, 13, 40, 32)
t = np.linspace(-1.12, 1.12, 401)
b.plot(t**2, t**3, color=BLUE, lw=1.4)
tk = np.arange(-1.0, 1.01, .2)
b.plot(tk**2, tk**3, 'o', ms=3.0, mfc=INK, mec=INK)
b.set_xlim(-.12, 1.32); b.set_ylim(-1.35, 1.35); b.set_xticks([0, .5, 1]); b.set_yticks([-1, 0, 1])
b.set_xlabel('$y_1$', labelpad=.5); b.set_ylabel('$y_2$', labelpad=.5, rotation=0)
b.annotate(r"$\gamma^{\prime}(0)=0$", xy=(0, 0), xytext=(.36, -.9), fontsize=8, color=INK, ha='left',
           arrowprops=dict(arrowstyle='-|>', color=MUTED, lw=.75, mutation_scale=6, shrinkA=1, shrinkB=2))
panel_tag(ax, 29, 1.4, '(a)'); panel_tag(ax, 82, 1.4, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'theta=t,2t,t^3; gamma(t)=(t^2,t^3), dots at t=-1,-0.8,...,1'})
