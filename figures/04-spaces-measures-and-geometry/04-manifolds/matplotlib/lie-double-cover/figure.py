"""Half-angle great circle q(theta) double-covering the rotation circle."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
t = np.linspace(0, 2*np.pi, 361)
R0 = 17
cx1, cy = 30, 26
# (a): the great circle (cos(theta/2), sin(theta/2)); theta in [0,2pi] upper arc, [2pi,4pi] lower arc.
up = np.linspace(0, np.pi, 180); low = np.linspace(np.pi, 2*np.pi, 180)
ax.plot(cx1+R0*np.cos(up), cy+R0*np.sin(up), color=BLUE, lw=1.4, zorder=3)
ax.plot(cx1+R0*np.cos(low), cy+R0*np.sin(low), color=GREEN, lw=1.4, zorder=3)
arrow(ax, (cx1-R0-4, cy), (cx1+R0+4, cy), color=MUTED, lw=.7, scale=5, zorder=1)
arrow(ax, (cx1, cy-R0-4), (cx1, cy+R0+4), color=MUTED, lw=.7, scale=5, zorder=1)
label(ax, (cx1+R0+4.4, cy-2.8), '$s$', 7.5, MUTED); label(ax, (cx1+1.9, cy+R0+4.6), r'$\Vert u\Vert$', 7.5, MUTED, ha='left')
q = np.array([np.cos(np.pi/4), np.sin(np.pi/4)])
pts = {'q': np.array([cx1, cy])+R0*q, '-q': np.array([cx1, cy])-R0*q, 'e': np.array([cx1+R0, cy]), '-e': np.array([cx1-R0, cy])}
for k in ('q', '-q'):
    dot(ax, pts[k], RED, zorder=8)
dot(ax, pts['e'], INK, zorder=8); dot(ax, pts['-e'], INK, zorder=8)
ax.plot(*zip(pts['q'], pts['-q']), color=RED, lw=.7, ls=(0, (3, 2)), zorder=2)
label(ax, pts['q']+[2.5, 2.5], '$q$', color=RED, halo=True)
label(ax, pts['-q']+[-3.0, -2.5], '$-q$', color=RED, halo=True)
label(ax, pts['e']+[5.5, 4.0], r'$\theta=0$', 7.5, INK, halo=True)
label(ax, pts['-e']+[-5.5, 4.0], r'$\theta=2\pi$', 7.5, INK, halo=True)
# (b): the rotation circle.
cx2 = 90
ax.plot(cx2+R0*np.cos(t), cy+R0*np.sin(t), color=BLUE, lw=1.4, zorder=3)
ax.plot(cx2+(R0-1.5)*np.cos(t), cy+(R0-1.5)*np.sin(t), color=GREEN, lw=1.0, zorder=3)
arrow(ax, (cx2-R0-4, cy), (cx2+R0+4, cy), color=MUTED, lw=.7, scale=5, zorder=1)
P = np.array([cx2, cy+R0]); dot(ax, P, RED, zorder=8)
label(ax, P+[9.4, 2.0], r'$\theta=\pi/2$', 7.5, RED, halo=True)
E = np.array([cx2+R0, cy]); dot(ax, E, INK, zorder=8)
label(ax, E+[3.4, 2.5], '$I$', halo=True)
arrow(ax, (cx1+R0+7, cy+11), (cx2-R0-7, cy+11), color=STROKE, lw=.9, scale=6, rad=-.15)
label(ax, ((cx1+cx2)/2, cy+18), r'$q\mapsto R(q)$')
panel_tag(ax, cx1, 1.7, '(a)'); panel_tag(ax, cx2, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'q(theta)=(cos(theta/2), sin(theta/2)a); q=(cos pi/4, sin pi/4) for theta=pi/2, -q for theta=pi/2+2pi'})
