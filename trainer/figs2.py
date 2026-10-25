"""Diagram drawers added for 6091 (Pure Physics) chapters 1, 5, 7-9 and 12: digital instruments, vectors on a grid,
liquid pressure, thermal set-ups, Brownian motion, and ray optics (reflection, refraction, total internal reflection, lenses).
Every drawing is computed from the numbers in the question, so picture and answer always agree. PNG bytes, DPI 170."""
import io
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

from .figs import DPI, _fig, _png, graph

# ------------------------------------------------------------------ seven-segment digital displays (Ch 1)
_T, _W, _H = 0.085, 0.62, 1.0
_SEG = {
    "a": [(_T, _H), (_W - _T, _H), (_W - 2 * _T, _H - _T), (2 * _T, _H - _T)],
    "g": [(_T, _H / 2), (2 * _T, _H / 2 + _T / 2), (_W - 2 * _T, _H / 2 + _T / 2), (_W - _T, _H / 2), (_W - 2 * _T, _H / 2 - _T / 2), (2 * _T, _H / 2 - _T / 2)],
    "d": [(_T, 0), (2 * _T, _T), (_W - 2 * _T, _T), (_W - _T, 0)],
    "f": [(0, _H - _T), (0, _H / 2 + _T / 2), (_T, _H / 2), (2 * _T, _H / 2 + _T / 2), (2 * _T, _H - 2 * _T)],
    "b": [(_W, _H - _T), (_W, _H / 2 + _T / 2), (_W - _T, _H / 2), (_W - 2 * _T, _H / 2 + _T / 2), (_W - 2 * _T, _H - 2 * _T)],
    "e": [(0, _T), (0, _H / 2 - _T / 2), (_T, _H / 2), (2 * _T, _H / 2 - _T / 2), (2 * _T, 2 * _T)],
    "c": [(_W, _T), (_W, _H / 2 - _T / 2), (_W - _T, _H / 2), (_W - 2 * _T, _H / 2 - _T / 2), (_W - 2 * _T, 2 * _T)],
}
_DIG = {"0": "abcdef", "1": "bc", "2": "abged", "3": "abgcd", "4": "fgbc", "5": "afgcd", "6": "afgedc", "7": "abc", "8": "abcdefg", "9": "abcdfg", "-": "g", " ": ""}


def _seg_text(ax, x, y, text, h):
    for ch in text:
        if ch == ".":
            ax.add_patch(Rectangle((x + 0.02 * h, y), 0.11 * h, 0.11 * h, color="#101010", lw=0, zorder=6))
            x += 0.26 * h
            continue
        if ch == ":":
            for yy in (0.28, 0.68):
                ax.add_patch(Rectangle((x + 0.02 * h, y + yy * h), 0.11 * h, 0.11 * h, color="#101010", lw=0, zorder=6))
            x += 0.30 * h
            continue
        for seg, pts in _SEG.items():
            on = seg in _DIG[ch]
            ax.add_patch(Polygon([(x + px * h, y + py * h) for px, py in pts], closed=True, fc="#101010" if on else "#d4dccb", ec="none", zorder=6))
        x += 0.82 * h
    return x


def _seg_width(text, h):
    return sum(0.26 * h if c == "." else 0.30 * h if c == ":" else 0.82 * h for c in text)


def _lcd(ax, x0, y0, w, h, text, unit=None):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.08", fc="#dfe6d3", ec="black", lw=1.6, zorder=1))
    dh = h * 0.52
    _seg_text(ax, x0 + w * 0.76 - _seg_width(text, dh), y0 + (h - dh) / 2, text, dh)
    if unit:
        ax.text(x0 + w * 0.97, y0 + h * 0.2, unit, ha="right", va="bottom", fontsize=8, fontweight="bold")


def digital_display(text, unit="mm", label=None):
    """One digital read-out (calipers, micrometer, balance, meter)."""
    fig, ax = _fig(3.0, 1.6)
    _lcd(ax, 0, 0.45, 2.6, 1.0, text, unit)
    if label:
        ax.text(1.3, 0.18, label, ha="center", va="center", fontsize=10)
    ax.set_xlim(-0.1, 2.7)
    ax.set_ylim(0, 1.6)
    return _png(fig)


def caliper_pair(zero_text, read_text, left_label="jaws closed", right_label="object between the jaws", unit="mm"):
    """Two displays of the same digital instrument: with the jaws closed (zero error) and with the object in place."""
    fig, ax = _fig(5.6, 1.8)
    for x0, text, lab in ((0.0, zero_text, left_label), (3.0, read_text, right_label)):
        _lcd(ax, x0, 0.55, 2.5, 1.0, text, unit)
        ax.text(x0 + 1.25, 0.22, lab, ha="center", va="center", fontsize=9.5)
    ax.set_xlim(-0.1, 5.6)
    ax.set_ylim(0, 1.7)
    return _png(fig)


def digital_calipers(text, unit="mm", object_label=None):
    """Digital calipers holding a small object, with the read-out."""
    fig, ax = _fig(6.0, 2.6)
    ax.add_patch(Rectangle((0.0, 1.0), 7.0, 0.5, fc="#e8e8e8", ec="black", lw=1.5))              # main beam
    for i in range(0, 15):
        ax.plot([0.4 + i * 0.45] * 2, [1.5, 1.5 - (0.22 if i % 5 == 0 else 0.12)], color="black", lw=0.8)
    ax.add_patch(Rectangle((0.0, 0.0), 0.35, 1.0, fc="#dddddd", ec="black", lw=1.4))               # fixed jaw
    ax.add_patch(Rectangle((1.75, 0.0), 0.35, 1.0, fc="#dddddd", ec="black", lw=1.4))              # sliding jaw
    ax.add_patch(FancyBboxPatch((1.9, 1.55), 3.2, 1.0, boxstyle="round,pad=0.02", fc="#cfcfcf", ec="black", lw=1.4))   # slider body
    _lcd(ax, 2.05, 1.65, 2.9, 0.8, text, unit)
    ax.add_patch(Ellipse((1.05, 0.5), 1.3, 0.8, fc="#bbbbbb", ec="black", lw=1.4))                # the object
    if object_label:
        ax.text(1.05, -0.35, object_label, ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-0.3, 7.3)
    ax.set_ylim(-0.8, 2.8)
    return _png(fig)


# ------------------------------------------------------------------ vectors on a grid (Ch 1, 3)
def vector_grid(vectors, nx=9, ny=7, origin=(1, 3), scale_label="1 square = 1 N", resultant=None, name_origin="O"):
    """vectors: [(label, dx, dy)] in squares from the origin. resultant: (label, dx, dy) drawn dashed, if given."""
    fig, ax = _fig(5.4, 5.4 * ny / nx)
    ax.set_xlim(0, nx)
    ax.set_ylim(0, ny)
    for i in range(nx + 1):
        ax.axvline(i, color="#bdbdbd", lw=0.6, zorder=0)
    for j in range(ny + 1):
        ax.axhline(j, color="#bdbdbd", lw=0.6, zorder=0)
    ox, oy = origin
    for lab, dx, dy in vectors:
        ax.add_patch(FancyArrowPatch((ox, oy), (ox + dx, oy + dy), arrowstyle="-|>", mutation_scale=15, lw=2.0, color="black", shrinkA=0, shrinkB=0, zorder=4))
        ax.text(ox + dx / 2 + (0.35 if dy >= 0 else -0.35) * (1 if dx >= 0 else -1) * 0, oy + dy / 2 + (0.4 if dy >= 0 else -0.4), lab, ha="center", va="center",
                fontsize=12, fontweight="bold", bbox=dict(fc="white", ec="none", pad=1.0), zorder=5)
    if resultant:
        lab, dx, dy = resultant
        ax.add_patch(FancyArrowPatch((ox, oy), (ox + dx, oy + dy), arrowstyle="-|>", mutation_scale=15, lw=1.8, color="black", ls="--", shrinkA=0, shrinkB=0, zorder=4))
        ax.text(ox + dx / 2, oy + dy / 2 - 0.45, lab, ha="center", va="center", fontsize=12, fontweight="bold", bbox=dict(fc="white", ec="none", pad=1.0), zorder=5)
    ax.plot([ox], [oy], "o", color="black", ms=5, zorder=5)
    ax.text(ox - 0.25, oy - 0.25, name_origin, ha="right", va="top", fontsize=11, fontweight="bold")
    ax.text(nx / 2, -0.45, scale_label, ha="center", va="top", fontsize=10)
    ax.set_ylim(-0.9, ny + 0.1)
    return _png(fig)


def vector_pair(a_label, b_label, angle_deg, a_len=2.6, b_len=2.0):
    """Two vectors from one point with the angle between them marked (for parallelogram / scale-drawing questions)."""
    fig, ax = _fig(4.6, 3.4)
    ang = math.radians(angle_deg)
    ax.add_patch(FancyArrowPatch((0, 0), (a_len, 0), arrowstyle="-|>", mutation_scale=16, lw=2.0, color="black", shrinkA=0, shrinkB=0))
    ax.add_patch(FancyArrowPatch((0, 0), (b_len * math.cos(ang), b_len * math.sin(ang)), arrowstyle="-|>", mutation_scale=16, lw=2.0, color="black", shrinkA=0, shrinkB=0))
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=0, theta2=angle_deg, lw=1.2, color="black"))
    mid = math.radians(angle_deg / 2)
    ax.text(0.85 * math.cos(mid), 0.85 * math.sin(mid), f"{angle_deg}°", ha="center", va="center", fontsize=10)
    ax.text(a_len / 2, -0.3, a_label, ha="center", va="top", fontsize=11)
    ax.text(b_len / 2 * math.cos(ang) - 0.3 * math.sin(ang), b_len / 2 * math.sin(ang) + 0.3 * math.cos(ang), b_label, ha="center", va="center", fontsize=11)
    ax.plot([0], [0], "o", color="black", ms=5)
    ax.set_xlim(-0.8, max(a_len, b_len) + 0.8)
    ax.set_ylim(-0.8, max(0.8, b_len * math.sin(ang) + 0.8))
    return _png(fig)


# ------------------------------------------------------------------ pressure (Ch 5)
def liquid_column(h_label, liquid_label="water", point_label="X", extra=None):
    """Tank of liquid with a marked point at depth h below the surface."""
    fig, ax = _fig(4.2, 3.6)
    ax.add_patch(Rectangle((0, 0), 4.0, 3.6, fc="white", ec="black", lw=1.8))
    ax.add_patch(Rectangle((0.03, 0.03), 3.94, 3.0, fc="#dfe8f3", ec="none"))
    ax.plot([0.03, 3.97], [3.03, 3.03], color="black", lw=1.2)
    ax.plot([2.4], [0.9], "o", color="black", ms=5)
    ax.text(2.6, 0.9, point_label, ha="left", va="center", fontsize=11, fontweight="bold")
    ax.add_patch(FancyArrowPatch((1.0, 3.03), (1.0, 0.9), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(0.85, 1.95, h_label, ha="right", va="center", fontsize=10.5)
    ax.text(3.9, 3.2, liquid_label, ha="right", va="bottom", fontsize=10)
    if extra:
        ax.text(2.0, -0.3, extra, ha="center", va="top", fontsize=10)
    ax.set_xlim(-0.6, 4.4)
    ax.set_ylim(-0.9, 4.0)
    return _png(fig)


def manometer(h_label, gas_label="gas supply", left_higher=False):
    """U-tube manometer open to the atmosphere on the right, connected to a gas on the left. The liquid is lower on the side with the higher pressure."""
    fig, ax = _fig(4.4, 3.8)
    d = 0.9 if not left_higher else -0.9
    base = 1.6
    yl, yr = base - d / 2, base + d / 2          # liquid levels (left, right)
    for x in (1.0, 2.6):
        ax.plot([x, x], [0.4, 3.6], color="black", lw=1.6)
        ax.plot([x + 0.4, x + 0.4], [0.4, 3.6], color="black", lw=1.6)
    ax.plot([1.0, 1.0, 3.0, 3.0], [0.4, 0.0, 0.0, 0.4], color="black", lw=1.6)
    ax.plot([1.4, 1.4, 2.6, 2.6], [0.4, 0.4, 0.4, 0.4], color="black", lw=1.6)
    ax.add_patch(Rectangle((1.02, 0.02), 0.36, yl, fc="#9ec3e6", ec="none"))
    ax.add_patch(Rectangle((2.62, 0.02), 0.36, yr, fc="#9ec3e6", ec="none"))
    ax.add_patch(Rectangle((1.02, 0.02), 1.96, 0.38, fc="#9ec3e6", ec="none"))
    ax.plot([0.0, 1.0], [3.6, 3.6], color="black", lw=1.6)
    ax.plot([0.0, 1.4], [3.3, 3.3], color="black", lw=1.6)
    ax.text(-0.1, 3.45, gas_label, ha="right", va="center", fontsize=9.5)
    ax.text(2.8, 3.75, "open to\natmosphere", ha="center", va="bottom", fontsize=8.5)
    ax.add_patch(FancyArrowPatch((3.5, min(yl, yr)), (3.5, max(yl, yr)), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.plot([1.4, 3.6], [yl, yl], color="#555555", lw=0.6, ls=":")
    ax.plot([3.0, 3.6], [yr, yr], color="#555555", lw=0.6, ls=":")
    ax.text(3.65, base, h_label, ha="left", va="center", fontsize=10.5)
    ax.set_xlim(-2.0, 5.2)
    ax.set_ylim(-0.3, 4.6)
    return _png(fig)


def hydraulic_press(f1_label, a1_label, a2_label, f2_label):
    """Two connected cylinders with pistons: small piston (left) and large piston (right)."""
    fig, ax = _fig(5.6, 3.2)
    ax.add_patch(Rectangle((0, 0), 5.8, 1.0, fc="#dfe8f3", ec="none"))
    ax.add_patch(Rectangle((0.4, 1.0), 0.8, 2.0, fc="#dfe8f3", ec="none"))
    ax.add_patch(Rectangle((3.4, 1.0), 2.0, 1.6, fc="#dfe8f3", ec="none"))
    ax.plot([0.4, 0.4, 0, 0, 5.8, 5.8, 5.4, 5.4], [3.0, 1.0, 1.0, 0, 0, 1.0, 1.0, 2.6], color="black", lw=1.8)
    ax.plot([1.2, 1.2, 3.4, 3.4], [3.0, 1.0, 1.0, 2.6], color="black", lw=1.8)
    ax.add_patch(Rectangle((0.42, 2.4), 0.76, 0.3, fc="#999999", ec="black", lw=1.2))
    ax.add_patch(Rectangle((3.42, 2.1), 1.96, 0.3, fc="#999999", ec="black", lw=1.2))
    ax.add_patch(FancyArrowPatch((0.8, 3.7), (0.8, 2.75), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black"))
    ax.text(1.0, 3.3, f1_label, ha="left", va="center", fontsize=10.5)
    ax.add_patch(FancyArrowPatch((4.4, 2.45), (4.4, 3.4), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black"))
    ax.text(4.6, 3.0, f2_label, ha="left", va="center", fontsize=10.5)
    ax.text(0.8, 1.7, a1_label, ha="center", va="center", fontsize=9, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(4.4, 1.5, a2_label, ha="center", va="center", fontsize=9, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(2.3, 0.45, "liquid", ha="center", va="center", fontsize=9)
    ax.set_xlim(-0.3, 6.6)
    ax.set_ylim(-0.3, 4.1)
    return _png(fig)


def barometer(h_label, liquid="mercury"):
    fig, ax = _fig(3.2, 4.0)
    ax.add_patch(Rectangle((0.0, 0.0), 3.0, 0.9, fc="white", ec="black", lw=1.6))
    ax.add_patch(Rectangle((0.03, 0.03), 2.94, 0.55, fc="#bbbbbb", ec="none"))
    ax.add_patch(Rectangle((1.2, 0.3), 0.6, 4.2, fc="white", ec="black", lw=1.6))
    ax.add_patch(Rectangle((1.23, 0.33), 0.54, 3.1, fc="#bbbbbb", ec="none"))
    ax.text(1.5, 4.0, "vacuum", ha="center", va="center", fontsize=8)
    ax.add_patch(FancyArrowPatch((2.4, 0.58), (2.4, 3.43), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(2.55, 2.0, h_label, ha="left", va="center", fontsize=10.5)
    ax.text(0.5, 0.3, liquid, ha="center", va="center", fontsize=8.5)
    ax.set_xlim(-0.3, 4.2)
    ax.set_ylim(-0.3, 4.6)
    return _png(fig)


# ------------------------------------------------------------------ thermal set-ups (Ch 7-9)
def heater_block(lines, body="metal block"):
    """Block with an immersion heater and thermometer; data lines on the right."""
    fig, ax = _fig(5.6, 3.0)
    ax.add_patch(Rectangle((0, 0), 2.4, 2.0, fc="#dddddd", ec="black", lw=1.8))
    ax.add_patch(Rectangle((0.5, 0.4), 0.3, 2.4, fc="#f4c7a1", ec="black", lw=1.2))
    ax.plot([0.55, 0.55, 0.75, 0.75], [2.8, 3.2, 3.2, 2.8], color="black", lw=1.2)
    ax.text(0.6, 3.3, "heater", ha="right", va="bottom", fontsize=8.5)
    ax.add_patch(Rectangle((1.6, 0.4), 0.16, 2.6, fc="white", ec="black", lw=1.2))
    ax.plot([1.68, 1.68], [0.5, 1.8], color="#c0392b", lw=3)
    ax.text(1.85, 3.1, "thermometer", ha="left", va="bottom", fontsize=8.5)
    ax.text(1.2, -0.3, body, ha="center", va="top", fontsize=10)
    for i, t in enumerate(lines):
        ax.text(3.0, 2.4 - 0.5 * i, t, ha="left", va="center", fontsize=10.5)
    ax.set_xlim(-0.3, 7.2)
    ax.set_ylim(-0.8, 3.8)
    return _png(fig)


def beaker_heater(lines, liquid="water"):
    fig, ax = _fig(5.6, 3.0)
    ax.add_patch(Rectangle((0, 0), 2.4, 2.4, fc="white", ec="black", lw=1.8))
    ax.add_patch(Rectangle((0.03, 0.03), 2.34, 1.8, fc="#dfe8f3", ec="none"))
    ax.add_patch(Rectangle((0.6, 0.3), 0.3, 2.6, fc="#f4c7a1", ec="black", lw=1.2))
    ax.text(0.75, 3.0, "heater", ha="center", va="bottom", fontsize=8.5)
    ax.add_patch(Rectangle((1.6, 0.3), 0.16, 2.8, fc="white", ec="black", lw=1.2))
    ax.plot([1.68, 1.68], [0.4, 1.6], color="#c0392b", lw=3)
    ax.text(1.68, 3.2, "thermometer", ha="center", va="bottom", fontsize=8.5)
    ax.text(1.2, -0.3, liquid, ha="center", va="top", fontsize=10)
    for i, t in enumerate(lines):
        ax.text(3.0, 2.4 - 0.5 * i, t, ha="left", va="center", fontsize=10.5)
    ax.set_xlim(-0.3, 7.2)
    ax.set_ylim(-0.8, 3.8)
    return _png(fig)


def temp_time_graph(pts, labels=None, xlabel="time / min", ymax=None, xstep=None):
    """Temperature-time graph through the given corner points (data-reading questions)."""
    xs, ys = zip(*pts)
    xstep = xstep or next(s for s in (1, 2, 5, 10, 20, 50, 100) if max(xs) / s <= 8)
    xmax = (int(max(xs) / xstep) + (1 if max(xs) % xstep else 0)) * xstep
    ymax = ymax or (int(max(ys) / 20) + 1) * 20
    return graph(pts, xmax, ymax, xstep, 20, xlabel=xlabel, ylabel="temperature / °C", labels=labels)


def two_curves(curves, xmax, ymax, xstep, ystep, xlabel="time / min", ylabel="temperature / °C"):
    """curves: [(name, [(x, y), ...])] drawn on one set of axes, each labelled at its last point."""
    fig, ax = plt.subplots(figsize=(4.8, 3.1), dpi=DPI)
    styles = ["-", "--", ":"]
    for (name, pts), ls in zip(curves, styles):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color="black", lw=2.0, ls=ls)
        ax.text(xs[-1], ys[-1], f" {name}", fontsize=10, fontweight="bold", va="center")
    ax.set_xlim(0, xmax * 1.12)
    ax.set_ylim(0, ymax)
    ax.set_xticks(np.arange(0, xmax + 1e-9, xstep))
    ax.set_yticks(np.arange(0, ymax + 1e-9, ystep))
    ax.grid(which="major", color="#888888", linewidth=0.6)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.tick_params(labelsize=9)
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def gas_syringe(lines):
    """Gas trapped in a syringe by a piston, with data lines."""
    fig, ax = _fig(5.6, 2.2)
    ax.add_patch(Rectangle((0, 0.4), 3.4, 1.2, fc="#eef3f8", ec="black", lw=1.8))
    ax.add_patch(Rectangle((2.2, 0.45), 0.25, 1.1, fc="#999999", ec="black", lw=1.2))
    ax.plot([2.45, 4.0], [1.0, 1.0], color="black", lw=2.5)
    ax.add_patch(Rectangle((4.0, 0.7), 0.15, 0.6, fc="#999999", ec="black", lw=1.2))
    ax.text(1.1, 1.0, "gas", ha="center", va="center", fontsize=10)
    ax.text(2.3, -0.1, "piston", ha="center", va="top", fontsize=9)
    for i, t in enumerate(lines):
        ax.text(4.6, 1.5 - 0.5 * i, t, ha="left", va="center", fontsize=10.5)
    ax.set_xlim(-0.3, 8.0)
    ax.set_ylim(-0.6, 2.2)
    return _png(fig)


def brownian_cell(seed=2):
    """Smoke cell: a bright speck's random zig-zag path, with the microscope and lamp labelled."""
    fig, ax = _fig(4.4, 3.4)
    ax.add_patch(Rectangle((0, 0), 3.0, 2.2, fc="#f7f7f7", ec="black", lw=1.6))
    rng = np.random.default_rng(seed)
    p = np.array([1.5, 1.1])
    pts = [p.copy()]
    for _ in range(14):
        p = p + rng.uniform(-0.5, 0.5, 2)
        p = np.clip(p, 0.2, [2.8, 2.0])
        pts.append(p.copy())
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color="black", lw=1.2)
    ax.plot(pts[:, 0], pts[:, 1], "o", color="black", ms=3)
    ax.text(1.5, 2.35, "smoke cell (viewed through a microscope)", ha="center", va="bottom", fontsize=8.5)
    ax.add_patch(FancyArrowPatch((-0.9, 1.1), (-0.05, 1.1), arrowstyle="-|>", mutation_scale=12, lw=1.4, color="black"))
    ax.text(-0.5, 1.35, "light", ha="center", va="bottom", fontsize=9)
    ax.text(1.5, -0.3, "path of one smoke particle", ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-1.3, 3.3)
    ax.set_ylim(-0.8, 2.9)
    return _png(fig)


# ------------------------------------------------------------------ light (Ch 12)
def _angle_arc(ax, centre, r, start, end, label, label_r=None):
    ax.add_patch(Arc(centre, 2 * r, 2 * r, theta1=min(start, end), theta2=max(start, end), lw=1.1, color="black"))
    mid = math.radians((start + end) / 2)
    rr = label_r or r + 0.35
    ax.text(centre[0] + rr * math.cos(mid), centre[1] + rr * math.sin(mid), label, ha="center", va="center", fontsize=10)


def mirror_reflection(i_deg, label_i=None, label_r=None, show_reflected=True):
    """Plane mirror (horizontal), normal, incident ray from the upper left at angle i to the normal, reflected ray at angle i."""
    fig, ax = _fig(4.6, 3.2)
    ax.add_patch(Rectangle((-3.0, -0.25), 6.0, 0.25, fc="#cccccc", ec="black", lw=1.4, hatch="////"))
    ax.plot([0, 0], [0, 3.0], color="black", lw=1.0, ls="--")
    ax.text(0.1, 3.0, "normal", ha="left", va="top", fontsize=8.5)
    a = math.radians(i_deg)
    L = 2.8
    ax.add_patch(FancyArrowPatch((-L * math.sin(a), L * math.cos(a)), (0, 0), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black", shrinkA=0, shrinkB=0))
    if show_reflected:
        ax.add_patch(FancyArrowPatch((0, 0), (L * math.sin(a), L * math.cos(a)), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black", shrinkA=0, shrinkB=0))
    _angle_arc(ax, (0, 0), 0.9, 90, 90 + i_deg, label_i or f"{i_deg}°")
    if show_reflected:
        _angle_arc(ax, (0, 0), 0.9, 90 - i_deg, 90, label_r or "r")
    ax.text(-L * math.sin(a) - 0.1, L * math.cos(a) + 0.1, "incident ray", ha="right", va="bottom", fontsize=8.5)
    ax.text(-2.9, -0.55, "plane mirror", ha="left", va="top", fontsize=9)
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-0.9, 3.4)
    return _png(fig)


def refraction(i_deg, r_deg, upper="air", lower="glass", label_i=None, label_r=None, show_refracted=True):
    """Ray crossing a horizontal boundary from the upper medium into the lower one. Angles measured from the normal."""
    fig, ax = _fig(4.6, 4.0)
    ax.add_patch(Rectangle((-3.0, -2.8), 6.0, 2.8, fc="#dfe8f3" if lower != "air" else "white", ec="none"))
    ax.add_patch(Rectangle((-3.0, 0), 6.0, 2.8, fc="#dfe8f3" if upper != "air" else "white", ec="none"))
    ax.plot([-3.0, 3.0], [0, 0], color="black", lw=1.6)
    ax.plot([0, 0], [-2.8, 2.8], color="black", lw=1.0, ls="--")
    ax.text(0.1, 2.75, "normal", ha="left", va="top", fontsize=8.5)
    a, b = math.radians(i_deg), math.radians(r_deg)
    L = 2.6
    ax.add_patch(FancyArrowPatch((-L * math.sin(a), L * math.cos(a)), (0, 0), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black", shrinkA=0, shrinkB=0))
    if show_refracted:
        ax.add_patch(FancyArrowPatch((0, 0), (L * math.sin(b), -L * math.cos(b)), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black", shrinkA=0, shrinkB=0))
        _angle_arc(ax, (0, 0), 0.9, 270, 270 + r_deg, label_r or f"{r_deg}°")
    _angle_arc(ax, (0, 0), 0.9, 90, 90 + i_deg, label_i or f"{i_deg}°")
    ax.text(-2.9, 2.6, upper, ha="left", va="top", fontsize=10)
    ax.text(-2.9, -2.6, lower, ha="left", va="bottom", fontsize=10)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.0, 3.0)
    return _png(fig)


def tir(i_deg, c_deg=None, medium="glass", label=None):
    """Ray inside a denser medium (below) meeting the boundary with air: refracted + weak reflected ray if i < c, total internal reflection if i > c."""
    fig, ax = _fig(4.6, 3.8)
    ax.add_patch(Rectangle((-3.0, -2.8), 6.0, 2.8, fc="#dfe8f3", ec="none"))
    ax.plot([-3.0, 3.0], [0, 0], color="black", lw=1.6)
    ax.plot([0, 0], [-2.8, 2.4], color="black", lw=1.0, ls="--")
    a = math.radians(i_deg)
    L = 2.5
    ax.add_patch(FancyArrowPatch((-L * math.sin(a), -L * math.cos(a)), (0, 0), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black", shrinkA=0, shrinkB=0))
    total = c_deg is not None and i_deg > c_deg
    ax.add_patch(FancyArrowPatch((0, 0), (L * math.sin(a), -L * math.cos(a)), arrowstyle="-|>", mutation_scale=14, lw=1.8 if total else 1.0, color="black", shrinkA=0, shrinkB=0))
    if not total and c_deg is not None:
        n = 1 / math.sin(math.radians(c_deg))
        s = n * math.sin(a)
        if s < 1:
            b = math.asin(s)
            ax.add_patch(FancyArrowPatch((0, 0), (L * math.sin(b), L * math.cos(b)), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black", shrinkA=0, shrinkB=0))
    _angle_arc(ax, (0, 0), 0.9, 270 - i_deg, 270, label or f"{i_deg}°")
    ax.text(-2.9, 2.2, "air", ha="left", va="top", fontsize=10)
    ax.text(-2.9, -2.6, medium, ha="left", va="bottom", fontsize=10)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.0, 2.6)
    return _png(fig)


def optical_fibre():
    fig, ax = _fig(5.6, 2.2)
    ax.add_patch(Rectangle((0, 0.4), 6.0, 1.0, fc="#dfe8f3", ec="black", lw=1.6))
    x, y, dy = 0.2, 0.6, 0.8
    pts = [(x, y)]
    while x < 5.8:
        x2 = x + 1.0
        y2 = 0.4 + 0.02 if dy < 0 else 1.4 - 0.02
        pts.append((min(x2, 5.9), y2))
        x, y, dy = x2, y2, -dy
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color="black", lw=1.6)
    ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=12, lw=1.6, color="black", shrinkA=0, shrinkB=0))
    ax.text(3.0, 1.6, "glass core", ha="center", va="bottom", fontsize=9.5)
    ax.text(3.0, 0.2, "light reflects off the inside of the fibre", ha="center", va="top", fontsize=9)
    ax.set_xlim(-0.2, 6.2)
    ax.set_ylim(-0.4, 2.2)
    return _png(fig)


def lens_rays(f, u, h=1.0, show_image=True, grid=True, label_f=True):
    """Thin converging lens at x = 0 with focal length f; object (upright arrow of height h) at distance u on the left.
    Draws the two standard rays and the image (real: beyond the lens; virtual: dashed, same side). Squares are 1 unit."""
    v = None if abs(u - f) < 1e-9 else 1 / (1 / f - 1 / u)
    m = None if v is None else -v / u
    xmin = -max(u, 2 * f) - 1.5
    xmax = (max(v, 2 * f) if v and v > 0 else 2 * f) + 1.5
    ymax = max(h, abs(h * m) if m else h) + 1.0
    fig, ax = plt.subplots(figsize=(6.6, 3.4), dpi=DPI)
    if grid:
        for gx in range(int(math.floor(xmin)), int(math.ceil(xmax)) + 1):
            ax.axvline(gx, color="#d8d8d8", lw=0.5, zorder=0)
        for gy in range(int(-math.ceil(ymax)), int(math.ceil(ymax)) + 1):
            ax.axhline(gy, color="#d8d8d8", lw=0.5, zorder=0)
    ax.axhline(0, color="black", lw=1.0, zorder=1)
    ax.add_patch(Ellipse((0, 0), 0.5, 2 * ymax * 0.9, fc="#dfe8f3", ec="black", lw=1.4, zorder=2))
    for fx, name in ((-f, "F"), (f, "F"), (-2 * f, "2F"), (2 * f, "2F")):
        ax.plot([fx], [0], "o", color="black", ms=4, zorder=3)
        if label_f:
            ax.text(fx, -0.35, name, ha="center", va="top", fontsize=9)
    ax.add_patch(FancyArrowPatch((-u, 0), (-u, h), arrowstyle="-|>", mutation_scale=14, lw=2.2, color="black", shrinkA=0, shrinkB=0, zorder=4))
    ax.text(-u, h + 0.15, "object", ha="center", va="bottom", fontsize=9)
    # ray 1: parallel to axis, then through F on the far side
    ax.plot([-u, 0], [h, h], color="black", lw=1.4, zorder=3)
    # ray 2: through the optical centre, undeviated
    if v is not None and v > 0 and show_image:
        hi = h * m
        ax.plot([0, v + 0.6], [h, h - h / f * (v + 0.6)], color="black", lw=1.4, zorder=3)            # ray 1 refracted through F
        ax.plot([-u, v + 0.6], [h, -h * (v + 0.6) / u], color="black", lw=1.4, zorder=3)              # ray 2 straight through the centre
        ax.add_patch(FancyArrowPatch((v, 0), (v, hi), arrowstyle="-|>", mutation_scale=14, lw=2.2, color="black", shrinkA=0, shrinkB=0, zorder=4))
        ax.text(v, hi - 0.15 if hi < 0 else hi + 0.15, "image", ha="center", va="top" if hi < 0 else "bottom", fontsize=9)
    elif v is not None and v < 0 and show_image:      # virtual image: extend rays back
        hi = h * m
        ax.plot([0, 2 * f + 1], [h, h - h / f * (2 * f + 1)], color="black", lw=1.4, zorder=3)
        ax.plot([-u, 2 * f + 1], [h, -h * (2 * f + 1) / u], color="black", lw=1.4, zorder=3)
        ax.plot([0, v], [h, hi], color="black", lw=1.0, ls="--", zorder=3)
        ax.plot([-u, v], [h, hi], color="black", lw=1.0, ls="--", zorder=3)
        ax.add_patch(FancyArrowPatch((v, 0), (v, hi), arrowstyle="-|>", mutation_scale=14, lw=2.0, color="black", ls="--", shrinkA=0, shrinkB=0, zorder=4))
        ax.text(v, hi + 0.15, "image", ha="center", va="bottom", fontsize=9)
        xmin = min(xmin, v - 1.0)
        ymax = max(ymax, abs(hi) + 0.8)
    elif not show_image and v is not None and v > 0:
        ax.plot([0, v + 0.6], [h, h - h * (v + 0.6) / f], color="black", lw=1.4, zorder=3)
        ax.plot([-u, v + 0.6], [h, -h * (v + 0.6) / u], color="black", lw=1.4, zorder=3)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-ymax, ymax)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(xmin + 0.1, -ymax + 0.1, "1 square = 1 cm", fontsize=8.5, ha="left", va="bottom")
    return _png(fig)


def lens_beam(f, label="f"):
    """Parallel beam brought to a focus by a converging lens; focal length marked."""
    fig, ax = _fig(5.4, 2.8)
    ax.add_patch(Ellipse((0, 0), 0.5, 3.2, fc="#dfe8f3", ec="black", lw=1.4))
    for y in (-1.2, -0.6, 0.0, 0.6, 1.2):
        ax.plot([-3.0, 0], [y, y], color="black", lw=1.3)
        ax.add_patch(FancyArrowPatch((0, y), (f, 0), arrowstyle="-|>", mutation_scale=11, lw=1.3, color="black", shrinkA=0, shrinkB=0))
        ax.plot([f, f + 0.8], [0, -y * 0.8 / f], color="black", lw=1.0)
    ax.plot([f], [0], "o", color="black", ms=5)
    ax.text(f, 0.25, "F", ha="center", va="bottom", fontsize=10)
    ax.plot([-3.2, f + 1.0], [0, 0], color="black", lw=0.7, ls="--")
    ax.add_patch(FancyArrowPatch((0, -1.9), (f, -1.9), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(f / 2, -2.05, label, ha="center", va="top", fontsize=10.5)
    ax.set_xlim(-3.4, f + 1.4)
    ax.set_ylim(-2.6, 2.0)
    return _png(fig)


# ------------------------------------------------------------------ bank-extension drawers (25 Oct 2026)
def rule_object(a_cm, b_cm, label="pencil"):
    """An object lying against a centimetre rule from a_cm to b_cm (mm ticks), readings computed from the numbers."""
    lo, hi = int(a_cm) - 1 if a_cm >= 1 else 0, int(b_cm) + 2
    fig, ax = _fig(6.4, 1.9)
    ax.add_patch(Rectangle((lo - 0.2, 0), hi - lo + 0.4, 0.9, fc="#f4ecd6", ec="black", lw=1.3))
    for k in range(int(lo * 10), int(hi * 10) + 1):
        x = k / 10
        L = 0.42 if k % 10 == 0 else (0.28 if k % 5 == 0 else 0.16)
        ax.plot([x, x], [0.9, 0.9 - L], color="black", lw=0.8 if k % 10 else 1.1)
        if k % 10 == 0:
            ax.text(x, 0.3, str(k // 10), ha="center", va="center", fontsize=8)
    ax.text(hi + 0.25, 0.3, "cm", ha="left", va="center", fontsize=8)
    ax.add_patch(Rectangle((a_cm, 0.95), b_cm - a_cm, 0.32, fc="#d9d9d9", ec="black", lw=1.3))
    ax.text((a_cm + b_cm) / 2, 1.11, label, ha="center", va="center", fontsize=9)
    for x in (a_cm, b_cm):
        ax.plot([x, x], [0.9, 1.4], color="#c00000", lw=1.0, ls="--")
    ax.set_xlim(lo - 0.5, hi + 1.0)
    ax.set_ylim(-0.1, 1.5)
    return _png(fig)


def forces_on_line(items, body="box"):
    """Forces along one horizontal line on a box: items = [(label, 'right'|'left', relative length)], stacked so none overlap."""
    fig, ax = _fig(6.0, 2.2)
    ax.plot([-3.2, 3.2], [-0.5, -0.5], color="black", lw=1.4)
    ax.add_patch(Rectangle((-0.7, -0.5), 1.4, 1.0, fc="white", ec="black", lw=1.6))
    ax.text(0, 0, body, ha="center", va="center", fontsize=10)
    ys = np.linspace(0.3, -0.3, len(items)) if len(items) > 1 else [0.0]
    for (lab, d, L), y in zip(items, ys):
        L = 0.6 + 1.6 * L / max(x[2] for x in items)
        if d == "right":
            p0, p1, tx = (0.7, y), (0.7 + L, y), 0.7 + L + 0.1
            ha = "left"
        else:
            p0, p1, tx = (-0.7, y), (-0.7 - L, y), -0.7 - L - 0.1
            ha = "right"
        ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=13, lw=1.8, color="black", shrinkA=0, shrinkB=0))
        ax.text(tx, y, lab, ha=ha, va="center", fontsize=10)
    ax.set_xlim(-4.2, 4.2)
    ax.set_ylim(-0.9, 0.8)
    return _png(fig)


def stopwatch_text(t):
    """mm:ss.hh display string for a time in seconds."""
    return f"{int(t // 60)}:{t - 60 * int(t // 60):05.2f}"


def stability_shapes(items):
    """Side views of objects for stability comparisons. items = [(name, base_width, height, cg_height)] in any consistent unit."""
    fig, ax = _fig(1.9 * len(items) + 0.6, 3.0)
    H = max(h for _, _, h, _ in items)
    k = 2.2 / H
    x = 0.0
    for name, w, h, c in items:
        wk, hk = w * k, h * k
        ax.add_patch(Polygon([(x, 0), (x + wk, 0), (x + wk * 0.5 + 0.18, hk), (x + wk * 0.5 - 0.18, hk)] if w > 0.6 * h else [(x, 0), (x + wk, 0), (x + wk, hk), (x, hk)],
                             closed=True, fc="#e6e6e6", ec="black", lw=1.5))
        ax.plot([x + wk / 2], [c * k], "o", color="black", ms=5)
        ax.text(x + wk / 2 + 0.08, c * k, "G", fontsize=9, va="bottom")
        ax.text(x + wk / 2, -0.25, name, ha="center", va="top", fontsize=11, fontweight="bold")
        x += max(wk, 0.8) + 0.9
    ax.plot([-0.3, x - 0.6], [0, 0], color="black", lw=1.4)
    ax.set_xlim(-0.4, x - 0.5)
    ax.set_ylim(-0.7, 2.6)
    return _png(fig)


def tilt_block(w, h, angle_deg, label=None):
    """A uniform block of base width w and height h tilted about its lower right corner by angle_deg; the vertical through G is drawn."""
    import math as _m
    fig, ax = _fig(3.8, 3.4)
    k = 2.4 / max(w, h)
    W, Hh = w * k, h * k
    a = -_m.radians(angle_deg)
    pivot = (2.0, 0.0)

    def rot(px, py):
        dx, dy = px - pivot[0], py - pivot[1]
        return (pivot[0] + dx * _m.cos(a) - dy * _m.sin(a), pivot[1] + dx * _m.sin(a) + dy * _m.cos(a))
    corners = [rot(pivot[0] - W, 0), rot(pivot[0], 0), rot(pivot[0], Hh), rot(pivot[0] - W, Hh)]
    ax.add_patch(Polygon(corners, closed=True, fc="#e6e6e6", ec="black", lw=1.6))
    g = rot(pivot[0] - W / 2, Hh / 2)
    ax.plot([g[0]], [g[1]], "o", color="black", ms=5)
    ax.text(g[0] - 0.12, g[1], "G", ha="right", va="center", fontsize=10)
    ax.plot([g[0], g[0]], [g[1], -0.05], color="#c00000", lw=1.2, ls="--")
    ax.plot([-0.5, 3.4], [0, 0], color="black", lw=1.4)
    ax.plot([pivot[0]], [0], "^", color="black", ms=7)
    if label:
        ax.text(1.4, -0.35, label, ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-0.6, 3.6)
    ax.set_ylim(-0.8, 3.1)
    return _png(fig)


def spanner_force(L, F_label, ang_deg, d_label):
    """A spanner of length L from a nut, with a force at ang_deg to the spanner at its end; the line of action and the
    perpendicular distance from the nut are drawn."""
    fig, ax = _fig(4.6, 3.2)
    k = 3.0 / L
    end = (3.0, 0.0)
    ax.add_patch(Circle((0, 0), 0.22, fc="#bbbbbb", ec="black", lw=1.4, zorder=4))
    ax.text(0, -0.38, "nut", ha="center", va="top", fontsize=9.5)
    ax.plot([0, end[0]], [0, 0], color="#555555", lw=7, solid_capstyle="round", zorder=3)
    a = math.radians(180 - ang_deg)
    ux, uy = math.cos(a), math.sin(a)
    tip = (end[0] + 1.4 * ux, end[1] + 1.4 * uy)
    ax.add_patch(FancyArrowPatch(end, tip, arrowstyle="-|>", mutation_scale=16, lw=2, color="black", zorder=5))
    ax.text(tip[0] + 0.1, tip[1] + 0.05, F_label, ha="left", va="bottom", fontsize=10)
    far = (end[0] + 3.2 * ux, end[1] + 3.2 * uy)
    ax.plot([end[0], far[0]], [end[1], far[1]], color="black", lw=0.9, ls=":")
    t = -(end[0] * ux + end[1] * uy)
    foot = (end[0] + t * ux, end[1] + t * uy)
    ax.plot([0, foot[0]], [0, foot[1]], color="#c00000", lw=1.3, ls="--")
    ax.text(foot[0] / 2 - 0.12, foot[1] / 2 + 0.08, d_label, ha="right", va="bottom", fontsize=9.5, color="#c00000")
    ax.add_patch(Arc(end, 0.8, 0.8, theta1=180 - ang_deg, theta2=180, lw=1))
    ax.text(end[0] - 0.55, 0.12, f"{ang_deg}°", ha="right", va="bottom", fontsize=9.5)
    ax.text(end[0] / 2, -0.25, f"{L:g} m", ha="center", va="top", fontsize=9.5)
    xs = [0, end[0], tip[0], foot[0], far[0]]
    ys = [0, tip[1], foot[1], far[1]]
    ax.set_xlim(min(xs) - 0.7, max(xs) + 0.9)
    ax.set_ylim(min(ys) - 0.7, max(ys) + 0.4)
    return _png(fig)


def ladder_wall(x_label, h_label, W_label="W"):
    """A uniform ladder against a smooth wall: weight at its midpoint, horizontal wall force at the top, foot distance and height labelled."""
    fig, ax = _fig(3.8, 3.8)
    X0, H = 1.3, 2.8
    ax.plot([X0 + 0.0, X0 + 0.0], [0, 3.2], color="black", lw=2)
    for yy in np.arange(0.1, 3.2, 0.25):
        ax.plot([X0, X0 + 0.15], [yy, yy + 0.15], color="black", lw=0.8)
    ax.plot([-0.6, X0 + 0.2], [0, 0], color="black", lw=2)
    ax.plot([0, X0], [0, H], color="#8b5a2b", lw=5, solid_capstyle="butt")
    mx, my = X0 / 2, H / 2
    ax.plot([mx], [my], "o", color="black", ms=5, zorder=5)
    ax.add_patch(FancyArrowPatch((mx, my), (mx, my - 0.9), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black"))
    ax.text(mx - 0.08, my - 0.9, W_label, ha="right", va="top", fontsize=10)
    ax.add_patch(FancyArrowPatch((X0, H), (X0 - 0.8, H), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black"))
    ax.text(X0 - 0.85, H + 0.08, "F", ha="right", va="bottom", fontsize=10)
    ax.add_patch(FancyArrowPatch((0, -0.3), (X0, -0.3), arrowstyle="<|-|>", mutation_scale=10, lw=0.9, color="black"))
    ax.text(X0 / 2, -0.38, x_label, ha="center", va="top", fontsize=9.5)
    ax.add_patch(FancyArrowPatch((X0 + 0.45, 0), (X0 + 0.45, H), arrowstyle="<|-|>", mutation_scale=10, lw=0.9, color="black"))
    ax.text(X0 + 0.55, H / 2, h_label, ha="left", va="center", fontsize=9.5)
    ax.text(-0.05, 0.1, "foot", ha="right", va="bottom", fontsize=9)
    ax.set_xlim(-0.9, X0 + 1.6)
    ax.set_ylim(-0.8, 3.4)
    return _png(fig)


def drop_sketch(h_label, body_label=None):
    """An object released from rest at height h above the ground, with its path dashed and the height marked."""
    fig, ax = _fig(3.0, 3.4)
    ax.plot([-0.4, 2.6], [0, 0], color="black", lw=1.6)
    for xx in np.arange(-0.3, 2.6, 0.25):
        ax.plot([xx, xx - 0.15], [0, -0.15], color="black", lw=0.8)
    ax.add_patch(Circle((1.0, 2.6), 0.17, fc="#bbbbbb", ec="black", lw=1.3, zorder=4))
    ax.add_patch(Circle((1.0, 0.17), 0.17, fc="none", ec="black", lw=1.0, ls="--"))
    ax.plot([1.0, 1.0], [2.4, 0.4], color="#555555", lw=1, ls=":")
    ax.add_patch(FancyArrowPatch((1.0, 1.7), (1.0, 1.2), arrowstyle="-|>", mutation_scale=12, lw=1.2, color="black"))
    if body_label:
        ax.text(1.25, 2.6, body_label, ha="left", va="center", fontsize=9.5)
    ax.text(1.25, 2.3, "released from rest", ha="left", va="top", fontsize=8.5)
    ax.add_patch(FancyArrowPatch((0.2, 0), (0.2, 2.6), arrowstyle="<|-|>", mutation_scale=10, lw=1, color="black"))
    ax.text(0.1, 1.3, h_label, ha="right", va="center", fontsize=10)
    ax.set_xlim(-0.9, 2.8)
    ax.set_ylim(-0.3, 3.0)
    return _png(fig)


def cro_trace(period_div, amp_div, timebase_label=None, second=None):
    """Oscilloscope screen, 10 x 8 divisions, with a sine trace of the given period and amplitude (in divisions).
    second: optional (period_div, amp_div) drawn dashed for comparison."""
    fig, ax = _fig(4.4, 3.6)
    ax.add_patch(Rectangle((0, -4), 10, 8, fc="#f4f8f4", ec="black", lw=1.6))
    for i in range(1, 10):
        ax.plot([i, i], [-4, 4], color="#9aa89a", lw=0.6)
    for j in range(-3, 4):
        ax.plot([0, 10], [j, j], color="#9aa89a", lw=0.6 if j else 0.9)
    xs = np.linspace(0, 10, 600)
    ax.plot(xs, amp_div * np.sin(2 * np.pi * xs / period_div), color="black", lw=1.8)
    if second:
        ax.plot(xs, second[1] * np.sin(2 * np.pi * xs / second[0]), color="black", lw=1.4, ls="--")
    if timebase_label:
        ax.text(5, -4.4, timebase_label, ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-0.3, 10.3)
    ax.set_ylim(-5.2, 4.3)
    return _png(fig)
