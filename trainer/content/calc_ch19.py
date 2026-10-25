"""Chapter 19 Electromagnetic Induction (6091): transformer equations (ideal), turns ratios, input/output current, a.c. output graphs,
induced e.m.f. factors and direction, power loss in transmission cables."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template, text_options


# ---------------------------------------------------------------- L1
@template("c19_secondary_voltage", chapter=19, level=1, lo="19e")
def secondary_voltage(rng):
    Vp = nice(rng, 230, 240, 120, 12)
    Np, Ns = rng.choice([(1000, 50), (2000, 100), (500, 2500), (400, 1200), (1200, 60), (100, 500)])
    Vs = Vp * Ns / Np
    opts, key, mis = numeric_options(rng, Vs, [
        (Vp * Np / Ns, "You have the turns ratio upside down: Vs / Vp = Ns / Np."),
        (Vp, "The output equals the input only when the two coils have the same number of turns."),
        (Vp * Ns, "Multiply by the RATIO Ns/Np, not by Ns alone."),
    ], unit="V", sf=3)
    return dict(
        stem=f"Fig. 1 shows an ideal transformer. The primary coil has **{Np} turns** and is connected to a **{Vp} V** a.c. supply. The secondary coil has **{Ns} turns**. What is the output p.d.?",
        figure=figs3.transformer(f"{Np} turns", f"{Ns} turns", f"{Vp} V", "Vs = ?", n_p=6 if Np > Ns else 4, n_s=4 if Np > Ns else 12),
        options=opts, key=key, misconceptions=mis,
        formula="Vs / Vp = Ns / Np",
        working=["Vs = Vp × Ns ÷ Np", f"= {Vp} × {Ns} ÷ {Np}", f"= **{fmt(Vs, sf=3)} V**"],
        hints=["Which equation links the voltages and the numbers of turns?", "Vs/Vp = Ns/Np. Rearrange for Vs.", f"Vs = {Vp} × {Ns}/{Np}."],
    )


@template("c19_step_up_or_down", chapter=19, level=1, lo="19d")
def step_up_or_down(rng):
    Np, Ns = rng.choice([(200, 1000), (1000, 50), (300, 900), (2400, 120), (500, 2000), (1500, 75)])
    up = Ns > Np
    ans = "step-up, because the secondary has more turns than the primary" if up else "step-down, because the secondary has fewer turns than the primary"
    wrongs = {("step-down, because the secondary has more turns than the primary" if up else "step-up, because the secondary has fewer turns than the primary"):
              "More turns on the SECONDARY steps the voltage UP; fewer turns steps it down.",
              ("step-up, because the primary has more turns" if up else "step-down, because the primary has fewer turns"): "Compare the secondary with the primary: the voltage changes in the same ratio as the turns.",
              "neither: a transformer never changes the voltage": "Changing the voltage is exactly what a transformer is for."}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["coil", "number of turns"], [["primary", Np], ["secondary", Ns]])
    return dict(
        stem=f"The table gives the numbers of turns on the coils of a transformer.\n\n{table}\n\nWhat type of transformer is it?",
        options=opts, key=key, misconceptions=mis,
        formula="Vs/Vp = Ns/Np: Ns > Np steps the voltage up; Ns < Np steps it down",
        working=[f"Ns = {Ns}, Np = {Np}", f"Ns {'>' if up else '<'} Np, so Vs {'>' if up else '<'} Vp", f"**{ans.split(',')[0]}**"],
        hints=["Compare the secondary turns with the primary turns.", "The voltage ratio equals the turns ratio.", "More secondary turns = step-up."],
    )


# ---------------------------------------------------------------- L2
@template("c19_turns_needed", chapter=19, level=2, lo="19e")
def turns_needed(rng):
    Vp = nice(rng, 230, 240)
    Vs = nice(rng, 6, 12, 24, 46, 115)
    Np = nice(rng, 920, 1150, 2300, 4600) if Vp == 230 else nice(rng, 960, 1200, 2400, 4800)
    Ns = Np * Vs / Vp
    opts, key, mis = numeric_options(rng, Ns, [
        (Np * Vp / Vs, "You have the ratio upside down: Ns = Np × Vs ÷ Vp."),
        (Np - Vs, "The turns are in the RATIO of the voltages; you cannot subtract a voltage from a number of turns."),
        (Vs, "That is the output voltage, not a number of turns."),
    ], unit="turns", sf=3)
    table = md_table(["", "value"], [["supply p.d.", f"{Vp} V"], ["required output p.d.", f"{Vs} V"], ["primary turns", Np]])
    return dict(
        stem=f"A transformer is needed to run a {Vs} V device from the mains.\n\n{table}\n\nHow many turns are needed on the secondary coil?",
        options=opts, key=key, misconceptions=mis,
        formula="Ns / Np = Vs / Vp  →  Ns = Np × Vs ÷ Vp",
        working=["Ns = Np × Vs ÷ Vp", f"= {Np} × {Vs} ÷ {Vp}", f"= **{fmt(Ns, sf=3)} turns**"],
        hints=["Use the transformer equation with the unknown on the secondary side.", "Ns/Np = Vs/Vp.", f"Ns = {Np} × {Vs}/{Vp}."],
    )


@template("c19_ac_frequency_from_graph", chapter=19, level=2, lo="19c")
def ac_frequency_from_graph(rng):
    T_ms = nice(rng, 10, 20, 25, 40, 50)
    Vpk = nice(rng, 4.0, 6.0, 8.0, 10.0)
    f = 1000 / T_ms
    opts, key, mis = numeric_options(rng, f, [
        (T_ms, "That is the period in milliseconds. Frequency = 1 ÷ period, with the period in seconds."),
        (1 / T_ms, "You used the period in ms. Change it to seconds first (÷ 1000)."),
        (f / 2, "One complete cycle includes both a positive and a negative half; read the period as the time for a FULL cycle."),
    ], unit="Hz", sf=3)
    return dict(
        stem="Fig. 1 shows the output of a simple a.c. generator. What is the frequency of the output?",
        figure=figs3.ac_output(period=T_ms / 1000, vpeak=Vpk),
        options=opts, key=key, misconceptions=mis,
        formula="frequency = 1 ÷ period (period in seconds = time for one complete cycle)",
        working=[f"one complete cycle takes {T_ms} ms = {fmt(T_ms / 1000)} s", f"f = 1 ÷ {fmt(T_ms / 1000)}", f"= **{fmt(f, sf=3)} Hz**"],
        hints=["Read the time for ONE complete cycle (up, down and back to the start).", f"That period is {T_ms} ms. Convert to seconds.", "f = 1/T."],
    )


# ---------------------------------------------------------------- L3
@template("c19_primary_current_ideal", chapter=19, level=3, lo="19e")
def primary_current_ideal(rng):
    Vp = nice(rng, 230, 240)
    Vs = nice(rng, 12, 24, 6)
    Is = nice(rng, 2.0, 2.5, 4.0, 5.0)
    Ip = Vs * Is / Vp
    opts, key, mis = numeric_options(rng, Ip, [
        (Is, "The currents are not the same: in an ideal transformer the POWER is the same on both sides (Vp Ip = Vs Is)."),
        (Vp * Is / Vs, "You have the ratio upside down. A step-down transformer has a SMALLER current in the primary."),
        (Vs * Is, "That is the power in watts. Divide by the primary p.d. to find the primary current."),
    ], unit="A", sf=3)
    return dict(
        stem=f"Fig. 1 shows an ideal transformer connected to the **{Vp} V** mains. It supplies **{Vs} V** to a lamp that takes a current of **{fmt(Is)} A**. What is the current in the primary coil?",
        figure=figs3.transformer("Np", "Ns", f"{Vp} V", f"{Vs} V", n_p=8, n_s=3),
        options=opts, key=key, misconceptions=mis,
        formula="ideal transformer: power in = power out, Vp Ip = Vs Is",
        working=[f"power out = Vs Is = {Vs} × {fmt(Is)} = {fmt(Vs * Is)} W", f"Ip = power ÷ Vp = {fmt(Vs * Is)} ÷ {Vp}", f"= **{fmt(Ip, sf=3)} A**"],
        hints=["An ideal transformer wastes no energy. What is the same on both sides?", "Vp Ip = Vs Is.", f"Ip = {Vs} × {fmt(Is)} ÷ {Vp}."],
    )


@template("c19_emf_factor_table", chapter=19, level=3, lo="19a")
def emf_factor_table(rng):
    base_speed = nice(rng, 1.0, 2.0)
    base_turns = nice(rng, 100, 200)
    rows = [("P", base_speed, base_turns, "weak"), ("Q", 2 * base_speed, base_turns, "weak"), ("R", base_speed, 2 * base_turns, "weak"), ("S", 2 * base_speed, 2 * base_turns, "strong")]
    rng.shuffle(rows)
    ans = "S"
    wrongs = {r[0]: f"Trial {r[0]} has a {'slower' if r[1] == base_speed else 'faster'} magnet, {'fewer' if r[2] == base_turns else 'more'} turns and a {r[3]} magnet; trial S is better on every factor." for r in rows if r[0] != "S"}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["trial", "speed of magnet / m/s", "turns on coil", "magnet"], [[r[0], fmt(r[1]), r[2], r[3]] for r in rows])
    return dict(
        stem=f"A magnet is pushed into a coil connected to a galvanometer. The table shows four trials.\n\n{table}\n\nIn which trial is the induced e.m.f. largest?",
        options=opts, key=key, misconceptions=mis,
        formula="the induced e.m.f. is larger when the magnetic field through the coil changes faster: faster motion, more turns, stronger magnet",
        working=["e.m.f. increases with speed, number of turns and magnet strength", "trial S is fastest, has the most turns and the strongest magnet", "**S**"],
        hints=["Which three factors increase the induced e.m.f.?", "Speed of movement, number of turns, strength of the magnet.", "Find the trial that maximises all three."],
    )


# ---------------------------------------------------------------- L4
@template("c19_cable_power_loss", chapter=19, level=4, lo="19f")
def cable_power_loss(rng):
    P_mw = nice(rng, 10, 20, 50, 100)
    V_kv = nice(rng, 25, 50, 132, 275, 400)
    R = nice(rng, 2.0, 4.0, 5.0, 10.0)
    I = P_mw * 1e6 / (V_kv * 1e3)
    loss = I * I * R
    opts, key, mis = numeric_options(rng, loss, [
        (I * R, "That is the p.d. across the cables (V = IR), not the power lost. Power lost = I² R."),
        (P_mw * 1e6 * R / (V_kv * 1e3), "You used I R × (P/V)/R in a muddled way; find I = P ÷ V first, then I² R."),
        ((V_kv * 1e3) ** 2 / R, "That uses the transmission voltage, but most of that p.d. is across the consumers, not the cables. Use I² R with the cable current."),
    ], unit="W", sf=3)
    table = md_table(["quantity", "value"], [["power transmitted", f"{P_mw} MW"], ["transmission p.d.", f"{V_kv} kV"], ["total resistance of the cables", f"{fmt(R)} Ω"]])
    return dict(
        stem=f"Fig. 1 shows electrical energy being transmitted from a power station.\n\n{table}\n\nWhat power is lost as thermal energy in the cables?",
        figure=figs3.transmission([f"power = {P_mw} MW", f"voltage = {V_kv} kV", f"cable resistance = {fmt(R)} Ω"]),
        options=opts, key=key, misconceptions=mis,
        formula="current in cables I = P ÷ V; power lost in cables = I² R",
        working=[f"I = P ÷ V = {P_mw} × 10⁶ ÷ ({V_kv} × 10³) = {fmt(I, sf=3)} A", f"power lost = I² R = {fmt(I, sf=3)}² × {fmt(R)}", f"= **{fmt(loss, sf=3)} W**"],
        hints=["First find the current in the cables from the power and the transmission p.d.", "The heating in the cables depends on the current and their resistance.", "Power lost = I² R."],
    )


@template("c19_loss_ratio_voltage", chapter=19, level=4, lo="19f")
def loss_ratio_voltage(rng):
    k = nice(rng, 2, 4, 5, 10)
    V1 = nice(rng, 11, 25, 33)
    opts, key, mis = numeric_options(rng, k * k, [
        (k, f"Raising the voltage {k} times reduces the CURRENT {k} times, but the power lost depends on I², so it falls {k * k} times."),
        (1 / k, "The loss becomes smaller, so the factor it is DIVIDED by is greater than 1."),
        (2 * k, "Power lost ∝ I², so the factor is the square of the current factor."),
    ], unit="", sf=3)
    table = md_table(["", "transmission p.d."], [["before", f"{V1} kV"], ["after", f"{V1 * k} kV"]])
    return dict(
        stem=f"The same power is transmitted through the same cables at a higher p.d.\n\n{table}\n\nBy what factor is the power lost in the cables reduced?",
        options=opts, key=key, misconceptions=mis,
        formula="for the same power, I = P ÷ V, so I falls by the same factor as V rises; power lost = I² R falls by that factor squared",
        working=[f"V × {k} → I ÷ {k}", f"power lost = I² R → ÷ {k}²", f"reduced by a factor of **{k * k}**"],
        hints=["For a fixed power, how does the current depend on the transmission p.d.?", f"Raising V {k} times divides I by {k}.", "Power lost depends on I squared."],
    )


# ---------------------------------------------------------------- L5
@template("c19_transformer_efficiency", chapter=19, level=5, lo="19e")
def transformer_efficiency(rng):
    Vp, Ip = nice(rng, 230, 240), nice(rng, 0.40, 0.50, 0.80, 1.0)
    Vs = nice(rng, 12, 24)
    eff = nice(rng, 0.80, 0.85, 0.90, 0.95)
    Is = round(Vp * Ip * eff / Vs, 2)
    actual = Vs * Is / (Vp * Ip) * 100
    opts, key, mis = numeric_options(rng, actual, [
        (100, "Real transformers waste some energy (heating of the coils and core), so the efficiency is below 100%."),
        (Vp * Ip / (Vs * Is) * 100, "You divided input by output. Efficiency = output power ÷ input power × 100%."),
        (Vs / Vp * 100, "Efficiency compares POWERS (V × I), not just the voltages."),
    ], unit="%", sf=3)
    table = md_table(["", "p.d. / V", "current / A"], [["primary", Vp, fmt(Ip)], ["secondary", Vs, fmt(Is)]])
    return dict(
        stem=f"Measurements on a real transformer are shown.\n\n{table}\n\nWhat is the efficiency of the transformer?",
        options=opts, key=key, misconceptions=mis,
        formula="efficiency = output power (Vs Is) ÷ input power (Vp Ip) × 100%",
        working=[f"input = {Vp} × {fmt(Ip)} = {fmt(Vp * Ip)} W;  output = {Vs} × {fmt(Is)} = {fmt(Vs * Is)} W", f"efficiency = {fmt(Vs * Is)} ÷ {fmt(Vp * Ip)} × 100", f"= **{fmt(actual, sf=3)}%**"],
        hints=["Work out the power on each side: P = V I.", "Efficiency = useful output ÷ input.", "Multiply by 100 for a percentage."],
    )


@template("c19_galvanometer_direction", chapter=19, level=5, lo="19a")
def galvanometer_direction(rng):
    pole = rng.choice(["N", "S"])
    move = rng.choice(["in", "out"])
    first = rng.choice(["left", "right"])
    other = "right" if first == "left" else "left"
    case = rng.choice(["pulled out", "turned round and pushed in", "held still inside the coil"])
    if case == "held still inside the coil":
        ans = "no deflection"
    else:
        ans = f"to the {other}"
    wrongs = {}
    if ans == "no deflection":
        wrongs = {f"to the {first}": "With no relative movement the magnetic field through the coil is not changing, so no e.m.f. is induced.",
                  f"to the {other}": "An e.m.f. is induced only while the field through the coil is CHANGING.",
                  "a steady deflection to the left and right in turn": "A stationary magnet produces no change, so no deflection at all."}
    else:
        wrongs = {f"to the {first}": "Reversing EITHER the direction of motion OR the pole reverses the induced current (Lenz's law: the induced current opposes the change).",
                  "no deflection": "The magnet is moving relative to the coil, so the field through the coil is changing and an e.m.f. is induced.",
                  "a larger deflection in the same direction": "Reversing the motion or the pole reverses the direction of the induced current; its size depends on the speed."}
    opts, key, mis = text_options(rng, ans, wrongs)
    m2 = {"pulled out": "pulled out of the coil", "turned round and pushed in": f"turned round so that its {'S' if pole == 'N' else 'N'} pole enters first, and pushed in", "held still inside the coil": "held still inside the coil"}[case]
    return dict(
        stem=f"Fig. 1 shows the {pole} pole of a magnet being pushed into a coil. The galvanometer needle deflects to the **{first}**. The magnet is then {m2} at the same speed. What does the galvanometer needle do?",
        figure=figs3.magnet_into_coil("in", pole=pole),
        options=opts, key=key, misconceptions=mis,
        formula="an e.m.f. is induced only while the field through the coil changes; reversing the motion or the pole reverses the induced current (it opposes the change)",
        working=[f"first: {pole} pole pushed in → deflection to the {first}", f"now: {case}", f"→ **{ans}**"],
        hints=["Is the magnetic field through the coil changing in the new situation?", "If it is, has the motion or the pole been reversed (once) compared with the first case?", "One reversal → opposite deflection; no change → no deflection."],
    )
