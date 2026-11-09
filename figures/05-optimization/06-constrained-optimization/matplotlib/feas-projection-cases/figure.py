from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
ax = axs[0]; ax.fill([0, 1, 1, 0], [0, 0, 1, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95)
for z in ([1.4, -.3], [.5, 1.35], [-.3, .4]):
    z = np.array(z); p = np.clip(z, 0, 1); ax.plot([z[0], p[0]], [z[1], p[1]], color=YELLOW, lw=1.1, ls=(0, (2, 1.4))); hollow(ax, z, GREEN, ms=4); dot(ax, p, GREEN, ms=4.4)
off(ax, (-.42, 1.5), (-.46, 1.46))
ax = axs[1]; triangle(ax, labels=True); off(ax, (-.2, 1.2), (-.42, 1.02))
for x in ([1.5, -.3, -.2], [.9, .5, -.4], [.3, -.4, 1.1]):
    z = np.array(x, float); za = z-(z.sum()-1)/3; p = proj(z)[0]; Z = bary(za); Q = bary(p); ax.plot([Z[0], Q[0]], [Z[1], Q[1]], color=YELLOW, lw=1.1, ls=(0, (2, 1.4))); hollow(ax, Z, GREEN, ms=4); dot(ax, Q, GREEN, ms=4.4)
ax = axs[2]; ax.plot([1, 0], [0, 1], color=BLUE, lw=1.6, zorder=2); ax.axhline(0, color=MUTED, lw=.7, zorder=0); ax.axvline(0, color=MUTED, lw=.7, zorder=0)
z = np.array([1.2, .4]); p = proj(z)[0]; n = z/z.sum()
ax.plot([z[0], p[0]], [z[1], p[1]], color=YELLOW, lw=1.1, ls=(0, (2, 1.4))); ax.plot([0, z[0]], [0, z[1]], color=MUTED, lw=.85, ls=(0, (1, 1.5)))
hollow(ax, z, GREEN, ms=4); dot(ax, p, GREEN, ms=4.4); dot(ax, n, RED, ms=4.4)
z2 = np.array([1.4, -.4]); hollow(ax, z2, RED, ms=4); dot(ax, proj(z2)[0], GREEN, ms=4.4); ax.plot([z2[0], 1], [z2[1], 0], color=YELLOW, lw=1.1, ls=(0, (2, 1.4)))
ax.text(1.27, .5, '$z$', fontsize=8); ax.text(.42, .02, '归一化', fontsize=7.5, ha='center', color=RED); ax.text(1.03, .17, '投影', fontsize=7.5, ha='left'); ax.text(1.31, -.5, "$z'$", fontsize=8, ha='right')
ax.text(1.58, -.06, '$x_1$', fontsize=7.5, va='top', ha='right'); ax.text(.04, 1.08, '$x_2$', fontsize=7.5)
off(ax, (-.12, 1.6), (-.56, 1.22))
panels(fig, .01, .99, .99, .1, .02); tags(fig, axs)
save(fig, HERE, 'figure', {'box': [0, 1], 'normalize': n.tolist(), 'project': p.tolist()})
