"""Drawers for the O level 2026 MCQ practice set (6091), redrawn from the SEAB specimen Paper 1 and school prelim figures.
Same conventions as figs.py: black line art on white, PNG bytes at 170 dpi, labels computed from the arguments."""
import math

import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

from .figs import _fig, _png

ARROW = dict(arrowstyle="-|>", mutation_scale=13, lw=1.6, color="black")


def _arrow(ax, p0, p1, **kw):
    ax.add_patch(FancyArrowPatch(p0, p1, **{**ARROW, **kw}))


# ------------------------------------------------------------------ Ch 4 turning effects
def couple_rod(f_label="5.0 N"):
    """Horizontal rod with equal and opposite forces at its two ends (a couple)."""
    fig, ax = _fig(5.0, 2.4)
    ax.add_patch(Rectangle((0, 0), 5.0, 0.22, fc="white", ec="black", lw=1.6))
    _arrow(ax, (0.3, 1.4), (0.3, 0.26))
    ax.text(0.45, 1.1, f_label, ha="left", va="center", fontsize=10.5)
    _arrow(ax, (4.7, -1.2), (4.7, -0.04))
    ax.text(4.55, -0.9, f_label, ha="right", va="center", fontsize=10.5)
    ax.set_xlim(-0.4, 5.4)
    ax.set_ylim(-1.5, 1.7)
    return _png(fig)


def tilted_box_points(letters=("P", "Q", "R", "S"), correct_index=2, angle_deg=32):
    """A tall box (a bus) tilted on a ramp until it is about to topple; four marked points inside, one vertically above the
    pivot corner (index `correct_index`), the others off that vertical line. Returns PNG bytes."""
    fig, ax = _fig(5.2, 4.4)
    a = math.radians(angle_deg)
    ux, uy = math.cos(a), math.sin(a)          # along the ramp (up-slope, to the left is downhill)
    vx, vy = -math.sin(a), math.cos(a)         # normal to the ramp
    # ramp: a thick line through the pivot corner, falling to the left
    px, py = 1.8, 1.2
    ax.plot([px - 2.2 * ux, px + 2.6 * ux], [py - 2.2 * uy, py + 2.6 * uy], color="#555555", lw=6, solid_capstyle="butt")
    ax.plot([-1.0, 5.0], [py - 2.2 * uy - 0.05, py - 2.2 * uy - 0.05], color="black", lw=1.4)
    for x in np.arange(-0.8, 5.0, 0.4):
        ax.plot([x, x - 0.25], [py - 2.2 * uy - 0.05, py - 2.2 * uy - 0.35], color="black", lw=0.8)
    w, h = 1.6, 3.1                            # box resting on the ramp, lower-left corner at the pivot
    corners = [(px, py), (px + w * ux, py + w * uy), (px + w * ux + h * vx, py + w * uy + h * vy), (px + h * vx, py + h * vy)]
    ax.add_patch(Polygon(corners, closed=True, fc="white", ec="black", lw=1.8))
    # windows
    for k in range(3):
        s = 0.55 + k * 0.8
        win = [(px + 0.25 * ux + s * vx, py + 0.25 * uy + s * vy), (px + (w - 0.25) * ux + s * vx, py + (w - 0.25) * uy + s * vy),
               (px + (w - 0.25) * ux + (s + 0.5) * vx, py + (w - 0.25) * uy + (s + 0.5) * vy), (px + 0.25 * ux + (s + 0.5) * vx, py + 0.25 * uy + (s + 0.5) * vy)]
        ax.add_patch(Polygon(win, closed=True, fc="#eeeeee", ec="black", lw=1.0))
    # candidate points: along the box's centre line at different heights, one of them on the vertical through the pivot
    heights = [0.9, 1.5, 2.1, 2.7]
    pts = []
    for i, hh in enumerate(heights):
        if i == correct_index:
            # on the vertical through the pivot, at height hh above the ramp (measured along the normal)
            # pivot vertical: x = px. point = px + t*ux + hh*vx  ->  t = -hh*vx/ux
            t = -hh * vx / ux
            x, y = px + t * ux + hh * vx, py + t * uy + hh * vy
        else:
            t = w * 0.5 + (0.35 if i % 2 else -0.15)
            x, y = px + t * ux + hh * vx, py + t * uy + hh * vy
        pts.append((x, y))
        ax.plot([x], [y], "o", color="black", ms=5)
        ax.text(x + 0.9, y + 0.55 + 0.1 * i, letters[i], ha="left", va="center", fontsize=11, fontweight="bold")
        ax.plot([x + 0.08, x + 0.85], [y + 0.05, y + 0.5 + 0.1 * i], color="black", lw=0.8)
    ax.text(px + 2.6 * ux + 0.3, py + 2.6 * uy, "ramp", ha="left", va="center", fontsize=10)
    ax.text(5.0, py - 2.2 * uy - 0.05, " ground", ha="left", va="center", fontsize=10)
    ax.set_xlim(-1.2, 6.4)
    ax.set_ylim(py - 2.2 * uy - 0.6, py + h * vy + w * uy + 0.6)
    return _png(fig)


# ------------------------------------------------------------------ Ch 6 energy
def stairs(h_label="5.0 m", steps=6):
    """A flight of stairs with the vertical height marked."""
    fig, ax = _fig(4.8, 3.0)
    x, y = 0.0, 0.0
    xs, ys = [x], [y]
    for _ in range(steps):
        x += 0.6
        xs.append(x); ys.append(y)
        y += 0.42
        xs.append(x); ys.append(y)
    ax.plot(xs, ys, color="black", lw=1.8)
    ax.plot([0, x + 0.4], [0, 0], color="black", lw=1.4)
    ax.plot([x, x + 0.4], [y, y], color="black", lw=1.8)
    _arrow(ax, (x + 0.9, 0), (x + 0.9, y), arrowstyle="<|-|>")
    ax.text(x + 1.05, y / 2, h_label, ha="left", va="center", fontsize=10.5)
    ax.text(x / 2, -0.3, "flight of stairs", ha="center", va="top", fontsize=10)
    ax.set_xlim(-0.3, x + 2.4)
    ax.set_ylim(-0.7, y + 0.5)
    return _png(fig)


# ------------------------------------------------------------------ Ch 7-8 thermal
def beaker_xy(top_label="X", bottom_label="Y"):
    """Beaker of water with a point near the top on one side and a point near the bottom on the other."""
    fig, ax = _fig(3.6, 3.4)
    ax.add_patch(Rectangle((0, 0), 3.0, 3.0, fc="#dddddd", ec="none"))
    ax.plot([0, 0, 3.0, 3.0], [3.3, 0, 0, 3.3], color="black", lw=1.8)
    ax.plot([0, 3.0], [3.0, 3.0], color="black", lw=1.0)
    ax.text(0.15, 2.75, top_label, ha="left", va="center", fontsize=11, fontweight="bold")
    ax.text(2.85, 0.25, bottom_label, ha="right", va="center", fontsize=11, fontweight="bold")
    ax.text(3.2, 2.9, "water", ha="left", va="center", fontsize=10)
    ax.plot([3.0, 3.15], [2.8, 2.9], color="black", lw=0.8)
    ax.set_xlim(-0.3, 4.3)
    ax.set_ylim(-0.3, 3.6)
    return _png(fig)


def state_arrows(letters=("P", "Q", "R", "S")):
    """solid -> liquid -> gas boxes with four labelled arrows: letters[0] solid->liquid, [1] liquid->gas, [2] liquid->solid, [3] gas->liquid."""
    fig, ax = _fig(6.4, 1.8)
    for x, name in ((0, "solid"), (2.4, "liquid"), (4.8, "gas")):
        ax.add_patch(Rectangle((x, 0), 1.4, 0.9, fc="white", ec="black", lw=1.6))
        ax.text(x + 0.7, 0.45, name, ha="center", va="center", fontsize=11)
    for x0, (up, down) in ((1.4, (letters[0], letters[2])), (3.8, (letters[1], letters[3]))):
        _arrow(ax, (x0 + 0.1, 0.62), (x0 + 0.9, 0.62))
        _arrow(ax, (x0 + 0.9, 0.28), (x0 + 0.1, 0.28))
        ax.text(x0 + 0.5, 0.95, up, ha="center", va="bottom", fontsize=11, fontweight="bold")
        ax.text(x0 + 0.5, -0.05, down, ha="center", va="top", fontsize=11, fontweight="bold")
    ax.set_xlim(-0.2, 6.4)
    ax.set_ylim(-0.5, 1.4)
    return _png(fig)


# ------------------------------------------------------------------ Ch 10 waves
def two_traces(f_ratio=1.5, a_ratio=1.6, names=("P", "Q")):
    """Two displacement-time traces on identical grids: the first has f_ratio times the frequency and a_ratio times the amplitude."""
    fig, ax = _fig(6.6, 2.8)
    for k, (x0, f, a) in enumerate(((0.0, f_ratio, a_ratio), (3.6, 1.0, 1.0))):
        for gx in np.arange(0, 2.81, 0.4):
            ax.plot([x0 + gx, x0 + gx], [-1.0, 1.0], color="#999999", lw=0.6)
        for gy in np.arange(-1.0, 1.01, 0.4):
            ax.plot([x0, x0 + 2.8], [gy, gy], color="#999999", lw=0.6)
        _arrow(ax, (x0, -1.0), (x0, 1.25), mutation_scale=9, lw=1.2)
        _arrow(ax, (x0, -1.0), (x0 + 3.05, -1.0), mutation_scale=9, lw=1.2)
        t = np.linspace(0, 2.8, 400)
        ax.plot(x0 + t, 0.55 * a * np.sin(2 * math.pi * f * t / 1.4), color="black", lw=1.8)
        ax.text(x0 + 1.4, 1.35, f"wave {names[k]}", ha="center", va="bottom", fontsize=10.5)
        ax.text(x0 - 0.1, 1.05, "displacement", ha="right", va="center", fontsize=8.5)
        ax.text(x0 + 2.8, -1.25, "time", ha="right", va="top", fontsize=9)
    ax.set_xlim(-1.4, 6.8)
    ax.set_ylim(-1.6, 1.8)
    return _png(fig)


# ------------------------------------------------------------------ Ch 12 light
def mirror_points(front_label="R", behind_label="P"):
    """A lamp in front of a plane mirror with a ray to the mirror; one marked point behind the mirror level with the lamp (the image
    position) and one in front, below the lamp."""
    fig, ax = _fig(5.2, 3.6)
    ax.plot([2.6, 2.6], [0, 3.4], color="black", lw=2.2)
    for y in np.arange(0.1, 3.4, 0.25):
        ax.plot([2.6, 2.85], [y, y + 0.22], color="black", lw=0.8)
    lx, ly = 0.6, 2.9
    ax.add_patch(Circle((lx, ly), 0.17, fc="white", ec="black", lw=1.4))
    ax.plot([lx - 0.12, lx + 0.12], [ly - 0.12, ly + 0.12], color="black", lw=1.0)
    ax.plot([lx - 0.12, lx + 0.12], [ly + 0.12, ly - 0.12], color="black", lw=1.0)
    ax.text(lx, ly + 0.3, "lamp", ha="center", va="bottom", fontsize=10)
    _arrow(ax, (lx + 0.15, ly - 0.12), (2.6, 1.6))
    ax.plot([4.6], [ly], "o", color="black", ms=5)
    ax.text(4.8, ly, behind_label, ha="left", va="center", fontsize=11, fontweight="bold")
    ax.plot([lx], [0.6], "o", color="black", ms=5)
    ax.text(lx - 0.2, 0.6, front_label, ha="right", va="center", fontsize=11, fontweight="bold")
    ax.set_xlim(-0.4, 5.6)
    ax.set_ylim(-0.2, 3.7)
    return _png(fig)


def prism_beam(entry="short", c_label="42°"):
    """A 45-90-45 glass prism with a narrow beam arriving normally at one short face (entry='short'), so it meets the long face at 45°."""
    fig, ax = _fig(4.6, 3.8)
    pts = [(0, 0), (3.0, 0), (0, 3.0)]
    ax.add_patch(Polygon(pts, closed=True, fc="#dfe8f3", ec="black", lw=1.8))
    ax.add_patch(Rectangle((0, 0), 0.25, 0.25, fc="none", ec="black", lw=1.0))
    ax.text(0.45, 2.3, "45°", ha="left", va="center", fontsize=9.5)
    ax.text(2.1, 0.15, "45°", ha="left", va="bottom", fontsize=9.5)
    _arrow(ax, (-1.6, 1.5), (0, 1.5))
    ax.text(-1.6, 1.65, "beam", ha="left", va="bottom", fontsize=10)
    ax.text(3.3, 1.6, f"critical angle of glass = {c_label}", ha="left", va="center", fontsize=9.5)
    ax.set_xlim(-1.9, 7.4)
    ax.set_ylim(-0.4, 3.4)
    return _png(fig)


# ------------------------------------------------------------------ Ch 17-18 magnetism
def three_bars(poles=(("N", "S"), ("N", "S")), names=("X", "Y", "Z")):
    """Two bar magnets and a bar of soft iron in a line (the iron bar is unlabelled)."""
    fig, ax = _fig(6.6, 1.6)
    for k, x in enumerate((0.0, 2.3, 4.6)):
        ax.add_patch(Rectangle((x, 0), 1.7, 0.5, fc="white", ec="black", lw=1.6))
        ax.text(x + 0.85, 0.85, names[k], ha="center", va="bottom", fontsize=11)
        if k < 2:
            ax.text(x + 0.1, 0.25, poles[k][0], ha="left", va="center", fontsize=11)
            ax.text(x + 1.6, 0.25, poles[k][1], ha="right", va="center", fontsize=11)
    ax.text(5.45, -0.15, "soft iron", ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-0.3, 6.6)
    ax.set_ylim(-0.6, 1.4)
    return _png(fig)


def two_wires_section(opposite=True):
    """Cross-section of two parallel straight wires: current into the page (cross) on the left and, if opposite, out of the page (dot)
    on the right, with a small arrow showing the field direction of each wire midway between them."""
    fig, ax = _fig(5.0, 2.4)
    for x, out in ((-1.2, False), (1.2, opposite)):
        ax.add_patch(Circle((x, 0), 0.28, fc="#dddddd", ec="black", lw=1.5))
        if out:
            ax.plot([x], [0], "o", color="black", ms=5)
        else:
            ax.plot([x - 0.15, x + 0.15], [-0.15, 0.15], color="black", lw=1.4)
            ax.plot([x - 0.15, x + 0.15], [0.15, -0.15], color="black", lw=1.4)
    ax.text(-1.2, -0.5, "wire 1", ha="center", va="top", fontsize=10)
    ax.text(1.2, -0.5, "wire 2", ha="center", va="top", fontsize=10)
    ax.add_patch(Circle((3.0, 0.75), 0.16, fc="#dddddd", ec="black", lw=1.2))
    ax.plot([2.9, 3.1], [0.65, 0.85], color="black", lw=1.1); ax.plot([2.9, 3.1], [0.85, 0.65], color="black", lw=1.1)
    ax.text(3.3, 0.75, "current into the page", ha="left", va="center", fontsize=9)
    ax.add_patch(Circle((3.0, 0.15), 0.16, fc="#dddddd", ec="black", lw=1.2))
    ax.plot([3.0], [0.15], "o", color="black", ms=3.5)
    ax.text(3.3, 0.15, "current out of the page", ha="left", va="center", fontsize=9)
    ax.set_xlim(-1.8, 6.4)
    ax.set_ylim(-1.0, 1.2)
    return _png(fig)


# ------------------------------------------------------------------ Ch 20 radioactivity
def beam_in_field(curve_up=True):
    """Shaded region of magnetic field into the page (crosses); an incident beam from the left splits into a straight path and
    one curved path."""
    fig, ax = _fig(5.6, 3.0)
    ax.add_patch(Rectangle((0, -1.2), 4.4, 2.4, fc="#dddddd", ec="none"))
    for x in np.arange(0.4, 4.4, 0.6):
        for y in np.arange(-0.9, 1.2, 0.6):
            ax.text(x, y, "×", ha="center", va="center", fontsize=11)
    _arrow(ax, (-1.6, 0), (0.6, 0))
    ax.text(-1.6, 0.15, "incident beam", ha="left", va="bottom", fontsize=10)
    _arrow(ax, (0.6, 0), (3.2, 0), arrowstyle="-|>")
    ax.plot([3.1, 4.4], [0, 0], color="black", lw=1.6)
    t = np.linspace(0, 1, 100)
    sgn = 1 if curve_up else -1
    xs, ys = 0.6 + 3.0 * t, sgn * 1.5 * t ** 2
    keep = np.abs(ys) <= 1.2
    ax.plot(xs[keep], ys[keep], color="black", lw=1.6)
    ax.text(4.5, -1.15, "vacuum", ha="left", va="bottom", fontsize=9)
    ax.text(4.5, 0.9, "magnetic field\ninto the page", ha="left", va="center", fontsize=9)
    ax.set_xlim(-1.8, 6.6)
    ax.set_ylim(-1.5, 1.6)
    return _png(fig)
