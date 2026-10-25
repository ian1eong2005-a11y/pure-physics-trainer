"""Chapter 4 Turning Effects of Forces: moments, principle of moments, centre of gravity."""
from .. import sketches
from ..config import G
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c4_moment_direct", chapter=4, level=1, lo="4b")
def moment_direct(rng):
    F = nice(rng, 5, 8, 10, 12, 15, 20, 25, 40)
    d = nice(rng, 0.2, 0.25, 0.4, 0.5, 0.6, 0.8, 1.2, 1.5)
    M = F * d
    opts, key, mis = numeric_options(rng, M, [
        (F / d, "You divided force by distance. Moment = force × perpendicular distance."),
        (F + d, "You added. Moment = force × perpendicular distance."),
        (F * d / 2, "You halved the result. There is no ½ in the moment formula."),
    ], unit="N m")
    return dict(
        stem=f"Fig. 1 shows a force of **{fmt(F)} N** acting on a beam at a perpendicular distance of **{fmt(d)} m** from the pivot. What is the moment of the force about the pivot?",
        figure=sketches.beam(d + 0.5, 0.25, [(f"{fmt(F)} N", 0.25 + d, "down")], dist_labels=[(0.25, 0.25 + d, f"{fmt(d)} m")]),
        options=opts, key=key, misconceptions=mis,
        formula="moment = force × perpendicular distance from the pivot",
        working=["moment = F × d", f"= {fmt(F)} × {fmt(d)}", f"= **{fmt(M)} N m**"],
        hints=["A moment measures the turning effect of a force. Which two quantities does it depend on?",
               f"The force is {fmt(F)} N and it acts {fmt(d)} m from the pivot, at right angles to the beam.",
               f"moment = {fmt(F)} × {fmt(d)}."],
    )


@template("c4_moment_distance_cm", chapter=4, level=1, lo="4b")
def moment_distance_cm(rng):
    F = nice(rng, 4, 6, 8, 10, 15, 20, 30)
    d_cm = nice(rng, 20, 25, 30, 40, 50, 60, 80)
    d = d_cm / 100
    M = F * d
    opts, key, mis = numeric_options(rng, M, [
        (F * d_cm, "You left the distance in cm. For a moment in N m the distance must be in metres (÷ 100)."),
        (F * d_cm / 10, "You divided by 10 instead of 100. 1 m = 100 cm."),
        (F / d, "You divided force by distance. Moment = force × distance."),
    ], unit="N m")
    return dict(
        stem=f"Fig. 1 shows a spanner turning a nut. A force of **{fmt(F)} N** is applied at right angles to the spanner, **{d_cm} cm** from the centre of the nut. What is the moment of the force about the nut, in N m?",
        figure=sketches.beam(d + 0.1, 0.05, [(f"{fmt(F)} N", 0.05 + d, "down")], dist_labels=[(0.05, 0.05 + d, f"{d_cm} cm")]),
        options=opts, key=key, misconceptions=mis,
        formula="moment = force × perpendicular distance, with the distance in metres",
        working=[f"d = {d_cm} cm = {fmt(d)} m", f"moment = {fmt(F)} × {fmt(d)}", f"= **{fmt(M)} N m**"],
        hints=["The answer is wanted in N m. Which of the two given quantities needs converting first?",
               f"{d_cm} cm = {d_cm} ÷ 100 m = {fmt(d)} m.",
               f"moment = {fmt(F)} × {fmt(d)}."],
    )


# ---------------------------------------------------------------- L2
@template("c4_force_from_moment", chapter=4, level=2, lo="4b")
def force_from_moment(rng):
    d = nice(rng, 0.2, 0.25, 0.4, 0.5, 0.8, 1.5, 2.0)
    F = nice(rng, 5, 8, 10, 15, 20, 30, 50)
    M = F * d
    opts, key, mis = numeric_options(rng, F, [
        (M * d, "You multiplied. Rearrange moment = F × d to get F = moment ÷ d."),
        (d / M, "You divided the wrong way round: F = moment ÷ distance."),
        (M, "That is the moment itself. The question asks for the force."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a force F acting **{fmt(d)} m** from a pivot. The moment of F about the pivot is **{fmt(M)} N m**. What is the size of F?",
        figure=sketches.beam(d + 0.5, 0.25, [("F", 0.25 + d, "down")], dist_labels=[(0.25, 0.25 + d, f"{fmt(d)} m")]),
        options=opts, key=key, misconceptions=mis,
        formula="moment = F × d, rearranged: F = moment ÷ d",
        working=["F = moment ÷ d", f"= {fmt(M)} ÷ {fmt(d)}", f"= **{fmt(F)} N**"],
        hints=["You know the moment and the distance. Rearrange moment = F × d.",
               f"A moment of {fmt(M)} N m produced at {fmt(d)} m from the pivot.",
               f"F = {fmt(M)} ÷ {fmt(d)}."],
    )


# ---------------------------------------------------------------- L3
@template("c4_balance_unknown_force", chapter=4, level=3, lo="4d")
def balance_unknown_force(rng):
    F1 = nice(rng, 10, 15, 20, 30, 40, 60)
    d1 = nice(rng, 0.5, 1.0, 1.5, 2.0)
    d2 = nice(rng, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
    if d2 == d1:
        d2 = d1 + 0.5
    F2 = F1 * d1 / d2
    opts, key, mis = numeric_options(rng, F2, [
        (F1, "You assumed the forces must be equal. They balance only if the MOMENTS are equal: F₁d₁ = F₂d₂."),
        (F1 * d2 / d1, "You used the distances the wrong way round. The force further from the pivot must be smaller."),
        (F1 * d1, "That is the anticlockwise moment in N m, not the force. Divide by the distance on the other side."),
    ], unit="N")
    L = d1 + d2 + 0.4
    return dict(
        stem=f"Fig. 1 shows a uniform beam balanced on a pivot at its centre. A force of **{fmt(F1)} N** acts **{fmt(d1)} m** to the left of the pivot and a force F acts **{fmt(d2)} m** to the right. The beam is in equilibrium. What is F?",
        figure=sketches.beam(L, L / 2, [(f"{fmt(F1)} N", L / 2 - d1, "down"), ("F", L / 2 + d2, "down")],
                             dist_labels=[(L / 2 - d1, L / 2, f"{fmt(d1)} m"), (L / 2, L / 2 + d2, f"{fmt(d2)} m")]),
        options=opts, key=key, misconceptions=mis,
        formula="principle of moments: anticlockwise moment = clockwise moment, F₁ × d₁ = F₂ × d₂",
        working=[f"anticlockwise moment = {fmt(F1)} × {fmt(d1)} = {fmt(F1 * d1)} N m",
                 f"clockwise moment = F × {fmt(d2)} must equal {fmt(F1 * d1)} N m",
                 f"F = {fmt(F1 * d1)} ÷ {fmt(d2)} = **{fmt(F2)} N**"],
        hints=["The beam is in equilibrium. What does the principle of moments say about the clockwise and anticlockwise moments?",
               f"Anticlockwise moment = {fmt(F1)} × {fmt(d1)} = {fmt(F1 * d1)} N m. The clockwise moment F × {fmt(d2)} must be the same.",
               f"F = {fmt(F1 * d1)} ÷ {fmt(d2)}."],
    )


@template("c4_balance_unknown_distance", chapter=4, level=3, lo="4d")
def balance_unknown_distance(rng):
    F1 = nice(rng, 20, 30, 40, 50, 60)
    d1 = nice(rng, 0.5, 1.0, 1.5, 2.0)
    F2 = nice(rng, 10, 15, 20, 25, 40, 75, 100)
    if F2 == F1:
        F2 = F1 * 2
    d2 = F1 * d1 / F2
    opts, key, mis = numeric_options(rng, d2, [
        (d1, "You assumed equal distances. The moments must be equal, so the larger force sits closer to the pivot."),
        (F2 * d1 / F1, "You used the forces the wrong way round: d₂ = F₁d₁ ÷ F₂."),
        (F1 * d1, "That is the moment in N m, not a distance. Divide by the other force."),
    ], unit="m")
    L = d1 + d2 + 0.6
    return dict(
        stem=f"Fig. 1 shows a beam balanced on a pivot. A child of weight **{fmt(F1)} N** sits **{fmt(d1)} m** to the left of the pivot. An adult of weight **{fmt(F2)} N** sits on the right so that the beam balances. How far from the pivot is the adult?",
        figure=sketches.beam(L, d1 + 0.3, [(f"{fmt(F1)} N", 0.3, "down"), (f"{fmt(F2)} N", d1 + 0.3 + d2, "down")],
                             dist_labels=[(0.3, d1 + 0.3, f"{fmt(d1)} m"), (d1 + 0.3, d1 + 0.3 + d2, "d = ?")]),
        options=opts, key=key, misconceptions=mis,
        formula="F₁ × d₁ = F₂ × d₂, so d₂ = F₁d₁ ÷ F₂",
        working=[f"anticlockwise moment = {fmt(F1)} × {fmt(d1)} = {fmt(F1 * d1)} N m",
                 f"{fmt(F2)} × d = {fmt(F1 * d1)}", f"d = {fmt(F1 * d1)} ÷ {fmt(F2)} = **{fmt(d2)} m**"],
        hints=["Balanced beam: clockwise moment = anticlockwise moment. Write each moment as force × distance.",
               f"The child's moment is {fmt(F1)} × {fmt(d1)} = {fmt(F1 * d1)} N m. The adult's moment is {fmt(F2)} × d.",
               f"d = {fmt(F1 * d1)} ÷ {fmt(F2)}."],
    )


# ---------------------------------------------------------------- L4
@template("c4_three_forces", chapter=4, level=4, lo="4d")
def three_forces(rng):
    F1 = nice(rng, 10, 20, 30, 40)
    d1 = nice(rng, 1.0, 1.5, 2.0)
    F2 = nice(rng, 10, 15, 20, 30)
    d2 = nice(rng, 0.5, 1.0)
    d3 = nice(rng, 1.0, 1.5, 2.0, 2.5)
    F3 = (F1 * d1 + F2 * d2) / d3
    opts, key, mis = numeric_options(rng, F3, [
        (F1 * d1 / d3, "You left out the second force on the left. ADD the two anticlockwise moments first."),
        ((F1 * d1 - F2 * d2) / d3, "You subtracted. Both left-hand forces turn the beam anticlockwise, so their moments add."),
        (F1 + F2, "You added the forces. Balance needs equal MOMENTS, not equal forces."),
    ], unit="N")
    L = d1 + d3 + 0.6
    p = d1 + 0.3
    return dict(
        stem=f"Fig. 1 shows a light beam in equilibrium on a pivot. Forces of **{fmt(F1)} N** and **{fmt(F2)} N** act on the left at **{fmt(d1)} m** and **{fmt(d2)} m** from the pivot. A single force F acts **{fmt(d3)} m** to the right of the pivot. What is F?",
        figure=sketches.beam(L, p, [(f"{fmt(F1)} N", p - d1, "down"), (f"{fmt(F2)} N", p - d2, "down"), ("F", p + d3, "down")],
                             dist_labels=[(p - d1, p, f"{fmt(d1)} m"), (p - d2, p, f"{fmt(d2)} m"), (p, p + d3, f"{fmt(d3)} m")]),
        options=opts, key=key, misconceptions=mis,
        formula="sum of anticlockwise moments = sum of clockwise moments",
        working=[f"anticlockwise moments = {fmt(F1)} × {fmt(d1)} + {fmt(F2)} × {fmt(d2)} = {fmt(F1 * d1)} + {fmt(F2 * d2)} = {fmt(F1 * d1 + F2 * d2)} N m",
                 f"clockwise moment = F × {fmt(d3)}", f"F = {fmt(F1 * d1 + F2 * d2)} ÷ {fmt(d3)} = **{fmt(F3)} N**"],
        hints=["Two forces turn the beam one way and one force turns it the other way. Add up the moments on each side.",
               f"Anticlockwise: {fmt(F1)} × {fmt(d1)} + {fmt(F2)} × {fmt(d2)} = {fmt(F1 * d1 + F2 * d2)} N m.",
               f"F × {fmt(d3)} = {fmt(F1 * d1 + F2 * d2)}, so F = {fmt(F1 * d1 + F2 * d2)} ÷ {fmt(d3)}."],
    )


@template("c4_uniform_beam_cg", chapter=4, level=4, lo="4e")
def uniform_beam_cg(rng):
    L = nice(rng, 2.0, 3.0, 4.0, 6.0)
    W = nice(rng, 20, 30, 40, 60, 90)
    p = nice(rng, 0.5, 1.0, 1.5)
    if p >= L / 2:
        p = L / 4
    F = W * (L / 2 - p) / p
    opts, key, mis = numeric_options(rng, F, [
        (W, "You assumed the load equals the weight. The weight acts at the centre, a different distance from the pivot, so use moments."),
        (W * (L - p) / p, "You took the weight as acting at the far end. A uniform beam's weight acts at its CENTRE (centre of gravity)."),
        (W * p / (L / 2 - p), "You swapped the distances. The load is {p} m from the pivot; the weight is (L/2 − p) from it."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a uniform beam of length **{fmt(L)} m** and weight **{fmt(W)} N** resting on a pivot **{fmt(p)} m** from its left end. A downward force F at the left end keeps the beam horizontal. What is F?",
        figure=sketches.beam(L, p, [("F", 0.0, "down")], dist_labels=[(0.0, p, f"{fmt(p)} m"), (p, L / 2, f"{fmt(L / 2 - p)} m")], uniform=True, weight_label=f"W = {fmt(W)} N"),
        options=opts, key=key, misconceptions=mis,
        formula="weight of a uniform beam acts at its centre; F × p = W × (L/2 − p)",
        working=[f"the weight acts at the centre, {fmt(L / 2)} m from the left end, i.e. {fmt(L / 2 - p)} m from the pivot",
                 f"F × {fmt(p)} = {fmt(W)} × {fmt(L / 2 - p)} = {fmt(W * (L / 2 - p))}", f"F = {fmt(W * (L / 2 - p))} ÷ {fmt(p)} = **{fmt(F)} N**"],
        hints=["Where does the weight of a uniform beam act? Mark that point and find its distance from the pivot.",
               f"The centre of gravity is {fmt(L / 2)} m from the end, so {fmt(L / 2 - p)} m from the pivot. Weight moment = {fmt(W)} × {fmt(L / 2 - p)} = {fmt(W * (L / 2 - p))} N m.",
               f"F × {fmt(p)} = {fmt(W * (L / 2 - p))}."],
    )


# ---------------------------------------------------------------- L5
@template("c4_two_supports", chapter=4, level=5, lo="4d")
def two_supports(rng):
    L = nice(rng, 4.0, 5.0, 6.0, 8.0)
    W = nice(rng, 100, 150, 200, 300)
    P = nice(rng, 400, 500, 600, 800)
    x = nice(rng, 1.0, 1.5, 2.0, 3.0)
    if x >= L:
        x = L / 4
    R = (W * L / 2 + P * x) / L
    opts, key, mis = numeric_options(rng, R, [
        (P * x / L, "You forgot the weight of the plank, which acts at its centre."),
        ((W + P) / 2, "You shared the total weight equally. That is only true if the person stands at the centre."),
        ((W * L / 2 + P * (L - x)) / L, "You used the person's distance from the wrong support. Take moments about the LEFT support to find the RIGHT support's force."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a uniform plank of length **{fmt(L)} m** and weight **{fmt(W)} N** resting on two supports at its ends. A person of weight **{fmt(P)} N** stands **{fmt(x)} m** from the left support. What is the upward force R exerted by the right support?",
        figure=sketches.beam(L, None, [(f"{fmt(P)} N", x, "down"), ("R", L, "up"), ("S", 0.0, "up")],
                             dist_labels=[(0.0, x, f"{fmt(x)} m"), (0.0, L / 2, f"{fmt(L / 2)} m")], uniform=True, weight_label=f"W = {fmt(W)} N"),
        options=opts, key=key, misconceptions=mis,
        formula="take moments about the left support: R × L = W × (L/2) + P × x",
        working=[f"moments about the left support (so S has no moment):",
                 f"clockwise: {fmt(W)} × {fmt(L / 2)} + {fmt(P)} × {fmt(x)} = {fmt(W * L / 2)} + {fmt(P * x)} = {fmt(W * L / 2 + P * x)} N m",
                 f"anticlockwise: R × {fmt(L)}", f"R = {fmt(W * L / 2 + P * x)} ÷ {fmt(L)} = **{fmt(R)} N**"],
        hints=["Two unknown support forces: take moments about one support so that its force drops out. Which point removes S?",
               f"About the left support: the plank's weight acts at {fmt(L / 2)} m and the person at {fmt(x)} m, both clockwise. R acts at {fmt(L)} m, anticlockwise.",
               f"R × {fmt(L)} = {fmt(W)} × {fmt(L / 2)} + {fmt(P)} × {fmt(x)}."],
    )


@template("c4_mass_hung_moment", chapter=4, level=5, lo="4b")
def mass_hung_moment(rng):
    m = nice(rng, 0.2, 0.5, 1.5, 2.0, 2.5, 4.0)
    d_cm = nice(rng, 20, 25, 30, 40, 60, 80)
    W = m * G
    d = d_cm / 100
    M = W * d
    opts, key, mis = numeric_options(rng, M, [
        (m * d, "You used the mass instead of the weight. Moment needs a FORCE: weight = mg."),
        (W * d_cm, "You left the distance in cm. Convert to metres for N m."),
        (m * d_cm, "You used the mass (not the weight) and left the distance in cm. Two conversions are needed."),
    ], unit="N m")
    return dict(
        stem=f"Fig. 1 shows a mass of **{fmt(m)} kg** hung from a horizontal rod at **{d_cm} cm** from the pivot. Taking g = 10 N/kg, what is the moment of the weight of the mass about the pivot?",
        figure=sketches.beam(d + 0.2, 0.1, [(f"{fmt(m)} kg", 0.1 + d, "down")], dist_labels=[(0.1, 0.1 + d, f"{d_cm} cm")]),
        options=opts, key=key, misconceptions=mis,
        formula="weight = mg; moment = weight × perpendicular distance (in m)",
        working=[f"weight = {fmt(m)} × 10 = {fmt(W)} N", f"d = {d_cm} cm = {fmt(d)} m", f"moment = {fmt(W)} × {fmt(d)} = **{fmt(M)} N m**"],
        hints=["A moment needs a force, but you are given a mass. Which force does the hanging mass exert on the rod?",
               f"weight = {fmt(m)} × 10 = {fmt(W)} N. The distance {d_cm} cm must also become {fmt(d)} m.",
               f"moment = {fmt(W)} × {fmt(d)}."],
    )
