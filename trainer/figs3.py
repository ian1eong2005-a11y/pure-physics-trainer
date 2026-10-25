"""Diagram drawers for 6091 chapters 13-20: electric fields and charging, circuits (series, parallel, potential dividers),
I-V graphs, mains plug, magnets and fields, electromagnetism (wire, solenoid, Fleming's left-hand rule, motor),
induction (magnet and coil, a.c. output, transformer) and radioactivity (atom, nuclide, decay curve, penetration).
Every drawing is computed from the numbers in the question. PNG bytes, DPI 170."""
import io
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

from .figs import DPI, _fig, _png


def _arrow(ax, p0, p1, lw=1.6, ms=12, color="black", ls="-"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color, ls=ls, shrinkA=0, shrinkB=0))


def _dim(ax, p0, p1, text, offset=0.3, fontsize=10):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black", shrinkA=0, shrinkB=0))
    ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + offset, text, ha="center", va="bottom", fontsize=fontsize, bbox=dict(fc="white", ec="none", pad=1))


# ================================================================== Ch 13 static electricity
def _charge(ax, x, y, sign, r=0.32):
    ax.add_patch(Circle((x, y), r, fc="white", ec="black", lw=1.6, zorder=5))
    ax.text(x, y, sign, ha="center", va="center", fontsize=13, fontweight="bold", zorder=6)


def point_charge_field(sign="+", n=8):
    """Radial field lines of an isolated point charge; arrows point away from + and towards −."""
    fig, ax = _fig(3.6, 3.6)
    for k in range(n):
        a = 2 * math.pi * k / n
        p_in, p_out = (0.45 * math.cos(a), 0.45 * math.sin(a)), (1.7 * math.cos(a), 1.7 * math.sin(a))
        if sign == "+":
            _arrow(ax, p_in, p_out)
        else:
            _arrow(ax, p_out, p_in)
    _charge(ax, 0, 0, sign)
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)
    return _png(fig)


def _trace(ax, start, charges, step=0.04, nmax=400, reverse=False):
    p = np.array(start, dtype=float)
    pts = [p.copy()]
    for _ in range(nmax):
        E = np.zeros(2)
        for (cx, cy, q) in charges:
            d = p - np.array([cx, cy])
            r = np.hypot(*d)
            if r < 0.3:
                pts.append(np.array([cx, cy]) + d / r * 0.32)
                return np.array(pts)
            E += q * d / r ** 3
        n = np.hypot(*E)
        if n == 0:
            break
        p = p + (-1 if reverse else 1) * step * E / n
        pts.append(p.copy())
        if abs(p[0]) > 3.2 or abs(p[1]) > 2.4:
            break
    return np.array(pts)


def two_charges_field(signs=("+", "-"), n=10):
    """Field pattern between two point charges (unlike: lines run from + to −; like: lines repel)."""
    fig, ax = _fig(5.6, 3.8)
    q1 = 1 if signs[0] == "+" else -1
    q2 = 1 if signs[1] == "+" else -1
    charges = [(-1.3, 0, q1), (1.3, 0, q2)]
    for (cx, cy, q) in charges:
        for k in range(n):
            a = 2 * math.pi * (k + 0.5) / n
            start = (cx + 0.34 * math.cos(a), cy + 0.34 * math.sin(a))
            line = _trace(ax, start, charges, reverse=(q < 0))
            if len(line) < 4:
                continue
            ax.plot(line[:, 0], line[:, 1], color="black", lw=1.1, zorder=2)
            m = len(line) // 2
            if q > 0 or (q1 < 0 and q2 < 0):
                a0, a1 = line[m - 1], line[m + 1]
            else:
                a0, a1 = line[m + 1], line[m - 1]
            if q1 < 0 and q2 < 0:
                a0, a1 = a1, a0
            _arrow(ax, tuple(a0), tuple(a1), lw=0.1, ms=10)
    for (cx, cy, q) in charges:
        _charge(ax, cx, cy, "+" if q > 0 else "−")
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-2.3, 2.3)
    return _png(fig)


def induction_spheres(stage=1, rod_sign="-"):
    """Charging two touching metal spheres by induction. stage 1: charged rod brought near; 2: spheres separated with rod present;
    3: rod removed, spheres oppositely charged."""
    fig, ax = _fig(5.6, 2.8)
    gap = 0.0 if stage == 1 else 0.9
    xa, xb = -0.6 - gap / 2, 0.6 + gap / 2
    for x, lab in ((xa, "A"), (xb, "B")):
        ax.add_patch(Circle((x, 0), 0.6, fc="#eeeeee", ec="black", lw=1.6))
        ax.text(x, -0.95, lab, ha="center", va="top", fontsize=11, fontweight="bold")
        ax.add_patch(Rectangle((x - 0.05, -1.5), 0.1, 0.95, fc="white", ec="black", lw=1.0))   # insulating stand
    near, far = ("+", "−") if rod_sign == "-" else ("−", "+")
    if stage in (1, 2, 3):
        for dy in (-0.25, 0.0, 0.25):
            ax.text(xa - 0.42, dy, near, ha="center", va="center", fontsize=11, fontweight="bold")
            ax.text(xb + 0.42, dy, far, ha="center", va="center", fontsize=11, fontweight="bold")
    if stage < 3:
        ax.add_patch(Rectangle((-3.4, -0.18), 1.9, 0.36, fc="#cccccc", ec="black", lw=1.4))
        for xx in np.linspace(-3.2, -1.7, 5):
            ax.text(xx, 0, rod_sign if rod_sign == "+" else "−", ha="center", va="center", fontsize=11, fontweight="bold")
        ax.text(-2.45, 0.45, "charged rod", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-3.7, 2.6)
    ax.set_ylim(-1.8, 1.3)
    return _png(fig)


def precipitator():
    fig, ax = _fig(4.6, 3.6)
    ax.add_patch(Rectangle((0, 0), 3.0, 3.6, fc="#f4f4f4", ec="black", lw=1.6))
    ax.plot([0.15, 0.15], [0.2, 3.4], color="black", lw=4)
    ax.plot([2.85, 2.85], [0.2, 3.4], color="black", lw=4)
    ax.text(-0.1, 1.8, "+", ha="right", va="center", fontsize=14, fontweight="bold")
    ax.text(3.1, 1.8, "+", ha="left", va="center", fontsize=14, fontweight="bold")
    ax.plot([1.5, 1.5], [0.3, 3.3], color="black", lw=1.8)
    ax.text(1.5, 3.4, "− wire (high voltage)", ha="center", va="bottom", fontsize=8.5)
    ax.text(-0.1, 2.6, "+ plate", ha="right", va="center", fontsize=8.5)
    _arrow(ax, (1.5, -0.5), (1.5, -0.05))
    ax.text(1.5, -0.6, "dirty smoke in", ha="center", va="top", fontsize=9)
    for x, y in ((0.8, 0.6), (2.1, 0.9), (1.1, 1.4), (1.9, 1.9), (0.7, 2.4), (2.2, 2.7)):
        ax.plot([x], [y], "o", color="#555555", ms=4)
    ax.set_xlim(-1.3, 4.6)
    ax.set_ylim(-1.1, 4.1)
    return _png(fig)


# ================================================================== Ch 14-15 circuits
def _sym(ax, kind, x, y, label=None, horiz=True, size=0.8):
    """Draw one circuit symbol centred at (x, y) on a wire (which should already be drawn through the point)."""
    w, h = (size, 0.36) if horiz else (0.36, size)
    if kind in ("R", "fuse"):
        ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc="white", ec="black", lw=1.5, zorder=4))
        if kind == "fuse":
            ax.plot([x - w / 2, x + w / 2], [y, y], color="black", lw=1.2, zorder=5)
    elif kind == "varR":
        ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc="white", ec="black", lw=1.5, zorder=4))
        _arrow(ax, (x - 0.5, y - 0.4), (x + 0.5, y + 0.4), lw=1.3, ms=10)
    elif kind == "LDR":
        ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc="white", ec="black", lw=1.5, zorder=4))
        ax.add_patch(Circle((x, y), 0.5, fc="none", ec="black", lw=1.0, zorder=3))
        for dx in (-0.15, 0.1):
            _arrow(ax, (x + dx - 0.35, y + 0.95), (x + dx - 0.05, y + 0.55), lw=1.1, ms=8)
    elif kind == "therm":
        ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc="white", ec="black", lw=1.5, zorder=4))
        ax.plot([x - 0.5, x - 0.3, x + 0.4], [y - 0.5, y - 0.5, y + 0.45], color="black", lw=1.3, zorder=5)
    elif kind in ("lamp", "A", "V", "G"):
        ax.add_patch(Circle((x, y), 0.26, fc="white", ec="black", lw=1.5, zorder=4))
        if kind == "lamp":
            d = 0.26 / math.sqrt(2)
            ax.plot([x - d, x + d], [y - d, y + d], color="black", lw=1.3, zorder=5)
            ax.plot([x - d, x + d], [y + d, y - d], color="black", lw=1.3, zorder=5)
        else:
            ax.text(x, y, kind, ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)
    elif kind == "switch":
        ax.add_patch(Rectangle((x - 0.42, y - 0.08), 0.84, 0.16, fc="white", ec="none", zorder=4))
        ax.plot([x - 0.4], [y], "o", color="black", ms=4, zorder=5)
        ax.plot([x + 0.4], [y], "o", color="black", ms=4, zorder=5)
        ax.plot([x - 0.4, x + 0.3], [y, y + 0.35], color="black", lw=1.5, zorder=5)
    elif kind == "switch_closed":
        ax.plot([x - 0.4], [y], "o", color="black", ms=4, zorder=5)
        ax.plot([x + 0.4], [y], "o", color="black", ms=4, zorder=5)
    elif kind == "diode":
        ax.add_patch(Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, fc="white", ec="none", zorder=4))
        ax.add_patch(Polygon([(x - 0.25, y - 0.25), (x - 0.25, y + 0.25), (x + 0.2, y)], fc="white", ec="black", lw=1.4, zorder=5))
        ax.plot([x + 0.2, x + 0.2], [y - 0.25, y + 0.25], color="black", lw=1.6, zorder=5)
        ax.plot([x - 0.3, x - 0.25], [y, y], color="black", lw=1.2, zorder=5)
    elif kind == "LED":
        ax.add_patch(Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, fc="white", ec="none", zorder=4))
        ax.add_patch(Polygon([(x - 0.25, y - 0.25), (x - 0.25, y + 0.25), (x + 0.2, y)], fc="white", ec="black", lw=1.4, zorder=5))
        ax.plot([x + 0.2, x + 0.2], [y - 0.25, y + 0.25], color="black", lw=1.6, zorder=5)
        for dx in (-0.1, 0.15):
            _arrow(ax, (x + dx, y + 0.3), (x + dx + 0.25, y + 0.65), lw=1.0, ms=7)
    elif kind == "cell":
        ax.add_patch(Rectangle((x - 0.22, y - 0.5), 0.44, 1.0, fc="white", ec="none", zorder=4))
        ax.plot([x - 0.08, x - 0.08], [y - 0.45, y + 0.45], color="black", lw=2.2, zorder=5)   # long = positive
        ax.plot([x + 0.08, x + 0.08], [y - 0.22, y + 0.22], color="black", lw=4.0, zorder=5)
    if label:
        if kind in ("V", "A", "G", "lamp"):
            ax.text(x, y + 0.42 if horiz else y, label, ha="center" if horiz else "left", va="bottom" if horiz else "center", fontsize=9.5)
        elif horiz:
            ax.text(x, y + 0.3, label, ha="center", va="bottom", fontsize=9.5)
        else:
            ax.text(x + (0.6 if kind in ("LDR", "therm") else 0.3), y, label, ha="left", va="center", fontsize=9.5)


def circuit(top=(), bottom=(), branches=None, emf="6.0 V", left_kind="cell", volt_across=None, right=(), width=6.0, height=3.0, branch_gap=1.0):
    """Schematic circuit on a rectangular loop.
    top / bottom / right: sequences of (kind, label) placed along that edge (top runs left to right).
    branches: list of sequences of (kind, label): a parallel section in the middle of the top edge, one row per branch
              (the first row sits ON the top edge, the next ones hang below it, inside the loop).
    volt_across: index into `top` of the component a voltmeter is connected across (label 'V'), or ('b', i, j) for branch i comp j.
    The cell (left edge) has the long plate on top: conventional current leaves the top terminal and flows clockwise."""
    fig, ax = _fig(width + 1.6, height + 1.9)
    W, H = width, height
    ax.plot([0, W, W, 0, 0], [0, 0, H, H, 0], color="black", lw=1.5, zorder=1)
    # left edge: source
    if left_kind == "cell":
        ax.plot([-0.5, 0.5], [H / 2 + 0.08, H / 2 + 0.08], color="black", lw=2.2, zorder=5)
        ax.plot([-0.25, 0.25], [H / 2 - 0.08, H / 2 - 0.08], color="black", lw=4.0, zorder=5)
        ax.add_patch(Rectangle((-0.1, H / 2 - 0.06), 0.2, 0.12, fc="white", ec="none", zorder=4))
        ax.text(-0.65, H / 2, emf, ha="right", va="center", fontsize=10)
    elif left_kind == "battery":
        for k, dy in enumerate((-0.35, 0.0, 0.35)):
            ax.plot([-0.45, 0.45], [H / 2 + dy + 0.08, H / 2 + dy + 0.08], color="black", lw=2.0, zorder=5)
            ax.plot([-0.22, 0.22], [H / 2 + dy - 0.08, H / 2 + dy - 0.08], color="black", lw=3.5, zorder=5)
        ax.add_patch(Rectangle((-0.1, H / 2 - 0.5), 0.2, 1.0, fc="white", ec="none", zorder=4))
        ax.text(-0.65, H / 2, emf, ha="right", va="center", fontsize=10)
    elif left_kind == "ac":
        ax.add_patch(Circle((0, H / 2), 0.32, fc="white", ec="black", lw=1.5, zorder=4))
        xs = np.linspace(-0.2, 0.2, 30)
        ax.plot(xs, H / 2 + 0.12 * np.sin(xs / 0.2 * math.pi), color="black", lw=1.3, zorder=5)
        ax.text(-0.5, H / 2, emf, ha="right", va="center", fontsize=10)
    # top edge
    n_top = len(top)
    if branches:
        xa, xb = W * 0.3, W * 0.7
        left_items = list(top)
        xs = np.linspace(0.6, xa - 0.6, n_top + 2)[1:-1] if n_top else []
        for (kind, label), x in zip(left_items, xs):
            _sym(ax, kind, x, H, label)
        for bi, br in enumerate(branches):
            y = H - bi * branch_gap
            if bi:
                ax.plot([xa, xa], [y, H], color="black", lw=1.5, zorder=1)
                ax.plot([xb, xb], [y, H], color="black", lw=1.5, zorder=1)
                ax.plot([xa, xb], [y, y], color="black", lw=1.5, zorder=1)
            ax.plot([xa], [H], "o", color="black", ms=4, zorder=3)
            ax.plot([xb], [H], "o", color="black", ms=4, zorder=3)
            bxs = np.linspace(xa, xb, len(br) + 2)[1:-1]
            for (kind, label), x in zip(br, bxs):
                _sym(ax, kind, x, y, label)
                if volt_across == ("b", bi, list(br).index((kind, label))):
                    _volt(ax, x, y, up=(bi == 0))
    else:
        xs = np.linspace(0, W, n_top + 2)[1:-1]
        for i, ((kind, label), x) in enumerate(zip(top, xs)):
            _sym(ax, kind, x, H, label)
            if volt_across == i:
                _volt(ax, x, H, up=True)
    # bottom edge (runs right to left for current, but we just place symbols)
    xs = np.linspace(0, W, len(bottom) + 2)[1:-1]
    for (kind, label), x in zip(bottom, xs):
        _sym(ax, kind, x, 0, label)
    ys = np.linspace(0, H, len(right) + 2)[1:-1]
    for (kind, label), y in zip(right, ys):
        _sym(ax, kind, W, y, label, horiz=False)
    ax.set_xlim(-1.6, W + 1.2)
    ax.set_ylim(-0.9, H + 1.4)
    return _png(fig)


def _volt(ax, x, y, up=True):
    dy = 0.9 if up else -0.9
    ax.plot([x - 0.55, x - 0.55, x + 0.55, x + 0.55], [y, y + dy, y + dy, y], color="black", lw=1.3, zorder=1)
    ax.plot([x - 0.55], [y], "o", color="black", ms=4, zorder=3)
    ax.plot([x + 0.55], [y], "o", color="black", ms=4, zorder=3)
    _sym(ax, "V", x, y + dy)


def potential_divider(vin="6.0 V", r1="R₁", r2="R₂", out_label="V out", top_kind="R", bottom_kind="R"):
    """Two components in series across a supply, output taken across the lower one."""
    fig, ax = _fig(4.6, 3.6)
    ax.plot([0, 2.0, 2.0, 0, 0], [0, 0, 4.0, 4.0, 0], color="black", lw=1.5)
    ax.plot([-0.5, 0.5], [2.08, 2.08], color="black", lw=2.2, zorder=5)
    ax.plot([-0.25, 0.25], [1.92, 1.92], color="black", lw=4.0, zorder=5)
    ax.add_patch(Rectangle((-0.1, 1.94), 0.2, 0.12, fc="white", ec="none", zorder=4))
    ax.text(-0.65, 2.0, vin, ha="right", va="center", fontsize=10)
    _sym(ax, top_kind, 2.0, 3.0, r1, horiz=False)
    _sym(ax, bottom_kind, 2.0, 1.0, r2, horiz=False)
    ax.plot([2.0, 3.2], [2.0, 2.0], color="black", lw=1.3)
    ax.plot([2.0, 3.2], [0.0, 0.0], color="black", lw=1.3)
    ax.plot([2.0], [2.0], "o", color="black", ms=4, zorder=3)
    ax.plot([3.2], [2.0], "o", color="black", ms=4)
    ax.plot([3.2], [0.0], "o", color="black", ms=4)
    _dim(ax, (3.5, 0.0), (3.5, 2.0), "", offset=0)
    ax.text(3.65, 1.0, out_label, ha="left", va="center", fontsize=10)
    ax.set_xlim(-1.7, 5.0)
    ax.set_ylim(-0.6, 4.6)
    return _png(fig)


def iv_graph(kind="ohmic", R=None, vmax=6.0, imax=None, labels=None):
    """I-V characteristic through the origin for an ohmic conductor (R ohms), a filament lamp or a semiconductor diode."""
    fig, ax = plt.subplots(figsize=(4.4, 3.4), dpi=DPI)
    v = np.linspace(-vmax, vmax, 400)
    if kind == "ohmic":
        R = R or 2.0
        i = v / R
    elif kind == "lamp":
        i = np.sign(v) * (np.abs(v) ** 0.6) * (vmax ** 0.4 / R if R else 1.0)
    else:
        i = np.where(v > 0.6, (v - 0.6) * 1.2, 0.0)
    ax.plot(v, i, color="black", lw=2.0)
    ax.axhline(0, color="black", lw=1.0)
    ax.axvline(0, color="black", lw=1.0)
    imax = imax or max(abs(i)) * 1.15
    ax.set_xlim(-vmax * 1.1, vmax * 1.1)
    ax.set_ylim(-imax, imax)
    ax.set_xlabel("p.d. / V", fontsize=10)
    ax.set_ylabel("current / A", fontsize=10)
    ax.xaxis.set_label_coords(0.93, 0.42)
    ax.yaxis.set_label_coords(0.40, 0.88)
    ax.grid(color="#cccccc", lw=0.5)
    ax.tick_params(labelsize=8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for (x, y, t) in (labels or []):
        ax.plot([x], [y], "o", color="black", ms=4)
        ax.text(x, y, " " + t, fontsize=10, fontweight="bold", va="bottom")
    return _png(fig)


def lhr_force(field="right", current="into"):
    """Direction of the force on the wire drawn by flemings_lhr(): 'up' or 'down' (F = I L × B)."""
    bx = 1 if field == "right" else -1
    iz = -1 if current == "into" else 1
    fy = iz * bx          # (0,0,iz) × (bx,0,0) = (0, iz*bx, 0)
    return "up" if fy > 0 else "down"


def wire_sketch(length_label, area_label, name="wire"):
    fig, ax = _fig(5.2, 1.9)
    ax.add_patch(Rectangle((0.3, 0.6), 4.0, 0.5, fc="#dddddd", ec="black", lw=1.5))
    ax.add_patch(Ellipse((4.3, 0.85), 0.25, 0.5, fc="#bbbbbb", ec="black", lw=1.5))
    _dim(ax, (0.3, 0.2), (4.3, 0.2), "", offset=0)
    ax.text(2.3, -0.05, length_label, ha="center", va="top", fontsize=10)
    ax.text(4.55, 0.85, area_label, ha="left", va="center", fontsize=10)
    ax.text(0.3, 1.3, name, ha="left", va="bottom", fontsize=10)
    ax.set_xlim(0, 6.6)
    ax.set_ylim(-0.6, 1.8)
    return _png(fig)


# ================================================================== Ch 16 practical electricity
def plug_wiring(fault=None):
    """Three-pin plug: E top, L bottom right (with fuse), N bottom left. fault: 'LN_swapped' | 'no_earth' | 'fuse_neutral'."""
    fig, ax = _fig(5.0, 4.2)
    ax.add_patch(FancyBboxPatch((0, 0), 5.0, 4.4, boxstyle="round,pad=0.02,rounding_size=0.3", fc="#f7f7f7", ec="black", lw=1.6))
    ax.add_patch(Rectangle((2.3, 3.5), 0.4, 0.8, fc="#bbbbbb", ec="black", lw=1.2))     # earth pin
    ax.add_patch(Rectangle((0.6, 1.4), 0.4, 0.7, fc="#bbbbbb", ec="black", lw=1.2))     # neutral pin (left)
    ax.add_patch(Rectangle((4.0, 1.4), 0.4, 0.7, fc="#bbbbbb", ec="black", lw=1.2))     # live pin (right)
    ax.add_patch(Rectangle((3.6, 2.4), 1.2, 0.4, fc="white", ec="black", lw=1.4))       # fuse
    ax.text(4.2, 2.6, "fuse", ha="center", va="center", fontsize=8)
    ax.add_patch(Rectangle((2.2, -0.6), 0.6, 0.8, fc="#dddddd", ec="black", lw=1.2))     # cable grip
    colours = {"E": ("#2e8b57", "green/yellow"), "N": ("#1f5fa6", "blue"), "L": ("#8b4513", "brown")}
    left, right = ("N", "L") if fault != "LN_swapped" else ("L", "N")
    if fault != "no_earth":
        ax.plot([2.5, 2.5], [0.2, 3.5], color=colours["E"][0], lw=3)
    ax.plot([2.4, 1.2, 0.8, 0.8], [0.2, 0.9, 1.0, 1.4], color=colours[left][0], lw=3)
    ax.plot([2.6, 3.9, 4.2, 4.2], [0.2, 1.2, 1.6, 2.4], color=colours[right][0], lw=3)
    ax.plot([4.2, 4.2], [2.1, 1.4], color=colours[right][0], lw=3)
    for x, y, t in ((2.5, 4.4, "E"), (0.8, 1.05, left), (4.2, 1.05, right)):
        ax.text(x, y, t, ha="center", va="bottom" if y > 4 else "top", fontsize=11, fontweight="bold")
    ax.set_xlim(-0.3, 5.3)
    ax.set_ylim(-0.9, 4.9)
    return _png(fig)


def rating_plate(lines):
    fig, ax = _fig(3.8, 2.0)
    ax.add_patch(Rectangle((0, 0), 3.6, 0.5 + 0.45 * len(lines), fc="#f0f0f0", ec="black", lw=1.4))
    for i, t in enumerate(lines):
        ax.text(0.2, 0.3 + 0.45 * (len(lines) - 1 - i), t, ha="left", va="center", fontsize=10, family="monospace")
    ax.set_xlim(-0.2, 3.8)
    ax.set_ylim(-0.2, 0.7 + 0.45 * len(lines))
    return _png(fig)


# ================================================================== Ch 17 magnetism
def _magnet(ax, x, y, w=2.4, h=0.7, flip=False, labels=True):
    n_fc, s_fc = "#d9534f", "#5b9bd5"
    left, right = ("S", "N") if flip else ("N", "S")
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w / 2, h, fc=n_fc if left == "N" else s_fc, ec="black", lw=1.5, zorder=3))
    ax.add_patch(Rectangle((x, y - h / 2), w / 2, h, fc=n_fc if right == "N" else s_fc, ec="black", lw=1.5, zorder=3))
    if labels:
        ax.text(x - w / 4, y, left, ha="center", va="center", fontsize=13, fontweight="bold", color="white", zorder=4)
        ax.text(x + w / 4, y, right, ha="center", va="center", fontsize=13, fontweight="bold", color="white", zorder=4)


def bar_magnet_field(flip=False):
    """Field lines around a bar magnet (closed loops from N to S outside the magnet)."""
    fig, ax = _fig(5.6, 3.6)
    _magnet(ax, 0, 0, flip=flip)
    sgn = -1 if flip else 1
    for a, b in ((1.5, 0.75), (2.1, 1.25), (2.8, 1.85)):
        t = np.linspace(0, 2 * math.pi, 300)
        xs, ys = a * np.cos(t), b * np.sin(t)
        ax.plot(xs, ys, color="black", lw=1.1, zorder=1)
    # arrows: outside the magnet the field runs from N to S (over the top from the N end towards the S end)
    for a, b in ((1.5, 0.75), (2.1, 1.25), (2.8, 1.85)):
        for yy in (b, -b):
            ax.add_patch(FancyArrowPatch((0.2 * sgn, yy), (0.6 * sgn, yy), arrowstyle="-|>", mutation_scale=10, lw=0.1, color="black"))
    ax.plot([-3.2, -1.3], [0, 0], color="black", lw=1.1)
    ax.plot([1.3, 3.2], [0, 0], color="black", lw=1.1)
    ax.add_patch(FancyArrowPatch((-2.2 * sgn if not flip else 2.2, 0), ((-2.6 if not flip else 2.6), 0), arrowstyle="-|>", mutation_scale=10, lw=0.1, color="black"))
    ax.add_patch(FancyArrowPatch(((2.6 if not flip else -2.6), 0), ((2.2 if not flip else -2.2), 0), arrowstyle="-|>", mutation_scale=10, lw=0.1, color="black"))
    ax.set_xlim(-3.4, 3.4)
    ax.set_ylim(-2.3, 2.3)
    return _png(fig)


def two_magnets(facing="NS", gap=1.2):
    """Two bar magnets end to end: facing 'NS' (unlike poles facing, attract) or 'NN' / 'SS' (like poles, repel)."""
    fig, ax = _fig(6.0, 2.6)
    left_flip = facing[0] == "N"       # _magnet draws N on the left by default; flip so the left magnet's RIGHT pole is facing[0]
    right_flip = facing[1] == "S"      # ... and the right magnet's LEFT pole is facing[1]
    _magnet(ax, -1.2 - gap / 2, 0, flip=left_flip)
    _magnet(ax, 1.2 + gap / 2, 0, flip=right_flip)
    if facing in ("NS", "SN"):
        for yy in (0.0, 0.3, -0.3):
            ax.plot([-gap / 2, gap / 2], [yy, yy], color="black", lw=1.0)
        ax.add_patch(FancyArrowPatch((-0.15 if facing == "NS" else 0.15, 0), (0.15 if facing == "NS" else -0.15, 0), arrowstyle="-|>", mutation_scale=10, lw=0.1, color="black"))
    else:
        for s in (1, -1):
            t = np.linspace(0.3, 1.4, 50)
            ax.plot(-gap / 2 + 0.05 - 0.35 * t ** 1.5, s * t * 0.8, color="black", lw=1.0)
            ax.plot(gap / 2 - 0.05 + 0.35 * t ** 1.5, s * t * 0.8, color="black", lw=1.0)
    ax.text(0, -1.0, "X", ha="center", va="top", fontsize=11, fontweight="bold")
    ax.set_xlim(-3.8 - gap / 2, 3.8 + gap / 2)
    ax.set_ylim(-1.6, 1.6)
    return _png(fig)


def compass_near_magnet(position="right", flip=False):
    """Bar magnet with a plotting compass at one of: right, left, above, below. The needle points along the field (away from N)."""
    fig, ax = _fig(5.4, 3.2)
    _magnet(ax, 0, 0, flip=flip)
    pos = {"right": (2.2, 0), "left": (-2.2, 0), "above": (0, 1.3), "below": (0, -1.3)}[position]
    # N on the left (default): the field leaves the N end heading left, loops over the top and bottom heading right, and enters the S end heading left
    nx = {"left": (-1, 0), "right": (-1, 0), "above": (1, 0), "below": (1, 0)}[position]
    if flip:
        nx = (-nx[0], -nx[1])
    ax.add_patch(Circle(pos, 0.45, fc="white", ec="black", lw=1.4, zorder=3))
    ax.add_patch(FancyArrowPatch((pos[0] - 0.3 * nx[0], pos[1] - 0.3 * nx[1]), (pos[0] + 0.32 * nx[0], pos[1] + 0.32 * nx[1]), arrowstyle="-|>", mutation_scale=12, lw=2.0, color="#d9534f", zorder=4))
    ax.text(pos[0], pos[1] - 0.65 if position != "below" else pos[1] + 0.55, "compass", ha="center", va="top" if position != "below" else "bottom", fontsize=9)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-2.1, 2.1)
    return _png(fig)


def induced_magnetism(material="iron"):
    """Bar magnet with an unmagnetised bar close to its N pole; the near end becomes S."""
    fig, ax = _fig(5.6, 2.2)
    _magnet(ax, -1.6, 0)
    ax.add_patch(Rectangle((0.3, -0.3), 2.2, 0.6, fc="#cccccc", ec="black", lw=1.5))
    ax.text(1.4, 0, material + " bar", ha="center", va="center", fontsize=10)
    ax.text(0.45, 0.5, "?", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.text(2.35, 0.5, "?", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.set_xlim(-3.2, 3.0)
    ax.set_ylim(-1.0, 1.3)
    return _png(fig)


# ================================================================== Ch 18 electromagnetism
def wire_field(current="out"):
    """Field around a straight wire seen end-on: current out of the page (dot) gives anticlockwise circles."""
    fig, ax = _fig(3.6, 3.6)
    for r in (0.6, 1.1, 1.6):
        ax.add_patch(Circle((0, 0), r, fc="none", ec="black", lw=1.1))
        if current == "out":
            _arrow(ax, (r * math.cos(0.05), -r * math.sin(0.05)), (r * math.cos(-0.05), -r * math.sin(-0.05)), lw=0.1, ms=10)   # at the right-hand side pointing up = anticlockwise
        else:
            _arrow(ax, (r * math.cos(-0.05), r * math.sin(-0.05)), (r * math.cos(0.05), r * math.sin(0.05)), lw=0.1, ms=10)
    ax.add_patch(Circle((0, 0), 0.22, fc="white", ec="black", lw=1.6, zorder=5))
    if current == "out":
        ax.plot([0], [0], "o", color="black", ms=6, zorder=6)
    else:
        ax.plot([-0.12, 0.12], [-0.12, 0.12], color="black", lw=1.6, zorder=6)
        ax.plot([-0.12, 0.12], [0.12, -0.12], color="black", lw=1.6, zorder=6)
    ax.text(0, -2.0, "current " + ("out of the page" if current == "out" else "into the page"), ha="center", va="top", fontsize=9)
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.4, 2.1)
    return _png(fig)


def solenoid(n_turns=8, current_left_to_right=True, show_field=True):
    """Solenoid in section with the current direction marked; field lines inside run along the axis."""
    fig, ax = _fig(6.0, 3.2)
    L = 4.0
    xs = np.linspace(-L / 2, L / 2, n_turns)
    for x in xs:
        ax.add_patch(Ellipse((x, 0), 0.5, 1.6, fc="none", ec="black", lw=1.3))
    ax.plot([-L / 2 - 1.0, -L / 2], [0.8, 0.8], color="black", lw=1.3)
    ax.plot([L / 2, L / 2 + 1.0], [-0.8, -0.8], color="black", lw=1.3)
    if current_left_to_right:
        _arrow(ax, (-L / 2 - 0.9, 0.8), (-L / 2 - 0.4, 0.8))
        ax.text(-L / 2 - 0.65, 1.0, "I", ha="center", va="bottom", fontsize=11, fontstyle="italic")
    else:
        _arrow(ax, (L / 2 + 0.9, -0.8), (L / 2 + 0.4, -0.8))
        ax.text(L / 2 + 0.65, -1.0, "I", ha="center", va="top", fontsize=11, fontstyle="italic")
    if show_field:
        for yy in (-0.35, 0.0, 0.35):
            ax.plot([-L / 2 - 0.3, L / 2 + 0.3], [yy, yy], color="#555555", lw=0.9, ls="--")
    ax.text(-L / 2 - 0.2, -1.3, "P", ha="center", va="top", fontsize=11, fontweight="bold")
    ax.text(L / 2 + 0.2, -1.3, "Q", ha="center", va="top", fontsize=11, fontweight="bold")
    ax.set_xlim(-L / 2 - 1.6, L / 2 + 1.6)
    ax.set_ylim(-1.8, 1.5)
    return _png(fig)


def flemings_lhr(field="right", current="into", show_force=False, force_dir=None):
    """Wire between the poles of a magnet. field: 'right' (N on the left) or 'left'. current: 'into' (cross) or 'out' (dot) of the page.
    force_dir: 'up' | 'down' drawn when show_force."""
    fig, ax = _fig(5.0, 3.4)
    left_is_N = field == "right"
    for x, lab in ((-2.0, "N" if left_is_N else "S"), (2.0, "S" if left_is_N else "N")):
        ax.add_patch(Rectangle((x - 0.5, -1.2), 1.0, 2.4, fc="#d9534f" if lab == "N" else "#5b9bd5", ec="black", lw=1.5))
        ax.text(x, 0, lab, ha="center", va="center", fontsize=14, fontweight="bold", color="white")
    for yy in (-0.7, 0.0, 0.7):
        if field == "right":
            _arrow(ax, (-1.45, yy), (1.45, yy), lw=1.1, ms=10)
        else:
            _arrow(ax, (1.45, yy), (-1.45, yy), lw=1.1, ms=10)
    ax.add_patch(Circle((0, 0), 0.28, fc="white", ec="black", lw=1.6, zorder=5))
    if current == "out":
        ax.plot([0], [0], "o", color="black", ms=7, zorder=6)
    else:
        ax.plot([-0.15, 0.15], [-0.15, 0.15], color="black", lw=1.8, zorder=6)
        ax.plot([-0.15, 0.15], [0.15, -0.15], color="black", lw=1.8, zorder=6)
    ax.text(0, -0.45, "wire", ha="center", va="top", fontsize=9)
    if show_force and force_dir:
        dy = 1.0 if force_dir == "up" else -1.0
        _arrow(ax, (0, 0.35 * dy), (0, 0.35 * dy + dy), lw=2.0, ms=14)
        ax.text(0.15, 0.35 * dy + dy, "F", ha="left", va="center", fontsize=11, fontweight="bold")
    ax.text(0, 1.55, "current " + ("into the page" if current == "into" else "out of the page"), ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-2.8, 2.8)
    ax.set_ylim(-1.7, 2.1)
    return _png(fig)


def motor_diagram():
    """Simple d.c. motor: coil ABCD between poles, split-ring commutator and brushes."""
    fig, ax = _fig(5.6, 3.8)
    for x, lab in ((-2.4, "N"), (2.4, "S")):
        ax.add_patch(Rectangle((x - 0.5, -1.3), 1.0, 2.6, fc="#d9534f" if lab == "N" else "#5b9bd5", ec="black", lw=1.5))
        ax.text(x, 0, lab, ha="center", va="center", fontsize=14, fontweight="bold", color="white")
    coil = [(-1.5, 0.9), (1.5, 0.9), (1.5, -0.9), (-1.5, -0.9), (-1.5, 0.9)]
    xs, ys = zip(*coil)
    ax.plot(xs, ys, color="black", lw=1.8)
    for (x, y, t) in ((-1.5, 0.9, "A"), (1.5, 0.9, "B"), (1.5, -0.9, "C"), (-1.5, -0.9, "D")):
        ax.text(x + (-0.2 if x < 0 else 0.2), y + (0.15 if y > 0 else -0.15), t, ha="center", va="center", fontsize=11, fontweight="bold")
    _arrow(ax, (-0.6, 0.9), (0.6, 0.9), lw=1.6, ms=12)
    _arrow(ax, (0.6, -0.9), (-0.6, -0.9), lw=1.6, ms=12)
    ax.add_patch(Arc((0, -2.2), 0.9, 0.9, theta1=100, theta2=260, lw=2.0))
    ax.add_patch(Arc((0, -2.2), 0.9, 0.9, theta1=-80, theta2=80, lw=2.0))
    ax.plot([-1.5, -0.1], [-0.9, -2.0], color="black", lw=1.0)
    ax.plot([1.5, 0.1], [-0.9, -2.0], color="black", lw=1.0)
    ax.add_patch(Rectangle((-0.95, -2.35), 0.3, 0.3, fc="#555555", ec="black", lw=1.0))
    ax.add_patch(Rectangle((0.65, -2.35), 0.3, 0.3, fc="#555555", ec="black", lw=1.0))
    ax.text(0, -2.8, "split-ring commutator and brushes", ha="center", va="top", fontsize=8.5)
    ax.plot([-1.6, -0.95], [-2.2, -2.2], color="black", lw=1.2)
    ax.plot([0.95, 1.6], [-2.2, -2.2], color="black", lw=1.2)
    ax.text(-1.7, -2.2, "+", ha="right", va="center", fontsize=12, fontweight="bold")
    ax.text(1.7, -2.2, "−", ha="left", va="center", fontsize=12, fontweight="bold")
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.4, 1.7)
    return _png(fig)


# ================================================================== Ch 19 electromagnetic induction
def magnet_into_coil(moving="in", pole="N"):
    """Bar magnet moved into / out of a coil connected to a centre-zero galvanometer."""
    fig, ax = _fig(5.8, 3.0)
    for x in np.linspace(0.8, 2.6, 6):
        ax.add_patch(Ellipse((x, 0), 0.4, 1.4, fc="none", ec="black", lw=1.3))
    ax.plot([0.8, 0.8, 1.7], [0.7, 1.6, 1.6], color="black", lw=1.2)
    ax.plot([2.6, 2.6, 1.7], [-0.7, 1.6, 1.6], color="black", lw=1.2)
    ax.plot([2.6, 2.6], [-0.7, 1.6], color="black", lw=1.2, alpha=0)
    ax.plot([2.6, 2.6], [-0.7, -1.3], color="black", lw=1.2)
    ax.plot([0.8, 0.8], [0.7, -1.3], color="black", lw=1.2)
    ax.plot([0.8, 2.6], [-1.3, -1.3], color="black", lw=1.2)
    _sym(ax, "G", 1.7, -1.3)
    _magnet(ax, -1.9, 0, w=2.0, h=0.6, flip=(pole == "S"))
    if moving == "in":
        _arrow(ax, (-0.7, 0.75), (0.3, 0.75), lw=1.8, ms=13)
        ax.text(-0.2, 0.9, "moved in", ha="center", va="bottom", fontsize=9)
    elif moving == "out":
        _arrow(ax, (0.3, 0.75), (-0.7, 0.75), lw=1.8, ms=13)
        ax.text(-0.2, 0.9, "moved out", ha="center", va="bottom", fontsize=9)
    else:
        ax.text(-0.2, 0.9, "held still", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-3.2, 3.4)
    ax.set_ylim(-1.9, 1.9)
    return _png(fig)


def ac_output(period=0.02, vpeak=6.0, cycles=2, label_points=None):
    """Voltage-time output of a simple a.c. generator (sinusoidal)."""
    fig, ax = plt.subplots(figsize=(4.8, 2.8), dpi=DPI)
    t = np.linspace(0, cycles * period, 400)
    ax.plot(t * 1000, vpeak * np.sin(2 * math.pi * t / period), color="black", lw=2.0)
    ax.axhline(0, color="black", lw=1.0)
    ax.set_xlim(0, cycles * period * 1000)
    ax.set_ylim(-vpeak * 1.4, vpeak * 1.4)
    ax.set_xlabel("time / ms", fontsize=10)
    ax.set_ylabel("e.m.f. / V", fontsize=10)
    ax.set_xticks(np.linspace(0, cycles * period * 1000, 2 * cycles + 1))
    ax.set_yticks([-vpeak, 0, vpeak])
    ax.grid(color="#cccccc", lw=0.5)
    ax.tick_params(labelsize=8.5)
    for (x, y, tt) in (label_points or []):
        ax.plot([x], [y], "o", color="black", ms=4)
        ax.text(x, y, " " + tt, fontsize=10, fontweight="bold", va="bottom")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def transformer(np_label="N₁ turns", ns_label="N₂ turns", vp_label="V₁", vs_label="V₂", n_p=6, n_s=12):
    fig, ax = _fig(5.6, 3.2)
    ax.add_patch(Rectangle((-1.5, -1.4), 3.0, 2.8, fc="#bbbbbb", ec="black", lw=1.6))
    ax.add_patch(Rectangle((-0.8, -0.7), 1.6, 1.4, fc="white", ec="black", lw=1.6))
    for k in range(min(n_p, 9)):
        y = -1.0 + 2.0 * (k + 0.5) / min(n_p, 9)
        ax.add_patch(Ellipse((-1.5, y), 0.55, 0.22, fc="none", ec="black", lw=1.4))
    for k in range(min(n_s, 12)):
        y = -1.0 + 2.0 * (k + 0.5) / min(n_s, 12)
        ax.add_patch(Ellipse((1.5, y), 0.55, 0.16, fc="none", ec="black", lw=1.4))
    ax.plot([-1.8, -2.6], [1.0, 1.0], color="black", lw=1.2)
    ax.plot([-1.8, -2.6], [-1.0, -1.0], color="black", lw=1.2)
    ax.plot([1.8, 2.6], [1.0, 1.0], color="black", lw=1.2)
    ax.plot([1.8, 2.6], [-1.0, -1.0], color="black", lw=1.2)
    ax.text(-2.7, 0, vp_label, ha="right", va="center", fontsize=10.5)
    ax.text(2.7, 0, vs_label, ha="left", va="center", fontsize=10.5)
    ax.text(-1.5, -1.75, "primary\n" + np_label, ha="center", va="top", fontsize=9)
    ax.text(1.5, -1.75, "secondary\n" + ns_label, ha="center", va="top", fontsize=9)
    ax.text(0, 1.55, "soft-iron core", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-3.9, 3.9)
    ax.set_ylim(-2.6, 2.0)
    return _png(fig)


def transmission(lines):
    """Power station -> step-up -> cables -> step-down -> homes, with data lines."""
    fig, ax = _fig(6.4, 2.4)
    boxes = [(0.0, "power\nstation"), (1.7, "step-up\ntransformer"), (4.6, "step-down\ntransformer"), (6.3, "homes")]
    for x, t in boxes:
        ax.add_patch(Rectangle((x, 0), 1.2, 1.0, fc="white", ec="black", lw=1.4))
        ax.text(x + 0.6, 0.5, t, ha="center", va="center", fontsize=8)
    ax.plot([1.2, 1.7], [0.5, 0.5], color="black", lw=1.2)
    ax.plot([2.9, 4.6], [0.6, 0.6], color="black", lw=1.2)
    ax.plot([2.9, 4.6], [0.4, 0.4], color="black", lw=1.2)
    ax.text(3.75, 0.75, "cables", ha="center", va="bottom", fontsize=8.5)
    ax.plot([5.8, 6.3], [0.5, 0.5], color="black", lw=1.2)
    for i, t in enumerate(lines):
        ax.text(0, -0.4 - 0.4 * i, t, ha="left", va="top", fontsize=9.5)
    ax.set_xlim(-0.2, 7.7)
    ax.set_ylim(-0.5 - 0.4 * len(lines), 1.3)
    return _png(fig)


# ================================================================== Ch 20 radioactivity
def atom_diagram(Z=3, N=4, label=None):
    """Nucleus with Z protons (+) and N neutrons, Z electrons on shells."""
    fig, ax = _fig(3.6, 3.6)
    rng = np.random.default_rng(Z * 10 + N)
    k = 0
    for i in range(Z + N):
        a, r = rng.uniform(0, 2 * math.pi), 0.35 * math.sqrt(rng.uniform(0, 1)) * min(1.0, 0.5 + (Z + N) / 12)
        is_p = i < Z
        ax.add_patch(Circle((r * math.cos(a), r * math.sin(a)), 0.16, fc="#d9534f" if is_p else "#999999", ec="black", lw=0.8, zorder=3))
        if is_p:
            ax.text(r * math.cos(a), r * math.sin(a), "+", ha="center", va="center", fontsize=8, color="white", fontweight="bold", zorder=4)
    shells = [2, 8, 18]
    left, r = Z, 0.9
    for cap in shells:
        if left <= 0:
            break
        ax.add_patch(Circle((0, 0), r, fc="none", ec="black", lw=0.9, ls="--"))
        n = min(cap, left)
        for j in range(n):
            a = 2 * math.pi * j / n
            ax.add_patch(Circle((r * math.cos(a), r * math.sin(a)), 0.09, fc="#1f5fa6", ec="black", lw=0.6, zorder=3))
            ax.text(r * math.cos(a) + 0.18, r * math.sin(a) + 0.12, "−", fontsize=8, fontweight="bold")
        left -= n
        r += 0.55
    if label:
        ax.text(0, -r + 0.1, label, ha="center", va="top", fontsize=10)
    ax.set_xlim(-r - 0.1, r + 0.1)
    ax.set_ylim(-r - 0.5, r + 0.1)
    return _png(fig)


def nuclide(A, Z, X, extra=None):
    """Large nuclide notation A over Z before the symbol X."""
    fig, ax = _fig(2.6, 1.6)
    ax.text(0.0, 0.62, str(A), ha="right", va="center", fontsize=16)
    ax.text(0.0, 0.18, str(Z), ha="right", va="center", fontsize=16)
    ax.text(0.08, 0.4, X, ha="left", va="center", fontsize=30, fontweight="bold")
    if extra:
        ax.text(0.3, -0.35, extra, ha="center", va="top", fontsize=9)
    ax.set_xlim(-0.8, 1.4)
    ax.set_ylim(-0.7, 1.1)
    return _png(fig)


def decay_curve(n0, half_life, tmax, unit="min", ylabel="count rate / counts per second", mark=None):
    """Exponential decay from n0 with the given half-life, on a grid (for reading half-lives off the curve)."""
    fig, ax = plt.subplots(figsize=(4.8, 3.2), dpi=DPI)
    t = np.linspace(0, tmax, 400)
    ax.plot(t, n0 * 0.5 ** (t / half_life), color="black", lw=2.0)
    step = next(s for s in (1, 2, 5, 10, 20, 50, 100, 200, 500) if tmax / s <= 10)
    ystep = next(s for s in (5, 10, 20, 25, 50, 100, 200, 500, 1000) if n0 / s <= 10)
    ax.set_xlim(0, tmax)
    ax.set_ylim(0, (int(n0 / ystep) + 1) * ystep)
    ax.set_xticks(np.arange(0, tmax + 1e-9, step))
    ax.set_yticks(np.arange(0, (int(n0 / ystep) + 1) * ystep + 1e-9, ystep))
    ax.set_xticks(np.arange(0, tmax + 1e-9, step / 5), minor=True)
    ax.set_yticks(np.arange(0, (int(n0 / ystep) + 1) * ystep + 1e-9, ystep / 5), minor=True)
    ax.grid(which="major", color="#666666", lw=0.7)
    ax.grid(which="minor", color="#cccccc", lw=0.4)
    ax.set_xlabel(f"time / {unit}", fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.tick_params(labelsize=8.5)
    for (x, y, tt) in (mark or []):
        ax.plot([x], [y], "o", color="black", ms=4)
        ax.text(x, y, " " + tt, fontsize=10, fontweight="bold", va="bottom")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def penetration():
    """Alpha stopped by paper, beta by a few mm of aluminium, gamma reduced by thick lead."""
    fig, ax = _fig(6.0, 2.8)
    ax.text(-0.2, 2.0, "α", ha="right", va="center", fontsize=13)
    ax.text(-0.2, 1.2, "β", ha="right", va="center", fontsize=13)
    ax.text(-0.2, 0.4, "γ", ha="right", va="center", fontsize=13)
    _arrow(ax, (0, 2.0), (1.3, 2.0), lw=1.6)
    _arrow(ax, (0, 1.2), (3.3, 1.2), lw=1.6)
    _arrow(ax, (0, 0.4), (5.9, 0.4), lw=1.6)
    ax.add_patch(Rectangle((1.4, -0.1), 0.08, 2.6, fc="white", ec="black", lw=1.2))
    ax.add_patch(Rectangle((3.4, -0.1), 0.3, 2.6, fc="#cccccc", ec="black", lw=1.2))
    ax.add_patch(Rectangle((5.0, -0.1), 0.9, 2.6, fc="#777777", ec="black", lw=1.2))
    ax.text(1.44, 2.6, "paper", ha="center", va="bottom", fontsize=9)
    ax.text(3.55, 2.6, "aluminium\n(a few mm)", ha="center", va="bottom", fontsize=9)
    ax.text(5.45, 2.6, "lead\n(several cm)", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-0.7, 6.4)
    ax.set_ylim(-0.3, 3.5)
    return _png(fig)


def detector_setup(lines):
    """Source, absorber and GM tube with a counter; data lines below."""
    fig, ax = _fig(5.6, 2.6)
    ax.add_patch(Rectangle((0, 0.3), 0.6, 0.6, fc="#777777", ec="black", lw=1.3))
    ax.text(0.3, 1.05, "source", ha="center", va="bottom", fontsize=9)
    ax.add_patch(Rectangle((1.6, 0.0), 0.2, 1.2, fc="#cccccc", ec="black", lw=1.2))
    ax.text(1.7, 1.3, "absorber", ha="center", va="bottom", fontsize=9)
    ax.add_patch(Rectangle((2.8, 0.3), 1.6, 0.6, fc="white", ec="black", lw=1.3))
    ax.text(3.6, 0.6, "GM tube", ha="center", va="center", fontsize=9)
    ax.plot([4.4, 5.0], [0.6, 0.6], color="black", lw=1.2)
    ax.add_patch(Rectangle((5.0, 0.3), 1.2, 0.6, fc="white", ec="black", lw=1.3))
    ax.text(5.6, 0.6, "counter", ha="center", va="center", fontsize=9)
    for i, t in enumerate(lines):
        ax.text(0, -0.4 - 0.4 * i, t, ha="left", va="top", fontsize=9.5)
    ax.set_xlim(-0.2, 6.5)
    ax.set_ylim(-0.5 - 0.4 * len(lines), 1.8)
    return _png(fig)
