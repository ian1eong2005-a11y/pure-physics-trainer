"""Chapter 18 Electromagnetism (6091) bank extension: rule-based, data-reading and proportionality templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: wire between magnet poles on a balance, relays and
circuit breakers, electromagnets lifting pins, simple d.c. motors and commutators, electron beams; school papers 2024-2025)."""
from .. import figs, figs3
from .base import fmt, md_table, mk, mkt, nice, template

DIRS = ["upwards", "downwards", "to the left", "to the right"]


def flip(d):
    return {"upwards": "downwards", "downwards": "upwards", "to the left": "to the right", "to the right": "to the left"}[d]


# ================================================================== L1
@template("c18x_grip_rule_table", chapter=18, level=1, lo="18a")
def grip_rule_table(rng):
    current = rng.choice(["upwards (wire vertical)", "downwards (wire vertical)"])
    ans = "anticlockwise" if current.startswith("upwards") else "clockwise"
    wrongs = {("clockwise" if ans == "anticlockwise" else "anticlockwise"): "Use the right-hand grip rule: thumb along the current.",
              "radially outwards": "The field lines are circles round the wire.", "parallel to the wire": "The field goes round the wire."}
    return mkt(rng, ans, wrongs, f"{md_table(['quantity', 'value'], [['current in a vertical wire', current], ['viewed from', 'above']])}\n\nViewed from above, in which direction do the magnetic field lines circle the wire?",
               "right-hand grip: thumb along current, fingers give field", [f"current {current.split(' ')[0]}: fingers curl **{ans}** seen from above"],
               ["Point your right thumb along the current.", "Your fingers curl round the wire.", "Look from above."])


@template("c18x_wire_field_fig", chapter=18, level=1, lo="18a")
def wire_field_fig(rng):
    current = rng.choice(["out", "into"])
    ans = "it reverses"
    wrongs = {"it stays the same": "Reversing the current reverses the field direction.", "it becomes radial": "The lines are still circles.", "it disappears": "A current always has a field."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the field around a wire carrying a current {current} of the page. The current is reversed. What happens to the direction of the field lines?".replace("into of", "into"),
               "reversing the current reverses the field", ["**it reverses**"],
               ["Does the field depend on current direction?", "Yes.", "Reverse current → reverse field."], figure=figs3.wire_field(current))


@template("c18x_electromagnet_turns_table", chapter=18, level=1, lo="18b")
def electromagnet_turns_table(rng):
    rows = [(20, nice(rng, 4, 5)), (40, nice(rng, 9, 10)), (60, nice(rng, 13, 15)), (80, nice(rng, 18, 20))]
    k = rng.randrange(4)
    return mk(rng, rows[k][1], [(rows[(k + 1) % 4][1], "Read the row for this number of turns."), (rows[k][0], "That is the number of turns."), (rows[k][1] + 3, "Read the table.")],
              "paper clips", f"An electromagnet is tested with different numbers of turns (same current).\n\n{md_table(['number of turns', 'paper clips lifted'], rows)}\n\nHow many clips are lifted with **{rows[k][0]}** turns?",
              "read the table: more turns → stronger", [f"**{rows[k][1]} clips**"],
              ["Find the row.", "Read across.", "More turns, stronger electromagnet."], dp=0)


@template("c18x_electromagnet_strongest_pick", chapter=18, level=1, lo="18b")
def electromagnet_strongest_pick(rng):
    rows = [("A", 50, 1.0, "iron"), ("B", 100, 1.0, "iron"), ("C", 100, 2.0, "iron"), ("D", 100, 2.0, "none")]
    rng.shuffle(rows)
    ans = "C"
    wrongs = {n: ("No core makes it much weaker." if c == "none" else "More turns and more current both help.") for n, t, i, c in rows if n != ans}
    table = md_table(["electromagnet", "turns", "current / A", "core"], [[n, t, fmt(i), c] for n, t, i, c in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich electromagnet is strongest?",
               "strength increases with turns, current and an iron core", ["most turns, most current, iron core → **C**"],
               ["What makes an electromagnet stronger?", "Turns, current, iron core.", "Find the one with all three."])


@template("c18x_relay_switch", chapter=18, level=1, lo="18b")
def relay_switch(rng):
    I_coil = nice(rng, 0.05, 0.1)
    I_motor = nice(rng, 5, 10, 20)
    return mk(rng, I_motor / I_coil, [(I_coil / I_motor, "The relay lets a SMALL current switch a LARGE one: motor ÷ coil."), (I_motor - I_coil, "Find the ratio."), (I_motor, "Divide by the coil current.")],
              "times", f"A relay uses a small current in its coil to switch on a large current to a motor.\n\n{md_table(['circuit', 'current / A'], [['relay coil', fmt(I_coil)], ['motor', I_motor]])}\n\nHow many times larger is the motor current?",
              "ratio = I_motor ÷ I_coil", [f"{I_motor} ÷ {fmt(I_coil)} = **{fmt(I_motor / I_coil)}**"],
              ["A relay uses an electromagnet.", "Small current controls a large one.", "Divide."])


@template("c18x_force_scale_current", chapter=18, level=1, lo="18c")
def force_scale_current(rng):
    F1 = nice(rng, 0.02, 0.03, 0.05)
    k = nice(rng, 2, 3)
    return mk(rng, F1 * k, [(F1 / k, "A LARGER current gives a LARGER force."), (F1 * k * k, "F ∝ I, not I²."), (F1, "The force depends on the current.")],
              "N", f"The force on a wire in a magnetic field is proportional to the current.\n\n{md_table(['current', 'force / N'], [['I', fmt(F1)], [f'{k}I', '?']])}\n\nWhat is the new force?",
              "F ∝ I", [f"F = {fmt(F1)} × {k} = **{fmt(F1 * k)} N**"],
              ["F ∝ I.", f"The current is × {k}.", "Multiply."])


@template("c18x_force_reverse_one", chapter=18, level=1, lo="18c")
def force_reverse_one(rng):
    d = rng.choice(DIRS)
    change = rng.choice(["the current is reversed", "the magnetic field is reversed"])
    ans = flip(d)
    wrongs = {d: "Reversing one of them reverses the force.", ("to the left" if d in ("upwards", "downwards") else "upwards"): "The force reverses; it does not turn through 90°.", "there is no force": "There is still a force."}
    return mkt(rng, ans, wrongs, f"{md_table(['', 'force on wire'], [['before', d], ['after: ' + change, '?']])}\n\nWhat is the direction of the force now?",
               "reversing current OR field reverses the force", [f"**{ans}**"],
               ["What does reversing one quantity do?", "It reverses the force.", "Opposite direction."])


@template("c18x_force_reverse_both", chapter=18, level=1, lo="18c")
def force_reverse_both(rng):
    d = rng.choice(DIRS)
    wrongs = {flip(d): "Reversing BOTH current and field reverses the force twice, so it is unchanged.", ("to the right" if d in ("upwards", "downwards") else "downwards"): "The force does not turn sideways.", "there is no force": "There is still a force."}
    return mkt(rng, d, wrongs, f"{md_table(['', 'force on wire'], [['before', d], ['after: both current and field reversed', '?']])}\n\nWhat is the direction of the force now?",
               "reversing both: force direction unchanged", [f"**{d}**"],
               ["Reverse one → force reverses.", "Reverse both → reverses twice.", "Same as before."])


@template("c18x_lhr_fig_simple", chapter=18, level=1, lo="18d")
def lhr_fig_simple(rng):
    field = rng.choice(["right", "left"])
    current = rng.choice(["into", "out"])
    f = figs3.lhr_force(field, current)
    ans = "upwards" if f == "up" else "downwards"
    wrongs = {flip(ans): "Check Fleming's LEFT-hand rule: First finger Field, seCond Current, thuMb Motion.", f"to the {field}": "That is the field direction.", "there is no force": "There is a force."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a wire carrying a current **{current}** the page between magnet poles. Using Fleming's left-hand rule, in which direction is the force on the wire?",
               "LHR: First finger Field (N→S), seCond finger Current, thuMb Motion", [f"thumb points **{ans}**"],
               ["Use your LEFT hand.", "Field N → S; current as shown.", "Thumb = force."], figure=figs3.flemings_lhr(field=field, current=current))


# ================================================================== L2
@template("c18x_compass_near_wire", chapter=18, level=2, lo="18a")
def compass_near_wire(rng):
    current = rng.choice(["out", "into"])
    pos = rng.choice(["above", "below"])
    circ = "anticlockwise" if current == "out" else "clockwise"
    if circ == "anticlockwise":
        ans = "to the left" if pos == "above" else "to the right"
    else:
        ans = "to the right" if pos == "above" else "to the left"
    wrongs = {flip(ans): "Use the right-hand grip rule to find the direction of the circular field at that point.", "towards the wire": "The field is tangential, not towards the wire.", "away from the wire": "The field circles the wire."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a wire carrying current {current} of the page. A plotting compass is placed just **{pos}** the wire. In which direction does its N pole point?".replace("into of", "into"),
               "right-hand grip gives the circular field direction; compass points along it", [f"field is {circ}; {pos} the wire it points **{ans}**"],
               ["Find the direction of the circles.", "Right-hand grip rule.", "The compass follows the circle at that point."], figure=figs3.wire_field(current))


@template("c18x_field_distance_wire", chapter=18, level=2, lo="18a")
def field_distance_wire(rng):
    B1 = nice(rng, 40, 60, 80)
    k = nice(rng, 2, 4)
    return mk(rng, B1 / k, [(B1 * k, "The field is WEAKER further from the wire."), (B1 / k ** 2, "B ∝ 1/r here, not 1/r²."), (B1, "The field depends on distance.")],
              "µT", f"The field strength around a long straight wire is inversely proportional to the distance from it.\n\n{md_table(['distance from wire', 'field strength / µT'], [['r', B1], [f'{k}r', '?']])}\n\nWhat is the field strength at the larger distance?",
              "B ∝ 1/r", [f"B = {B1} ÷ {k} = **{fmt(B1 / k)} µT**"],
              ["How does the field change with distance?", "B ∝ 1/r.", f"÷ {k}."])


@template("c18x_electromagnet_current_table", chapter=18, level=2, lo="18b")
def electromagnet_current_table(rng):
    rows = [(0.5, nice(rng, 5, 6)), (1.0, nice(rng, 11, 12)), (1.5, nice(rng, 16, 18)), (2.0, nice(rng, 22, 24))]
    return mk(rng, rows[3][1] - rows[0][1], [(rows[3][1], "Find the INCREASE."), (rows[0][1], "That is at 0.5 A."), (rows[3][1] + rows[0][1], "Subtract.")],
              "pins", f"{md_table(['current / A', 'pins lifted'], [[fmt(i), p] for i, p in rows])}\n\nHow many more pins are lifted at 2.0 A than at 0.5 A?",
              "difference of readings", [f"{rows[3][1]} − {rows[0][1]} = **{rows[3][1] - rows[0][1]} pins**"],
              ["Read both values.", "Subtract.", "More current → stronger."], dp=0)


@template("c18x_breaker_trip_current", chapter=18, level=2, lo="18b")
def breaker_trip_current(rng):
    trip = nice(rng, 10, 16, 20)
    Ps = [nice(rng, 1500, 2000), nice(rng, 1000, 1200), nice(rng, 500, 800)]
    I = sum(Ps) / 230
    ans = "yes" if I > trip else "no"
    wrongs = {("no" if ans == "yes" else "yes"): f"Total current = {sum(Ps)} ÷ 230 = {fmt(I, sf=3)} A; compare with {trip} A.", "only if the appliances are faulty": "An overload alone can trip it.",
              "breakers never trip": "They trip when the current exceeds their rating."}
    table = md_table(["appliance", "power / W"], [[i + 1, p] for i, p in enumerate(Ps)])
    return mkt(rng, ans, wrongs, f"An electromagnetic circuit breaker trips when the current exceeds **{trip} A**. These 230 V appliances are switched on together:\n\n{table}\n\nDoes the breaker trip?",
               "I = ΣP ÷ V; trips if I > rating", [f"I = {sum(Ps)} ÷ 230 = {fmt(I, sf=3)} A → **{ans}**"],
               ["Add the powers.", "Find the current.", "Compare with the trip current."])


@template("c18x_force_balance_reading", chapter=18, level=2, lo="18c")
def force_balance_reading(rng):
    m1 = nice(rng, 120.0, 150.0, 200.0)
    dm = nice(rng, 1.2, 2.0, 3.5)
    F = dm / 1000 * 10
    return mk(rng, F * 1000, [(F, "That is in N; the answer is in mN."), (dm * 10, "Convert g to kg first."), (m1 / 1000 * 10 * 1000, "Use the CHANGE in reading.")],
              "mN", f"A magnet sits on a top-pan balance with a wire held between its poles. When a current flows in the wire, the balance reading changes.\n\n{md_table(['current', 'balance reading / g'], [['off', fmt(m1)], ['on', fmt(m1 + dm)]])}\n\nWhat is the size of the force between the wire and the magnet, in mN? (g = 10 N/kg)",
              "F = Δm × g", [f"Δm = {fmt(dm)} g = {fmt(dm / 1000)} kg", f"F = {fmt(dm / 1000)} × 10 = **{fmt(F * 1000)} mN**"],
              ["Find the change in reading.", "Convert to kg.", "F = m g."])


@template("c18x_lhr_fig_field_left", chapter=18, level=2, lo="18d")
def lhr_fig_field_left(rng):
    field = rng.choice(["left", "right"])
    current = rng.choice(["into", "out"])
    f = figs3.lhr_force(field, current)
    ans = "upwards" if f == "up" else "downwards"
    wrongs = {flip(ans): "Using the RIGHT hand gives the opposite answer: use the LEFT hand.", "along the wire": "The force is at right angles to the wire.", f"to the {field}": "That is the field direction."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a wire between magnet poles with the current **{current}** the page. In which direction does the wire move?",
               "Fleming's left-hand rule", [f"field to the {field}, current {current} → **{ans}**"],
               ["First finger along the field (N → S).", "Second finger along the current.", "Thumb gives the motion."], figure=figs3.flemings_lhr(field=field, current=current))


@template("c18x_lhr_find_current", chapter=18, level=2, lo="18d")
def lhr_find_current(rng):
    field = rng.choice(["right", "left"])
    force = rng.choice(["up", "down"])
    cur = next(c for c in ("into", "out") if figs3.lhr_force(field, c) == force)
    ans = f"{cur} the page"
    wrongs = {("out of the page" if cur == "into" else "into the page"): "Check Fleming's left-hand rule again.", f"to the {field}": "The current is along the wire, into or out of the page.", "there must be no current": "A force shows there is a current."}
    return mkt(rng, ans, wrongs, f"{md_table(['quantity', 'direction'], [['magnetic field (N → S)', f'to the {field}'], ['force on wire', 'upwards' if force == 'up' else 'downwards']])}\n\nThe wire runs into/out of the page. Which way does the current flow?",
               "rearrange Fleming's left-hand rule", [f"**{ans}**"],
               ["Point the first finger along the field.", "Point the thumb along the force.", "The second finger gives the current."])


@template("c18x_motor_speed_current", chapter=18, level=2, lo="18e")
def motor_speed_current(rng):
    rows = [(0.5, nice(rng, 300, 350)), (1.0, nice(rng, 600, 700)), (1.5, nice(rng, 900, 1000)), (2.0, nice(rng, 1200, 1350))]
    k = rng.randrange(4)
    return mk(rng, rows[k][1], [(rows[(k + 1) % 4][1], "Read the row for this current."), (rows[k][0] * 100, "Read the speed from the table."), (rows[k][1] / 2, "Read the value directly.")],
              "rev/min", f"A model d.c. motor is run at different currents.\n\n{md_table(['current / A', 'speed / rev/min'], [[fmt(i), s] for i, s in rows])}\n\nWhat is its speed at **{fmt(rows[k][0])} A**?",
              "read the table: more current → faster", [f"**{rows[k][1]} rev/min**"],
              ["Find the current.", "Read across.", "More current, larger turning effect."], dp=0)


@template("c18x_motor_factor_choice", chapter=18, level=2, lo="18e")
def motor_factor_choice(rng):
    rows = [("A", 50, 1.0, "weak"), ("B", 100, 1.0, "weak"), ("C", 100, 2.0, "strong"), ("D", 50, 2.0, "weak")]
    rng.shuffle(rows)
    ans = "C"
    wrongs = {n: "A larger turning effect needs more turns, more current and a stronger magnet." for n, t, i, m in rows if n != ans}
    table = md_table(["motor", "turns on coil", "current / A", "magnet"], [[n, t, fmt(i), m] for n, t, i, m in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich motor has the largest turning effect on its coil?",
               "turning effect increases with turns, current and field strength", ["**C** has the most of each"],
               ["What increases the turning effect?", "Turns, current, magnet strength.", "Pick the largest of all three."])


# ================================================================== L3
@template("c18x_solenoid_end_pole", chapter=18, level=3, lo="18a")
def solenoid_end_pole(rng):
    view = rng.choice(["clockwise", "anticlockwise"])
    ans = "S" if view == "clockwise" else "N"
    wrongs = {("N" if ans == "S" else "S"): "Use the end rule: clockwise current seen from an end gives a S pole.", "no pole": "A solenoid with current has poles.", "both poles at that end": "Each end has one pole."}
    return mkt(rng, ans, wrongs, f"{md_table(['view of solenoid end', 'current direction seen'], [['end X', view]])}\n\nWhat pole is at end X?",
               "clockwise → S; anticlockwise → N (or right-hand grip on the coil)", [f"{view} → **{ans}**"],
               ["Use the right-hand grip rule on the coil.", "Or the end rule.", "Clockwise S, anticlockwise N."])


@template("c18x_solenoid_field_strength", chapter=18, level=3, lo="18a")
def solenoid_field_strength(rng):
    B1 = nice(rng, 2.0, 3.0, 4.0)
    kN, kI = nice(rng, 2, 3), nice(rng, 2)
    return mk(rng, B1 * kN * kI, [(B1 * kN, "The current also changes: multiply by both factors."), (B1 * kI, "Multiply by the turns factor too."), (B1 * (kN + kI), "Multiply the factors, do not add.")],
              "mT", f"The field inside a long solenoid is proportional to the number of turns per metre and to the current.\n\n{md_table(['change', 'factor'], [['turns per metre', f'× {kN}'], ['current', f'× {kI}']])}\n\nThe original field was **{fmt(B1)} mT**. What is the new field?",
              "B ∝ n I", [f"B = {fmt(B1)} × {kN} × {kI} = **{fmt(B1 * kN * kI)} mT**"],
              ["B ∝ turns per metre.", "B ∝ current.", "Multiply both factors."])


@template("c18x_bell_frequency", chapter=18, level=3, lo="18b")
def bell_frequency(rng):
    n = nice(rng, 30, 40, 50, 60)
    t = nice(rng, 2, 3, 5)
    return mk(rng, n / t, [(n * t, "Frequency = number ÷ time."), (t / n, "Number goes on top."), (n, "Divide by the time.")],
              "Hz", f"In an electric bell, an electromagnet pulls the hammer, breaking the circuit, and a spring returns it.\n\n{md_table(['quantity', 'value'], [['number of strikes', n], ['time', f'{t} s']])}\n\nAt what frequency does the hammer strike?",
              "f = number ÷ time", [f"f = {n} ÷ {t} = **{fmt(n / t)} Hz**"],
              ["Count strikes per second.", "Divide.", "Unit Hz."])


@template("c18x_relay_coil_current", chapter=18, level=3, lo="18b")
def relay_coil_current(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    R = nice(rng, 60, 100, 120, 200)
    I = V / R * 1000
    return mk(rng, I, [(V / R, "Convert A to mA."), (V * R, "I = V ÷ R."), (I / 10, "Check the conversion.")],
              "mA", f"A relay coil is connected to a battery.\n\n{md_table(['quantity', 'value'], [['battery p.d.', f'{fmt(V)} V'], ['coil resistance', f'{R} Ω']])}\n\nWhat current flows in the coil, in mA?",
              "I = V ÷ R", [f"I = {fmt(V)} ÷ {R} = {fmt(V / R, sf=3)} A = **{fmt(I)} mA**"],
              ["Use I = V ÷ R.", "Convert to mA.", "A small current works the relay."])


@template("c18x_force_length_field", chapter=18, level=3, lo="18c")
def force_length_field(rng):
    F1 = nice(rng, 0.04, 0.06, 0.08)
    kL, kB = nice(rng, 2, 3), nice(rng, 2)
    return mk(rng, F1 * kL / kB, [(F1 * kL * kB, "The field is WEAKER: divide by its factor."), (F1 * kL, "Include the change in field."), (F1 / (kL * kB), "A longer wire in the field gives MORE force.")],
              "N", f"The force on a wire in a magnetic field is proportional to the current, the length in the field, and the field strength.\n\n{md_table(['change', 'factor'], [['length of wire in field', f'× {kL}'], ['field strength', f'÷ {kB}']])}\n\nThe original force was **{fmt(F1)} N** (same current). What is the new force?",
              "F ∝ B I L", [f"F = {fmt(F1)} × {kL} ÷ {kB} = **{fmt(F1 * kL / kB)} N**"],
              ["F ∝ L and F ∝ B.", "Apply both factors.", "Multiply and divide."])


@template("c18x_force_parallel_wire", chapter=18, level=3, lo="18c")
def force_parallel_wire(rng):
    F90 = nice(rng, 0.05, 0.1, 0.2)
    return mkt(rng, "zero", {f"{fmt(F90)} N": "That is the force at right angles; parallel to the field there is no force.", f"{fmt(F90 * 2)} N": "A wire parallel to the field feels no force.",
                                 f"{fmt(F90 / 2)} N": "The force is zero, not halved."},
                   f"A wire experiences **{fmt(F90)} N** when at right angles to a magnetic field.\n\n{md_table(['orientation', 'force / N'], [['at right angles to field', fmt(F90)], ['parallel to field', '?']])}\n\nWhat is the force when the wire is parallel to the field?",
                   "no force when current is parallel to the field", ["parallel → **zero** force"],
                   ["When is the force largest?", "At right angles.", "Parallel → no force."])


@template("c18x_lhr_vertical_field", chapter=18, level=3, lo="18d")
def lhr_vertical_field(rng):
    field = rng.choice(["downwards", "upwards"])
    current = rng.choice(["to the right", "to the left"])
    table = {("downwards", "to the right"): "out of the page", ("downwards", "to the left"): "into the page", ("upwards", "to the right"): "into the page", ("upwards", "to the left"): "out of the page"}
    ans = table[(field, current)]
    wrongs = {("into the page" if ans == "out of the page" else "out of the page"): "Use the LEFT hand: first finger field, second finger current, thumb force.", field: "That is the field direction.", current: "That is the current direction."}
    return mkt(rng, ans, wrongs, f"{md_table(['quantity', 'direction'], [['magnetic field', field], ['current in wire', current]])}\n\nIn which direction is the force on the wire?",
               "Fleming's left-hand rule in 3D", [f"**{ans}**"],
               ["First finger: field.", "Second finger: current.", "Thumb: force."])


@template("c18x_lhr_electron_flow", chapter=18, level=3, lo="18d")
def lhr_electron_flow(rng):
    field = rng.choice(["right", "left"])
    e_dir = rng.choice(["into", "out"])
    conv = "out" if e_dir == "into" else "into"
    f = figs3.lhr_force(field, conv)
    ans = "upwards" if f == "up" else "downwards"
    wrongs = {flip(ans): "Electrons flow OPPOSITE to conventional current: point the second finger the other way.", f"to the {field}": "That is the field.", "no force": "Moving charges in a field feel a force."}
    return mkt(rng, ans, wrongs, f"A wire lies between magnet poles.\n\n{md_table(['quantity', 'direction'], [['magnetic field (N → S)', f'to the {field}'], ['flow of electrons in the wire', f'{e_dir} the page']])}\n\nIn which direction is the force on the wire?",
               "conventional current is opposite to electron flow; then use the LHR", [f"conventional current {conv} the page → **{ans}**"],
               ["Which way is conventional current?", "Opposite to the electrons.", "Then use Fleming's left-hand rule."])


@template("c18x_commutator_reversals_rev", chapter=18, level=3, lo="18f")
def commutator_reversals_rev(rng):
    n = nice(rng, 5, 10, 20, 50)
    return mk(rng, 2 * n, [(n, "The current reverses TWICE per revolution."), (4 * n, "Twice per revolution, not four times."), (n / 2, "Multiply by 2.")],
              "reversals", f"The split-ring commutator of a d.c. motor reverses the current in the coil every half turn.\n\n{md_table(['quantity', 'value'], [['revolutions made', n]])}\n\nHow many times does the current in the coil reverse?",
              "2 reversals per revolution", [f"2 × {n} = **{2 * n}**"],
              ["When does the commutator reverse the current?", "Every half turn.", "Twice per revolution."], dp=0)


@template("c18x_commutator_rpm", chapter=18, level=3, lo="18f")
def commutator_rpm(rng):
    rpm = nice(rng, 600, 1200, 1800, 3000)
    rev_s = rpm / 60
    return mk(rng, 2 * rev_s, [(rev_s, "Two reversals per revolution."), (2 * rpm, "Convert rev/min to rev/s first."), (rpm / 30 * 2, "Reversals per second = 2 × rev per second.")],
              "per second", f"A motor turns at **{rpm} rev/min**.\n\n{md_table(['quantity', 'value'], [['speed', f'{rpm} rev/min'], ['reversals per revolution (commutator)', 2]])}\n\nHow many times per second does the commutator reverse the coil current?",
              "rev/s = rpm ÷ 60; reversals/s = 2 × rev/s", [f"{rpm} ÷ 60 = {fmt(rev_s)} rev/s", f"reversals = **{fmt(2 * rev_s)} per second**"],
              ["Convert to revolutions per second.", "Two reversals each turn.", "Multiply."])


# ================================================================== L4
@template("c18x_force_graph_gradient", chapter=18, level=4, lo="18c")
def force_graph_gradient(rng):
    k = nice(rng, 0.02, 0.04, 0.05)
    I = 4.0
    F = k * I
    return mk(rng, F * 1000, [(F, "That is in N; give mN."), (k * 1000, "Read the force at the current asked."), (F * 1000 / 2, "Read at 4.0 A.")],
              "mN", f"Fig. 1 shows how the force on a wire in a magnetic field varies with current. What is the force at **4.0 A**, in mN?",
              "read the graph (F ∝ I)", [f"at 4.0 A, F = **{fmt(F * 1000)} mN**"],
              ["Find 4.0 A on the x-axis.", "Read up to the line.", "Convert to mN."], figure=figs.graph([(0, 0), (5, 5 * k * 1000)], 5, 6 * k * 1000, 1, k * 1000, xlabel="current / A", ylabel="force / mN"))


@template("c18x_force_from_two_changes", chapter=18, level=4, lo="18c")
def force_from_two_changes(rng):
    F1 = nice(rng, 0.03, 0.06, 0.09)
    kI = nice(rng, 2, 3)
    return mk(rng, F1 * kI, [(F1 / kI, "More current → more force."), (F1 * kI * kI, "F ∝ I."), (F1 * kI * 2, "The reversed field changes only the DIRECTION, not the size.")],
              "N", f"A wire in a field feels a force of **{fmt(F1)} N**. The current is multiplied by **{kI}** and the field direction is reversed.\n\n{md_table(['change', 'effect'], [['current', f'× {kI}'], ['field', 'reversed']])}\n\nWhat is the SIZE of the new force?",
              "F ∝ I; reversing field changes direction only", [f"F = {fmt(F1)} × {kI} = **{fmt(F1 * kI)} N** (direction reversed)"],
              ["Which change affects the size?", "The current.", "The field reversal only flips the direction."])


@template("c18x_breaker_coil_turns", chapter=18, level=4, lo="18b")
def breaker_coil_turns(rng):
    I_trip = nice(rng, 20, 30)
    k = nice(rng, 2)
    return mk(rng, I_trip / k, [(I_trip * k, "More turns make the electromagnet stronger, so it trips at a LOWER current."), (I_trip, "The turns affect the trip current."), (I_trip / k ** 2, "Strength ∝ N I.")],
              "A", f"An electromagnetic circuit breaker trips when (turns × current) reaches a fixed value.\n\n{md_table(['coil', 'turns', 'trip current / A'], [['original', 'N', I_trip], ['new', f'{k}N', '?']])}\n\nWhat is the new trip current?",
              "N × I constant at tripping", [f"I = {I_trip} ÷ {k} = **{fmt(I_trip / k)} A**"],
              ["What decides the trip point?", "N × I.", "More turns → smaller current."])


@template("c18x_relay_power_ratio", chapter=18, level=4, lo="18b")
def relay_power_ratio(rng):
    V1, I1 = nice(rng, 6.0, 12.0), nice(rng, 0.05, 0.1)
    V2, I2 = 230, nice(rng, 5, 10)
    return mk(rng, V2 * I2 / (V1 * I1), [((V1 * I1) / (V2 * I2), "The switched circuit has the LARGER power."), (V2 * I2, "That is the motor's power; find the ratio."), (I2 / I1, "Include the p.d.s.")],
              "times", f"A relay lets a low-power circuit control a high-power one.\n\n{md_table(['circuit', 'p.d. / V', 'current / A'], [['relay coil', fmt(V1), fmt(I1)], ['heater switched', V2, I2]])}\n\nHow many times greater is the power in the heater circuit?",
              "P = V I for each; ratio", [f"coil: {fmt(V1 * I1)} W; heater: {fmt(V2 * I2)} W", f"ratio = **{fmt(V2 * I2 / (V1 * I1))}**"],
              ["P = V I.", "Find each power.", "Divide."])


@template("c18x_lhr_three_wires", chapter=18, level=4, lo="18d")
def lhr_three_wires(rng):
    field = rng.choice(["right", "left"])
    rows = [("X", "into"), ("Y", "out"), ("Z", rng.choice(["into", "out"]))]
    target = rng.choice(["up", "down"])
    ans_list = sorted(n for n, c in rows if figs3.lhr_force(field, c) == target)
    ans = " and ".join(ans_list) if ans_list else "none"
    opts = ["X only", "Y only", "X and Z", "Y and Z", "X and Y"]
    ans_text = {("X",): "X only", ("Y",): "Y only", ("X", "Z"): "X and Z", ("Y", "Z"): "Y and Z", ("X", "Y"): "X and Y"}.get(tuple(ans_list), ans)
    wrongs = {o: "Apply Fleming's left-hand rule to each wire." for o in opts if o != ans_text}
    table = md_table(["wire", "current"], [[n, f"{c} the page"] for n, c in rows])
    return mkt(rng, ans_text, dict(list(wrongs.items())[:3]), f"Three wires lie between magnet poles; the field points to the **{field}**.\n\n{table}\n\nWhich wires are pushed **{'upwards' if target == 'up' else 'downwards'}**?",
               "apply LHR to each", [", ".join(f"{n}: {'up' if figs3.lhr_force(field, c) == 'up' else 'down'}" for n, c in rows), f"→ **{ans_text}**"],
               ["Use the left-hand rule for each wire.", "Same field, different currents.", "Opposite currents → opposite forces."])


@template("c18x_lhr_beam_direction", chapter=18, level=4, lo="18d")
def lhr_beam_direction(rng):
    field = rng.choice(["into the page", "out of the page"])
    beam = rng.choice(["to the right", "to the left"])
    conv = flip(beam)
    tbl = {("into the page", "to the right"): "upwards", ("into the page", "to the left"): "downwards", ("out of the page", "to the right"): "downwards", ("out of the page", "to the left"): "upwards"}
    ans = tbl[(field, conv)]
    wrongs = {flip(ans): "The electrons are negative: conventional current is OPPOSITE to their motion.", beam: "The force is at right angles to the motion.", field: "That is the field direction."}
    return mkt(rng, ans, wrongs, f"A beam of electrons travels **{beam}** through a magnetic field pointing **{field}**.\n\n{md_table(['quantity', 'direction'], [['electron motion', beam], ['magnetic field', field]])}\n\nIn which direction is the beam deflected?",
               "conventional current opposite to electrons; then LHR", [f"conventional current {conv} → **{ans}**"],
               ["Electrons are negative.", "Conventional current is opposite.", "Then use the left-hand rule."])


@template("c18x_motor_double_turns", chapter=18, level=4, lo="18e")
def motor_double_turns(rng):
    T1 = nice(rng, 0.02, 0.03, 0.05)
    kN, kI = nice(rng, 2, 3), nice(rng, 2)
    return mk(rng, T1 * kN * kI, [(T1 * kN, "Include the current factor too."), (T1 * kI, "Include the turns factor too."), (T1 * (kN + kI), "Multiply the factors.")],
              "N m", f"The turning effect on a motor coil is proportional to the number of turns and to the current.\n\n{md_table(['change', 'factor'], [['turns', f'× {kN}'], ['current', f'× {kI}']])}\n\nThe original turning effect was **{fmt(T1)} N m**. What is the new turning effect?",
              "torque ∝ N I", [f"= {fmt(T1)} × {kN} × {kI} = **{fmt(T1 * kN * kI)} N m**"],
              ["Turning effect ∝ turns.", "∝ current.", "Multiply both."])


@template("c18x_motor_reverse_rotation", chapter=18, level=4, lo="18e")
def motor_reverse_rotation(rng):
    change = rng.choice(["reverse the battery", "reverse the magnet", "reverse both the battery and the magnet", "double the current"])
    ans = {"reverse the battery": "anticlockwise", "reverse the magnet": "anticlockwise", "reverse both the battery and the magnet": "clockwise", "double the current": "clockwise"}[change]
    wrongs = {("clockwise" if ans == "anticlockwise" else "anticlockwise"): "Reversing ONE of current or field reverses the rotation; reversing both does not.", "it stops": "The motor keeps turning.", "it turns back and forth": "The commutator keeps it turning one way."}
    return mkt(rng, ans, wrongs, f"A d.c. motor turns **clockwise** (Fig. 1). The student decides to **{change}**. Which way does it now turn?",
               "reverse one of I or B → reverses rotation", [f"{change} → **{ans}**"],
               ["Which change reverses the force on the coil?", "Reversing current OR field.", "Both reversed: no change."], figure=figs3.motor_diagram())


@template("c18x_commutator_time_half", chapter=18, level=4, lo="18f")
def commutator_time_half(rng):
    rps = nice(rng, 10, 20, 25, 50)
    t = 1 / (2 * rps) * 1000
    return mk(rng, t, [(1 / rps * 1000, "The current reverses every HALF turn."), (t / 1000, "Convert s to ms."), (rps / 2, "Find the time for half a turn.")],
              "ms", f"{md_table(['quantity', 'value'], [['motor speed', f'{rps} revolutions per second']])}\n\nHow long is it between successive reversals of the coil current by the commutator, in ms?",
              "time per revolution = 1 ÷ rps; reversal every half turn", [f"period = 1 ÷ {rps} = {fmt(1 / rps)} s", f"half = {fmt(1 / (2 * rps))} s = **{fmt(t)} ms**"],
              ["Find the time for one revolution.", "Reversals happen every half turn.", "Halve it; convert to ms."])


@template("c18x_brushes_wear", chapter=18, level=4, lo="18f")
def brushes_wear(rng):
    wear = nice(rng, 0.1, 0.2, 0.25)
    length = nice(rng, 8, 10, 12)
    min_len = nice(rng, 3, 4)
    hours = (length - min_len) / wear
    return mk(rng, hours, [(length / wear, "The brush must be replaced before it is used up completely: use (length − minimum)."), ((length - min_len) * wear, "hours = usable length ÷ wear per hour."), (min_len / wear, "Use the usable length.")],
              "h", f"The carbon brushes that touch a motor's commutator slowly wear away.\n\n{md_table(['quantity', 'value'], [['new brush length', f'{length} mm'], ['minimum safe length', f'{min_len} mm'], ['wear rate', f'{fmt(wear)} mm per hour']])}\n\nAfter how many hours of running must the brushes be replaced?",
              "hours = (length − minimum) ÷ wear rate", [f"usable = {length} − {min_len} = {length - min_len} mm", f"time = {length - min_len} ÷ {fmt(wear)} = **{fmt(hours)} h**"],
              ["Find the usable length.", "Divide by the wear rate.", "Answer in hours."])


# ================================================================== L5
@template("c18x_grip_two_wires", chapter=18, level=5, lo="18a")
def grip_two_wires(rng):
    same = rng.choice([True, False])
    ans = "the fields add (strong field)" if not same else "the fields cancel (zero field)"
    wrongs = {("the fields cancel (zero field)" if not same else "the fields add (strong field)"): "Use the right-hand grip rule for each wire at the midpoint.",
              "only one wire has a field": "Both wires produce fields.", "the fields are at right angles": "At the midpoint the fields are along the same line."}
    return mkt(rng, ans, wrongs, f"Two long parallel wires carry equal currents **{'in the same direction' if same else 'in opposite directions'}**.\n\n{md_table(['wire', 'current'], [['A', 'out of the page'], ['B', 'out of the page' if same else 'into the page']])}\n\nAt the point midway between them, what happens to their magnetic fields?",
               "right-hand grip for each: same direction → opposite fields at midpoint", [f"**{ans}**"],
               ["Find each wire's field at the midpoint.", "Use the right-hand grip rule.", "Compare their directions."])


@template("c18x_solenoid_turns_per_metre", chapter=18, level=5, lo="18a")
def solenoid_turns_per_metre(rng):
    N = nice(rng, 200, 300, 500)
    L = nice(rng, 0.2, 0.25, 0.5)
    B1 = nice(rng, 2.0, 3.0)
    L2 = L / 2
    return mk(rng, B1 * 2, [(B1, "Squashing the same turns into half the length doubles the turns per metre."), (B1 / 2, "More turns per metre → STRONGER field."), (B1 * 4, "Turns per metre doubles, so B doubles.")],
              "mT", f"The field inside a solenoid is proportional to the number of turns per metre (same current).\n\n{md_table(['', 'turns', 'length / m', 'field / mT'], [['original', N, fmt(L), fmt(B1)], ['squashed', N, fmt(L2), '?']])}\n\nWhat is the field after the solenoid is squashed to half its length?",
              "B ∝ N ÷ L", [f"turns per metre doubles → B = {fmt(B1)} × 2 = **{fmt(B1 * 2)} mT**"],
              ["Find the turns per metre each time.", "B ∝ turns per metre.", "Scale."])


@template("c18x_breaker_vs_fuse_choice", chapter=18, level=5, lo="18b")
def breaker_vs_fuse_choice(rng):
    rows = [("fuse", f"{nice(rng, 0.1, 0.2, 0.5)} s", "must be replaced"), ("electromagnetic breaker", f"{nice(rng, 0.01, 0.02, 0.03)} s", "reset by switch")]
    wrongs = {"the fuse, because it can be reset": "Fuses must be replaced; breakers are reset.", "the fuse, because it is faster": "The breaker is faster here.",
              "neither, they are identical": "They differ in speed and reuse."}
    table = md_table(["device", "time to cut off", "after tripping"], [list(r) for r in rows])
    return mkt(rng, "the breaker, because it is faster and can be reset", wrongs, f"{table}\n\nWhich device is better for protecting a household circuit, and why?",
               "breaker: faster, resettable", [f"**the breaker** ({rows[1][1]}, resettable)"],
               ["Compare the cut-off times.", "Compare what happens after.", "Choose."])


@template("c18x_electromagnet_core_effect", chapter=18, level=5, lo="18b")
def electromagnet_core_effect(rng):
    no_core = nice(rng, 3, 4)
    k = nice(rng, 5, 8, 10)
    iron = no_core * k
    I_factor = 2
    new = iron * I_factor
    return mk(rng, new, [(iron, "Doubling the current doubles the strength too."), (no_core * I_factor, "Include the iron core's effect."), (no_core * k + I_factor, "Multiply the factors.")],
              "pins", f"An electromagnet is improved in two steps.\n\n{md_table(['electromagnet', 'pins lifted'], [['no core, current I', no_core], ['iron core, current I', iron], ['iron core, current 2I', '?']])}\n\nAssuming the number of pins is proportional to the current, how many pins are lifted in the last case?",
              "pins ∝ current (with the same core)", [f"= {iron} × 2 = **{new} pins**"],
              ["Start from the iron-core value.", "Double the current.", "Double the pins."], dp=0)


@template("c18x_force_balance_current", chapter=18, level=5, lo="18c")
def force_balance_current(rng):
    dm1 = nice(rng, 1.2, 1.5, 2.0)
    I1 = nice(rng, 2.0, 3.0)
    I2 = nice(rng, 5.0, 6.0)
    dm2 = dm1 * I2 / I1
    return mk(rng, dm2, [(dm1 * I1 / I2, "A LARGER current gives a LARGER change."), (dm1, "The change depends on the current."), (dm1 + (I2 - I1), "Use proportion: Δm ∝ I.")],
              "g", f"A wire between the poles of a magnet on a balance changes the reading when current flows.\n\n{md_table(['current / A', 'change in balance reading / g'], [[fmt(I1), fmt(dm1)], [fmt(I2), '?']])}\n\nWhat is the change in reading at the larger current?",
              "F ∝ I so Δm ∝ I", [f"Δm = {fmt(dm1)} × {fmt(I2)} ÷ {fmt(I1)} = **{fmt(dm2)} g**"],
              ["The force is proportional to the current.", "So is the change in reading.", "Scale."])


@template("c18x_motor_power_efficiency", chapter=18, level=5, lo="18e")
def motor_power_efficiency(rng):
    V = nice(rng, 6.0, 12.0)
    I = nice(rng, 0.5, 1.0, 2.0)
    m = nice(rng, 0.5, 1.0)
    h = nice(rng, 0.6, 1.0, 1.2)
    t = nice(rng, 2, 4, 5)
    eff = m * 10 * h / (V * I * t) * 100
    return mk(rng, eff, [(V * I * t / (m * 10 * h) * 100, "Efficiency = useful ÷ input."), (m * h / (V * I * t) * 100, "GPE = m g h: include g."), (100 - eff, "That is the percentage wasted.")],
              "%", f"A model d.c. motor lifts a load.\n\n{md_table(['quantity', 'value'], [['p.d.', f'{fmt(V)} V'], ['current', f'{fmt(I)} A'], ['time', f'{t} s'], ['mass lifted', f'{fmt(m)} kg'], ['height', f'{fmt(h)} m']])}\n\nWhat is the motor's efficiency? (g = 10 N/kg)",
              "input = V I t; useful = m g h; efficiency = useful ÷ input × 100%", [f"input = {fmt(V)} × {fmt(I)} × {t} = {fmt(V * I * t)} J; useful = {fmt(m * 10 * h)} J", f"efficiency = **{fmt(eff)}%**"],
              ["Find the electrical energy input.", "Find the GPE gained.", "Divide; × 100%."])


@template("c18x_motor_speed_turns", chapter=18, level=5, lo="18e")
def motor_speed_turns(rng):
    rows = [(25, nice(rng, 400, 450)), (50, nice(rng, 800, 900)), (100, nice(rng, 1500, 1700))]
    ratio = rows[2][1] / rows[0][1]
    return mk(rng, ratio, [(rows[0][1] / rows[2][1], "The 100-turn motor is FASTER."), (rows[2][1] - rows[0][1], "Find the ratio."), (4, "Calculate from the data.")],
              "times", f"Model motors with different numbers of turns are run at the same current.\n\n{md_table(['turns', 'speed / rev/min'], rows)}\n\nHow many times faster is the 100-turn motor than the 25-turn motor?",
              "ratio = speed(100) ÷ speed(25)", [f"{rows[2][1]} ÷ {rows[0][1]} = **{fmt(ratio)}**"],
              ["Read the two speeds.", "Divide.", "More turns → larger turning effect."])


@template("c18x_commutator_ac_compare", chapter=18, level=5, lo="18f")
def commutator_ac_compare(rng):
    rps = nice(rng, 25, 50)
    f_ac = rps
    return mk(rng, f_ac, [(2 * rps, "The current reverses twice per revolution, but one full cycle is two reversals."), (rps / 2, "One cycle per revolution."), (60 * rps, "Do not convert to per minute.")],
              "Hz", f"In a d.c. motor, the commutator makes the coil current reverse every half turn, so the coil's current is like an a.c. with one cycle per revolution.\n\n{md_table(['quantity', 'value'], [['motor speed', f'{rps} rev/s']])}\n\nWhat is the frequency of this alternating current in the coil?",
              "one cycle per revolution → f = rev/s", [f"f = **{rps} Hz** ({2 * rps} reversals per second)"],
              ["Two reversals make one cycle.", "One revolution = two reversals.", "f = revolutions per second."], dp=0)


@template("c18x_commutator_no_split", chapter=18, level=5, lo="18f")
def commutator_no_split(rng):
    ans = "it rocks back and forth and stops in the vertical position"
    wrongs = {"it turns continuously in one direction": "Without a split ring the current never reverses, so the coil cannot keep turning one way.",
              "it turns twice as fast": "The coil cannot complete a turn.", "nothing happens at all": "It turns part way first."}
    V = nice(rng, 3.0, 4.5, 6.0, 9.0)
    table = md_table(["motor", "connection to coil", "supply"], [["normal", "split-ring commutator", f"{fmt(V)} V d.c."], ["faulty", "two complete slip rings (no split)", f"{fmt(V)} V d.c."]])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhat happens to the faulty motor's coil when it is switched on?",
               "without reversal, the turning effect reverses after half a turn", [f"**{ans}**"],
               ["What does the split ring do?", "Reverses the current every half turn.", "Without it, the forces reverse after half a turn."])
