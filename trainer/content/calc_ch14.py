"""Chapter 14 Current of Electricity (6091): Q = I t, R = V / I, e.m.f. of cells in series, W = Q V, I-V graphs,
resistance and the length / area of a wire, electrons per second."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template

E = 1.6e-19


# ---------------------------------------------------------------- L1
@template("c14_charge_from_current_time", chapter=14, level=1, lo="14c")
def charge_from_current_time(rng):
    I = nice(rng, 0.2, 0.5, 1.5, 2.0, 2.5, 3.0, 4.0)
    t = nice(rng, 10, 20, 30, 40, 60, 120)
    Q = I * t
    opts, key, mis = numeric_options(rng, Q, [
        (I / t, "You divided. Charge = current × time."),
        (t / I, "You divided the time by the current. Charge = current × time."),
        (I * t * 60, "The time is already in seconds; do not multiply by 60."),
    ], unit="C", sf=3)
    return dict(
        stem=f"Fig. 1 shows a lamp in a circuit. The ammeter reads **{fmt(I)} A**. How much charge passes through the lamp in **{t} s**?",
        figure=figs3.circuit(top=[("lamp", "")], bottom=[("A", f"{fmt(I)} A")]),
        options=opts, key=key, misconceptions=mis,
        formula="charge = current × time  (Q = I t, with t in seconds)",
        working=["Q = I t", f"= {fmt(I)} × {t}", f"= **{fmt(Q, sf=3)} C**"],
        hints=[
            "Current is the rate of flow of charge: how many coulombs pass each second?",
            f"{fmt(I)} A means {fmt(I)} C every second. How many seconds?",
            f"Q = {fmt(I)} × {t}.",
        ],
    )


@template("c14_resistance_from_v_i", chapter=14, level=1, lo="14h")
def resistance_from_v_i(rng):
    R = nice(rng, 2, 4, 5, 6, 8, 10, 12, 15, 20)
    I = nice(rng, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 1.5)
    V = R * I
    opts, key, mis = numeric_options(rng, R, [
        (I / V, "You divided the wrong way: R = V ÷ I."),
        (V * I, "You multiplied V by I. That gives power, not resistance."),
        (V + I, "Resistance is the RATIO of p.d. to current, not the sum."),
    ], unit="Ω", sf=3)
    return dict(
        stem=f"Fig. 1 shows a resistor in a circuit. The voltmeter reads **{fmt(V)} V** and the ammeter reads **{fmt(I)} A**. What is the resistance of the resistor?",
        figure=figs3.circuit(top=[("R", "")], bottom=[("A", f"{fmt(I)} A")], volt_across=0, emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="resistance = p.d. ÷ current  (R = V / I)",
        working=["R = V ÷ I", f"= {fmt(V)} ÷ {fmt(I)}", f"= **{fmt(R, sf=3)} Ω**"],
        hints=[
            "Resistance is defined as p.d. divided by current.",
            "The voltmeter gives V (across the resistor) and the ammeter gives I (through it).",
            f"R = {fmt(V)} ÷ {fmt(I)}.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c14_current_from_charge_minutes", chapter=14, level=2, lo="14c")
def current_from_charge_minutes(rng):
    I = nice(rng, 0.2, 0.25, 0.5, 0.8, 1.2, 1.5, 2.0)
    t_min = nice(rng, 2, 3, 4, 5, 10)
    Q = I * t_min * 60
    opts, key, mis = numeric_options(rng, I, [
        (Q / t_min, "You used the time in minutes. Current in amperes needs the time in SECONDS."),
        (Q * t_min * 60, "You multiplied. Current = charge ÷ time."),
        (I / 60, "Check the conversion: multiply the minutes by 60 to get seconds, then divide the charge by that."),
    ], unit="A", sf=3)
    table = md_table(["quantity", "value"], [["charge passing through the heater", f"{fmt(Q)} C"], ["time", f"{t_min} min"]])
    return dict(
        stem=f"The table shows measurements for a small electric heater.\n\n{table}\n\nWhat is the current in the heater?",
        options=opts, key=key, misconceptions=mis,
        formula="current = charge ÷ time  (I = Q / t, t in seconds)",
        working=[f"t = {t_min} min = {t_min * 60} s", f"I = Q ÷ t = {fmt(Q)} ÷ {t_min * 60}", f"= **{fmt(I, sf=3)} A**"],
        hints=[
            "Current is charge per second. What must you do to the time first?",
            f"{t_min} minutes = {t_min * 60} seconds.",
            f"I = {fmt(Q)} ÷ {t_min * 60}.",
        ],
    )


@template("c14_emf_cells_in_series", chapter=14, level=2, lo="14e")
def emf_cells_in_series(rng):
    n = nice(rng, 2, 3, 4, 6)
    e = nice(rng, 1.2, 1.5, 2.0)
    total = n * e
    opts, key, mis = numeric_options(rng, total, [
        (e, "Cells in series add their e.m.f.s. One cell's e.m.f. is only part of the total."),
        (e / n, "You divided. Each cell does extra work on the charge, so the e.m.f.s ADD."),
        (total * 2, "Check the number of cells in the battery."),
    ], unit="V", sf=3)
    table = md_table(["", "value"], [["number of identical cells in series", n], ["e.m.f. of each cell", f"{fmt(e)} V"]])
    return dict(
        stem=f"A battery is made from identical cells connected in series.\n\n{table}\n\nWhat is the e.m.f. of the battery?",
        options=opts, key=key, misconceptions=mis,
        formula="for cells in series (connected + to −), total e.m.f. = sum of the individual e.m.f.s",
        working=[f"each cell does {fmt(e)} J of work per coulomb; in series the charge passes through every cell", f"total e.m.f. = {n} × {fmt(e)}", f"= **{fmt(total, sf=3)} V**"],
        hints=[
            "E.m.f. is the work done per coulomb by the source. In series, each coulomb passes through every cell.",
            "So the work done per coulomb by all the cells adds up.",
            f"{n} × {fmt(e)} V.",
        ],
    )


@template("c14_pd_from_i_r", chapter=14, level=2, lo="14h")
def pd_from_i_r(rng):
    R = nice(rng, 20, 50, 100, 220, 470, 1000)
    I_ma = nice(rng, 5, 10, 12, 20, 25, 40, 50)
    V = R * I_ma / 1000
    opts, key, mis = numeric_options(rng, V, [
        (R * I_ma, "You left the current in milliamperes. 1 mA = 0.001 A."),
        (R / (I_ma / 1000), "You divided. V = I × R."),
        (V / 1000, "Check the conversion: mA → A is ÷ 1000, giving a p.d. of a few volts."),
    ], unit="V", sf=3)
    table = md_table(["quantity", "value"], [["resistance of the resistor", f"{R} Ω"], ["current in the resistor", f"{I_ma} mA"]])
    return dict(
        stem=f"A resistor carries a small current.\n\n{table}\n\nWhat is the potential difference across the resistor?",
        options=opts, key=key, misconceptions=mis,
        formula="V = I R, with I in amperes (1 mA = 10⁻³ A)",
        working=[f"I = {I_ma} mA = {fmt(I_ma / 1000)} A", f"V = I R = {fmt(I_ma / 1000)} × {R}", f"= **{fmt(V, sf=3)} V**"],
        hints=[
            "Rearrange R = V ÷ I to find V.",
            "The current is in mA; change it to A before multiplying.",
            f"V = {fmt(I_ma / 1000)} × {R}.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c14_energy_from_pd_charge", chapter=14, level=3, lo="14f")
def energy_from_pd_charge(rng):
    V = nice(rng, 3.0, 6.0, 9.0, 12, 230)
    Q = nice(rng, 5, 10, 20, 25, 40, 60)
    W = V * Q
    opts, key, mis = numeric_options(rng, W, [
        (V / Q, "You divided. P.d. is work done PER coulomb, so work = p.d. × charge."),
        (Q / V, "You divided the charge by the p.d. Work done = V × Q."),
        (V + Q, "Volts × coulombs gives joules. Do not add."),
    ], unit="J", sf=3)
    table = md_table(["quantity", "value"], [["p.d. across the lamp", f"{fmt(V)} V"], ["charge passing through the lamp", f"{Q} C"]])
    return dict(
        stem=f"The p.d. across a component is the work done per unit charge driving charge through it.\n\n{table}\n\nHow much energy is transferred in the lamp by this charge?",
        options=opts, key=key, misconceptions=mis,
        formula="p.d. = work done ÷ charge, so work done (energy transferred) = p.d. × charge  (W = Q V)",
        working=[f"each coulomb transfers {fmt(V)} J", f"W = Q V = {Q} × {fmt(V)}", f"= **{fmt(W, sf=3)} J**"],
        hints=[
            "What does a p.d. of 1 volt mean in terms of joules and coulombs?",
            f"{fmt(V)} V means {fmt(V)} J for every coulomb. How many coulombs pass?",
            f"W = {Q} × {fmt(V)}.",
        ],
    )


@template("c14_resistance_from_iv_graph", chapter=14, level=3, lo="14k")
def resistance_from_iv_graph(rng):
    R = nice(rng, 2.0, 2.5, 4.0, 5.0, 10.0)
    V_read = nice(rng, 2.0, 4.0, 5.0, 6.0)
    I_read = V_read / R
    opts, key, mis = numeric_options(rng, R, [
        (1 / R, "You divided current by p.d. Resistance = p.d. ÷ current (the inverse of the gradient of an I-V graph)."),
        (V_read * I_read, "You multiplied V and I from the graph. Divide V by I."),
        (R * 2, "Check your reading of the graph: pick a point on the line and read both V and I carefully."),
    ], unit="Ω", sf=3)
    return dict(
        stem=f"Fig. 1 shows the I-V graph of a metal wire at constant temperature. Using the graph, what is the resistance of the wire? (For example, read the current when the p.d. is {fmt(V_read)} V.)",
        figure=figs3.iv_graph("ohmic", R=R, vmax=6.0, labels=[(V_read, I_read, "")]),
        options=opts, key=key, misconceptions=mis,
        formula="R = V ÷ I for any point on the line (an ohmic conductor gives a straight line through the origin)",
        working=[f"at V = {fmt(V_read)} V the graph gives I = {fmt(I_read, sf=3)} A", f"R = V ÷ I = {fmt(V_read)} ÷ {fmt(I_read, sf=3)}", f"= **{fmt(R, sf=3)} Ω**"],
        hints=[
            "Choose any point on the line and read off its p.d. and current.",
            f"At {fmt(V_read)} V the current is {fmt(I_read, sf=3)} A.",
            f"R = {fmt(V_read)} ÷ {fmt(I_read, sf=3)}.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c14_wire_length_area", chapter=14, level=4, lo="14i")
def wire_length_area(rng):
    R1 = nice(rng, 2.0, 3.0, 4.0, 6.0, 8.0)
    kL = nice(rng, 2, 3, 4)
    kA = nice(rng, 0.5, 2)
    R2 = R1 * kL / kA
    area_word = "half" if kA == 0.5 else "twice"
    opts, key, mis = numeric_options(rng, R2, [
        (R1 * kL * kA, "Resistance is INVERSELY proportional to the area: a larger area gives a smaller resistance." if kA == 2 else "Halving the area DOUBLES the resistance; you divided instead."),
        (R1 * kL, "You allowed for the length but not for the change in area."),
        (R1 / kA, "You allowed for the area but not for the length."),
    ], unit="Ω", sf=3)
    return dict(
        stem=f"Fig. 1 shows a wire of resistance **{fmt(R1)} Ω**. A second wire of the same material is **{kL} times** as long and has **{area_word}** the cross-sectional area. What is the resistance of the second wire?",
        figure=figs3.wire_sketch("length L", "area A", name=f"wire 1: {fmt(R1)} Ω"),
        options=opts, key=key, misconceptions=mis,
        formula="R ∝ L / A  (resistance proportional to length, inversely proportional to cross-sectional area)",
        working=[f"{kL} times the length → × {kL}", f"{area_word} the area → × {fmt(1 / kA)}", f"R₂ = {fmt(R1)} × {kL} × {fmt(1 / kA)} = **{fmt(R2, sf=3)} Ω**"],
        hints=[
            "How does resistance depend on length? On cross-sectional area?",
            f"Longer wire: more resistance (× {kL}). {area_word.capitalize()} the area: resistance × {fmt(1 / kA)}.",
            f"{fmt(R1)} × {kL} × {fmt(1 / kA)}.",
        ],
    )


@template("c14_lamp_resistance_table", chapter=14, level=4, lo="14k")
def lamp_resistance_table(rng):
    rows = [(1.0, 0.50), (2.0, 0.80), (4.0, 1.20), (6.0, 1.50)]
    scale = nice(rng, 1.0, 0.5, 2.0)
    rows = [(v, round(i * scale, 3)) for v, i in rows]
    (v1, i1), (v2, i2) = rows[0], rows[-1]
    r1, r2 = v1 / i1, v2 / i2
    ratio = r2 / r1
    opts, key, mis = numeric_options(rng, ratio, [
        (1 / ratio, "You have the ratio upside down: the resistance at the higher p.d. is LARGER."),
        (1.0, "The resistance is not constant: a filament lamp is not an ohmic conductor, so R = V/I changes."),
        (v2 / v1, "That is the ratio of the p.d.s. Work out R = V ÷ I at each p.d. first."),
    ], unit="", sf=3)
    table = md_table(["p.d. / V", "current / A"], [[fmt(v), fmt(i, dp=2)] for v, i in rows])
    return dict(
        stem=f"The table shows readings for a filament lamp.\n\n{table}\n\nHow many times greater is the resistance of the lamp at **{fmt(v2)} V** than at **{fmt(v1)} V**?",
        options=opts, key=key, misconceptions=mis,
        formula="R = V ÷ I at each point; the filament's resistance rises as it gets hotter",
        working=[f"at {fmt(v1)} V: R = {fmt(v1)} ÷ {fmt(i1, dp=2)} = {fmt(r1, sf=3)} Ω", f"at {fmt(v2)} V: R = {fmt(v2)} ÷ {fmt(i2, dp=2)} = {fmt(r2, sf=3)} Ω", f"ratio = {fmt(r2, sf=3)} ÷ {fmt(r1, sf=3)} = **{fmt(ratio, sf=3)}**"],
        hints=[
            "Work out the resistance at each of the two p.d.s separately.",
            f"R = V ÷ I: {fmt(v1)} ÷ {fmt(i1, dp=2)} and {fmt(v2)} ÷ {fmt(i2, dp=2)}.",
            "Divide the larger resistance by the smaller.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c14_two_wires_compare", chapter=14, level=5, lo="14i")
def two_wires_compare(rng):
    R1 = nice(rng, 1.0, 1.5, 2.0, 3.0)
    L1, L2 = rng.choice([(1.0, 2.0), (2.0, 3.0), (1.0, 3.0), (0.5, 2.0)])
    d1, d2 = rng.choice([(1.0, 2.0), (2.0, 1.0), (1.0, 0.5), (0.5, 1.0)])
    R2 = R1 * (L2 / L1) * (d1 / d2) ** 2
    opts, key, mis = numeric_options(rng, R2, [
        (R1 * (L2 / L1) * (d1 / d2), "Resistance depends on the cross-sectional AREA, which is proportional to diameter SQUARED."),
        (R1 * (L2 / L1) * (d2 / d1) ** 2, "A thicker wire (larger diameter) has a LOWER resistance: area goes on the bottom."),
        (R1 * (L1 / L2) * (d1 / d2) ** 2, "A longer wire has a HIGHER resistance: length goes on top."),
    ], unit="Ω", sf=3)
    table = md_table(["wire", "length / m", "diameter / mm", "resistance / Ω"], [["X", fmt(L1), fmt(d1), fmt(R1)], ["Y", fmt(L2), fmt(d2), "?"]])
    return dict(
        stem=f"Two wires X and Y are made of the same metal at the same temperature.\n\n{table}\n\nWhat is the resistance of wire Y?",
        options=opts, key=key, misconceptions=mis,
        formula="R ∝ L / A and A ∝ d², so R₂ = R₁ × (L₂/L₁) × (d₁/d₂)²",
        working=[f"length factor = {fmt(L2)} ÷ {fmt(L1)} = {fmt(L2 / L1)}", f"area factor: diameter ratio {fmt(d1)}/{fmt(d2)}, so resistance × ({fmt(d1)}/{fmt(d2)})² = {fmt((d1 / d2) ** 2)}", f"R = {fmt(R1)} × {fmt(L2 / L1)} × {fmt((d1 / d2) ** 2)} = **{fmt(R2, sf=3)} Ω**"],
        hints=[
            "Deal with the length and the thickness separately. Thickness is given as a diameter, but resistance depends on the AREA.",
            "Area ∝ diameter². Doubling the diameter gives four times the area and a quarter of the resistance.",
            f"R = {fmt(R1)} × ({fmt(L2)}/{fmt(L1)}) × ({fmt(d1)}/{fmt(d2)})².",
        ],
    )


@template("c14_electrons_per_second", chapter=14, level=5, lo="14a")
def electrons_per_second(rng):
    I = nice(rng, 0.16, 0.32, 0.48, 0.80, 1.6)
    n = I / E
    opts, key, mis = numeric_options(rng, n, [
        (I * E, "You multiplied the current by the electron charge. Number per second = charge per second ÷ charge per electron."),
        (n / 60, "The current already tells you the charge per SECOND; no time conversion is needed."),
        (n * 10, "Check the powers of ten when dividing by 1.6 × 10⁻¹⁹."),
    ], unit="", sf=2)
    table = md_table(["quantity", "value"], [["current in the wire", f"{fmt(I)} A"], ["charge of one electron", "1.6 × 10⁻¹⁹ C"]])
    return dict(
        stem=f"Current is the rate of flow of charge.\n\n{table}\n\nHow many electrons pass a point in the wire each second?",
        options=opts, key=key, misconceptions=mis,
        formula="charge per second = I; number of electrons per second = I ÷ e",
        working=[f"charge passing per second = {fmt(I)} C", f"number of electrons = {fmt(I)} ÷ (1.6 × 10⁻¹⁹)", f"= **{fmt(n, sf=2)}** per second"],
        hints=[
            f"A current of {fmt(I)} A means {fmt(I)} coulombs pass every second.",
            "Each electron carries 1.6 × 10⁻¹⁹ C. How many make up that charge?",
            f"{fmt(I)} ÷ 1.6 × 10⁻¹⁹.",
        ],
    )
