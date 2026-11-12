"""Certificate for the minimum-KL problem, P uniform on {0,1,2}, T(x)=x, m=10/7, along Newton iterates from theta=0.
Lower bound l(theta)=theta m - A(theta) (purple); upper bound u = D(Qtilde||P) for the repaired feasible
Qtilde=(1-alpha)Q_theta+alpha delta_2, alpha=(m-mean)/(2-mean) (green); exact D*=0.142912 (blue).
(a) bounds for t=0,1,2,3; (b) gap u-l on log scale."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

m = 10/7
Dst = m*math.log(2)-math.log(7/3)
th = 0.0; rows = []
for t in range(5):
    q = tilt(U3, X3, th); mu = q@X3; v = q@(X3**2)-mu**2
    A = math.log(np.sum(U3*np.exp(th*X3)))
    low = th*m-A
    al = (m-mu)/(2-mu); qt = (1-al)*q; qt[2] += al
    up = kl(qt, U3)
    rows.append((t, th, float(mu), low, float(al), up, up-low))
    th = th-(mu-m)/v
R = np.array(rows)
fig, (a, b) = figure(width_mm=112, height_mm=46, ncols=2)
k = R[:4, 0]
a.plot(k, R[:4, 3], color=PURPLE, lw=1.2, marker='o', ms=2.6)
a.plot(k, R[:4, 5], color=GREEN, lw=1.3, marker='o', ms=2.6)
a.axhline(Dst, color=BLUE, lw=1.0, ls='--')
a.text(3.0, 0.03, r'$\ell(\theta^{(t)})$', color=PURPLE, ha='right', fontsize=7.5)
a.text(0.25, 0.165, r'$u^{(t)}$', color=GREEN, ha='left', fontsize=7.5)
a.text(3.0, Dst+0.006, r'$D^{*}$', color=BLUE, ha='right', va='bottom', fontsize=7.5)
a.set_xticks([0, 1, 2, 3]); a.set_xlim(-0.2, 3.2); a.set_ylim(-0.01, 0.19)
a.set_xlabel(r'$t$', labelpad=1)
g = R[:4, 6]
b.semilogy(k, g, color=GREEN, lw=1.3, marker='o', ms=2.6)
b.set_xticks([0, 1, 2, 3]); b.set_xlim(-0.2, 3.2)
b.set_xlabel(r'$t$', labelpad=1); b.set_ylabel(r'$u^{(t)}-\ell(\theta^{(t)})$', labelpad=1)
tag(a, '(a)', y=-0.29); tag(b, '(b)', y=-0.29)
save(fig, HERE, 'figure', {'D_star': Dst, 'rows_t_theta_mean_low_alpha_up_gap': R.tolist()})
