from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Least squares N=80, n=40, column scales 10^U(-1,1); coordinate gradient steps with three selection rules.
rng = np.random.default_rng(5); N, n = 80, 40
A = rng.standard_normal((N, n))*(10**rng.uniform(-1, 1, n)); b0 = rng.standard_normal(N)
L = (A**2).sum(0); xs = np.linalg.lstsq(A, b0, rcond=None)[0]; fs = .5*((A@xs-b0)**2).sum(); T = 1600
def run(rule, seed=0):
    r = np.random.default_rng(seed); x = np.zeros(n); res = A@x-b0; G = [.5*res@res-fs]
    for t in range(T):
        g = A.T@res
        i = r.integers(n) if rule == 'r' else (np.argmax(abs(g)) if rule == 'gs' else np.argmax(g*g/L))
        d = -g[i]/L[i]; x[i] += d; res += A[:, i]*d; G.append(.5*res@res-fs)
    return np.array(G)
gs, gl = run('gs'), run('gl'); gr = np.exp(np.mean([np.log(np.maximum(run('r', s), 1e-300)) for s in range(10)], 0))
fig, (a, b2) = figure(width_mm=112, height_mm=58, ncols=2, gridspec_kw={'width_ratios': [1.7, 1]})
panel(fig, .125, .985, .97, .25, wspace=.3)
a.semilogy(gr/gr[0], color=YELLOW, lw=1.6); a.semilogy(gs/gr[0], color=PURPLE, lw=1.4); a.semilogy(gl/gr[0], color=GREEN, lw=1.4)
a.text(1150, 3e-6, '随机', fontsize=7.5, color=INK); a.text(800, 8e-3, r'$|\partial_j f|$', fontsize=7.5, color=INK); a.text(170, 1e-9, r'$(\partial_j f)^2/L_j$', fontsize=7.5, color=INK)
a.set_xlabel('单坐标更新次数', labelpad=1); a.set_ylabel('相对目标差', labelpad=1); a.set_xlim(0, T)
x = np.arange(2); b2.bar(x-.18, [3, 5], width=.32, color=PURPLE); b2.bar(x+.18, [4.5, .5], width=.32, color=GREEN)
b2.set_xticks(x); b2.set_xticklabels(['$x_1$', '$x_2$']); b2.set_ylim(0, 6.2)
b2.text(1-.18, 5.15, '5', fontsize=7.5, color=INK, ha='center'); b2.text(-.18, 3.15, '3', fontsize=7.5, color=INK, ha='center'); b2.text(.18, 4.65, '4.5', fontsize=7.5, color=INK, ha='center'); b2.text(1.18, .65, '0.5', fontsize=7.5, color=INK, ha='center')
tag(fig, a, '(a)'); tag(fig, b2, '(b)')
save(fig, HERE, 'figure', {'N': N, 'n': n, 'seed': 5, 'final': [float(gr[-1]), float(gs[-1]), float(gl[-1])]})
print(gr[[400,1600]]/gr[0], gs[[400,1600]]/gr[0], gl[[400,1600]]/gr[0])
