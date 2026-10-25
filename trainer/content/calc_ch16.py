"""Chapter 16 Practical Electricity (6091): P = V I, E = V I t, the kilowatt-hour and cost, fuse ratings, meter readings,
comparing appliances, resistance of a heating element."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template, text_options

MAINS = 230


# ---------------------------------------------------------------- L1
@template("c16_power_from_v_i", chapter=16, level=1, lo="16b")
def power_from_v_i(rng):
    I = nice(rng, 0.5, 2.0, 4.0, 5.0, 8.0, 10.0)
    P = MAINS * I
    opts, key, mis = numeric_options(rng, P, [
        (MAINS / I, "You divided. Power = p.d. × current."),
        (I / MAINS, "You divided the wrong way. P = V I."),
        (MAINS + I, "Multiply V and I; do not add."),
    ], unit="W", sf=3)
    return dict(
        stem=f"Fig. 1 shows the rating plate of an appliance. It works from the **{MAINS} V** mains and takes a current of **{fmt(I)} A**. What is its power?",
        figure=figs3.rating_plate([f"{MAINS} V ~ 50 Hz", f"{fmt(I)} A"]),
        options=opts, key=key, misconceptions=mis,
        formula="P = V I",
        working=["P = V I", f"= {MAINS} × {fmt(I)}", f"= **{fmt(P, sf=3)} W**"],
        hints=[
            "Which formula links power, p.d. and current?",
            "P = V × I, with V in volts and I in amperes.",
            f"{MAINS} × {fmt(I)} = ?",
        ],
    )


@template("c16_cost_single_appliance", chapter=16, level=1, lo="16c")
def cost_single_appliance(rng):
    P_kw = nice(rng, 1.0, 1.5, 2.0, 2.5, 3.0)
    h = nice(rng, 2, 3, 4, 5, 6)
    tariff = nice(rng, 25, 28, 30, 32)
    E = P_kw * h
    cost = E * tariff
    opts, key, mis = numeric_options(rng, cost, [
        (P_kw * tariff, "You forgot to multiply by the time. Energy in kWh = power in kW × time in hours."),
        (E, "That is the energy in kWh. Multiply by the price of one kWh to get the cost."),
        (P_kw * 1000 * h * tariff, "You used the power in watts. The kilowatt-hour uses power in KILOwatts."),
    ], unit="cents", sf=3)
    table = md_table(["quantity", "value"], [["power of heater", f"{fmt(P_kw)} kW"], ["time switched on", f"{h} h"], ["cost of 1 kWh", f"{tariff} cents"]])
    return dict(
        stem=f"An electric heater is used as shown in the table.\n\n{table}\n\nWhat is the cost of running the heater for this time?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h); cost = energy × price per kWh",
        working=[f"energy = {fmt(P_kw)} kW × {h} h = {fmt(E)} kWh", f"cost = {fmt(E)} × {tariff} cents", f"= **{fmt(cost, sf=3)} cents**"],
        hints=[
            "A kilowatt-hour is the energy used by a 1 kW appliance in 1 hour.",
            f"energy = {fmt(P_kw)} × {h} kWh.",
            f"cost = {fmt(E)} kWh × {tariff} cents per kWh.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c16_current_from_power", chapter=16, level=2, lo="16b")
def current_from_power(rng):
    P = nice(rng, 460, 920, 1150, 1840, 2300, 2760)
    I = P / MAINS
    opts, key, mis = numeric_options(rng, I, [
        (P * MAINS, "You multiplied. Rearrange P = V I to give I = P ÷ V."),
        (MAINS / P, "You divided the wrong way: I = P ÷ V."),
        (P / 110, "The mains p.d. here is 230 V."),
    ], unit="A", sf=3)
    return dict(
        stem=f"Fig. 1 shows the rating plate of a kettle: **{P} W** on the **{MAINS} V** mains. What current does it take?",
        figure=figs3.rating_plate([f"{MAINS} V ~ 50 Hz", f"{P} W"]),
        options=opts, key=key, misconceptions=mis,
        formula="P = V I  →  I = P ÷ V",
        working=["I = P ÷ V", f"= {P} ÷ {MAINS}", f"= **{fmt(I, sf=3)} A**"],
        hints=[
            "Start from P = V I and make I the subject.",
            f"I = {P} ÷ {MAINS}.",
            "The answer is a few amperes, as expected for a kettle.",
        ],
    )


@template("c16_energy_vit", chapter=16, level=2, lo="16b")
def energy_vit(rng):
    V = nice(rng, 12, 230)
    I = nice(rng, 0.5, 2.0, 3.0, 5.0)
    t_min = nice(rng, 2, 5, 10, 15)
    E = V * I * t_min * 60
    opts, key, mis = numeric_options(rng, E, [
        (V * I * t_min, "You used the time in minutes. E = V I t needs the time in seconds."),
        (V * I, "That is the power in watts. Multiply by the time in seconds to get the energy."),
        (V * t_min * 60, "You left out the current."),
    ], unit="J", sf=3)
    table = md_table(["quantity", "value"], [["p.d.", f"{V} V"], ["current", f"{fmt(I)} A"], ["time", f"{t_min} min"]])
    return dict(
        stem=f"A motor runs as shown in the table.\n\n{table}\n\nHow much electrical energy is transferred to the motor?",
        options=opts, key=key, misconceptions=mis,
        formula="E = V I t  (t in seconds)",
        working=[f"t = {t_min} min = {t_min * 60} s", f"E = V I t = {V} × {fmt(I)} × {t_min * 60}", f"= **{fmt(E, sf=3)} J**"],
        hints=[
            "Energy = power × time, and power = V I.",
            "Change the minutes into seconds first.",
            f"E = {V} × {fmt(I)} × {t_min * 60}.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c16_choose_fuse", chapter=16, level=3, lo="16e")
def choose_fuse(rng):
    P = nice(rng, 400, 600, 800, 1000, 2000, 2500)
    I = P / MAINS
    fuses = [3, 5, 13]
    ans = next(f for f in fuses if f > I)
    wrongs = {}
    for f in fuses:
        if f == ans:
            continue
        if f < I:
            wrongs[f"{f} A"] = f"The appliance takes {fmt(I, sf=2)} A, so a {f} A fuse would melt as soon as it was switched on."
        else:
            wrongs[f"{f} A"] = f"A {f} A fuse is far above the normal current of {fmt(I, sf=2)} A; it would let a dangerously large current flow before melting."
    wrongs["1 A"] = f"The appliance needs {fmt(I, sf=2)} A, so a 1 A fuse would blow immediately."
    opts, key, mis = text_options(rng, f"{ans} A", dict(list(wrongs.items())[:3]))
    return dict(
        stem=f"Fig. 1 shows the rating plate of an appliance: **{P} W, {MAINS} V**. Fuses of 3 A, 5 A and 13 A are available. Which fuse should be fitted in its plug?",
        figure=figs3.rating_plate([f"{MAINS} V ~ 50 Hz", f"{P} W"]),
        options=opts, key=key, misconceptions=mis,
        formula="I = P ÷ V; choose the fuse rating just ABOVE the normal operating current",
        working=[f"I = P ÷ V = {P} ÷ {MAINS} = {fmt(I, sf=2)} A", f"the smallest available fuse above {fmt(I, sf=2)} A is **{ans} A**"],
        hints=[
            "First work out the normal current: I = P ÷ V.",
            f"The current is {fmt(I, sf=2)} A. A fuse must not blow in normal use, but should blow soon after a fault raises the current.",
            "Pick the smallest rating that is still above the normal current.",
        ],
    )


@template("c16_cost_several_appliances", chapter=16, level=3, lo="16c")
def cost_several_appliances(rng):
    items = [("kettle", 2.0, nice(rng, 0.25, 0.5)), ("television", nice(rng, 0.1, 0.2), nice(rng, 3, 4, 5)), ("heater", nice(rng, 1.0, 1.5), nice(rng, 2, 3))]
    tariff = nice(rng, 25, 30)
    E = sum(p * h for _, p, h in items)
    cost = E * tariff
    opts, key, mis = numeric_options(rng, cost, [
        (E, "That is the total energy in kWh. Multiply by the price per kWh."),
        (sum(p for _, p, _ in items) * sum(h for _, _, h in items) * tariff, "You multiplied the total power by the total time. Work out each appliance's energy separately, then add."),
        (cost / 100, "Check the units: the answer is in cents, matching the tariff."),
    ], unit="cents", sf=3)
    table = md_table(["appliance", "power / kW", "time used / h"], [[n, fmt(p), fmt(h)] for n, p, h in items])
    return dict(
        stem=f"The table shows the appliances used in a home one evening. Electricity costs **{tariff} cents per kWh**.\n\n{table}\n\nWhat is the total cost?",
        options=opts, key=key, misconceptions=mis,
        formula="for each appliance energy = power (kW) × time (h); add the energies; cost = total kWh × price",
        working=[" + ".join(f"{fmt(p)} × {fmt(h)}" for _, p, h in items) + f" = {fmt(E, sf=3)} kWh", f"cost = {fmt(E, sf=3)} × {tariff}", f"= **{fmt(cost, sf=3)} cents**"],
        hints=[
            "Work out the kilowatt-hours for each appliance separately.",
            f"Energies: " + ", ".join(f"{n} {fmt(p * h)} kWh" for n, p, h in items) + ".",
            f"Add them and multiply by {tariff} cents.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c16_meter_readings", chapter=16, level=4, lo="16c")
def meter_readings(rng):
    start = rng.randint(10000, 60000)
    used = nice(rng, 180, 240, 300, 360, 420)
    tariff = nice(rng, 25, 28, 30)
    cost_dollars = used * tariff / 100
    opts, key, mis = numeric_options(rng, cost_dollars, [
        (used, "That is the energy used in kWh, not the cost."),
        (used * tariff, "That is the cost in CENTS. The options are in dollars."),
        ((start + used) * tariff / 100, "You used the final meter reading instead of the DIFFERENCE between the readings."),
    ], unit="$", sf=4)
    table = md_table(["", "meter reading / kWh"], [["1 March", start], ["1 April", start + used]])
    return dict(
        stem=f"The table shows the readings on a household electricity meter. Electricity costs **{tariff} cents per kWh**.\n\n{table}\n\nWhat is the cost of the electricity used in March, in dollars?",
        options=opts, key=key, misconceptions=mis,
        formula="energy used = difference between the readings (kWh); cost = energy × price, then cents → dollars (÷ 100)",
        working=[f"energy = {start + used} − {start} = {used} kWh", f"cost = {used} × {tariff} = {used * tariff} cents", f"= **${fmt(cost_dollars, sf=4)}**"],
        hints=[
            "The meter counts kWh continuously. How much was used during March?",
            f"Subtract the readings: {used} kWh. Then multiply by the price.",
            "Convert cents to dollars at the end.",
        ],
    )


@template("c16_heater_energy_kj", chapter=16, level=4, lo="16b")
def heater_energy_kj(rng):
    P = nice(rng, 500, 750, 1200, 1500, 2000)
    t_min = nice(rng, 3, 5, 8, 10, 12)
    E_kj = P * t_min * 60 / 1000
    opts, key, mis = numeric_options(rng, E_kj, [
        (P * t_min / 1000, "You used the time in minutes. Convert to seconds first."),
        (P * t_min * 60, "That is the energy in joules. The options are in kilojoules."),
        (P * t_min * 60 / 1000 / 60, "Check the conversions: minutes → seconds (× 60), J → kJ (÷ 1000)."),
    ], unit="kJ", sf=3)
    table = md_table(["quantity", "value"], [["power of heater", f"{P} W"], ["time", f"{t_min} min"]])
    return dict(
        stem=f"An electric heater is switched on for a few minutes.\n\n{table}\n\nHow much energy does it transfer, in kJ?",
        options=opts, key=key, misconceptions=mis,
        formula="E = P t (t in seconds), then J → kJ",
        working=[f"t = {t_min} × 60 = {t_min * 60} s", f"E = {P} × {t_min * 60} = {fmt(P * t_min * 60)} J", f"= **{fmt(E_kj, sf=3)} kJ**"],
        hints=[
            "Power is energy per second. How many seconds is the heater on for?",
            f"E = {P} × {t_min * 60} J.",
            "Divide by 1000 to change joules into kilojoules.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c16_led_vs_filament_saving", chapter=16, level=5, lo="16c")
def led_vs_filament_saving(rng):
    P_old = nice(rng, 60, 75, 100)
    P_new = nice(rng, 8, 10, 12)
    h_day = nice(rng, 4, 5, 6)
    tariff = nice(rng, 25, 30)
    days = 365
    saving_kwh = (P_old - P_new) / 1000 * h_day * days
    saving = saving_kwh * tariff / 100
    opts, key, mis = numeric_options(rng, saving, [
        (saving_kwh, "That is the energy saved in kWh. Multiply by the price per kWh and convert to dollars."),
        ((P_old - P_new) * h_day * days * tariff / 100, "You used the power in watts. Convert to kilowatts (÷ 1000) for kWh."),
        (P_old / 1000 * h_day * days * tariff / 100, "That is the full cost of the OLD lamp, not the saving. Use the difference in power."),
    ], unit="$", sf=3)
    table = md_table(["lamp", "power / W"], [["filament lamp", P_old], ["LED lamp", P_new]])
    return dict(
        stem=f"A filament lamp is replaced by an LED lamp giving the same light. The lamp is used for **{h_day} hours a day** for a year (365 days). Electricity costs **{tariff} cents per kWh**.\n\n{table}\n\nHow much money is saved in the year?",
        options=opts, key=key, misconceptions=mis,
        formula="energy saved (kWh) = (P_old − P_new in kW) × hours; cost saved = kWh × price",
        working=[f"power saved = {P_old} − {P_new} = {P_old - P_new} W = {fmt((P_old - P_new) / 1000)} kW", f"energy saved = {fmt((P_old - P_new) / 1000)} × {h_day} × 365 = {fmt(saving_kwh, sf=3)} kWh", f"cost saved = {fmt(saving_kwh, sf=3)} × {tariff} cents = **${fmt(saving, sf=3)}**"],
        hints=[
            "Only the DIFFERENCE in power is saved. Work it out in kilowatts.",
            f"Hours in the year = {h_day} × 365. Energy saved = kW × hours.",
            f"Multiply the kWh by {tariff} cents and convert to dollars.",
        ],
    )


@template("c16_element_resistance", chapter=16, level=5, lo="16b")
def element_resistance(rng):
    P = nice(rng, 1150, 1840, 2300, 2760)
    I = P / MAINS
    R = MAINS / I
    opts, key, mis = numeric_options(rng, R, [
        (MAINS / P, "You divided V by P. First find the current I = P ÷ V, then R = V ÷ I."),
        (P / MAINS, "That is the current in amperes. The question asks for the resistance."),
        (MAINS * I, "You multiplied V by I, which gives the power again. R = V ÷ I."),
    ], unit="Ω", sf=3)
    return dict(
        stem=f"Fig. 1 shows the rating plate of a kettle: **{P} W, {MAINS} V**. What is the resistance of its heating element when it is operating?",
        figure=figs3.rating_plate([f"{MAINS} V ~ 50 Hz", f"{P} W"]),
        options=opts, key=key, misconceptions=mis,
        formula="I = P ÷ V, then R = V ÷ I",
        working=[f"I = P ÷ V = {P} ÷ {MAINS} = {fmt(I, sf=3)} A", f"R = V ÷ I = {MAINS} ÷ {fmt(I, sf=3)}", f"= **{fmt(R, sf=3)} Ω**"],
        hints=[
            "Two steps: find the current from the power, then the resistance from the current.",
            f"I = {P} ÷ {MAINS} A.",
            f"R = {MAINS} ÷ I.",
        ],
    )
