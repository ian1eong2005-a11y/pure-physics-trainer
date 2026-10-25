"""Chapter 8 Thermal Processes (6091): data-reading 'calculation' templates: conduction comparisons, rates of cooling from
tables and graphs, radiation and surface area, thermal equilibrium, vacuum-flask energy budgets."""
from .. import figs2, sketches
from .base import fmt, md_table, nice, numeric_options, template, text_options


# ---------------------------------------------------------------- L1
@template("c8_best_conductor_table", chapter=8, level=1, lo="8b")
def best_conductor_table(rng):
    mats = [("copper", 25), ("aluminium", 40), ("iron", 95), ("glass", 400)]
    scale = rng.choice([1.0, 1.2, 0.8, 1.5])
    rows = [(m, round(t * scale)) for m, t in mats]
    rng.shuffle(rows)
    best = min(rows, key=lambda r: r[1])[0]
    wrongs = {m: f"The wax on the {m} rod took {t} s to melt: longer than on the best conductor, so energy travelled along it more slowly." for m, t in rows if m != best}
    opts, key, mis = text_options(rng, best, wrongs)
    table = md_table(["rod", "time for wax to melt / s"], [[m, t] for m, t in rows])
    return dict(
        stem=f"Fig. 1 shows four rods of equal size heated at one end. A pin is held by wax at the far end of each rod. The table shows how long the wax takes to melt.\n\n{table}\n\nWhich material is the best conductor of heat?",
        figure=sketches.rod_sketch([m for m, _ in rows]),
        options=opts, key=key, misconceptions=mis,
        formula="the best conductor transfers energy fastest, so its wax melts in the shortest time",
        working=["energy must travel the length of the rod before the wax melts", "the shortest time means the fastest conduction", f"best conductor = **{best}**"],
        hints=[
            "What has to happen along the rod before the wax at the far end melts?",
            "A good conductor passes energy along quickly, so the wax melts sooner.",
            "Pick the material with the SMALLEST time.",
        ],
    )


@template("c8_temperature_fall_table", chapter=8, level=1, lo="8d")
def temperature_fall_table(rng):
    start = nice(rng, 80, 85, 90)
    drop_black = nice(rng, 22, 25, 28, 30)
    drop_silver = drop_black - nice(rng, 6, 8, 10)
    which = rng.choice(["dull black", "shiny silver"])
    drop = drop_black if which == "dull black" else drop_silver
    other = drop_silver if which == "dull black" else drop_black
    opts, key, mis = numeric_options(rng, drop, [
        (other, f"That is the temperature fall of the OTHER can. Read the row for the {which} can."),
        (start - drop, f"That is the final temperature of the {which} can, not the fall in temperature."),
        (drop_black + drop_silver, "You added the two falls together. The question asks about one can only."),
    ], unit="°C")
    table = md_table(["can", "temperature at start / °C", "temperature after 10 min / °C"], [["dull black", start, start - drop_black], ["shiny silver", start, start - drop_silver]])
    return dict(
        stem=f"Two identical cans, one painted dull black and one shiny silver, are filled with hot water and left to cool. Fig. 1 shows the cans and the table shows the readings.\n\n{table}\n\nBy how much did the temperature of the **{which}** can fall in 10 minutes?",
        figure=sketches.two_cups_sketch(),
        options=opts, key=key, misconceptions=mis,
        formula="temperature fall = starting temperature − final temperature (a dull black surface emits radiation faster, so it cools more)",
        working=[f"{which} can: {start} °C → {start - drop} °C", f"fall = {start} − {start - drop}", f"= **{drop} °C**"],
        hints=[
            "Find the row for the can the question asks about.",
            "Subtract the final temperature from the starting temperature.",
            f"{start} − {start - drop} = ?",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c8_rate_of_cooling", chapter=8, level=2, lo="8a")
def rate_of_cooling(rng):
    t0 = nice(rng, 70, 75, 80, 90)
    minutes = nice(rng, 4, 5, 8, 10)
    rate = nice(rng, 1.5, 2.0, 2.5, 3.0, 4.0)
    t1 = t0 - rate * minutes
    opts, key, mis = numeric_options(rng, rate, [
        (t0 - t1, "That is the total temperature fall. Divide by the time to get the rate (°C per minute)."),
        (minutes / (t0 - t1), "You divided the wrong way round: rate of cooling = temperature fall ÷ time."),
        (rate * 60, "That would be the rate in °C per HOUR. The options are per minute."),
    ], unit="°C/min", sf=2)
    table = md_table(["time / min", "temperature / °C"], [[0, t0], [minutes, fmt(t1)]])
    return dict(
        stem=f"A beaker of hot water cools in a room. The table shows two readings.\n\n{table}\n\nWhat is the average rate of cooling over this time?",
        options=opts, key=key, misconceptions=mis,
        formula="average rate of cooling = fall in temperature ÷ time taken",
        working=[f"fall in temperature = {t0} − {fmt(t1)} = {fmt(t0 - t1)} °C", f"rate = {fmt(t0 - t1)} ÷ {minutes}", f"= **{fmt(rate, sf=2)} °C/min**"],
        hints=[
            "A rate is a change per unit time. What changed, and over how long?",
            f"The temperature fell by {fmt(t0 - t1)} °C in {minutes} minutes.",
            f"rate = {fmt(t0 - t1)} ÷ {minutes}.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c8_equilibrium_temperature", chapter=8, level=3, lo="8a")
def equilibrium_temperature(rng):
    m1, m2 = rng.choice([(1, 1), (1, 2), (2, 1), (1, 3), (3, 1)])
    hot = nice(rng, 60, 70, 80, 90)
    cold = nice(rng, 10, 20, 30)
    final = (m1 * hot + m2 * cold) / (m1 + m2)
    opts, key, mis = numeric_options(rng, final, [
        ((hot + cold) / 2, "That is the simple average, which is right only when the two masses are equal. Here they are not." if m1 != m2 else "Check the arithmetic of (hot + cold) ÷ 2."),
        (hot - cold, "That is the temperature DIFFERENCE, not the final temperature."),
        ((m2 * hot + m1 * cold) / (m1 + m2) if m1 != m2 else final + 5, "You weighted the masses the wrong way round: the larger mass pulls the final temperature towards its own." if m1 != m2 else "The final temperature must lie between the two starting temperatures."),
    ], unit="°C", sf=3)
    table = md_table(["water", "mass / kg", "temperature / °C"], [["hot", m1, hot], ["cold", m2, cold]])
    return dict(
        stem=f"Hot and cold water are mixed in an insulated container and left until thermal equilibrium is reached.\n\n{table}\n\nNo energy is lost to the surroundings. What is the final temperature?",
        options=opts, key=key, misconceptions=mis,
        formula="energy lost by the hot water = energy gained by the cold water, so the final temperature is the mass-weighted average: (m₁θ₁ + m₂θ₂) ÷ (m₁ + m₂)",
        working=["energy flows from hot to cold until both are at the same temperature", f"final = ({m1} × {hot} + {m2} × {cold}) ÷ ({m1} + {m2})", f"= **{fmt(final, sf=3)} °C**"],
        hints=[
            "Energy is transferred from the hotter water to the colder water until they reach the SAME temperature. Each kilogram of water changes temperature by the same amount per joule.",
            f"With {m1} kg hot and {m2} kg cold, the final temperature is closer to the {'hot' if m1 > m2 else 'cold' if m2 > m1 else 'middle'} value.",
            f"({m1} × {hot} + {m2} × {cold}) ÷ {m1 + m2}.",
        ],
    )


@template("c8_radiation_area", chapter=8, level=3, lo="8d")
def radiation_area(rng):
    P1 = nice(rng, 6, 8, 10, 12, 15)
    A1 = nice(rng, 0.02, 0.04, 0.05)
    k = nice(rng, 2, 2.5, 3, 4)
    A2 = A1 * k
    P2 = P1 * k
    opts, key, mis = numeric_options(rng, P2, [
        (P1, "Rate of radiation depends on surface area as well as temperature. A larger area at the same temperature radiates more."),
        (P1 / k, "A larger area radiates MORE energy per second, not less."),
        (P1 * k * k, "The rate is proportional to the area, not to the area squared."),
    ], unit="W", sf=3)
    table = md_table(["heater", "surface area / m²", "temperature / °C", "rate of emission / W"], [["P", fmt(A1), 200, P1], ["Q", fmt(A2), 200, "?"]])
    return dict(
        stem=f"Two heaters have the same dull black surface and the same temperature but different surface areas.\n\n{table}\n\nAt what rate does heater Q emit radiation?",
        options=opts, key=key, misconceptions=mis,
        formula="at the same temperature and surface finish, rate of radiation ∝ surface area",
        working=[f"area ratio = {fmt(A2)} ÷ {fmt(A1)} = {fmt(k)}", f"rate for Q = {fmt(k)} × {P1}", f"= **{fmt(P2, sf=3)} W**"],
        hints=[
            "Which three things affect the rate at which a surface radiates? Here only one of them differs between P and Q.",
            f"Q has {fmt(k)} times the area of P at the same temperature and colour.",
            f"{fmt(k)} × {P1} W.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c8_cooling_gradient", chapter=8, level=4, lo="8d")
def cooling_gradient(rng):
    t0 = nice(rng, 80, 90)
    rb = nice(rng, 6, 8, 10)        # black: °C per min over the first 2 min
    rs = rb - nice(rng, 2, 3, 4)
    black = [(0, t0), (2, t0 - 2 * rb), (4, t0 - 2 * rb - 1.4 * rb), (6, t0 - 2 * rb - 1.4 * rb - rb), (8, t0 - 2 * rb - 1.4 * rb - rb - 0.7 * rb)]
    silver = [(0, t0), (2, t0 - 2 * rs), (4, t0 - 2 * rs - 1.4 * rs), (6, t0 - 2 * rs - 1.4 * rs - rs), (8, t0 - 2 * rs - 1.4 * rs - rs - 0.7 * rs)]
    opts, key, mis = numeric_options(rng, rb, [
        (rs, "That is the gradient of the SILVER can's curve. Read the black can's curve."),
        (2 * rb, "That is the total fall in the first 2 minutes. Divide by 2 minutes to get the rate."),
        ((t0 - black[-1][1]) / 8, "That is the average rate over the whole 8 minutes. The question asks for the first 2 minutes, when the can is hottest and cools fastest."),
    ], unit="°C/min", sf=2)
    return dict(
        stem="Fig. 1 shows cooling curves for two identical cans of hot water, one dull black and one shiny silver. What is the rate of cooling of the **black** can during the **first 2 minutes**?",
        figure=figs2.two_curves([("black", black), ("silver", silver)], 8, 100, 2, 20),
        options=opts, key=key, misconceptions=mis,
        formula="rate of cooling = gradient of the temperature-time curve = fall in temperature ÷ time",
        working=[f"black can: {t0} °C at 0 min, {fmt(black[1][1])} °C at 2 min", f"rate = ({t0} − {fmt(black[1][1])}) ÷ 2", f"= **{rb} °C/min**"],
        hints=[
            "The rate of cooling is the gradient of the curve. Which curve is the black can? (Dull black surfaces emit radiation faster.)",
            f"Read the black can's temperature at 0 min and at 2 min.",
            f"({t0} − {fmt(black[1][1])}) ÷ 2 min.",
        ],
    )


@template("c8_extra_energy_lost", chapter=8, level=4, lo="8d")
def extra_energy_lost(rng):
    pb = nice(rng, 8, 10, 12, 15)
    ps = pb - nice(rng, 3, 4, 5)
    minutes = nice(rng, 2, 3, 5)
    extra = (pb - ps) * minutes * 60
    opts, key, mis = numeric_options(rng, extra, [
        ((pb - ps) * minutes, "You used the time in minutes. Power is in watts (joules per SECOND), so convert the time to seconds."),
        (pb * minutes * 60, "That is the total energy radiated by the black can, not how much MORE than the silver can."),
        ((pb + ps) * minutes * 60, "You added the two powers. The question asks for the difference."),
    ], unit="J")
    table = md_table(["can", "surface", "rate of energy loss by radiation / W"], [["P", "dull black", pb], ["Q", "shiny silver", ps]])
    return dict(
        stem=f"Two identical cans of water are at the same temperature.\n\n{table}\n\nHow much more energy does can P radiate than can Q in **{minutes} minutes**, assuming the rates stay the same?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time (time in seconds); extra energy = (difference in power) × time",
        working=[f"difference in power = {pb} − {ps} = {pb - ps} W", f"time = {minutes} min = {minutes * 60} s", f"extra energy = {pb - ps} × {minutes * 60} = **{extra} J**"],
        hints=[
            "A watt is a joule per second. How many seconds are there in the given time?",
            f"The black can loses {pb - ps} J more every second than the silver can.",
            f"{pb - ps} × {minutes * 60}.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c8_flask_energy_budget", chapter=8, level=5, lo="8e")
def flask_energy_budget(rng):
    cond, conv, rad = nice(rng, 20, 30, 40), nice(rng, 60, 80, 100), nice(rng, 30, 40, 50)
    f_cond, f_rad = nice(rng, 4, 5), nice(rng, 2, 4, 5)
    new = [cond // f_cond if cond % f_cond == 0 else round(cond / f_cond), 0, round(rad / f_rad)]
    before = cond + conv + rad
    after = sum(new)
    pct = (before - after) / before * 100
    opts, key, mis = numeric_options(rng, pct, [
        (after / before * 100, "That is the percentage of the energy loss that REMAINS. The question asks for the percentage reduction."),
        ((before - after) / after * 100, "You divided by the new loss. A percentage reduction is measured against the ORIGINAL loss."),
        (before - after, "That is the reduction in joules per hour, not as a percentage."),
    ], unit="%", sf=2)
    table = md_table(["process", "loss per hour, plain container / J", "loss per hour, vacuum flask / J"], [["conduction", cond, new[0]], ["convection", conv, new[1]], ["radiation", rad, new[2]]])
    return dict(
        stem=f"The table estimates the energy lost per hour from hot water in a plain container and in a vacuum flask (Fig. 1).\n\n{table}\n\nBy what percentage does the vacuum flask reduce the total energy loss per hour?",
        figure=sketches.flask_sketch(),
        options=opts, key=key, misconceptions=mis,
        formula="percentage reduction = (original total − new total) ÷ original total × 100%",
        working=[f"plain total = {cond} + {conv} + {rad} = {before} J;  flask total = {new[0]} + 0 + {new[2]} = {after} J",
                 f"reduction = {before} − {after} = {before - after} J", f"percentage = {before - after} ÷ {before} × 100 = **{fmt(pct, sf=2)}%**"],
        hints=[
            "Add up each column to get the total loss per hour for each container. (The vacuum stops conduction and convection almost completely; silvering cuts radiation.)",
            f"Totals: {before} J and {after} J. The reduction is the difference.",
            f"({before} − {after}) ÷ {before} × 100.",
        ],
    )
