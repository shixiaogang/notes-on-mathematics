"""Convexity of R(D) for Bern(0.3), Hamming. q1 optimal at D1=0.02, q2 optimal at D2=0.2,
mixture q=(q1+q2)/2 has distortion 0.11 and I(q) between R(0.11) and the chord."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

p = P_SRC; px = np.array([1-p, p]); d = np.array([[0, 1], [1, 0.]])


def qopt(D):
    if D >= p:
        return np.array([[1., 0.], [1., 0.]])
    r = (p-D)/(1-2*D)
    a = r*D/(1-p); b = (1-r)*D/p
    return np.array([[1-a, a], [b, 1-b]])


D1, D2 = 0., .3
q1, q2 = qopt(D1), qopt(D2); qm = (q1+q2)/2
I1, I2, Im = mutual_info(px, q1), mutual_info(px, q2), mutual_info(px, qm)
Dm = exp_dist(px, qm, d)
fig, ax = figure(width_mm=88, height_mm=52)
D = np.linspace(0, .34, 400)
ax.plot(D, rd_binary(D), color=BLUE, lw=1.4)
ax.plot([D1, D2], [I1, I2], color=PURPLE, lw=1.1, ls=DASH)
dot(ax, D1, I1, RED); dot(ax, D2, I2, RED)
dot(ax, Dm, Im, GREEN, ms=5)
dot(ax, Dm, float(rd_binary(Dm)), BLUE, ms=4)
ax.plot([Dm, Dm], [float(rd_binary(Dm)), (I1+I2)/2], color=STROKE, lw=.6, ls=DOT)
lab(ax, D1+.008, I1+.01, '$q_1$', INK, ha='left')
lab(ax, D2-.004, I2+.04, '$q_2$', INK, ha='center')
lab(ax, Dm+.008, Im+.01, '$q_{1/2}$', GREEN, ha='left')
lab(ax, .2, .3, '弦', PURPLE)
ax.set_xlim(0, .34); ax.set_ylim(0, .92)
axlab(ax, '$D$', '码率（bit）')
save(fig, HERE, 'figure', {'I1': I1, 'I2': I2, 'Imix': Im, 'Dmix': Dm, 'R_Dmix': float(rd_binary(Dm)), 'chord': (I1+I2)/2})
