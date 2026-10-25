"""Chapter 14 Current of Electricity (6091) bank extension: calculation and data-reading templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: wire length and area, filament lamp and
diode I-V graphs, thermistor and LDR data, cells in series, charge and energy in a torch; school papers 2024-2025)."""
import math

from .. import figs, figs3
from .base import fmt, md_table, mk, mkt, nice, sci, template

E = 1.6e-19


# ================================================================== L1
@template("c14x_current_q_t", chapter=14, level=1, lo="14a")
def current_q_t(rng):
    Q = nice(rng, 6, 12, 18, 30, 60)
    t = nice(rng, 2, 3, 5, 10)
    return mk(rng, Q / t, [(Q * t, "I = Q ÷ t."), (t / Q, "Charge goes on top."), (Q, "Divide by the time.")],
              "A", f"{md_table(['quantity', 'value'], [['charge passing a point', f'{Q} C'], ['time', f'{t} s']])}\n\nWhat is the current?",
              "I = Q ÷ t", [f"I = {Q} ÷ {t} = **{fmt(Q / t)} A**"],
              ["Current = rate of flow of charge.", "I = Q ÷ t.", "Divide."])


@template("c14x_current_ammeter_charge", chapter=14, level=1, lo="14a")
def current_ammeter_charge(rng):
    I = nice(rng, 0.2, 0.5, 1.5, 2.0)
    t = nice(rng, 10, 20, 30, 60)
    return mk(rng, I * t, [(I / t, "Q = I × t."), (t / I, "Multiply current by time."), (I * t * 60, "The time is already in seconds.")],
              "C", f"The ammeter in Fig. 1 reads **{fmt(I)} A** for **{t} s**. How much charge flows through the lamp?",
              "Q = I t", [f"Q = {fmt(I)} × {t} = **{fmt(I * t)} C**"],
              ["Rearrange I = Q ÷ t.", "Q = I × t.", "Multiply."], figure=figs3.circuit(top=[("lamp", "")], bottom=[("A", f"{fmt(I)} A")]))


@template("c14x_charge_minutes", chapter=14, level=1, lo="14c")
def charge_minutes(rng):
    I = nice(rng, 0.25, 0.5, 2.0, 3.0)
    t_min = nice(rng, 2, 4, 5, 10)
    return mk(rng, I * t_min * 60, [(I * t_min, "Convert minutes to seconds."), (I * t_min * 3600, "1 minute = 60 s, not 3600 s."), (I / (t_min * 60), "Q = I × t.")],
              "C", f"{md_table(['quantity', 'value'], [['current in a heater', f'{fmt(I)} A'], ['time switched on', f'{t_min} min']])}\n\nHow much charge flows?",
              "Q = I t, with t in s", [f"t = {t_min * 60} s", f"Q = {fmt(I)} × {t_min * 60} = **{fmt(I * t_min * 60)} C**"],
              ["Convert the time to seconds.", "Q = I t.", "Multiply."])


@template("c14x_r_simple_table", chapter=14, level=1, lo="14h")
def r_simple_table(rng):
    V = nice(rng, 3.0, 4.5, 6.0, 9.0, 12.0)
    I = nice(rng, 0.2, 0.3, 0.5, 1.5)
    return mk(rng, V / I, [(V * I, "R = V ÷ I."), (I / V, "Voltage goes on top."), (V, "Divide by the current.")],
              "Ω", f"{md_table(['quantity', 'value'], [['p.d. across resistor', f'{fmt(V)} V'], ['current through resistor', f'{fmt(I)} A']])}\n\nWhat is its resistance?",
              "R = V ÷ I", [f"R = {fmt(V)} ÷ {fmt(I)} = **{fmt(V / I)} Ω**"],
              ["Resistance = p.d. ÷ current.", "R = V ÷ I.", "Divide."])


@template("c14x_energy_qv_simple", chapter=14, level=1, lo="14f")
def energy_qv_simple(rng):
    Q = nice(rng, 5, 10, 20, 50)
    V = nice(rng, 1.5, 3.0, 6.0, 12.0)
    return mk(rng, Q * V, [(Q / V, "W = Q × V."), (V / Q, "Multiply charge by p.d."), (Q + V, "Multiply.")],
              "J", f"{md_table(['quantity', 'value'], [['charge passing through a lamp', f'{Q} C'], ['p.d. across the lamp', f'{fmt(V)} V']])}\n\nHow much electrical energy is converted in the lamp?",
              "W = Q V", [f"W = {Q} × {fmt(V)} = **{fmt(Q * V)} J**"],
              ["p.d. = energy per unit charge.", "W = Q V.", "Multiply."])


@template("c14x_pd_from_energy", chapter=14, level=1, lo="14f")
def pd_from_energy(rng):
    W = nice(rng, 30, 60, 90, 120)
    Q = nice(rng, 5, 10, 20)
    return mk(rng, W / Q, [(W * Q, "V = W ÷ Q."), (Q / W, "Energy goes on top."), (W, "Divide by the charge.")],
              "V", f"{md_table(['quantity', 'value'], [['energy converted in a motor', f'{W} J'], ['charge passing through it', f'{Q} C']])}\n\nWhat is the p.d. across the motor?",
              "V = W ÷ Q", [f"V = {W} ÷ {Q} = **{fmt(W / Q)} V**"],
              ["p.d. is energy per coulomb.", "V = W ÷ Q.", "Divide."])


@template("c14x_cells_series_total", chapter=14, level=1, lo="14e")
def cells_series_total(rng):
    e = nice(rng, 1.2, 1.5, 2.0)
    n = nice(rng, 2, 3, 4, 6)
    return mk(rng, n * e, [(e, "Cells in series ADD their e.m.f.s."), (e / n, "Multiply, do not divide."), (n + e, "Multiply the number of cells by the e.m.f. of each.")],
              "V", f"{md_table(['quantity', 'value'], [['number of identical cells in series', n], ['e.m.f. of each cell', f'{fmt(e)} V']])}\n\nWhat is the total e.m.f.?",
              "cells in series (same way round): e.m.f.s add", [f"= {n} × {fmt(e)} = **{fmt(n * e)} V**"],
              ["Cells in series add up.", "All face the same way.", "Multiply."])


@template("c14x_cells_parallel_emf", chapter=14, level=1, lo="14e")
def cells_parallel_emf(rng):
    e = nice(rng, 1.5, 2.0, 9.0)
    n = nice(rng, 2, 3, 4)
    return mk(rng, e, [(n * e, "Identical cells in PARALLEL give the same e.m.f. as one cell."), (e / n, "The e.m.f. does not divide."), (e * 2, "Parallel cells do not add.")],
              "V", f"{md_table(['quantity', 'value'], [['number of identical cells in parallel', n], ['e.m.f. of each cell', f'{fmt(e)} V']])}\n\nWhat is the combined e.m.f.? (They last longer, but the e.m.f. is the same.)",
              "identical cells in parallel: e.m.f. = one cell", [f"e.m.f. = **{fmt(e)} V**"],
              ["Parallel cells share the current.", "The e.m.f. stays the same.", "Same as one cell."])


# ================================================================== L2
@template("c14x_battery_mah", chapter=14, level=2, lo="14c")
def battery_mah(rng):
    mah = nice(rng, 1000, 2000, 2500, 3000)
    I_ma = nice(rng, 100, 200, 250, 500)
    return mk(rng, mah / I_ma, [(mah * I_ma, "Time = capacity ÷ current."), (I_ma / mah, "Capacity goes on top."), (mah / I_ma * 60, "The answer is in hours.")],
              "h", f"A phone battery is rated in milliamp-hours (mA h), a unit of charge.\n\n{md_table(['quantity', 'value'], [['battery capacity', f'{mah} mA h'], ['average current drawn', f'{I_ma} mA']])}\n\nHow long will a full battery last?",
              "t = Q ÷ I (mA h ÷ mA = h)", [f"t = {mah} ÷ {I_ma} = **{fmt(mah / I_ma)} h**"],
              ["mA h is current × time.", "t = Q ÷ I.", "Answer in hours."])


@template("c14x_charge_mah_coulombs", chapter=14, level=2, lo="14c")
def charge_mah_coulombs(rng):
    mah = nice(rng, 500, 1000, 2000)
    Q = mah / 1000 * 3600
    return mk(rng, Q, [(mah * 3600, "Convert mA to A first."), (mah / 1000, "Convert hours to seconds."), (mah * 3.6 * 1000, "1 mA h = 0.001 A × 3600 s = 3.6 C.")],
              "C", f"{md_table(['quantity', 'value'], [['battery capacity', f'{mah} mA h']])}\n\nHow much charge is this in coulombs?",
              "Q = I t = (mA ÷ 1000) × (h × 3600)", [f"Q = {fmt(mah / 1000)} A × 3600 s = **{fmt(Q)} C**"],
              ["Write mA h as a current × time.", "Convert to A and s.", "Multiply."])


@template("c14x_cells_reversed", chapter=14, level=2, lo="14e")
def cells_reversed(rng):
    e = nice(rng, 1.5, 2.0)
    n = nice(rng, 4, 5, 6)
    rev = 1
    tot = (n - 2 * rev) * e
    return mk(rng, tot, [(n * e, "A reversed cell SUBTRACTS its e.m.f."), ((n - 1) * e, "A reversed cell does not just drop out: it subtracts."), (2 * e, "Count the forward cells minus the reversed one.")],
              "V", f"A torch has **{n}** cells of e.m.f. **{fmt(e)} V** each in series, but **one** is put in the wrong way round.\n\n{md_table(['quantity', 'value'], [['cells the right way', n - 1], ['cells reversed', 1], ['e.m.f. of each', f'{fmt(e)} V']])}\n\nWhat is the total e.m.f.?",
              "reversed cell subtracts: total = (forward − reversed) × e", [f"= ({n - 1} − 1) × {fmt(e)} = **{fmt(tot)} V**"],
              ["Forward cells add.", "A reversed cell opposes them.", "Subtract it."])


@template("c14x_current_from_v_r", chapter=14, level=2, lo="14h")
def current_from_v_r(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    R = nice(rng, 20, 30, 40, 60)
    return mk(rng, V / R, [(V * R, "I = V ÷ R."), (R / V, "Voltage goes on top."), (V / R * 1000, "The answer is in A.")],
              "A", f"A resistor of **{R} Ω** is connected across a **{fmt(V)} V** supply (Fig. 1). What current flows?",
              "I = V ÷ R", [f"I = {fmt(V)} ÷ {R} = **{fmt(V / R)} A**"],
              ["Rearrange R = V ÷ I.", "I = V ÷ R.", "Divide."], figure=figs3.circuit(top=[("R", f"{R} Ω")], bottom=[("A", "?")], emf=f"{fmt(V)} V"))


@template("c14x_pd_from_ir_table", chapter=14, level=2, lo="14h")
def pd_from_ir_table(rng):
    I = nice(rng, 0.2, 0.25, 0.4, 0.5)
    R = nice(rng, 12, 20, 24, 50)
    return mk(rng, I * R, [(R / I, "V = I × R."), (I / R, "Multiply current by resistance."), (I + R, "Multiply.")],
              "V", f"{md_table(['quantity', 'value'], [['current through resistor', f'{fmt(I)} A'], ['resistance', f'{R} Ω']])}\n\nWhat is the p.d. across it?",
              "V = I R", [f"V = {fmt(I)} × {R} = **{fmt(I * R)} V**"],
              ["V = I R.", "Multiply.", "Answer in volts."])


@template("c14x_r_double_length", chapter=14, level=2, lo="14i")
def r_double_length(rng):
    R1 = nice(rng, 2, 4, 5, 8)
    k = nice(rng, 2, 3, 4)
    return mk(rng, R1 * k, [(R1 / k, "A LONGER wire has MORE resistance."), (R1 * k * k, "R ∝ L, not L²."), (R1, "The length affects the resistance.")],
              "Ω", f"A wire of the same material and thickness is used, but its length changes (Fig. 1).\n\n{md_table(['wire', 'length', 'resistance / Ω'], [['A', 'L', R1], ['B', f'{k}L', '?']])}\n\nWhat is the resistance of B?",
              "R ∝ L (same material and area)", [f"R_B = {R1} × {k} = **{R1 * k} Ω**"],
              ["How does R depend on length?", "Directly proportional.", f"× {k}."], figure=figs3.wire_sketch("length L", "area A"), dp=0)


@template("c14x_r_double_area", chapter=14, level=2, lo="14i")
def r_double_area(rng):
    R1 = nice(rng, 6, 8, 12, 16)
    k = nice(rng, 2, 4)
    return mk(rng, R1 / k, [(R1 * k, "A THICKER wire has LESS resistance."), (R1 / k ** 2, "R ∝ 1/A, so divide by the area factor once."), (R1, "The area affects the resistance.")],
              "Ω", f"Two wires of the same metal and length:\n\n{md_table(['wire', 'cross-sectional area', 'resistance / Ω'], [['P', 'A', R1], ['Q', f'{k}A', '?']])}\n\nWhat is the resistance of Q?",
              "R ∝ 1/A", [f"R_Q = {R1} ÷ {k} = **{fmt(R1 / k)} Ω**"],
              ["How does R depend on area?", "Inversely.", f"÷ {k}."])


@template("c14x_energy_battery_charge", chapter=14, level=2, lo="14f")
def energy_battery_charge(rng):
    V = nice(rng, 3.7, 6.0, 9.0, 12.0)
    Q = nice(rng, 100, 200, 500)
    return mk(rng, V * Q / 1000, [(V * Q, "That is in J; the answer is in kJ."), (Q / V / 1000, "W = Q V."), (V * Q / 1e6, "1 kJ = 1000 J.")],
              "kJ", f"{md_table(['quantity', 'value'], [['charge delivered by a battery', f'{Q} C'], ['p.d. of battery', f'{fmt(V)} V']])}\n\nHow much energy does it transfer, in kJ?",
              "W = Q V", [f"W = {Q} × {fmt(V)} = {fmt(V * Q)} J = **{fmt(V * Q / 1000)} kJ**"],
              ["Energy = charge × p.d.", "Multiply.", "Convert to kJ."])


@template("c14x_pd_component_energy", chapter=14, level=2, lo="14f")
def pd_component_energy(rng):
    I = nice(rng, 0.5, 1.0, 2.0)
    t = nice(rng, 10, 20, 30)
    W = nice(rng, 60, 120, 180)
    V = W / (I * t)
    return mk(rng, V, [(W / I, "Find the charge Q = I t first."), (W * I * t, "V = W ÷ Q."), (W / t, "That is the power, not the p.d.")],
              "V", f"{md_table(['quantity', 'value'], [['current in a heater', f'{fmt(I)} A'], ['time', f'{t} s'], ['energy converted', f'{W} J']])}\n\nWhat is the p.d. across the heater?",
              "Q = I t; V = W ÷ Q", [f"Q = {fmt(I)} × {t} = {fmt(I * t)} C", f"V = {W} ÷ {fmt(I * t)} = **{fmt(V)} V**"],
              ["Find the charge first.", "Q = I t.", "Then V = W ÷ Q."])


# ================================================================== L3
@template("c14x_emf_definition_calc", chapter=14, level=3, lo="14d")
def emf_definition_calc(rng):
    W = nice(rng, 45, 90, 180)
    Q = nice(rng, 15, 30, 60)
    return mk(rng, W / Q, [(W * Q, "e.m.f. = energy ÷ charge."), (Q / W, "Energy goes on top."), (W, "Divide by the charge.")],
              "V", f"A cell does work driving charge round a complete circuit.\n\n{md_table(['quantity', 'value'], [['energy converted by the cell', f'{W} J'], ['charge driven round the circuit', f'{Q} C']])}\n\nWhat is the e.m.f. of the cell?",
              "e.m.f. = W ÷ Q (energy per unit charge supplied)", [f"e.m.f. = {W} ÷ {Q} = **{fmt(W / Q)} V**"],
              ["e.m.f. is energy per coulomb.", "From the source.", "Divide."])


@template("c14x_emf_energy_time", chapter=14, level=3, lo="14d")
def emf_energy_time(rng):
    emf = nice(rng, 1.5, 3.0, 9.0)
    I = nice(rng, 0.1, 0.2, 0.3)
    t_min = nice(rng, 5, 10, 20)
    W = emf * I * t_min * 60
    return mk(rng, W, [(emf * I * t_min, "Convert minutes to seconds."), (emf * t_min * 60, "Find the charge: Q = I t."), (emf * I, "That is the power; multiply by the time.")],
              "J", f"{md_table(['quantity', 'value'], [['e.m.f. of battery', f'{fmt(emf)} V'], ['current', f'{fmt(I)} A'], ['time', f'{t_min} min']])}\n\nHow much energy does the battery supply?",
              "Q = I t; W = e.m.f. × Q", [f"Q = {fmt(I)} × {t_min * 60} = {fmt(I * t_min * 60)} C", f"W = {fmt(emf)} × {fmt(I * t_min * 60)} = **{fmt(W)} J**"],
              ["Find the charge.", "Multiply by the e.m.f.", "Time in seconds."])


@template("c14x_r_from_graph_ohmic", chapter=14, level=3, lo="14h")
def r_from_graph_ohmic(rng):
    R = nice(rng, 2.0, 4.0, 5.0, 10.0)
    vmax = 6.0
    return mk(rng, R, [(1 / R, "R = V ÷ I, not I ÷ V."), (R * 2, "Read one point carefully."), (vmax, "Use a point on the line: V ÷ I.")],
              "Ω", f"Fig. 1 shows the I-V graph for a resistor at constant temperature. What is its resistance?",
              "R = V ÷ I at any point (straight line through origin)", [f"e.g. at {fmt(vmax)} V, I = {fmt(vmax / R)} A", f"R = {fmt(vmax)} ÷ {fmt(vmax / R)} = **{fmt(R)} Ω**"],
              ["Pick a point on the line.", "Read V and I.", "R = V ÷ I."], figure=figs3.iv_graph("ohmic", R=R, vmax=vmax))


@template("c14x_r_table_average", chapter=14, level=3, lo="14h")
def r_table_average(rng):
    R = nice(rng, 5.0, 8.0, 10.0)
    Vs = [2.0, 4.0, 6.0]
    Is = [round(v / R * nice(rng, 0.98, 1.0, 1.02), 3) for v in Vs]
    Rs = [v / i for v, i in zip(Vs, Is)]
    avg = sum(Rs) / 3
    return mk(rng, avg, [(Vs[0] / Is[0], "Average all three values."), (sum(Vs) / sum(Is) * 2, "Find R = V ÷ I for each row, then average."), (avg / 2, "R = V ÷ I.")],
              "Ω", f"A student measures a resistor three times.\n\n{md_table(['V / V', 'I / A'], [[fmt(v), fmt(i, sf=3)] for v, i in zip(Vs, Is)])}\n\nWhat is the average resistance?",
              "R = V ÷ I for each; average", [", ".join(f"{fmt(r, sf=3)} Ω" for r in Rs), f"average = **{fmt(avg, sf=3)} Ω**"],
              ["Find R for each row.", "R = V ÷ I.", "Average them."], sf=3)


@template("c14x_r_diameter", chapter=14, level=3, lo="14i")
def r_diameter(rng):
    R1 = nice(rng, 8, 12, 16, 20)
    k = nice(rng, 2, 3)
    return mk(rng, R1 / k ** 2, [(R1 / k, "Area ∝ diameter²: R falls by the SQUARE of the diameter factor."), (R1 * k ** 2, "A thicker wire has LESS resistance."), (R1, "Changing the diameter changes the area.")],
              "Ω", f"Two wires of the same metal and length:\n\n{md_table(['wire', 'diameter', 'resistance / Ω'], [['X', 'd', R1], ['Y', f'{k}d', '?']])}\n\nWhat is the resistance of Y?",
              "A ∝ d²; R ∝ 1/A → R ∝ 1/d²", [f"area increases by {k}² = {k * k}", f"R_Y = {R1} ÷ {k * k} = **{fmt(R1 / k ** 2)} Ω**"],
              ["How does area depend on diameter?", "A = π d² ÷ 4.", "R ∝ 1/d²."])


@template("c14x_resistivity_simple", chapter=14, level=3, lo="14i")
def resistivity_simple(rng):
    rho = nice(rng, 1.7e-8, 2.8e-8, 4.9e-7, 1.1e-6)
    L = nice(rng, 1.0, 2.0, 5.0, 10.0)
    A = nice(rng, 1e-6, 2e-6, 5e-7)
    R = rho * L / A
    return mk(rng, R, [(rho * A / L, "R = ρ L ÷ A."), (rho * L, "Divide by the area."), (R * 1000, "Check the powers of ten.")],
              "Ω", f"{md_table(['quantity', 'value'], [['resistivity of the metal', f'{sci(rho)} Ω m'], ['length of wire', f'{fmt(L)} m'], ['cross-sectional area', f'{sci(A)} m²']])}\n\nWhat is the resistance of the wire?",
              "R = ρ L ÷ A", [f"R = {sci(rho)} × {fmt(L)} ÷ {sci(A)} = **{fmt(R, sf=3)} Ω**"],
              ["Use R = ρ L ÷ A.", "Substitute.", "Watch the powers of ten."], sf=3)


@template("c14x_lamp_r_two_points", chapter=14, level=3, lo="14k")
def lamp_r_two_points(rng):
    rows = [(2.0, 0.20), (4.0, 0.30), (6.0, 0.36)]
    k = rng.randrange(3)
    V, I = rows[k]
    return mk(rng, V / I, [(I / V, "R = V ÷ I."), (rows[0][0] / rows[0][1], "Use the row asked for: a lamp's resistance changes."), (V * I, "Divide V by I.")],
              "Ω", f"Readings for a filament lamp:\n\n{md_table(['p.d. / V', 'current / A'], [[fmt(v), fmt(i)] for v, i in rows])}\n\nWhat is the lamp's resistance at **{fmt(V)} V**?",
              "R = V ÷ I at that point", [f"R = {fmt(V)} ÷ {fmt(I)} = **{fmt(V / I)} Ω**"],
              ["Read the current at this p.d.", "R = V ÷ I.", "The resistance changes with V for a lamp."])


@template("c14x_diode_threshold", chapter=14, level=3, lo="14k")
def diode_threshold(rng):
    V = nice(rng, -3.0, -2.0, 0.3, 1.0, 1.5, 2.0)
    I = 0 if V <= 0.6 else (V - 0.6) * 1.2
    if I == 0:
        ans = "zero"
    else:
        ans = f"{fmt(I)} A"
    wrongs_txt = ["zero", f"{fmt(abs(V) / 2)} A", f"{fmt(abs(V) * 1.2)} A", "1.0 A"]
    wrongs = {w: ("A diode only conducts in the forward direction above about 0.6 V." if w == "zero" else "Read the current from the graph at this p.d.") for w in wrongs_txt if w != ans}
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"Fig. 1 shows the I-V characteristic of a semiconductor diode. What is the current when the p.d. across it is **{fmt(V)} V**?",
               "diode: no current in reverse or below ≈ 0.6 V; then current rises steeply", [f"at {fmt(V)} V → **{ans}**"],
               ["Is the p.d. forward or reverse?", "Is it above the threshold?", "Read the graph."], figure=figs3.iv_graph("diode", vmax=3.0))


@template("c14x_charge_from_energy_pd", chapter=14, level=3, lo="14f")
def charge_from_energy_pd(rng):
    W = nice(rng, 240, 360, 480, 720)
    V = nice(rng, 6.0, 12.0, 24.0)
    Q = W / V
    return mk(rng, Q, [(W * V, "Q = W ÷ V."), (V / W, "Energy goes on top."), (Q / 60, "No time conversion is needed.")],
              "C", f"A car headlamp converts energy as charge passes through it.\n\n{md_table(['quantity', 'value'], [['energy converted', f'{W} J'], ['p.d. across lamp', f'{fmt(V)} V']])}\n\nHow much charge passed through the lamp?",
              "W = Q V → Q = W ÷ V", [f"Q = {W} ÷ {fmt(V)} = **{fmt(Q)} C**"],
              ["p.d. = energy per coulomb.", "Rearrange for Q.", "Divide."])


# ================================================================== L4
@template("c14x_electrons_per_second_ma", chapter=14, level=4, lo="14c")
def electrons_per_second_ma(rng):
    I_ma = nice(rng, 80, 160, 320, 480)
    n = I_ma / 1000 / E
    return mk(rng, n, [(I_ma / E, "Convert mA to A."), (I_ma / 1000 * E, "n = I ÷ e."), (n / 60, "This is per SECOND.")],
              "electrons per second", f"{md_table(['quantity', 'value'], [['current in an LED', f'{I_ma} mA'], ['charge on an electron', '1.6 × 10⁻¹⁹ C']])}\n\nHow many electrons pass any point each second?",
              "Q per second = I; n = I ÷ e", [f"I = {fmt(I_ma / 1000)} A", f"n = {fmt(I_ma / 1000)} ÷ 1.6 × 10⁻¹⁹ = **{sci(n)}**"],
              ["Current = charge per second.", "Each electron carries e.", "n = I ÷ e."])


@template("c14x_charge_varying_current", chapter=14, level=4, lo="14c")
def charge_varying_current(rng):
    I1, t1 = nice(rng, 0.5, 1.0), nice(rng, 20, 30)
    I2, t2 = nice(rng, 2.0, 1.5), nice(rng, 10, 20)
    Q = I1 * t1 + I2 * t2
    return mk(rng, Q, [((I1 + I2) * (t1 + t2), "Find the charge in each stage separately."), (I1 * t1, "Include the second stage."), ((I1 + I2) / 2 * (t1 + t2), "Do not average the currents; add Q₁ + Q₂.")],
              "C", f"A motor draws different currents during start-up.\n\n{md_table(['stage', 'current / A', 'time / s'], [['1', fmt(I1), t1], ['2', fmt(I2), t2]])}\n\nWhat total charge flows?",
              "Q = I₁t₁ + I₂t₂", [f"Q = {fmt(I1)}×{t1} + {fmt(I2)}×{t2} = **{fmt(Q)} C**"],
              ["Find the charge in each stage.", "Q = I t.", "Add."])


@template("c14x_thermistor_graph", chapter=14, level=4, lo="14j")
def thermistor_graph(rng):
    pts = [(0, 12), (20, 6), (40, 3), (60, 1.5), (80, 0.75)]
    T = rng.choice([20, 40, 60])
    R = dict(pts)[T]
    return mk(rng, R, [(dict(pts)[T + 20], "Read at the temperature asked for; R FALLS as T rises."), (dict(pts)[T - 20], "Read at the correct temperature."), (R * 1000, "The graph is in kΩ.")],
              "kΩ", f"Fig. 1 shows how the resistance of a thermistor varies with temperature. What is its resistance at **{T} °C**?",
              "read the graph: thermistor resistance falls as temperature rises", [f"at {T} °C, R = **{fmt(R)} kΩ**"],
              ["Find the temperature on the x-axis.", "Read up to the curve.", "Read across."], figure=figs.graph(pts, 80, 14, 20, 2, xlabel="temperature / °C", ylabel="resistance / kΩ"))


@template("c14x_ldr_table", chapter=14, level=4, lo="14j")
def ldr_table(rng):
    rows = [("bright sunlight", 0.2), ("classroom light", 2.0), ("dim room", 20), ("darkness", 500)]
    rng.shuffle(rows)
    V = 6.0
    which = rng.choice(rows)
    I = V / (which[1] * 1000) * 1000
    return mk(rng, I, [(V / which[1], "Convert kΩ to Ω."), (V * which[1], "I = V ÷ R."), (I / 1000, "The answer is in mA.")],
              "mA", f"An LDR is connected directly across a **6.0 V** supply.\n\n{md_table(['light level', 'resistance of LDR / kΩ'], [[n, r] for n, r in rows])}\n\nWhat current flows in **{which[0]}**?",
              "I = V ÷ R with R in Ω", [f"R = {fmt(which[1])} kΩ = {fmt(which[1] * 1000)} Ω", f"I = 6.0 ÷ {fmt(which[1] * 1000)} = **{fmt(I)} mA**"],
              ["Find R for that light level.", "Convert to ohms.", "I = V ÷ R, give mA."])


@template("c14x_energy_charge_component", chapter=14, level=4, lo="14f")
def energy_charge_component(rng):
    V = nice(rng, 3.0, 6.0, 12.0)
    I = nice(rng, 0.2, 0.5, 1.5)
    t_min = nice(rng, 2, 5, 10)
    W = V * I * t_min * 60
    return mk(rng, W, [(V * I * t_min, "Convert minutes to seconds."), (V * I, "Multiply by the time too."), (V * t_min * 60, "Find the charge Q = I t first.")],
              "J", f"{md_table(['quantity', 'value'], [['p.d. across a lamp', f'{fmt(V)} V'], ['current', f'{fmt(I)} A'], ['time', f'{t_min} min']])}\n\nHow much energy does the lamp convert?",
              "W = Q V = V I t", [f"Q = {fmt(I)} × {t_min * 60} = {fmt(I * t_min * 60)} C", f"W = {fmt(I * t_min * 60)} × {fmt(V)} = **{fmt(W)} J**"],
              ["Find the charge.", "Multiply by the p.d.", "Time in seconds."])


@template("c14x_pd_from_energy_current", chapter=14, level=4, lo="14f")
def pd_from_energy_current(rng):
    W = nice(rng, 1800, 3600, 7200)
    I = nice(rng, 2, 3, 5)
    t = nice(rng, 60, 120, 300)
    V = W / (I * t)
    return mk(rng, V, [(W / I, "Divide by the charge (I × t), not just I."), (W / t, "That is the power."), (W * I * t, "V = W ÷ (I t).")],
              "V", f"{md_table(['quantity', 'value'], [['energy converted in a kettle element', f'{W} J'], ['current', f'{I} A'], ['time', f'{t} s']])}\n\nWhat is the p.d. across the element?",
              "V = W ÷ Q = W ÷ (I t)", [f"Q = {I} × {t} = {I * t} C", f"V = {W} ÷ {I * t} = **{fmt(V)} V**"],
              ["Find the charge.", "Q = I t.", "V = W ÷ Q."])


@template("c14x_resistivity_find_length", chapter=14, level=4, lo="14i")
def resistivity_find_length(rng):
    rho = nice(rng, 1.1e-6, 4.9e-7)
    A = nice(rng, 2e-7, 5e-7)
    R = nice(rng, 10, 20, 50)
    L = R * A / rho
    return mk(rng, L, [(R * rho / A, "L = R A ÷ ρ."), (R / (rho * A), "Rearrange R = ρ L ÷ A."), (L * 100, "The answer is in metres.")],
              "m", f"A heating coil must have a resistance of **{R} Ω**.\n\n{md_table(['quantity', 'value'], [['resistivity of nichrome', f'{sci(rho)} Ω m'], ['cross-sectional area of wire', f'{sci(A)} m²']])}\n\nWhat length of wire is needed?",
              "R = ρ L ÷ A → L = R A ÷ ρ", [f"L = {R} × {sci(A)} ÷ {sci(rho)} = **{fmt(L, sf=3)} m**"],
              ["Rearrange the resistivity formula.", "L = R A ÷ ρ.", "Substitute."], sf=3)


@template("c14x_lamp_r_change", chapter=14, level=4, lo="14k")
def lamp_r_change(rng):
    V1, I1 = 1.0, 0.25
    V2, I2 = nice(rng, 6.0, 12.0), nice(rng, 0.5, 0.6)
    R1, R2 = V1 / I1, V2 / I2
    return mk(rng, R2 - R1, [(R2, "That is the hot resistance; find the INCREASE."), (R1, "That is the cold resistance."), (R2 / R1, "Find the difference, not the ratio.")],
              "Ω", f"Readings for a filament lamp:\n\n{md_table(['p.d. / V', 'current / A'], [[fmt(V1), fmt(I1)], [fmt(V2), fmt(I2)]])}\n\nBy how much does its resistance increase between these two readings?",
              "R = V ÷ I at each; subtract", [f"R₁ = {fmt(V1)} ÷ {fmt(I1)} = {fmt(R1)} Ω; R₂ = {fmt(V2)} ÷ {fmt(I2)} = {fmt(R2)} Ω", f"increase = **{fmt(R2 - R1)} Ω**"],
              ["Find R at each p.d.", "R = V ÷ I.", "Subtract."])


# ================================================================== L5
@template("c14x_electron_drift_count", chapter=14, level=5, lo="14a")
def electron_drift_count(rng):
    I = nice(rng, 0.8, 1.6, 3.2)
    t_min = nice(rng, 1, 5, 10)
    n = I * t_min * 60 / E
    return mk(rng, n, [(I / E, "That is per second; multiply by the time."), (I * t_min / E, "Convert minutes to seconds."), (n * E, "n = Q ÷ e.")],
              "electrons", f"{md_table(['quantity', 'value'], [['current in a wire', f'{fmt(I)} A'], ['time', f'{t_min} min'], ['e', '1.6 × 10⁻¹⁹ C']])}\n\nHow many electrons pass a point in the wire in this time?",
              "Q = I t; n = Q ÷ e", [f"Q = {fmt(I)} × {t_min * 60} = {fmt(I * t_min * 60)} C", f"n = {fmt(I * t_min * 60)} ÷ 1.6 × 10⁻¹⁹ = **{sci(n)}**"],
              ["Find the total charge.", "Divide by e.", "Standard form."])


@template("c14x_resistivity_compare", chapter=14, level=5, lo="14i")
def resistivity_compare(rng):
    rho_a, rho_b = 1.7e-8, 2.8e-8
    kL = nice(rng, 2, 3)
    kd = nice(rng, 2)
    ratio = (rho_b / rho_a) * kL / kd ** 2
    return mk(rng, ratio, [((rho_b / rho_a) * kL / kd, "Area ∝ d²: divide by the diameter factor SQUARED."), (kL / kd ** 2, "Include the ratio of resistivities."), ((rho_b / rho_a) * kL * kd ** 2, "A larger diameter means LESS resistance.")],
              "times", f"Compare two wires.\n\n{md_table(['wire', 'material (resistivity / Ω m)', 'length', 'diameter'], [['A', 'copper (1.7 × 10⁻⁸)', 'L', 'd'], ['B', 'aluminium (2.8 × 10⁻⁸)', f'{kL}L', f'{kd}d']])}\n\nHow many times greater is the resistance of B than that of A?",
              "R = ρ L ÷ A, A ∝ d² → R_B ÷ R_A = (ρ_B ÷ ρ_A) × (L ratio) ÷ (d ratio)²", [f"= (2.8 ÷ 1.7) × {kL} ÷ {kd}² = **{fmt(ratio, sf=3)}**"],
              ["Write R for each wire.", "Area depends on d².", "Combine the three factors."], sf=3)


@template("c14x_iv_gradient_meaning", chapter=14, level=5, lo="14k")
def iv_gradient_meaning(rng):
    R = nice(rng, 2.5, 4.0, 5.0)
    vmax = 6.0
    g = 1 / R
    return mk(rng, g, [(R, "The gradient of an I-V graph is I ÷ V = 1/R."), (g * 2, "Read rise ÷ run carefully."), (vmax / R * vmax, "Gradient = ΔI ÷ ΔV.")],
              "A/V", f"Fig. 1 shows the I-V graph for an ohmic conductor. What is the gradient of the line (current ÷ p.d.)?",
              "gradient = ΔI ÷ ΔV = 1/R", [f"at {fmt(vmax)} V, I = {fmt(vmax / R)} A", f"gradient = {fmt(vmax / R)} ÷ {fmt(vmax)} = **{fmt(g)} A/V** (so R = {fmt(R)} Ω)"],
              ["Gradient = rise ÷ run.", "I on the y-axis, V on the x-axis.", "It equals 1/R."], figure=figs3.iv_graph("ohmic", R=R, vmax=vmax))


@template("c14x_diode_circuit_current", chapter=14, level=5, lo="14k")
def diode_circuit_current(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    R = nice(rng, 100, 200, 470)
    forward = rng.choice([True, False])
    I = (V - 0.7) / R * 1000 if forward else 0.0
    if forward:
        return mk(rng, I, [(V / R * 1000, "Subtract the 0.7 V across the diode first."), ((V - 0.7) / R, "Convert A to mA."), ((V + 0.7) / R * 1000, "Subtract, do not add, the diode's p.d.")],
                  "mA", f"A diode (forward-biased, with 0.7 V across it when conducting) is in series with a **{R} Ω** resistor and a **{fmt(V)} V** supply.\n\n{md_table(['quantity', 'value'], [['supply', f'{fmt(V)} V'], ['diode p.d. when conducting', '0.7 V'], ['resistor', f'{R} Ω']])}\n\nWhat current flows, in mA?",
                  "p.d. across R = V − 0.7; I = V_R ÷ R", [f"V_R = {fmt(V)} − 0.7 = {fmt(V - 0.7)} V", f"I = {fmt(V - 0.7)} ÷ {R} = **{fmt(I)} mA**"],
                  ["How much p.d. is across the diode?", "The rest is across the resistor.", "I = V ÷ R."])
    return mkt(rng, "zero", {f"{fmt(V / R * 1000)} mA": "A reverse-biased diode has a very high resistance: almost no current.",
                              f"{fmt((V - 0.7) / R * 1000)} mA": "That would be for forward bias.", "it depends on the resistor only": "The diode blocks the current."},
               f"A diode is connected the WRONG way round (reverse-biased) in series with a **{R} Ω** resistor and a **{fmt(V)} V** supply.\n\n{md_table(['quantity', 'value'], [['supply', f'{fmt(V)} V'], ['resistor', f'{R} Ω']])}\n\nWhat current flows?",
               "reverse-biased diode: very high resistance, no current", ["reverse bias → **zero** current"],
               ["Which way does the diode conduct?", "Reverse bias blocks current.", "Current is zero."])


@template("c14x_r_from_ohms_law_table", chapter=14, level=5, lo="14h")
def r_from_ohms_law_table(rng):
    R = nice(rng, 15, 20, 25)
    rows = [(1.5, 1.5 / R), (3.0, 3.0 / R), (4.5, 4.5 / R), (6.0, 6.0 / R)]
    miss = rng.randrange(4)
    V, I = rows[miss]
    return mk(rng, I * 1000, [(V * R, "I = V ÷ R."), (I, "Convert A to mA."), (rows[(miss + 1) % 4][1] * 1000, "Use the p.d. in this row.")],
              "mA", f"A student records readings for a fixed resistor. One current is missing.\n\n{md_table(['p.d. / V', 'current / mA'], [[fmt(v), ('?' if k == miss else fmt(i * 1000))] for k, (v, i) in enumerate(rows)])}\n\nWhat is the missing current?",
              "R constant (ohmic): I ∝ V", [f"R = {fmt(rows[(miss + 1) % 4][0])} ÷ {fmt(rows[(miss + 1) % 4][1])} = {R} Ω", f"I = {fmt(V)} ÷ {R} = **{fmt(I * 1000)} mA**"],
              ["Find R from a complete row.", "R is constant.", "I = V ÷ R."])


@template("c14x_r_heating_element_hot", chapter=14, level=5, lo="14h")
def r_heating_element_hot(rng):
    V = 230
    P = nice(rng, 1000, 2000, 2300, 3000)
    I = P / V
    R = V / I
    return mk(rng, R, [(I, "That is the current; R = V ÷ I."), (V * I, "That is the power."), (R / 2, "R = V ÷ I.")],
              "Ω", f"A heater on the 230 V mains draws a current found from its power rating.\n\n{md_table(['quantity', 'value'], [['mains p.d.', '230 V'], ['current when hot', f'{fmt(I, sf=3)} A']])}\n\nWhat is its resistance when hot?",
              "R = V ÷ I", [f"R = 230 ÷ {fmt(I, sf=3)} = **{fmt(R, sf=3)} Ω**"],
              ["R = V ÷ I.", "Use the hot current.", "Divide."], sf=3)


@template("c14x_thermistor_temp_from_current", chapter=14, level=5, lo="14j")
def thermistor_temp_from_current(rng):
    pts = [(0, 12), (20, 6), (40, 3), (60, 1.5), (80, 0.75)]
    T = rng.choice([20, 40, 60])
    R = dict(pts)[T] * 1000
    V = 6.0
    I = V / R * 1000
    return mk(rng, T, [(T + 20, "Find R = V ÷ I first, then read the temperature."), (T - 20, "Check the resistance you read."), (R / 1000, "That is the resistance in kΩ, not the temperature.")],
              "°C", f"A thermistor is connected directly to a **6.0 V** supply and the current is **{fmt(I)} mA**. Fig. 1 shows how its resistance varies with temperature. What is its temperature?",
              "R = V ÷ I; read T from the graph", [f"R = 6.0 ÷ {fmt(I / 1000)} = {fmt(R)} Ω = {fmt(R / 1000)} kΩ", f"from the graph: **{T} °C**"],
              ["Find R from V and I.", "Convert to kΩ.", "Read the temperature from the graph."], figure=figs.graph(pts, 80, 14, 20, 2, xlabel="temperature / °C", ylabel="resistance / kΩ"), dp=0)


@template("c14x_ldr_light_level", chapter=14, level=5, lo="14j")
def ldr_light_level(rng):
    rows = [("bright sunlight", 200), ("classroom", 2000), ("dim room", 20000), ("dark", 500000)]
    target = rng.choice(rows[:3])
    V = 6.0
    I = V / target[1] * 1000
    ans = target[0]
    wrongs = {n: "Find R = V ÷ I and compare with the table." for n, r in rows if n != ans}
    table = md_table(["light level", "resistance of LDR / Ω"], [[n, r] for n, r in rows])
    return mkt(rng, ans, wrongs, f"An LDR across a **6.0 V** supply passes a current of **{fmt(I)} mA**.\n\n{table}\n\nWhat is the light level?",
               "R = V ÷ I; match with the table (LDR resistance falls as light increases)", [f"R = 6.0 ÷ {fmt(I / 1000)} = {fmt(target[1])} Ω → **{ans}**"],
               ["Find the resistance.", "R = V ÷ I.", "Match it to the table."])
