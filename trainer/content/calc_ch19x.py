"""Chapter 19 Electromagnetic Induction (6091) bank extension: transformer equations, a.c. output graphs, induced e.m.f. factors and
direction, generators and transmission, 10 per level, each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025:
magnets and coils with galvanometers, simple a.c. generators and their output traces, phone chargers and mains transformers,
the National Grid; school papers 2024-2025)."""
import math

from .. import figs3
from .base import fmt, md_table, mk, mkt, nice, template


# ================================================================== L1
@template("c19x_secondary_table", chapter=19, level=1, lo="19e")
def secondary_table(rng):
    Vp = nice(rng, 12, 24, 230, 240)
    Np, Ns = rng.choice([(200, 50), (400, 100), (100, 400), (300, 600), (500, 100), (240, 60)])
    Vs = Vp * Ns / Np
    table = md_table(["", "primary", "secondary"], [["number of turns", Np, Ns], ["p.d. / V", Vp, "?"]])
    return mk(rng, Vs, [(Vp * Np / Ns, "Upside down: Vs = Vp × Ns ÷ Np."), (Vp, "The p.d. changes unless the two coils have equal turns."),
                        (Ns / Np, "That is only the turns ratio; multiply it by the primary p.d.")],
              "V", f"The table gives data for an ideal transformer.\n\n{table}\n\nWhat is the secondary p.d.?",
              "Vs / Vp = Ns / Np", ["Vs = Vp × Ns ÷ Np", f"= {Vp} × {Ns} ÷ {Np}", f"= **{fmt(Vs, sf=3)} V**"],
              ["Which equation links the p.d.s and the turns?", "Vs/Vp = Ns/Np.", f"Vs = {Vp} × {Ns}/{Np}."])


@template("c19x_core_material_table", chapter=19, level=1, lo="19d")
def core_material_table(rng):
    labels = ["P", "Q", "R", "S"]
    rng.shuffle(labels)
    rows = [(labels[0], "yes", "yes", "yes"), (labels[1], "yes", "no", "no"), (labels[2], "yes", "yes", "no"), (labels[3], "no", "no", "—")]
    ans = labels[0]
    wrongs = {labels[1]: "This material keeps its magnetism, so energy is wasted each time the field reverses.",
              labels[2]: "The core must also LOSE its magnetism easily, because the a.c. reverses the field many times a second.",
              labels[3]: "A non-magnetic core cannot carry the changing magnetic field from the primary to the secondary."}
    table = md_table(["material", "magnetic?", "magnetised easily?", "loses magnetism easily?"], sorted([list(r) for r in rows]))
    return mkt(rng, ans, wrongs, f"The table describes four materials.\n\n{table}\n\nWhich material is the best for the core of a transformer?",
               "a transformer core must be magnetised and demagnetised easily (soft iron)",
               [f"material {ans} is magnetic, magnetised easily and loses its magnetism easily → **{ans}** (soft iron)"],
               ["What does the core have to do?", "Carry a field that reverses many times a second.", "It must magnetise and demagnetise easily."])


@template("c19x_emf_speed_scale", chapter=19, level=1, lo="19a")
def emf_speed_scale(rng):
    v = nice(rng, 0.5, 1.0, 1.5, 2.0)
    E = nice(rng, 2.0, 3.0, 4.0, 5.0)
    k = nice(rng, 2, 3)
    table = md_table(["trial", "speed of magnet / m/s", "maximum e.m.f. / mV"], [["1", fmt(v), fmt(E)], ["2", fmt(k * v), "?"]])
    return mk(rng, E * k, [(E, "Moving the magnet faster makes the field through the coil change faster, so the e.m.f. increases."),
                           (E / k, "A faster magnet gives a LARGER e.m.f., not a smaller one."), (E * k * k, "The e.m.f. is proportional to the speed, not to the speed squared.")],
              "mV", f"A magnet is pushed into the same coil at two speeds. The induced e.m.f. is proportional to the speed.\n\n{table}\n\nWhat is the maximum e.m.f. in trial 2?",
              "induced e.m.f. ∝ speed of the magnet", [f"speed × {k} → e.m.f. × {k}", f"= {fmt(E)} × {k} = **{fmt(E * k)} mV**"],
              ["How many times faster is trial 2?", f"{k} times.", "The e.m.f. goes up by the same factor."])


@template("c19x_zero_reading_stage", chapter=19, level=1, lo="19a")
def zero_reading_stage(rng):
    pole = rng.choice(["N", "S"])
    actions = [f"{pole} pole pushed into the coil", "magnet held still inside the coil", "magnet pulled out of the coil", f"{pole} pole pushed in more quickly"]
    rng.shuffle(actions)
    k = actions.index("magnet held still inside the coil")
    ans = f"stage {k + 1}"
    wrongs = {f"stage {i + 1}": "The magnet is moving here, so the field through the coil is changing and an e.m.f. is induced." for i in range(4) if i != k}
    table = md_table(["stage", "what happens"], [[i + 1, a] for i, a in enumerate(actions)])
    return mkt(rng, ans, wrongs, f"A magnet and a coil connected to a galvanometer are used in four stages.\n\n{table}\n\nAt which stage is the galvanometer reading zero?",
               "an e.m.f. is induced only while the magnetic field through the coil changes",
               [f"stage {k + 1}: magnet stationary → no change in the field → **no e.m.f.**"],
               ["When is an e.m.f. induced?", "Only while the field through the coil changes.", "Find the stage with no movement."])


@template("c19x_ac_peak_read", chapter=19, level=1, lo="19c")
def ac_peak_read(rng):
    T = nice(rng, 10, 20, 40)
    V = nice(rng, 3.0, 4.0, 6.0, 8.0)
    return mk(rng, V, [(2 * V, "That is the peak-to-peak value. The peak is measured from zero."), (V / 2, "Read the highest point of the curve on the e.m.f. axis."),
                       (T, "That is the period in ms, read from the time axis.")],
              "V", "Fig. 1 shows the output of a simple a.c. generator. What is the peak e.m.f.?",
              "peak e.m.f. = highest value of the curve measured from zero", [f"highest point of the curve: **{fmt(V)} V**"],
              ["Which axis shows the e.m.f.?", "Find the highest point of the curve.", "Measure from zero, not from the lowest point."],
              figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_ac_period_read", chapter=19, level=1, lo="19c")
def ac_period_read(rng):
    T = nice(rng, 10, 20, 40, 50)
    V = nice(rng, 4.0, 6.0, 10.0)
    return mk(rng, T, [(T / 2, "That is half a cycle. One complete cycle has a positive AND a negative half."), (2 * T, "The graph shows two cycles; the period is the time for ONE."),
                       (1000 / T, "That is the frequency in Hz, not the period.")],
              "ms", "Fig. 1 shows the e.m.f. from a simple a.c. generator. What is the period of the output?",
              "period = time for one complete cycle", [f"one complete cycle (up, down and back to the start) takes **{T} ms**"],
              ["What is one complete cycle?", "Up, down and back to the starting point.", "Read the time it takes."],
              figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_cable_current", chapter=19, level=1, lo="19f")
def cable_current(rng):
    P = nice(rng, 10, 20, 50, 100)
    V = nice(rng, 100, 200, 250, 400, 500)
    I = P * 1e6 / (V * 1e3)
    return mk(rng, I, [(P / V, "Convert MW to W (× 10⁶) and kV to V (× 10³) first."), (I * 1000, "Check the powers of ten: mega = 10⁶ and kilo = 10³."),
                       (V * 1e3 / (P * 1e6), "Upside down: I = P ÷ V.")],
              "A", f"Fig. 1 shows a power station sending **{P} MW** of power along cables at **{V} kV**. What is the current in the cables?",
              "P = V I  →  I = P ÷ V", [f"I = {P} × 10⁶ ÷ ({V} × 10³)", f"= **{fmt(I, sf=3)} A**"],
              ["Which equation links power, p.d. and current?", "P = VI.", "Convert to W and V before dividing."],
              figure=figs3.transmission([f"power = {P} MW", f"transmission p.d. = {V} kV"]))


@template("c19x_step_up_stage", chapter=19, level=1, lo="19f")
def step_up_stage(rng):
    gen = nice(rng, 11, 22, 25)
    grid = nice(rng, 275, 400)
    local = nice(rng, 11, 33)
    labels = ["W", "X", "Y"]
    rng.shuffle(labels)
    rows = [(labels[0], f"{gen} kV", f"{grid} kV"), (labels[1], f"{grid} kV", f"{local} kV"), (labels[2], f"{local} kV", "230 V")]
    ans = labels[0]
    wrongs = {labels[1]: f"Transformer {labels[1]} lowers the p.d., so it is step-down.", labels[2]: f"Transformer {labels[2]} lowers the p.d. for homes, so it is step-down.",
              "none of them": "A transformer whose output p.d. is larger than its input is step-up."}
    table = md_table(["transformer", "input p.d.", "output p.d."], sorted([list(r) for r in rows]))
    return mkt(rng, ans, wrongs, f"The table shows three transformers in a transmission system.\n\n{table}\n\nWhich transformer is a step-up transformer?",
               "step-up: output p.d. > input p.d.", [f"{ans}: {gen} kV → {grid} kV, the p.d. increases → **{ans}**"],
               ["Compare the output p.d. with the input p.d.", "Step-up raises the p.d.", "Find the one that increases."])


# ================================================================== L2
@template("c19x_primary_turns", chapter=19, level=2, lo="19e")
def primary_turns(rng):
    Vp, Vs, Ns = rng.choice([(230, 23, 100), (240, 12, 60), (230, 46, 200), (240, 24, 150), (230, 11.5, 50), (240, 6, 40)])
    Np = Ns * Vp / Vs
    return mk(rng, Np, [(Ns * Vs / Vp, "Upside down: Np = Ns × Vp ÷ Vs."), (Ns * Vp, "Multiply by the RATIO Vp/Vs, not by Vp alone."),
                        (Vp / Vs, "That is the voltage ratio; multiply it by the secondary turns.")],
              "turns", f"Fig. 1 shows an ideal transformer that steps **{Vp} V** down to **{fmt(Vs)} V**. The secondary coil has **{Ns} turns**. How many turns are on the primary coil?",
              "Np / Ns = Vp / Vs", ["Np = Ns × Vp ÷ Vs", f"= {Ns} × {Vp} ÷ {fmt(Vs)}", f"= **{fmt(Np, sf=3)} turns**"],
              ["Write the transformer equation.", "Np/Ns = Vp/Vs.", f"Np = {Ns} × {Vp}/{fmt(Vs)}."],
              figure=figs3.transformer("Np = ?", f"{Ns} turns", f"{Vp} V", f"{fmt(Vs)} V", n_p=9, n_s=3))


@template("c19x_period_from_freq", chapter=19, level=2, lo="19c")
def period_from_freq(rng):
    f = nice(rng, 25, 40, 50, 60, 100)
    T = 1000 / f
    table = md_table(["quantity", "value"], [["frequency of the a.c. output", f"{f} Hz"], ["peak e.m.f.", f"{nice(rng, 6, 9, 12)} V"]])
    return mk(rng, T, [(1 / f, "That is the period in seconds; the question asks for milliseconds."), (f, "That is the frequency, not the period."),
                       (T / 2, "That is the time for half a cycle.")],
              "ms", f"A generator produces an alternating e.m.f.\n\n{table}\n\nWhat is the time for one complete cycle?",
              "T = 1 ÷ f", [f"T = 1 ÷ {f} = {fmt(1 / f, sf=3)} s", f"= **{fmt(T, sf=3)} ms**"],
              ["How are period and frequency related?", "T = 1/f.", "Convert seconds to milliseconds (× 1000)."])


@template("c19x_generator_rev_freq", chapter=19, level=2, lo="19b")
def generator_rev_freq(rng):
    R = nice(rng, 600, 1200, 1500, 1800, 3000, 3600)
    f = R / 60
    table = md_table(["quantity", "value"], [["rotation of the coil", f"{R} revolutions per minute"], ["number of turns on the coil", nice(rng, 50, 100, 200)]])
    return mk(rng, f, [(R, "Revolutions per MINUTE are not hertz. Divide by 60 to get revolutions per second."), (R / 30, "Each revolution of the coil gives ONE complete cycle, not two."),
                       (60 / R, "Upside down: revolutions per second = revolutions per minute ÷ 60.")],
              "Hz", f"The coil of a simple a.c. generator rotates steadily.\n\n{table}\n\nWhat is the frequency of the a.c. output?",
              "one revolution = one cycle, so f = revolutions per second", [f"f = {R} ÷ 60", f"= **{fmt(f, sf=3)} Hz**"],
              ["How many cycles does one revolution give?", "One.", "Convert revolutions per minute to per second."])


@template("c19x_generator_faster", chapter=19, level=2, lo="19b")
def generator_faster(rng):
    V0 = nice(rng, 4, 5, 6, 8)
    f0 = nice(rng, 10, 20, 25, 50)
    k = nice(rng, 2, 3)
    ans = f"peak e.m.f. {k * V0} V, frequency {k * f0} Hz"
    wrongs = {f"peak e.m.f. {V0} V, frequency {k * f0} Hz": "Turning faster also makes the field through the coil change faster, so the peak e.m.f. rises too.",
              f"peak e.m.f. {k * V0} V, frequency {f0} Hz": "More revolutions per second means more cycles per second: the frequency rises.",
              f"peak e.m.f. {k * V0} V, frequency {fmt(f0 / k)} Hz": "A faster coil gives a HIGHER frequency (shorter period)."}
    table = md_table(["", "peak e.m.f. / V", "frequency / Hz"], [["before", V0, f0], ["after", "?", "?"]])
    return mkt(rng, ans, wrongs, f"The coil of a simple a.c. generator is turned {k} times as fast.\n\n{table}\n\nWhat are the new peak e.m.f. and frequency?",
               "faster rotation → larger peak e.m.f. AND higher frequency (both ∝ speed)", [f"both × {k}: **{ans}**"],
               ["What happens to the number of cycles per second?", "It goes up with the speed.", "The field also changes faster, so the e.m.f. rises."])


@template("c19x_emf_turns_scale", chapter=19, level=2, lo="19a")
def emf_turns_scale(rng):
    N1 = nice(rng, 100, 200, 250)
    m = nice(rng, 2, 3, 4)
    E1 = nice(rng, 1.5, 2.0, 2.5, 3.0)
    table = md_table(["coil", "number of turns", "maximum e.m.f. / mV"], [["A", N1, fmt(E1)], ["B", m * N1, "?"]])
    return mk(rng, m * E1, [(E1, "More turns means more of the coil is linked by the changing field, so the e.m.f. is larger."),
                            (E1 / m, "More turns give a LARGER e.m.f."), (m * m * E1, "The e.m.f. is proportional to the number of turns, not its square.")],
              "mV", f"The same magnet is pushed at the same speed into two coils. The e.m.f. is proportional to the number of turns.\n\n{table}\n\nWhat is the maximum e.m.f. for coil B?",
              "induced e.m.f. ∝ number of turns", [f"turns × {m} → e.m.f. × {m}", f"= **{fmt(m * E1)} mV**"],
              ["How many times more turns does B have?", f"{m} times.", "Multiply the e.m.f. by the same factor."])


@template("c19x_galv_pulled_out", chapter=19, level=2, lo="19a")
def galv_pulled_out(rng):
    pole = rng.choice(["N", "S"])
    first = rng.choice(["left", "right"])
    other = "right" if first == "left" else "left"
    ans = f"to the {other}"
    wrongs = {f"to the {first}": "Pulling the magnet out reverses the change in the field, so the induced current reverses.",
              "no deflection": "The magnet is moving, so the field through the coil is changing and an e.m.f. is induced.",
              f"to the {other}, and it stays there after the magnet has left": "The current flows only while the field is changing; the needle returns to zero."}
    return mkt(rng, ans, wrongs, f"When the {pole} pole of a magnet is pushed into a coil, the galvanometer needle deflects to the **{first}**. Fig. 1 shows the magnet being pulled out at the same speed. What does the needle do while the magnet moves out?",
               "reversing the motion reverses the induced current", [f"in → {first}; out → **{ans}**"],
               ["What has been reversed?", "The direction of motion.", "One reversal → opposite deflection."],
               figure=figs3.magnet_into_coil("out", pole=pole))


@template("c19x_cable_current_ratio", chapter=19, level=2, lo="19f")
def cable_current_ratio(rng):
    V1 = nice(rng, 11, 25, 33)
    k = nice(rng, 4, 5, 10)
    table = md_table(["", "transmission p.d. / kV"], [["system 1", V1], ["system 2", V1 * k]])
    return mk(rng, k, [(k * k, "That is the factor for the POWER LOST. The current falls by the voltage factor."), (1 / k, "The current is smaller, so it is divided by a number greater than 1."),
                       (V1 * k - V1, "Compare the p.d.s as a ratio, not a difference.")],
              "", f"The same power is sent along the same cables by two systems.\n\n{table}\n\nHow many times smaller is the current in system 2?",
              "same power: I = P ÷ V, so I ∝ 1/V", [f"p.d. × {k} → current ÷ {k}", f"**{k} times smaller**"],
              ["For a fixed power, how does I depend on V?", "I = P/V.", f"V rises {k} times."])


@template("c19x_cable_loss_simple", chapter=19, level=2, lo="19f")
def cable_loss_simple(rng):
    I = nice(rng, 50, 100, 200, 250)
    R = nice(rng, 2, 4, 5, 8)
    return mk(rng, I * I * R, [(I * R, "That is the p.d. across the cables (V = IR). Power lost = I² R."), (I * I / R, "Multiply by R; do not divide."),
                               (I * R * R, "Square the current, not the resistance.")],
              "W", f"Fig. 1 shows a transmission system. The current in the cables is **{I} A** and their total resistance is **{R} Ω**. What power is lost as heat in the cables?",
              "power lost = I² R", [f"P = {I}² × {R}", f"= **{fmt(I * I * R, sf=3)} W**"],
              ["What causes the power loss?", "Heating of the resistance of the cables.", "P = I²R."],
              figure=figs3.transmission([f"current in cables = {I} A", f"cable resistance = {R} Ω"]))


# ================================================================== L3
@template("c19x_secondary_current_ideal", chapter=19, level=3, lo="19e")
def secondary_current_ideal(rng):
    Vp = nice(rng, 230, 240)
    Ip = nice(rng, 0.20, 0.25, 0.40, 0.50)
    Vs = nice(rng, 6, 12, 24)
    Is = Vp * Ip / Vs
    return mk(rng, Is, [(Ip, "The currents are different: the POWER is the same on both sides."), (Vs * Ip / Vp, "Upside down: a step-down transformer has a LARGER secondary current."),
                        (Vp * Ip, "That is the power in watts; divide by the secondary p.d.")],
              "A", f"Fig. 1 shows an ideal transformer. The primary is connected to **{Vp} V** and takes **{fmt(Ip)} A**. The secondary p.d. is **{Vs} V**. What is the secondary current?",
              "ideal: Vp Ip = Vs Is", [f"power = {Vp} × {fmt(Ip)} = {fmt(Vp * Ip)} W", f"Is = {fmt(Vp * Ip)} ÷ {Vs}", f"= **{fmt(Is, sf=3)} A**"],
              ["What is the same on both sides of an ideal transformer?", "The power.", "Is = Vp Ip ÷ Vs."],
              figure=figs3.transformer("Np", "Ns", f"{Vp} V", f"{Vs} V", n_p=8, n_s=3))


@template("c19x_ac_faster_period", chapter=19, level=3, lo="19c")
def ac_faster_period(rng):
    T = nice(rng, 20, 40)
    V = nice(rng, 4.0, 6.0, 8.0)
    k = nice(rng, 2, 4)
    return mk(rng, T / k, [(T * k, "Turning faster gives a SHORTER period."), (T, "The rotation speed sets the period, so it changes."),
                           (1000 * k / T, "That is the new frequency in Hz, not the period.")],
              "ms", f"Fig. 1 shows the output of a simple a.c. generator. The coil is then turned **{k} times as fast**. What is the new period?",
              "period ∝ 1 / rotation speed", [f"original period = {T} ms", f"new period = {T} ÷ {k}", f"= **{fmt(T / k)} ms**"],
              ["Read the period from the graph.", "Faster rotation → more cycles per second.", "Divide the period by the speed factor."],
              figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_ac_time_to_peak", chapter=19, level=3, lo="19c")
def ac_time_to_peak(rng):
    T = nice(rng, 20, 40)
    V = nice(rng, 4.0, 6.0, 8.0, 10.0)
    return mk(rng, T / 4, [(T / 2, "At half a period the e.m.f. is back to zero."), (T, "That is a whole cycle."),
                           (3 * T / 4, "At three-quarters of a period the e.m.f. is at its NEGATIVE peak.")],
              "ms", "Fig. 1 shows the output of a simple a.c. generator, starting from zero. How long after the start does the e.m.f. first reach its maximum value?",
              "the first peak is a quarter of a period after the start", [f"period = {T} ms", f"first peak at T/4 = **{fmt(T / 4)} ms**"],
              ["Read the period first.", "The first peak is between 0 and the half-period mark.", "It is a quarter of a period."],
              figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_loss_percent", chapter=19, level=3, lo="19f")
def loss_percent(rng):
    P = nice(rng, 20, 40, 50)
    V = nice(rng, 132, 275, 400)
    R = nice(rng, 4, 5, 8, 10)
    I = P * 1e6 / (V * 1e3)
    loss = I * I * R
    pct = loss / (P * 1e6) * 100
    table = md_table(["quantity", "value"], [["power transmitted", f"{P} MW"], ["transmission p.d.", f"{V} kV"], ["cable resistance", f"{R} Ω"]])
    return mk(rng, pct, [(loss / 1e6, "That is the power lost in MW; express it as a percentage of the power transmitted."), (100 - pct, "That is the percentage DELIVERED, not lost."),
                         (pct / 100, "That is the fraction lost; multiply by 100 for a percentage.")],
              "%", f"Electrical power is transmitted along overhead cables.\n\n{table}\n\nWhat percentage of the power is lost in the cables?",
              "I = P ÷ V; loss = I² R; % = loss ÷ P × 100",
              [f"I = {P} × 10⁶ ÷ {V} × 10³ = {fmt(I, sf=3)} A", f"loss = {fmt(I, sf=3)}² × {R} = {fmt(loss, sf=3)} W", f"% = {fmt(loss, sf=3)} ÷ {P} × 10⁶ × 100 = **{fmt(pct, sf=3)}%**"],
              ["Find the current first.", "Then the power lost, I²R.", "Compare with the power transmitted."])


@template("c19x_cable_voltage_drop", chapter=19, level=3, lo="19f")
def cable_voltage_drop(rng):
    P = nice(rng, 10, 20, 50)
    V = nice(rng, 25, 50, 132)
    R = nice(rng, 2, 4, 5, 8)
    I = P * 1e6 / (V * 1e3)
    return mk(rng, I * R, [(I * I * R, "That is the power lost. The p.d. across the cables is I R."), (V * 1e3, "That is the transmission p.d., not the drop across the cables."),
                           (I, "That is the current; multiply by the resistance.")],
              "V", f"Fig. 1 shows a power station sending **{P} MW** at **{V} kV** through cables of total resistance **{R} Ω**. What is the p.d. across the cables?",
              "I = P ÷ V, then V_cables = I R", [f"I = {P} × 10⁶ ÷ ({V} × 10³) = {fmt(I, sf=3)} A", f"V = {fmt(I, sf=3)} × {R}", f"= **{fmt(I * R, sf=3)} V**"],
              ["First find the current in the cables.", "The cables obey V = IR.", "Multiply the current by the cable resistance."],
              figure=figs3.transmission([f"power = {P} MW", f"transmission p.d. = {V} kV", f"cable resistance = {R} Ω"]))


@template("c19x_dc_supply_output", chapter=19, level=3, lo="19d")
def dc_supply_output(rng):
    V = nice(rng, 6, 12, 24)
    Np, Ns = rng.choice([(100, 500), (200, 1000), (400, 100), (600, 200), (300, 1200)])
    ans = "0 V"
    wrongs = {f"{fmt(V * Ns / Np, sf=3)} V": "That uses the turns ratio, but a steady d.c. gives no CHANGING field in the core, so nothing is induced.",
              f"{V} V": "The secondary is not connected to the battery; it only gets an e.m.f. from a changing field.",
              f"{fmt(V * Np / Ns, sf=3)} V": "A steady d.c. supply induces no e.m.f., whatever the turns ratio."}
    table = md_table(["", "value"], [["supply", f"{V} V battery (d.c.)"], ["primary turns", Np], ["secondary turns", Ns]])
    return mkt(rng, ans, wrongs, f"A transformer is connected to a battery and the current is allowed to become steady.\n\n{table}\n\nWhat is the steady reading of a voltmeter across the secondary coil?",
               "a transformer needs a CHANGING field: steady d.c. induces nothing", ["steady current → steady field → no change → **0 V**"],
               ["What must happen to the field in the core for an e.m.f. to be induced?", "It must change.", "Does a steady d.c. make a changing field?"])


@template("c19x_working_design", chapter=19, level=3, lo="19d")
def working_design(rng):
    V = nice(rng, 12, 24, 230)
    labels = ["A", "B", "C", "D"]
    rng.shuffle(labels)
    rows = [(labels[0], "laminated soft iron", f"{V} V a.c."), (labels[1], "laminated soft iron", f"{V} V d.c."),
            (labels[2], "copper", f"{V} V a.c."), (labels[3], "plastic", f"{V} V d.c.")]
    ans = labels[0]
    wrongs = {labels[1]: "A d.c. supply gives a steady field, so no e.m.f. is induced in the secondary.",
              labels[2]: "Copper is not magnetic, so it cannot carry the changing magnetic field to the secondary.",
              labels[3]: "Neither the core nor the supply is suitable."}
    table = md_table(["design", "core", "supply"], sorted([list(r) for r in rows]))
    return mkt(rng, ans, wrongs, f"Four transformer designs are tested.\n\n{table}\n\nWhich design works as a transformer?",
               "a transformer needs an a.c. supply and a soft-iron core", [f"design {ans}: soft-iron core and a.c. supply → **{ans}**"],
               ["What kind of supply makes a changing field?", "a.c.", "Which core carries the field best?"])


@template("c19x_emf_combined", chapter=19, level=3, lo="19a")
def emf_combined(rng):
    E0 = nice(rng, 1.0, 1.5, 2.0, 2.5)
    a, b = rng.choice([(2, 3), (3, 2), (2, 4), (4, 2), (3, 4)])
    table = md_table(["", "speed of magnet", "number of turns", "maximum e.m.f. / mV"], [["original", "v", "N", fmt(E0)], ["new", f"{a}v", f"{b}N", "?"]])
    return mk(rng, E0 * a * b, [(E0 * (a + b), "The factors multiply; they do not add."), (E0 * a, "The extra turns also increase the e.m.f."),
                                (E0 * b, "The faster magnet also increases the e.m.f.")],
              "mV", f"The induced e.m.f. is proportional to the speed of the magnet and to the number of turns on the coil.\n\n{table}\n\nWhat is the new maximum e.m.f.?",
              "e.m.f. ∝ speed × number of turns", [f"factor = {a} × {b} = {a * b}", f"e.m.f. = {fmt(E0)} × {a * b} = **{fmt(E0 * a * b)} mV**"],
              ["What happens with the speed change alone?", "What happens with the turns change alone?", "Multiply the two factors."])


# ================================================================== L4
@template("c19x_two_stage", chapter=19, level=4, lo="19e")
def two_stage(rng):
    V1 = nice(rng, 11, 22, 25)
    r1 = nice(rng, 10, 16, 20)
    r2 = nice(rng, 25, 40, 50)
    final = V1 * r1 / r2
    table = md_table(["transformer", "primary turns", "secondary turns"], [["T₁ (at the power station)", 100, 100 * r1], ["T₂ (at the substation)", 50 * r2, 50]])
    return mk(rng, final, [(V1 * r1, "That is the p.d. after T₁ only; T₂ then steps it down."), (V1 * r2 / r1, "You have both turns ratios upside down."),
                           (V1 / r2, "T₁ steps the p.d. UP before T₂ steps it down.")],
              "kV", f"A generator gives **{V1} kV**. Its output passes through two ideal transformers in turn.\n\n{table}\n\nWhat is the output p.d. of T₂?",
              "apply Vs = Vp × Ns ÷ Np to each transformer in turn", [f"after T₁: {V1} × {r1} = {V1 * r1} kV", f"after T₂: {V1 * r1} ÷ {r2}", f"= **{fmt(final, sf=3)} kV**"],
              ["Work out the output of T₁ first.", "That is the input of T₂.", "Apply the turns ratio of T₂."])


@template("c19x_turns_from_currents", chapter=19, level=4, lo="19e")
def turns_from_currents(rng):
    Np = nice(rng, 1000, 2000, 2400)
    Ip = nice(rng, 0.20, 0.25, 0.50)
    Is = nice(rng, 2.0, 4.0, 5.0, 10.0)
    Ns = Np * Ip / Is
    table = md_table(["", "primary", "secondary"], [["number of turns", Np, "?"], ["current / A", fmt(Ip), fmt(Is)]])
    return mk(rng, Ns, [(Np * Is / Ip, "The current ratio is the INVERSE of the turns ratio: the coil with more turns has the smaller current."),
                        (Is / Ip, "That is only the current ratio; use it with the primary turns."), (Np * Ip, "Divide by the secondary current as well.")],
              "turns", f"The table gives data for an ideal transformer.\n\n{table}\n\nHow many turns are on the secondary coil?",
              "ideal: Vp Ip = Vs Is and Vs/Vp = Ns/Np, so Ns/Np = Ip/Is", [f"Ns = Np × Ip ÷ Is", f"= {Np} × {fmt(Ip)} ÷ {fmt(Is)}", f"= **{fmt(Ns, sf=3)} turns**"],
              ["Power in = power out, so how do the currents compare with the p.d.s?", "Is/Ip = Vp/Vs = Np/Ns.", "Ns = Np × Ip/Is."])


@template("c19x_ac_faster_peak", chapter=19, level=4, lo="19c")
def ac_faster_peak(rng):
    T = nice(rng, 20, 40)
    V = nice(rng, 3.0, 4.0, 6.0)
    k = nice(rng, 2, 3)
    return mk(rng, k * V, [(V, "Faster rotation makes the field through the coil change faster, so the peak rises."), (V / k, "The peak gets LARGER when the coil turns faster."),
                           (k * k * V, "The peak e.m.f. is proportional to the speed, not its square.")],
              "V", f"Fig. 1 shows the output of a simple a.c. generator. The coil is turned **{k} times as fast** in the same field. What is the new peak e.m.f.?",
              "peak e.m.f. ∝ rotation speed", [f"original peak = {fmt(V)} V", f"new peak = {k} × {fmt(V)}", f"= **{fmt(k * V)} V**"],
              ["Read the original peak.", "How does the rate of change of the field depend on the speed?", "Multiply by the speed factor."],
              figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_rpm_from_graph", chapter=19, level=4, lo="19c")
def rpm_from_graph(rng):
    T = nice(rng, 10, 20, 40, 50)
    V = nice(rng, 4.0, 6.0)
    rpm = 60000 / T
    return mk(rng, rpm, [(1000 / T, "That is revolutions per SECOND; multiply by 60."), (T * 60, "Use the frequency (1 ÷ period), not the period."),
                         (120000 / T, "One revolution gives ONE complete cycle, not half a cycle.")],
              "rev/min", "Fig. 1 shows the output of a simple a.c. generator. How many revolutions per minute does the coil make?",
              "one revolution = one cycle: rev/s = f = 1 ÷ T; rev/min = 60 f",
              [f"T = {T} ms → f = {fmt(1000 / T, sf=3)} Hz", f"rev/min = 60 × {fmt(1000 / T, sf=3)}", f"= **{fmt(rpm, sf=3)} rev/min**"],
              ["Read the period.", "One revolution gives one cycle, so rev/s = frequency.", "Multiply by 60."],
              figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_time_for_magnet", chapter=19, level=4, lo="19a")
def time_for_magnet(rng):
    t1 = nice(rng, 0.40, 0.60, 0.80, 1.20)
    k = nice(rng, 2, 4)
    E1 = nice(rng, 2.0, 3.0, 5.0)
    table = md_table(["trial", "time to push the magnet in / s", "average e.m.f. / mV"], [["1", fmt(t1), fmt(E1)], ["2", fmt(t1 / k), "?"]])
    return mk(rng, k * E1, [(E1 / k, "A shorter time means a FASTER change, so a larger e.m.f."), (E1, "The same change happening faster gives a larger e.m.f."),
                            (E1 * k * k, "The e.m.f. is inversely proportional to the time, not to its square.")],
              "mV", f"A magnet is pushed fully into a coil in different times. The average e.m.f. is inversely proportional to the time taken.\n\n{table}\n\nWhat is the average e.m.f. in trial 2?",
              "e.m.f. ∝ rate of change of the field ∝ 1 / time", [f"time ÷ {k} → e.m.f. × {k}", f"= **{fmt(k * E1)} mV**"],
              ["Is trial 2 faster or slower?", "Faster change → larger e.m.f.", f"The time is {k} times shorter."])


@template("c19x_lenz_pole", chapter=19, level=4, lo="19a")
def lenz_pole(rng):
    pole = rng.choice(["N", "S"])
    other = "S" if pole == "N" else "N"
    moving = rng.choice(["in", "out"])
    if moving == "in":
        ans = f"a {pole} pole, which repels the approaching magnet"
        wrong1 = f"a {other} pole, which attracts the approaching magnet"
    else:
        ans = f"an {other} pole, which attracts the leaving magnet" if other == "N" else f"a {other} pole, which attracts the leaving magnet"
        wrong1 = f"a {pole} pole, which repels the leaving magnet"
    wrongs = {wrong1: "The induced current OPPOSES the change (Lenz's law), so the coil must oppose the motion of the magnet.",
              "no pole, because copper is not magnetic": "The induced current in the coil makes it an electromagnet.",
              "no pole, because the magnet does not touch the coil": "Contact is not needed: the changing field induces a current."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the {pole} pole of a magnet being moved {'into' if moving == 'in' else 'out of'} a coil. What pole is induced at the end of the coil nearest the magnet?",
               "Lenz's law: the induced current opposes the change producing it", [f"magnet moving {moving} → the coil opposes the motion → **{ans}**"],
               ["What does the induced current always do to the change?", "It opposes it.", "Approaching → repel; leaving → attract."],
               figure=figs3.magnet_into_coil(moving, pole=pole))


@template("c19x_core_loss_table", chapter=19, level=4, lo="19d")
def core_loss_table(rng):
    effs = sorted(rng.sample(range(60, 99), 3) + [rng.randint(10, 25)], reverse=True)
    rows = [["laminated soft iron", effs[0]], ["solid soft iron", effs[1]], ["laminated steel", effs[2]], ["no core (air)", effs[3]]]
    rng.shuffle(rows)
    ans = "laminated soft iron: it is easily magnetised and demagnetised, and the layers reduce heating by eddy currents"
    wrongs = {"solid soft iron: a solid core carries the most magnetic field": "Large currents are induced in a solid core, heating it and wasting energy.",
              "laminated steel: steel keeps its magnetism, so the field is strongest": "Steel is hard to demagnetise, so energy is wasted each time the field reverses.",
              "no core: there is no core to heat up": "Without an iron core, most of the changing field from the primary misses the secondary."}
    table = md_table(["core", "efficiency / %"], rows)
    return mkt(rng, ans, wrongs, f"A transformer is tested with four different cores.\n\n{table}\n\nWhich core gives the highest efficiency, and why?",
               "the best core is laminated soft iron", [f"highest efficiency: laminated soft iron ({effs[0]}%) → **{ans}**"],
               ["Read the highest efficiency.", "Why is soft iron better than steel?", "Why are the layers insulated from each other?"])


@template("c19x_wasted_power", chapter=19, level=4, lo="19d")
def wasted_power(rng):
    Vp = nice(rng, 230, 240)
    Ip = nice(rng, 0.40, 0.50, 0.80, 1.00)
    Vs = nice(rng, 12, 24)
    eff = nice(rng, 0.85, 0.90, 0.95)
    Is = round(Vp * Ip * eff / Vs, 1)
    waste = Vp * Ip - Vs * Is
    table = md_table(["", "p.d. / V", "current / A"], [["primary", Vp, fmt(Ip)], ["secondary", Vs, fmt(Is)]])
    return mk(rng, waste, [(Vs * Is, "That is the useful output power."), (Vp * Ip, "That is the input power; subtract the output."),
                           (Vp * Ip + Vs * Is, "Wasted power = input − output, not input + output.")],
              "W", f"Measurements on a real transformer are shown.\n\n{table}\n\nWhat power is wasted, mainly as heat in the coils and core?",
              "wasted power = Vp Ip − Vs Is", [f"input = {Vp} × {fmt(Ip)} = {fmt(Vp * Ip)} W", f"output = {Vs} × {fmt(Is)} = {fmt(Vs * Is, sf=3)} W", f"wasted = **{fmt(waste, sf=3)} W**"],
              ["Work out the input power.", "Work out the output power.", "Subtract."])


# ================================================================== L5
@template("c19x_charger_primary", chapter=19, level=5, lo="19e")
def charger_primary(rng):
    Vp = 230
    Vs = nice(rng, 5, 9, 12)
    Is = nice(rng, 1.0, 2.0, 2.4, 3.0)
    eff = nice(rng, 80, 85, 90)
    Ip = Vs * Is / (eff / 100 * Vp)
    table = md_table(["quantity", "value"], [["mains p.d.", f"{Vp} V"], ["output p.d.", f"{Vs} V"], ["output current", f"{fmt(Is)} A"], ["efficiency", f"{eff}%"]])
    return mk(rng, Ip, [(Vs * Is / Vp, "That assumes an ideal transformer. The input power is LARGER than the output when the efficiency is below 100%."),
                        (Vs * Is * eff / 100 / Vp, "Divide the output power by the efficiency to get the input power, do not multiply."),
                        (Is * Vp / Vs, "Upside down: the primary of a step-down transformer has the smaller current.")],
              "A", f"A phone charger contains a transformer.\n\n{table}\n\nWhat is the current in the primary coil?",
              "input power = output power ÷ efficiency; Ip = input power ÷ Vp",
              [f"output = {Vs} × {fmt(Is)} = {fmt(Vs * Is)} W", f"input = {fmt(Vs * Is)} ÷ {eff / 100} = {fmt(Vs * Is / (eff / 100), sf=3)} W", f"Ip = input ÷ {Vp} = **{fmt(Ip, sf=3)} A**"],
              ["Find the output power.", "The input power is larger because of the efficiency.", "Divide the input power by the mains p.d."])


@template("c19x_lenz_trials", chapter=19, level=5, lo="19a")
def lenz_trials(rng):
    pole = rng.choice(["N", "S"])
    other = "S" if pole == "N" else "N"
    first = rng.choice(["left", "right"])
    labels = ["A", "B", "C", "D"]
    rng.shuffle(labels)
    trials = [(labels[0], f"{other} pole pulled out"), (labels[1], f"{pole} pole pulled out"), (labels[2], f"{other} pole pushed in"), (labels[3], f"{pole} pole held still inside")]
    ans = labels[0]
    wrongs = {labels[1]: "Only the motion is reversed, so the deflection is reversed.", labels[2]: "Only the pole is reversed, so the deflection is reversed.",
              labels[3]: "A stationary magnet induces nothing."}
    table = md_table(["trial", "what is done (same speed)"], sorted([list(t) for t in trials]))
    return mkt(rng, ans, wrongs, f"When the {pole} pole of a magnet is pushed into a coil, a galvanometer deflects to the **{first}**. Four more trials are done.\n\n{table}\n\nIn which trial does the galvanometer also deflect to the {first}?",
               "reversing the motion OR the pole reverses the current; reversing both leaves it unchanged",
               [f"trial {ans}: pole reversed AND motion reversed → two reversals → same direction → **{ans}**"],
               ["Count the reversals compared with the first test.", "One reversal → opposite direction.", "Two reversals → same direction."])


@template("c19x_choose_voltage", chapter=19, level=5, lo="19f")
def choose_voltage(rng):
    P = nice(rng, 20, 50)
    R = nice(rng, 1, 2, 4)
    Vs = [33, 66, 132, 400]
    pct = [P * 1e6 * R / (v * 1e3) ** 2 * 100 for v in Vs]
    j = rng.choice([1, 2, 3])
    thr = float(f"{math.sqrt(pct[j - 1] * pct[j]):.1g}")
    if not pct[j] < thr < pct[j - 1]:
        thr = float(f"{math.sqrt(pct[j - 1] * pct[j]):.2g}")
    ans = f"{Vs[j]} kV"
    wrongs = {}
    for i, v in enumerate(Vs):
        if i < j:
            wrongs[f"{v} kV"] = f"At {v} kV the loss is {fmt(pct[i], sf=2)}%, which is above the limit."
        elif i > j:
            wrongs[f"{v} kV"] = f"{v} kV meets the limit, but a lower p.d. ({Vs[j]} kV) also does and is cheaper to insulate."
    table = md_table(["quantity", "value"], [["power to transmit", f"{P} MW"], ["cable resistance", f"{R} Ω"], ["p.d.s available", ", ".join(f"{v} kV" for v in Vs)]])
    return mkt(rng, ans, wrongs, f"An engineer must choose a transmission p.d.\n\n{table}\n\nThe cheapest choice is the LOWEST p.d. that keeps the power lost in the cables below **{fmt(thr, sf=2)}%** of the power transmitted. Which p.d. should be chosen?",
               "loss = I² R with I = P ÷ V; % lost = loss ÷ P × 100",
               [f"{v} kV: I = {fmt(P * 1e3 / v, sf=3)} A, loss = {fmt(pct[i], sf=2)}%" for i, v in enumerate(Vs)] + [f"lowest p.d. below {fmt(thr, sf=2)}% → **{ans}**"],
               ["Find the current for each p.d.", "Then the percentage lost, I²R ÷ P × 100.", "Pick the lowest p.d. that meets the limit."])


@template("c19x_loss_new_voltage", chapter=19, level=5, lo="19f")
def loss_new_voltage(rng):
    L1 = nice(rng, 400, 800, 1200, 1600)
    V1 = nice(rng, 33, 66, 132)
    k = nice(rng, 2, 4)
    V2 = V1 * k
    L2 = L1 / k ** 2
    table = md_table(["transmission p.d. / kV", "power lost in cables / kW"], [[V1, L1], [V2, "?"]])
    return mk(rng, L2, [(L1 / k, "The loss depends on I², so it falls by the square of the factor."), (L1 * k ** 2, "A higher p.d. gives a SMALLER current and a smaller loss."),
                        (L1 * k, "A higher p.d. REDUCES the loss.")],
              "kW", f"The same power is sent through the same cables at a higher p.d.\n\n{table}\n\nWhat is the new power lost in the cables?",
              "I ∝ 1/V, loss = I² R ∝ 1/V²", [f"p.d. × {k} → I ÷ {k} → loss ÷ {k * k}", f"= {L1} ÷ {k * k} = **{fmt(L2, sf=3)} kW**"],
              ["How does the current change?", "How does the loss depend on the current?", "Square the factor."])


@template("c19x_generator_two_changes", chapter=19, level=5, lo="19c")
def generator_two_changes(rng):
    T = nice(rng, 20, 40)
    V = nice(rng, 2.0, 3.0, 4.0)
    a = nice(rng, 2, 3)
    b = nice(rng, 2, 3)
    ans = f"peak {fmt(a * b * V)} V, period {fmt(T / a)} ms"
    wrongs = {f"peak {fmt(a * V)} V, period {fmt(T / a)} ms": "Doubling the turns also increases the e.m.f.",
              f"peak {fmt(a * b * V)} V, period {fmt(T / (a * b))} ms": "The number of turns does not change how many cycles there are each second.",
              f"peak {fmt(a * b * V)} V, period {fmt(T * a)} ms": "Faster rotation gives a SHORTER period."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the output of a simple a.c. generator. The coil is replaced by one with **{b} times** as many turns and turned **{a} times** as fast. What are the new peak e.m.f. and period?",
               "peak ∝ speed × turns; period ∝ 1/speed only", [f"peak = {fmt(V)} × {a} × {b} = {fmt(a * b * V)} V", f"period = {T} ÷ {a} = {fmt(T / a)} ms", f"**{ans}**"],
               ["Which changes affect the peak?", "Which changes affect the period?", "Only the speed changes the period."],
               figure=figs3.ac_output(period=T / 1000, vpeak=V))


@template("c19x_coil_position_point", chapter=19, level=5, lo="19c")
def coil_position_point(rng):
    T = nice(rng, 20, 40)
    V = nice(rng, 4.0, 6.0, 8.0)
    times = [T / 8, T / 4, T / 2, 5 * T / 8]
    pts = [(t, V * math.sin(2 * math.pi * t / T), lab) for t, lab in zip(times, "ABCD")]
    kind = rng.choice(["max", "zero"])
    if kind == "max":
        q = "the sides of the coil are cutting the field lines at the fastest rate"
        ans = "B"
        wrongs = {"A": "At A the e.m.f. is still rising; the sides cut the lines fastest where the e.m.f. is largest.", "C": "At C the e.m.f. is zero: the sides are moving along the field lines.",
                  "D": "At D the e.m.f. is not at its largest value."}
    else:
        q = "the sides of the coil are moving parallel to the field lines (not cutting them)"
        ans = "C"
        wrongs = {"A": "At A an e.m.f. is induced, so the sides are cutting field lines.", "B": "At B the e.m.f. is largest: the sides cut the lines fastest.",
                  "D": "At D an e.m.f. is induced, so the sides are cutting field lines."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the output of a simple a.c. generator with four points marked. At which point are {q}?",
               "e.m.f. is largest when the coil sides cut the field lines fastest and zero when they move along the lines",
               [f"{'largest' if kind == 'max' else 'zero'} e.m.f. → **{ans}**"],
               ["What does the size of the e.m.f. tell you about how fast lines are cut?", "Largest e.m.f. = fastest cutting.", "Zero e.m.f. = no cutting."],
               figure=figs3.ac_output(period=T / 1000, vpeak=V, label_points=pts))


@template("c19x_dc_switch_claim", chapter=19, level=5, lo="19d")
def dc_switch_claim(rng):
    V = nice(rng, 6, 9, 12)
    Np, Ns = rng.choice([(100, 1000), (200, 1000), (50, 500), (150, 600)])
    ans = "only for an instant, each time the switch is closed or opened"
    wrongs = {f"all the time the switch is closed, at {fmt(V * Ns / Np, sf=3)} V": "A steady d.c. gives a steady field, so there is no e.m.f. once the current is steady.",
              "never, because a transformer cannot respond to a battery at all": "When the switch is closed or opened the current, and so the field, changes briefly.",
              f"all the time the switch is closed, at {V} V": "The secondary is not connected to the battery, and a steady field induces nothing."}
    table = md_table(["", "value"], [["supply", f"{V} V battery with a switch"], ["primary turns", Np], ["secondary turns", Ns]])
    return mkt(rng, ans, wrongs, f"A student connects a transformer to a battery through a switch and puts a voltmeter across the secondary coil.\n\n{table}\n\nWhen does the voltmeter show a reading?",
               "an e.m.f. is induced only while the field in the core changes", ["the field changes only as the current starts or stops → **brief readings only**"],
               ["When does the current in the primary change?", "Only when it is switched on or off.", "A changing field is needed for an induced e.m.f."])


@template("c19x_supply_choice", chapter=19, level=5, lo="19d")
def supply_choice(rng):
    r = nice(rng, 2, 5, 10)
    S = nice(rng, 6, 12, 24)
    labels = ["W", "X", "Y", "Z"]
    rng.shuffle(labels)
    rows = [(labels[0], f"{S} V a.c."), (labels[1], f"{S} V d.c."), (labels[2], f"{2 * S} V a.c."), (labels[3], f"{fmt(S / 2)} V a.c.")]
    ans = labels[0]
    target = r * S
    wrongs = {labels[1]: "A d.c. supply gives no changing field, so there is no output.", labels[2]: f"That gives {r * 2 * S} V.", labels[3]: f"That gives {fmt(r * S / 2)} V."}
    table = md_table(["supply", "type"], sorted([list(x) for x in rows]))
    return mkt(rng, ans, wrongs, f"An ideal transformer has **{r} times** as many turns on its secondary as on its primary.\n\n{table}\n\nWhich supply gives an output of **{target} V**?",
               "Vs = Vp × Ns/Np, and only a.c. works", [f"Vp = {target} ÷ {r} = {S} V, and it must be a.c. → **{ans}**"],
               ["What input p.d. is needed?", "Divide the output by the turns ratio.", "Check the supply type too."])
