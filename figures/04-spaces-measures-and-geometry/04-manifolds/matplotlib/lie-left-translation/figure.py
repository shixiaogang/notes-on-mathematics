"""SO(2) as the unit circle in span(I,J): the velocity J at I, its left translate A J, and the left-invariant field."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 100, 50
fig, ax = canvas(W, H)
th0 = np.radians(62)
def base(cx, cy, r):
    t = np.linspace(0, 2*np.pi, 361)
    ax.plot(cx+r*np.cos(t), cy+r*np.sin(t), color=BLUE, lw=1.3, zorder=3)
    arrow(ax, (cx-r-5, cy), (cx+r+6, cy), color=MUTED, lw=.7, scale=5, zorder=1)
    arrow(ax, (cx, cy-r-4), (cx, cy+r+6), color=MUTED, lw=.7, scale=5, zorder=1)
    label(ax, (cx+r+6.8, cy+.2), '$I$', 7.5, MUTED, ha='left')
    label(ax, (cx+1.7, cy+r+5.7), '$J$', 7.5, MUTED, ha='left')
L = 8.2
r = 15
cx, cy = 24.5, 26
base(cx, cy, r)
I = np.array([cx+r, cy])
A = np.array([cx+r*np.cos(th0), cy+r*np.sin(th0)])
arrow(ax, I, I+[0, L], color=RED, lw=1.25, scale=6.5)
arrow(ax, A, A+L*np.array([-np.sin(th0), np.cos(th0)]), color=RED, lw=1.25, scale=6.5)
dot(ax, I, INK); dot(ax, A, INK)
label(ax, I+[2.5, 3.8], '$J$', color=RED, halo=True)
label(ax, A+L*np.array([-np.sin(th0), np.cos(th0)])+[-2.8, .8], '$AJ$', color=RED, halo=True)
label(ax, I+[2.7, -1.8], '$I$', halo=True)
label(ax, A+[2.5, 1.2], '$A$', halo=True)
t = np.linspace(.08, th0-.08, 30)
ax.plot(cx+(r-3.6)*np.cos(t), cy+(r-3.6)*np.sin(t), color=STROKE, lw=.8, zorder=3)
arrow(ax, (cx+(r-3.6)*np.cos(t[-3]), cy+(r-3.6)*np.sin(t[-3])), (cx+(r-3.6)*np.cos(t[-1]), cy+(r-3.6)*np.sin(t[-1])), color=STROKE, lw=.8, scale=5)
label(ax, (cx+(r-8.4)*np.cos(th0/2), cy+(r-8.4)*np.sin(th0/2)), '$L_A$', halo=True)
# (b) field
cx2 = 74
base(cx2, cy, r)
for k in range(12):
    a = 2*np.pi*k/12+.13
    P = np.array([cx2+r*np.cos(a), cy+r*np.sin(a)])
    arrow(ax, P, P+.72*L*np.array([-np.sin(a), np.cos(a)]), color=RED, lw=1.1, scale=6)
panel_tag(ax, cx, 1.7, '(a)'); panel_tag(ax, cx2, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'cos t I + sin t J; tangent at A=R(62deg) is AJ=-sin t I+cos t J; field A->AJ'})
