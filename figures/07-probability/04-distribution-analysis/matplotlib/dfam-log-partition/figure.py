"""A(theta)=ln(1+e^t+e^{2t}) with tangent at ln 2 (slope 10/7), asymptotes 0 and 2t; (b) mean A' and variance A''."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

import math
t = np.linspace(-4, 4, 800)
def mom(t):
    w = np.vstack([np.ones_like(t), np.exp(t), np.exp(2*t)]); w = w/w.sum(0)
    m = w[1]+2*w[2]; v = w[1]+4*w[2]-m*m
    return m, v
A = np.log(1+np.exp(t)+np.exp(2*t))
m, v = mom(t)
t0 = math.log(2); A0 = math.log(7); m0, v0 = 10/7, 26/49
fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2)
a.plot(t, A, color=BLUE, lw=1.4)
a.plot(t, np.zeros_like(t), color=STROKE, lw=0.7, ls='--'); a.plot(t, 2*t, color=STROKE, lw=0.7, ls='--')
tt = np.linspace(t0-1.6, t0+1.6, 50)
a.plot(tt, A0+m0*(tt-t0), color=PURPLE, lw=1.2, ls='--')
a.scatter([t0], [A0], s=16, color=RED, zorder=5)
a.set_xlim(-4, 4); a.set_ylim(-1, 8.2); a.set_xlabel(r'$\theta$', labelpad=1); a.set_ylabel(r'$A(\theta)$')
b.plot(t, m, color=BLUE, lw=1.4); b.plot(t, v, color=YELLOW, lw=1.5)
b.axhline(2, color=STROKE, lw=0.6, ls=':')
b.scatter([t0, t0], [m0, v0], s=16, color=RED, zorder=5)
b.text(1.6, 0.25, '方差', color=YELLOW, fontsize=7.5); b.text(2.4, 1.72, '均值', color=BLUE, fontsize=7.5)
b.set_xlim(-4, 4); b.set_ylim(0, 2.15); b.set_xlabel(r'$\theta$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
mm, vv = mom(np.array([t0]))
save(fig, HERE, 'figure', {'A_ln2': A0, 'mean_ln2_numeric': float(mm[0]), 'var_ln2_numeric': float(vv[0]), 'max_var': float(v.max()), 'theta_at_max_var': float(t[v.argmax()])})
