"""Running example of the nonlinear interior-point chapter.
min f(x)=((x1-3)^2+x2^2)/2  s.t. g1=x1^2-x2<=0, g2=x2-4<=0;  x*=(1,1), lambda*=(1,0), f*=5/2."""
from pathlib import Path
import sys
_ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(_ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
EDGE = '#4C4D4F'
def tag(ax, xl, t):
    ax.set_xlabel((xl + '\n' if xl else '') + t, labelpad=1, linespacing=1.5)
def region(ax, fill=True, x2top=4.):
    """feasible set x1^2<=x2<=4"""
    u = np.linspace(-2, 2, 300)
    if fill: ax.fill_between(u, u**2, x2top, color=BLUE_FILL, lw=0, zorder=0)
    ax.plot(u, u**2, color=EDGE, lw=1.7, zorder=2); ax.plot([-2, 2], [4, 4], color=EDGE, lw=1.7, zorder=2)
def f_contours(ax, lim, levels):
    a, b = np.meshgrid(np.linspace(lim[0], lim[1], 300), np.linspace(lim[2], lim[3], 300))
    ax.contour(a, b, .5*((a-3)**2+b**2), levels=levels, colors=BLUE, linewidths=.7, zorder=1)
def f(x): return .5*((x[0]-3)**2+x[1]**2)
def df(x): return np.array([x[0]-3., x[1]])
def g(x): return np.array([x[0]**2-x[1], x[1]-4.])
def J(x): return np.array([[2*x[0],-1.],[0.,1.]])
def W(x,l): return np.diag([1+2*l[0],1.])
XSTAR=np.array([1.,1.]); LSTAR=np.array([1.,0.]); FSTAR=2.5

def barrier_val(x,mu):
    gg=g(x)
    if np.any(gg>=0): return np.inf
    return f(x)-mu*np.log(-gg).sum()
def barrier_grad_hess(x,mu):
    gg=g(x); JJ=J(x)
    gr=df(x)+mu*JJ.T@(1/(-gg))
    H=np.eye(2)+mu*(np.diag([2/(-gg[0]),0.])+JJ.T@np.diag(1/gg**2)@JJ)
    return gr,H
def center(mu,x0=None,tol=1e-12):
    """damped Newton on the barrier problem"""
    x=np.array([.5,1.5]) if x0 is None else np.array(x0,float)
    n=0
    for _ in range(500):
        gr,H=barrier_grad_hess(x,mu); d=-np.linalg.solve(H,gr); dec=-gr@d
        if dec/2<tol: break
        a=1.
        while a>1e-14 and barrier_val(x+a*d,mu)>barrier_val(x,mu)-.25*a*dec: a*=.5
        x=x+a*d; n+=1
    return x,n
def central_path(mus):
    out=[];x=np.array([0.,2.])
    for m in sorted(mus,reverse=True):
        x,_=center(m,x); out.append((m,x.copy()))
    return out[::-1] if False else out

def residuals(x,s,l,mu_target):
    return df(x)+J(x).T@l, g(x)+s, mu_target*np.ones(2)-s*l
def direction(x,s,l,mu_t):
    rd,rp,rc=residuals(x,s,l,mu_t); JJ=J(x); D=l/s
    H=W(x,l)+JJ.T@np.diag(D)@JJ
    rhs=-rd-JJ.T@((rc+l*rp)/s)
    dx=np.linalg.solve(H,rhs)
    ds=-rp-JJ@dx
    dl=(rc-l*ds)/s
    return dict(rd=rd,rp=rp,rc=rc,H=H,rhs=rhs,dx=dx,ds=ds,dl=dl)
def Fnorm(x,s,l,mu_t):
    rd,rp,rc=residuals(x,s,l,mu_t); return np.sqrt((rd@rd)+(rp@rp)+(rc@rc))
def pd_ipm(x0,s0,l0,sigma=.2,eta=.9,tol=1e-6,maxit=60,merit=True,c=1e-4):
    x,s,l=[np.array(v,float) for v in (x0,s0,l0)]
    hist=[]
    for t in range(maxit):
        mu=s@l/2
        rd,rp,_=residuals(x,s,l,0)
        rec=dict(t=t,x=x.copy(),s=s.copy(),l=l.copy(),mu=mu,rd=rd.copy(),rp=rp.copy(),prod=s*l)
        if max(np.abs(rd).max(),np.abs(rp).max(),(s*l).max())<=tol:
            hist.append(rec);break
        mt=sigma*mu
        d=direction(x,s,l,mt)
        amax=np.inf
        for v,dv in ((s,d['ds']),(l,d['dl'])):
            neg=dv<0
            if neg.any(): amax=min(amax,(v[neg]/-dv[neg]).min())
        a=min(1.,eta*amax); a0=a
        if merit:
            F0=Fnorm(x,s,l,mt)
            while a>1e-14 and Fnorm(x+a*d['dx'],s+a*d['ds'],l+a*d['dl'],mt)>(1-c*a)*F0: a*=.5
        rec.update(d=d,amax=amax,a0=a0,a=a,mt=mt)
        hist.append(rec)
        x=x+a*d['dx'];s=s+a*d['ds'];l=l+a*d['dl']
    return hist
def barrier_method(x0,mu0,tau,tol=1e-6,inner=1e-5,m=2):
    x=np.array(x0,float);mu=mu0;path=[x.copy()];counts=[];mus=[]
    while True:
        k=0
        for _ in range(200):
            gr,H=barrier_grad_hess(x,mu); d=-np.linalg.solve(H,gr); dec=-gr@d
            if dec/2<=inner: break
            a=1.
            while a>1e-14 and barrier_val(x+a*d,mu)>barrier_val(x,mu)-.25*a*dec: a*=.5
            x=x+a*d;k+=1;path.append(x.copy())
        counts.append(k);mus.append(mu)
        if m*mu<=tol: break
        mu*=tau
    return dict(path=np.array(path),counts=counts,mus=mus)
