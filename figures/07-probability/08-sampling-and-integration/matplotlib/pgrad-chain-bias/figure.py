from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# Target N(theta,1), f = x^2, J'(theta) = 2 theta, theta = 1.  Chain X^(t+1) = rho X^(t) + (1-rho) theta + sqrt(1-rho^2) eps_t,
# rho = 0.8, X^(0) = 0, so X^(K) ~ N(m_K, v_K), m_K = theta (1 - rho^K), v_K = 1 - rho^{2K}.
# Blue: target 2.  Yellow: derivative of the K-step program J_K(theta) = m_K^2 + v_K, i.e. 2 theta (1-rho^K)^2.
# Green solid: mean of the target reparameterization formula 2X applied to X^(K): 2 m_K.
# Green dashed: mean of the target score formula X^2 (X - theta) applied to X^(K): m^3 + 3 m v - theta (m^2 + v).
rho, th = .8, 1.0
K = np.arange(0, 26)
m = th*(1-rho**K); v = 1-rho**(2*K)
prog = 2*th*(1-rho**K)**2; rep = 2*m; sf = m**3+3*m*v-th*(m*m+v)
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.12, right=.97, bottom=.19, top=.96)
ax.axhline(2*th, color=BLUE, lw=1.4)
ax.plot(K, prog, color=YELLOW, lw=1.5)
ax.plot(K, rep, color=GREEN, lw=1.3)
ax.plot(K, sf, color=GREEN, lw=1.1, ls=DASH)
lab(ax, 3.3, 1.55, r'$2m_K$', GREEN); lab(ax, 7.2, .55, r'$\nabla J_K$', YELLOW); lab(ax, 1.2, -.42, '得分公式', GREEN)
ax.set_xlim(0, 25); ax.set_ylim(-.6, 2.3); ax.set_xticks([0, 5, 10, 15, 20, 25]); ax.set_yticks([0, 1, 2])
axlab(ax, r'$K$')
save(fig, HERE, 'figure', {'K': K.tolist(), 'program_derivative': prog.tolist(), 'reparam_formula_mean': rep.tolist(), 'score_formula_mean': sf.tolist()})
