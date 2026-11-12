"""Copula samples (top) and the same samples with Exp(1) marginals (bottom): product, Gaussian rho=0.7, comonotone M. 600 pts, seed 716.
Exact P(X1<=1,X2<=1)=C(F(1),F(1)), F(1)=1-e^{-1}."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 600
rho = 0.7
U_pi = rng.random((n, 2))
G1 = rng.standard_normal(n); G2 = rho*G1+np.sqrt(1-rho*rho)*rng.standard_normal(n)
U_g = np.column_stack([Phi(G1), Phi(G2)])
u = rng.random(n); U_m = np.column_stack([u, u])
F1 = 1-np.exp(-1)
z = float(Phi_inv(F1)[0])
probs = [F1*F1, binorm_cdf(z, z, rho), F1]
fig, axs = figure(width_mm=112, height_mm=76, nrows=2, ncols=3)
names = [r'$\Pi$', r'$C_{0.7}$', r'$M$']
for j, U in enumerate([U_pi, U_g, U_m]):
    top, bot = axs[0, j], axs[1, j]
    top.scatter(U[:, 0], U[:, 1], s=1.2, color=GREEN, linewidths=0)
    top.set_xlim(0, 1); top.set_ylim(0, 1); top.set_xticks([0, 0.5, 1]); top.set_yticks([0, 0.5, 1])
    top.set_xlabel('$u_1$', labelpad=0)
    top.text(0.5, 1.04, names[j], transform=top.transAxes, va='bottom', ha='center', fontsize=8)
    X = -np.log(1-U)
    bot.scatter(X[:, 0], X[:, 1], s=1.2, color=GREEN, linewidths=0)
    bot.plot([0, 1, 1], [1, 1, 0], color=RED, lw=1.0, ls='--')
    bot.set_xlim(0, 4.5); bot.set_ylim(0, 4.5); bot.set_xticks([0, 2, 4]); bot.set_yticks([0, 2, 4])
    bot.set_xlabel('$x_1$', labelpad=0)
    bot.text(0.5, 1.04, f'{probs[j]:.3f}', transform=bot.transAxes, color=RED, fontsize=7.5, ha='center', va='bottom')
    for ax_ in (top, bot):
        ax_.set_box_aspect(1)
axs[0, 0].set_ylabel('$u_2$', labelpad=0); axs[1, 0].set_ylabel('$x_2$', labelpad=0)
emp = [float(np.mean((-np.log(1-U)).max(axis=1) <= 1)) for U in (U_pi, U_g, U_m)]
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'rho': rho, 'F1': F1, 'z': z, 'exact_probs': probs, 'empirical_probs': emp})
