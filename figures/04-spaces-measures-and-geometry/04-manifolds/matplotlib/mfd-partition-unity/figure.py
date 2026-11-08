"""The flat function eta, the cutoff chi, and a two-function partition of unity on the real line."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 110, 44
fig, ax = canvas(W, H)
def inset(x, y, w, h):
    a = fig.add_axes([x/W, y/H, w/W, h/H])
    a.spines[['top', 'right']].set_visible(False)
    a.tick_params(length=2, width=.75, pad=1.5)
    return a
def eta(t):
    t = np.asarray(t, float); out = np.zeros_like(t); out[t > 0] = np.exp(-1/t[t > 0]); return out
a = inset(10, 12.5, 25, 29)
t = np.linspace(-1.5, 4, 801); a.plot(t, eta(t), color=BLUE, lw=1.4)
a.set_xlim(-1.5, 4); a.set_ylim(-.05, 1.0); a.set_xticks([0, 2, 4]); a.set_yticks([0, .5, 1], ['$0$', '$0.5$', '$1$']); a.set_xlabel('$t$', labelpad=.5); a.set_ylabel(r'$\eta(t)$', labelpad=.5)
b = inset(45, 12.5, 25, 29)
r, R = 1.0, 2.0
x = np.linspace(-3, 3, 1201); nu = eta(R**2-x**2); de = nu+eta(x**2-r**2); b.plot(x, nu/de, color=BLUE, lw=1.4)
for v in (-2, -1, 1, 2):
    b.axvline(v, color=MUTED, lw=.6, ls=(0, (2.2, 1.8)))
b.set_xlim(-3, 3); b.set_ylim(-.05, 1.12); b.set_xticks([-2, -1, 1, 2]); b.set_yticks([0, 1], ['$0$', '$1$']); b.set_xlabel('$x$', labelpad=.5); b.set_ylabel(r'$\chi(x)$', labelpad=.5)
c = inset(79, 15, 27, 26)
x = np.linspace(-2, 2, 1201)
u, v = eta(.5-x), eta(x+.5)
c.plot(x, u/(u+v), color=BLUE, lw=1.4); c.plot(x, v/(u+v), color=GREEN, lw=1.4)
c.set_xlim(-2, 2); c.set_ylim(-.05, 1.08); c.set_xticks([-1, -.5, .5, 1], ['$-1$', r'$-\frac{1}{2}$', r'$\frac{1}{2}$', '$1$']); c.set_yticks([0, 1], ['$0$', '$1$'])
c.text(-1.75, .78, r'$\psi_1$', color=BLUE, fontsize=8); c.text(1.25, .78, r'$\psi_2$', color=GREEN, fontsize=8)
c.spines['bottom'].set_position(('data', -.05))
# supports of the cover drawn under the axis, in the canvas.
xp = lambda v: 79+(v+2)/4*27
ax.plot([xp(-2), xp(1)], [10.2, 10.2], color=BLUE, lw=1.6); ax.plot([xp(-1), xp(2)], [8.0, 8.0], color=GREEN, lw=1.6)
dot(ax, (xp(1), 10.2), BLUE, size=1.1, hollow=True); dot(ax, (xp(-1), 8.0), GREEN, size=1.1, hollow=True)
label(ax, (xp(-1.62), 7.6), '$U_2$', 7.5, GREEN); label(ax, (xp(1.65), 11.2), '$U_1$', 7.5, BLUE)
panel_tag(ax, 22.5, 1.4, '(a)'); panel_tag(ax, 57.5, 1.4, '(b)'); panel_tag(ax, xp(0), 1.4, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'eta(t)=exp(-1/t) for t>0, else 0; chi with r=1,R=2; psi_1,psi_2 on U1=(-inf,1), U2=(-1,inf)'})
