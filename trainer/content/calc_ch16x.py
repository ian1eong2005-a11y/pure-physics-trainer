"""Chapter 16 Practical Electricity (6091) bank extension: calculation and data-reading templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: kettles, heaters and irons, rating plates,
electricity bills, fuse choice, overloaded sockets, extension cables, earthed metal cases; school papers 2024-2025)."""
from .. import figs3
from .base import fmt, md_table, mk, mkt, nice, template

FUSES = [3, 5, 13]


def fuse_for(I):
    return next(f for f in FUSES if f > I)


# ================================================================== L1
@template("c16x_power_vi_simple", chapter=16, level=1, lo="16b")
def power_vi_simple(rng):
    V = nice(rng, 12, 230)
    I = nice(rng, 0.5, 2.0, 4.0, 8.0)
    return mk(rng, V * I, [(V / I, "P = V × I."), (I / V, "Multiply p.d. by current."), (V + I, "Multiply.")],
              "W", f"{md_table(['quantity', 'value'], [['p.d. across appliance', f'{V} V'], ['current', f'{fmt(I)} A']])}\n\nWhat is its power?",
              "P = V I", [f"P = {V} × {fmt(I)} = **{fmt(V * I)} W**"],
              ["Power = p.d. × current.", "P = V I.", "Multiply."])


@template("c16x_kwh_simple", chapter=16, level=1, lo="16c")
def kwh_simple(rng):
    P = nice(rng, 500, 1000, 1500, 2000, 3000)
    t = nice(rng, 0.5, 1, 2, 3, 4)
    return mk(rng, P / 1000 * t, [(P * t, "Convert W to kW first."), (P / 1000 / t, "E = P × t."), (P / 1000 * t * 60, "The time is already in hours.")],
              "kWh", f"{md_table(['quantity', 'value'], [['power of appliance', f'{P} W'], ['time switched on', f'{fmt(t)} h']])}\n\nHow much energy does it use, in kWh?",
              "E (kWh) = P (kW) × t (h)", [f"P = {fmt(P / 1000)} kW", f"E = {fmt(P / 1000)} × {fmt(t)} = **{fmt(P / 1000 * t)} kWh**"],
              ["Convert the power to kW.", "Time in hours.", "Multiply."])


@template("c16x_heating_energy_kettle", chapter=16, level=1, lo="16a")
def heating_energy_kettle(rng):
    P = nice(rng, 2000, 2200, 2500, 3000)
    t = nice(rng, 60, 90, 120, 180)
    return mk(rng, P * t / 1000, [(P * t, "That is in J; the answer is in kJ."), (P / t, "E = P × t."), (P * t / 1e6, "1 kJ = 1000 J.")],
              "kJ", f"An electric kettle uses the heating effect of a current.\n\n{md_table(['quantity', 'value'], [['power', f'{P} W'], ['time', f'{t} s']])}\n\nHow much thermal energy does the element produce, in kJ?",
              "E = P t", [f"E = {P} × {t} = {P * t} J = **{fmt(P * t / 1000)} kJ**"],
              ["Energy = power × time.", "Use seconds.", "Convert to kJ."])


@template("c16x_heating_appliance_table", chapter=16, level=1, lo="16a")
def heating_appliance_table(rng):
    rows = [("kettle", 2200, True), ("television", 120, False), ("toaster", 900, True), ("phone charger", 10, False), ("radio", 15, False), ("iron", 1100, True)]
    pick = rng.sample(rows, 4)
    if not any(h for _, _, h in pick):
        pick[0] = rows[0]
    heat = [r for r in pick if r[2]]
    ans = max(heat, key=lambda r: r[1])[0]
    wrongs = {n: ("It does not mainly use the heating effect." if not h else "It uses the heating effect, but with a lower power.") for n, p, h in pick if n != ans}
    while len(wrongs) < 3:
        extra = next(r for r in rows if r[0] not in wrongs and r[0] != ans)
        wrongs[extra[0]] = "Compare the heating appliances' power ratings."
    table = md_table(["appliance", "power / W"], [[n, p] for n, p, _ in pick])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"{table}\n\nWhich of these appliances, designed to use the heating effect of a current, converts the most energy each second?",
               "heating appliances: kettles, toasters, irons; largest power → most energy per second", [f"**{ans}**"],
               ["Which appliances are meant to heat?", "Compare their powers.", "Largest power."])


@template("c16x_fuse_simple", chapter=16, level=1, lo="16e")
def fuse_simple(rng):
    I = nice(rng, 1.5, 2.2, 4.0, 8.7, 10.0)
    ans = f"{fuse_for(I)} A"
    wrongs = {f"{f} A": ("This fuse would blow in normal use." if f < I else "This fuse is too large to protect the cable well.") for f in FUSES if f"{f} A" != ans}
    wrongs["30 A"] = "Plug fuses are 3 A, 5 A or 13 A."
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"{md_table(['quantity', 'value'], [['normal current in appliance', f'{fmt(I)} A'], ['fuses available', '3 A, 5 A, 13 A']])}\n\nWhich fuse should be fitted?",
               "choose the smallest fuse rating just above the normal current", [f"smallest above {fmt(I)} A → **{ans}**"],
               ["The fuse must not blow in normal use.", "But it should be as small as possible.", "Just above the current."])


@template("c16x_fuse_from_power", chapter=16, level=1, lo="16e")
def fuse_from_power(rng):
    P = nice(rng, 300, 600, 1000, 2000, 2500)
    I = P / 230
    ans = f"{fuse_for(I)} A"
    wrongs = {f"{f} A": ("It would blow when the appliance is used." if f < I else "Too large: it would not protect against a smaller overload.") for f in FUSES if f"{f} A" != ans}
    wrongs["1 A"] = "Calculate I = P ÷ V first."
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"An appliance is rated **{P} W, 230 V**.\n\n{md_table(['fuses available', ''], [['3 A, 5 A, 13 A', '']])}\n\nWhich fuse should be fitted?",
               "I = P ÷ V; choose the next fuse above I", [f"I = {P} ÷ 230 = {fmt(I, sf=3)} A → **{ans}**"],
               ["Find the current.", "I = P ÷ V.", "Choose the next fuse above it."])


@template("c16x_socket_total_current", chapter=16, level=1, lo="16d")
def socket_total_current(rng):
    Is = [nice(rng, 4.0, 5.0), nice(rng, 6.0, 7.0), nice(rng, 3.0, 4.5)]
    tot = sum(Is)
    return mk(rng, tot, [(max(Is), "All the appliances draw current at once: add them."), (tot / 3, "Add, do not average."), (Is[0] + Is[1], "Include all three.")],
              "A", f"Three appliances are plugged into one multi-socket adaptor.\n\n{md_table(['appliance', 'current / A'], [[i + 1, fmt(x)] for i, x in enumerate(Is)])}\n\nWhat total current flows in the adaptor's cable? (Too much current can overheat the cable.)",
              "parallel appliances: currents add", [f"I = {' + '.join(fmt(x) for x in Is)} = **{fmt(tot)} A**"],
              ["The appliances are in parallel.", "Their currents add.", "Add them."])


@template("c16x_overload_check", chapter=16, level=1, lo="16d")
def overload_check(rng):
    Is = [nice(rng, 5, 6), nice(rng, 4, 5), nice(rng, 3, 4)]
    rating = 13
    tot = sum(Is)
    ans = "yes, the total exceeds 13 A" if tot > rating else "no, the total is below 13 A"
    wrongs = {("no, the total is below 13 A" if tot > rating else "yes, the total exceeds 13 A"): f"Add the currents: total = {fmt(tot)} A.",
              "only if they are switched on one at a time": "Overload happens when they are on together.", "it depends on the colour of the cable": "Colour is not relevant."}
    table = md_table(["appliance", "current / A"], [[i + 1, x] for i, x in enumerate(Is)])
    return mkt(rng, ans, wrongs, f"Three appliances are used together on one extension lead rated at **13 A**.\n\n{table}\n\nIs the lead overloaded?",
               "total current = sum; overloaded if > rating", [f"total = {fmt(tot)} A → **{ans}**"],
               ["Add the currents.", "Compare with 13 A.", "Overloaded if larger."])


# ================================================================== L2
@template("c16x_cost_simple", chapter=16, level=2, lo="16c")
def cost_simple(rng):
    P = nice(rng, 1000, 1500, 2000, 2500)
    t = nice(rng, 2, 3, 4, 5)
    price = nice(rng, 25, 30, 32)
    E = P / 1000 * t
    return mk(rng, E * price, [(E, "That is the energy in kWh; multiply by the price."), (P * t * price, "Convert W to kW."), (P / 1000 * price, "Multiply by the time too.")],
              "cents", f"{md_table(['quantity', 'value'], [['power of heater', f'{P} W'], ['time', f'{t} h'], ['cost of 1 kWh', f'{price} cents']])}\n\nHow much does it cost to run?",
              "E = P(kW) × t(h); cost = E × price", [f"E = {fmt(P / 1000)} × {t} = {fmt(E)} kWh", f"cost = {fmt(E)} × {price} = **{fmt(E * price)} cents**"],
              ["Find the kWh used.", "Multiply by the price per kWh.", "Answer in cents."])


@template("c16x_kwh_minutes", chapter=16, level=2, lo="16c")
def kwh_minutes(rng):
    P = nice(rng, 1200, 1800, 2400)
    t_min = nice(rng, 15, 30, 45)
    E = P / 1000 * t_min / 60
    return mk(rng, E, [(P / 1000 * t_min, "Convert minutes to hours."), (P * t_min / 60, "Convert W to kW."), (E * 60, "Divide the minutes by 60.")],
              "kWh", f"{md_table(['quantity', 'value'], [['power of hair dryer', f'{P} W'], ['time used', f'{t_min} min']])}\n\nHow much energy is used, in kWh?",
              "E = P(kW) × t(h)", [f"P = {fmt(P / 1000)} kW; t = {fmt(t_min / 60)} h", f"E = **{fmt(E)} kWh**"],
              ["Convert to kW.", "Convert minutes to hours.", "Multiply."])


@template("c16x_fuse_compare_appliances", chapter=16, level=2, lo="16e")
def fuse_compare_appliances(rng):
    rows = [("lamp", 60), ("hair dryer", 1200), ("kettle", 2400), ("TV", 150)]
    which = rng.choice(rows)
    I = which[1] / 230
    ans = f"{fuse_for(I)} A"
    wrongs = {f"{f} A": "Calculate I = P ÷ 230 and choose the next rating above." for f in FUSES if f"{f} A" != ans}
    wrongs["10 A"] = "Plug fuses come in 3 A, 5 A and 13 A."
    table = md_table(["appliance (230 V)", "power / W"], [[n, p] for n, p in rows])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"{table}\n\nWhich fuse (3 A, 5 A or 13 A) should be fitted to the **{which[0]}**?",
               "I = P ÷ V; next fuse above", [f"I = {which[1]} ÷ 230 = {fmt(I, sf=3)} A → **{ans}**"],
               ["Find the current for that appliance.", "I = P ÷ V.", "Choose the fuse."])


@template("c16x_breaker_trip", chapter=16, level=2, lo="16e")
def breaker_trip(rng):
    rating = nice(rng, 16, 20, 32)
    P_each = nice(rng, 1000, 1500, 2000)
    n_max = int(rating * 230 // P_each)
    return mk(rng, n_max, [(n_max + 1, "That many would draw more than the rating and trip it."), (rating * 230 / P_each, "Only whole heaters: round DOWN."), (rating, "That is the current rating, not a number of heaters.")],
              "heaters", f"A circuit breaker on a ring main trips at **{rating} A**.\n\n{md_table(['quantity', 'value'], [['mains p.d.', '230 V'], ['power of each heater', f'{P_each} W']])}\n\nWhat is the greatest number of heaters that can be used at once without tripping it?",
              "max power = I × V; number = max power ÷ P each (round down)", [f"max power = {rating} × 230 = {rating * 230} W", f"{rating * 230} ÷ {P_each} = {fmt(rating * 230 / P_each)} → **{n_max}**"],
              ["Find the maximum power allowed.", "Divide by one heater's power.", "Round down."], dp=0)


@template("c16x_iron_heating", chapter=16, level=2, lo="16a")
def iron_heating(rng):
    P = nice(rng, 1000, 1100, 1200)
    t_min = nice(rng, 5, 10, 15)
    E = P * t_min * 60 / 1000
    return mk(rng, E, [(P * t_min, "Convert minutes to seconds."), (P * t_min * 60, "That is in J; give kJ."), (P * t_min / 60, "Multiply by 60 to get seconds.")],
              "kJ", f"An electric iron (Fig. 1 shows its rating plate) is used for **{t_min} minutes**. How much thermal energy does it produce, in kJ?",
              "E = P t", [f"t = {t_min * 60} s", f"E = {P} × {t_min * 60} = **{fmt(E)} kJ**"],
              ["Read the power from the plate.", "Convert the time to seconds.", "E = P t."], figure=figs3.rating_plate(["ELECTRIC IRON", "230 V ~ 50 Hz", f"{P} W"]))


@template("c16x_heater_temperature_rise", chapter=16, level=2, lo="16a")
def heater_temperature_rise(rng):
    P = nice(rng, 500, 1000)
    t = nice(rng, 60, 120)
    m = nice(rng, 0.5, 1.0)
    dT = P * t / (m * 4200)
    return mk(rng, dT, [(P * t / 4200, "Divide by the mass too."), (P * t / m, "Divide by c = 4200 too."), (P / (m * 4200), "Multiply power by time first.")],
              "°C", f"An immersion heater heats water using the heating effect of a current.\n\n{md_table(['quantity', 'value'], [['power', f'{P} W'], ['time', f'{t} s'], ['mass of water', f'{fmt(m)} kg'], ['c (water)', '4200 J/(kg K)']])}\n\nWhat is the temperature rise (no losses)?",
              "P t = m c Δθ", [f"E = {P} × {t} = {P * t} J", f"Δθ = {P * t} ÷ ({fmt(m)} × 4200) = **{fmt(dT)} °C**"],
              ["Find the energy supplied.", "E = m c Δθ.", "Solve for Δθ."])


@template("c16x_cable_power_loss", chapter=16, level=2, lo="16d")
def cable_power_loss(rng):
    I = nice(rng, 5, 8, 10, 13)
    R = nice(rng, 0.1, 0.2, 0.5)
    return mk(rng, I * I * R, [(I * R, "P = I² R: square the current."), (I * I / R, "Multiply by R."), (I * R * R, "Square the current, not the resistance.")],
              "W", f"A current flows in an extension cable, which heats up a little.\n\n{md_table(['quantity', 'value'], [['current', f'{I} A'], ['resistance of cable', f'{fmt(R)} Ω']])}\n\nAt what rate is energy converted to heat in the cable?",
              "P = I² R", [f"P = {I}² × {fmt(R)} = **{fmt(I * I * R)} W**"],
              ["Heating in a wire: P = I² R.", "Square the current.", "Multiply by R."])


@template("c16x_coiled_cable", chapter=16, level=2, lo="16d")
def coiled_cable(rng):
    I1 = nice(rng, 4, 5)
    k = nice(rng, 2, 3)
    return mk(rng, k * k, [(k, "Heating ∝ I²: square the current factor."), (k * 2, "Square, do not double."), (1, "More current gives more heating.")],
              "times", f"The heating in a cable is proportional to the square of the current.\n\n{md_table(['situation', 'current / A'], [['one appliance', I1], ['several appliances', I1 * k]])}\n\nHow many times greater is the rate of heating in the cable with several appliances?",
              "P ∝ I² → factor = (I₂ ÷ I₁)²", [f"factor = {k}² = **{k * k}**"],
              ["P = I² R.", "R is the same.", "Square the ratio."], dp=0)


# ================================================================== L3
@template("c16x_cost_week", chapter=16, level=3, lo="16c")
def cost_week(rng):
    P = nice(rng, 100, 150, 200)
    h = nice(rng, 4, 5, 6, 8)
    days = 7
    price = nice(rng, 25, 30)
    E = P / 1000 * h * days
    return mk(rng, E * price, [(P / 1000 * h * price, "Multiply by 7 days."), (P * h * days * price, "Convert W to kW."), (E, "That is the energy; multiply by the price.")],
              "cents", f"{md_table(['quantity', 'value'], [['power of TV', f'{P} W'], ['hours used each day', h], ['days', days], ['cost of 1 kWh', f'{price} cents']])}\n\nWhat does it cost to run for the week?",
              "E = P(kW) × total hours; cost = E × price", [f"E = {fmt(P / 1000)} × {h} × {days} = {fmt(E)} kWh", f"cost = **{fmt(E * price)} cents**"],
              ["Find the total hours.", "Find the kWh.", "Multiply by the price."])


@template("c16x_meter_cost", chapter=16, level=3, lo="16c")
def meter_cost(rng):
    r1 = nice(rng, 12345, 23456, 34567)
    used = nice(rng, 250, 320, 410)
    r2 = r1 + used
    price = nice(rng, 28, 30, 32)
    return mk(rng, used * price / 100, [(used * price, "That is in cents; give dollars."), (used / 100, "Multiply by the price per kWh."), (r2 * price / 100, "Use the DIFFERENCE between the readings.")],
              "dollars", f"Electricity meter readings for one month:\n\n{md_table(['reading', 'kWh'], [['start of month', r1], ['end of month', r2]])}\n\nThe price is **{price} cents per kWh**. What is the bill, in dollars?",
              "units used = end − start; cost = units × price", [f"used = {r2} − {r1} = {used} kWh", f"cost = {used} × {price} = {used * price} cents = **${fmt(used * price / 100)}**"],
              ["Subtract the readings.", "Multiply by the price.", "Convert cents to dollars."])


@template("c16x_fuse_appliance_power_choice", chapter=16, level=3, lo="16e")
def fuse_appliance_power_choice(rng):
    P = nice(rng, 700, 1050, 1150)
    I = P / 230
    ans = f"{fuse_for(I)} A"
    wrongs = {"13 A": "13 A would work, but a smaller fuse gives better protection.", "3 A": f"I = {fmt(I, sf=3)} A, so a 3 A fuse would blow." if I > 3 else "Compare with the current.",
              "5 A": f"I = {fmt(I, sf=3)} A, so a 5 A fuse would blow." if I > 5 else "Compare with the current.", "2 A": "Too small."}
    wrongs = {k: v for k, v in wrongs.items() if k != ans}
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"A microwave oven's rating plate reads **{P} W, 230 V** (Fig. 1). Which fuse (3 A, 5 A or 13 A) should be fitted?",
               "I = P ÷ V; choose the smallest fuse above I", [f"I = {P} ÷ 230 = {fmt(I, sf=3)} A → **{ans}**"],
               ["Read P and V from the plate.", "I = P ÷ V.", "Choose the fuse just above."], figure=figs3.rating_plate(["MICROWAVE OVEN", "230 V ~ 50 Hz", f"{P} W"]))


@template("c16x_current_kettle", chapter=16, level=3, lo="16b")
def current_kettle(rng):
    P = nice(rng, 2000, 2300, 2760, 3000)
    return mk(rng, P / 230, [(P * 230, "I = P ÷ V."), (230 / P, "Power goes on top."), (P / 230 / 1000, "The answer is in A.")],
              "A", f"Fig. 1 shows a kettle's rating plate: **{P} W, 230 V**. What current does it take?",
              "I = P ÷ V", [f"I = {P} ÷ 230 = **{fmt(P / 230, sf=3)} A**"],
              ["Rearrange P = V I.", "I = P ÷ V.", "Divide."], figure=figs3.rating_plate(["KETTLE", "230 V ~ 50 Hz", f"{P} W"]), sf=3)


@template("c16x_resistance_from_power", chapter=16, level=3, lo="16b")
def resistance_from_power(rng):
    P = nice(rng, 1000, 2000, 2300)
    V = 230
    R = V * V / P
    return mk(rng, R, [(P / V, "That is the current; R = V² ÷ P."), (V / P, "R = V² ÷ P."), (P / V ** 2, "Invert: R = V² ÷ P.")],
              "Ω", f"Fig. 1 shows the rating plate of a heater (**{P} W**, **230 V**). What is the resistance of its element when working?",
              "P = V² ÷ R → R = V² ÷ P", [f"R = 230² ÷ {P} = **{fmt(R, sf=3)} Ω**"],
              ["Use P = V² ÷ R.", "Rearrange for R.", "Calculate."], figure=figs3.rating_plate(["HEATER", "230 V ~ 50 Hz", f"{P} W"]), sf=3)


@template("c16x_cable_rating", chapter=16, level=3, lo="16d")
def cable_rating(rng):
    rows = [("thin (0.5 mm²)", 3), ("medium (0.75 mm²)", 6), ("thick (1.5 mm²)", 13), ("very thick (2.5 mm²)", 20)]
    P = nice(rng, 1000, 1400, 2500)
    I = P / 230
    ans = next(n for n, r in rows if r >= I)
    wrongs = {n: ("This cable would overheat: its rating is below the current." if r < I else "This works but is thicker than needed.") for n, r in rows if n != ans}
    table = md_table(["cable", "maximum safe current / A"], [[n, r] for n, r in rows])
    return mkt(rng, ans, wrongs, f"A **{P} W, 230 V** appliance needs a flex.\n\n{table}\n\nWhich is the thinnest cable that can safely be used?",
               "I = P ÷ V; cable rating must be at least I", [f"I = {P} ÷ 230 = {fmt(I, sf=3)} A → **{ans}**"],
               ["Find the current.", "The cable must carry it without overheating.", "Choose the thinnest that is enough."])


@template("c16x_heating_effect_compare", chapter=16, level=3, lo="16a")
def heating_effect_compare(rng):
    P1, P2 = nice(rng, 1000, 1200), nice(rng, 2000, 2400)
    t = nice(rng, 60, 120, 180)
    return mk(rng, (P2 - P1) * t / 1000, [(P2 * t / 1000, "Find the DIFFERENCE in energy."), ((P2 - P1) * t, "Convert J to kJ."), ((P2 + P1) * t / 1000, "Subtract.")],
              "kJ", f"Two heaters run for the same time.\n\n{md_table(['heater', 'power / W'], [['A', P1], ['B', P2]])}\n\nHow much more thermal energy does B produce in **{t} s**, in kJ?",
              "ΔE = (P_B − P_A) × t", [f"ΔE = ({P2} − {P1}) × {t} = {(P2 - P1) * t} J = **{fmt((P2 - P1) * t / 1000)} kJ**"],
              ["Energy = P t for each.", "Or use the power difference.", "Convert to kJ."])


@template("c16x_toaster_element", chapter=16, level=3, lo="16a")
def toaster_element(rng):
    V = 230
    R = nice(rng, 46, 53, 60)
    P = V * V / R
    return mk(rng, P, [(V / R, "That is the current; P = V² ÷ R."), (V * R, "P = V² ÷ R."), (V * V * R, "Divide by R.")],
              "W", f"A toaster's heating element of resistance **{R} Ω** is connected to the **230 V** mains (Fig. 1). What is its power?",
              "P = V² ÷ R", [f"P = 230² ÷ {R} = **{fmt(P, sf=3)} W**"],
              ["Use P = V² ÷ R.", "Square the p.d.", "Divide by R."], figure=figs3.circuit(emf="230 V", top=[("R", f"{R} Ω")]), sf=3)


@template("c16x_adaptor_spare_capacity", chapter=16, level=3, lo="16d")
def adaptor_spare_capacity(rng):
    Ps = [nice(rng, 800, 1000), nice(rng, 500, 600)]
    I_used = sum(Ps) / 230
    spare = 13 - I_used
    P_more = spare * 230
    return mk(rng, P_more, [(spare, "That is the spare CURRENT; convert to power: P = V I."), (13 * 230, "Subtract the power already in use."), (sum(Ps), "That is the power already in use.")],
              "W", f"Two appliances are plugged into a 13 A multi-socket adaptor on the 230 V mains.\n\n{md_table(['appliance', 'power / W'], [[i + 1, p] for i, p in enumerate(Ps)])}\n\nWhat is the largest extra power that can be added without exceeding 13 A?",
              "max power = 13 × 230; spare = max − in use", [f"max = 13 × 230 = 2990 W; in use = {sum(Ps)} W", f"spare = **{fmt(2990 - sum(Ps), sf=3)} W**"],
              ["Find the maximum power the adaptor allows.", "P = V I.", "Subtract the power already used."], sf=3)


# ================================================================== L4
@template("c16x_compare_bulbs_cost", chapter=16, level=4, lo="16c")
def compare_bulbs_cost(rng):
    P1, P2 = 60, nice(rng, 8, 10, 12)
    h = nice(rng, 1000, 2000)
    price = nice(rng, 25, 30)
    save = (P1 - P2) / 1000 * h * price / 100
    return mk(rng, save, [((P1 - P2) / 1000 * h * price, "That is in cents; give dollars."), (P1 / 1000 * h * price / 100, "Use the DIFFERENCE in power."), ((P1 - P2) * h * price / 100, "Convert W to kW.")],
              "dollars", f"A 60 W filament lamp is replaced by an LED lamp that gives the same light.\n\n{md_table(['quantity', 'value'], [['power of LED', f'{P2} W'], ['hours used', h], ['cost of 1 kWh', f'{price} cents']])}\n\nHow much money is saved, in dollars?",
              "saving = (P₁ − P₂)(kW) × t(h) × price", [f"ΔP = {P1 - P2} W = {fmt((P1 - P2) / 1000)} kW", f"ΔE = {fmt((P1 - P2) / 1000)} × {h} = {fmt((P1 - P2) / 1000 * h)} kWh", f"saving = **${fmt(save)}**"],
              ["Find the power saved.", "Find the kWh saved.", "Multiply by the price, in dollars."])


@template("c16x_kwh_to_joules", chapter=16, level=4, lo="16c")
def kwh_to_joules(rng):
    k = nice(rng, 1, 2, 5, 10)
    return mk(rng, k * 3.6, [(k * 3600, "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J = 3.6 MJ."), (k * 1000, "Multiply by 3600 s too."), (k * 0.36, "1 kWh = 3.6 MJ.")],
              "MJ", f"{md_table(['quantity', 'value'], [['energy used', f'{k} kWh']])}\n\nWhat is this energy in megajoules (MJ)?",
              "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J", [f"{k} × 3.6 = **{fmt(k * 3.6)} MJ**"],
              ["1 kWh = 1 kW for 1 hour.", "= 1000 J/s × 3600 s.", "= 3.6 MJ."])


@template("c16x_energy_vit_minutes", chapter=16, level=4, lo="16b")
def energy_vit_minutes(rng):
    V = 230
    I = nice(rng, 2.0, 4.0, 5.0)
    t_min = nice(rng, 2, 5, 10)
    E = V * I * t_min * 60
    return mk(rng, E / 1000, [(V * I * t_min / 1000, "Convert minutes to seconds."), (E, "That is in J; give kJ."), (V * I / 1000, "Multiply by the time.")],
              "kJ", f"{md_table(['quantity', 'value'], [['p.d.', '230 V'], ['current', f'{fmt(I)} A'], ['time', f'{t_min} min']])}\n\nHow much energy does the appliance use, in kJ?",
              "E = V I t", [f"E = 230 × {fmt(I)} × {t_min * 60} = {fmt(E)} J", f"= **{fmt(E / 1000)} kJ**"],
              ["E = V I t.", "Time in seconds.", "Convert to kJ."])


@template("c16x_power_i2r", chapter=16, level=4, lo="16b")
def power_i2r(rng):
    I = nice(rng, 2, 3, 4, 5)
    R = nice(rng, 10, 20, 46)
    return mk(rng, I * I * R, [(I * R, "That is the p.d.; P = I² R."), (I * I / R, "Multiply by R."), (I * R * R, "Square the current.")],
              "W", f"{md_table(['quantity', 'value'], [['current in heating element', f'{I} A'], ['resistance of element', f'{R} Ω']])}\n\nWhat is the power of the element?",
              "P = I² R", [f"P = {I}² × {R} = **{fmt(I * I * R)} W**"],
              ["Use P = I² R.", "Square the current.", "Multiply."])


@template("c16x_fault_current_earth", chapter=16, level=4, lo="16f")
def fault_current_earth(rng):
    R = nice(rng, 0.5, 1.0, 2.0)
    I = 230 / R
    return mk(rng, I, [(R / 230, "I = V ÷ R."), (230 * R, "Divide by R."), (I / 1000, "The answer is in A.")],
              "A", f"A live wire touches the earthed metal case of a washing machine. The earth path has a very low resistance.\n\n{md_table(['quantity', 'value'], [['mains p.d.', '230 V'], ['resistance of earth path', f'{fmt(R)} Ω']])}\n\nWhat current flows to earth? (This large current blows the fuse.)",
              "I = V ÷ R", [f"I = 230 ÷ {fmt(R)} = **{fmt(I)} A**"],
              ["The earth path has low resistance.", "I = V ÷ R.", "It is far larger than the fuse rating."])


@template("c16x_fault_fuse_blows", chapter=16, level=4, lo="16f")
def fault_fuse_blows(rng):
    R = nice(rng, 1.0, 2.0, 4.0)
    fuse = nice(rng, 5, 13)
    I = 230 / R
    ratio = I / fuse
    return mk(rng, ratio, [(fuse / I, "The fault current is MUCH larger than the fuse rating."), (I, "That is the fault current; compare with the fuse."), (I - fuse, "Find the ratio.")],
              "times", f"In a fault, the live wire touches an earthed metal case.\n\n{md_table(['quantity', 'value'], [['mains p.d.', '230 V'], ['earth path resistance', f'{fmt(R)} Ω'], ['fuse rating', f'{fuse} A']])}\n\nHow many times larger than the fuse rating is the fault current?",
              "I = V ÷ R; ratio = I ÷ fuse", [f"I = 230 ÷ {fmt(R)} = {fmt(I)} A", f"ratio = {fmt(I)} ÷ {fuse} = **{fmt(ratio)}**"],
              ["Find the fault current.", "Compare with the fuse rating.", "So the fuse blows quickly."])


@template("c16x_fuse_after_upgrade", chapter=16, level=4, lo="16e")
def fuse_after_upgrade(rng):
    P_old, P_new = nice(rng, 500, 600), nice(rng, 1500, 2000, 2500)
    I_new = P_new / 230
    ans = f"{fuse_for(I_new)} A"
    wrongs = {f"{f} A": ("Too small for the new current." if f < I_new else "Bigger than necessary.") for f in FUSES if f"{f} A" != ans}
    wrongs["keep the old fuse"] = f"The old fuse (for {P_old} W) would blow."
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"A {P_old} W appliance with a 3 A fuse is replaced by a new model (rating plate in Fig. 1) using the same plug. Which fuse should now be used?",
               "I = P ÷ V for the new appliance; next fuse above", [f"I = {P_new} ÷ 230 = {fmt(I_new, sf=3)} A → **{ans}**"],
               ["Find the new current.", "Does the old fuse still suit?", "Choose the next rating above."], figure=figs3.rating_plate(["NEW MODEL", "230 V ~ 50 Hz", f"{P_new} W"]))


@template("c16x_breaker_vs_fuse_time", chapter=16, level=4, lo="16e")
def breaker_vs_fuse_time(rng):
    t_fuse = nice(rng, 0.1, 0.2, 0.5)
    t_rccb = nice(rng, 0.02, 0.03, 0.04)
    return mk(rng, t_fuse / t_rccb, [(t_rccb / t_fuse, "The RCCB is FASTER, so the ratio fuse ÷ RCCB is greater than 1."), (t_fuse - t_rccb, "Find the ratio."), (t_fuse, "Divide by the RCCB time.")],
              "times", f"Protective devices take time to cut off a fault current.\n\n{md_table(['device', 'time to cut off / s'], [['fuse', fmt(t_fuse)], ['residual current circuit breaker (RCCB)', fmt(t_rccb)]])}\n\nHow many times faster is the RCCB?",
              "ratio = t_fuse ÷ t_RCCB", [f"= {fmt(t_fuse)} ÷ {fmt(t_rccb)} = **{fmt(t_fuse / t_rccb)}**"],
              ["Which is faster?", "Divide the times.", "Fuse ÷ RCCB."])


@template("c16x_cable_heating_increase", chapter=16, level=4, lo="16d")
def cable_heating_increase(rng):
    R = nice(rng, 0.2, 0.3, 0.4)
    I1, I2 = nice(rng, 5, 6), nice(rng, 12, 15)
    dP = (I2 ** 2 - I1 ** 2) * R
    return mk(rng, dP, [(I2 ** 2 * R, "Find the INCREASE in heating power."), ((I2 - I1) ** 2 * R, "Find each P = I² R and subtract."), ((I2 - I1) * R, "Square the currents.")],
              "W", f"An extension cable of resistance **{fmt(R)} Ω** is overloaded.\n\n{md_table(['situation', 'current / A'], [['normal', I1], ['overloaded', I2]])}\n\nBy how much does the rate of heating in the cable increase?",
              "P = I² R in each case; subtract", [f"normal: {I1}² × {fmt(R)} = {fmt(I1 ** 2 * R)} W; overloaded: {I2}² × {fmt(R)} = {fmt(I2 ** 2 * R)} W", f"increase = **{fmt(dP)} W**"],
              ["P = I² R.", "Work out both.", "Subtract."])


@template("c16x_damaged_insulation_current", chapter=16, level=4, lo="16d")
def damaged_insulation_current(rng):
    R_body = nice(rng, 2000, 5000, 10000)
    R_wet = R_body / nice(rng, 5, 10)
    I_dry = 230 / R_body * 1000
    I_wet = 230 / R_wet * 1000
    return mk(rng, I_wet, [(I_dry, "That is with DRY skin; wet skin has much lower resistance."), (230 / R_wet, "Convert A to mA."), (I_wet / 10, "Use the wet-skin resistance.")],
              "mA", f"Touching a bare live wire passes current through the body to earth.\n\n{md_table(['condition', 'body resistance / Ω'], [['dry skin', R_body], ['wet skin', fmt(R_wet)]])}\n\nWhat current would flow with wet skin? (Currents above about 50 mA can be fatal.)",
              "I = V ÷ R", [f"I = 230 ÷ {fmt(R_wet)} = {fmt(I_wet / 1000, sf=3)} A = **{fmt(I_wet)} mA**"],
              ["Use the wet-skin resistance.", "I = V ÷ R.", "Convert to mA."])


# ================================================================== L5
@template("c16x_bill_several", chapter=16, level=5, lo="16c")
def bill_several(rng):
    rows = [("air conditioner", nice(rng, 1.5, 2.0), nice(rng, 6, 8)), ("fridge", 0.2, 24), ("lights", nice(rng, 0.3, 0.4), 5)]
    price = nice(rng, 28, 30)
    E = sum(p * h for _, p, h in rows)
    cost = E * 30 * price / 100
    return mk(rng, cost, [(E * price / 100, "Multiply by 30 days."), (E * 30 * price, "Convert cents to dollars."), (rows[0][1] * rows[0][2] * 30 * price / 100, "Include every appliance.")],
              "dollars", f"A family's daily use:\n\n{md_table(['appliance', 'power / kW', 'hours per day'], [[n, fmt(p), h] for n, p, h in rows])}\n\nAt **{price} cents per kWh**, what is the bill for 30 days, in dollars?",
              "daily kWh = Σ P t; monthly = × 30; cost = × price", [f"daily = {' + '.join(fmt(p * h) for _, p, h in rows)} = {fmt(E)} kWh", f"30 days: {fmt(E * 30)} kWh × {price} cents = **${fmt(cost)}**"],
              ["Find each appliance's daily kWh.", "Add, then × 30.", "Multiply by the price; convert to dollars."])


@template("c16x_standby_waste", chapter=16, level=5, lo="16c")
def standby_waste(rng):
    P = nice(rng, 2, 5, 8)
    n = nice(rng, 4, 6, 10)
    h = 24 * 365
    price = nice(rng, 30)
    E = P * n / 1000 * h
    return mk(rng, E * price / 100, [(E * price, "Convert cents to dollars."), (P * n * h * price / 100, "Convert W to kW."), (P / 1000 * h * price / 100, "Multiply by the number of devices.")],
              "dollars", f"Devices left on standby all year waste energy.\n\n{md_table(['quantity', 'value'], [['standby power of each device', f'{P} W'], ['number of devices', n], ['hours in a year', h], ['price', f'{price} cents per kWh']])}\n\nHow much does this cost in a year, in dollars?",
              "E = n P(kW) t(h); cost = E × price", [f"E = {n} × {fmt(P / 1000)} × {h} = {fmt(E)} kWh", f"cost = **${fmt(E * price / 100)}**"],
              ["Total standby power.", "kWh for the year.", "Cost in dollars."])


@template("c16x_heater_two_settings", chapter=16, level=5, lo="16b")
def heater_two_settings(rng):
    R = nice(rng, 46, 53)
    P_one = 230 ** 2 / R
    P_par = 2 * P_one
    return mk(rng, P_par, [(P_one, "In parallel, each element has the full 230 V, so the powers add."), (P_one / 2, "Parallel elements give MORE power, not less."), (P_one * 4, "The two elements' powers add.")],
              "W", f"A heater has two identical elements, each of resistance **{R} Ω**. On its high setting both are connected in parallel across 230 V.\n\n{md_table(['quantity', 'value'], [['p.d.', '230 V'], ['resistance of each element', f'{R} Ω']])}\n\nWhat is the total power on the high setting?",
              "each: P = V² ÷ R; parallel: add", [f"each = 230² ÷ {R} = {fmt(P_one, sf=3)} W", f"total = **{fmt(P_par, sf=3)} W**"],
              ["Each element has the full p.d.", "P = V² ÷ R for each.", "Add."], sf=3)


@template("c16x_heater_series_low", chapter=16, level=5, lo="16b")
def heater_series_low(rng):
    R = nice(rng, 46, 53)
    P = 230 ** 2 / (2 * R)
    return mk(rng, P, [(230 ** 2 / R, "In series the total resistance doubles, halving the power."), (230 ** 2 / R * 2, "Series → less power."), (230 ** 2 / (4 * R), "Total R = 2R, so P = V² ÷ 2R.")],
              "W", f"The same heater (two **{R} Ω** elements) has a low setting with the elements in **series** across 230 V (Fig. 1). What is the power on the low setting?",
              "series: R_total = 2R; P = V² ÷ R_total", [f"R = 2 × {R} = {2 * R} Ω", f"P = 230² ÷ {2 * R} = **{fmt(P, sf=3)} W**"],
              ["Find the total resistance.", "Series: add.", "P = V² ÷ R."], figure=figs3.circuit(emf="230 V", top=[("R", f"{R} Ω"), ("R", f"{R} Ω")]), sf=3)


@template("c16x_fuse_multiple_appliances", chapter=16, level=5, lo="16e")
def fuse_multiple_appliances(rng):
    Ps = [nice(rng, 1000, 1200), nice(rng, 700, 900), nice(rng, 300, 500)]
    I = sum(Ps) / 230
    ans = "yes" if I > 13 else "no"
    wrongs = {("no" if ans == "yes" else "yes"): f"Total current = {sum(Ps)} ÷ 230 = {fmt(I, sf=3)} A; compare with 13 A.",
              "only the largest appliance matters": "All the currents add.", "it depends on the length of the lead": "The fuse blows on total current."}
    table = md_table(["appliance", "power / W"], [[i + 1, p] for i, p in enumerate(Ps)])
    return mkt(rng, ans, wrongs, f"Three 230 V appliances are plugged into an extension lead whose plug has a **13 A** fuse.\n\n{table}\n\nWill the fuse blow when all three are used together?",
               "I_total = ΣP ÷ V; blows if > 13 A", [f"I = {sum(Ps)} ÷ 230 = {fmt(I, sf=3)} A → **{ans}**"],
               ["Add the powers.", "I = P ÷ V.", "Compare with 13 A."])


@template("c16x_fuse_margin", chapter=16, level=5, lo="16e")
def fuse_margin(rng):
    P = nice(rng, 2500, 2800, 2990)
    I = P / 230
    return mk(rng, 13 - I, [(I, "That is the current; find how far below 13 A it is."), (13 + I, "Subtract."), (I - 3, "Compare with the 13 A fuse.")],
              "A", f"A **{P} W, 230 V** kettle is fitted with a 13 A fuse.\n\n{md_table(['quantity', 'value'], [['power', f'{P} W'], ['fuse rating', '13 A']])}\n\nBy how many amperes is the normal current below the fuse rating?",
              "I = P ÷ V; margin = 13 − I", [f"I = {P} ÷ 230 = {fmt(I, sf=3)} A", f"margin = 13 − {fmt(I, sf=3)} = **{fmt(13 - I, sf=3)} A**"],
              ["Find the current.", "Compare with 13 A.", "Subtract."], sf=3)


@template("c16x_earth_vs_body", chapter=16, level=5, lo="16f")
def earth_vs_body(rng):
    R_earth = nice(rng, 0.5, 1.0)
    R_body = nice(rng, 1000, 2000, 5000)
    ratio = R_body / R_earth
    return mk(rng, ratio, [(R_earth / R_body, "Current divides inversely to resistance: the EARTH path takes far more."), (R_body - R_earth, "Find the ratio."), (ratio / 1000, "Check the powers of ten.")],
              "times", f"A person touches a faulty earthed metal case. The earth wire and the person form two parallel paths to earth.\n\n{md_table(['path', 'resistance / Ω'], [['earth wire', fmt(R_earth)], ['person', R_body]])}\n\nHow many times more current flows through the earth wire than through the person?",
              "parallel paths: I ∝ 1/R → ratio = R_person ÷ R_earth", [f"= {R_body} ÷ {fmt(R_earth)} = **{fmt(ratio)}**"],
              ["The paths are in parallel.", "Same p.d. across each.", "I ∝ 1/R."])


@template("c16x_earth_fuse_time", chapter=16, level=5, lo="16f")
def earth_fuse_time(rng):
    R = nice(rng, 0.5, 1.0)
    I = 230 / R
    E_rate = I * I * R
    return mk(rng, E_rate / 1000, [(E_rate, "That is in W; give kW."), (I * R / 1000, "P = I² R."), (230 * 230 / 1000, "Use the earth path resistance.")],
              "kW", f"In a fault, the live wire touches the earthed case.\n\n{md_table(['quantity', 'value'], [['mains p.d.', '230 V'], ['earth path resistance', f'{fmt(R)} Ω']])}\n\nAt what rate is energy converted in the earth path, in kW? (This is why the fuse must blow quickly.)",
              "I = V ÷ R; P = I² R (= V² ÷ R)", [f"I = 230 ÷ {fmt(R)} = {fmt(I)} A", f"P = {fmt(I)}² × {fmt(R)} = {fmt(E_rate)} W = **{fmt(E_rate / 1000)} kW**"],
              ["Find the fault current.", "P = I² R.", "Convert to kW."])


@template("c16x_cable_voltage_drop", chapter=16, level=5, lo="16d")
def cable_voltage_drop(rng):
    I = nice(rng, 8, 10, 13)
    R = nice(rng, 0.2, 0.3, 0.5)
    drop = I * R
    return mk(rng, 230 - drop, [(drop, "That is the p.d. lost in the cable; subtract it from 230 V."), (230 + drop, "The cable REDUCES the p.d. at the appliance."), (230, "Some p.d. is lost in the cable.")],
              "V", f"A long extension cable has a total resistance of **{fmt(R)} Ω** and carries **{I} A**.\n\n{md_table(['quantity', 'value'], [['mains p.d.', '230 V'], ['current', f'{I} A'], ['cable resistance', f'{fmt(R)} Ω']])}\n\nWhat p.d. reaches the appliance?",
              "p.d. lost in cable = I R; at appliance = 230 − I R", [f"lost = {I} × {fmt(R)} = {fmt(drop)} V", f"at appliance = 230 − {fmt(drop)} = **{fmt(230 - drop)} V**"],
              ["Find the p.d. across the cable.", "V = I R.", "Subtract from 230 V."])


@template("c16x_cable_length_limit", chapter=16, level=5, lo="16d")
def cable_length_limit(rng):
    r_per_m = nice(rng, 0.02, 0.025, 0.04)
    I = nice(rng, 10, 13)
    P_max = nice(rng, 20, 30, 40)
    L = P_max / (I * I * r_per_m)
    return mk(rng, L, [(P_max / (I * r_per_m), "P = I² R: square the current."), (P_max * I * I * r_per_m, "L = P ÷ (I² × r per metre)."), (L * 2, "Use R = r × L.")],
              "m", f"To avoid overheating, a cable carrying **{I} A** must not waste more than **{P_max} W** as heat.\n\n{md_table(['quantity', 'value'], [['resistance per metre of cable', f'{fmt(r_per_m)} Ω'], ['current', f'{I} A'], ['maximum heating', f'{P_max} W']])}\n\nWhat is the greatest length of cable that can be used?",
              "P = I² R, R = r L → L = P ÷ (I² r)", [f"R_max = {P_max} ÷ {I}² = {fmt(P_max / I ** 2, sf=3)} Ω", f"L = {fmt(P_max / I ** 2, sf=3)} ÷ {fmt(r_per_m)} = **{fmt(L, sf=3)} m**"],
              ["Find the maximum resistance allowed.", "R = P ÷ I².", "Divide by resistance per metre."], sf=3)
