"""Overcomplete Bernoulli T=(1{x=0},1{x=1}): distribution depends on theta1-theta0 only. (a) lines of constant p; red (0,ln2),(1,1+ln2) give p=2/3.
(b) along theta=(0,ln2)+c(1,1): A=ln 3 + c (linear), p constant 2/3."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

import math
fig, (a, b) = figure(width_mm=100, height_mm=48, ncols=2)
for p in (0.2, 0.5, 2/3, 0.8):
    d = math.log(p/(1-p))
    s = np.linspace(-2.2, 2.6, 10)
    a.plot(s, s+d, color=STROKE, lw=0.9)
    lab = '$2/3$' if abs(p-2/3) < 1e-9 else f'${p:g}$'
    a.text(2.68, 2.6+d, lab, fontsize=7.5, color=MUTED, ha='left', va='center')
r = np.array([[0, math.log(2)], [1, 1+math.log(2)]])
a.scatter(r[:, 0], r[:, 1], s=16, color=RED, zorder=5)
a.set_xlim(-2, 3.3); a.set_ylim(-2, 4.1); a.set_xticks([-2, 0, 2]); a.set_aspect('equal')
a.set_xlabel(r'$\theta_0$', labelpad=1); a.set_ylabel(r'$\theta_1$', labelpad=1)
c = np.linspace(-2, 2, 100)
b.plot(c, math.log(3)+c, color=BLUE, lw=1.4)
b.plot(c, np.full_like(c, 2/3), color=YELLOW, lw=1.5)
b.text(1.2, 2.55, '$A$', color=BLUE, fontsize=8); b.text(1.2, 0.85, '$p$', color=YELLOW, fontsize=8)
b.set_xlim(-2, 2); b.set_ylim(-1.2, 3.3); b.set_xlabel('$c$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
A = lambda th: math.log(math.exp(th[0])+math.exp(th[1]))
save(fig, HERE, 'figure', {'A_at_red': [A(r[0]), A(r[1])], 'p_at_red': [math.exp(r[0][1])/(math.exp(r[0][0])+math.exp(r[0][1])), math.exp(r[1][1])/(math.exp(r[1][0])+math.exp(r[1][1]))]})
