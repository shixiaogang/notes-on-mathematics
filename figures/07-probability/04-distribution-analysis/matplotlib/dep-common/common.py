"""Shared numerics for chapter 7.19 (dependence measures) figures.

All values are computed from exact formulas or deterministic quadrature;
simulations fix their seeds.  Running examples:
  * three-point parabola: X uniform on {-1,0,1}, Y = X^2;
  * continuous parabola: X ~ Unif(-1,1), Y = X^2 (+ sigma*Z);
  * standard bivariate Gaussian with correlation rho.
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
SEED = 719


def phi(z):
    return np.exp(-np.asarray(z, float)**2/2)/math.sqrt(2*math.pi)


def _erf(z):
    """Vectorised erf (W. J. Cody style rational approximation via erfc continued in numpy; |err| < 1.2e-7)."""
    z = np.asarray(z, float)
    t = 1/(1+0.5*np.abs(z))
    y = 1-t*np.exp(-z*z-1.26551223+t*(1.00002368+t*(0.37409196+t*(0.09678418+t*(-0.18628806+t*(0.27886807+t*(-1.13520398+t*(1.48851587+t*(-0.82215223+t*0.17087277)))))))))
    return np.where(z >= 0, y, -y)


def Phi(z):
    return 0.5*(1+_erf(np.asarray(z, float)/math.sqrt(2)))


def Phi_inv(u):
    u = np.atleast_1d(np.asarray(u, float))
    lo = np.full_like(u, -12.0); hi = np.full_like(u, 12.0)
    for _ in range(80):
        mid = (lo+hi)/2
        m = Phi(mid) < u
        lo = np.where(m, mid, lo); hi = np.where(m, hi, mid)
    return (lo+hi)/2


# ---------- discrete (weighted point) versions of the population measures ----------
def double_center(A, w):
    """Double centering of a pairwise matrix A under point weights w."""
    r = A @ w
    g = w @ r
    return A - r[:, None] - r[None, :] + g


def dcov2_points(x, y, w):
    """Population dCov^2 of the discrete law putting mass w_i on (x_i, y_i); x, y arrays (n,) or (n,d)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    if x.ndim == 1: x = x[:, None]
    if y.ndim == 1: y = y[:, None]
    A = np.sqrt(((x[:, None, :]-x[None, :, :])**2).sum(-1))
    B = np.sqrt(((y[:, None, :]-y[None, :, :])**2).sum(-1))
    At = double_center(A, w); Bt = double_center(B, w)
    W = np.outer(w, w)
    return float((W*At*Bt).sum()), float((W*At*At).sum()), float((W*Bt*Bt).sum())


def dcor_points(x, y, w):
    c, a, b = dcov2_points(x, y, w)
    if a <= 0 or b <= 0:
        return 0.0
    return math.sqrt(c/math.sqrt(a*b))


def hsic_points(x, y, w, sx, sy):
    """Population HSIC with Gaussian kernels exp(-|u|^2/(2 s^2)) for a weighted point law."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    K = np.exp(-(x[:, None]-x[None, :])**2/(2*sx*sx))
    L = np.exp(-(y[:, None]-y[None, :])**2/(2*sy*sy))
    Kt = double_center(K, w)
    W = np.outer(w, w)
    return float((W*Kt*L).sum())


def mi_table(P):
    """Mutual information (nat) of a joint probability table."""
    P = np.asarray(P, float)
    px = P.sum(1, keepdims=True); py = P.sum(0, keepdims=True)
    m = P > 0
    return float((P[m]*np.log(P[m]/(px@py)[m])).sum())


# ---------- bivariate Gaussian ----------
def gauss_mi(rho):
    return -0.5*np.log(1-np.asarray(rho, float)**2)


def gauss_dcor(rho):
    """Szekely-Rizzo-Bakirov closed form for the standard bivariate normal."""
    r = np.abs(np.asarray(rho, float))
    num = r*np.arcsin(r)+np.sqrt(1-r*r)-r*np.arcsin(r/2)-np.sqrt(4-r*r)+1
    den = 1+math.pi/3-math.sqrt(3)
    return np.sqrt(num/den)


def gauss_hsic(rho, s=1.0):
    """HSIC with Gaussian kernels of bandwidth s on both coordinates, standard bivariate normal.
    E exp(-(U^2+V^2)/(2s^2)) for (U,V) ~ N(0,[[2,c],[c,2]]) equals det(I+S/s^2)^{-1/2}."""
    rho = np.asarray(rho, float)
    def g(c):
        a = 1+2/(s*s)
        return 1/np.sqrt(a*a-(c/(s*s))**2)
    return g(2*rho)+g(0*rho)-2*g(rho)


# ---------- continuous parabola X ~ Unif(-1,1), Y = X^2 + sigma Z ----------
def grid_x(n=2400):
    x = -1+(np.arange(n)+0.5)*2/n
    w = np.full(n, 1/n)
    return x, w


def abs_gauss_mean(m, s):
    """E|m + s W|, W ~ N(0,1)."""
    if s == 0:
        return np.abs(m)
    return s*math.sqrt(2/math.pi)*np.exp(-m*m/(2*s*s))+m*(1-2*Phi(-m/s))


def parabola_dcov(sigma, n=1600):
    """Return dCov^2, dVar^2(X), dVar^2(Y) for X~U(-1,1), Y=X^2+sigma Z by quadrature in (x,x')."""
    x, w = grid_x(n)
    W = np.outer(w, w)
    A = np.abs(x[:, None]-x[None, :])
    m = x[:, None]**2-x[None, :]**2
    G = abs_gauss_mean(m, sigma*math.sqrt(2))          # E|Y-Y'| given X=x, X'=x'
    hx = A @ w                                          # E|x-X'|
    t1 = (W*A*G).sum()
    t2 = (W*A).sum()*(W*G).sum()
    t3 = (w*hx) @ (G @ w)                               # E[ h(X) * E|Y-Y''| | X ] with X'' independent
    # careful: E|X-X'||Y-Y''| = E_X[ E_{X'}|X-X'| * E_{X''}E|Y-Y''| ]
    dcov2 = t1+t2-2*t3
    dvx = (W*A*A).sum()+(W*A).sum()**2-2*(w*hx*hx).sum()
    # dVar^2(Y): needs E|Y-Y'|^2 type terms; compute via E|Y-Y'||Y-Y'| = E(Y-Y')^2 and triple term by MC-free quadrature
    EYY2 = (W*(m*m+2*sigma*sigma)).sum()
    gy = G @ w                                          # E|y-Y'| averaged over noise of Y' but y random too -> approximate below
    # E|Y-Y'||Y-Y''|: condition on X, Z: y = x^2 + sigma z.  Use Gauss-Hermite in z.
    zs, zw = np.polynomial.hermite_e.hermegauss(40); zw = zw/zw.sum()
    yv = (x[:, None]**2+sigma*zs[None, :]).ravel(); yw = (w[:, None]*zw[None, :]).ravel()
    # E|y - Y'| for Y' = X'^2 + sigma Z'
    hy = np.array([(w*abs_gauss_mean(yy-x**2, sigma)).sum() for yy in yv])
    dvy = EYY2+(W*G).sum()**2-2*(yw*hy*hy).sum()
    return float(dcov2), float(dvx), float(dvy)


def parabola_dcor(sigma, n=1600):
    c, a, b = parabola_dcov(sigma, n)
    return math.sqrt(c/math.sqrt(a*b))


def parabola_hsic(sigma, sx, sy, n=1600):
    x, w = grid_x(n)
    W = np.outer(w, w)
    K = np.exp(-(x[:, None]-x[None, :])**2/(2*sx*sx))
    m = x[:, None]**2-x[None, :]**2
    v = sy*sy+2*sigma*sigma
    L = sy/math.sqrt(v)*np.exp(-m*m/(2*v))               # E l(Y,Y') given X, X'
    Kt = double_center(K, w)
    return float((W*Kt*L).sum())


def parabola_mi(sigma, n=40000):
    """I(X; X^2 + sigma Z) = h(Y) - 0.5 ln(2 pi e sigma^2)."""
    x, w = grid_x(n)
    y = np.linspace(-6*sigma, 1+6*sigma, 6001)
    f = np.zeros_like(y)
    for i in range(0, n, 2000):
        f += (w[i:i+2000, None]*np.exp(-(y[None, :]-x[i:i+2000, None]**2)**2/(2*sigma*sigma))).sum(0)
    f /= sigma*math.sqrt(2*math.pi)
    dy = y[1]-y[0]
    m = f > 1e-300
    hY = -float((f[m]*np.log(f[m])).sum()*dy)
    return hY-0.5*math.log(2*math.pi*math.e*sigma*sigma)


def gauss_binned_mi(rho, k):
    """MI of equal-probability k x k bin labels for the standard bivariate normal with correlation rho."""
    edges = Phi_inv(np.arange(1, k)/k)
    e = np.concatenate([[-np.inf], edges, [np.inf]])
    # cell probabilities via integrating over x the conditional normal
    xs = np.linspace(-8, 8, 8001); dx = xs[1]-xs[0]
    fx = phi(xs)
    s = math.sqrt(1-rho*rho)
    P = np.zeros((k, k))
    cond = np.stack([Phi((e[j+1]-rho*xs)/s)-Phi((e[j]-rho*xs)/s) for j in range(k)])  # (k, nx)
    lab = np.searchsorted(edges, xs)
    for i in range(k):
        m = lab == i
        P[i] = (cond[:, m]*fx[m]).sum(1)*dx
    P /= P.sum()
    return mi_table(P)


def gfmt(*axes):
    from matplotlib.ticker import FormatStrFormatter
    for ax in axes:
        ax.xaxis.set_major_formatter(FormatStrFormatter('%g')); ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))


def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha='center', va='top')
