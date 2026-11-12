"""Degenerate Fisher information. (a) N(a+b,1): L=(a+b-1)^2/2 constant on lines a+b=c (gray); G=[[1,1],[1,1]] has null direction (1,-1) (red);
natural direction via pseudo-inverse at (1.5,0.5) is ((c-1)/2)(1,1) (green). (b) N(theta^3,1), L=(theta^3-1)^2/2:
Euclidean gradient 3 theta^2(theta^3-1) (yellow) vanishes at 0, G^{-1} g=(theta^3-1)/(3 theta^2) (green) blows up; in m=theta^3 the natural gradient is m-1 (blue)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, (a, b) = figure(width_mm=108, height_mm=52, ncols=2)
x = np.linspace(-0.5, 2.5, 10)
for c in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    a.plot(x, c-x, color=BLUE if c == 1.0 else STROKE, lw=1.3 if c == 1.0 else 0.6, ls='-' if c == 1.0 else (0, (3, 2)))
P = np.array([1.5, 0.5]); c = P.sum()
a.annotate('', xy=P+0.5*np.array([1, -1]), xytext=P-0.5*np.array([1, -1]), arrowprops=dict(arrowstyle='<|-|>', color=RED, lw=1.2, mutation_scale=7))
d = -(c-1)/2*np.array([1, 1])
a.annotate('', xy=P+d, xytext=P, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.5, mutation_scale=8))
a.scatter([P[0]], [P[1]], s=12, color=STROKE, zorder=5)
a.set_xlim(-0.5, 2.5); a.set_ylim(-0.5, 2.5); a.set_aspect('equal')
a.set_xlabel(r'$a$', labelpad=1); a.set_ylabel(r'$b$', labelpad=1)
t = np.linspace(-1.2, 1.4, 600); tn = t[np.abs(t) > 0.18]
b.axhline(0, color=STROKE, lw=0.6)
b.plot(t, 3*t**2*(t**3-1), color=YELLOW, lw=1.5)
tl = t[t < -0.18]; tr = t[t > 0.18]
for seg in (tl, tr):
    b.plot(seg, (seg**3-1)/(3*seg**2), color=GREEN, lw=1.4)
b.plot(t, t**3-1, color=BLUE, lw=1.2, ls='--')
b.scatter([0], [0], s=14, color=RED, zorder=5)
b.set_xlim(-1.2, 1.4); b.set_ylim(-6, 3); b.set_xlabel(r'$\theta$', labelpad=1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30)
save(fig, HERE, 'figure', {'point': P.tolist(), 'pinv_dir': d.tolist()})
