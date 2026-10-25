"""Chapter 6 Energy (6091) bank extension: calculation templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2015-2024: man running up stairs, box pushed with 300 N, walker climbing a hill,
bullet through wood, golf ball, bungee jumper, hay elevator; school papers 2024-2025)."""
import math

from .. import figs, figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, template

G = 10


# ================================================================== L1
@template("c6x_work_push", chapter=6, level=1, lo="6d")
def work_push(rng):
    F = nice(rng, 20, 25, 40, 50, 80)
    d = nice(rng, 2, 3, 4, 5, 6)
    return mk(rng, F * d, [(F / d, "Work done = force × distance, not ÷."), (F + d, "Multiply force by distance."), (F * d / 2, "No ½ in W = F d.")],
              "J", f"A crate is pushed with a force of **{F} N** through a distance of **{d} m** in the direction of the force (Fig. 1). How much work is done?",
              "W = F × d", [f"W = {F} × {d} = **{F * d} J**"],
              ["Work done = force × distance moved in the direction of the force.", "Both values are in SI units.", "Multiply."], figure=sketches.push_sketch(f"{F} N", f"{d} m"))


@template("c6x_work_lift", chapter=6, level=1, lo="6d")
def work_lift(rng):
    W = nice(rng, 20, 40, 50, 80, 120)
    h = nice(rng, 1.5, 2.0, 2.5, 3.0)
    return mk(rng, W * h, [(W * h * G, "The weight is already in newtons; do not multiply by g again."), (W / h, "W = F × d."), (W + h, "Multiply.")],
              "J", f"A box of weight **{W} N** is lifted steadily through a height of **{fmt(h)} m** (Fig. 1). How much work is done against gravity?",
              "W = F × d = weight × height", [f"W = {W} × {fmt(h)} = **{fmt(W * h)} J**"],
              ["The force needed equals the weight.", "The distance is the height lifted.", "Multiply."], figure=sketches.lift_sketch(f"{fmt(h)} m", f"{W} N"))


@template("c6x_power_simple", chapter=6, level=1, lo="6e")
def power_simple(rng):
    E = nice(rng, 600, 1200, 1500, 2400, 3000)
    t = nice(rng, 5, 10, 20, 30)
    return mk(rng, E / t, [(E * t, "Power = energy ÷ time."), (t / E, "Energy goes on top."), (E, "Divide by the time.")],
              "W", f"A motor transfers energy.\n\n{md_table(['quantity', 'value'], [['energy transferred', f'{E} J'], ['time taken', f'{t} s']])}\n\nWhat is its power?",
              "P = E ÷ t", [f"P = {E} ÷ {t} = **{fmt(E / t)} W**"],
              ["Power = rate of energy transfer.", "P = E ÷ t.", "Divide."])


@template("c6x_energy_from_power", chapter=6, level=1, lo="6e")
def energy_from_power(rng):
    P = nice(rng, 60, 100, 500, 1000, 2000)
    t = nice(rng, 10, 30, 60, 120)
    return mk(rng, P * t, [(P / t, "E = P × t."), (P * t / 60, "The time is already in seconds."), (P, "Multiply by the time.")],
              "J", f"An appliance is switched on.\n\n{md_table(['quantity', 'value'], [['power', f'{P} W'], ['time', f'{t} s']])}\n\nHow much energy does it transfer?",
              "E = P × t", [f"E = {P} × {t} = **{fmt(P * t)} J**"],
              ["Rearrange P = E ÷ t.", "E = P × t.", "Multiply."])


@template("c6x_efficiency_simple", chapter=6, level=1, lo="6f")
def efficiency_simple(rng):
    Ein = nice(rng, 200, 400, 500, 800, 1000)
    frac = nice(rng, 0.2, 0.25, 0.4, 0.6, 0.75)
    Eout = Ein * frac
    return mk(rng, frac * 100, [(Ein / Eout * 100, "Efficiency = useful output ÷ total input (output on top)."), ((1 - frac) * 100, "That is the percentage WASTED."), (Eout, "Express as a percentage of the input.")],
              "%", f"A lamp is tested.\n\n{md_table(['energy', 'value / J'], [['total input', Ein], ['useful output (light)', fmt(Eout)]])}\n\nWhat is its efficiency?",
              "efficiency = useful output ÷ total input × 100%", [f"= {fmt(Eout)} ÷ {Ein} × 100% = **{fmt(frac * 100)}%**"],
              ["Efficiency compares useful output with total input.", "Output ÷ input.", "× 100 for a percentage."])


@template("c6x_wasted_energy", chapter=6, level=1, lo="6f")
def wasted_energy(rng):
    Ein = nice(rng, 500, 1000, 1200, 2000)
    Eu = Ein * nice(rng, 0.3, 0.45, 0.6, 0.8)
    return mk(rng, Ein - Eu, [(Eu, "That is the USEFUL energy."), (Ein + Eu, "Wasted = input − useful."), (Ein, "Subtract the useful energy.")],
              "J", f"An electric motor is used to lift a load.\n\n{md_table(['energy', 'value / J'], [['electrical energy input', Ein], ['useful output (gravitational potential energy gained)', fmt(Eu)]])}\n\nHow much energy is wasted?",
              "wasted = input − useful output (conservation of energy)", [f"wasted = {Ein} − {fmt(Eu)} = **{fmt(Ein - Eu)} J**"],
              ["Energy is conserved.", "Input = useful + wasted.", "Subtract."])


@template("c6x_ke_at_bottom", chapter=6, level=1, lo="6c")
def ke_at_bottom(rng):
    m = nice(rng, 0.5, 1.0, 2.0, 5.0)
    h = nice(rng, 2.0, 3.0, 5.0, 8.0)
    E = m * G * h
    return mk(rng, E, [(m * h, "GPE = m g h: include g."), (E / 2, "No ½ here: all the GPE becomes KE."), (m * G, "Multiply by the height too.")],
              "J", f"A ball of mass **{fmt(m)} kg** is dropped from a height of **{fmt(h)} m** (Fig. 1). Ignoring air resistance, what is its kinetic energy just before it hits the ground? (g = 10 N/kg)",
              "KE gained = GPE lost = m g h", [f"m g h = {fmt(m)} × 10 × {fmt(h)} = **{fmt(E)} J**"],
              ["Energy is conserved.", "GPE lost becomes KE.", "Find m g h."], figure=figs2.drop_sketch(f"{fmt(h)} m", f"{fmt(m)} kg"))


@template("c6x_gpe_to_ke_table", chapter=6, level=1, lo="6c")
def gpe_to_ke_table(rng):
    top = nice(rng, 200, 300, 400, 500)
    mid_frac = nice(rng, 0.25, 0.4, 0.5, 0.6)
    gpe_mid = top * mid_frac
    return mk(rng, top - gpe_mid, [(gpe_mid, "That is the GPE at the point; KE = total − GPE."), (top, "That is the total energy."), (top + gpe_mid, "Subtract, do not add.")],
              "J", f"A roller-coaster car is released from rest at the top of a track. Ignore friction.\n\n{md_table(['position', 'GPE / J', 'KE / J'], [['top', top, 0], ['point P', fmt(gpe_mid), '?']])}\n\nWhat is its kinetic energy at P?",
              "total energy is conserved: KE = total − GPE", [f"total = {top} J", f"KE at P = {top} − {fmt(gpe_mid)} = **{fmt(top - gpe_mid)} J**"],
              ["What is the total energy at the top?", "It is the same at P.", "KE = total − GPE."])


# ================================================================== L2
@template("c6x_ke_speed_kmh", chapter=6, level=2, lo="6b")
def ke_speed_kmh(rng):
    m = nice(rng, 800, 1000, 1200, 1500)
    v_kmh = nice(rng, 36, 54, 72, 90)
    v = v_kmh / 3.6
    KE = 0.5 * m * v * v
    return mk(rng, KE, [(0.5 * m * v_kmh ** 2, "Convert km/h to m/s first (÷ 3.6)."), (m * v * v, "KE = ½ m v²: include the ½."), (0.5 * m * v, "Square the speed.")],
              "J", f"A car is moving along a road.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} kg'], ['speed', f'{v_kmh} km/h']])}\n\nWhat is its kinetic energy?",
              "v in m/s = km/h ÷ 3.6; KE = ½ m v²", [f"v = {v_kmh} ÷ 3.6 = {fmt(v)} m/s", f"KE = ½ × {m} × {fmt(v)}² = **{fmt(KE)} J**"],
              ["Convert the speed to m/s.", "Use KE = ½ m v².", "Square the speed."])


@template("c6x_gpe_cm_g", chapter=6, level=2, lo="6b")
def gpe_cm_g(rng):
    m_g = nice(rng, 200, 250, 400, 500)
    h_cm = nice(rng, 40, 60, 80, 150)
    E = m_g / 1000 * G * h_cm / 100
    return mk(rng, E, [(m_g * G * h_cm, "Convert g to kg and cm to m."), (m_g / 1000 * G * h_cm, "Convert cm to m too."), (m_g * G * h_cm / 100, "Convert g to kg too.")],
              "J", f"A book is lifted onto a shelf.\n\n{md_table(['quantity', 'value'], [['mass', f'{m_g} g'], ['height raised', f'{h_cm} cm'], ['g', '10 N/kg']])}\n\nWhat is the gain in its gravitational potential energy?",
              "GPE = m g h, with m in kg and h in m", [f"m = {fmt(m_g / 1000)} kg, h = {fmt(h_cm / 100)} m", f"GPE = {fmt(m_g / 1000)} × 10 × {fmt(h_cm / 100)} = **{fmt(E)} J**"],
              ["Use SI units.", "g → kg, cm → m.", "GPE = m g h."])


@template("c6x_speed_from_drop", chapter=6, level=2, lo="6c")
def speed_from_drop(rng):
    h = nice(rng, 0.8, 1.8, 3.2, 5.0, 7.2)
    v = math.sqrt(2 * G * h)
    return mk(rng, v, [(2 * G * h, "Take the square root: v² = 2 g h."), (G * h, "v = √(2 g h)."), (math.sqrt(G * h), "Include the 2: ½ m v² = m g h → v² = 2 g h.")],
              "m/s", f"A stone falls from rest through **{fmt(h)} m** (Fig. 1). Ignoring air resistance, what is its speed when it has fallen this distance? (g = 10 N/kg)",
              "½ m v² = m g h → v = √(2 g h)", [f"v = √(2 × 10 × {fmt(h)}) = **{fmt(v)} m/s**"],
              ["GPE lost = KE gained.", "The mass cancels.", "v = √(2 g h)."], figure=figs2.drop_sketch(f"{fmt(h)} m", "stone"))


@template("c6x_pendulum_height", chapter=6, level=2, lo="6c")
def pendulum_height(rng):
    v = nice(rng, 1.0, 1.2, 1.4, 2.0)
    h = v * v / (2 * G)
    return mk(rng, h * 100, [(v * v / G * 100, "h = v² ÷ (2 g): include the 2."), (h, "That is in metres; the answer is in cm."), (v / (2 * G) * 100, "Square the speed.")],
              "cm", f"The bob of the pendulum in Fig. 1 passes its lowest point at **{fmt(v)} m/s**. Ignoring air resistance, how high above the lowest point does it rise? (g = 10 N/kg)",
              "½ m v² = m g h → h = v² ÷ (2 g)", [f"h = {fmt(v)}² ÷ 20 = {fmt(h)} m", f"= **{fmt(h * 100)} cm**"],
              ["KE at the bottom becomes GPE at the top.", "h = v² ÷ (2 g).", "Convert to cm."], figure=sketches.pendulum_sketch(f"{fmt(v)} m/s at the lowest point"))


@template("c6x_distance_from_work", chapter=6, level=2, lo="6d")
def distance_from_work(rng):
    F = nice(rng, 20, 25, 40, 50)
    d = nice(rng, 4, 5, 8, 10, 12)
    W = F * d
    m = nice(rng, 5, 8, 10)
    return mk(rng, d, [(W / (m * G), "Use the applied force, not the block's weight."), (W * F, "d = W ÷ F."), (F / W, "d = W ÷ F, not F ÷ W.")],
              "m", f"A block is pulled along a horizontal floor.\n\n{md_table(['quantity', 'value'], [['work done by the pulling force', f'{W} J'], ['pulling force (horizontal)', f'{F} N'], ['mass of block', f'{m} kg']])}\n\nHow far does the block move?",
              "W = F d → d = W ÷ F", [f"d = {W} ÷ {F} = **{fmt(d)} m**"],
              ["Which force does the work?", "The horizontal pulling force.", "d = W ÷ F."])


@template("c6x_power_stairs_weight", chapter=6, level=2, lo="6e")
def power_stairs_weight(rng):
    W = nice(rng, 500, 600, 700)
    h = nice(rng, 3.0, 4.0, 4.5, 6.0)
    t = nice(rng, 3.0, 4.0, 5.0, 6.0)
    P = W * h / t
    return mk(rng, P, [(W * h, "That is the work done; divide by the time."), (W * h * t, "P = W ÷ t."), (W * G * h / t, "The weight is already in newtons.")],
              "W", f"A student runs up a staircase.\n\n{md_table(['quantity', 'value'], [['weight of student', f'{W} N'], ['vertical height of stairs', f'{fmt(h)} m'], ['time taken', f'{fmt(t)} s']])}\n\nWhat useful power does the student develop?",
              "P = work ÷ time = W h ÷ t", [f"work = {W} × {fmt(h)} = {fmt(W * h)} J", f"P = {fmt(W * h)} ÷ {fmt(t)} = **{fmt(P)} W**"],
              ["Find the work done against gravity.", "Use the vertical height.", "Divide by the time."])


@template("c6x_useful_from_efficiency", chapter=6, level=2, lo="6f")
def useful_from_efficiency(rng):
    Ein = nice(rng, 500, 800, 1000, 2000)
    eff = nice(rng, 20, 25, 35, 40, 85)
    Eu = Ein * eff / 100
    return mk(rng, Eu, [(Ein - Eu, "That is the WASTED energy."), (Ein / (eff / 100), "Useful = efficiency × input."), (Ein * eff, "Change the percentage to a decimal.")],
              "J", f"An engine is **{eff}%** efficient.\n\n{md_table(['quantity', 'value'], [['energy input', f'{Ein} J'], ['efficiency', f'{eff}%']])}\n\nHow much useful energy does it output?",
              "useful output = efficiency × input", [f"= {eff / 100:g} × {Ein} = **{fmt(Eu)} J**"],
              ["Efficiency = useful ÷ input.", "Rearrange for useful output.", "Use the decimal."])


# ================================================================== L3
@template("c6x_bullet_ke_loss", chapter=6, level=3, lo="6b")
def bullet_ke_loss(rng):
    m = nice(rng, 0.01, 0.02, 0.05)
    u = nice(rng, 400, 500, 600)
    v = nice(rng, 100, 200, 250)
    loss = 0.5 * m * (u * u - v * v)
    return mk(rng, loss, [(0.5 * m * (u - v) ** 2, "Find each KE and subtract; do not square the change in speed."), (0.5 * m * u * u, "That is the initial KE only."), (m * (u * u - v * v), "Include the ½.")],
              "J", f"A bullet passes through a block of wood and slows down.\n\n{md_table(['quantity', 'value'], [['mass of bullet', f'{fmt(m)} kg'], ['speed before', f'{u} m/s'], ['speed after', f'{v} m/s']])}\n\nHow much kinetic energy does the bullet lose?",
              "loss = ½ m u² − ½ m v²", [f"before: ½ × {fmt(m)} × {u}² = {fmt(0.5 * m * u * u)} J", f"after: ½ × {fmt(m)} × {v}² = {fmt(0.5 * m * v * v)} J", f"loss = **{fmt(loss)} J**"],
              ["Find the KE before and after.", "KE = ½ m v².", "Subtract."])


@template("c6x_ke_double_speed", chapter=6, level=3, lo="6b")
def ke_double_speed(rng):
    E1 = nice(rng, 100, 200, 250, 400)
    k = nice(rng, 2, 3)
    E2 = E1 * k * k
    return mk(rng, E2, [(E1 * k, "KE depends on v²: multiplying v by k multiplies KE by k²."), (E1 + k, "KE is proportional to v²."), (E1 * 2 * k, "Square the factor.")],
              "J", f"A runner has **{E1} J** of kinetic energy.\n\n{md_table(['', 'speed'], [['before', 'v'], ['after', f'{k}v']])}\n\nWhat is the runner's kinetic energy at the new speed?",
              "KE ∝ v²", [f"factor = {k}² = {k * k}", f"KE = {E1} × {k * k} = **{fmt(E2)} J**"],
              ["KE = ½ m v².", "The mass is unchanged.", "Square the speed factor."])


@template("c6x_work_force_distance_graph", chapter=6, level=3, lo="6d")
def work_force_distance_graph(rng):
    F = nice(rng, 20, 30, 40)
    d1 = nice(rng, 2, 3, 4)
    d2 = d1 + nice(rng, 2, 3, 4)
    W = F * d1 + 0.5 * F * (d2 - d1)
    return mk(rng, W, [(F * d2, "The force falls to zero after the first part: use the area under the graph."), (F * d1, "Include the triangle where the force decreases."), (0.5 * F * d2, "The first part is a rectangle, not a triangle.")],
              "J", f"Fig. 1 shows how the force on a trolley varies with the distance it moves. How much work is done by the force?",
              "work done = area under the force–distance graph", [f"rectangle: {F} × {d1} = {F * d1} J", f"triangle: ½ × {F} × {d2 - d1} = {fmt(0.5 * F * (d2 - d1))} J", f"total = **{fmt(W)} J**"],
              ["Work = force × distance.", "For a varying force, use the area under the graph.", "Add the rectangle and the triangle."],
              figure=figs.graph([(0, F), (d1, F), (d2, 0)], d2 + 1, F * 1.25, 1, 10, xlabel="distance / m", ylabel="force / N"))


@template("c6x_work_against_friction", chapter=6, level=3, lo="6d")
def work_against_friction(rng):
    f = nice(rng, 30, 40, 60, 80)
    d = nice(rng, 5, 8, 10, 15)
    W = nice(rng, 200, 300, 500)
    return mk(rng, f * d, [(W * d, "The weight acts vertically; the box moves horizontally. Use the friction force."), ((f + W) * d, "Only the friction opposes the horizontal motion."), (f / d, "W = F × d.")],
              "J", f"A box is pushed at a steady speed along a floor (Fig. 1).\n\n{md_table(['quantity', 'value'], [['weight of box', f'{W} N'], ['friction force', f'{f} N'], ['distance moved', f'{d} m']])}\n\nHow much work is done against friction?",
              "work against friction = friction × distance", [f"W = {f} × {d} = **{f * d} J**"],
              ["Which force is the work done against?", "Friction, along the direction of motion.", "Multiply by the distance."], figure=sketches.push_sketch("push", f"{d} m", None, f"{f} N"))


@template("c6x_efficiency_motor_lift", chapter=6, level=3, lo="6f")
def efficiency_motor_lift(rng):
    m = nice(rng, 20, 40, 50)
    h = nice(rng, 3, 4, 5, 6)
    Ein = m * G * h / nice(rng, 0.4, 0.5, 0.6, 0.8)
    eff = m * G * h / Ein * 100
    return mk(rng, eff, [(Ein / (m * G * h) * 100, "Efficiency = useful ÷ input."), (m * h / Ein * 100, "Useful output = m g h: include g."), (100 - eff, "That is the percentage wasted.")],
              "%", f"An electric hoist lifts a load.\n\n{md_table(['quantity', 'value'], [['mass of load', f'{m} kg'], ['height raised', f'{h} m'], ['electrical energy used', f'{fmt(Ein)} J']])}\n\nWhat is the efficiency of the hoist? (g = 10 N/kg)",
              "useful output = m g h; efficiency = useful ÷ input × 100%", [f"useful = {m} × 10 × {h} = {m * G * h} J", f"efficiency = {m * G * h} ÷ {fmt(Ein)} × 100% = **{fmt(eff)}%**"],
              ["What is the useful output?", "The GPE gained.", "Divide by the input."])


@template("c6x_input_from_efficiency", chapter=6, level=3, lo="6f")
def input_from_efficiency(rng):
    Eu = nice(rng, 300, 450, 600, 900)
    eff = nice(rng, 30, 45, 60, 75)
    Ein = Eu / (eff / 100)
    return mk(rng, Ein, [(Eu * eff / 100, "The input must be LARGER than the useful output."), (Eu / eff, "Use the decimal: 30% = 0.30."), (Eu + eff, "Input = useful ÷ efficiency.")],
              "J", f"A pump must provide useful energy.\n\n{md_table(['quantity', 'value'], [['useful energy needed', f'{Eu} J'], ['efficiency of pump', f'{eff}%']])}\n\nHow much energy must be supplied to it?",
              "input = useful output ÷ efficiency", [f"input = {Eu} ÷ {eff / 100:g} = **{fmt(Ein)} J**"],
              ["Efficiency = useful ÷ input.", "Rearrange for the input.", "Divide by the decimal."])


@template("c6x_slope_speed_friction", chapter=6, level=3, lo="6c")
def slope_speed_friction(rng):
    m = nice(rng, 2, 4, 5)
    h = nice(rng, 1.8, 2.0, 3.2, 5.0)
    loss = m * G * h * nice(rng, 0.19, 0.36, 0.51)
    ke = m * G * h - loss
    v = math.sqrt(2 * ke / m)
    return mk(rng, v, [(math.sqrt(2 * G * h), "Some energy is lost to friction; subtract it first."), (2 * ke / m, "Take the square root."), (math.sqrt(2 * (m * G * h + loss) / m), "Friction REDUCES the KE.")],
              "m/s", f"A trolley of mass **{m} kg** is released from rest at the top of a slope of vertical height **{fmt(h)} m** (Fig. 1). **{fmt(loss)} J** is lost to friction on the way down. What is its speed at the bottom? (g = 10 N/kg)",
              "KE = m g h − energy lost; v = √(2 KE ÷ m)", [f"GPE lost = {m} × 10 × {fmt(h)} = {fmt(m * G * h)} J", f"KE = {fmt(m * G * h)} − {fmt(loss)} = {fmt(ke)} J", f"v = √(2 × {fmt(ke)} ÷ {m}) = **{fmt(v)} m/s**"],
              ["Find the GPE lost.", "Subtract the energy lost to friction.", "Find v from KE = ½ m v²."], figure=sketches.slope_sketch(f"{fmt(h)} m", f"{m} kg, from rest"))


@template("c6x_power_time_needed", chapter=6, level=3, lo="6e")
def power_time_needed(rng):
    m = nice(rng, 100, 200, 250, 500)
    h = nice(rng, 8, 10, 12, 20)
    P = nice(rng, 500, 1000, 2000)
    t = m * G * h / P
    return mk(rng, t, [(m * h / P, "Work = m g h: include g."), (P / (m * G * h), "t = W ÷ P."), (m * G * h * P, "Divide the work by the power.")],
              "s", f"A crane motor lifts a load.\n\n{md_table(['quantity', 'value'], [['mass of load', f'{m} kg'], ['height', f'{h} m'], ['useful power', f'{P} W']])}\n\nHow long does it take? (g = 10 N/kg)",
              "W = m g h; t = W ÷ P", [f"W = {m} × 10 × {h} = {m * G * h} J", f"t = {m * G * h} ÷ {P} = **{fmt(t)} s**"],
              ["Find the work done.", "W = m g h.", "t = W ÷ P."])


# ================================================================== L4
@template("c6x_speed_from_ke", chapter=6, level=4, lo="6b")
def speed_from_ke(rng):
    m = nice(rng, 0.05, 0.06, 0.1, 0.2)
    v = nice(rng, 10, 15, 20, 30)
    KE = 0.5 * m * v * v
    return mk(rng, v, [(v * v, "Take the square root."), (2 * KE / m / v, "v = √(2 KE ÷ m)."), (math.sqrt(KE / m), "Include the 2: v² = 2 KE ÷ m.")],
              "m/s", f"A golf ball is hit.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['kinetic energy', f'{fmt(KE)} J']])}\n\nWhat is its speed?",
              "KE = ½ m v² → v = √(2 KE ÷ m)", [f"v² = 2 × {fmt(KE)} ÷ {fmt(m)} = {fmt(v * v)}", f"v = **{fmt(v)} m/s**"],
              ["Rearrange KE = ½ m v².", "v² = 2 KE ÷ m.", "Square root."])


@template("c6x_mass_from_gpe", chapter=6, level=4, lo="6b")
def mass_from_gpe(rng):
    m = nice(rng, 12, 15, 20, 25)
    h = nice(rng, 1.5, 2.5, 4.0)
    E = m * G * h
    return mk(rng, m, [(E / h, "That is the weight in N; divide by g as well."), (E / G, "Divide by the height too."), (E * G * h, "m = E ÷ (g h).")],
              "kg", f"Bales of hay are lifted by an elevator.\n\n{md_table(['quantity', 'value'], [['GPE gained by one bale', f'{fmt(E)} J'], ['height lifted', f'{fmt(h)} m'], ['g', '10 N/kg']])}\n\nWhat is the mass of one bale?",
              "GPE = m g h → m = GPE ÷ (g h)", [f"m = {fmt(E)} ÷ (10 × {fmt(h)}) = **{fmt(m)} kg**"],
              ["Rearrange GPE = m g h.", "Divide by g and by h.", "Calculate."])


@template("c6x_braking_force", chapter=6, level=4, lo="6d")
def braking_force(rng):
    m = nice(rng, 800, 1000, 1200)
    v = nice(rng, 10, 15, 20)
    d = nice(rng, 20, 25, 40)
    F = 0.5 * m * v * v / d
    return mk(rng, F, [(m * v * v / d, "KE = ½ m v²: include the ½."), (0.5 * m * v / d, "Square the speed."), (0.5 * m * v * v * d, "F = KE ÷ d.")],
              "N", f"A car brakes to a stop.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} kg'], ['initial speed', f'{v} m/s'], ['braking distance', f'{d} m']])}\n\nWhat is the average braking force?",
              "work done by brakes = KE lost: F d = ½ m v²", [f"KE = ½ × {m} × {v}² = {fmt(0.5 * m * v * v)} J", f"F = {fmt(0.5 * m * v * v)} ÷ {d} = **{fmt(F)} N**"],
              ["The brakes do work to remove all the KE.", "F × d = ½ m v².", "Solve for F."])


@template("c6x_box_300N_work", chapter=6, level=4, lo="6d")
def box_300N_work(rng):
    F = nice(rng, 200, 250, 300)
    W = nice(rng, 500, 600, 800)
    d = nice(rng, 3.0, 4.0, 5.0)
    t = nice(rng, 10, 15, 20)
    work = F * d
    return mk(rng, work / t, [(W * d / t, "The weight acts vertically and does no work on a horizontal move; use the push."), (work, "That is the work; divide by the time for power."), ((F + W) * d / t, "Only the horizontal force does work here.")],
              "W", f"A force is applied to a box, which moves horizontally.\n\n{md_table(['quantity', 'value'], [['horizontal force applied', f'{F} N'], ['weight of box', f'{W} N'], ['distance moved', f'{fmt(d)} m'], ['time', f'{t} s']])}\n\nWhat is the average power of the applied force?",
              "W = F d (horizontal force); P = W ÷ t", [f"work = {F} × {fmt(d)} = {fmt(work)} J", f"P = {fmt(work)} ÷ {t} = **{fmt(work / t)} W**"],
              ["Which force moves the box?", "The weight does no work on a horizontal move.", "P = work ÷ time."])


@template("c6x_walker_uphill_power", chapter=6, level=4, lo="6e")
def walker_uphill_power(rng):
    W = nice(rng, 500, 600, 750)
    h = nice(rng, 10, 12, 15)
    t = 60
    return mk(rng, W * h / t, [(W * h, "That is the work in one minute; divide by 60 s."), (W * h * t, "P = work ÷ time."), (W * h / t * 60, "Use t = 60 s.")],
              "W", f"A walker climbs a hill steadily.\n\n{md_table(['quantity', 'value'], [['weight of walker', f'{W} N'], ['vertical height gained each minute', f'{h} m']])}\n\nWhat useful power does the walker develop?",
              "P = W h ÷ t with t = 60 s", [f"work each minute = {W} × {h} = {W * h} J", f"P = {W * h} ÷ 60 = **{fmt(W * h / t)} W**"],
              ["Find the work done against gravity each minute.", "Convert 1 minute to seconds.", "P = W ÷ t."])


@template("c6x_compare_power_students", chapter=6, level=4, lo="6e")
def compare_power_students(rng):
    rows = [("A", nice(rng, 50, 55), nice(rng, 5.0, 5.5)), ("B", nice(rng, 60, 65), nice(rng, 7.0, 7.5)), ("C", nice(rng, 45, 48), nice(rng, 4.0, 4.4)), ("D", nice(rng, 70, 75), nice(rng, 9.0, 9.5))]
    rng.shuffle(rows)
    h = 4.0
    P = {n: m * G * h / t for n, m, t in rows}
    best = max(P, key=P.get)
    heaviest = max(rows, key=lambda r: r[1])[0]
    fastest = min(rows, key=lambda r: r[2])[0]
    wrongs = {}
    for n in P:
        if n == best:
            continue
        wrongs[n] = "That student is the heaviest, but power also depends on the time taken." if n == heaviest else ("That student is the fastest, but power also depends on mass." if n == fastest else "Work out m g h ÷ t for each student.")
    table = md_table(["student", "mass / kg", "time to climb 4.0 m / s"], [[n, m, fmt(t)] for n, m, t in rows])
    return mkt(rng, best, wrongs, f"Four students run up the same flight of stairs of height 4.0 m.\n\n{table}\n\nWhich student develops the greatest power?",
               "P = m g h ÷ t", [", ".join(f"{n}: {fmt(P[n])} W" for n, _, _ in rows), f"greatest: **{best}**"],
               ["Power = work ÷ time.", "Work = m g h, and h is the same.", "Compare m ÷ t."])


@template("c6x_power_efficiency_heater", chapter=6, level=4, lo="6f")
def power_efficiency_heater(rng):
    P = nice(rng, 1000, 1500, 2000, 2500)
    t = nice(rng, 60, 120, 180)
    Eu = P * t * nice(rng, 0.7, 0.8, 0.9)
    eff = Eu / (P * t) * 100
    return mk(rng, eff, [(Eu / P * 100, "The input energy is P × t."), (P * t / Eu * 100, "Efficiency = useful ÷ input."), (100 - eff, "That is the percentage wasted.")],
              "%", f"An electric kettle is tested.\n\n{md_table(['quantity', 'value'], [['power rating', f'{P} W'], ['time switched on', f'{t} s'], ['energy gained by the water', f'{fmt(Eu)} J']])}\n\nWhat is the efficiency of the kettle?",
              "input = P t; efficiency = useful ÷ input × 100%", [f"input = {P} × {t} = {P * t} J", f"efficiency = {fmt(Eu)} ÷ {P * t} × 100% = **{fmt(eff)}%**"],
              ["Find the input energy from the power and time.", "The useful output is the energy gained by the water.", "Divide and × 100."])


# ================================================================== L5
@template("c6x_ke_stopping_compare", chapter=6, level=5, lo="6b")
def ke_stopping_compare(rng):
    v1 = nice(rng, 10, 15, 20)
    k = nice(rng, 1.5, 2.0, 3.0)
    d1 = nice(rng, 12, 15, 20)
    d2 = d1 * k * k
    return mk(rng, d2, [(d1 * k, "Braking distance ∝ KE ∝ v², so it scales with k², not k."), (d1 + k, "Use the ratio of the kinetic energies."), (d1 * 2 * k, "Square the speed factor.")],
              "m", f"A car braking with the same force stops in **{d1} m** from **{v1} m/s**.\n\n{md_table(['speed / m/s', 'braking distance / m'], [[v1, d1], [fmt(v1 * k), '?']])}\n\nWhat is its braking distance from the higher speed?",
              "F d = ½ m v² with F constant → d ∝ v²", [f"speed factor = {fmt(k)}", f"d = {d1} × {fmt(k)}² = **{fmt(d2)} m**"],
              ["The brakes remove all the KE.", "F d = ½ m v², with the same F.", "d ∝ v²."])


@template("c6x_bungee_speed", chapter=6, level=5, lo="6b")
def bungee_speed(rng):
    m = nice(rng, 60, 70, 80)
    L = nice(rng, 15, 20, 25)
    loss = nice(rng, 0.1, 0.15, 0.2)
    ke = m * G * L * (1 - loss)
    v = math.sqrt(2 * ke / m)
    return mk(rng, v, [(math.sqrt(2 * G * L), "Some energy is lost to air resistance; reduce the KE first."), (math.sqrt(2 * G * L * loss), "Only a FRACTION is lost; most becomes KE."), (2 * ke / m, "Take the square root.")],
              "m/s", f"A bungee jumper falls freely before the cord begins to stretch.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} kg'], ['distance fallen before the cord stretches', f'{L} m'], ['fraction of GPE lost to air resistance', f'{loss:g}']])}\n\nWhat is the jumper's speed when the cord starts to stretch? (g = 10 N/kg)",
              "KE = (1 − fraction lost) × m g h; v = √(2 KE ÷ m)", [f"GPE lost = {m} × 10 × {L} = {m * G * L} J", f"KE = {1 - loss:g} × {m * G * L} = {fmt(ke)} J", f"v = √(2 × {fmt(ke)} ÷ {m}) = **{fmt(v)} m/s**"],
              ["Find the GPE lost.", "Take away the fraction lost to air resistance.", "Find v from KE."])


@template("c6x_ramp_height_reached", chapter=6, level=5, lo="6c")
def ramp_height_reached(rng):
    m = nice(rng, 2, 4, 5)
    v = nice(rng, 6, 8, 10)
    loss = nice(rng, 20, 30, 40)
    h = (0.5 * m * v * v - loss) / (m * G)
    return mk(rng, h, [(v * v / (2 * G), "Some KE is lost to friction; subtract it first."), ((0.5 * m * v * v + loss) / (m * G), "Friction REDUCES the height reached."), ((0.5 * m * v * v - loss) / m, "Divide by m g, not m.")],
              "m", f"A trolley of mass **{m} kg** moving at **{v} m/s** runs up a rough ramp and stops. **{loss} J** of energy is lost to friction on the way up (Fig. 1). What vertical height does it reach? (g = 10 N/kg)",
              "KE = m g h + energy lost → h = (KE − loss) ÷ (m g)", [f"KE = ½ × {m} × {v}² = {fmt(0.5 * m * v * v)} J", f"m g h = {fmt(0.5 * m * v * v)} − {loss} = {fmt(0.5 * m * v * v - loss)} J", f"h = **{fmt(h)} m**"],
              ["Find the starting KE.", "Some goes to friction, the rest to GPE.", "h = GPE ÷ (m g)."], figure=sketches.slope_sketch("h = ?", None, f"{m} kg, {v} m/s"))


@template("c6x_ball_bounce_loss", chapter=6, level=5, lo="6c")
def ball_bounce_loss(rng):
    m = nice(rng, 0.05, 0.1, 0.2)
    h1 = nice(rng, 2.0, 2.5, 3.0)
    h2 = h1 * nice(rng, 0.5, 0.6, 0.75)
    pct = (h1 - h2) / h1 * 100
    return mk(rng, pct, [(h2 / h1 * 100, "That is the percentage KEPT, not lost."), (m * G * (h1 - h2), "That is the energy lost in J; the question asks for the percentage."), ((h1 - h2) / h2 * 100, "Divide by the ORIGINAL GPE (height h₁).")],
              "%", f"A ball is dropped and bounces.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['height dropped from', f'{fmt(h1)} m'], ['height of first bounce', f'{fmt(h2)} m']])}\n\nWhat percentage of its original energy is lost in the bounce?",
              "GPE ∝ h; % lost = (h₁ − h₂) ÷ h₁ × 100%", [f"lost = {fmt(h1)} − {fmt(h2)} = {fmt(h1 - h2)} m of height", f"% = {fmt(h1 - h2)} ÷ {fmt(h1)} × 100% = **{fmt(pct)}%**"],
              ["Compare the GPE at the two heights.", "m and g are the same, so compare heights.", "% lost = loss ÷ original × 100."])


@template("c6x_power_car_resistive", chapter=6, level=5, lo="6e")
def power_car_resistive(rng):
    F = nice(rng, 400, 500, 600, 800)
    v = nice(rng, 15, 20, 25, 30)
    return mk(rng, F * v / 1000, [(F * v, "That is in W; the answer is in kW."), (F / v / 1000, "P = F × v."), (0.5 * F * v / 1000, "No ½: P = F v.")],
              "kW", f"A car travels at a steady speed against air resistance and friction.\n\n{md_table(['quantity', 'value'], [['total resistive force', f'{F} N'], ['speed', f'{v} m/s']])}\n\nWhat useful power must the engine provide, in kW?",
              "at steady speed, driving force = resistive force; P = F v", [f"P = {F} × {v} = {F * v} W", f"= **{fmt(F * v / 1000)} kW**"],
              ["At a steady speed, the driving force equals the resistance.", "Power = work ÷ time = F × d ÷ t = F × v.", "Convert to kW."])


@template("c6x_power_station_efficiency", chapter=6, level=5, lo="6f")
def power_station_efficiency(rng):
    Pin = nice(rng, 1500, 2000, 2500)
    eff = nice(rng, 35, 38, 40)
    Pout = Pin * eff / 100
    waste = Pin - Pout
    return mk(rng, waste, [(Pout, "That is the useful electrical output; the question asks for the wasted power."), (Pin, "Subtract the useful output."), (Pin * (100 + eff) / 100, "Wasted = input − useful.")],
              "MW", f"A fossil-fuel power station is **{eff}%** efficient.\n\n{md_table(['quantity', 'value'], [['power input from fuel', f'{Pin} MW'], ['efficiency', f'{eff}%']])}\n\nAt what rate is energy wasted (mainly as thermal energy to the surroundings)?",
              "useful = eff × input; wasted = input − useful", [f"useful = {eff / 100:g} × {Pin} = {fmt(Pout)} MW", f"wasted = {Pin} − {fmt(Pout)} = **{fmt(waste)} MW**"],
              ["Find the useful output first.", "Energy is conserved.", "Wasted = input − useful."])


@template("c6x_pump_efficiency_water", chapter=6, level=5, lo="6f")
def pump_efficiency_water(rng):
    m = nice(rng, 50, 60, 100)
    h = nice(rng, 5, 8, 10)
    t = nice(rng, 10, 20, 30)
    Pin = nice(rng, 500, 600, 800)
    eff = m * G * h / t / Pin * 100
    if eff >= 100:
        Pin = 2000
        eff = m * G * h / t / Pin * 100
    return mk(rng, eff, [(m * G * h / Pin * 100, "Use the useful POWER (energy ÷ time), not the energy."), (Pin * t / (m * G * h) * 100, "Efficiency = useful ÷ input."), (m * h / t / Pin * 100, "GPE = m g h: include g.")],
              "%", f"An electric pump lifts water from a well.\n\n{md_table(['quantity', 'value'], [['mass of water lifted', f'{m} kg'], ['height lifted', f'{h} m'], ['time taken', f'{t} s'], ['electrical power input', f'{Pin} W']])}\n\nWhat is the efficiency of the pump? (g = 10 N/kg)",
              "useful power = m g h ÷ t; efficiency = useful power ÷ input power × 100%", [f"useful power = {m} × 10 × {h} ÷ {t} = {fmt(m * G * h / t)} W", f"efficiency = {fmt(m * G * h / t)} ÷ {Pin} × 100% = **{fmt(eff)}%**"],
              ["Find the useful power: GPE gained ÷ time.", "Compare with the input power.", "× 100 for a percentage."])


@template("c6x_work_climb_slope", chapter=6, level=5, lo="6d")
def work_climb_slope(rng):
    W = nice(rng, 600, 700, 800)
    L = nice(rng, 100, 200, 250)
    rise = L / 50
    f = nice(rng, 20, 30, 40)
    work = W * rise + f * L
    return mk(rng, work, [(W * L, "Work against gravity uses the VERTICAL rise, not the distance along the road."), (W * rise, "Include the work against friction along the road."), (f * L, "Include the work against gravity too.")],
              "J", f"A cyclist rides up a road that rises 1 m vertically for every 50 m along the road.\n\n{md_table(['quantity', 'value'], [['weight of cyclist and bicycle', f'{W} N'], ['distance along the road', f'{L} m'], ['average resistive force', f'{f} N']])}\n\nHow much work does the cyclist do, at a steady speed?",
              "work = W × rise + resistive force × distance along road", [f"rise = {L} ÷ 50 = {fmt(rise)} m", f"against gravity = {W} × {fmt(rise)} = {fmt(W * rise)} J; against resistance = {f} × {L} = {f * L} J", f"total = **{fmt(work)} J**"],
              ["Work against gravity uses the vertical height.", "Work against resistance uses the distance along the road.", "Add the two."])


@template("c6x_power_lift_people", chapter=6, level=5, lo="6e")
def power_lift_people(rng):
    n = nice(rng, 8, 10, 12)
    m = nice(rng, 60, 70, 75)
    h = nice(rng, 20, 30, 40)
    t = nice(rng, 20, 25, 30)
    P = n * m * G * h / t
    return mk(rng, P / 1000, [(m * G * h / t / 1000, "Multiply by the number of people."), (n * m * h / t / 1000, "Include g = 10 N/kg."), (P, "That is in W; the answer is in kW.")],
              "kW", f"A lift carries people to an upper floor.\n\n{md_table(['quantity', 'value'], [['number of people', n], ['average mass per person', f'{m} kg'], ['height raised', f'{h} m'], ['time taken', f'{t} s']])}\n\nWhat useful power does the lift motor provide, in kW? (Ignore the mass of the lift car.)",
              "P = n m g h ÷ t", [f"work = {n} × {m} × 10 × {h} = {fmt(n * m * G * h)} J", f"P = {fmt(n * m * G * h)} ÷ {t} = {fmt(P)} W = **{fmt(P / 1000)} kW**"],
              ["Find the total mass lifted.", "Work = m g h.", "P = W ÷ t, then convert to kW."])
