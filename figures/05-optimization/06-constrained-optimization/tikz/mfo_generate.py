#!/usr/bin/env python3
"""Generate the TikZ sources of chapter "manifold optimization" (prefix mfo-).

Three-dimensional geometry is sampled here (orthographic camera, real data of
the running example f = x'Ax/2, A = diag(1,2,4), x0 = (2,2,1)/3) and written as
plain editable figure.tex files. Usage: python3 mfo_generate.py [names...]
"""
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
HEAD = r"""% Original analytic teaching diagram, 2026-11-09.
% Coordinates sampled by ../mfo_generate.py.
\definecolor{VB}{HTML}{7188A3}\definecolor{VBF}{HTML}{E5EAF0}
\definecolor{VG}{HTML}{829C8B}\definecolor{VGF}{HTML}{E8EEE9}
\definecolor{VY}{HTML}{B4A16F}\definecolor{VYF}{HTML}{F1ECDD}
\definecolor{VR}{HTML}{A7787D}\definecolor{VRF}{HTML}{F0E5E6}
\definecolor{VP}{HTML}{9588A5}\definecolor{VPF}{HTML}{ECE8F0}
\definecolor{VI}{HTML}{3B4252}\definecolor{VM}{HTML}{6B7280}\definecolor{VL}{HTML}{4C4D4F}
\begin{tikzpicture}[x=1mm,y=1mm,>=Stealth,font=\figurefont\fontsize{8}{10}\selectfont,
lab/.style={text=VM,font=\figurefont\fontsize{7.5}{9}\selectfont},
pt/.style={circle,inner sep=0pt,minimum size=1.9mm},
box/.style={draw=VB,fill=white,rounded corners=.65mm,line width=.7pt,inner sep=1.4mm,align=center,text=VI}]
"""
A = np.diag([1., 2, 4])
x0 = np.array([2, 2, 1]) / 3
E1 = np.array([1, -2, 2]) / 3
E2 = np.array([2, -1, -2]) / 3
normalize = lambda u: u / np.linalg.norm(u)
q = lambda x: x @ A @ x
g = lambda x: A @ x - q(x) * x


class Cam:
    """Orthographic camera; scale in mm per unit, origin at (ox, oy)."""
    def __init__(self, az, el, scale=22, ox=0, oy=0):
        a, e = np.radians(az), np.radians(el)
        self.view = np.array([np.cos(e) * np.cos(a), np.cos(e) * np.sin(a), np.sin(e)])
        self.right = np.array([-np.sin(a), np.cos(a), 0.])
        self.up = np.cross(self.view, self.right)
        self.s, self.ox, self.oy = scale, ox, oy

    @classmethod
    def from_basis(cls, view, right, scale=22, ox=0, oy=0):
        """Camera with explicit view direction and screen-right direction."""
        c = cls(0, 0, scale, ox, oy)
        c.view = normalize(view)
        c.right = normalize(right - (right @ c.view) * c.view)
        c.up = np.cross(c.view, c.right)
        return c

    def xy(self, p):
        p = np.asarray(p, float)
        return self.ox + self.s * (p @ self.right), self.oy + self.s * (p @ self.up)

    def c(self, p):
        x, y = self.xy(p)
        return f"({x:.2f},{y:.2f})"

    def line(self, pts):
        return " -- ".join(self.c(p) for p in pts)

    def sphere(self, fill="VBF", stroke="VB"):
        return f"\\draw[{stroke},fill={fill},line width=.9pt] ({self.ox:.2f},{self.oy:.2f}) circle ({self.s:.2f});\n"

    def curve(self, pts, style, back="dashed,line width=.45pt"):
        """Draw a curve on the unit sphere; the hidden part is dashed."""
        pts = np.asarray(pts)
        front = pts @ self.view >= 0
        out, i, n = "", 0, len(pts)
        while i < n:
            j = i
            while j + 1 < n and front[j + 1] == front[i]:
                j += 1
            seg = pts[max(i - 1, 0):j + 1]
            if len(seg) >= 2:
                out += f"\\draw[{style}{',' + back if not front[i] else ''}] {self.line(seg)};\n"
            i = j + 1
        return out

    def patch(self, centre, u, v, a, style="VL,line width=.55pt"):
        c = [centre + s * a * u + t * a * v for s, t in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
        return f"\\draw[{style}] {self.line(c)} -- cycle;\n"

    def arrow(self, p, r, style):
        return f"\\draw[->,{style}] {self.c(p)} -- {self.c(r)};\n"

    def point(self, p, colour):
        return f"\\node[pt,fill={colour}] at {self.c(p)} {{}};\n"

    def label(self, p, text, anchor="center", dx=0, dy=0, style="text=VI"):
        x, y = self.xy(p)
        return f"\\node[{style},anchor={anchor}] at ({x + dx:.2f},{y + dy:.2f}) {{{text}}};\n"


def side_cam(top, right, scale, ox, oy, tilt):
    """Look almost along the normal of the plane (top, right), with top pointing up."""
    n = normalize(np.cross(right, top))
    c = Cam.from_basis(n + tilt * top, right, scale, ox, oy)
    if c.up @ top < 0:
        n = -n
        c = Cam.from_basis(n + tilt * top, right, scale, ox, oy)
    c.n = n
    return c


def slab(c, centre, u, n, a0, a1, b, style="VL,line width=.55pt"):
    """Outline of a rectangle in a tangent plane."""
    q = [centre + s * u + t * n for s, t in [(a0, -b), (a1, -b), (a1, b), (a0, b)]]
    return f"\\draw[{style}] {c.line(q)} -- cycle;\n"


def great(a, b, n=80, t0=0., t1=1.):
    """Points of the shortest arc from a to b, optional sub-interval."""
    w = np.arccos(np.clip(a @ b, -1, 1))
    o = normalize(b - (a @ b) * a)
    th = np.linspace(t0 * w, t1 * w, n)
    return np.array([np.cos(t) * a + np.sin(t) * o for t in th])


def meridians(cam, n=7, style="VB!55,line width=.35pt"):
    """A few light coordinate circles giving the sphere its shape."""
    out = ""
    for lat in np.radians([-50, 0, 50]):
        th = np.linspace(0, 2 * np.pi, 160)
        pts = np.c_[np.cos(lat) * np.cos(th), np.cos(lat) * np.sin(th), np.full_like(th, np.sin(lat))]
        out += cam.curve(pts, style, back="dotted,line width=.3pt")
    return out


FIGS = {}
def fig(f):
    FIGS["mfo-" + f.__name__.replace("_", "-")] = f
    return f


@fig
def regular_singular():
    """Regular level set, crossing, corner: 2D sketches."""
    s = ""
    s += r"""\begin{scope}[shift={(0,0)}]
\draw[VB,fill=VBF,line width=1.1pt] (0,0) circle (13);
\draw[VL,line width=.8pt] (5.9,19.4) -- (19.4,1.6);
\node[pt,fill=VG] at (9.19,9.19) {};
\draw[->,VG,line width=1.1pt] (9.19,9.19) -- (15.5,4.4);
\draw[->,VP,line width=1.1pt] (9.19,9.19) -- (15.5,15.5);
\node[text=VI,anchor=north east] at (9,8.8) {$\bm{x}$};
\node[lab,anchor=west] at (15.7,15.8) {$\nabla h$};
\node[lab,anchor=north] at (19.4,1.2) {切线};
\node[text=VI] at (0,-20) {(a)};
\end{scope}
\begin{scope}[shift={(37,0)}]
\draw[VB,line width=1.5pt] (-15,0) -- (15,0);
\draw[VB,line width=1.5pt] (0,-15) -- (0,15);
\node[pt,fill=VR] at (0,0) {};
\draw[->,VG,line width=1.1pt] (0,0) -- (9,0);
\draw[->,VG,line width=1.1pt] (0,0) -- (0,9);
\draw[->,VR,dashed,line width=.9pt] (0,0) -- (7,7);
\node[lab,anchor=south west] at (6.8,6.8) {和方向};
\node[lab,anchor=north east] at (-.6,-.7) {$\nabla h=\bm{0}$};
\node[text=VI] at (0,-20) {(b)};
\end{scope}
\begin{scope}[shift={(74,0)}]
\draw[VB,line width=1.5pt,fill=VBF] (-13,-13) rectangle (13,13);
\node[pt,fill=VR] at (13,13) {};
\draw[->,VG,line width=1.1pt] (13,13) -- (13,3);
\draw[->,VG,line width=1.1pt] (13,13) -- (3,13);
\draw[->,VR,dashed,line width=.9pt] (13,13) -- (19,19);
\node[lab,anchor=north east] at (12,12) {棱角};
\node[lab,anchor=south west] at (15.5,18) {离开};
\node[text=VI] at (0,-20) {(c)};
\end{scope}
"""
    return s


@fig
def retraction_grid():
    """Polar grid of the tangent plane and its image under normalization."""
    S = 11.0
    s = "\\begin{scope}[shift={(0,0)}]\n"
    rs = [.5, 1., 1.5]
    for r in rs:
        s += f"\\draw[VG,line width=.8pt] (0,0) circle ({S*r:.2f});\n"
    for k in range(8):
        a = k * np.pi / 4
        s += f"\\draw[VB,line width=.65pt] (0,0) -- ({S*1.75*np.cos(a):.2f},{S*1.75*np.sin(a):.2f});\n"
    s += "\\node[pt,fill=VG] at (0,0) {};\n\\node[text=VI,anchor=north west] at (.6,-.6) {$\\bm{x}$};\n"
    s += "\\node[lab,anchor=south east] at (-13,14) {$T_{\\bm{x}}S^2$};\n"
    s += "\\node[text=VI] at (0,-25) {(a)};\n\\end{scope}\n"
    c = Cam(25, 30, 23, 66, 0)
    x = normalize(np.array([1., .15, .75]))
    u = normalize(np.cross(np.array([0, 0, 1.]), x))
    v = np.cross(x, u)
    s += c.sphere()
    for k in range(8):
        a = k * np.pi / 4
        d = np.cos(a) * u + np.sin(a) * v
        pts = np.array([normalize(x + r * d) for r in np.linspace(0, 1.75, 40)])
        s += c.curve(pts, "VB,line width=.65pt", back="line width=.01pt,draw=none")
    for r in rs:
        th = np.linspace(0, 2 * np.pi, 120)
        pts = np.array([normalize(x + r * (np.cos(a) * u + np.sin(a) * v)) for a in th])
        s += c.curve(pts, "VG,line width=.8pt", back="line width=.01pt,draw=none")
    s += c.point(x, "VG") + c.label(x, r"$\bm{x}$", "south west", .5, .5)
    s += "\\node[text=VI] at (66,-27) {(b)};\n"
    return s


@fig
def stiefel_qr_polar():
    X = np.eye(3)[:, :2]
    D = np.array([[0, 0], [0, 0], [1, 1.]])
    Y = X + D
    Qq, Rr = np.linalg.qr(Y)
    Qq = Qq * np.sign(np.diag(Rr))
    w, V = np.linalg.eigh(Y.T @ Y)
    Pl = Y @ (V @ np.diag(w ** -.5) @ V.T)
    s = ""
    o = np.zeros(3)
    for k, (Z, ox, name) in enumerate([(Qq, 0, "QR"), (Pl, 66, "polar")]):
        c = Cam(40, 22, 20, ox, 0)
        u1 = normalize(Y[:, 0] + Y[:, 1])
        u2 = normalize(Y[:, 0] - Y[:, 1])
        s += c.patch(o, u1, u2, 1.05, "VL,line width=.5pt")
        for j in (0, 1):
            s += c.arrow(o, X[:, j], "VB,line width=1.15pt")
            s += c.arrow(o, Y[:, j], "VY,line width=1.15pt")
            s += c.arrow(o, Z[:, j], "VG,line width=1.45pt")
        s += c.label(X[:, 0], r"$\bm{x}_1$", "north", 0, -.9) + c.label(X[:, 1], r"$\bm{x}_2$", "north", 1.5, -.8)
        s += c.label(Y[:, 0], r"$\bm{y}_1$", "south east", -.4, .5) + c.label(Y[:, 1], r"$\bm{y}_2$", "south west", .3, .5)
        s += f"\\node[text=VI] at ({ox},-20) {{({'ab'[k]})}};\n"
    return s


@fig
def operator_square():
    return r"""\node[box] (a) at (0,18) {$T_{\bm{x}}M$};
\node[box] (b) at (46,18) {$T_{\bm{x}}M$};
\node[box] (c) at (0,0) {$T_{\bm{x}^{+}}M$};
\node[box] (d) at (46,0) {$T_{\bm{x}^{+}}M$};
\draw[->,VG,line width=.95pt] (a) -- node[above,text=VI] {$\bm{B}$} (b);
\draw[->,VL,line width=.85pt] (b) -- node[right,text=VI] {$\mathcal{T}$} (d);
\draw[<-,VL,line width=.85pt] (a) -- node[left,text=VI] {$\mathcal{T}^{-1}$} (c);
\draw[->,VG,dashed,line width=.95pt] (c) -- node[below,text=VI] {$\widetilde{\bm{B}}=\mathcal{T}\bm{B}\mathcal{T}^{-1}$} (d);
"""


@fig
def iteration_loop():
    return r"""\node[box,minimum width=23mm] (a) at (0,14) {切空间候选步};
\node[box,minimum width=20mm] (b) at (40,14) {回缩};
\node[box,minimum width=23mm] (c) at (80,14) {拉回目标检验};
\node[box,minimum width=23mm] (d) at (80,0) {接受新点};
\node[box,minimum width=23mm] (e) at (0,0) {搬运历史向量};
\draw[->,VL,line width=.85pt] (a) -- (b);
\draw[->,VL,line width=.85pt] (b) -- (c);
\draw[->,VL,line width=.85pt] (c) -- node[right,lab] {通过} (d);
\draw[->,VL,line width=.85pt] (d) -- (e);
\draw[->,VL,line width=.85pt] (e) -- (a);
\draw[->,VR,dashed,line width=.85pt] (c.north) -- ++(0,5) -| node[pos=.25,above,lab] {未通过：缩短} (a.north);
"""


@fig
def step_leaves():
    """Euclidean update leaves the sphere; two columns lose orthonormality."""
    G = g(x0)
    c = side_cam(x0, normalize(-G), 24, 0, 0, .3)
    n = c.n
    y = x0 - .5 * G
    u = normalize(-G)
    s = c.sphere() + c.curve(great(x0, normalize(x0 + 1.2 * u)), "VB,line width=.6pt")
    s += slab(c, x0, u, n, -.55, .9, .45)
    s += c.arrow(x0, y, "VY,line width=1.3pt")
    s += f"\\draw[VM,dashed,line width=.55pt] {c.c(y)} -- {c.c(normalize(y))};\n"
    s += c.point(x0, "VG") + c.point(normalize(y), "VG")
    s += f"\\node[pt,draw=VR,fill=white,line width=.8pt] at {c.c(y)} {{}};\n"
    s += c.label(x0, r"$\bm{x}$", "south", 0, 1.2)
    s += c.label(y, r"$\bm{x}+\alpha\bm{d}$", "south", 0, 1.2)
    s += c.label(normalize(y), r"$\bm{x}^{+}$", "north", 0, -1.2)
    s += c.label(x0 - .5 * u, r"$T_{\bm{x}}S^2$", "south", 0, 1.8, "lab")
    s += "\\node[text=VI] at (0,-29) {(a)};\n"
    X = np.c_[x0, E1]
    S = X.T @ A @ X
    Gm = A @ X - X @ ((S + S.T) / 2)
    Y = X - .5 * Gm
    d = Cam.from_basis(normalize(E2 * .55 + normalize(x0 + E1) * .75 + normalize(x0 - E1) * .1), normalize(x0 - E1), 22, 56, -3)
    o = np.zeros(3)
    s += d.patch(o, normalize(x0 + E1), normalize(x0 - E1), 1.1)
    s += d.arrow(o, X[:, 0], "VG,line width=1.3pt") + d.arrow(o, X[:, 1], "VG,line width=1.3pt")
    s += d.arrow(o, Y[:, 0], "VY,line width=1.2pt") + d.arrow(o, Y[:, 1], "VY,line width=1.2pt")
    s += d.label(X[:, 0], r"$\bm{x}_1$", "south", 0, .8) + d.label(X[:, 1], r"$\bm{x}_2$", "south", 0, .8)
    s += d.label(Y[:, 0], r"$\bm{y}_1$", "north", 0, -.9) + d.label(Y[:, 1], r"$\bm{y}_2$", "north", 0, -.9)
    s += "\\node[text=VI] at (56,-29) {(b)};\n"
    return s


@fig
def metric_gradient():
    """Same differential, two metrics, two gradients."""
    c = np.array([1., 1.])
    out = ""
    S = 11.0
    for k, (G, ox) in enumerate([(np.eye(2), 0), (np.diag([4., 1.]), 56)]):
        gr = np.linalg.solve(G, c)
        u = gr / np.sqrt(gr @ G @ gr)
        top = c @ u
        out += f"\\begin{{scope}}[shift={{({ox},0)}}]\n"
        out += f"\\draw[VL,line width=.6pt,->] (-21,0) -- (24,0) node[lab,anchor=north east] {{$v_1$}};\n"
        out += f"\\draw[VL,line width=.6pt,->] (0,-19) -- (0,22) node[lab,anchor=north west] {{$v_2$}};\n"
        for lv in (-top, 0., top):
            a, b = (lv / 2 + 1.3, lv / 2 - 1.3), (lv / 2 - 1.3, lv / 2 + 1.3)
            out += f"\\draw[VB,line width=.75pt] ({S*a[0]:.2f},{S*a[1]:.2f}) -- ({S*b[0]:.2f},{S*b[1]:.2f});\n"
        th = np.linspace(0, 2 * np.pi, 120)
        Li = np.linalg.cholesky(np.linalg.inv(G))
        e = (Li @ np.c_[np.cos(th), np.sin(th)].T).T
        out += "\\draw[VG,line width=1.1pt,fill=VGF] " + " -- ".join(f"({S*p[0]:.2f},{S*p[1]:.2f})" for p in e) + " -- cycle;\n"
        out += f"\\draw[->,VR,line width=1.3pt] (0,0) -- ({S*gr[0]:.2f},{S*gr[1]:.2f});\n"
        out += f"\\node[pt,fill=VG] at ({S*u[0]:.2f},{S*u[1]:.2f}) {{}};\n"
        out += f"\\node[text=VI,anchor=south west] at ({S*gr[0]+.4:.2f},{S*gr[1]+.4:.2f}) {{$\\operatorname{{grad}}f$}};\n"
        out += f"\\node[text=VI] at (0,-23) {{({'ab'[k]})}};\n\\end{{scope}}\n"
    return out


@fig
def tangent_projection():
    gf = A @ x0
    G = g(x0)
    sc = .6
    c = side_cam(x0, normalize(G), 24, 0, 0, .3)
    u, n = normalize(G), c.n
    tip = x0 + sc * gf
    nor = x0 + sc * (x0 @ gf) * x0
    tan = x0 + sc * G
    s = c.sphere() + slab(c, x0, u, n, -.75, 1.05, .4)
    s += f"\\draw[VM,dashed,line width=.55pt] {c.c(tip)} -- {c.c(nor)};\n\\draw[VM,dashed,line width=.55pt] {c.c(tip)} -- {c.c(tan)};\n"
    s += c.arrow(x0, tip, "VB,line width=1.3pt")
    s += c.arrow(x0, nor, "VP,line width=1.2pt")
    s += c.arrow(x0, tan, "VG,line width=1.4pt")
    s += c.point(x0, "VG")
    s += c.label(tip, r"$\nabla f(\bm{x})$", "south west", .4, .3)
    s += c.label(nor, r"$(\bm{x}^\top\nabla f)\bm{x}$", "south east", -.6, .3)
    s += c.label(tan, r"$\operatorname{grad}f(\bm{x})$", "north west", .2, -3)
    s += c.label(x0, r"$\bm{x}$", "north east", -.8, -2.2)
    s += c.label(x0 - .75 * u, r"$T_{\bm{x}}S^2$", "north west", 1, -3.2, "lab")
    return s


@fig
def retraction_cut():
    S = 20
    s = ""
    def P(th, r=1.0):
        return f"({S*r*np.sin(th):.2f},{S*r*np.cos(th):.2f})"
    sv = 1.2
    s += f"\\draw[VB,fill=VBF,line width=1pt] (0,0) circle ({S});\n"
    s += f"\\draw[VL,line width=.75pt] (-10,{S}) -- (31,{S});\n"
    s += "\\node[pt,fill=VL,minimum size=1.2mm] at (0,0) {};\n"
    s += f"\\draw[->,VY,line width=1.3pt] (0,{S}) -- ({S*sv:.2f},{S});\n"
    t = np.arctan(sv)
    s += f"\\draw[VM,dashed,line width=.55pt] (0,0) -- ({S*sv:.2f},{S});\n"
    s += "\\draw[VP,line width=1.5pt] " + " -- ".join(P(a) for a in np.linspace(0, sv, 40)) + ";\n"
    s += f"\\node[pt,fill=VP] at {P(sv)} {{}};\n\\node[pt,fill=VG] at {P(t)} {{}};\n\\node[pt,fill=VG] at (0,{S}) {{}};\n"
    s += f"\\node[text=VI,anchor=south] at (0,{S+.8}) {{$\\bm{{x}}$}};\n"
    s += f"\\node[text=VI,anchor=south] at ({S*sv:.2f},{S+.8}) {{$\\bm{{x}}+\\bm{{v}}$}};\n"
    s += f"\\node[text=VI] at {P(.42, .62)} {{归一化}};\n"
    s += f"\\node[text=VI,anchor=west] at ({S*np.sin(sv)+1.2:.2f},{S*np.cos(sv)-.5:.2f}) {{指数映射}};\n"
    s += "\\node[text=VI] at (4,-26) {(a)};\n"
    s += "\\begin{scope}[shift={(62,0)}]\n"
    th = np.linspace(np.pi / 2, 3 * np.pi / 2, 60)
    s += "\\draw[VR,line width=2pt] " + " -- ".join(P(a) for a in th) + ";\n"
    th = np.linspace(-np.pi / 2, np.pi / 2, 90)
    s += "\\draw[VG,line width=2pt] " + " -- ".join(P(a) for a in th) + ";\n"
    s += f"\\draw[VL,line width=.75pt] (-27,{S}) -- (27,{S});\n"
    for sv in [.25, .6, 1.1, 2.0, 4.6]:
        for sg in (1, -1):
            a = sg * np.arctan(sv)
            xt = min(S * sv, 27)
            yy = S if S * sv <= 27 else S * 27 / (S * sv)
            s += f"\\draw[VM,line width=.45pt] (0,0) -- ({sg*xt:.2f},{yy:.2f});\n"
            s += f"\\node[pt,fill=VG,minimum size=1.5mm] at {P(a)} {{}};\n"
    s += f"\\node[pt,fill=VG] at (0,{S}) {{}};\n\\node[text=VI,anchor=south] at (0,{S+.8}) {{$\\bm{{x}}$}};\n"
    s += f"\\node[text=VI,anchor=north] at (0,{-S-.9}) {{$-\\bm{{x}}$}};\n"
    s += f"\\node[lab,anchor=east] at ({-S*.75:.2f},{-S*.82:.2f}) {{到不了}};\n"
    s += "\\node[text=VI] at (0,-29) {(b)};\n\\end{scope}\n"
    return s


@fig
def transport():
    x = normalize(np.array([.55, -.55, .62]))
    t0 = normalize(np.array([.72, .55, .42]) - (np.array([.72, .55, .42]) @ x) * x)
    ang = np.radians(62)
    y = np.cos(ang) * x + np.sin(ang) * t0
    mid = normalize(x + y)
    c = side_cam(mid, normalize(y - x), 26, 0, 0, .32)
    n = c.n
    t = normalize(y - (x @ y) * x)
    v = .68 * t + .18 * n
    par = v - ((x + y) @ v) / (1 + x @ y) * (x + y)
    proj = v - (y @ v) * y
    ty = normalize(x - (x @ y) * y)
    s = c.sphere() + c.curve(great(x, y), "VL,line width=1.1pt")
    s += slab(c, x, t, n, -.4, .85, .32, "VM,line width=.5pt")
    s += slab(c, y, -ty, n, -.4, .85, .32, "VM,line width=.5pt")
    s += c.arrow(x, x + v, "VB,line width=1.35pt")
    s += c.arrow(y, y + v, "VM,dashed,line width=.75pt")
    s += f"\\draw[VM,dashed,line width=.5pt] {c.c(y + v)} -- {c.c(y + proj)};\n"
    s += c.arrow(y, y + par, "VG,line width=1.4pt")
    s += c.arrow(y, y + proj, "VY,line width=1.6pt")
    s += c.point(x, "VG") + c.point(y, "VG")
    s += c.label(x, r"$\bm{x}$", "north", 0, -1.2) + c.label(y, r"$\bm{y}$", "north east", -1, -1)
    s += c.label(x + v, r"$\bm{v}$", "south", 0, .5)
    s += c.label(y + proj, r"投影", "north east", 0, -1.6)
    s += c.label(y + par, r"平行移动", "north west", -2, -1.5)
    s += c.label(y + v, r"平移副本", "west", .8, .3, "lab")
    return s


@fig
def rgd_step():
    G = g(x0)
    u = normalize(-G)
    c = side_cam(x0, u, 28, 0, 0, .3)
    y1, y2 = x0 - G, x0 - .5 * G
    p1, p2 = normalize(y1), normalize(y2)
    s = c.sphere() + slab(c, x0, u, c.n, -.45, 1.15, .42)
    s += c.arrow(x0, y1, "VY,line width=1.2pt")
    s += c.arrow(x0, y2, "VG,line width=1.6pt")
    for a, b in ((y1, p1), (y2, p2)):
        s += f"\\draw[VM,dashed,line width=.5pt] {c.c(a)} -- {c.c(b)};\n"
    s += c.curve(great(x0, p1, 60), "VG,line width=.9pt")
    s += c.point(x0, "VG") + c.point(p2, "VG")
    s += f"\\node[pt,fill=white,draw=VY,line width=.9pt] at {c.c(p1)} {{}};\n"
    s += c.label(x0, r"$\bm{x}^{(0)}$", "south", 0, 4.2)
    s += c.label(y2, r"$\alpha=\frac12$", "south", 0, 4.2, "lab")
    s += c.label(y1, r"$\alpha=1$", "south", 0, 4.2, "lab")
    s += c.label(p2, r"$\bm{x}^{(1)}$", "north east", -1, -1) + c.label(p1, r"被拒绝的试探点", "north east", -1.2, -1.6, "lab")
    return s


@fig
def rtr_disc():
    u = E2
    c = side_cam(x0, u, 27, 0, 0, .42)
    n = c.n
    Dl = 1.0
    th = np.linspace(0, 2 * np.pi, 180)
    v1 = normalize(np.cross(x0, u))
    disc = np.array([x0 + Dl * (np.cos(a) * u + np.sin(a) * v1) for a in th])
    s = c.sphere()
    s += f"\\draw[VP,line width=.95pt] {c.line(disc)} -- cycle;\n"
    cap = np.array([normalize(p) for p in disc])
    s += c.curve(cap, "VG,line width=1.2pt", back="line width=.01pt,draw=none")
    vc = -0.18378378 * E1 + 0.73513514 * E2
    vt = E2
    for w, col in ((vc, "VY"), (vt, "VG")):
        s += c.arrow(x0, x0 + w, f"{col},line width=1.35pt")
        s += f"\\draw[VM,dashed,line width=.5pt] {c.c(x0 + w)} -- {c.c(normalize(x0 + w))};\n"
    s += c.point(x0, "VG") + c.point(normalize(x0 + vt), "VG")
    s += f"\\node[pt,fill=white,draw=VY,line width=.9pt] at {c.c(normalize(x0 + vc))} {{}};\n"
    s += c.label(x0, r"$\bm{x}^{(0)}$", "south east", -.5, .8)
    s += c.label(x0 + vt, r"$\bm{v}$", "west", 1, 0)
    s += c.label(x0 + vc, r"$\bm{v}^{\mathrm{C}}$", "south", 0, 1.2)
    s += c.label(x0 - Dl * u, r"$\lVert\bm{v}\rVert_2=\Delta$", "east", -1, 0, "lab")
    s += c.label(normalize(x0 + vt), r"$R(\bm{v})$", "west", 1.3, -1.5)
    return s


@fig
def grassmann_fibre():
    c = Cam(30, 58, 20, 0, 0)
    a, b = normalize(np.array([1., 0, .3])), normalize(np.array([0, 1., .35]))
    b = normalize(b - (a @ b) * a)
    o = np.zeros(3)
    s = c.patch(o, a, b, 1.2, "VB,line width=.7pt,fill=VBF")
    for ang, col in ((0, "VG"), (35, "VY"), (70, "VP")):
        t = np.radians(ang)
        p1 = np.cos(t) * a + np.sin(t) * b
        p2 = -np.sin(t) * a + np.cos(t) * b
        s += c.arrow(o, p1, f"{col},line width=1.3pt") + c.arrow(o, p2, f"{col},line width=1.3pt")
    s += "\\node[text=VI] at (0,-31) {(a)};\n"
    s += r"""\begin{scope}[shift={(54,0)}]
\draw[VB,line width=1.1pt] (-24,-14) .. controls (-10,-18) and (10,-10) .. (24,-14);
\node[lab,anchor=north] at (17,-15.6) {$\mathrm{Gr}(k,n)$};
\foreach \x/\y in {-16/-15.15,0/-14,16/-13.1}{
\draw[VM,line width=.75pt] (\x,\y+6) -- (\x,\y+30);
\node[pt,fill=VB,minimum size=1.4mm] at (\x,\y) {};}
\node[lab,anchor=south] at (-16,15.2) {纤维};
\node[pt,fill=VG] at (0,6) {};
\node[text=VI,anchor=north east] at (-.6,5.8) {$\bm{X}$};
\draw[->,VR,line width=1.2pt] (0,6) -- (0,17);
\node[lab,anchor=west] at (.7,14.5) {竖直};
\draw[->,VG,line width=1.4pt] (0,6) -- (13,7.8);
\node[lab,anchor=north west] at (5,6) {水平};
\node[text=VI] at (0,-31) {(b)};
\end{scope}
"""
    return s


def main():
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        d = HERE / n
        d.mkdir(exist_ok=True)
        (d / "figure.tex").write_text(HEAD + FIGS[n]() + "\\end{tikzpicture}\n")


if __name__ == "__main__":
    main()
