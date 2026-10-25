"""Chapter 9 Thermal Properties of Matter (6091) bank extension: calculation and data-reading templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: lauric acid cooling in a polystyrene beaker,
salty ice melting, a substance heated from -5 °C to 110 °C, solid heated from 5 °C to 150 °C, large and small cotton sheets drying)."""
from .. import figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, template

C_WATER = 4200
C_ICE = 2100
L_ICE = 334000
L_STEAM = 2260000


# ================================================================== L1
@template("c9x_internal_energy_sum", chapter=9, level=1, lo="9a")
def internal_energy_sum(rng):
    ke = nice(rng, 1200, 1500, 2400, 3000)
    pe = nice(rng, 800, 900, 1600, 2000)
    return mk(rng, ke + pe, [(ke, "Internal energy includes the potential energy of the particles too."), (pe, "Include the kinetic energy of the particles."), (ke - pe, "Add the two stores.")],
              "J", f"For a small block of metal:\n\n{md_table(['energy of the particles', 'total / J'], [['kinetic (vibration)', ke], ['potential (due to forces between them)', pe]])}\n\nWhat is the internal energy of the block?",
              "internal energy = total KE + total PE of the particles", [f"U = {ke} + {pe} = **{ke + pe} J**"],
              ["Internal energy has two parts.", "Kinetic and potential energy of the particles.", "Add them."], dp=0)


@template("c9x_internal_energy_gain", chapter=9, level=1, lo="9a")
def internal_energy_gain(rng):
    P = nice(rng, 50, 100, 200)
    t = nice(rng, 30, 60, 120)
    return mk(rng, P * t, [(P / t, "Energy = power × time."), (P, "Multiply by the time."), (P * t / 60, "The time is already in seconds.")],
              "J", f"An insulated block is heated; all the energy supplied goes into the block.\n\n{md_table(['quantity', 'value'], [['heater power', f'{P} W'], ['time', f'{t} s']])}\n\nBy how much does the internal energy of the block increase?",
              "increase in internal energy = energy supplied = P t", [f"ΔU = {P} × {t} = **{fmt(P * t)} J**"],
              ["No energy is lost.", "The energy supplied all goes into the block.", "E = P × t."])


@template("c9x_heat_capacity_simple", chapter=9, level=1, lo="9b")
def heat_capacity_simple(rng):
    Q = nice(rng, 4500, 6000, 9000, 12000)
    dT = nice(rng, 10, 15, 20, 30)
    return mk(rng, Q / dT, [(Q * dT, "Heat capacity = Q ÷ Δθ."), (dT / Q, "Energy goes on top."), (Q, "Divide by the temperature rise.")],
              "J/K", f"A metal block is heated.\n\n{md_table(['quantity', 'value'], [['energy supplied', f'{Q} J'], ['temperature rise', f'{dT} °C']])}\n\nWhat is the heat capacity of the block?",
              "heat capacity C = Q ÷ Δθ", [f"C = {Q} ÷ {dT} = **{fmt(Q / dT)} J/K**"],
              ["Heat capacity is energy per degree.", "C = Q ÷ Δθ.", "Divide."])


@template("c9x_shc_simple", chapter=9, level=1, lo="9b")
def shc_simple(rng):
    m = nice(rng, 0.5, 1.0, 2.0)
    c = nice(rng, 400, 450, 900)
    dT = nice(rng, 10, 20)
    Q = m * c * dT
    return mk(rng, c, [(Q / dT, "That is the heat capacity of the block; divide by the mass too."), (Q / m, "Divide by the temperature rise too."), (Q, "c = Q ÷ (m Δθ).")],
              "J/(kg K)", f"A block of metal is heated.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['energy supplied', f'{fmt(Q)} J'], ['temperature rise', f'{dT} °C']])}\n\nWhat is the specific heat capacity of the metal?",
              "c = Q ÷ (m Δθ)", [f"c = {fmt(Q)} ÷ ({fmt(m)} × {dT}) = **{fmt(c)} J/(kg K)**"],
              ["Specific means per kilogram.", "c = Q ÷ (m Δθ).", "Divide by both m and Δθ."])


@template("c9x_q_mc_dt_metal", chapter=9, level=1, lo="9c")
def q_mc_dt_metal(rng):
    m = nice(rng, 0.2, 0.5, 1.0, 2.0)
    c = nice(rng, 380, 450, 900)
    dT = nice(rng, 10, 20, 25, 40)
    Q = m * c * dT
    return mk(rng, Q, [(c * dT, "Multiply by the mass too."), (m * c, "Multiply by the temperature rise too."), (m * dT, "Include the specific heat capacity.")],
              "J", f"A metal block is heated.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['specific heat capacity', f'{c} J/(kg K)'], ['temperature rise', f'{dT} °C']])}\n\nHow much energy is needed?",
              "Q = m c Δθ", [f"Q = {fmt(m)} × {c} × {dT} = **{fmt(Q)} J**"],
              ["Use Q = m c Δθ.", "All values are in SI units.", "Multiply."])


@template("c9x_q_ml_steam", chapter=9, level=1, lo="9g")
def q_ml_steam(rng):
    m = nice(rng, 0.1, 0.2, 0.25, 0.5)
    Q = m * L_STEAM
    return mk(rng, Q, [(m * L_ICE, "Boiling uses the latent heat of VAPORISATION (2 260 000 J/kg)."), (L_STEAM / m, "Q = m L."), (m * C_WATER * 100, "At 100 °C no temperature change is needed: use Q = m L.")],
              "J", f"Water at 100 °C is boiled away.\n\n{md_table(['quantity', 'value'], [['mass boiled', f'{fmt(m)} kg'], ['specific latent heat of vaporisation of water', '2 260 000 J/kg']])}\n\nHow much energy is needed?",
              "Q = m L_v", [f"Q = {fmt(m)} × 2 260 000 = **{fmt(Q)} J**"],
              ["The water is already at 100 °C.", "Only a change of state.", "Q = m L."])


@template("c9x_melting_point_graph", chapter=9, level=1, lo="9d")
def melting_point_graph(rng):
    mp = nice(rng, 40, 50, 60, 70)
    pts = [(0, 20), (3, mp), (8, mp), (11, mp + 30)]
    return mk(rng, mp, [(mp + 30, "That is the final temperature; the melting point is the flat part."), (20, "That is the starting temperature."), (8, "That is a time, not a temperature.")],
              "°C", "Fig. 1 shows the heating curve of a solid heated steadily. What is its melting point?",
              "melting point = temperature of the flat section", [f"the flat section is at **{mp} °C**"],
              ["Which part shows melting?", "The temperature stays constant.", "Read that temperature."], figure=sketches.heating_curve(pts), dp=0)


@template("c9x_state_at_time", chapter=9, level=1, lo="9d")
def state_at_time(rng):
    mp = nice(rng, 40, 50, 60)
    pts = [(0, 20), (3, mp), (8, mp), (11, mp + 30)]
    t = rng.choice([1, 5, 10])
    ans = {1: "solid", 5: "solid and liquid", 10: "liquid"}[t]
    wrongs = {o: "Find which part of the curve the time falls on." for o in ["solid", "solid and liquid", "liquid", "gas"] if o != ans}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the heating curve of a solid heated steadily. What is the state of the substance at **{t} min**?",
               "rising before the flat part: solid; flat: melting (solid + liquid); after: liquid", [f"at {t} min → **{ans}**"],
               ["Where is the flat part?", "Before it: solid; during it: melting; after it: liquid.", "Locate the time."], figure=sketches.heating_curve(pts))


# ================================================================== L2
@template("c9x_temp_rise_from_q", chapter=9, level=2, lo="9c")
def temp_rise_from_q(rng):
    m = nice(rng, 0.5, 1.0, 2.0)
    Q = nice(rng, 21000, 42000, 84000)
    dT = Q / (m * C_WATER)
    return mk(rng, dT, [(Q / C_WATER, "Divide by the mass too."), (Q / m, "Divide by c too."), (m * C_WATER / Q, "Δθ = Q ÷ (m c).")],
              "°C", f"Energy is supplied to water.\n\n{md_table(['quantity', 'value'], [['mass of water', f'{fmt(m)} kg'], ['energy supplied', f'{Q} J'], ['specific heat capacity of water', '4200 J/(kg K)']])}\n\nWhat is the rise in temperature?",
              "Δθ = Q ÷ (m c)", [f"Δθ = {Q} ÷ ({fmt(m)} × 4200) = **{fmt(dT)} °C**"],
              ["Rearrange Q = m c Δθ.", "Δθ = Q ÷ (m c).", "Calculate."])


@template("c9x_mass_melted", chapter=9, level=2, lo="9g")
def mass_melted(rng):
    Q = nice(rng, 33400, 66800, 100200, 167000)
    m = Q / L_ICE
    return mk(rng, m, [(Q / L_STEAM, "Melting uses the latent heat of FUSION."), (Q * L_ICE, "m = Q ÷ L."), (m * 1000, "The answer is in kg.")],
              "kg", f"Ice at 0 °C is melted.\n\n{md_table(['quantity', 'value'], [['energy supplied', f'{Q} J'], ['specific latent heat of fusion of ice', '334 000 J/kg']])}\n\nWhat mass of ice melts?",
              "m = Q ÷ L_f", [f"m = {Q} ÷ 334 000 = **{fmt(m)} kg**"],
              ["Q = m L.", "Rearrange for m.", "Use the latent heat of fusion."])


@template("c9x_heat_capacity_from_c", chapter=9, level=2, lo="9b")
def heat_capacity_from_c(rng):
    m = nice(rng, 0.5, 1.5, 2.0, 3.0)
    c = nice(rng, 450, 900, 4200)
    return mk(rng, m * c, [(c / m, "Heat capacity = m × c."), (c, "That is per kg; multiply by the mass."), (m * c / 1000, "The answer is in J/K.")],
              "J/K", f"{md_table(['quantity', 'value'], [['mass of object', f'{fmt(m)} kg'], ['specific heat capacity of its material', f'{c} J/(kg K)']])}\n\nWhat is the heat capacity of the object?",
              "C = m c", [f"C = {fmt(m)} × {c} = **{fmt(m * c)} J/K**"],
              ["Heat capacity is for the whole object.", "Specific heat capacity is per kg.", "C = m c."])


@template("c9x_compare_shc_table", chapter=9, level=2, lo="9b")
def compare_shc_table(rng):
    rows = [("aluminium", 900), ("copper", 390), ("iron", 450), ("lead", 130)]
    rng.shuffle(rows)
    ans = max(rows, key=lambda r: r[1])[0]
    wrongs = {n: ("A LOW specific heat capacity means a FAST temperature rise." if c == 130 else "Compare the specific heat capacities: the largest c gives the smallest rise.") for n, c in rows if n != ans}
    table = md_table(["metal", "specific heat capacity / J/(kg K)"], [[n, c] for n, c in rows])
    return mkt(rng, ans, wrongs, f"Blocks of equal mass of four metals receive the same energy.\n\n{table}\n\nWhich block has the SMALLEST temperature rise?",
               "Δθ = Q ÷ (m c): largest c → smallest Δθ", [f"largest c → **{ans}**"],
               ["Δθ = Q ÷ (m c).", "Q and m are the same.", "The biggest c gives the smallest Δθ."])


@template("c9x_boiling_time_graph", chapter=9, level=2, lo="9d")
def boiling_time_graph(rng):
    t1 = nice(rng, 4, 5, 6)
    dur = nice(rng, 6, 8, 10)
    pts = [(0, 20), (t1, 100), (t1 + dur, 100)]
    return mk(rng, dur, [(t1 + dur, "That is when boiling STOPS being recorded; find the length of the flat section."), (t1, "That is when boiling starts."), (100, "That is the boiling point, not a time.")],
              "min", "Fig. 1 shows the temperature of water heated steadily until it boils. For how long does the water boil during the time shown?",
              "boiling = flat section at the boiling point", [f"flat from {t1} min to {t1 + dur} min → **{dur} min**"],
              ["Which part shows boiling?", "The flat part at 100 °C.", "Subtract the start and end times."], figure=sketches.heating_curve(pts), dp=0)


@template("c9x_heating_curve_two_plateaus", chapter=9, level=2, lo="9d")
def heating_curve_two_plateaus(rng):
    mp = nice(rng, 5, 10, 20)
    bp = nice(rng, 80, 100, 110)
    pts = [(0, mp - 15), (2, mp), (5, mp), (9, bp), (14, bp)]
    which = rng.choice(["melting point", "boiling point"])
    ans = mp if which == "melting point" else bp
    wrong = bp if which == "melting point" else mp
    return mk(rng, ans, [(wrong, f"That is the {'boiling' if which == 'melting point' else 'melting'} point."), (9, "That is a time, not a temperature."), ((mp + bp) / 2, "Read the temperature of the correct flat section.")],
              "°C", f"Fig. 1 shows a substance heated steadily from below its melting point. What is its **{which}**?",
              "lower plateau = melting point; upper plateau = boiling point", [f"{which}: **{ans} °C**"],
              ["There are two flat sections.", "The lower one is melting, the upper one boiling.", "Read the right one."], figure=figs2.temp_time_graph(pts, ymax=140), dp=0)


@template("c9x_freezing_point_cooling", chapter=9, level=2, lo="9i")
def freezing_point_cooling(rng):
    fp = nice(rng, 44, 48, 54, 62)
    pts = [(0, 80), (3, fp), (9, fp), (13, fp - 20)]
    return mk(rng, fp, [(80, "That is the starting temperature."), (fp - 20, "That is the final temperature."), (9, "That is a time.")],
              "°C", "Fig. 1 shows the cooling curve of liquid lauric acid in a polystyrene beaker. What is its freezing point?",
              "freezing point = temperature of the flat section of a cooling curve", [f"flat section at **{fp} °C**"],
              ["Which part shows solidification?", "The temperature stays constant.", "Read that temperature."], figure=figs2.temp_time_graph(pts, ymax=100), dp=0)


@template("c9x_solidify_duration", chapter=9, level=2, lo="9i")
def solidify_duration(rng):
    fp = nice(rng, 44, 54)
    t1 = nice(rng, 2, 3, 4)
    dur = nice(rng, 5, 6, 8)
    pts = [(0, 80), (t1, fp), (t1 + dur, fp), (t1 + dur + 4, fp - 20)]
    return mk(rng, dur, [(t1 + dur, "That is when solidifying ENDS; subtract the start time."), (t1, "That is when it starts."), (fp, "That is the temperature.")],
              "min", "Fig. 1 shows the cooling curve of a liquid that solidifies. How long does it take to solidify completely?",
              "duration of the flat section", [f"from {t1} to {t1 + dur} min → **{dur} min**"],
              ["Find the flat section.", "Read its start and end times.", "Subtract."], figure=figs2.temp_time_graph(pts, ymax=100), dp=0)


# ================================================================== L3
@template("c9x_ice_from_freezer", chapter=9, level=3, lo="9g")
def ice_from_freezer(rng):
    m = nice(rng, 0.2, 0.5, 1.0)
    T0 = nice(rng, -10, -18, -20)
    Q1 = m * C_ICE * (0 - T0)
    Q2 = m * L_ICE
    return mk(rng, Q1 + Q2, [(Q2, "First warm the ice to 0 °C, then melt it."), (Q1, "Include the energy to MELT the ice."), (m * C_WATER * (0 - T0) + Q2, "Use the specific heat capacity of ICE (2100) for warming the ice.")],
              "J", f"Ice from a freezer is warmed to 0 °C and then melted.\n\n{md_table(['quantity', 'value'], [['mass of ice', f'{fmt(m)} kg'], ['starting temperature', f'{T0} °C'], ['specific heat capacity of ice', '2100 J/(kg K)'], ['specific latent heat of fusion', '334 000 J/kg']])}\n\nWhat is the total energy needed?",
              "Q = m c_ice Δθ + m L_f", [f"warming: {fmt(m)} × 2100 × {0 - T0} = {fmt(Q1)} J", f"melting: {fmt(m)} × 334 000 = {fmt(Q2)} J", f"total = **{fmt(Q1 + Q2)} J**"],
              ["Two stages: warming then melting.", "Warming: m c Δθ with c for ice.", "Melting: m L. Add."])


@template("c9x_latent_from_heater", chapter=9, level=3, lo="9g")
def latent_from_heater(rng):
    P = nice(rng, 50, 100, 200)
    t = nice(rng, 200, 300, 400)
    m = nice(rng, 0.05, 0.06, 0.1)
    L = P * t / m
    return mk(rng, L, [(P * t, "Divide the energy by the mass melted."), (P / m, "Multiply power by time first."), (m / (P * t), "L = Q ÷ m.")],
              "J/kg", f"An immersion heater melts a solid at its melting point.\n\n{md_table(['quantity', 'value'], [['heater power', f'{P} W'], ['time', f'{t} s'], ['mass melted', f'{fmt(m)} kg']])}\n\nWhat is the specific latent heat of fusion of the solid? (Assume no losses.)",
              "Q = P t; L = Q ÷ m", [f"Q = {P} × {t} = {P * t} J", f"L = {P * t} ÷ {fmt(m)} = **{fmt(L)} J/kg**"],
              ["Find the energy supplied.", "Divide by the mass melted.", "L = Q ÷ m."])


@template("c9x_shc_from_heater", chapter=9, level=3, lo="9b")
def shc_from_heater(rng):
    P = nice(rng, 24, 36, 48, 50)
    t = nice(rng, 300, 600)
    m = 1.0
    dT = nice(rng, 8, 10, 15, 20)
    c = P * t / (m * dT)
    return mk(rng, c, [(P * t / dT, "Divide by the mass too (here 1.0 kg, so the same)."), (P / dT, "Find the energy P × t first."), (P * t, "Divide by m and Δθ.")],
              "J/(kg K)", f"A 1.0 kg block has a heater and thermometer in it (Fig. 1). The heater runs for a time and the temperature rises.\n\n{md_table(['quantity', 'value'], [['heater power', f'{P} W'], ['time', f'{t} s'], ['temperature rise', f'{dT} °C']])}\n\nWhat is the specific heat capacity of the block?",
              "Q = P t; c = Q ÷ (m Δθ)", [f"Q = {P} × {t} = {P * t} J", f"c = {P * t} ÷ (1.0 × {dT}) = **{fmt(c)} J/(kg K)**"],
              ["Energy supplied = P × t.", "c = Q ÷ (m Δθ).", "Calculate."], figure=figs2.heater_block([f"power = {P} W", f"time = {t} s", f"Δθ = {dT} °C", "mass = 1.0 kg"]))


@template("c9x_shc_experiment_error", chapter=9, level=3, lo="9b")
def shc_experiment_error(rng):
    c_true = nice(rng, 900, 450)
    c_meas = c_true * nice(rng, 1.1, 1.15, 1.2)
    pct = (c_meas - c_true) / c_true * 100
    return mk(rng, pct, [((c_meas - c_true) / c_meas * 100, "Divide by the TRUE value."), (c_meas - c_true, "Give a percentage."), (c_meas / c_true * 100, "Find the percentage DIFFERENCE.")],
              "%", f"A student measures the specific heat capacity of a metal block.\n\n{md_table(['', 'specific heat capacity / J/(kg K)'], [['measured', fmt(c_meas)], ['accepted value', c_true]])}\n\nBy what percentage is the measured value too high? (Energy lost to the surroundings makes it too high.)",
              "% error = (measured − true) ÷ true × 100%", [f"= ({fmt(c_meas)} − {c_true}) ÷ {c_true} × 100% = **{fmt(pct)}%**"],
              ["Find the difference.", "Divide by the accepted value.", "× 100%."])


@template("c9x_heating_curve_power_melt", chapter=9, level=3, lo="9d")
def heating_curve_power_melt(rng):
    P = nice(rng, 50, 100, 200)
    t1 = nice(rng, 2, 3)
    dur = nice(rng, 4, 5, 6)
    mp = nice(rng, 50, 60)
    pts = [(0, 20), (t1, mp), (t1 + dur, mp), (t1 + dur + 3, mp + 30)]
    E = P * dur * 60
    return mk(rng, E, [(P * dur, "Convert minutes to seconds."), (P * (t1 + dur) * 60, "Use only the time of the flat section."), (E / 1000, "The answer is in J.")],
              "J", f"Fig. 1 shows the heating curve of a solid heated by a **{P} W** heater. Assuming no losses, how much energy is used to melt the solid?",
              "energy for melting = P × duration of the flat section", [f"flat section lasts {dur} min = {dur * 60} s", f"E = {P} × {dur * 60} = **{fmt(E)} J**"],
              ["Which section shows melting?", "How long does it last?", "E = P t with t in seconds."], figure=sketches.heating_curve(pts))


@template("c9x_cooling_energy_released", chapter=9, level=3, lo="9i")
def cooling_energy_released(rng):
    m = nice(rng, 0.05, 0.08, 0.1)
    L = nice(rng, 180000, 200000, 210000)
    return mk(rng, m * L, [(L / m, "Q = m L."), (m * L / 1000, "The answer is in J."), (L, "Multiply by the mass.")],
              "J", f"Liquid wax solidifies at its freezing point (the flat part of its cooling curve).\n\n{md_table(['quantity', 'value'], [['mass of wax', f'{fmt(m)} kg'], ['specific latent heat of fusion of wax', f'{L} J/kg']])}\n\nHow much energy does it release to the surroundings while solidifying?",
              "Q = m L (released on freezing)", [f"Q = {fmt(m)} × {L} = **{fmt(m * L)} J**"],
              ["Freezing releases the latent heat.", "Q = m L.", "Calculate."])


@template("c9x_cooling_rate_loss", chapter=9, level=3, lo="9i")
def cooling_rate_loss(rng):
    fp = nice(rng, 44, 48)
    dur = nice(rng, 5, 6, 8)
    P_loss = nice(rng, 20, 25, 30)
    t1 = 3
    pts = [(0, 80), (t1, fp), (t1 + dur, fp), (t1 + dur + 4, fp - 20)]
    E = P_loss * dur * 60
    return mk(rng, E, [(P_loss * dur, "Convert minutes to seconds."), (P_loss * (t1 + dur) * 60, "Use only the flat section."), (P_loss * t1 * 60, "Use the flat section, not the cooling of the liquid.")],
              "J", f"Fig. 1 shows the cooling curve of a liquid that solidifies. It loses energy to the surroundings at a steady **{P_loss} W**. How much latent heat is released during solidification?",
              "energy released while solidifying = rate of loss × duration of the flat section", [f"flat section lasts {dur} min = {dur * 60} s", f"E = {P_loss} × {dur * 60} = **{fmt(E)} J**"],
              ["During the flat part, the energy lost comes from latent heat.", "Find how long it lasts.", "E = P t."], figure=figs2.temp_time_graph(pts, ymax=100))


@template("c9x_kettle_time_boil", chapter=9, level=3, lo="9c")
def kettle_time_boil(rng):
    m = nice(rng, 0.5, 1.0, 1.5)
    T0 = nice(rng, 20, 25, 30)
    P = nice(rng, 2000, 2400, 3000)
    Q = m * C_WATER * (100 - T0)
    return mk(rng, Q / P, [(Q / P / 60, "The answer is in seconds."), (m * C_WATER * 100 / P, "Use the temperature RISE, 100 − start."), (Q * P, "t = Q ÷ P.")],
              "s", f"A kettle heats water to boiling point.\n\n{md_table(['quantity', 'value'], [['mass of water', f'{fmt(m)} kg'], ['starting temperature', f'{T0} °C'], ['power of kettle', f'{P} W'], ['specific heat capacity of water', '4200 J/(kg K)']])}\n\nAssuming no losses, how long does it take to reach 100 °C?",
              "Q = m c Δθ; t = Q ÷ P", [f"Q = {fmt(m)} × 4200 × {100 - T0} = {fmt(Q)} J", f"t = {fmt(Q)} ÷ {P} = **{fmt(Q / P)} s**"],
              ["Find the energy needed.", "Use the temperature rise.", "t = Q ÷ P."])


# ================================================================== L4
@template("c9x_internal_energy_cooling", chapter=9, level=4, lo="9a")
def internal_energy_cooling(rng):
    m = nice(rng, 0.25, 0.3, 0.5)
    T1 = nice(rng, 80, 90)
    T2 = nice(rng, 20, 25, 30)
    dU = m * C_WATER * (T1 - T2)
    return mk(rng, dU, [(m * C_WATER * T1, "Use the temperature CHANGE."), (C_WATER * (T1 - T2), "Multiply by the mass."), (dU / 1000, "The answer is in J.")],
              "J", f"Hot water cools in a room.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['initial temperature', f'{T1} °C'], ['final temperature', f'{T2} °C'], ['specific heat capacity', '4200 J/(kg K)']])}\n\nBy how much does its internal energy decrease?",
              "ΔU = m c Δθ", [f"ΔU = {fmt(m)} × 4200 × {T1 - T2} = **{fmt(dU)} J**"],
              ["The fall in internal energy is the energy lost.", "Use Q = m c Δθ.", "Δθ = initial − final."])


@template("c9x_internal_energy_melt_compare", chapter=9, level=4, lo="9a")
def internal_energy_melt_compare(rng):
    m = nice(rng, 0.1, 0.2, 0.5)
    dU_melt = m * L_ICE
    dU_warm = m * C_WATER * 10
    ratio = dU_melt / dU_warm
    return mk(rng, ratio, [(dU_warm / dU_melt, "Melting needs MORE energy than warming by 10 °C."), (L_ICE / C_WATER, "Include the 10 °C rise."), (dU_melt - dU_warm, "Find the ratio, not the difference.")],
              "times", f"{fmt(m)} kg of ice at 0 °C is melted, and the water is then warmed to 10 °C.\n\n{md_table(['constant', 'value'], [['specific latent heat of fusion', '334 000 J/kg'], ['specific heat capacity of water', '4200 J/(kg K)']])}\n\nHow many times greater is the increase in internal energy during melting than during warming?",
              "ΔU_melt = m L; ΔU_warm = m c Δθ; ratio", [f"melting: {fmt(dU_melt)} J; warming: {fmt(dU_warm)} J", f"ratio = **{fmt(ratio)}**"],
              ["Melting increases the potential energy of the particles.", "Warming increases their kinetic energy.", "Compare the two energies."])


@template("c9x_evap_rate_fan", chapter=9, level=4, lo="9e")
def evap_rate_fan(rng):
    m0 = nice(rng, 50.0, 60.0, 80.0)
    still = nice(rng, 1.2, 1.5, 2.0)
    fan = still * nice(rng, 2, 3)
    t = 10
    return mk(rng, (fan - still) / t, [(fan / t, "Find how much FASTER: subtract the rates."), (fan - still, "Divide by the time to get a rate."), ((fan + still) / t, "Subtract.")],
              "g/min", f"Two identical dishes of water are left for 10 minutes, one with a fan blowing over it.\n\n{md_table(['dish', 'start mass / g', 'mass after 10 min / g'], [['still air', fmt(m0), fmt(m0 - still)], ['fan', fmt(m0), fmt(m0 - fan)]])}\n\nHow much faster does the water evaporate with the fan, in g/min?",
              "rate = mass lost ÷ time; difference of rates", [f"still: {fmt(still)} ÷ 10 = {fmt(still / t)} g/min; fan: {fmt(fan)} ÷ 10 = {fmt(fan / t)} g/min", f"difference = **{fmt((fan - still) / t)} g/min**"],
              ["Find the mass lost by each.", "Divide by 10 min.", "Subtract."])


@template("c9x_evap_cooling_energy", chapter=9, level=4, lo="9e")
def evap_cooling_energy(rng):
    m_g = nice(rng, 10, 20, 25)
    L = 2400000
    Q = m_g / 1000 * L
    return mk(rng, Q, [(m_g * L, "Convert g to kg."), (m_g / 1000 * L_ICE, "Evaporation uses the latent heat of VAPORISATION."), (Q / 1000, "The answer is in J.")],
              "J", f"Sweat evaporates from a runner's skin, taking energy from the body.\n\n{md_table(['quantity', 'value'], [['mass of sweat evaporated', f'{m_g} g'], ['latent heat of vaporisation at skin temperature', '2 400 000 J/kg']])}\n\nHow much energy is removed from the body?",
              "Q = m L with m in kg", [f"Q = {fmt(m_g / 1000)} × 2 400 000 = **{fmt(Q)} J**"],
              ["Evaporation needs latent heat.", "Convert grams to kg.", "Q = m L."])


@template("c9x_boil_dry_time", chapter=9, level=4, lo="9g")
def boil_dry_time(rng):
    m = nice(rng, 0.2, 0.3, 0.5)
    P = nice(rng, 2000, 2500)
    t = m * L_STEAM / P
    return mk(rng, t, [(m * L_ICE / P, "Boiling away uses the latent heat of VAPORISATION."), (m * L_STEAM * P, "t = Q ÷ P."), (t / 60, "The answer is in seconds.")],
              "s", f"A kettle is left switched on after the water boils.\n\n{md_table(['quantity', 'value'], [['mass of water at 100 °C', f'{fmt(m)} kg'], ['power of kettle', f'{P} W'], ['specific latent heat of vaporisation', '2 260 000 J/kg']])}\n\nHow long would it take to boil all the water away (no losses)?",
              "Q = m L_v; t = Q ÷ P", [f"Q = {fmt(m)} × 2 260 000 = {fmt(m * L_STEAM)} J", f"t = {fmt(m * L_STEAM)} ÷ {P} = **{fmt(t)} s**"],
              ["Find the energy to vaporise the water.", "Q = m L.", "t = Q ÷ P."])


@template("c9x_steam_scald", chapter=9, level=4, lo="9c")
def steam_scald(rng):
    m = nice(rng, 0.002, 0.005, 0.01)
    T = nice(rng, 37, 40)
    Q_cond = m * L_STEAM
    Q_cool = m * C_WATER * (100 - T)
    return mk(rng, Q_cond + Q_cool, [(Q_cool, "Steam first CONDENSES, releasing latent heat, then cools."), (Q_cond, "Include the energy released as the water cools to skin temperature."), (m * C_WATER * T + Q_cond, "The water cools from 100 °C to skin temperature.")],
              "J", f"Steam at 100 °C condenses on the skin and the water then cools to skin temperature.\n\n{md_table(['quantity', 'value'], [['mass of steam', f'{fmt(m)} kg'], ['skin temperature', f'{T} °C'], ['specific latent heat of vaporisation', '2 260 000 J/kg'], ['specific heat capacity of water', '4200 J/(kg K)']])}\n\nHow much energy is released to the skin?",
              "Q = m L_v + m c Δθ", [f"condensing: {fmt(m)} × 2 260 000 = {fmt(Q_cond)} J", f"cooling: {fmt(m)} × 4200 × {100 - T} = {fmt(Q_cool)} J", f"total = **{fmt(Q_cond + Q_cool)} J**"],
              ["Two stages: condensing then cooling.", "Condensing releases m L.", "Cooling releases m c Δθ."])


@template("c9x_heating_curve_lv_ratio", chapter=9, level=4, lo="9d")
def heating_curve_lv_ratio(rng):
    melt = nice(rng, 2, 3)
    boil = melt * nice(rng, 6, 7)
    pts = [(0, -20), (2, 0), (2 + melt, 0), (2 + melt + 5, 100), (2 + melt + 5 + boil, 100)]
    return mk(rng, boil / melt, [(melt / boil, "Boiling takes LONGER, so the ratio is more than 1."), (boil - melt, "Find the ratio of the times."), (boil, "Divide by the melting time.")],
              "times", "Fig. 1 shows ice heated steadily until it has all boiled. Using the flat sections, how many times greater is the specific latent heat of vaporisation than that of fusion?",
              "same heater, same mass: L ∝ time on the flat section", [f"melting: {melt} min; boiling: {boil} min", f"ratio = {boil} ÷ {melt} = **{fmt(boil / melt)}**"],
              ["Energy supplied ∝ time.", "Same mass melts and boils.", "Ratio of the flat-section times."], figure=figs2.temp_time_graph(pts, ymax=120, xstep=5))


@template("c9x_heating_curve_state_energy", chapter=9, level=4, lo="9d")
def heating_curve_state_energy(rng):
    P = nice(rng, 100, 150)
    t_l = nice(rng, 4, 5, 6)
    pts = [(0, 10), (3, 50), (6, 50), (6 + t_l, 90)]
    E = P * t_l * 60
    return mk(rng, E, [(P * t_l, "Convert minutes to seconds."), (P * 3 * 60, "Use the LIQUID section (after the flat part)."), (P * (6 + t_l) * 60, "Use only the liquid section.")],
              "J", f"Fig. 1 shows a solid heated by a **{P} W** heater until it is a liquid at 90 °C. Assuming no losses, how much energy is supplied while the substance is a LIQUID?",
              "liquid section: after the plateau; E = P × time", [f"liquid from 6 min to {6 + t_l} min = {t_l} min = {t_l * 60} s", f"E = {P} × {t_l * 60} = **{fmt(E)} J**"],
              ["Which section is the liquid?", "After the flat section.", "E = P t."], figure=sketches.heating_curve(pts))


# ================================================================== L5
@template("c9x_ice_in_drink", chapter=9, level=5, lo="9g")
def ice_in_drink(rng):
    m_w = nice(rng, 0.2, 0.25, 0.3)
    T1 = nice(rng, 25, 30)
    m_i = nice(rng, 0.02, 0.03, 0.04)
    Tf = (m_w * C_WATER * T1 - m_i * L_ICE) / ((m_w + m_i) * C_WATER)
    return mk(rng, Tf, [((m_w * T1) / (m_w + m_i), "Include the latent heat needed to MELT the ice first."), (T1 - m_i * L_ICE / (m_w * C_WATER), "The melted ice also warms from 0 °C to the final temperature."), ((m_w * C_WATER * T1 + m_i * L_ICE) / ((m_w + m_i) * C_WATER), "Melting the ice TAKES energy from the drink.")],
              "°C", f"Ice at 0 °C is added to a drink (treat as water) in an insulated cup.\n\n{md_table(['quantity', 'value'], [['mass of drink', f'{fmt(m_w)} kg at {T1} °C'], ['mass of ice', f'{fmt(m_i)} kg at 0 °C'], ['c (water)', '4200 J/(kg K)'], ['L (fusion)', '334 000 J/kg']])}\n\nWhat is the final temperature once all the ice has melted?",
              "m_w c (T₁ − T) = m_i L + m_i c (T − 0)", [f"{fmt(m_w)}×4200×({T1} − T) = {fmt(m_i)}×334 000 + {fmt(m_i)}×4200×T", f"T = **{fmt(Tf, sf=3)} °C**"],
              ["Energy lost by the drink = energy to melt the ice + to warm the meltwater.", "Set up the energy balance.", "Solve for T."], sf=3)


@template("c9x_steam_heat_water", chapter=9, level=5, lo="9g")
def steam_heat_water(rng):
    m_w = nice(rng, 0.5, 1.0)
    T1 = nice(rng, 20, 25)
    T2 = nice(rng, 40, 50)
    per_kg = L_STEAM + C_WATER * (100 - T2)
    m_s = m_w * C_WATER * (T2 - T1) / per_kg
    return mk(rng, m_s * 1000, [(m_w * C_WATER * (T2 - T1) / L_STEAM * 1000, "The condensed steam also cools from 100 °C to the final temperature."), (m_s, "That is in kg; the answer is in g."), (m_w * C_WATER * (T2 - T1) / (C_WATER * (100 - T2)) * 1000, "Include the latent heat released on condensing.")],
              "g", f"Steam at 100 °C is bubbled into water until the water reaches **{T2} °C**.\n\n{md_table(['quantity', 'value'], [['mass of water', f'{fmt(m_w)} kg at {T1} °C'], ['L (vaporisation)', '2 260 000 J/kg'], ['c (water)', '4200 J/(kg K)']])}\n\nWhat mass of steam is needed (no losses)?",
              "m_s (L + c (100 − T₂)) = m_w c (T₂ − T₁)", [f"energy gained by water = {fmt(m_w)} × 4200 × {T2 - T1} = {fmt(m_w * C_WATER * (T2 - T1))} J", f"per kg of steam: 2 260 000 + 4200 × {100 - T2} = {fmt(per_kg)} J", f"m_s = **{fmt(m_s * 1000)} g**"],
              ["Each kg of steam releases latent heat and then cools.", "Set energy released = energy gained.", "Solve for m_s."])


@template("c9x_shc_from_mixing", chapter=9, level=5, lo="9b")
def shc_from_mixing(rng):
    m_b = nice(rng, 0.2, 0.5)
    c = nice(rng, 400, 450, 900)
    m_w = nice(rng, 0.2, 0.3)
    T_b, T_w = 100, nice(rng, 20, 22)
    Tf = (m_b * c * T_b + m_w * C_WATER * T_w) / (m_b * c + m_w * C_WATER)
    Tf = round(Tf, 1)
    c_calc = m_w * C_WATER * (Tf - T_w) / (m_b * (T_b - Tf))
    return mk(rng, c_calc, [(m_w * C_WATER * (Tf - T_w) / (m_b * Tf), "The block cools from 100 °C to the final temperature: Δθ = 100 − T_f."), (m_w * C_WATER * (Tf - T_w) / (T_b - Tf), "Divide by the block's mass too."), (C_WATER, "That is water's specific heat capacity.")],
              "J/(kg K)", f"A metal block at 100 °C is dropped into water in an insulated cup.\n\n{md_table(['quantity', 'value'], [['mass of block', f'{fmt(m_b)} kg'], ['mass of water', f'{fmt(m_w)} kg'], ['initial water temperature', f'{T_w} °C'], ['final temperature', f'{fmt(Tf)} °C'], ['c (water)', '4200 J/(kg K)']])}\n\nWhat is the specific heat capacity of the metal?",
              "energy lost by block = energy gained by water: m_b c (100 − T_f) = m_w c_w (T_f − T_w)", [f"gained by water = {fmt(m_w)} × 4200 × {fmt(Tf - T_w)} = {fmt(m_w * C_WATER * (Tf - T_w))} J", f"c = {fmt(m_w * C_WATER * (Tf - T_w))} ÷ ({fmt(m_b)} × {fmt(T_b - Tf)}) = **{fmt(c_calc)} J/(kg K)**"],
              ["Energy lost = energy gained.", "Find the water's gain.", "Divide by m_b × Δθ_b."])


@template("c9x_coolant_compare", chapter=9, level=5, lo="9b")
def coolant_compare(rng):
    P = nice(rng, 20000, 30000)
    dT = nice(rng, 10, 15)
    c_o = nice(rng, 2000, 2100)
    ratio = C_WATER / c_o
    return mk(rng, ratio, [(c_o / C_WATER, "Water has the HIGHER c, so it needs LESS mass flow; oil needs more."), (C_WATER - c_o, "Find the ratio."), (ratio * dT, "Δθ is the same for both; it cancels.")],
              "times", f"An engine must lose **{P} W** to its coolant, which may warm by at most **{dT} °C**.\n\n{md_table(['coolant', 'specific heat capacity / J/(kg K)'], [['water', 4200], ['oil', c_o]])}\n\nHow many times greater a mass of oil than of water must flow through each second?",
              "mass per second = P ÷ (c Δθ) → ratio = c_water ÷ c_oil", [f"ratio = 4200 ÷ {c_o} = **{fmt(ratio)}**"],
              ["Energy per second = (mass per second) × c × Δθ.", "P and Δθ are the same.", "Mass flow ∝ 1/c."])


@template("c9x_cooling_curve_lauric", chapter=9, level=5, lo="9i")
def cooling_curve_lauric(rng):
    fp = nice(rng, 44, 48)
    r1 = nice(rng, 5, 6, 8)
    pts = [(0, fp + 3 * r1), (3, fp), (9, fp), (12, fp - 12)]
    return mk(rng, r1, [(r1 * 3, "Divide by the time (3 min)."), (4, "That is the rate for the SOLID after solidifying."), (fp / 3, "Use the temperature DROP, not the temperature.")],
              "°C/min", f"Fig. 1 shows the cooling curve of liquid lauric acid. What is the average rate of cooling of the LIQUID before it starts to solidify?",
              "rate = drop ÷ time for the first section", [f"drop = {fp + 3 * r1} − {fp} = {3 * r1} °C in 3 min", f"rate = **{fmt(r1)} °C/min**"],
              ["Use the first (sloping) section.", "Find the drop and the time.", "Divide."], figure=figs2.temp_time_graph(pts, ymax=100))


@template("c9x_cooling_curve_mass", chapter=9, level=5, lo="9i")
def cooling_curve_mass(rng):
    P_loss = nice(rng, 15, 20, 25)
    dur = nice(rng, 6, 8, 10)
    L = nice(rng, 180000, 200000)
    m = P_loss * dur * 60 / L
    fp = 44
    pts = [(0, 80), (3, fp), (3 + dur, fp), (7 + dur, fp - 20)]
    return mk(rng, m * 1000, [(P_loss * dur / L * 1000, "Convert minutes to seconds."), (m, "That is in kg; the answer is in g."), (P_loss * (3 + dur) * 60 / L * 1000, "Use only the flat section.")],
              "g", f"Fig. 1 shows a cooling curve of a liquid in a beaker. It loses energy at a steady **{P_loss} W**, and its specific latent heat of fusion is **{L} J/kg**. What is the mass of the substance?",
              "latent heat released = P × flat time = m L → m = P t ÷ L", [f"E = {P_loss} × {dur * 60} = {P_loss * dur * 60} J", f"m = {P_loss * dur * 60} ÷ {L} = {fmt(m)} kg = **{fmt(m * 1000)} g**"],
              ["The flat section releases latent heat.", "E = P t.", "m = E ÷ L."], figure=figs2.temp_time_graph(pts, ymax=100))


@template("c9x_internal_energy_two_blocks", chapter=9, level=5, lo="9a")
def internal_energy_two_blocks(rng):
    m1, c1 = nice(rng, 1.0, 2.0), 900
    m2, c2 = nice(rng, 1.0, 2.0), 390
    dT = nice(rng, 10, 20)
    d1, d2 = m1 * c1 * dT, m2 * c2 * dT
    return mk(rng, d1 - d2, [(d1 + d2, "Find how much MORE, so subtract."), (d1, "That is only the aluminium's increase."), ((c1 - c2) * dT, "Multiply each by its own mass.")],
              "J", f"Two blocks are heated through the same temperature rise of **{dT} °C**.\n\n{md_table(['block', 'mass / kg', 'specific heat capacity / J/(kg K)'], [['aluminium', fmt(m1), c1], ['copper', fmt(m2), c2]])}\n\nHow much more does the internal energy of the aluminium block increase than that of the copper block?",
              "ΔU = m c Δθ for each; subtract", [f"aluminium: {fmt(m1)}×900×{dT} = {fmt(d1)} J; copper: {fmt(m2)}×390×{dT} = {fmt(d2)} J", f"difference = **{fmt(d1 - d2)} J**"],
              ["ΔU = m c Δθ.", "Work out each block.", "Subtract."])


@template("c9x_internal_energy_total_process", chapter=9, level=5, lo="9a")
def internal_energy_total_process(rng):
    m = nice(rng, 0.1, 0.2)
    T0 = nice(rng, 20, 30)
    dU = m * C_WATER * (100 - T0) + m * L_STEAM
    return mk(rng, dU, [(m * C_WATER * (100 - T0), "Boiling also increases the internal energy (potential energy of the particles)."), (m * L_STEAM, "Include heating to 100 °C first."), (m * C_WATER * 100 + m * L_STEAM, "Use the temperature rise 100 − start.")],
              "J", f"Water is heated from **{T0} °C** to 100 °C and then completely boiled away.\n\n{md_table(['quantity', 'value'], [['mass', f'{fmt(m)} kg'], ['c (water)', '4200 J/(kg K)'], ['L (vaporisation)', '2 260 000 J/kg']])}\n\nWhat is the total increase in internal energy (no losses)?",
              "ΔU = m c Δθ + m L", [f"heating: {fmt(m)} × 4200 × {100 - T0} = {fmt(m * C_WATER * (100 - T0))} J", f"boiling: {fmt(m)} × 2 260 000 = {fmt(m * L_STEAM)} J", f"total = **{fmt(dU)} J**"],
              ["Two stages.", "Heating raises KE; boiling raises PE.", "Add the energies."])
