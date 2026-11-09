"""Orthographic drawing helpers for the manifold chapters (sphere, torus, tangent planes).

Every curve is sampled from its analytic formula, then projected; visibility is decided
geometrically (sphere: sign of the outward normal; torus: a depth buffer), so hidden parts
are exact rather than sketched. The canvas unit is the physical millimetre.
"""
from pathlib import Path
import sys
import numpy as np
from matplotlib.collections import PolyCollection
from matplotlib.patches import FancyArrowPatch, Circle, Polygon

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, STROKE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401,E402


def canvas(width, height):
    """A full-bleed axes whose data coordinates are millimetres on the printed page."""
    fig, ax = figure(width_mm=width, height_mm=height)
    fig.set_layout_engine('none')
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    return fig, ax


class View:
    """Orthographic camera; ``f`` points from the object toward the viewer."""

    def __init__(self, azimuth, elevation):
        a, e = np.radians(azimuth), np.radians(elevation)
        self.f = np.array([np.cos(e)*np.cos(a), np.cos(e)*np.sin(a), np.sin(e)])
        self.r = np.array([-np.sin(a), np.cos(a), 0.0])
        self.u = np.cross(self.f, self.r)

    def xy(self, points):
        points = np.asarray(points, float)
        return np.stack([points@self.r, points@self.u], -1)

    def depth(self, points):
        return np.asarray(points, float)@self.f


class Placed:
    """A view placed on the canvas: centre (mm) and radius of one model unit (mm)."""

    def __init__(self, view, cx, cy, unit):
        self.view, self.c, self.unit = view, np.array([cx, cy], float), unit

    def __call__(self, points):
        return self.c + self.unit*self.view.xy(points)


def runs(mask):
    """Index ranges of consecutive True entries."""
    mask = np.asarray(mask, bool)
    edges = np.flatnonzero(np.diff(np.r_[0, mask.astype(int), 0]))
    return list(zip(edges[::2], edges[1::2]))


def split_plot(ax, xy, visible, color, lw=1.2, hidden_lw=.65, zorder=3, hidden=True):
    """Solid where visible; a thin dashed line where the surface hides the curve."""
    visible = np.asarray(visible, bool)
    for a, b in runs(visible):
        ax.plot(xy[a:b, 0], xy[a:b, 1], color=color, lw=lw, solid_capstyle='round', zorder=zorder)
    if hidden:
        for a, b in runs(~visible):
            ax.plot(xy[a:b, 0], xy[a:b, 1], color=color, lw=hidden_lw, ls=(0, (2.2, 1.8)), zorder=zorder-.5)


def sphere_disc(ax, place, fill=BLUE_FILL, edge=STROKE, lw=.95, zorder=1):
    ax.add_patch(Circle(place.c, place.unit, fc=fill, ec=edge, lw=lw, zorder=zorder))


def sphere_curve(ax, place, points, color, **kw):
    points = np.asarray(points, float)
    split_plot(ax, place(points), place.view.depth(points) >= 0, color, **kw)


def spherical(lat, lon):
    return np.stack([np.cos(lat)*np.cos(lon), np.cos(lat)*np.sin(lon), np.sin(lat)], -1)


def parallel(lat, n=361):
    return spherical(np.full(n, lat), np.linspace(-np.pi, np.pi, n))


def meridian(lon, n=361, lat0=-np.pi/2, lat1=np.pi/2):
    return spherical(np.linspace(lat0, lat1, n), np.full(n, lon))


def cap_boundary(center, radius, n=721):
    """Boundary of the spherical cap of angular radius ``radius`` around ``center``."""
    center = np.asarray(center, float)/np.linalg.norm(center)
    e1 = np.cross(center, [0.31, 0.47, 0.83]); e1 /= np.linalg.norm(e1)
    e2 = np.cross(center, e1)
    t = np.linspace(0, 2*np.pi, n)
    return np.cos(radius)*center+np.sin(radius)*(np.cos(t)[:, None]*e1+np.sin(t)[:, None]*e2)


def arrow(ax, a, b, color=STROKE, lw=.9, scale=6.5, zorder=6, rad=None, shrink=0):
    style = f'arc3,rad={rad}' if rad else 'arc3'
    patch = FancyArrowPatch(a, b, arrowstyle='-|>,head_length=.55,head_width=.22', mutation_scale=scale, lw=lw,
                            color=color, connectionstyle=style, shrinkA=shrink, shrinkB=shrink, zorder=zorder)
    ax.add_patch(patch)
    return patch


def dot(ax, p, color=INK, size=1.5, zorder=7, hollow=False):
    ax.plot([p[0]], [p[1]], 'o', ms=size*2.1, mfc='white' if hollow else color, mec=color, mew=.8, zorder=zorder)


def label(ax, p, text, size=8, color=INK, ha='center', va='center', zorder=9, halo=False):
    t = ax.text(p[0], p[1], text, fontsize=size, color=color, ha=ha, va=va, zorder=zorder)
    if halo:
        import matplotlib.patheffects as pe
        t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])
    return t


def mixed(ax, p, parts, size=8, color=INK, zorder=9):
    """Centre a run of pieces on one baseline; Chinese and mathtext must be separate text objects."""
    fig = ax.figure
    renderer = fig.canvas.get_renderer()
    mm = fig.get_figwidth()*25.4/fig.bbox.width
    items = [ax.text(0, p[1], t, fontsize=size, color=color, ha='left', va='baseline', zorder=zorder) for t in parts]
    widths = [it.get_window_extent(renderer).width*mm for it in items]
    gap = .6
    x = p[0]-(sum(widths)+gap*(len(items)-1))/2
    for it, w in zip(items, widths):
        it.set_x(x)
        x += w+gap


def panel_tag(ax, x, y, tag):
    ax.text(x, y, tag, fontsize=8, color=INK, ha='center', va='baseline', zorder=9)


class Torus:
    """Torus of radii R, r with painter-sorted facets and a depth buffer for curve visibility."""

    def __init__(self, place, R=2.0, r=.82, buffer_mm=.18):
        self.place, self.R, self.r = place, R, r
        n, m = 1600, 800
        th, ph = np.meshgrid(np.linspace(0, 2*np.pi, n), np.linspace(0, 2*np.pi, m), indexing='ij')
        pts = self.point(th, ph)
        xy = place(pts).reshape(-1, 2)
        depth = place.view.depth(pts).ravel()
        self.origin, self.step = xy.min(0)-2, buffer_mm
        size = np.ceil((xy.max(0)-self.origin)/buffer_mm).astype(int)+6
        self.buf = np.full(size, -np.inf)
        ij = ((xy-self.origin)/buffer_mm).astype(int)
        np.maximum.at(self.buf, (ij[:, 0], ij[:, 1]), depth)

    def point(self, th, ph):
        rho = self.R+self.r*np.cos(ph)
        return np.stack([rho*np.cos(th), rho*np.sin(th), self.r*np.sin(ph)], -1)

    def normal(self, th, ph):
        return np.stack([np.cos(ph)*np.cos(th), np.cos(ph)*np.sin(th), np.sin(ph)], -1)

    def visible(self, pts, tol=.34):
        xy = self.place(pts)
        ij = ((xy-self.origin)/self.step).astype(int)
        depth = self.place.view.depth(pts)
        return np.array([depth[k] >= self.buf[max(i-1, 0):i+2, max(j-1, 0):j+2].max()-tol for k, (i, j) in enumerate(ij)])

    def fill(self, ax, colour_of, nth=170, nph=90, zorder=1):
        th = np.linspace(0, 2*np.pi, nth+1); ph = np.linspace(0, 2*np.pi, nph+1)
        polys, depths, colours = [], [], []
        for i in range(nth):
            for j in range(nph):
                a, b = th[i], th[i+1]; c, d = ph[j], ph[j+1]
                mid = ((a+b)/2, (c+d)/2)
                if self.normal(*mid)@self.place.view.f <= -.02:
                    continue
                corners = self.point(np.array([a, b, b, a]), np.array([c, c, d, d]))
                polys.append(self.place(corners)); depths.append(self.place.view.depth(self.point(*mid)))
                colours.append(colour_of(*mid))
        order = np.argsort(depths)
        coll = PolyCollection([polys[k] for k in order], facecolors=[colours[k] for k in order],
                              edgecolors=[colours[k] for k in order], linewidths=.3, zorder=zorder)
        ax.add_collection(coll)

    def silhouette(self, ax, color=STROKE, lw=.95, zorder=4):
        from contourpy import contour_generator
        th = np.linspace(0, 2*np.pi, 1441); ph = np.linspace(0, 2*np.pi, 721)
        T, P = np.meshgrid(th, ph)
        z = self.normal(T, P)@self.place.view.f
        for line in contour_generator(th, ph, z).lines(0.0):
            pts = self.point(line[:, 0], line[:, 1])
            split_plot(ax, self.place(pts), self.visible(pts, tol=.62), color, lw=lw, hidden=False, zorder=zorder)

    def curve(self, ax, th, ph, color, lw=1.2, hidden=False, zorder=3):
        pts = self.point(np.asarray(th), np.asarray(ph))
        split_plot(ax, self.place(pts), self.visible(pts), color, lw=lw, hidden=hidden, zorder=zorder)
