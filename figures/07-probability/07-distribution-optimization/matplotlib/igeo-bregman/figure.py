"""Tilted family p_theta(x) ∝ e^{theta x} on {0,1,2}. (a) A(theta)=ln(1+e^theta+e^{2theta}), tangent at theta=ln2 (slope 10/7),
gap at theta'=0 equals D(P_ln2||P_0)=ln3-ln7+(10/7)ln2; purple dashed: tangent + (1/2)G(theta'-theta)^2, G=26/49.
(b) dual A*(m)=sum p ln p on (0,2); tangent at m'=1 (theta=0, slope 0); gap at m=10/7 equals the same KL."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

import math
def A(t): return np.log(1+np.exp(t)+np.exp(2*t))
def probs(t):
    w = np.exp(np.outer(np.atleast_1d(t), np.arange(3))); return w/w.sum(1, keepdims=True)
fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2)
t = np.linspace(-0.7, 1.3, 400); t0 = math.log(2); m0 = 10/7; G0 = 26/49
a.plot(t, A(t), color=BLUE, lw=1.4)
a.plot(t, A(t0)+m0*(t-t0), color=STROKE, lw=0.85, ls='--')
a.plot(t, A(t0)+m0*(t-t0)+0.5*G0*(t-t0)**2, color=PURPLE, lw=1.0, ls=(0, (2, 1.5)))
gap = float(A(0)-A(t0)-m0*(0-t0))
a.plot([0, 0], [A(t0)+m0*(0-t0), A(0)], color=RED, lw=2.0)
a.scatter([t0], [A(t0)], s=14, color=RED, zorder=5)
a.set_xlim(-0.7, 1.3); a.set_ylim(0.3, 2.9); a.set_xlabel(r'$\theta$', labelpad=1); a.set_ylabel(r'$A(\theta)$', labelpad=1)
a.text(t0+0.08, A(t0)-0.08, r'$\ln 2$', va='top', fontsize=7.5)
# dual
tt = np.linspace(-9, 9, 3000); P = probs(tt); m = P@np.arange(3); Astar = (P*np.log(P)).sum(1)
b.plot(m, Astar, color=BLUE, lw=1.4)
Am1 = -math.log(3)
b.plot([0.5, 1.9], [Am1, Am1], color=STROKE, lw=0.85, ls='--')
p0 = probs(t0)[0]; As0 = float((p0*np.log(p0)).sum())
b.plot([m0, m0], [Am1, As0], color=RED, lw=2.0)
b.scatter([1], [Am1], s=14, color=RED, zorder=5)
b.set_xlim(0.5, 1.9); b.set_ylim(-1.13, -0.83); b.set_xlabel(r'$m$', labelpad=1); b.set_ylabel(r'$A^{*}(m)$', labelpad=1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30)
save(fig, HERE, 'figure', {'gap_a': gap, 'gap_b': As0-Am1, 'quad_pred': 0.5*G0*t0**2})
