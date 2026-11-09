from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# Outer GD eta=1 from x=1 on the running example; inner GD alpha=.5 from y0=0, K steps; hypergradient -y*(y-1)/(1+x) at yhat.
fig, ax = figure(width_mm=100, height_mm=56)
def run(Kf,N=70):
    x=1.; E=[abs(x-2)]
    for t in range(N):
        K=Kf(t)
        if K is None: y=ystar(x)
        else: y=yT(x,K)
        x=x+y*(y-1)/(1+x); E.append(abs(x-2))
    return np.array(E)
ax.semilogy(run(lambda t:2),color=YELLOW,lw=1.6)
ax.semilogy(run(lambda t:4),color=PURPLE,lw=1.3)
ax.semilogy(run(lambda t:t+2),color=GREEN,lw=1.4)
ax.semilogy(run(lambda t:None),color=BLUE,lw=1.1,ls='--')
ax.text(45,.42,'$K=2$',color=YELLOW,fontsize=7.5); ax.text(45,.15,'$K=4$',color=PURPLE,fontsize=7.5)
ax.text(26,1.5e-3,'$K_t=t+2$',color=GREEN,fontsize=7.5); ax.text(49,1e-5*40,'',color=BLUE)
clean(ax,(0,70),(5e-5,2),'外层轮数 t',r'$|x^{(t)}-2|$')
save(fig, Path(__file__).resolve().parent, 'figure', {'eta':1,'x0':1})
for f in (lambda t:2, lambda t:4, lambda t:t+2, lambda t:None): print(run(f)[[0,5,20,70]])
