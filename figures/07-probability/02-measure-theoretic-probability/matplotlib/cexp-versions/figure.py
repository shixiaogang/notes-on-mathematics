"""Versions of E[X^+ | Y], Y=|X|, X~Unif(-1,1).
m(y)=y/2 (green). Another version mt: equal to y/2 on [0,1] except mt(1/2)=0.9, and mt(y)=1-y/2 for y>1, mt(y)=0.4 for y<0
(regions where P_Y has no mass). (a) as functions of y with P_Y density 1 on [0,1] (light blue band);
(b) composed with Y(w)=|w| on Omega=(-1,1): mt(Y) differs from m(Y) only at w=+-1/2."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
a.axvspan(0, 1, color=BLUE_FILL, lw=0)
y = np.linspace(-0.45, 1.45, 400)
a.plot(y, y/2, color=GREEN, lw=1.4)
yl = y[y < 0]; yr = y[y > 1]
a.plot(yl, np.full_like(yl, 0.4), color=YELLOW, lw=1.6)
a.plot(yr, 1 - yr/2, color=YELLOW, lw=1.6)
a.scatter([0.5], [0.25], s=16, facecolor='white', edgecolor=YELLOW, zorder=4, lw=1.0)
a.scatter([0.5], [0.9], s=16, color=RED, zorder=4)
a.text(0.5, 0.97, r'$\tilde m(1/2)$', ha='center', fontsize=7.5, color=RED)
a.text(1.43, 0.62, '$m$', ha='right', color=GREEN)
a.text(1.43, 0.18, r'$\tilde m$', ha='right', color=YELLOW)
a.text(0.5, 0.04, r'$P_Y$', ha='center', fontsize=7.5, color=BLUE)
a.set_xlim(-0.45, 1.45); a.set_ylim(-0.05, 1.08); a.set_xlabel('$y$', labelpad=1)
w = np.linspace(-1, 1, 401)
b.plot(w, np.abs(w)/2, color=GREEN, lw=1.4)
b.scatter([-0.5, 0.5], [0.25, 0.25], s=16, facecolor='white', edgecolor=GREEN, zorder=4, lw=1.0)
b.scatter([-0.5, 0.5], [0.9, 0.9], s=16, color=RED, zorder=4)
b.set_xlim(-1, 1); b.set_ylim(-0.05, 1.08); b.set_xticks([-1, -0.5, 0, 0.5, 1]); b.set_xticklabels(['-1', '-1/2', '0', '1/2', '1'])
b.set_xlabel(r'$\omega$', labelpad=1)
b.text(0.97, 0.56, r'$m(Y)$', ha='right', color=GREEN)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'m': 'y/2', 'changed_point': 0.5, 'changed_value': 0.9})
