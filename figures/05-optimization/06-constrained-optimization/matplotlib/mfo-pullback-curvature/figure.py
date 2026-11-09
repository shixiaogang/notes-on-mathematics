from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Circle example phi(theta)=(cos^2+4 sin^2)/2, three retractions, remainder of first-order expansion.
phi=lambda t:.5*(np.cos(t)**2+4*np.sin(t)**2)
dphi=lambda t:1.5*np.sin(2*t)
fig, axs = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
s=np.linspace(-.6,.6,300)
for ax,t0,lab in zip(axs,(np.pi/6,0.),'ab'):
    curves=[(t0+s,PURPLE,'-','指数映射'),(t0+np.arctan(s),GREEN,'-','归一化'),(t0+s+.5*s*s,YELLOW,'--','一阶回缩')]
    for th,c,ls,nm in curves:
        ax.plot(s,phi(th)-phi(t0)-dphi(t0)*s,color=c,ls=ls,lw=1.5,label=nm)
    ax.set_xlabel(r'$s$'+f'\n({lab})')
axs[0].set_ylabel(r'$\hat f(s)-f(\theta)-f^{\prime}(\theta)s$'); axs[0].legend(loc='upper center',handlelength=1.8)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'phi(t)=(cos^2 t+4 sin^2 t)/2; retractions t+s, t+arctan s, t+s+s^2/2; base t=pi/6 and t=0'})
