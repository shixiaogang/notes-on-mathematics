from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# n=200 的随机正定模型：截断共轭梯度随 Hessian 向量乘积次数的模型下降，与 Cauchy、狗腿和精确解对照。
rng = np.random.default_rng(9); n = 200
Q, _ = np.linalg.qr(rng.normal(size=(n, n))); w = np.logspace(0, 2, n)
B = (Q*w) @ Q.T; g = Q @ (rng.normal(size=n)*np.sqrt(w)); D = 5.5
pn = -np.linalg.solve(B, g); pe = exact(g, B, D)[0]; pc = cauchy(g, B, D); k = g @ B @ g
pu = -(g @ g)/k*g
pdog = pn if np.linalg.norm(pn) <= D else (pc if np.linalg.norm(pu) >= D else pu + boundary(pu, pn - pu, D)*(pn - pu))
print(np.linalg.norm(pu), np.linalg.norm(pn))
# 不截断时记录 tCG 的路径
p = 0*g; r = g.copy(); d = -r; pr = [0.]; N = [0.]; hit = None
for j in range(1, 61):
    Bd = B @ d; a = r @ r/(d @ Bd); q = p + a*d
    if np.linalg.norm(q) >= D and hit is None: hit = j; p = p + boundary(p, d, D)*d; pr.append(-mdec(p, g, B)); N.append(D); break
    p = q; pr.append(-mdec(p, g, B)); N.append(np.linalg.norm(p)); rn = r + a*Bd; d = -rn + (rn @ rn)/(r @ r)*d; r = rn
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
ax = axs[0]; ax.plot(range(len(pr)), pr, color=GREEN, lw=1.4, marker='o', ms=2.6, mew=0)
J = len(pr) - 1
for v, c, s, ls in ((-mdec(pc, g, B), YELLOW, 'Cauchy', '-'), (-mdec(pdog, g, B), PURPLE, '狗腿', '-'), (-mdec(pe, g, B), RED, '精确', (0, (3, 2)))):
    ax.axhline(v, color=c, lw=1.1, ls=ls); print(s, v)
ax.set_xlim(0, J + .5); ax.set_ylim(0, -mdec(pe, g, B)*1.12); ax.set_xlabel('Hessian 向量乘积次数', labelpad=1); ax.set_ylabel('预测下降', labelpad=1)
ax.text(J+.3, -mdec(pc, g, B)*.95, 'Cauchy', ha='right', va='top', fontsize=7.5)
ax.text(J+.3, -mdec(pdog, g, B)*.975, '狗腿', ha='right', va='top', fontsize=7.5)
ax.text(.5, -mdec(pe, g, B)*1.02, '精确', ha='left', va='bottom', fontsize=7.5)
ax = axs[1]; ax.plot(range(len(N)), N, color=GREEN, lw=1.4, marker='o', ms=2.6, mew=0); ax.axhline(D, color=EDGE, lw=1.1)
ax.set_xlim(0, J + .5); ax.set_ylim(0, D*1.12); ax.set_xlabel('Hessian 向量乘积次数', labelpad=1); ax.set_ylabel(r'$\Vert p^{(j)}\Vert_2$', labelpad=1)
ax.text(.5, D*1.015, '$\\Delta$', va='bottom', fontsize=7.5)
print(J, pr)
panels(fig, .095, .985, .98, .27, .26); tags(fig, axs)
save(fig, HERE, 'figure', {'n': n, 'seed': 9, 'eigs': 'logspace(0,2)', 'radius': D, 'steps': J})
