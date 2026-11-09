from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# One variable x in [0,4]: f1=x, f2=(x-1)^2(x-3)^2+0.4x. Curve in objective plane.
fig, ax = figure(width_mm=86, height_mm=58)
x = np.linspace(0, 4, 4001); f2 = (x-1)**2*(x-3)**2+.4*x
rec = np.minimum.accumulate(f2); glob = f2 <= rec+1e-12
d = np.gradient(f2, x); loc = (d < 0)&~glob
setup(ax, (-.15, 4.15), (0, 3.2), range(0, 5), range(0, 4))
ax.plot(x, f2, color=BLUE, lw=1.1, zorder=2)
def seg(mask, **kw):
    idx = np.where(mask)[0]
    for g in np.split(idx, np.where(np.diff(idx) > 1)[0]+1): ax.plot(x[g], f2[g], **kw)
seg(glob, color=RED, lw=2.2, zorder=4, solid_capstyle='round')
seg(loc, color=PURPLE, lw=2.2, zorder=4, solid_capstyle='round')
i1 = np.where(glob)[0][-1]; j = 3000+np.argmin(f2[2500:3500])-500
j = 2500+np.argmin(f2[2500:3500])
dot(ax, (x[i1], f2[i1])); dot(ax, (x[j], f2[j]), PURPLE)
ax.plot([x[i1], x[j]], [f2[i1]]*2, color=MUTED, lw=.85, ls=(0, (3, 2))); ax.plot([x[j]]*2, [f2[i1], f2[j]], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.text(x[i1]-.04, f2[i1]-.28, '$P$', color=INK, ha='center'); ax.text(x[j]+.05, f2[j]+.18, '$Q$', color=INK)
save(fig, HERE, 'figure', {'P': [float(x[i1]), float(f2[i1])], 'Q': [float(x[j]), float(f2[j])]})
print(x[i1], f2[i1], x[j], f2[j], x[loc].min(), x[loc].max())
