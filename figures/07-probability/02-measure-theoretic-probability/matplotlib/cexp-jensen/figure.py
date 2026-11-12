"""Conditional Jensen with phi(y)=y^2 on the sensor table.
(a) group X=1: points (y, y^2), y=0,1,2 with conditional probabilities 1/4,1/2,1/4 (blue, size ~ prob);
support line l(y)=1+2(y-1) at m=E[Y|X=1]=1 (purple dashed); phi(m)=1 (red), E[Y^2|X=1]=3/2 (green).
(b) for x=0,1,2: (E[Y|X=x])^2 = 1/9, 1, 25/9 (red) and E[Y^2|X=x] = 1/3, 3/2, 3 (green); gaps 2/9, 1/2, 2/9."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2)
y = np.linspace(-0.3, 2.3, 300)
a.plot(y, y**2, color=BLUE, lw=1.4)
a.plot(y, 1 + 2*(y - 1), color=PURPLE, lw=1.1, ls='--')
c = P[1]/P[1].sum()
a.scatter(np.arange(3), np.arange(3)**2, s=90*c/0.5, facecolor='white', edgecolor=BLUE, lw=1.1, zorder=4)
a.plot([1, 1], [1, 1.5], color=STROKE, lw=0.7, ls=':')
a.scatter([1], [1], s=18, color=RED, zorder=5)
a.scatter([1], [1.5], s=18, color=GREEN, zorder=5)
a.text(1.08, 1.55, r'$3/2$', fontsize=7.5, color=GREEN)
a.text(1.2, 0.45, r'$\varphi(1)=1$', fontsize=7.5, color=RED)
a.text(2.25, 4.1, r'$\varphi$', color=BLUE, ha='right')
a.set_xlim(-0.3, 2.3); a.set_ylim(-0.6, 4.6); a.set_xticks([0, 1, 2]); a.set_xlabel('$y$', labelpad=1)
x = np.arange(3)
m = np.array([1/3, 1, 5/3]); s2 = np.array([1/3, 1.5, 3])
b.bar(x - 0.17, m**2, width=0.32, color=RED_FILL, edgecolor=RED, lw=0.8)
b.bar(x + 0.17, s2, width=0.32, color=GREEN_FILL, edgecolor=GREEN, lw=0.8)
for i in range(3):
    b.text(x[i] - 0.17, m[i]**2 + 0.08, ['1/9', '1', '25/9'][i], ha='center', fontsize=7, color=MUTED)
    b.text(x[i] + 0.17, s2[i] + 0.08, ['1/3', '3/2', '3'][i], ha='center', fontsize=7, color=MUTED)
b.set_xticks(x); b.set_xticklabels(['$x=0$', '$x=1$', '$x=2$']); b.set_ylim(0, 3.4)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'m_sq': list(m**2), 'second_moment': list(s2), 'cond_var': list(s2 - m**2)})
