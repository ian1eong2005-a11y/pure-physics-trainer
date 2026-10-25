"""Chapter 4 Turning Effects of Forces (6091) bank extension: calculation templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2016-2025: forearm, ladder, plank with weights, toy mobile, ramp on lorry, pivoted window)."""
import math

from .. import figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, template


def beam(L, piv, forces, dims=None, uniform=False, wl=None):
    return sketches.beam(L, piv, forces, dist_labels=dims, uniform=uniform, weight_label=wl)


# ================================================================== L1
@template("c4x_moment_cm_to_nm", chapter=4, level=1, lo="4b")
def moment_cm_to_nm(rng):
    F = nice(rng, 20, 25, 40, 50, 80)
    d_cm = nice(rng, 15, 20, 25, 30, 40)
    M = F * d_cm / 100
    return mk(rng, M, [(F * d_cm, "That is in N cm. Convert the distance to metres first."), (F / (d_cm / 100), "Moment = force × distance, not ÷."), (F * d_cm / 10, "1 m = 100 cm.")],
              "N m", f"A force of **{F} N** is applied at right angles to a door, **{d_cm} cm** from the hinge (Fig. 1). What is the moment about the hinge?",
              "moment = F × perpendicular distance (in m)", [f"d = {d_cm} cm = {fmt(d_cm / 100)} m", f"M = {F} × {fmt(d_cm / 100)} = **{fmt(M)} N m**"],
              ["Moment = force × perpendicular distance.", "Put the distance in metres.", "Multiply."], figure=beam(1.0, 0.0, [(f"{F} N", d_cm / 100, "down")], [(0.0, d_cm / 100, f"{d_cm} cm")]))


@template("c4x_balance_force_simple", chapter=4, level=1, lo="4d")
def balance_force_simple(rng):
    F1 = nice(rng, 10, 20, 30, 40)
    d1, d2 = rng.choice([(0.4, 0.8), (0.6, 0.3), (0.5, 1.0), (0.8, 0.4), (0.3, 0.9)])
    F2 = F1 * d1 / d2
    return mk(rng, F2, [(F1, "Equal forces balance only at equal distances."), (F1 * d2 / d1, "You have the distances the wrong way round: F₁d₁ = F₂d₂."), (F1 * d1, "That is the moment, not the force.")],
              "N", f"A see-saw balances (Fig. 1): a child pushes down with **{F1} N** at **{fmt(d1)} m** from the pivot on one side. What downward force at **{fmt(d2)} m** on the other side balances it?",
              "principle of moments: F₁ d₁ = F₂ d₂", [f"{F1} × {fmt(d1)} = F × {fmt(d2)}", f"F = **{fmt(F2)} N**"],
              ["For balance, clockwise moment = anticlockwise moment.", "Write F₁d₁ = F₂d₂.", "Solve for F₂."], figure=beam(2.0, 1.0, [(f"{F1} N", 1.0 - d1, "down"), ("F = ?", 1.0 + d2, "down")], [(1.0 - d1, 1.0, f"{fmt(d1)} m"), (1.0, 1.0 + d2, f"{fmt(d2)} m")]))


@template("c4x_balance_distance_simple", chapter=4, level=1, lo="4d")
def balance_distance_simple(rng):
    F1, F2 = rng.choice([(20, 40), (30, 15), (50, 25), (12, 24), (40, 10)])
    d1 = nice(rng, 0.2, 0.3, 0.4, 0.5)
    d2 = F1 * d1 / F2
    return mk(rng, d2, [(d1, "The distances are only equal if the forces are equal."), (F2 * d1 / F1, "F₁d₁ = F₂d₂: the bigger force needs the SMALLER distance."), (F1 * d1, "That is the moment, not a distance.")],
              "m", f"A weight of **{F1} N** hangs **{fmt(d1)} m** from the pivot of a balanced rod. A weight of **{F2} N** hangs on the other side (Fig. 1). How far from the pivot is it?",
              "F₁ d₁ = F₂ d₂ → d₂ = F₁ d₁ ÷ F₂", [f"{F1} × {fmt(d1)} = {F2} × d", f"d = **{fmt(d2)} m**"],
              ["Use the principle of moments.", "The moment on each side is equal.", "Divide by the second force."], figure=beam(2.0, 1.0, [(f"{F1} N", 1.0 - d1, "down"), (f"{F2} N", 1.0 + min(d2, 0.95), "down")], [(1.0 - d1, 1.0, f"{fmt(d1)} m")]))


@template("c4x_is_balanced_check", chapter=4, level=1, lo="4d")
def is_balanced_check(rng):
    F1, d1 = nice(rng, 10, 20, 30), nice(rng, 0.3, 0.4, 0.6)
    F2 = nice(rng, 15, 20, 40)
    d2 = nice(rng, 0.3, 0.45, 0.6)
    m1, m2 = F1 * d1, F2 * d2
    ans = "anticlockwise moment is larger: the left end goes down" if m1 > m2 else ("balanced" if abs(m1 - m2) < 1e-9 else "clockwise moment is larger: the right end goes down")
    opts = {"anticlockwise moment is larger: the left end goes down": "Compare F × d on each side.", "clockwise moment is larger: the right end goes down": "Compare F × d on each side.",
            "balanced": "The two moments are not equal.", "the side with the larger force always goes down": "The distance matters too: compare moments, not forces."}
    wrongs = {k: v for k, v in opts.items() if k != ans}
    return mkt(rng, ans, dict(list(wrongs.items())[:3]),
               f"A rod is pivoted at its centre (Fig. 1). **{F1} N** acts **{fmt(d1)} m** to the left of the pivot and **{F2} N** acts **{fmt(d2)} m** to the right. What happens?",
               "compare anticlockwise (left) and clockwise (right) moments", [f"left: {F1} × {fmt(d1)} = {fmt(m1)} N m; right: {F2} × {fmt(d2)} = {fmt(m2)} N m", f"**{ans}**"],
               ["Work out the moment on each side.", "Moment = F × d.", "Which is bigger?"], figure=beam(2.0, 1.0, [(f"{F1} N", 1.0 - d1, "down"), (f"{F2} N", 1.0 + d2, "down")], [(1.0 - d1, 1.0, f"{fmt(d1)} m"), (1.0, 1.0 + d2, f"{fmt(d2)} m")]))


@template("c4x_uniform_cg_distance", chapter=4, level=1, lo="4e")
def uniform_cg_distance(rng):
    L = nice(rng, 1.0, 2.0, 3.0, 4.0)
    p = nice(rng, 0.1, 0.2, 0.25) * L
    d = L / 2 - p
    return mk(rng, d, [(L / 2, "That is the distance of the centre of gravity from the END, not from the pivot."), (p, "That is the pivot's distance from the end."), (L - p, "The weight acts at the centre of the uniform beam.")],
              "m", f"A uniform plank **{fmt(L)} m** long is pivoted **{fmt(p)} m** from one end (Fig. 1). How far from the pivot does its weight act?",
              "a uniform beam's weight acts at its centre (centre of gravity)", [f"centre = {fmt(L / 2)} m from the end", f"distance from pivot = {fmt(L / 2)} − {fmt(p)} = **{fmt(d)} m**"],
              ["Where is the centre of gravity of a uniform beam?", "At its midpoint.", "Subtract the pivot's position."], figure=beam(L, p, [], [(0, p, f"{fmt(p)} m")], uniform=True))


@template("c4x_uniform_weight_moment", chapter=4, level=1, lo="4e")
def uniform_weight_moment(rng):
    W = nice(rng, 10, 20, 30, 50)
    L = nice(rng, 1.0, 2.0)
    p = 0.0
    M = W * L / 2
    return mk(rng, M, [(W * L, "The weight acts at the CENTRE, L/2 from the end pivot."), (W / 2, "Moment = W × distance to the centre of gravity."), (W, "Multiply by the distance.")],
              "N m", f"A uniform shelf of weight **{W} N** and length **{fmt(L)} m** is hinged at one end (Fig. 1). What is the moment of its weight about the hinge?",
              "weight acts at the centre of gravity (L/2 for a uniform shelf); M = W × L/2", [f"d = {fmt(L)} ÷ 2 = {fmt(L / 2)} m", f"M = {W} × {fmt(L / 2)} = **{fmt(M)} N m**"],
              ["Where does the weight of a uniform object act?", "At its centre.", "Moment = W × d."], figure=beam(L, p, [], [(0, L / 2, f"{fmt(L / 2)} m")], uniform=True, wl=f"{W} N"))


@template("c4x_most_stable_table", chapter=4, level=1, lo="4f")
def most_stable_table(rng):
    items = [("P", 4, 6, 3), ("Q", 8, 4, 1.6), ("R", 3, 8, 4.5), ("S", 5, 6, 3.5)]
    rng.shuffle(items)
    best = max(items, key=lambda t: (t[1] / 2) / t[3])[0]
    wrongs = {n: f"{n} has a {'narrower base' if w < 8 else 'base'} and a {'higher' if c > 1.6 else 'similar'} centre of gravity, so it topples more easily." for n, w, h, c in items if n != best}
    return mkt(rng, best, wrongs, "Fig. 1 shows four objects drawn to the same scale, with their centres of gravity G marked. Which object is the most stable?",
               "most stable: widest base and lowest centre of gravity", [f"**{best}** has the widest base and the lowest G, so it must tilt furthest before G passes over the edge of the base"],
               ["What two features make an object stable?", "A wide base and a low centre of gravity.", "Find the object that has both."], figure=figs2.stability_shapes(items))


@template("c4x_least_stable_table", chapter=4, level=1, lo="4f")
def least_stable_table(rng):
    items = [("W", 6, 3, 1.2), ("X", 2, 8, 5), ("Y", 5, 5, 2.5), ("Z", 4, 4, 1.5)]
    rng.shuffle(items)
    worst = min(items, key=lambda t: (t[1] / 2) / t[3])[0]
    wrongs = {n: f"{n} has a wider base or lower centre of gravity than the least stable object." for n, w, h, c in items if n != worst}
    table = md_table(["object", "base width / cm", "height of G above base / cm"], [[n, w, c] for n, w, h, c in items])
    return mkt(rng, worst, wrongs, f"The table gives data for four objects.\n\n{table}\n\nWhich object topples most easily?",
               "least stable: narrowest base and highest centre of gravity", [f"**{worst}** has the narrowest base and the highest G"],
               ["Which features make toppling easy?", "Narrow base, high centre of gravity.", "Find the object with both."])


@template("c4x_moment_hand", chapter=4, level=1, lo="4b")
def moment_hand(rng):
    F = nice(rng, 30, 40, 50, 60)
    d = nice(rng, 0.2, 0.25, 0.3, 0.4)
    return mk(rng, F * d, [(F / d, "Multiply force by distance."), (F + d, "Moment = F × d."), (F * d * 2, "Use the distance from the pivot to the force only.")],
              "N m", f"A mechanic pushes a spanner handle with **{F} N** at right angles, **{fmt(d)} m** from the nut (Fig. 1). What moment does she apply to the nut?",
              "moment = F × perpendicular distance", [f"M = {F} × {fmt(d)} = **{fmt(F * d)} N m**"],
              ["Moment = force × distance from the pivot.", "The nut is the pivot.", "Multiply."], figure=beam(0.5, 0.0, [(f"{F} N", d, "down")], [(0, d, f"{fmt(d)} m")]))


# ================================================================== L2
@template("c4x_force_from_moment", chapter=4, level=2, lo="4b")
def force_from_moment(rng):
    M = nice(rng, 12, 15, 20, 24, 30)
    d = nice(rng, 0.2, 0.3, 0.4, 0.5)
    return mk(rng, M / d, [(M * d, "F = M ÷ d."), (d / M, "F = M ÷ d, not d ÷ M."), (M, "That is the moment, not the force.")],
              "N", f"A nut needs a moment of **{M} N m** to loosen it. A spanner applies the force **{fmt(d)} m** from the nut, at right angles (Fig. 1). What force is needed?",
              "M = F d → F = M ÷ d", [f"F = {M} ÷ {fmt(d)} = **{fmt(M / d)} N**"],
              ["Rearrange moment = F × d.", "Divide the moment by the distance.", f"{M} ÷ {fmt(d)}."], figure=beam(0.6, 0.0, [("F = ?", d, "down")], [(0, d, f"{fmt(d)} m")]))


@template("c4x_distance_from_moment", chapter=4, level=2, lo="4b")
def distance_from_moment(rng):
    F = nice(rng, 20, 25, 40, 50)
    M = nice(rng, 10, 12, 15, 20)
    d = M / F
    return mk(rng, d * 100, [(d, "That is in metres; the answer is in cm."), (F / M * 100, "d = M ÷ F."), (M * F, "d = M ÷ F.")],
              "cm", f"A force of **{F} N** must produce a moment of **{M} N m** about a hinge.\n\n{md_table(['quantity', 'value'], [['force (at right angles)', f'{F} N'], ['moment needed', f'{M} N m']])}\n\nHow far from the hinge must it act, in cm?",
              "d = M ÷ F (m), then × 100 for cm", [f"d = {M} ÷ {F} = {fmt(d)} m", f"= **{fmt(d * 100)} cm**"],
              ["Rearrange M = F d.", "That gives metres.", "Convert to cm."])


@template("c4x_balance_unknown_weight", chapter=4, level=2, lo="4d")
def balance_unknown_weight(rng):
    F1 = nice(rng, 3, 4, 5, 6)
    d1, d2 = rng.choice([(30, 20), (24, 36), (40, 25), (15, 45), (20, 40)])
    F2 = F1 * d1 / d2
    return mk(rng, F2, [(F1 * d2 / d1, "F₁d₁ = F₂d₂: check which distance goes with which force."), (F1, "Equal weights balance only at equal distances."), (F1 * d1, "That is a moment (N cm), not a weight.")],
              "N", f"A toy mobile is balanced (Fig. 1). A **{F1} N** model hangs **{d1} cm** from the thread; a second model hangs **{d2} cm** on the other side. What is its weight?",
              "F₁ d₁ = F₂ d₂ (any consistent distance unit)", [f"{F1} × {d1} = W × {d2}", f"W = **{fmt(F2)} N**"],
              ["The mobile is balanced: use the principle of moments.", "Distances in cm are fine if both are in cm.", "Solve for W."], figure=beam(d1 + d2 + 10, 5 + d1, [(f"{F1} N", 5, "down"), ("W = ?", 5 + d1 + d2, "down")], [(5, 5 + d1, f"{d1} cm"), (5 + d1, 5 + d1 + d2, f"{d2} cm")]))


@template("c4x_rule_mass_balance", chapter=4, level=2, lo="4d")
def rule_mass_balance(rng):
    m1 = nice(rng, 100, 200, 300)
    x1 = nice(rng, 10, 20, 30)
    x2 = nice(rng, 70, 80, 90)
    m2 = m1 * (50 - x1) / (x2 - 50)
    return mk(rng, m2, [(m1, "The masses balance only at equal distances from the 50 cm mark."), (m1 * (x2 - 50) / (50 - x1), "Distances are measured from the PIVOT (50 cm mark); check which goes with which mass."), (m1 * x1 / x2, "Measure distances from the pivot, not from the 0 cm end.")],
              "g", f"A metre rule is balanced at its 50 cm mark. A **{m1} g** mass hangs at the **{x1} cm** mark. Where a second mass hangs at the **{x2} cm** mark, the rule balances (Fig. 1). What is the second mass?",
              "moments about the pivot: m₁ d₁ = m₂ d₂ (distances from the 50 cm mark)", [f"d₁ = 50 − {x1} = {50 - x1} cm; d₂ = {x2} − 50 = {x2 - 50} cm", f"m₂ = {m1} × {50 - x1} ÷ {x2 - 50} = **{fmt(m2)} g**"],
              ["Measure each distance from the pivot.", "Use the principle of moments.", "Solve for the second mass."], figure=beam(100, 50, [(f"{m1} g", x1, "down"), ("? g", x2, "down")], [(x1, 50, f"{50 - x1} cm"), (50, x2, f"{x2 - 50} cm")]))


@template("c4x_balance_two_weights_find_d", chapter=4, level=2, lo="4d")
def balance_two_weights_find_d(rng):
    W1, W2 = rng.choice([(400, 300), (500, 250), (600, 400), (300, 450)])
    d1 = nice(rng, 1.2, 1.5, 1.8, 2.0)
    d2 = W1 * d1 / W2
    return mk(rng, d2, [(d1, "Different weights need different distances."), (W2 * d1 / W1, "W₁d₁ = W₂d₂: the lighter person sits further out."), (d1 * 2, "Use the ratio of the weights.")],
              "m", f"Two children sit on a see-saw (Fig. 1). One of weight **{W1} N** sits **{fmt(d1)} m** from the pivot. How far from the pivot must the other child, of weight **{W2} N**, sit to balance?",
              "W₁ d₁ = W₂ d₂", [f"{W1} × {fmt(d1)} = {W2} × d", f"d = **{fmt(d2)} m**"],
              ["Use the principle of moments.", "Equal moments on each side.", "Solve for d."], figure=beam(5.0, 2.5, [(f"{W1} N", 2.5 - d1, "down"), (f"{W2} N", min(4.9, 2.5 + d2), "down")], [(2.5 - d1, 2.5, f"{fmt(d1)} m")]))


@template("c4x_beam_weight_from_balance", chapter=4, level=2, lo="4e")
def beam_weight_from_balance(rng):
    L = 1.0
    p = nice(rng, 0.3, 0.35, 0.4)
    F = nice(rng, 2, 3, 4, 5)
    x = nice(rng, 0.05, 0.1, 0.15)
    W = F * (p - x) / (0.5 - p)
    return mk(rng, W, [(F, "The rule's own weight acts at its centre (50 cm), so its moment arm is 0.5 − p."), (F * (0.5 - p) / (p - x), "Check which distance goes with which force."), (F * (p - x), "That is the moment of the hanging weight.")],
              "N", f"A uniform metre rule balances on a pivot at the **{round(p * 100)} cm** mark when a **{F} N** weight hangs at the **{round(x * 100)} cm** mark (Fig. 1). What is the weight of the rule?",
              "rule's weight acts at 50 cm; F × (p − x) = W × (50 − p)", [f"{F} × {fmt(p - x)} = W × {fmt(0.5 - p)}", f"W = **{fmt(W)} N**"],
              ["Where does the rule's weight act?", "At the 50 cm mark (its centre of gravity).", "Take moments about the pivot."], figure=beam(L, p, [(f"{F} N", x, "down")], [(x, p, f"{fmt(p - x)} m"), (p, 0.5, f"{fmt(0.5 - p)} m")], uniform=True, wl="W"))


@template("c4x_cg_position_lamina", chapter=4, level=2, lo="4e")
def cg_position_lamina(rng):
    L = nice(rng, 1.0, 1.2, 2.0)
    W = nice(rng, 20, 30, 40)
    F_up = nice(rng, 10, 12, 15)
    d = F_up * L / W
    return mk(rng, d, [(L / 2, "The rod is NOT uniform here; find its centre of gravity from moments."), (W * L / F_up, "Take moments about the hinge: F × L = W × d."), (L - d, "Measure from the hinge end.")],
              "m", f"A non-uniform pole of weight **{W} N** and length **{fmt(L)} m** is hinged at one end and held horizontal by an upward force of **{F_up} N** at the other end (Fig. 1). How far from the hinge is its centre of gravity?",
              "moments about the hinge: F × L = W × d", [f"{F_up} × {fmt(L)} = {W} × d", f"d = **{fmt(d)} m**"],
              ["Take moments about the hinge.", "Upward force at the far end, weight at the centre of gravity.", "Solve for d."], figure=beam(L, 0.0, [(f"{F_up} N", L, "up"), (f"{W} N", d, "down")]))


@template("c4x_tilt_angle_block", chapter=4, level=2, lo="4f")
def tilt_angle_block(rng):
    w, h = rng.choice([(4, 8), (3, 10), (6, 8), (5, 12), (4, 6)])
    ang = math.degrees(math.atan((w / 2) / (h / 2)))
    return mk(rng, ang, [(90 - ang, "Measure the angle from the vertical position: tan θ = (half base) ÷ (height of G)."), (math.degrees(math.atan(w / h / 2)), "G is at half the height: use h/2, not h."), (45, "45° only for a square block.")],
              "°", f"A uniform block **{w} cm** wide and **{h} cm** tall is tilted about one bottom edge (Fig. 1). At what angle of tilt does its centre of gravity lie directly above the edge, so that it is about to topple?",
              "about to topple when G is above the pivot edge: tan θ = (w/2) ÷ (h/2)", [f"G is {fmt(h / 2)} cm high and {fmt(w / 2)} cm in from the edge", f"tan θ = {fmt(w / 2)} ÷ {fmt(h / 2)} → θ = **{fmt(ang, sf=3)}°**"],
              ["Where is the centre of gravity of a uniform block?", "At its centre: w/2 across, h/2 up.", "It topples when G passes over the edge: tan θ = (w/2)/(h/2)."], figure=figs2.tilt_block(w, h, round(ang * 0.6)), sf=3)


@template("c4x_tilt_angle_compare", chapter=4, level=2, lo="4f")
def tilt_angle_compare(rng):
    w = nice(rng, 4, 6)
    h1, h2 = nice(rng, 6, 8), nice(rng, 12, 16)
    a1 = math.degrees(math.atan(w / h1))
    a2 = math.degrees(math.atan(w / h2))
    return mk(rng, a1, [(a2, "That is the TALLER block's tipping angle; it topples sooner."), (math.degrees(math.atan(h1 / w)), "tan θ = (half width) ÷ (height of G) = w / h for a uniform block."), (a1 / 2, "Use tan θ = w ÷ h.")],
              "°", f"Two uniform blocks have the same base width **{w} cm** but heights **{h1} cm** and **{h2} cm**.\n\n{md_table(['block', 'width / cm', 'height / cm'], [['A', w, h1], ['B', w, h2]])}\n\nThrough what angle can the SHORTER block be tilted before it topples?",
              "tipping angle: tan θ = (w/2) ÷ (h/2) = w ÷ h", [f"tan θ = {w} ÷ {h1}", f"θ = **{fmt(a1, sf=3)}°** (the taller block only {fmt(a2, sf=3)}°)"],
              ["G is at the centre of each block.", "tan θ = (w/2)/(h/2).", "Use the shorter block's height."], sf=3)


# ================================================================== L3
@template("c4x_angled_force_moment", chapter=4, level=3, lo="4b")
def angled_force_moment(rng):
    F = nice(rng, 20, 30, 40, 50)
    L = nice(rng, 0.3, 0.4, 0.5)
    ang = nice(rng, 30, 60)
    d_perp = L * math.sin(math.radians(ang))
    return mk(rng, F * d_perp, [(F * L, "Use the PERPENDICULAR distance from the pivot to the line of action, not the length of the spanner."), (F * L * math.cos(math.radians(ang)), "The perpendicular distance is L sin θ (θ between the force and the spanner)."), (F * d_perp * 2, "Check the perpendicular distance.")],
              "N m", f"A force of **{F} N** is applied at the end of a spanner **{fmt(L)} m** long, at **{ang}°** to the spanner. The perpendicular distance from the nut to the line of the force is **{fmt(d_perp, sf=3)} m** (Fig. 1). What is the moment about the nut?",
              "moment = F × perpendicular distance from pivot to line of action", [f"M = {F} × {fmt(d_perp, sf=3)} = **{fmt(F * d_perp, sf=3)} N m**"],
              ["Which distance is used in a moment?", "The perpendicular distance to the force's line of action.", "Multiply by the force."], figure=figs2.spanner_force(L, f"{F} N", ang, f"{fmt(d_perp, sf=3)} m"), sf=3)


@template("c4x_door_handle_force", chapter=4, level=3, lo="4b")
def door_handle_force(rng):
    M = nice(rng, 6, 8, 10, 12)
    d1, d2 = rng.choice([(0.8, 0.2), (0.75, 0.25), (0.9, 0.3), (0.6, 0.15)])
    F1, F2 = M / d1, M / d2
    return mk(rng, F2 - F1, [(F2, "That is the force near the hinge; the question asks how much MORE."), (F1, "That is the force at the handle."), (F2 / F1, "That is the ratio; find the difference in newtons.")],
              "N", f"A door needs a moment of **{M} N m** to open.\n\n{md_table(['push position', 'distance from hinge / m'], [['at the handle', fmt(d1)], ['near the hinge', fmt(d2)]])}\n\nHow much more force is needed near the hinge than at the handle?",
              "F = M ÷ d for each position; subtract", [f"handle: {M} ÷ {fmt(d1)} = {fmt(F1)} N; hinge: {M} ÷ {fmt(d2)} = {fmt(F2)} N", f"difference = **{fmt(F2 - F1)} N**"],
              ["Find the force at each distance.", "F = M ÷ d.", "Subtract."])


@template("c4x_cg_rule_off_centre", chapter=4, level=3, lo="4e")
def cg_rule_off_centre(rng):
    W = nice(rng, 1.0, 1.2, 1.5, 2.0)
    m = nice(rng, 0.5, 1.0, 1.5)
    p = nice(rng, 30, 35, 40)
    x = nice(rng, 0, 5, 10)
    cg = p + m * (p - x) / W
    return mk(rng, cg, [(50, "The rule may not be uniform: find the centre of gravity from the balance."), (p - m * (p - x) / W, "The rule's weight must be on the OTHER side of the pivot from the hanging weight."), (p + W * (p - x) / m, "m (p − x) = W (G − p).")],
              "cm", f"A metre rule of weight **{fmt(W)} N** balances on a pivot at the **{p} cm** mark when a **{fmt(m)} N** weight hangs at the **{x} cm** mark (Fig. 1). At what mark is the rule's centre of gravity?",
              "moments about the pivot: m (p − x) = W (G − p)", [f"{fmt(m)} × {p - x} = {fmt(W)} × (G − {p})", f"G = **{fmt(cg, sf=3)} cm**"],
              ["The rule's weight acts at its centre of gravity G.", "G must be on the opposite side of the pivot from the hanging weight.", "Take moments."], figure=beam(100, p, [(f"{fmt(m)} N", x, "down"), (f"{fmt(W)} N at G", min(99, cg), "down")], [(x, p, f"{p - x} cm")]), sf=3)


@template("c4x_beam_support_force", chapter=4, level=3, lo="4e")
def beam_support_force(rng):
    W = nice(rng, 100, 200, 300)
    L = nice(rng, 2.0, 3.0, 4.0)
    F = W / 2
    return mk(rng, F, [(W, "Two supports share the weight; for a uniform beam supported at both ends each takes half."), (W / 4, "Take moments about one support: F × L = W × L/2."), (W * L, "That is a moment, not a force.")],
              "N", f"A uniform plank of weight **{W} N** and length **{fmt(L)} m** rests on two supports, one at each end (Fig. 1). What upward force does each support provide?",
              "weight acts at the centre; moments about one end: F × L = W × L/2", [f"F × {fmt(L)} = {W} × {fmt(L / 2)}", f"F = **{fmt(F)} N** at each end"],
              ["Where does the plank's weight act?", "At the centre, equally far from each support.", "Take moments about one end."], figure=beam(L, None, [("F", 0.05, "up"), ("F", L - 0.05, "up")], uniform=True, wl=f"{W} N"))


@template("c4x_two_forces_one_side", chapter=4, level=3, lo="4d")
def two_forces_one_side(rng):
    F1, d1 = nice(rng, 10, 20), nice(rng, 0.2, 0.4)
    F2, d2 = nice(rng, 15, 30), nice(rng, 0.6, 0.8)
    d3 = nice(rng, 0.5, 0.8, 1.0)
    F3 = (F1 * d1 + F2 * d2) / d3
    return mk(rng, F3, [((F1 + F2) * d1 / d3, "Each force has its own distance: add the MOMENTS, not the forces."), (F1 + F2, "The balancing force need not equal the total weight."), (F2 * d2 / d3, "Include both moments on the left side.")],
              "N", f"Two weights hang to the left of a pivot: **{F1} N** at **{fmt(d1)} m** and **{F2} N** at **{fmt(d2)} m** (Fig. 1). What single weight hung **{fmt(d3)} m** to the right balances them?",
              "sum of anticlockwise moments = sum of clockwise moments", [f"anticlockwise = {F1}×{fmt(d1)} + {F2}×{fmt(d2)} = {fmt(F1 * d1 + F2 * d2)} N m", f"F = {fmt(F1 * d1 + F2 * d2)} ÷ {fmt(d3)} = **{fmt(F3, sf=3)} N**"],
              ["Find the moment of each left-hand weight.", "Add them.", "Divide by the right-hand distance."], figure=beam(2.0, 1.0, [(f"{F1} N", 1.0 - d1, "down"), (f"{F2} N", 1.0 - d2, "down"), ("F = ?", 1.0 + d3 * 0.95, "down")], [(1.0 - d2, 1.0, f"{fmt(d2)} m")]), sf=3)


@template("c4x_forearm_muscle", chapter=4, level=3, lo="4d")
def forearm_muscle(rng):
    W = nice(rng, 20, 30, 40, 50)
    d_ball = nice(rng, 0.30, 0.32, 0.35)
    d_m = nice(rng, 0.04, 0.05)
    F = W * d_ball / d_m
    return mk(rng, F, [(W, "The muscle acts very close to the elbow, so it must pull much harder than the weight."), (W * d_m / d_ball, "F × d_muscle = W × d_ball: you have the distances swapped."), (W * d_ball, "That is the moment of the ball.")],
              "N", f"A forearm is held horizontal with a **{W} N** ball in the hand, **{fmt(d_ball)} m** from the elbow. The biceps muscle pulls upwards **{fmt(d_m)} m** from the elbow (Fig. 1). Ignoring the arm's weight, what force must the muscle provide?",
              "moments about the elbow: F × d_muscle = W × d_ball", [f"F × {fmt(d_m)} = {W} × {fmt(d_ball)}", f"F = **{fmt(F)} N**"],
              ["The elbow is the pivot.", "Clockwise moment of the ball = anticlockwise moment of the muscle.", "Solve for F."], figure=beam(0.4, 0.0, [("F", d_m, "up"), (f"{W} N", d_ball, "down")], [(0, d_ball, f"{fmt(d_ball)} m")]))


@template("c4x_tilt_which_topples", chapter=4, level=3, lo="4f")
def tilt_which_topples(rng):
    tilt = nice(rng, 25, 30, 35)
    items = [("A", 4, 12), ("B", 6, 8), ("C", 8, 6), ("D", 5, 10)]
    topples = [n for n, w, h in items if math.degrees(math.atan(w / h)) < tilt]
    ans = ", ".join(topples) if topples else "none"
    if len(topples) == 0 or len(topples) == 4:
        tilt = 30
        topples = [n for n, w, h in items if math.degrees(math.atan(w / h)) < tilt]
        ans = ", ".join(topples)
    allopts = ["A only", "A and D", "A, B and D", "none of them"]
    ans_text = {"A": "A only", "A, D": "A and D", "A, B, D": "A, B and D"}.get(ans, ans)
    wrongs = {o: "Compare each block's tipping angle (tan θ = width ÷ height) with the tilt." for o in allopts if o != ans_text}
    table = md_table(["block", "width / cm", "height / cm"], [[n, w, h] for n, w, h in items])
    return mkt(rng, ans_text, dict(list(wrongs.items())[:3]), f"Four uniform blocks stand on a board that is tilted to **{tilt}°**.\n\n{table}\n\nWhich blocks topple?",
               "a block topples if the tilt exceeds its tipping angle, tan θ = w ÷ h", [", ".join(f"{n}: {fmt(math.degrees(math.atan(w / h)), sf=3)}°" for n, w, h in items), f"toppling (angle < {tilt}°): **{ans_text}**"],
               ["Work out each block's tipping angle.", "tan θ = (w/2)/(h/2) = w/h.", f"Compare with {tilt}°."])


@template("c4x_tilt_angle_cg_height", chapter=4, level=3, lo="4f")
def tilt_angle_cg_height(rng):
    w = nice(rng, 1.6, 1.8, 2.0)
    hg = nice(rng, 0.8, 1.0, 1.2)
    ang = math.degrees(math.atan((w / 2) / hg))
    return mk(rng, ang, [(math.degrees(math.atan(w / hg)), "Use HALF the wheel base: G is above the middle of the base."), (90 - ang, "Measure the tilt from the upright position."), (math.degrees(math.atan(hg / (w / 2))), "tan θ = (half width) ÷ (height of G).")],
              "°", f"A car has a wheel base (track) of **{fmt(w)} m** and its centre of gravity is **{fmt(hg)} m** above the road, midway between the wheels (Fig. 1). Through what angle can it be tilted sideways before it topples?",
              "topples when G passes over the wheels: tan θ = (w/2) ÷ h_G", [f"tan θ = {fmt(w / 2)} ÷ {fmt(hg)}", f"θ = **{fmt(ang, sf=3)}°**"],
              ["Where is G relative to the wheels?", "It must pass over the lower wheels for the car to tip.", "tan θ = (w/2)/h."], figure=figs2.tilt_block(w, 2 * hg, round(ang * 0.5)), sf=3)


# ================================================================== L4
@template("c4x_window_force", chapter=4, level=4, lo="4d")
def window_force(rng):
    W = nice(rng, 80, 100, 120)
    dW = nice(rng, 0.2, 0.25, 0.3)
    dF = nice(rng, 0.5, 0.6, 0.7)
    F = W * dW / dF
    return mk(rng, F, [(W, "The force is further from the pivot than the window's centre of gravity, so it can be smaller than the weight."), (W * dF / dW, "Check which distance goes with which force."), (W * dW, "That is the moment of the weight.")],
              "N", f"A pivoted window of weight **{W} N** has its centre of gravity **{fmt(dW)} m** from the pivot. It is held open by a force at right angles **{fmt(dF)} m** from the pivot (Fig. 1). What is the size of the force?",
              "moments about the pivot: F × d_F = W × d_W", [f"F × {fmt(dF)} = {W} × {fmt(dW)}", f"F = **{fmt(F, sf=3)} N**"],
              ["Take moments about the pivot.", "The weight acts at the centre of gravity.", "Solve for F."], figure=beam(dF + 0.1, 0.0, [(f"{W} N", dW, "down"), ("F", dF, "up")], [(0, dW, f"{fmt(dW)} m"), (0, dF, f"{fmt(dF)} m")]), sf=3)


@template("c4x_ladder_wall", chapter=4, level=4, lo="4d")
def ladder_wall(rng):
    W = nice(rng, 150, 200, 240)
    L = nice(rng, 4.0, 5.0)
    x = nice(rng, 1.2, 1.5)
    h = math.sqrt(L * L - x * x)
    F = W * (x / 2) / h
    return mk(rng, F, [(W * x / h, "The ladder's weight acts at its MIDDLE, x/2 horizontally from the foot."), (W * (x / 2) / L, "Use the perpendicular (vertical) distance h to the wall force, not the ladder length."), (W / 2, "Take moments about the foot.")],
              "N", f"A uniform ladder of weight **{W} N** leans against a smooth wall. Its foot is **{fmt(x)} m** from the wall and its top is **{fmt(h, sf=3)} m** up the wall. The wall pushes horizontally on the top (Fig. 1). Taking moments about the foot, what is the force from the wall?",
              "moments about the foot: F_wall × h = W × (x/2)", [f"F × {fmt(h, sf=3)} = {W} × {fmt(x / 2)}", f"F = **{fmt(F, sf=3)} N**"],
              ["The weight of a uniform ladder acts at its midpoint.", "Its perpendicular distance from the foot is half the horizontal distance.", "The wall force is horizontal; its moment arm is the height h."], figure=figs2.ladder_wall(f"{fmt(x)} m", f"{fmt(h, sf=3)} m", f"{W} N"), sf=3)


@template("c4x_ramp_lorry", chapter=4, level=4, lo="4d")
def ramp_lorry(rng):
    W = nice(rng, 150, 165, 180)
    dW = nice(rng, 100, 120)
    dF = nice(rng, 220, 240)
    F = W * dW / dF
    return mk(rng, F, [(W, "The lifting force acts further from the pivot than the weight, so it is smaller."), (W * dF / dW, "F × d_F = W × d_W: check the distances."), (W * dW / 100, "That is the moment in N m, not the force.")],
              "N", f"A ramp of weight **{W} N** is hinged at one end O. Its centre of gravity is **{dW} cm** horizontally from O and it is lifted by a vertical force **{dF} cm** horizontally from O (Fig. 1). What force is needed to hold it in this position?",
              "moments about O: F × d_F = W × d_W", [f"F × {dF} = {W} × {dW}", f"F = **{fmt(F, sf=3)} N**"],
              ["O is the pivot.", "Use horizontal distances (perpendicular to the vertical forces).", "Solve for F."], figure=beam(dF + 20, 0.0, [(f"{W} N", dW, "down"), ("F", dF, "up")], [(0, dW, f"{dW} cm"), (0, dF, f"{dF} cm")]), sf=3)


@template("c4x_beam_weight_load", chapter=4, level=4, lo="4e")
def beam_weight_load(rng):
    L = 4.0
    Wb = nice(rng, 200, 300, 400)
    Wl = nice(rng, 500, 600, 800)
    x = nice(rng, 1.0, 3.0)
    R2 = (Wb * L / 2 + Wl * x) / L
    return mk(rng, R2, [((Wb + Wl) / 2, "The load is not at the centre, so the supports do not share equally."), (Wl * x / L, "Include the beam's own weight acting at its centre."), (Wb + Wl - (Wb * L / 2 + Wl * x) / L + 0.0 if x != 2 else R2 + 50, "That is the force at the OTHER support.")],
              "N", f"A uniform beam **{fmt(L)} m** long and of weight **{Wb} N** rests on supports at each end. A load of **{Wl} N** sits **{fmt(x)} m** from the left support (Fig. 1). What is the upward force at the RIGHT support?",
              "moments about the left support: R × L = W_beam × L/2 + W_load × x", [f"R × {fmt(L)} = {Wb} × 2 + {Wl} × {fmt(x)}", f"R = **{fmt(R2, sf=3)} N**"],
              ["Take moments about the left support.", "The beam's weight acts at its centre (2 m).", "Solve for the right-hand force."], figure=beam(L, None, [("R₁", 0.05, "up"), (f"{Wl} N", x, "down"), ("R₂ = ?", L - 0.05, "up")], [(0, x, f"{fmt(x)} m")], uniform=True, wl=f"{Wb} N"), sf=3)


@template("c4x_net_moment", chapter=4, level=4, lo="4b")
def net_moment(rng):
    F1, d1 = nice(rng, 20, 30, 40), nice(rng, 0.5, 0.6, 0.8)
    F2, d2 = nice(rng, 10, 15, 25), nice(rng, 0.4, 0.5)
    net = abs(F1 * d1 - F2 * d2)
    return mk(rng, net, [(F1 * d1 + F2 * d2, "The forces turn the wheel in OPPOSITE directions; subtract the moments."), (abs(F1 - F2) * (d1 + d2) / 2, "Work out each moment separately."), (F1 * d1, "Include both moments.")],
              "N m", f"Two children push on opposite sides of a roundabout's pivot: **{F1} N** at **{fmt(d1)} m** turning it clockwise, and **{F2} N** at **{fmt(d2)} m** turning it anticlockwise (Fig. 1). What is the resultant moment?",
              "resultant moment = clockwise moment − anticlockwise moment", [f"clockwise {F1}×{fmt(d1)} = {fmt(F1 * d1)} N m; anticlockwise {F2}×{fmt(d2)} = {fmt(F2 * d2)} N m", f"resultant = **{fmt(net)} N m**"],
              ["Find each moment.", "They act in opposite senses.", "Subtract."], figure=beam(2.0, 1.0, [(f"{F1} N", 1.0 + d1, "down"), (f"{F2} N", 1.0 - d2, "down")]))


@template("c4x_moment_two_same", chapter=4, level=4, lo="4b")
def moment_two_same(rng):
    F1, d1 = nice(rng, 10, 20), nice(rng, 0.3, 0.5)
    F2, d2 = nice(rng, 15, 25), nice(rng, 0.6, 0.8)
    tot = F1 * d1 + F2 * d2
    return mk(rng, tot, [(abs(F1 * d1 - F2 * d2), "Both forces turn the bar the SAME way, so their moments add."), ((F1 + F2) * d2, "Each force has its own distance."), ((F1 + F2) * (d1 + d2), "Multiply each force by its own distance, then add.")],
              "N m", f"Two weights hang on the same side of a hinged bar: **{F1} N** at **{fmt(d1)} m** and **{F2} N** at **{fmt(d2)} m** from the hinge (Fig. 1). What is the total moment about the hinge?",
              "moments in the same sense add: M = F₁d₁ + F₂d₂", [f"M = {F1}×{fmt(d1)} + {F2}×{fmt(d2)} = **{fmt(tot)} N m**"],
              ["Do both weights turn the bar the same way?", "Moments in the same direction add.", "Add F₁d₁ and F₂d₂."], figure=beam(1.0, 0.0, [(f"{F1} N", d1, "down"), (f"{F2} N", d2, "down")]))


@template("c4x_bus_tilt_cg", chapter=4, level=4, lo="4f")
def bus_tilt_cg(rng):
    w = nice(rng, 2.0, 2.2, 2.4)
    ang = nice(rng, 35, 40, 45)
    hg = (w / 2) / math.tan(math.radians(ang))
    return mk(rng, hg, [(w / math.tan(math.radians(ang)), "Use half the wheel track: G is midway between the wheels."), ((w / 2) * math.tan(math.radians(ang)), "tan θ = (w/2) ÷ h, so h = (w/2) ÷ tan θ."), (w / 2, "That is half the track, not the height of G.")],
              "m", f"In a tilt test a bus with wheels **{fmt(w)} m** apart only just stays upright when tilted to **{ang}°** (Fig. 1). How high above the road is its centre of gravity?",
              "just about to topple: tan θ = (w/2) ÷ h_G → h_G = (w/2) ÷ tan θ", [f"h = {fmt(w / 2)} ÷ tan {ang}°", f"= **{fmt(hg, sf=3)} m**"],
              ["At the tipping angle, G is directly above the lower wheels.", "Use the triangle with sides w/2 and h.", "Rearrange tan θ = (w/2)/h."], figure=figs2.tilt_block(w, 2 * hg, ang), sf=3)


@template("c4x_load_raises_cg", chapter=4, level=4, lo="4f")
def load_raises_cg(rng):
    w = nice(rng, 2.0, 2.4)
    h1 = nice(rng, 0.8, 1.0)
    h2 = h1 + nice(rng, 0.4, 0.6, 0.8)
    a1 = math.degrees(math.atan((w / 2) / h1))
    a2 = math.degrees(math.atan((w / 2) / h2))
    return mk(rng, a1 - a2, [(a2, "That is the new tipping angle; the question asks how much it has DECREASED."), (a1, "That is the original tipping angle."), (a1 + a2, "Subtract the two angles.")],
              "°", f"A lorry has a wheel track of **{fmt(w)} m**. Loading the roof raises its centre of gravity from **{fmt(h1)} m** to **{fmt(h2)} m** above the road.\n\n{md_table(['', 'height of G / m'], [['empty', fmt(h1)], ['roof loaded', fmt(h2)]])}\n\nBy how much does the maximum safe tilt angle decrease?",
              "tipping angle tan θ = (w/2) ÷ h for each; subtract", [f"empty: θ = tan⁻¹({fmt(w / 2)}/{fmt(h1)}) = {fmt(a1, sf=3)}°", f"loaded: θ = tan⁻¹({fmt(w / 2)}/{fmt(h2)}) = {fmt(a2, sf=3)}°", f"decrease = **{fmt(a1 - a2, sf=2)}°**"],
              ["Find both tipping angles.", "tan θ = (w/2)/h.", "Subtract."], sf=2)


# ================================================================== L5
@template("c4x_two_supports_unknown", chapter=4, level=5, lo="4d")
def two_supports_unknown(rng):
    L = nice(rng, 3.0, 4.0, 5.0)
    W = nice(rng, 400, 500, 600)
    x = nice(rng, 1.0, 1.5)
    R2 = W * x / L
    R1 = W - R2
    return mk(rng, R1, [(R2, "That is the force at the FAR support; the near support takes more of the load."), (W / 2, "The load is not at the centre."), (W, "Two supports share the load.")],
              "N", f"A light plank **{fmt(L)} m** long rests on supports at its ends. A man of weight **{W} N** stands **{fmt(x)} m** from the LEFT support (Fig. 1). What is the upward force from the left support?",
              "moments about the right support: R₁ × L = W × (L − x); or R₂ from the left and R₁ = W − R₂", [f"R₂ × {fmt(L)} = {W} × {fmt(x)} → R₂ = {fmt(R2)} N", f"R₁ = {W} − {fmt(R2)} = **{fmt(R1)} N**"],
              ["Take moments about one support to find the other's force.", "The upward forces add up to the weight.", "Find R₁."], figure=beam(L, None, [("R₁ = ?", 0.05, "up"), (f"{W} N", x, "down"), ("R₂", L - 0.05, "up")], [(0, x, f"{fmt(x)} m")]))


@template("c4x_crane_counterweight", chapter=4, level=5, lo="4d")
def crane_counterweight(rng):
    load = nice(rng, 5000, 8000, 10000)
    dl = nice(rng, 12, 15, 20)
    dc = nice(rng, 4, 5)
    Wj = nice(rng, 2000, 3000)
    dj = nice(rng, 6, 8)
    C = (load * dl + Wj * dj) / dc
    return mk(rng, C, [(load * dl / dc, "Include the moment of the jib's own weight, which acts on the same side as the load."), ((load + Wj) * dl / dc, "The jib's weight acts at its own centre of gravity, not at the load's distance."), (load, "The counterweight is much closer to the tower, so it must be much heavier.")],
              "N", f"A tower crane balances a load on its jib with a counterweight.\n\n{md_table(['force', 'size / N', 'distance from tower / m', 'side'], [['load', load, dl, 'right'], ['jib weight (at its centre of gravity)', Wj, dj, 'right'], ['counterweight', '?', dc, 'left']])}\n\nWhat counterweight balances the crane?",
              "sum of moments on the right = moment of the counterweight", [f"right: {load}×{dl} + {Wj}×{dj} = {load * dl + Wj * dj} N m", f"C = {load * dl + Wj * dj} ÷ {dc} = **{fmt(C, sf=3)} N**"],
              ["List every moment on the load side.", "The jib's weight acts at its centre of gravity.", "Divide the total by the counterweight's distance."], sf=3)


@template("c4x_plank_balance_person", chapter=4, level=5, lo="4d")
def plank_balance_person(rng):
    L = 4.0
    Wp = nice(rng, 100, 150, 200)
    piv = nice(rng, 2.5, 3.0)
    Wm = nice(rng, 400, 500, 600)
    x = piv + Wp * (piv - L / 2) / Wm
    return mk(rng, x, [(piv - Wp * (piv - L / 2) / Wm, "The plank's weight acts at its centre, on the LEFT of the pivot; the man must stand to the RIGHT."), (L / 2 + Wp * (piv - L / 2) / Wm, "Measure from the left end."), (piv + Wm * (piv - L / 2) / Wp, "Wm × d = Wp × (piv − 2): check which weight goes with which distance.")],
              "m", f"A uniform plank **4.0 m** long weighing **{Wp} N** rests on a pivot **{fmt(piv)} m** from its left end. How far from the left end must a man of weight **{Wm} N** stand for the plank to balance (Fig. 1)?",
              "moments about the pivot: W_plank × (pivot − 2.0) = W_man × (x − pivot)", [f"{Wp} × {fmt(piv - 2)} = {Wm} × (x − {fmt(piv)})", f"x = **{fmt(x, sf=3)} m**"],
              ["The plank's weight acts at 2.0 m from the left end.", "That is on one side of the pivot; the man must be on the other.", "Take moments about the pivot."], figure=beam(L, piv, [("man", min(3.95, x), "down")], [(2.0, piv, f"{fmt(piv - 2)} m")], uniform=True, wl=f"{Wp} N"), sf=3)


@template("c4x_lever_pivot_position", chapter=4, level=5, lo="4b")
def lever_pivot_position(rng):
    L = nice(rng, 1.2, 1.5, 2.0)
    W = nice(rng, 300, 400, 600)
    F = nice(rng, 50, 75, 100)
    d_load = L * F / (W + F)
    return mk(rng, d_load, [(L * W / (W + F), "That is the distance from the EFFORT end; the pivot is nearer the heavy load."), (L / 2, "The pivot is not at the centre when the forces are unequal."), (F * L / W, "Use d_load + d_effort = L with W d_load = F d_effort.")],
              "m", f"A **{fmt(L)} m** crowbar is used to lift a **{W} N** rock with a **{F} N** effort at the other end (Fig. 1). Ignoring the bar's weight, how far from the rock should the pivot be placed?",
              "W d₁ = F d₂ and d₁ + d₂ = L → d₁ = L F ÷ (W + F)", [f"{W} × d = {F} × ({fmt(L)} − d)", f"d = {fmt(L)} × {F} ÷ ({W} + {F}) = **{fmt(d_load, sf=3)} m**"],
              ["Let d be the distance from the rock to the pivot.", "The effort's distance is then L − d.", "Use W d = F (L − d)."], figure=beam(L, L * F / (W + F), [(f"{W} N rock", 0.03, "down"), (f"{F} N effort", L - 0.03, "down")]), sf=3)


@template("c4x_nonuniform_two_scales", chapter=4, level=5, lo="4e")
def nonuniform_two_scales(rng):
    L = nice(rng, 2.0, 3.0)
    R1, R2 = nice(rng, 120, 150, 180), nice(rng, 60, 80, 100)
    W = R1 + R2
    x = R2 * L / W
    return mk(rng, x, [(L / 2, "The readings differ, so the centre of gravity is NOT at the middle."), (R1 * L / W, "G is nearer the scale with the LARGER reading."), (W, "That is the weight; the question asks for the position of G.")],
              "m", f"A non-uniform log of length **{fmt(L)} m** rests with each end on a bathroom scale. The left scale reads **{R1} N** and the right scale reads **{R2} N** (Fig. 1). How far from the left end is its centre of gravity?",
              "W = R₁ + R₂; moments about the left end: R₂ × L = W × x", [f"W = {R1} + {R2} = {W} N", f"x = {R2} × {fmt(L)} ÷ {W} = **{fmt(x, sf=3)} m**"],
              ["The total weight equals the sum of the readings.", "Take moments about the left end.", "Solve for the position of G."], figure=beam(L, None, [(f"{R1} N", 0.05, "up"), ("W", x, "down"), (f"{R2} N", L - 0.05, "up")]), sf=3)


@template("c4x_cg_combined_rod", chapter=4, level=5, lo="4e")
def cg_combined_rod(rng):
    L = 1.0
    Wr = nice(rng, 2, 3, 4)
    Wm = nice(rng, 1, 2, 4)
    xm = nice(rng, 0.8, 0.9, 1.0)
    x = (Wr * 0.5 + Wm * xm) / (Wr + Wm)
    return mk(rng, x * 100, [(50, "Adding the mass moves the combined centre of gravity towards it."), ((Wr * 0.5 + Wm * xm) * 100, "Divide by the total weight."), ((0.5 + xm) / 2 * 100, "Weight the positions by the weights: the heavier part counts more.")],
              "cm", f"A uniform metre rule of weight **{Wr} N** has a **{Wm} N** weight fixed at the **{round(xm * 100)} cm** mark. At which mark does the combined centre of gravity lie (where it would balance)?\n\n{md_table(['part', 'weight / N', 'position of its G / cm'], [['rule', Wr, 50], ['fixed weight', Wm, round(xm * 100)]])}",
              "balance point x: W_total × x = Σ (W × position)", [f"x = ({Wr}×50 + {Wm}×{round(xm * 100)}) ÷ {Wr + Wm}", f"= **{fmt(x * 100, sf=3)} cm**"],
              ["The combined weight acts at the balance point.", "Moments about the 0 cm end must match.", "Divide the sum of moments by the total weight."], sf=3)


@template("c4x_max_load_top", chapter=4, level=5, lo="4f")
def max_load_top(rng):
    w = nice(rng, 0.6, 0.8)
    hb = nice(rng, 0.5, 0.6)
    Wb = nice(rng, 200, 300)
    hl = nice(rng, 1.6, 1.8, 2.0)
    Wl = nice(rng, 50, 100, 150)
    hg = (Wb * hb + Wl * hl) / (Wb + Wl)
    ang = math.degrees(math.atan((w / 2) / hg))
    return mk(rng, ang, [(math.degrees(math.atan((w / 2) / hb)), "That is the tipping angle WITHOUT the load; the load raises the combined G."), (math.degrees(math.atan(w / hg)), "Use half the base width."), (math.degrees(math.atan((w / 2) / hl)), "The combined G lies between the cabinet's G and the load's G.")],
              "°", f"A cabinet with a base **{fmt(w)} m** wide has a load put on top.\n\n{md_table(['part', 'weight / N', 'height of its G / m'], [['cabinet', Wb, fmt(hb)], ['load on top', Wl, fmt(hl)]])}\n\nThrough what angle can the loaded cabinet be tilted before it topples?",
              "combined G height = Σ(W h) ÷ ΣW; then tan θ = (w/2) ÷ h_G", [f"h_G = ({Wb}×{fmt(hb)} + {Wl}×{fmt(hl)}) ÷ {Wb + Wl} = {fmt(hg, sf=3)} m", f"tan θ = {fmt(w / 2)} ÷ {fmt(hg, sf=3)} → θ = **{fmt(ang, sf=3)}°**"],
              ["First find the height of the combined centre of gravity.", "Weight the heights by the weights.", "Then use tan θ = (w/2)/h_G."], sf=3)


@template("c4x_tilt_wide_vs_narrow", chapter=4, level=5, lo="4f")
def tilt_wide_vs_narrow(rng):
    h = nice(rng, 0.6, 0.8, 1.0)
    w1, w2 = nice(rng, 0.4, 0.5), nice(rng, 0.8, 1.0)
    a1 = math.degrees(math.atan((w1 / 2) / (h / 2)))
    a2 = math.degrees(math.atan((w2 / 2) / (h / 2)))
    return mk(rng, a2 - a1, [(a2, "That is the wide base's tipping angle; the question asks for the INCREASE."), (a1, "That is the narrow base's tipping angle."), (math.degrees(math.atan((w2 - w1) / h)), "Find each angle first, then subtract.")],
              "°", f"A uniform vase **{fmt(h)} m** tall is redesigned with a wider base.\n\n{md_table(['design', 'base width / m'], [['old', fmt(w1)], ['new', fmt(w2)]])}\n\nAssuming its centre of gravity stays at half its height, by how much does the tipping angle increase?",
              "tan θ = (w/2) ÷ (h/2) for each design; subtract", [f"old: {fmt(a1, sf=3)}°; new: {fmt(a2, sf=3)}°", f"increase = **{fmt(a2 - a1, sf=2)}°**"],
              ["Find both tipping angles.", "tan θ = w ÷ h.", "Subtract."], sf=2)
