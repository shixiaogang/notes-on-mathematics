from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Target pi = 0.7 N(-2,0.6^2)+0.3 N(2,0.6^2) (blue); Gaussian candidates N(m,s^2).
# D(Pi||Q) is minimised by moment matching: m=-0.8, s^2=3.72 (purple).
# D(Q||Pi) has two local minima, near N(-2,0.6^2) (value 0.356) and N(2,0.6^2) (value 1.202) (yellow).
# (b) profiles over m: min_s D(Q_{m,s}||Pi) (yellow, grid over s) and min_s D(Pi||Q_{m,s}) (purple, closed form in s).
x = np.linspace(-12, 12, 12001); dx = x[1]-x[0]
pi = mix_pdf(x)
mean = float(np.sum(x*pi)*dx); var = float(np.sum((x-mean)**2*pi)*dx)
hpi = float(-np.sum(pi*np.log(pi))*dx)
def rev(m, s):
    q = npdf(x, m, s); return float(np.sum(q*(np.log(q+1e-300)-np.log(pi)))*dx)
M = np.linspace(-4, 4, 161); S = np.linspace(.3, 3, 109)
prof = np.array([min(rev(m, s) for s in S) for m in M])
fprof = -hpi+0.5*np.log(2*np.pi*np.e*(var+(M-mean)**2))
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.28)
ax = axs[0]
xx = np.linspace(-5, 5, 1001)
ax.plot(xx, mix_pdf(xx), color=BLUE, lw=1.4)
ax.plot(xx, npdf(xx, mean, math.sqrt(var)), color=PURPLE, lw=1.4)
ax.plot(xx, npdf(xx, -2, .6), color=YELLOW, lw=1.6)
ax.plot(xx, npdf(xx, 2, .6), color=YELLOW, lw=1.6, ls=DASH)
lab(ax, -4.9, .5, r'$\pi$', BLUE); lab(ax, 2.6, .5, '局部', YELLOW, fontsize=7)
lab(ax, -4.9, .26, '矩匹配', PURPLE, fontsize=7)
ax.annotate('', xy=(-2.75, .39), xytext=(-4.55, .49), arrowprops=dict(arrowstyle='->', color=BLUE, lw=.85))
ax.set_xlim(-5, 5); ax.set_ylim(0, .72); axlab(ax, '$x$', None)
ax = axs[1]
ax.plot(M, prof, color=YELLOW, lw=1.6); ax.plot(M, fprof, color=PURPLE, lw=1.4)
i1 = np.argmin(np.where(M < 0, prof, 9)); i2 = np.argmin(np.where(M > 0, prof, 9))
dot(ax, M[i1], prof[i1], RED, ms=4); dot(ax, M[i2], prof[i2], RED, ms=4); dot(ax, mean, fprof[np.argmin(fprof)], RED, ms=4)
lab(ax, -3.9, 2.5, r'$D_{\mathrm{KL}}(Q\Vert\Pi)$', YELLOW, fontsize=7)
lab(ax, .4, .3, r'$D_{\mathrm{KL}}(\Pi\Vert Q)$', PURPLE, fontsize=7)
ax.set_xlim(-4, 4); ax.set_ylim(0, 3); axlab(ax, '$m$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'mean': mean, 'var': var, 'fwd_min': float(fprof.min()), 'rev_local': [[float(M[i1]), float(prof[i1])], [float(M[i2]), float(prof[i2])]]})
