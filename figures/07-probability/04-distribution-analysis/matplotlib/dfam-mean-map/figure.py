"""Gaussian natural parameters theta=(m/s^2,-1/(2s^2)) and mean parameters eta=(m, m^2+s^2).
(a) half-plane theta2<0 with lines theta1=const (blue), theta2=const (yellow); (b) their images under grad A; parabola eta2=eta1^2."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

def eta(t1, t2):
    return -t1/(2*t2), t1*t1/(4*t2*t2)-1/(2*t2)
fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2)
a.fill_between([-2.2, 2.2], [-2.2, -2.2], [0, 0], color=BLUE_FILL, lw=0)
a.axhline(0, color=STROKE, lw=0.9, ls='--')
t2s = np.linspace(-2.2, -0.12, 200)
for t1 in (-1.5, -1, -0.5, 0, 0.5, 1, 1.5):
    a.plot(np.full_like(t2s, t1), t2s, color=BLUE, lw=0.9)
    e1, e2 = eta(t1, t2s); b.plot(e1, e2, color=BLUE, lw=0.9)
t1s = np.linspace(-2.2, 2.2, 200)
for t2 in (-2, -1, -0.5, -0.25):
    a.plot(t1s, np.full_like(t1s, t2), color=YELLOW, lw=1.1)
    e1, e2 = eta(t1s, t2); b.plot(e1, e2, color=YELLOW, lw=1.1)
a.scatter([1], [-0.5], s=16, color=RED, zorder=5)
a.set_xlim(-2.2, 2.2); a.set_ylim(-2.2, 0.6); a.set_xlabel(r'$\theta_1$', labelpad=1); a.set_ylabel(r'$\theta_2$', labelpad=1)
e = np.linspace(-3, 3, 200)
b.plot(e, e*e, color=PURPLE, lw=1.3, ls='--')
b.scatter([1], [2], s=16, color=RED, zorder=5)
b.set_xlim(-3, 3); b.set_ylim(0, 6); b.set_xlabel(r'$\eta_1$', labelpad=1); b.set_ylabel(r'$\eta_2$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, HERE, 'figure', {'eta_of_(1,-0.5)': list(map(float, eta(1.0, -0.5)))})
