"""Chapter 3 Dynamics: F = ma, resultant force, friction, free-body situations."""
from .. import figs, sketches
from ..config import G
from .base import fmt, nice, numeric_options, template


def _axes(xmax_raw, ymax_raw):
    def pick(v):
        for lim, step in ((5, 1), (10, 2), (20, 4), (25, 5), (30, 5), (40, 8), (50, 10), (60, 10), (80, 20), (100, 20)):
            if v <= lim:
                return lim, step
        return v, v / 5
    (xmax, xstep), (ymax, ystep) = pick(xmax_raw), pick(ymax_raw)
    return xmax, ymax, xstep, ystep


# ---------------------------------------------------------------- L1
@template("c3_force_from_ma", chapter=3, level=1, lo="3j")
def force_from_ma(rng):
    m = nice(rng, 2, 4, 5, 8, 10, 20, 50)
    a = nice(rng, 0.5, 1.5, 2, 2.5, 3, 4)
    F = m * a
    opts, key, mis = numeric_options(rng, F, [
        (m / a, "You divided mass by acceleration. Resultant force = mass × acceleration."),
        (a / m, "You divided acceleration by mass. F = ma means multiply."),
        (m + a, "You added. F = m × a."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a trolley of mass **{fmt(m)} kg** on a smooth surface. A force F makes it accelerate at **{fmt(a)} m/s²**. What is the resultant force F acting on the trolley?",
        figure=figs.force_diagram([("F = ?", "right", 2.0)], label_body=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="resultant force = mass × acceleration (F = ma)",
        working=["F = ma", f"= {fmt(m)} × {fmt(a)}", f"= **{fmt(F)} N**"],
        hints=["Newton's second law links resultant force, mass and acceleration. Which formula is it?",
               f"m = {fmt(m)} kg and a = {fmt(a)} m/s². Force in newtons = kg × m/s².",
               f"F = {fmt(m)} × {fmt(a)}."],
    )


# ---------------------------------------------------------------- L2
@template("c3_acceleration_from_F_m", chapter=3, level=2, lo="3j")
def acceleration_from_F_m(rng):
    m = nice(rng, 2, 4, 5, 8, 10, 20, 25, 50)
    a = nice(rng, 0.4, 0.5, 1.2, 1.5, 2, 2.5, 3, 4)
    F = m * a
    opts, key, mis = numeric_options(rng, a, [
        (F * m, "You multiplied. Rearrange F = ma to get a = F ÷ m."),
        (m / F, "You divided mass by force, the wrong way round: a = F ÷ m."),
        (F - m, "You subtracted. Rearrange F = ma to get a = F ÷ m."),
    ], unit="m/s²")
    return dict(
        stem=f"Fig. 1 shows a resultant force of **{fmt(F)} N** acting on a box of mass **{fmt(m)} kg** on a smooth floor. What is the acceleration of the box?",
        figure=figs.force_diagram([(f"{fmt(F)} N", "right", 2.0)], label_body=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="F = ma, rearranged: a = F ÷ m",
        working=["F = ma  →  a = F ÷ m", f"= {fmt(F)} ÷ {fmt(m)}", f"= **{fmt(a)} m/s²**"],
        hints=["You know the resultant force and the mass. Rearrange F = ma to make a the subject.",
               f"A bigger mass accelerates less for the same force, so the mass must be on the bottom: a = {fmt(F)} ÷ {fmt(m)}.",
               f"a = {fmt(F)} ÷ {fmt(m)}."],
    )


# ---------------------------------------------------------------- L3
@template("c3_resultant_then_acceleration", chapter=3, level=3, lo="3j")
def resultant_then_acceleration(rng):
    m = nice(rng, 2, 4, 5, 8, 10, 20)
    a = nice(rng, 0.5, 1, 1.5, 2, 2.5, 3)
    f = nice(rng, 2, 4, 5, 6, 8, 10, 15)
    F = f + m * a
    opts, key, mis = numeric_options(rng, a, [
        (F / m, "You ignored friction. The RESULTANT force is the forward force minus the friction."),
        ((F + f) / m, "You added the two forces. They act in opposite directions, so subtract."),
        (F - f, "That is the resultant force in newtons, not the acceleration. Divide by the mass."),
    ], unit="m/s²")
    return dict(
        stem=f"Fig. 1 shows a box of mass **{fmt(m)} kg** pulled along a rough floor by a horizontal force of **{fmt(F)} N**. The friction on the box is **{fmt(f)} N**. What is the acceleration of the box?",
        figure=figs.force_diagram([(f"{fmt(F)} N", "right", 2.2), (f"{fmt(f)} N", "left", 1.2)], label_body=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="resultant force = forward force − friction; a = resultant force ÷ mass",
        working=[f"resultant force = {fmt(F)} − {fmt(f)} = {fmt(F - f)} N", f"a = F ÷ m = {fmt(F - f)} ÷ {fmt(m)}", f"= **{fmt(a)} m/s²**"],
        hints=["Two forces act horizontally in opposite directions. What is the RESULTANT force on the box?",
               f"resultant = {fmt(F)} − {fmt(f)} = {fmt(F - f)} N, to the right. Now use Newton's second law.",
               f"a = {fmt(F - f)} ÷ {fmt(m)}."],
    )


@template("c3_force_from_change_in_velocity", chapter=3, level=3, lo="3j")
def force_from_change_in_velocity(rng):
    m = nice(rng, 0.5, 2, 5, 8, 10, 60, 800, 1200)
    u = nice(rng, 0, 0, 2, 4, 5, 10)
    a = nice(rng, 0.5, 1, 1.5, 2, 2.5, 4)
    t = nice(rng, 2, 4, 5, 8, 10)
    v = u + a * t
    F = m * a
    wrongs = [((v - u) / t, "That is the acceleration, not the force. Multiply by the mass."),
              (m * (v - u), "You forgot to divide the change in velocity by the time. Find the acceleration first.")]
    if u:
        wrongs.append((m * v / t, "You used the final velocity instead of the CHANGE in velocity, v − u."))
    else:
        wrongs.append((m * v * t, "You multiplied by time instead of dividing. a = (v − u) ÷ t."))
    opts, key, mis = numeric_options(rng, F, wrongs, unit="N")
    return dict(
        stem=f"Fig. 1 shows a vehicle of mass **{fmt(m)} kg** that speeds up uniformly from **{fmt(u)} m/s to {fmt(v)} m/s in {fmt(t)} s**. What is the resultant force on the vehicle?",
        figure=sketches.motion_sketch(f"u = {fmt(u)} m/s", f"v = {fmt(v)} m/s", f"t = {fmt(t)} s", body_label=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="a = (v − u) ÷ t, then F = ma",
        working=[f"a = ({fmt(v)} − {fmt(u)}) ÷ {fmt(t)} = {fmt(a)} m/s²", f"F = ma = {fmt(m)} × {fmt(a)}", f"= **{fmt(F)} N**"],
        hints=["F = ma needs the acceleration, which is not given directly. How do you find it from the speeds and the time?",
               f"a = ({fmt(v)} − {fmt(u)}) ÷ {fmt(t)} = {fmt(a)} m/s².",
               f"F = {fmt(m)} × {fmt(a)}."],
    )


# ---------------------------------------------------------------- L4
@template("c3_force_from_graph", chapter=3, level=4, lo="3j")
def force_from_graph(rng):
    m = nice(rng, 2, 5, 10, 50, 500, 1000)
    u = nice(rng, 0, 0, 4, 5, 10)
    a = nice(rng, 0.5, 1, 1.5, 2, 2.5, 4)
    t = nice(rng, 4, 5, 8, 10)
    v = u + a * t
    F = m * a
    xmax, ymax, xstep, ystep = _axes(t, v)
    wrongs = [((v - u) / t, "That is the acceleration (the gradient). The question asks for the force: F = ma."),
              (m * 0.5 * (u + v) * t, "You used the AREA under the graph (the distance) instead of the gradient (the acceleration).")]
    if u:
        wrongs.append((m * v / t, "You used the final speed instead of the change in speed. The graph does not start from zero."))
    else:
        wrongs.append((m * v, "You multiplied the mass by the final speed. F = m × acceleration, and acceleration = gradient."))
    opts, key, mis = numeric_options(rng, F, wrongs, unit="N")
    return dict(
        stem=f"Fig. 1 shows the speed–time graph of an object of mass **{fmt(m)} kg**. What is the resultant force acting on the object?",
        figure=figs.graph([(0, u), (t, v)], xmax, ymax, xstep, ystep),
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = gradient of the speed–time graph; F = ma",
        working=[f"acceleration = gradient = ({fmt(v)} − {fmt(u)}) ÷ {t} = {fmt(a)} m/s²", f"F = ma = {fmt(m)} × {fmt(a)}", f"= **{fmt(F)} N**"],
        hints=["To use F = ma you need the acceleration. Where on a speed–time graph do you find it?",
               f"gradient = ({fmt(v)} − {fmt(u)}) ÷ {t} = {fmt(a)} m/s².",
               f"F = {fmt(m)} × {fmt(a)}."],
    )


@template("c3_find_friction", chapter=3, level=4, lo="3l")
def find_friction(rng):
    m = nice(rng, 2, 4, 5, 8, 10, 20, 40)
    a = nice(rng, 0.5, 1, 1.5, 2, 2.5)
    f = nice(rng, 2, 3, 5, 6, 8, 10, 12)
    F = f + m * a
    opts, key, mis = numeric_options(rng, f, [
        (F + m * a, "You added. The applied force is bigger than the resultant, so friction = applied force − ma."),
        (m * a, "That is the RESULTANT force (ma). Friction is the difference between the applied force and the resultant."),
        (F / m, "That is what the acceleration would be with no friction. Use friction = F − ma."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a crate of mass **{fmt(m)} kg** pushed along a floor by a horizontal force of **{fmt(F)} N**. The crate accelerates at **{fmt(a)} m/s²**. What is the friction acting on the crate?",
        figure=figs.force_diagram([(f"{fmt(F)} N", "right", 2.2), ("friction", "left", 1.2)], label_body=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="resultant force = ma; friction = applied force − resultant force",
        working=[f"resultant force = ma = {fmt(m)} × {fmt(a)} = {fmt(m * a)} N", f"friction = {fmt(F)} − {fmt(m * a)}", f"= **{fmt(f)} N**"],
        hints=["The crate accelerates, so there IS a resultant force. How big is it, from F = ma?",
               f"resultant = {fmt(m)} × {fmt(a)} = {fmt(m * a)} N. The applied force is {fmt(F)} N; friction makes up the difference.",
               f"friction = {fmt(F)} − {fmt(m * a)}."],
    )


# ---------------------------------------------------------------- L5
@template("c3_lift_scale_reading", chapter=3, level=5, lo="3j")
def lift_scale_reading(rng):
    m = nice(rng, 40, 50, 60, 70, 80)
    a = nice(rng, 1, 1.5, 2, 2.5)
    N = m * (G + a)
    opts, key, mis = numeric_options(rng, N, [
        (m * G, "That is just the weight. The lift accelerates UPWARDS, so the floor must push with MORE than the weight."),
        (m * (G - a), "You subtracted. For upward acceleration the resultant force is upward: N − W = ma, so N = W + ma."),
        (m * a, "That is the resultant force only. The scale reads the full normal force, N = W + ma."),
    ], unit="N")
    return dict(
        stem=f"A student of mass **{fmt(m)} kg** stands on a bathroom scale in a lift. The lift accelerates **upwards at {fmt(a)} m/s²**. Fig. 1 shows the forces on the student. Taking g = 10 N/kg, what is the reading on the scale (the normal force N)?",
        figure=figs.force_diagram([("N", "up", 2.0), (f"W = {fmt(m * G)} N", "down", 1.4)], label_body=f"{fmt(m)} kg", ground=True),
        options=opts, key=key, misconceptions=mis,
        formula="resultant force (upwards) = N − W = ma, so N = mg + ma",
        working=[f"W = mg = {fmt(m)} × 10 = {fmt(m * G)} N", f"N − W = ma  →  N = {fmt(m * G)} + {fmt(m)} × {fmt(a)}", f"= **{fmt(N)} N**"],
        hints=["Which direction is the resultant force, and which of the two forces must therefore be bigger?",
               f"Upward acceleration means N > W. Resultant = N − W = ma = {fmt(m)} × {fmt(a)} = {fmt(m * a)} N.",
               f"N = {fmt(m * G)} + {fmt(m * a)}."],
    )


@template("c3_parachutist_air_resistance", chapter=3, level=5, lo="3m")
def parachutist_air_resistance(rng):
    m = nice(rng, 50, 60, 70, 80, 90)
    a = nice(rng, 2, 4, 5, 6, 8)
    W = m * G
    R = m * (G - a)
    opts, key, mis = numeric_options(rng, a, [
        ((W + R) / m, "You added the forces. Air resistance acts UPWARDS, against the weight, so subtract."),
        (R / m, "You used only the air resistance. The resultant force is weight − air resistance."),
        (G, "That would be free fall with no air resistance. Here the air resistance reduces the acceleration."),
    ], unit="m/s²")
    return dict(
        stem=f"A skydiver of mass **{fmt(m)} kg** is falling. At one instant the air resistance acting on her is **{fmt(R)} N**, as shown in Fig. 1. Taking g = 10 N/kg, what is her acceleration at this instant?",
        figure=figs.force_diagram([(f"air resistance {fmt(R)} N", "up", 1.3), (f"weight {fmt(W)} N", "down", 2.0)], label_body=f"{fmt(m)} kg", ground=False),
        options=opts, key=key, misconceptions=mis,
        formula="resultant force (downwards) = weight − air resistance; a = resultant ÷ mass",
        working=[f"weight = {fmt(m)} × 10 = {fmt(W)} N", f"resultant = {fmt(W)} − {fmt(R)} = {fmt(W - R)} N downwards",
                 f"a = {fmt(W - R)} ÷ {fmt(m)} = **{fmt(a)} m/s²**"],
        hints=["Two vertical forces act: weight down and air resistance up. What is the resultant, and which way does it point?",
               f"Weight = {fmt(W)} N. Resultant = {fmt(W)} − {fmt(R)} = {fmt(W - R)} N, downwards.",
               f"a = {fmt(W - R)} ÷ {fmt(m)}."],
    )
