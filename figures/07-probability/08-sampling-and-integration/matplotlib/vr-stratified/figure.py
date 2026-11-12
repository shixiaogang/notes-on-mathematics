from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# I = int_0^1 e^u du, four equal strata [k/4,(k+1)/4).  (a) two points per stratum, u = (k + v)/4 with
# v = 0.37, 0.81 | 0.06, 0.52 | 0.23, 0.68 | 0.45, 0.91; stratum means mu_k as short segments.
# (b) allocation of n = 8 evaluations: proportional n_k = 2 versus Neyman n_k = 8 p_k s_k / sum p_j s_j.
V = [.37, .81, .06, .52, .23, .68, .45, .91]
mu = []; sd = []
for k in range(4):
    a0 = k/4; h = .25
    m = (math.exp(a0+h)-math.exp(a0))/h; m2 = (math.exp(2*(a0+h))-math.exp(2*a0))/(2*h)
    mu.append(m); sd.append(math.sqrt(m2-m*m))
ney = [8*s/sum(sd) for s in sd]
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.26)
a, b = axs
u = np.linspace(0, 1, 300)
a.plot(u, np.exp(u), color=BLUE, lw=1.4)
for k in range(1, 4):
    a.axvline(k/4, color=STROKE, lw=.85, ls=DASH)
pts = []
for k in range(4):
    a.plot([k/4+.02, (k+1)/4-.02], [mu[k], mu[k]], color=BLUE, lw=.9)
    for v in V[2*k:2*k+2]:
        x = (k+v)/4; pts.append(x); dot(a, x, math.exp(x), color=GREEN, ms=3.6)
a.set_xlim(0, 1); a.set_ylim(.9, 2.8); a.set_xticks([0, .25, .5, .75, 1]); a.set_xticklabels(['0', '1/4', '1/2', '3/4', '1'])
a.set_yticks([1, 1.5, 2, 2.5]); axlab(a, '$u$')
k = np.arange(4)
b.bar(k-.18, [2]*4, width=.34, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
b.bar(k+.18, ney, width=.34, color=YELLOW_FILL, edgecolor=YELLOW, lw=.8)
b.set_xticks(k); b.set_xticklabels(['$A_1$', '$A_2$', '$A_3$', '$A_4$'])
b.set_ylim(0, 3.2); b.set_yticks([0, 1, 2, 3]); b.set_ylabel(r'$n_k$', labelpad=1)
lab(b, -.45, 2.9, '比例分配', BLUE); lab(b, 1.6, 2.9, 'Neyman分配', YELLOW)
tags(fig, axs)
s2 = (E*E-1)/2-(E-1)**2
save(fig, HERE, 'figure', {'points': pts, 'values': [math.exp(x) for x in pts], 'estimate': float(np.mean([math.exp(x) for x in pts])),
     'mu': mu, 'sd': sd, 'neyman': ney, 'var_prop_n8': sum(.25*s*s for s in sd)/8,
     'var_neyman_n8': sum(.25*s for s in sd)**2/8, 'var_int_1223': sum(.0625*s*s/nk for s, nk in zip(sd, [1, 2, 2, 3])),
     'var_plain_n8': s2/8})
