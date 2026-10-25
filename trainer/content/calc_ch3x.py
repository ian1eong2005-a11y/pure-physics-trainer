"""Chapter 3 Dynamics (6091) bank extension: calculation templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2014-2025: crates and friction, parachutists, weight on planets, strings at a point)."""
import math

from .. import figs, figs2, sketches
from .base import fmt, md_table, mk, nice, template

G = 10


# ================================================================== L1
@template("c3x_weight_kg", chapter=3, level=1, lo="3e")
def weight_kg(rng):
    m = nice(rng, 2.5, 4.0, 6.0, 12, 45, 60, 75)
    return mk(rng, m * G, [(m, "That is the mass in kg. Weight = mass × g, in newtons."), (m / G, "Multiply by g; do not divide."), (m * 9.8 if abs(m * 9.8 - m * G) > 0.5 else m * G + 5, "Use g = 10 N/kg.")],
              "N", f"Fig. 1 shows a suitcase of mass **{fmt(m)} kg** hanging from a spring balance on Earth (g = 10 N/kg). What is its weight?",
              "W = m g", [f"W = {fmt(m)} × 10 = **{fmt(m * G)} N**"],
              ["Weight is the gravitational force on a mass.", "W = m × g.", f"{fmt(m)} × 10."], figure=sketches.spring_balance("? N", "case"))


@template("c3x_weight_planet", chapter=3, level=1, lo="3e")
def weight_planet(rng):
    planet, g = rng.choice([("the Moon", 1.6), ("Mars", 3.7), ("Jupiter", 25), ("Venus", 8.9)])
    m = nice(rng, 2, 5, 10, 20, 50)
    return mk(rng, m * g, [(m * G, f"That is the weight on Earth. On {planet} use g = {fmt(g)} N/kg."), (m, "That is the mass, which is the same everywhere."), (m / g, "Multiply by g.")],
              "N", f"A rover is taken to {planet}.\n\n{md_table(['quantity', 'value'], [['mass of rover', f'{m} kg'], [f'g on {planet}', f'{fmt(g)} N/kg']])}\n\nWhat is its weight there?",
              "W = m g (use the local g)", [f"W = {m} × {fmt(g)} = **{fmt(m * g)} N**"],
              ["Mass does not change; weight depends on g.", f"Use g = {fmt(g)} N/kg.", "Multiply."])


@template("c3x_weight_grams", chapter=3, level=1, lo="3e")
def weight_grams(rng):
    m_g = nice(rng, 200, 250, 400, 500, 800, 150)
    W = m_g / 1000 * G
    return mk(rng, W, [(m_g * G, "Convert grams to kilograms first (÷ 1000)."), (m_g / 1000, "That is the mass in kg. Multiply by g."), (m_g / 100 * G, "1 kg = 1000 g, not 100 g.")],
              "N", f"A packet of rice is weighed.\n\n{md_table(['quantity', 'value'], [['mass', f'{m_g} g'], ['g', '10 N/kg']])}\n\nWhat is its weight?",
              "W = m g with m in kg", [f"m = {m_g} g = {fmt(m_g / 1000)} kg", f"W = {fmt(m_g / 1000)} × 10 = **{fmt(W)} N**"],
              ["Is the mass in SI units?", "Change g to kg.", "Then multiply by 10 N/kg."])


@template("c3x_force_ma", chapter=3, level=1, lo="3j")
def force_ma(rng):
    m = nice(rng, 2, 5, 8, 50, 120, 800)
    a = nice(rng, 0.5, 1.5, 2.0, 3.0, 4.0)
    return mk(rng, m * a, [(m / a, "F = m × a; do not divide."), (a / m, "F = m × a."), (m * a / 2, "There is no ½ in F = ma.")],
              "N", f"Fig. 1 shows a trolley of mass **{m} kg** accelerating at **{fmt(a)} m/s²**. What resultant force acts on it?",
              "resultant force F = m a", [f"F = {m} × {fmt(a)} = **{fmt(m * a)} N**"],
              ["Which law links force, mass and acceleration?", "F = m a.", f"{m} × {fmt(a)}."], figure=figs.force_diagram([("F = ?", "right", 1.3)], label_body=f"{m} kg"))


@template("c3x_accel_fm", chapter=3, level=1, lo="3j")
def accel_fm(rng):
    m = nice(rng, 2, 4, 5, 10, 25, 50)
    a = nice(rng, 0.5, 1.5, 2.0, 3.0, 4.0)
    F = m * a
    return mk(rng, a, [(F * m, "a = F ÷ m."), (m / F, "a = F ÷ m, not m ÷ F."), (F, "That is the force; divide by the mass.")],
              "m/s²", f"A resultant force of **{fmt(F)} N** acts on a box of mass **{m} kg** (Fig. 1). What is its acceleration?",
              "F = m a → a = F ÷ m", [f"a = {fmt(F)} ÷ {m} = **{fmt(a)} m/s²**"],
              ["Rearrange F = m a for a.", "Divide the force by the mass.", f"{fmt(F)} ÷ {m}."], figure=figs.force_diagram([(f"{fmt(F)} N", "right", 1.3)], label_body=f"{m} kg"))


@template("c3x_force_ma_g", chapter=3, level=1, lo="3j")
def force_ma_g(rng):
    m_g = nice(rng, 200, 400, 500, 800)
    a = nice(rng, 2.0, 2.5, 4.0, 5.0)
    F = m_g / 1000 * a
    return mk(rng, F, [(m_g * a, "Convert the mass to kg before using F = m a."), (m_g / 100 * a, "1 kg = 1000 g."), (m_g / 1000 / a, "Multiply, don't divide.")],
              "N", f"A toy car accelerates.\n\n{md_table(['quantity', 'value'], [['mass', f'{m_g} g'], ['acceleration', f'{fmt(a)} m/s²']])}\n\nWhat resultant force acts on it?",
              "F = m a with m in kg", [f"m = {fmt(m_g / 1000)} kg", f"F = {fmt(m_g / 1000)} × {fmt(a)} = **{fmt(F)} N**"],
              ["Check the unit of mass.", "Convert g → kg.", "F = m a."])


@template("c3x_g_from_data", chapter=3, level=1, lo="3d")
def g_from_data(rng):
    g = nice(rng, 10, 1.6, 3.7, 8.9)
    m = nice(rng, 2, 4, 5, 10)
    W = g * m
    return mk(rng, g, [(W * m, "g = W ÷ m."), (m / W, "g = W ÷ m, not m ÷ W."), (W, "That is the weight; divide by the mass.")],
              "N/kg", f"A probe measures the weight of a known mass on another world.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} kg'], ['weight measured', f'{fmt(W)} N']])}\n\nWhat is the gravitational field strength there?",
              "g = gravitational force per unit mass = W ÷ m", [f"g = {fmt(W)} ÷ {m} = **{fmt(g)} N/kg**"],
              ["Define g in words.", "Force per kilogram.", "W ÷ m."])


@template("c3x_g_spring_balance", chapter=3, level=1, lo="3d")
def g_spring_balance(rng):
    g = nice(rng, 10, 1.6, 3.7)
    m_g = nice(rng, 200, 500, 1000)
    W = g * m_g / 1000
    return mk(rng, g, [(W / m_g, "Convert the mass to kg."), (W * m_g / 1000, "g = W ÷ m."), (W, "Divide by the mass in kg.")],
              "N/kg", f"Fig. 1 shows a spring balance holding a **{m_g} g** mass. It reads **{fmt(W)} N**. What is the gravitational field strength where the reading is taken?",
              "g = W ÷ m (m in kg)", [f"m = {fmt(m_g / 1000)} kg", f"g = {fmt(W)} ÷ {fmt(m_g / 1000)} = **{fmt(g)} N/kg**"],
              ["Change grams into kilograms.", "g = weight ÷ mass.", "Divide."], figure=sketches.spring_balance(f"{fmt(W)} N", f"{m_g} g"))


@template("c3x_resultant_friction", chapter=3, level=1, lo="3l")
def resultant_friction(rng):
    P = nice(rng, 30, 40, 50, 80, 120)
    f = nice(rng, 10, 15, 20, 25)
    return mk(rng, P - f, [(P + f, "Friction opposes the push, so subtract."), (f, "That is the friction alone."), (P, "Friction reduces the resultant.")],
              "N", f"A crate is pushed with **{P} N** across a floor. Friction is **{f} N** (Fig. 1). What is the resultant force on the crate?",
              "resultant = push − friction (friction opposes motion)", [f"{P} − {f} = **{P - f} N** forwards"],
              ["Which way does friction act?", "Opposite to the push.", "Subtract."], figure=figs2.forces_on_line([(f"{P} N push", "right", P), (f"{f} N friction", "left", f)], body="crate"))


@template("c3x_friction_constant_velocity", chapter=3, level=1, lo="3l")
def friction_constant_velocity(rng):
    P = nice(rng, 25, 40, 60, 75, 90)
    return mk(rng, P, [(0, "Constant velocity needs zero RESULTANT force, not zero friction."), (P / 2, "At constant velocity the forces balance exactly."), (2 * P, "Friction cannot exceed the push if the velocity is constant.")],
              "N", f"A box is pushed at a **constant velocity** with a horizontal force of **{P} N** (Fig. 1). What is the frictional force on it?",
              "constant velocity → resultant force = 0 → friction = push", [f"friction = **{P} N** (opposite to the push)"],
              ["What is the resultant force when the velocity is constant?", "Newton's first law: zero.", "So friction must equal the push."],
              figure=figs2.forces_on_line([(f"{P} N", "right", 1), ("friction = ?", "left", 1)], body="box"))


# ================================================================== L2
@template("c3x_mass_from_moon_weight", chapter=3, level=2, lo="3e")
def mass_from_moon_weight(rng):
    m = nice(rng, 5, 10, 20, 60, 80)
    W = m * 1.6
    return mk(rng, m, [(W / G, "Use the Moon's g (1.6 N/kg), not the Earth's."), (W * 1.6, "m = W ÷ g."), (W, "That is the weight; divide by g.")],
              "kg", f"An astronaut's toolkit weighs **{fmt(W)} N** on the Moon.\n\n{md_table(['quantity', 'value'], [['weight on the Moon', f'{fmt(W)} N'], ['g on the Moon', '1.6 N/kg']])}\n\nWhat is the mass of the toolkit?",
              "W = m g → m = W ÷ g", [f"m = {fmt(W)} ÷ 1.6 = **{fmt(m)} kg**"],
              ["Which g applies on the Moon?", "m = W ÷ g.", f"{fmt(W)} ÷ 1.6."])


@template("c3x_mass_from_fa", chapter=3, level=2, lo="3j")
def mass_from_fa(rng):
    a = nice(rng, 0.5, 2.0, 2.5, 4.0)
    m = nice(rng, 4, 8, 20, 40, 100)
    F = m * a
    return mk(rng, m, [(F * a, "m = F ÷ a."), (a / F, "m = F ÷ a, not a ÷ F."), (F, "Divide by the acceleration.")],
              "kg", f"A resultant force of **{fmt(F)} N** gives a sledge an acceleration of **{fmt(a)} m/s²** (Fig. 1). What is the mass of the sledge?",
              "F = m a → m = F ÷ a", [f"m = {fmt(F)} ÷ {fmt(a)} = **{fmt(m)} kg**"],
              ["Rearrange F = m a for m.", "Divide F by a.", "Check: a heavier sledge accelerates less."], figure=figs.force_diagram([(f"{fmt(F)} N", "right", 1.3)], label_body="sledge"))


@template("c3x_g_planet_falling", chapter=3, level=2, lo="3d")
def g_planet_falling(rng):
    g = nice(rng, 1.6, 3.7, 8.9, 25)
    m = nice(rng, 0.5, 2.0, 5.0)
    W = m * g
    return mk(rng, g, [(W * m, "g = W ÷ m."), (m / W, "g = W ÷ m."), (W / 10, "Do not use the Earth's g: find this planet's g from the data.")],
              "N/kg", f"A lander weighs a sample on another planet.\n\n{md_table(['quantity', 'value'], [['mass of sample', f'{fmt(m)} kg'], ['weight on the planet', f'{fmt(W)} N']])}\n\nWhat is the gravitational field strength on the planet?",
              "g = W ÷ m", [f"g = {fmt(W)} ÷ {fmt(m)} = **{fmt(g)} N/kg**"],
              ["g = gravitational force per unit mass.", "Divide weight by mass.", f"{fmt(W)} ÷ {fmt(m)}."])


@template("c3x_g_acceleration_free_fall", chapter=3, level=2, lo="3d")
def g_acceleration_free_fall(rng):
    g = nice(rng, 1.6, 3.7, 10, 25)
    t = nice(rng, 1, 2, 3)
    v = g * t
    return mk(rng, g, [(v, "That is the speed reached; divide by the time."), (v * t, "a = Δv ÷ t."), (t / v, "a = Δv ÷ t, not t ÷ Δv.")],
              "N/kg", f"A hammer is dropped from rest on another world (no air). Fig. 1 is its velocity-time graph: after **{t} s** its speed is **{fmt(v)} m/s**. The acceleration of free fall equals g in N/kg. What is g there?",
              "acceleration of free fall (m/s²) = g (N/kg); a = Δv ÷ t", [f"a = {fmt(v)} ÷ {t} = **{fmt(g)} N/kg**"],
              ["In free fall the only force is weight, so a = W/m = g.", "Find a from the speed and time.", f"{fmt(v)} ÷ {t}."], figure=figs.graph([(0, 0), (t, v)], t, v * 1.2 + 1, 1, max(1, round(v / 5))))


@template("c3x_friction_from_resultant", chapter=3, level=2, lo="3l")
def friction_from_resultant(rng):
    P = nice(rng, 50, 60, 80, 100)
    R = nice(rng, 10, 15, 20, 30)
    return mk(rng, P - R, [(P + R, "Friction = push − resultant."), (R, "That is the resultant force."), (P, "Some of the push is cancelled by friction.")],
              "N", f"A trolley is pushed with **{P} N**. The resultant force on it is **{R} N** forwards (Fig. 1). What is the frictional force?",
              "resultant = push − friction → friction = push − resultant", [f"friction = {P} − {R} = **{P - R} N**"],
              ["Write the resultant in terms of the push and friction.", "R = P − f.", f"f = {P} − {R}."], figure=figs2.forces_on_line([(f"{P} N", "right", P), ("friction", "left", P - R)], body="trolley"))


@template("c3x_friction_from_accel", chapter=3, level=2, lo="3l")
def friction_from_accel(rng):
    m = nice(rng, 2, 4, 5, 10)
    a = nice(rng, 1, 2, 3)
    P = m * a + nice(rng, 4, 6, 8, 10)
    f = P - m * a
    return mk(rng, f, [(m * a, "That is the resultant force. Friction = push − resultant."), (P, "Subtract the resultant from the push."), (P + m * a, "Friction is the difference, not the sum.")],
              "N", f"A block is pulled along a bench.\n\n{md_table(['quantity', 'value'], [['pull', f'{P} N'], ['mass', f'{m} kg'], ['acceleration', f'{a} m/s²']])}\n\nWhat is the friction on the block?",
              "resultant = m a; friction = pull − resultant", [f"resultant = {m} × {a} = {m * a} N", f"friction = {P} − {m * a} = **{f} N**"],
              ["Find the resultant force from F = m a.", "The pull minus friction equals the resultant.", "Solve for friction."])


@template("c3x_terminal_drag", chapter=3, level=2, lo="3m")
def terminal_drag(rng):
    m = nice(rng, 60, 70, 80, 90, 95)
    return mk(rng, m * G, [(m, "That is the mass. At terminal velocity, drag = weight in newtons."), (0, "Drag is not zero; the RESULTANT force is zero."), (m * G / 2, "The forces balance exactly.")],
              "N", f"A parachutist of total mass **{m} kg** falls at a steady terminal velocity (Fig. 1). What is the air resistance on her (g = 10 N/kg)?",
              "terminal velocity → resultant force zero → air resistance = weight = m g", [f"air resistance = {m} × 10 = **{m * G} N**"],
              ["What is the resultant force at constant velocity?", "So how does air resistance compare with weight?", "Weight = m g."], figure=figs.force_diagram([("air resistance", "up", 1.1), ("weight", "down", 1.1)], label_body="diver", ground=False))


@template("c3x_terminal_mass", chapter=3, level=2, lo="3m")
def terminal_mass(rng):
    D = nice(rng, 600, 750, 800, 900)
    return mk(rng, D / G, [(D, "That is the drag force in N. Divide by g for the mass."), (D * G, "m = W ÷ g."), (D / 9.8 if abs(D / 9.8 - D / G) > 1 else D / G + 5, "Use g = 10 N/kg.")],
              "kg", f"A skydiver falls at terminal velocity. The air resistance on him is **{D} N**.\n\n{md_table(['quantity', 'value'], [['air resistance', f'{D} N'], ['g', '10 N/kg']])}\n\nWhat is his total mass?",
              "terminal velocity → weight = air resistance; m = W ÷ g", [f"W = {D} N", f"m = {D} ÷ 10 = **{fmt(D / G)} kg**"],
              ["At terminal velocity the forces balance.", "So his weight equals the air resistance.", "m = W ÷ g."])


# ================================================================== L3
@template("c3x_weight_mass_conversion", chapter=3, level=3, lo="3e")
def weight_mass_conversion(rng):
    W = nice(rng, 2.5, 4.0, 6.0, 12)
    m_g = W / G * 1000
    return mk(rng, m_g, [(W / G, "That is in kg; the answer is asked in grams."), (W * 1000, "Divide by g before converting to grams."), (W / G * 100, "1 kg = 1000 g.")],
              "g", f"A bag of flour hanging on the spring balance in Fig. 1 has a weight of **{fmt(W)} N** (g = 10 N/kg). What is its mass in grams?",
              "m = W ÷ g, then kg → g (× 1000)", [f"m = {fmt(W)} ÷ 10 = {fmt(W / G)} kg", f"= **{fmt(m_g)} g**"],
              ["m = W ÷ g gives kg.", "Then convert to g.", "× 1000."], figure=sketches.spring_balance(f"{fmt(W)} N", "flour"))


@template("c3x_weight_two_planets", chapter=3, level=3, lo="3e")
def weight_two_planets(rng):
    gp, planet = rng.choice([(1.6, "the Moon"), (3.7, "Mars"), (25, "Jupiter")])
    W_e = nice(rng, 300, 450, 600, 700)
    m = W_e / G
    W_p = m * gp
    return mk(rng, W_p, [(W_e, "Weight changes with g; only the mass stays the same."), (W_e * gp, "Find the mass first: m = W ÷ 10."), (m, "That is the mass; multiply by the new g.")],
              "N", f"An astronaut weighs **{W_e} N** on Earth (g = 10 N/kg). On {planet}, g = **{fmt(gp)} N/kg** (Fig. 1). What is her weight on {planet}?",
              "m = W_E ÷ g_E (same everywhere); W = m g_planet", [f"m = {W_e} ÷ 10 = {fmt(m)} kg", f"W = {fmt(m)} × {fmt(gp)} = **{fmt(W_p)} N**"],
              ["What stays the same on another planet?", "Find the mass from her Earth weight.", "Multiply by the new g."], figure=sketches.two_bodies_sketch([f"{W_e} N", "g = 10 N/kg"], ["? N", f"g = {fmt(gp)} N/kg"], "Earth", planet.replace("the ", "")))


@template("c3x_friction_needed_accel", chapter=3, level=3, lo="3l")
def friction_needed_accel(rng):
    m = nice(rng, 800, 1000, 1200, 1500)
    u = nice(rng, 15, 20, 25)
    t = nice(rng, 4, 5)
    a = u / t
    return mk(rng, m * a, [(m * u, "Find the deceleration first (Δv ÷ t), then F = m a."), (m * a / G, "F = m a, no division by g."), (u / t, "That is the deceleration; multiply by the mass.")],
              "N", f"A car of mass **{m} kg** moving at **{u} m/s** brakes uniformly to rest in **{t} s** (Fig. 1). What is the braking (friction) force?",
              "a = Δv ÷ t; F = m a", [f"a = {u} ÷ {t} = {fmt(a)} m/s²", f"F = {m} × {fmt(a)} = **{fmt(m * a)} N**"],
              ["First find the deceleration.", "Δv ÷ t.", "Then F = m a."], figure=figs.graph([(0, u), (t, 0)], t + 1, u + 5, 1, 5))


@template("c3x_two_forces_accel", chapter=3, level=3, lo="3l")
def two_forces_accel(rng):
    m = nice(rng, 5, 10, 20, 40)
    P = nice(rng, 60, 80, 100, 150)
    f = nice(rng, 20, 30, 40)
    a = (P - f) / m
    return mk(rng, a, [(P / m, "Use the RESULTANT force: push − friction."), ((P + f) / m, "Friction opposes the push; subtract."), (f / m, "That uses only the friction.")],
              "m/s²", f"A cart of mass **{m} kg** is pushed with **{P} N**; friction is **{f} N** (Fig. 1). What is its acceleration?",
              "a = (push − friction) ÷ m", [f"resultant = {P} − {f} = {P - f} N", f"a = {P - f} ÷ {m} = **{fmt(a)} m/s²**"],
              ["Find the resultant force first.", "Then use F = m a.", f"({P} − {f}) ÷ {m}."], figure=figs2.forces_on_line([(f"{P} N", "right", P), (f"{f} N", "left", f)], body=f"{m} kg"))


@template("c3x_falling_accel_drag", chapter=3, level=3, lo="3m")
def falling_accel_drag(rng):
    m = nice(rng, 60, 70, 80)
    D = nice(rng, 200, 300, 400, 500)
    a = (m * G - D) / m
    return mk(rng, a, [(G, "That is the acceleration with NO air resistance."), (D / m, "Use the resultant (weight − drag)."), ((m * G + D) / m, "Drag acts upwards: subtract it.")],
              "m/s²", f"A skydiver of mass **{m} kg** is falling. At one instant the air resistance is **{D} N** (Fig. 1). What is her acceleration at that instant (g = 10 N/kg)?",
              "resultant = weight − air resistance; a = resultant ÷ m", [f"W = {m * G} N; resultant = {m * G} − {D} = {m * G - D} N", f"a = {m * G - D} ÷ {m} = **{fmt(a)} m/s²**"],
              ["Which two forces act, and in which directions?", "Resultant = W − drag.", "a = resultant ÷ m."], figure=figs.force_diagram([(f"{D} N", "up", 0.8), (f"W = {m * G} N", "down", 1.3)], label_body="diver", ground=False))


@template("c3x_drag_at_accel", chapter=3, level=3, lo="3m")
def drag_at_accel(rng):
    m = nice(rng, 0.2, 0.5, 1.0, 2.0)
    a = nice(rng, 2, 4, 6, 8)
    D = m * G - m * a
    return mk(rng, D, [(m * a, "That is the resultant force; drag = weight − resultant."), (m * G, "That is the weight."), (m * G + m * a, "Subtract the resultant from the weight.")],
              "N", f"A ball of mass **{fmt(m)} kg** falls through air with an acceleration of **{a} m/s²**.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['acceleration', f'{a} m/s²'], ['g', '10 N/kg']])}\n\nWhat is the air resistance on the ball?",
              "W − D = m a → D = m g − m a", [f"W = {fmt(m * G)} N; m a = {fmt(m * a)} N", f"D = {fmt(m * G)} − {fmt(m * a)} = **{fmt(D)} N**"],
              ["Write Newton's second law with both forces.", "Weight down, drag up.", "D = W − m a."])


@template("c3x_third_force_right_angle", chapter=3, level=3, lo="3i")
def third_force_right_angle(rng):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (12, 16, 20)])
    return mk(rng, c, [(a + b, "The two forces are at right angles; their resultant is found with Pythagoras or a scale drawing."), (abs(a - b), "Subtraction applies only to opposite forces."), (c * 2, "The third force equals the resultant of the other two.")],
              "N", f"A ring is held still by three forces. Two of them, **{a} N** and **{b} N**, act at right angles (Fig. 1). What is the size of the third force?",
              "equilibrium: third force = equal and opposite to the resultant of the other two", [f"resultant of {a} N and {b} N = √({a}² + {b}²) = {c} N", f"third force = **{c} N**, opposite to that resultant"],
              ["For the ring to stay still, what must the resultant of all three be?", "So the third force must cancel the other two.", "Find their resultant."], figure=figs2.vector_grid([(f"{a} N", a, 0), (f"{b} N", 0, b)], nx=max(a, 4) + 3, ny=max(b, 4) + 2, origin=(1, 1)) if max(a, b) <= 12 else figs2.vector_pair(f"{a} N", f"{b} N", 90))


@template("c3x_hanging_two_strings", chapter=3, level=3, lo="3i")
def hanging_two_strings(rng):
    T = nice(rng, 20, 30, 40, 50)
    return mk(rng, T, [(2 * T, "Each string is at 60° to the vertical, so only half of each tension acts upwards (T cos 60°)."), (T / 2, "There are two strings; each supplies T cos 60° = T/2 upwards."), (T * math.sqrt(3), "Use cos 60° = 0.5 for the vertical part.")],
              "N", f"A picture hangs at rest from two strings, each at **60° to the vertical**. Each string has a tension of **{T} N** (Fig. 1). A scale drawing of the three forces closes into a triangle. What is the weight of the picture?",
              "equilibrium: the vertical parts of the tensions balance the weight; each = T cos 60° = T/2", [f"vertical part of each tension = {T} × cos 60° = {fmt(T / 2)} N", f"W = 2 × {fmt(T / 2)} = **{T} N**"],
              ["The three forces balance: they form a closed triangle.", "The strings are at 60° to the vertical; how much of each tension acts upwards?", "Add the two upward parts."], figure=figs2.vector_pair(f"T = {T} N", f"T = {T} N", 120))


# ================================================================== L4
@template("c3x_force_from_vt", chapter=3, level=4, lo="3j")
def force_from_vt(rng):
    m = nice(rng, 50, 80, 100, 200)
    v = nice(rng, 6, 8, 10, 12)
    t = nice(rng, 4, 5)
    return mk(rng, m * v / t, [(m * v, "Find the acceleration from the gradient first."), (m * v * t / 2, "That uses the area, not the gradient."), (v / t, "That is the acceleration; multiply by the mass.")],
              "N", f"Fig. 1 is the velocity-time graph of a go-kart of mass **{m} kg** accelerating from rest. What resultant force acts on it?",
              "a = gradient of v-t; F = m a", [f"a = {v} ÷ {t} = {fmt(v / t)} m/s²", f"F = {m} × {fmt(v / t)} = **{fmt(m * v / t)} N**"],
              ["What does the gradient of a v-t graph give?", "Find a, then use F = m a.", f"a = {v} ÷ {t}."], figure=figs.graph([(0, 0), (t, v), (t + 3, v)], t + 3, v + 4, 1, 2))


@template("c3x_braking_force_distance", chapter=3, level=4, lo="3l")
def braking_force_distance(rng):
    m = nice(rng, 1000, 1200, 1500)
    u = nice(rng, 20, 25, 30)
    t = nice(rng, 4, 5, 6)
    a = u / t
    return mk(rng, m * a, [(m * u / (t * t), "a = Δv ÷ t."), (m * u, "Divide by the time to get the deceleration."), (m * a / 2, "F = m a; no ½.")],
              "N", f"A car of mass **{m} kg** brakes from **{u} m/s** to rest. Fig. 1 is its velocity-time graph. What braking force acts on the car?",
              "deceleration = gradient; braking force = m a", [f"a = {u} ÷ {t} = {fmt(a)} m/s²", f"F = {m} × {fmt(a)} = **{fmt(m * a)} N**"],
              ["Find the deceleration from the graph.", "Gradient = Δv ÷ Δt.", "F = m a."], figure=figs.graph([(0, u), (t, 0)], t + 1, u + 5, 1, 5))


@template("c3x_three_forces_equal", chapter=3, level=4, lo="3i")
def three_forces_equal(rng):
    W = nice(rng, 20, 40, 50, 60)
    ang = 120
    return mk(rng, W, [(W / 2, "At 120° to each other, the three forces are equal when they balance."), (W * 2, "The tensions are not twice the weight at this angle."), (W / math.sqrt(3), "Check with a scale drawing: an equilateral triangle closes.")],
              "N", f"A lamp of weight **{W} N** hangs from two cables. The cables and the vertical line of the weight are at **120°** to one another (Fig. 1). The lamp is at rest. What is the tension in each cable?",
              "three forces in equilibrium at 120° to each other form an equilateral triangle: all equal", [f"the force triangle is equilateral", f"T = W = **{W} N**"],
              ["Draw the three forces tip to tail: what triangle do they make?", "All angles between the forces are 120°.", "An equilateral triangle has equal sides."], figure=figs2.vector_pair("T", "T", 120))


@template("c3x_resultant_tensions", chapter=3, level=4, lo="3i")
def resultant_tensions(rng):
    a, b, c = rng.choice([(30, 40, 50), (60, 80, 100), (24, 7, 25), (12, 5, 13), (15, 20, 25)])
    return mk(rng, c, [(a + b, "The ropes are at right angles; use a scale drawing or Pythagoras."), (abs(a - b), "Subtract only for opposite forces."), (c / 2, "Use the full tensions.")],
              "N", f"A crate hangs at rest from two ropes at right angles to each other, with tensions **{a} N** and **{b} N** (Fig. 1). What is the weight of the crate?",
              "equilibrium: weight = resultant of the two tensions (diagonal of the rectangle)", [f"W = √({a}² + {b}²) = **{c} N**"],
              ["The two tensions together must hold up the weight.", "Their resultant must equal the weight.", "Perpendicular: Pythagoras."], figure=figs2.vector_pair(f"{a} N", f"{b} N", 90))


@template("c3x_drag_from_gradient", chapter=3, level=4, lo="3m")
def drag_from_gradient(rng):
    m = nice(rng, 60, 70, 80)
    a = nice(rng, 4, 5, 6)
    D = m * (G - a)
    return mk(rng, D, [(m * a, "That is the resultant force. Air resistance = weight − m a."), (m * G, "That is the weight."), (m * (G + a), "Air resistance acts upwards: subtract.")],
              "N", f"Fig. 1 is part of the velocity-time graph of a skydiver of mass **{m} kg**. At the moment shown the gradient gives her acceleration as **{a} m/s²**. What is the air resistance on her (g = 10 N/kg)?",
              "a from gradient; W − D = m a → D = m (g − a)", [f"W = {m * G} N; m a = {m * a} N", f"D = {m * G} − {m * a} = **{D} N**"],
              ["What does the gradient of a v-t graph give?", "Write W − D = m a.", "Solve for D."], figure=figs.graph([(0, 0), (2, 18), (4, 32), (6, 41), (8, 45), (10, 46)], 10, 55, 2, 10))


@template("c3x_terminal_heavier", chapter=3, level=4, lo="3m")
def terminal_heavier(rng):
    m1 = nice(rng, 60, 70)
    m2 = m1 + nice(rng, 10, 20, 30)
    return mk(rng, m2 * G, [(m1 * G, "That is the first diver's terminal drag. The heavier diver needs more drag to balance."), (m2, "Drag is a force in N."), ((m1 + m2) * G / 2, "Each diver's drag balances their OWN weight.")],
              "N", f"Two skydivers in the same position fall at their terminal velocities.\n\n{md_table(['diver', 'mass / kg'], [['A', m1], ['B', m2]])}\n\nWhat is the air resistance on diver B?",
              "at terminal velocity drag = own weight", [f"drag on B = {m2} × 10 = **{m2 * G} N** (B must fall faster to reach this drag)"],
              ["At terminal velocity, what balances the weight?", "Use B's weight only.", "W = m g."])


@template("c3x_moon_earth_ratio", chapter=3, level=4, lo="3f")
def moon_earth_ratio(rng):
    m = nice(rng, 2, 5, 10, 20)
    gm = 1.6
    return mk(rng, m, [(m * gm, "That is the weight on the Moon. A beam balance compares MASSES, so it reads the same."), (m * G / gm, "Mass does not depend on g."), (m * gm / G, "The mass is unchanged on the Moon.")],
              "kg", f"A beam balance shows that a rock has a mass of **{m} kg** on Earth. The rock and the balance are taken to the Moon (g = 1.6 N/kg), as in Fig. 1. What does the beam balance show there?",
              "mass is the amount of matter: the same everywhere; a beam balance compares masses", [f"mass on the Moon = **{m} kg** (its weight changes from {m * G} N to {fmt(m * gm)} N)"],
              ["Does the amount of matter change?", "A beam balance compares the rock with standard masses; both feel the same g.", "So the reading is unchanged."], figure=sketches.two_bodies_sketch([f"{m} kg rock"], ["? kg"], "Earth", "Moon"))


@template("c3x_spring_balance_mars", chapter=3, level=4, lo="3f")
def spring_balance_mars(rng):
    W_e = nice(rng, 20, 30, 50, 80)
    g = 3.7
    W_m = W_e / G * g
    return mk(rng, W_m, [(W_e, "A spring balance measures WEIGHT, which is smaller on Mars."), (W_e / G, "That is the mass in kg, not the spring balance reading."), (W_e * g, "Find the mass first: m = W ÷ 10.")],
              "N", f"The spring balance in Fig. 1 reads **{W_e} N** when holding a box on Earth (g = 10 N/kg). What will it read when holding the same box on Mars (g = 3.7 N/kg)?",
              "m = W_E ÷ 10; reading on Mars = m × 3.7", [f"m = {W_e} ÷ 10 = {fmt(W_e / G)} kg", f"reading = {fmt(W_e / G)} × 3.7 = **{fmt(W_m)} N**"],
              ["What does a spring balance measure?", "The mass is unchanged; the weight depends on g.", "Use the mass with the new g."], figure=sketches.spring_balance(f"{W_e} N on Earth", "box"))


# ================================================================== L5
@template("c3x_weight_vs_mass_lift", chapter=3, level=5, lo="3f")
def weight_vs_mass_lift(rng):
    m = nice(rng, 50, 60, 70)
    g_p = nice(rng, 1.6, 3.7)
    W_p = m * g_p
    F_jump = nice(rng, 300, 400)
    a = (F_jump - W_p) / m
    return mk(rng, a, [((F_jump - m * G) / m if F_jump > m * G else (F_jump - W_p) / m + 2, "Use the weight on this world (m × local g), not the Earth weight."), (F_jump / m, "Subtract the weight to get the resultant force."), ((F_jump + W_p) / m, "Weight acts downwards: subtract it.")],
              "m/s²", f"An astronaut of mass **{m} kg** on a world where g = **{fmt(g_p)} N/kg** pushes up from the ground with a force of **{F_jump} N**.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} kg'], ['local g', f'{fmt(g_p)} N/kg'], ['upward push from the ground', f'{F_jump} N']])}\n\nWhat is her upward acceleration while pushing?",
              "W = m g_local; resultant = push − W; a = resultant ÷ m", [f"W = {m} × {fmt(g_p)} = {fmt(W_p)} N", f"resultant = {F_jump} − {fmt(W_p)} = {fmt(F_jump - W_p)} N", f"a = **{fmt(a)} m/s²**"],
              ["Her mass is the same as on Earth, but her weight here is different.", "Work out her local weight.", "Resultant ÷ mass."])


@template("c3x_two_blocks_tension", chapter=3, level=5, lo="3j")
def two_blocks_tension(rng):
    m1, m2 = nice(rng, 2, 3, 4), nice(rng, 1, 2, 6)
    F = nice(rng, 12, 18, 24, 30)
    a = F / (m1 + m2)
    T = m2 * a
    return mk(rng, T, [(F, "The rope only has to accelerate the REAR block, not both."), (m1 * a, "The rope pulls block B; use B's mass."), (F / 2, "The tension depends on the masses, not simply half the force.")],
              "N", f"Two blocks on a smooth floor are joined by a light rope. A force of **{F} N** pulls block A (**{m1} kg**), which pulls block B (**{m2} kg**) behind it (Fig. 1). What is the tension in the rope?",
              "a = F ÷ (total mass); tension = m_B × a", [f"a = {F} ÷ ({m1} + {m2}) = {fmt(a)} m/s²", f"T = {m2} × {fmt(a)} = **{fmt(T)} N**"],
              ["Both blocks have the same acceleration. Find it using the total mass.", "Now look at block B alone: which force accelerates it?", "T = m_B a."], figure=figs2.forces_on_line([(f"{F} N on A", "right", 1)], body=f"B {m2} kg — A {m1} kg"))


@template("c3x_terminal_force_balance", chapter=3, level=5, lo="3m")
def terminal_force_balance(rng):
    m = nice(rng, 70, 80, 90)
    D_open = nice(rng, 1500, 1800, 2000)
    a = (D_open - m * G) / m
    return mk(rng, a, [(D_open / m, "Weight still acts: resultant = drag − weight."), ((D_open + m * G) / m, "Drag and weight act in opposite directions."), (G, "That is free-fall acceleration; here the drag is larger than the weight.")],
              "m/s²", f"A parachutist of mass **{m} kg** opens her parachute. Just after it opens, the air resistance is **{D_open} N** (Fig. 1). What is the size of her deceleration at that moment (g = 10 N/kg)?",
              "resultant = drag − weight (upwards); deceleration = resultant ÷ m", [f"W = {m * G} N; resultant = {D_open} − {m * G} = {D_open - m * G} N upwards", f"deceleration = **{fmt(a)} m/s²**"],
              ["Which is larger now, drag or weight?", "The resultant acts upwards, so she slows down.", "a = resultant ÷ m."], figure=figs.force_diagram([(f"{D_open} N", "up", 1.4), (f"W = {m * G} N", "down", 0.8)], label_body="diver", ground=False))


@template("c3x_friction_incline_free", chapter=3, level=5, lo="3l")
def friction_coasting(rng):
    m = nice(rng, 60, 80, 100)
    u = nice(rng, 6, 8, 10)
    d = nice(rng, 20, 25, 40)
    a = u * u / (2 * d)
    f = m * a
    t = u / a
    return mk(rng, f, [(m * u / d, "Use the deceleration from the area of the v-t graph: d = ½ u t, so a = u ÷ t."), (m * u * u / d, "The stopping distance is the area ½ u t; find t, then a."), (f * 2, "Check: a = u² ÷ (2 d).")],
              "N", f"A cyclist and bicycle of total mass **{m} kg** stop pedalling at **{u} m/s** and coast to rest in **{d} m** under a constant friction force (Fig. 1). What is the friction force?",
              "area of v-t triangle = d → t = 2d ÷ u; a = u ÷ t; F = m a", [f"t = 2 × {d} ÷ {u} = {fmt(t)} s", f"a = {u} ÷ {fmt(t)} = {fmt(a)} m/s²", f"F = {m} × {fmt(a)} = **{fmt(f)} N**"],
              ["Sketch the v-t graph: a triangle with area equal to the stopping distance.", "Use the area to find the time, then the deceleration.", "F = m a."], figure=figs.graph([(0, u), (t, 0)], t + 1, u + 2, max(1, round(t / 5)), 2))


@template("c3x_friction_two_stage", chapter=3, level=5, lo="3l")
def friction_two_stage(rng):
    m = nice(rng, 20, 25, 40)
    a1 = nice(rng, 2, 3)
    f = nice(rng, 20, 30, 40, 60)
    P = m * a1 + f
    a2 = f / m
    return mk(rng, a2, [(a1, "Once the push stops, only friction acts; the acceleration changes."), (P / m, "That is the push alone."), ((P - f) / m, "That is the acceleration while pushing.")],
              "m/s²", f"A sledge of mass **{m} kg** is pushed with **{P} N** and accelerates at **{a1} m/s²**. The push then stops but the same friction acts.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} kg'], ['push', f'{P} N'], ['acceleration while pushed', f'{a1} m/s²']])}\n\nWhat is the size of its deceleration after the push stops?",
              "while pushed: P − f = m a₁ → f; after: deceleration = f ÷ m", [f"f = {P} − {m} × {a1} = {f} N", f"deceleration = {f} ÷ {m} = **{fmt(a2)} m/s²**"],
              ["Find the friction from the first stage.", "After the push stops, friction is the only horizontal force.", "a = f ÷ m."])


@template("c3x_three_forces_scale", chapter=3, level=5, lo="3i")
def three_forces_scale(rng):
    W = nice(rng, 30, 40, 60, 80)
    ang = nice(rng, 30, 45)
    T = W / (2 * math.cos(math.radians(ang)))
    return mk(rng, T, [(W / 2, "Only the vertical part of each tension (T cos θ) supports the weight."), (W, "Two strings share the weight."), (W / (2 * math.sin(math.radians(ang))), "Use cos θ for the angle with the VERTICAL.")],
              "N", f"A sign of weight **{W} N** hangs at rest from two equal chains, each at **{ang}° to the vertical** (Fig. 1). By a scale drawing (or calculation), what is the tension in each chain?",
              "equilibrium: 2 T cos θ = W", [f"2 T cos {ang}° = {W}", f"T = {W} ÷ (2 × {fmt(math.cos(math.radians(ang)), sf=3)}) = **{fmt(T, sf=3)} N**"],
              ["The three forces close into a triangle.", "Each chain's upward part is T cos θ.", "Two chains: 2 T cos θ = W."], figure=figs2.vector_pair("T", "T", 2 * ang))


@template("c3x_lift_reading", chapter=3, level=5, lo="3j")
def lift_reading(rng):
    m = nice(rng, 50, 60, 70)
    a = nice(rng, 1.0, 1.5, 2.0)
    up = rng.choice([True, False])
    R = m * (G + a) if up else m * (G - a)
    return mk(rng, R, [(m * G, "That is the reading when the lift is NOT accelerating."), (m * (G - a) if up else m * (G + a), "Check the direction: accelerating upwards needs a reaction BIGGER than the weight." if up else "Accelerating downwards: the reaction is LESS than the weight."), (m * a, "That is only the resultant force.")],
              "N", f"A student of mass **{m} kg** stands on bathroom scales (which read the normal force in N) in a lift that is accelerating **{'upwards' if up else 'downwards'}** at **{fmt(a)} m/s²** (Fig. 1). What do the scales read?",
              "R − W = m a (upwards positive)", [f"W = {m * G} N", f"R = {m * G} {'+' if up else '−'} {m} × {fmt(a)} = **{fmt(R)} N**"],
              ["Two forces act on the student: weight and the normal force.", "The resultant gives the acceleration.", "Solve for the normal force."], figure=sketches.lift_sketch(f"a = {fmt(a)} m/s² {'up' if up else 'down'}", body_label="student"))


@template("c3x_third_force_direction", chapter=3, level=5, lo="3i")
def third_force_direction(rng):
    a, b = rng.choice([(6, 8), (8, 6), (5, 12), (12, 5), (9, 12)])
    ang = math.degrees(math.atan2(b, a))
    return mk(rng, ang, [(90 - ang, "Measure the angle from the direction stated in the question (the east-pointing force's line)."), (ang + 90, "The third force points opposite to the resultant, but its angle below the west line equals the resultant's angle above the east line."), (45, "45° only if the two forces are equal.")],
              "°", f"A ring is held at rest by three forces. One is **{a} N** due east and another is **{b} N** due north (Fig. 1). The third force points south-west. At what angle below the westward direction does it act?",
              "equilibrium: third force = minus (resultant of the other two); tan θ = b ÷ a", [f"the resultant of {a} N E and {b} N N is at tan⁻¹({b}/{a}) = {fmt(ang, sf=3)}° north of east", f"the third force is opposite: **{fmt(ang, sf=3)}°** south of west"],
              ["The third force must cancel the resultant of the other two.", "Find the direction of that resultant.", "The third force points exactly the opposite way."],
              figure=figs2.vector_grid([("E", a, 0), ("N", 0, b)], nx=max(a, 4) + 3, ny=max(b, 4) + 2, origin=(1, 1)), sf=3)
