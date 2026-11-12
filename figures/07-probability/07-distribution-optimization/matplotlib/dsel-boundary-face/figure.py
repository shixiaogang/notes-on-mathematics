"""Boundary moment. P uniform on {0,1,2}, T(x)=1{x>=1}, feasible moments [0,1].
For 0<m<1: Q*=(1-m, m/2, m/2), theta(m)=ln(m/(2(1-m))), D*(m)=(1-m)ln(3(1-m))+m ln(3m/2).
m=1: face {1,2}, Q*=(0,1/2,1/2), D*=ln(3/2), no finite theta.
(a) simplex: tilt family (yellow segment from delta_0 to (0,1/2,1/2)), constraint lines q1+q2=m for m=0.5,0.8,0.95 (thin red),
    optimal points (green), face q0=0 (thick red) with Q* (red point).
(b) theta(m) (blue) diverging as m->1.  (c) D*(m) (blue), continuous up to ln(3/2) (red point)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

fig, (a, b, c) = figure(width_mm=112, height_mm=44, ncols=3, gridspec_kw={'width_ratios': [1.15, 1, 1]})
simplex_axes(a)
fam = np.array([[1-mm, mm/2, mm/2] for mm in np.linspace(0, 1, 50)]); fx, fy = simplex_xy(fam)
a.plot(fx, fy, color=YELLOW, lw=1.5)
for mm in (0.5, 0.8, 0.95):
    L = np.array([[1-mm, mm, 0], [1-mm, 0, mm]]); lx, ly = simplex_xy(L)
    a.plot(lx, ly, color=RED, lw=0.7)
    gx, gy = simplex_xy(np.array([1-mm, mm/2, mm/2])); a.scatter([gx], [gy], s=10, color=GREEN, zorder=5)
E = np.array([[0, 1, 0], [0, 0, 1]]); ex, ey = simplex_xy(E)
a.plot(ex, ey, color=RED, lw=1.8)
sx, sy = simplex_xy(np.array([0, .5, .5])); a.scatter([sx], [sy], s=16, color=RED, zorder=6)
a.text(sx+0.04, sy, r'$Q^{*}$', va='center', ha='left')
m = np.linspace(0.01, 0.995, 400)
b.plot(m, np.log(m/(2*(1-m))), color=BLUE, lw=1.4)
b.axvline(1, color=STROKE, lw=0.8, ls='--')
b.set_xlim(0, 1.05); b.set_ylim(-4, 5)
b.set_xlabel(r'$m$', labelpad=1); b.set_ylabel(r'$\theta(m)$', labelpad=1)
mm = np.linspace(1e-6, 1-1e-9, 400)
D = (1-mm)*np.log(3*(1-mm))+mm*np.log(1.5*mm)
c.plot(mm, D, color=BLUE, lw=1.4)
c.scatter([1], [math.log(1.5)], s=16, color=RED, zorder=5)
c.scatter([2/3], [0], s=12, color=STROKE, zorder=5)
c.set_xlim(0, 1.05); c.set_ylim(0, 1.2)
c.set_xlabel(r'$m$', labelpad=1); c.set_ylabel(r'$D^{*}(m)$', labelpad=1)
fig.get_layout_engine().set(rect=(0, 0.1, 1, 0.9))
fig.canvas.draw()
for ax_, t_ in ((a, '(a)'), (b, '(b)'), (c, '(c)')):
    bb = ax_.get_position(); fig.text((bb.x0+bb.x1)/2, 0.015, t_, ha='center', va='bottom')
save(fig, HERE, 'figure', {'D_at_1': math.log(1.5), 'D_at_0': math.log(3), 'theta_0.9': math.log(0.9/0.2), 'theta_0.99': math.log(0.99/0.02)})
