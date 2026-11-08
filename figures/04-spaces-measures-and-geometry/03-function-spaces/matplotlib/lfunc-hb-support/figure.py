from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (R^2,l1) 与 (R^2,l2) 中延拓 l(s,0)=s：约束 -||m+z||-l(m)<=t<=||m+z||-l(m)，m=(a,0)，z=(0,1)。
from matplotlib.patches import Circle, Polygon
fig, axes = figure(width_mm=112, height_mm=92, nrows=2, ncols=2, height_ratios=[1, 1.1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.985, bottom=.09, wspace=.2, hspace=.3)
a = axes[0, 0]; b = axes[0, 1]; c = axes[1, 0]; d = axes[1, 1]
for ax in (a, b):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.75, 2.15); ax.set_ylim(-1.55, 1.55)
a.add_patch(Polygon([[1, 0], [0, 1], [-1, 0], [0, -1]], closed=True, fc=BLUE_FILL, ec=BLUE, lw=1.2, zorder=1))
for ts in (-1, -.5, 0, .5, 1):
    y = np.array([-1.5, 1.5]); x = 1-ts*y
    a.plot(x, y, color=GREEN if ts != 0 else YELLOW, lw=1.0 if ts != 0 else 1.2, zorder=2)
a.plot([1], [0], 'o', color=BLUE, ms=4.2, mew=0, zorder=4); a.text(1.16, -.33, '$(1,0)$', ha='left', va='center', bbox=dict(fc='white', ec='none', pad=.8), zorder=5)
a.plot([-1.7, 2.1], [0, 0], color=MUTED, lw=.85, zorder=0); 
a.text(-1.72, .08, '$M$', ha='left', va='bottom')
a.text(-.0, -.12, r'', ha='center')
th = np.linspace(0, 2*np.pi, 300)
b.add_patch(Circle((0, 0), 1, fc=BLUE_FILL, ec=BLUE, lw=1.2, zorder=1))
b.plot([1, 1], [-1.5, 1.5], color=YELLOW, lw=1.2, zorder=2)
b.plot([1], [0], 'o', color=BLUE, ms=4.2, mew=0, zorder=4); b.text(1.07, -.3, '$(1,0)$', ha='left', va='center')
b.plot([-1.7, 2.1], [0, 0], color=MUTED, lw=.85, zorder=0)
b.text(-1.72, .08, '$M$', ha='left', va='bottom')
s = np.linspace(-3, 3, 601)
up1 = np.abs(s)+1-s; lo1 = -np.abs(s)-1-s
up2 = np.sqrt(s**2+1)-s; lo2 = -np.sqrt(s**2+1)-s
for ax, u, l in ((c, up1, lo1), (d, up2, lo2)):
    ax.plot(s, u, color=BLUE, lw=1.4); ax.plot(s, l, color=BLUE, lw=1.4)
    ax.axhline(0, color=MUTED, lw=.85, zorder=0)
    ax.set_xlim(-3, 3); ax.set_ylim(-4.6, 4.6); ax.set_xticks([-3, 0, 3]); ax.set_yticks([-3, -1, 0, 1, 3])
    ax.text(1.0, .025, '$a$', transform=ax.transAxes, ha='right', va='bottom')
c.axhspan(-1, 1, xmin=0, xmax=1, color=GREEN_FILL, lw=0, zorder=0)
c.plot([0, 0], [-1, 1], color=GREEN, lw=2.0, zorder=3, solid_capstyle='butt')
c.text(.25, .35, 't 的可选范围', ha='left', va='center', fontsize=7.5)
d.axhline(0, color=GREEN, lw=1.6, zorder=3)
c.text(-2.75, 3.5, '上界', ha='left'); c.text(.4, -4.1, '下界', ha='left')
d.text(-2.75, 3.5, '上界', ha='left'); d.text(.4, -4.1, '下界', ha='left')
for ax, q in (('(a)', a), ('(b)', b)):
    pos = q.get_position(); fig.text((pos.x0+pos.x1)/2, pos.y0-.028, ax, ha='center', va='top')
for ax, q in (('(c)', c), ('(d)', d)):
    pos = q.get_position(); fig.text((pos.x0+pos.x1)/2, pos.y0-.058, ax, ha='center', va='top')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'L_t(x)=x1+t x2, |t|<=1; envelopes |a|+1-a, -|a|-1-a; sqrt(a^2+1)-a, -sqrt(a^2+1)-a'})
