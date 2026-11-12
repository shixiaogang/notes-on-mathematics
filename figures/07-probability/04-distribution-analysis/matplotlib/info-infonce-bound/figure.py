from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# InfoNCE bound ln N - L with the optimal score (log density ratio), against the number N of candidates.
# (a) binary example: X ~ Bern(1/2), Y = X xor Bern(1/4); ratio 3/2 on matches, 1/2 otherwise.
#     Exact sum over the number of matching candidates. I(X;Y) = 0.1308 nat (purple dashed).
# (b) standard bivariate normal, rho = 0.99, I = 1.9585 nat; Monte Carlo, seed 0, 40000 draws per N.
#     ln N (grey dashed) caps the bound.
def nce_binary(N, e=.25):
    a, b = 2*(1-e), 2*e; Hs = 0.0
    for mJ, pJ in ((1, 1-e), (0, e)):
        for k in range(N):
            pk = math.comb(N-1, k)*.5**(N-1); m = k+mJ; Z = m*a+(N-m)*b; ent = 0.0
            if m: ent -= m*(a/Z)*math.log(a/Z)
            if N-m: ent -= (N-m)*(b/Z)*math.log(b/Z)
            Hs += pJ*pk*ent
    return math.log(N) - Hs
rng = np.random.default_rng(0); rho = .99; Ig = -.5*math.log(1-rho*rho)
def nce_gauss(N, reps=40000, chunk=4000):
    out = []
    for _ in range(reps//chunk):
        out.append(_chunk(N, chunk))
    v = np.concatenate(out); SE[int(N)] = float(v.std()/math.sqrt(len(v)))
    return math.log(N) - float(v.mean())
SE = {}
def _chunk(N, reps):
    x = rng.standard_normal(reps); yt = rho*x + math.sqrt(1-rho*rho)*rng.standard_normal(reps)
    ys = rng.standard_normal((reps, N)); ys[:, 0] = yt   # hidden position placed in column 0 (exchangeable)
    lr = -(rho*rho*x[:, None]**2 - 2*rho*x[:, None]*ys + rho*rho*ys**2)/(2*(1-rho*rho))
    m = lr.max(1, keepdims=True); lse = m[:, 0] + np.log(np.exp(lr-m).sum(1))
    return lse - lr[:, 0]
Ns = 2**np.arange(1, 11)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, bottom=.28, top=.95, wspace=.3)
vb = [nce_binary(int(n)) for n in Ns]
a.plot(Ns, vb, '-o', color=GREEN, lw=1.1, ms=3, mew=0); a.axhline(LN2-float(hb(.25)), color=PURPLE, lw=.85, ls=DASH)
a.set_xscale('log', base=2); a.minorticks_off(); a.set_xticks([2, 8, 32, 128, 512]); a.set_xticklabels(['$2$', '$8$', '$32$', '$128$', '$512$'])
a.set_ylim(0, .15); axlab(a, '$N$', 'nat'); lab(a, 2, .137, r'$I(X;Y)=0.1308$', PURPLE)
vg = [nce_gauss(int(n)) for n in Ns]
b.plot(Ns, vg, '-o', color=GREEN, lw=1.1, ms=3, mew=0); b.axhline(Ig, color=PURPLE, lw=.85, ls=DASH)
b.plot(Ns, np.log(Ns), color=STROKE, lw=.85, ls=DASH)
b.set_xscale('log', base=2); b.minorticks_off(); b.set_xticks([2, 8, 32, 128, 512]); b.set_xticklabels(['$2$', '$8$', '$32$', '$128$', '$512$'])
b.set_ylim(0, 2.4); axlab(b, '$N$', 'nat'); lab(b, 40, 2.07, r'$I(X;Y)=1.959$', PURPLE); lab(b, 2.4, 1.5, r'$\ln N$', STROKE)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'binary': dict(zip(map(int, Ns), vb)), 'gauss': dict(zip(map(int, Ns), vg)), 'I_gauss': Ig, 'gauss_se': SE})
