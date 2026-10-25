"""Chapter 8 Thermal Processes (6091) bank extension: calculation and data-reading templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2015-2024: three copper cans with different surfaces and lids, two cans near a
radiant heater, hot-water tank with an immersion heater, oven elements, emergency blanket, trapped air in insulation)."""
from .. import figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, template


def _rank_text(rows, key, reverse=True):
    return ", ".join(n for n, *_ in sorted(rows, key=key, reverse=reverse))


# ================================================================== L1
@template("c8x_equilibrium_direction", chapter=8, level=1, lo="8a")
def equilibrium_direction(rng):
    Ta = nice(rng, 15, 20, 25)
    Tb = nice(rng, 60, 70, 80, 90)
    first = rng.choice(["A", "B"])
    temps = {"A": Ta, "B": Tb} if first == "A" else {"A": Tb, "B": Ta}
    hot = max(temps, key=temps.get)
    cold = "A" if hot == "B" else "B"
    ans = f"from {hot} to {cold}"
    wrongs = {f"from {cold} to {hot}": "Energy flows from the HOTTER body to the colder one.", "no energy flows": "They are at different temperatures, so energy flows.",
              "both lose energy": "One gains what the other loses."}
    table = md_table(["block", "temperature / °C"], [["A", temps["A"]], ["B", temps["B"]]])
    return mkt(rng, ans, wrongs, f"Two metal blocks are placed in contact.\n\n{table}\n\nIn which direction is energy transferred by heating?",
               "energy flows from higher to lower temperature until both are equal", [f"{hot} is hotter → energy flows **{ans}**"],
               ["Which block is hotter?", "Heat flows from hot to cold.", "Until they reach the same temperature."])


@template("c8x_temperature_difference", chapter=8, level=1, lo="8a")
def temperature_difference(rng):
    T1 = nice(rng, 80, 85, 90, 95)
    T2 = nice(rng, 25, 28, 30)
    return mk(rng, T1 - T2, [(T1 + T2, "Subtract the temperatures."), (T1, "That is the tea's temperature."), ((T1 + T2) / 2, "Find the difference, not the average.")],
              "°C", f"A cup of tea is left in a room.\n\n{md_table(['', 'temperature / °C'], [['tea', T1], ['room', T2]])}\n\nWhat is the temperature difference between the tea and the room? (A larger difference gives a faster rate of cooling.)",
              "ΔT = T_tea − T_room", [f"ΔT = {T1} − {T2} = **{T1 - T2} °C**"],
              ["Subtract the lower temperature from the higher.", "That is the temperature difference.", "Calculate."], dp=0)


@template("c8x_wax_rods_first", chapter=8, level=1, lo="8b")
def wax_rods_first(rng):
    rows = [("copper", nice(rng, 40, 45, 50)), ("aluminium", nice(rng, 70, 80)), ("iron", nice(rng, 150, 180)), ("glass", nice(rng, 900, 1200))]
    rng.shuffle(rows)
    worst = max(rows, key=lambda r: r[1])[0]
    wrongs = {n: "Compare the times: the poorest conductor takes the LONGEST." for n, t in rows if n != worst}
    table = md_table(["rod", "time for wax at the far end to melt / s"], [[n, t] for n, t in rows])
    return mkt(rng, worst, wrongs, f"Rods of the same size are heated at one end (Fig. 1).\n\n{table}\n\nWhich rod is the poorest conductor of heat?",
               "poorest conductor → longest time", [f"longest time → **{worst}**"],
               ["How does a good conductor behave?", "The wax melts quickly.", "The poorest takes the longest."], figure=sketches.rod_sketch([n for n, _ in rows]))


@template("c8x_black_can_cooling", chapter=8, level=1, lo="8d")
def black_can_cooling(rng):
    T0 = nice(rng, 80, 85, 90)
    drops = {"dull black": nice(rng, 18, 20, 22), "shiny silver": nice(rng, 6, 8), "white": nice(rng, 10, 12), "dull grey": nice(rng, 14, 16)}
    names = list(drops)
    rng.shuffle(names)
    ans = "dull black"
    wrongs = {n: ("Shiny surfaces are the POOREST emitters." if n == "shiny silver" else "Compare the temperature drops: the best emitter cools most.") for n in names if n != ans}
    table = md_table(["can surface", "start / °C", "after 10 min / °C"], [[n, T0, T0 - drops[n]] for n in names])
    return mkt(rng, ans, wrongs, f"Four identical cans of hot water have different outer surfaces.\n\n{table}\n\nWhich surface is the best emitter of infrared radiation?",
               "best emitter → largest temperature drop", [f"largest drop: {drops['dull black']} °C → **{ans}**"],
               ["Which can cools fastest?", "Find the largest temperature drop.", "That surface emits best."])


@template("c8x_convection_direction", chapter=8, level=1, lo="8c")
def convection_direction(rng):
    wrongs = {"sinks, because it becomes denser": "Heated water expands and becomes LESS dense.", "stays still, because water is a poor conductor": "Convection moves the water.",
              "rises, because it becomes denser": "Less dense water rises."}
    return mkt(rng, "rises, because it expands and becomes less dense", wrongs,
               "Fig. 1 shows water heated at the bottom left of a beaker. What happens to the water at A, directly above the flame?",
               "heated fluid expands → less dense → rises; cooler denser fluid sinks", ["warm water at A expands, is less dense and **rises**"],
               ["What happens to water when heated?", "It expands.", "Less dense → rises."], figure=sketches.convection_sketch())


@template("c8x_density_hot_cold_air", chapter=8, level=1, lo="8c")
def density_hot_cold_air(rng):
    rows = [("cold air", 1.29), ("warm air", 1.16), ("hot air", 1.00)]
    k = rng.randrange(3)
    picks = [r for i, r in enumerate(rows)]
    rng.shuffle(picks)
    ans = min(picks, key=lambda r: r[1])[0]
    wrongs = {n: "Denser air sinks; the LEAST dense air rises to the top." for n, d in picks if n != ans}
    wrongs["all mix evenly"] = "Convection separates air by density."
    table = md_table(["air sample", "density / kg/m³"], [[n, d] for n, d in picks])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich sample rises to the top of a room by convection?",
               "less dense fluid rises", [f"lowest density → **{ans}** rises"],
               ["Compare the densities.", "Which is least dense?", "Less dense rises."])


@template("c8x_flask_loss_compare", chapter=8, level=1, lo="8e")
def flask_loss_compare(rng):
    T0 = nice(rng, 80, 90)
    d_flask = nice(rng, 3, 4, 5)
    d_mug = nice(rng, 25, 30, 35)
    return mk(rng, d_mug - d_flask, [(d_mug, "That is the mug's drop; find the difference."), (d_flask, "That is the flask's drop."), (d_mug + d_flask, "Subtract the drops.")],
              "°C", f"Hot coffee is poured into a vacuum flask (Fig. 1) and into an open mug.\n\n{md_table(['container', 'start / °C', 'after 1 hour / °C'], [['vacuum flask', T0, T0 - d_flask], ['open mug', T0, T0 - d_mug]])}\n\nHow many more degrees does the coffee in the mug cool than the coffee in the flask?",
              "difference in temperature drops", [f"mug: {d_mug} °C; flask: {d_flask} °C", f"difference = **{d_mug - d_flask} °C**"],
              ["Find each temperature drop.", "Subtract.", "The flask reduces all three transfers."], figure=sketches.flask_sketch(), dp=0)


@template("c8x_insulation_best", chapter=8, level=1, lo="8e")
def insulation_best(rng):
    rows = [("wool", nice(rng, 8, 9)), ("aluminium foil only", nice(rng, 22, 25)), ("bubble wrap", nice(rng, 10, 11)), ("no wrapping", nice(rng, 28, 30))]
    rng.shuffle(rows)
    ans = min(rows, key=lambda r: r[1])[0]
    wrongs = {n: "The best insulator gives the SMALLEST temperature drop." for n, d in rows if n != ans}
    table = md_table(["wrapping on beaker", "temperature drop in 20 min / °C"], [[n, d] for n, d in rows])
    return mkt(rng, ans, wrongs, f"Beakers of hot water are wrapped in different materials.\n\n{table}\n\nWhich wrapping is the best insulator?",
               "best insulator → smallest temperature drop", [f"smallest drop → **{ans}** (traps air, a poor conductor)"],
               ["What does a good insulator do?", "It keeps the water hot.", "Smallest drop."])


# ================================================================== L2
@template("c8x_mix_equal_masses", chapter=8, level=2, lo="8a")
def mix_equal_masses(rng):
    T1 = nice(rng, 10, 20, 24)
    T2 = nice(rng, 60, 70, 80)
    Tf = (T1 + T2) / 2
    return mk(rng, Tf, [(T2 - T1, "That is the difference; the final temperature lies between the two."), (T1 + T2, "Equal masses of water end at the AVERAGE temperature."), (T2, "The hot water cools as the cold water warms.")],
              "°C", f"Equal masses of water are mixed in an insulated container.\n\n{md_table(['sample', 'temperature / °C'], [['cold', T1], ['hot', T2]])}\n\nWhat is the temperature when thermal equilibrium is reached?",
              "equal masses of the same substance: T_f = (T₁ + T₂) ÷ 2", [f"T_f = ({T1} + {T2}) ÷ 2 = **{fmt(Tf)} °C**"],
              ["Energy lost by hot = energy gained by cold.", "Equal masses of the same liquid.", "The average."])


@template("c8x_wax_order_conductors", chapter=8, level=2, lo="8b")
def wax_order_conductors(rng):
    rows = [("P", nice(rng, 30, 35)), ("Q", nice(rng, 90, 100)), ("R", nice(rng, 55, 60)), ("S", nice(rng, 400, 500))]
    rng.shuffle(rows)
    ans = _rank_text(rows, key=lambda r: r[1], reverse=False)
    wrongs = {_rank_text(rows, key=lambda r: r[1], reverse=True): "That is from worst to best; the best conductor melts the wax first.",
              ", ".join(n for n, _ in rows): "That is just the order in the table; sort by time.",
              ", ".join(n for n, _ in sorted(rows, key=lambda r: r[0])): "Sort by the times, not alphabetically."}
    wrongs = {k: v for k, v in wrongs.items() if k != ans}
    while len(wrongs) < 3:
        perm = rows[:]
        rng.shuffle(perm)
        k = ", ".join(n for n, _ in perm)
        if k != ans:
            wrongs[k] = "Sort the rods by the time taken, shortest first."
    table = md_table(["rod", "time for wax to melt / s"], [[n, t] for n, t in rows])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"Rods of four materials are heated at one end; wax at the other end melts after the times shown.\n\n{table}\n\nWhich list gives the rods from BEST to WORST conductor?",
               "shorter time → better conductor", [f"order of increasing time: **{ans}**"],
               ["Which melts the wax first?", "The best conductor.", "Sort by time, shortest first."])


@template("c8x_rate_conduction_thickness", chapter=8, level=2, lo="8b")
def rate_conduction_thickness(rng):
    P1 = nice(rng, 200, 300, 400)
    k = nice(rng, 2, 4)
    return mk(rng, P1 / k, [(P1 * k, "A THICKER wall conducts LESS: divide."), (P1, "The thickness affects the rate."), (P1 / (k * k), "The rate is inversely proportional to thickness, not thickness².")],
              "W", f"The rate of conduction through a wall is inversely proportional to its thickness (other things unchanged).\n\n{md_table(['wall', 'thickness', 'rate of energy loss / W'], [['original', 'd', P1], ['new', f'{k}d', '?']])}\n\nWhat is the new rate of energy loss?",
              "rate ∝ 1 ÷ thickness", [f"rate = {P1} ÷ {k} = **{fmt(P1 / k)} W**"],
              ["Thicker walls conduct less.", "Inversely proportional.", f"Divide by {k}."])


@template("c8x_room_temp_heights", chapter=8, level=2, lo="8c")
def room_temp_heights(rng):
    floor = nice(rng, 18, 19, 20)
    rise = nice(rng, 2, 3, 4)
    temps = [floor + i * rise for i in range(4)]
    return mk(rng, temps[3] - temps[0], [(temps[3], "Find the DIFFERENCE between ceiling and floor."), (rise, "That is the rise per step; use the full height."), (temps[3] + temps[0], "Subtract.")],
              "°C", f"A heater is switched on near the floor of a room. Thermometers at different heights read:\n\n{md_table(['height above floor / m', 'temperature / °C'], [[fmt(h), t] for h, t in zip([0.5, 1.0, 1.5, 2.0], temps)])}\n\nHow much warmer is it at 2.0 m than at 0.5 m?",
              "warm air rises by convection, so it is warmer higher up", [f"{temps[3]} − {temps[0]} = **{temps[3] - temps[0]} °C**"],
              ["Read both temperatures.", "Subtract.", "Warm air collects near the ceiling."], dp=0)


@template("c8x_hot_water_density", chapter=8, level=2, lo="8c")
def hot_water_density(rng):
    m = nice(rng, 500, 1000)
    V_cold = m / 1.000
    V_hot = m / 0.97
    return mk(rng, V_hot - V_cold, [(V_hot, "Find the INCREASE in volume."), (V_cold, "That is the cold volume."), (m * 0.03, "Use V = m ÷ ρ for each temperature.")],
              "cm³", f"Water expands when heated, so its density falls.\n\n{md_table(['temperature / °C', 'density / g/cm³'], [[20, '1.00'], [90, '0.97']])}\n\nBy how much does the volume of **{m} g** of water increase when heated from 20 °C to 90 °C?",
              "V = m ÷ ρ at each temperature; subtract", [f"V₂₀ = {m} ÷ 1.00 = {fmt(V_cold)} cm³; V₉₀ = {m} ÷ 0.97 = {fmt(V_hot)} cm³", f"increase = **{fmt(V_hot - V_cold)} cm³**"],
              ["Find the volume at each temperature.", "V = m ÷ ρ.", "Subtract."])


@template("c8x_radiation_area_fins", chapter=8, level=2, lo="8d")
def radiation_area_fins(rng):
    P1 = nice(rng, 50, 60, 80)
    k = nice(rng, 2, 3, 4)
    return mk(rng, P1 * k, [(P1 / k, "A LARGER area emits MORE."), (P1, "The area affects the rate."), (P1 * k * k, "Rate ∝ area, not area².")],
              "W", f"Fins on an engine increase its surface area. The rate of emission of infrared radiation is proportional to the surface area.\n\n{md_table(['', 'surface area', 'rate of emission / W'], [['without fins', 'A', P1], ['with fins', f'{k}A', '?']])}\n\nWhat is the rate of emission with the fins (same temperature and surface)?",
              "rate ∝ area", [f"rate = {P1} × {k} = **{P1 * k} W**"],
              ["What does the area do?", "Rate ∝ area.", f"Multiply by {k}."])


@template("c8x_heater_distance_cans", chapter=8, level=2, lo="8d")
def heater_distance_cans(rng):
    tb = nice(rng, 40, 45, 50)
    ts = nice(rng, 120, 150, 180)
    wrongs = {"the shiny can, because it reflects the radiation onto its wax": "A shiny surface reflects radiation AWAY.",
              "both at the same time, because they are the same distance away": "Their surfaces absorb differently.",
              "neither, because radiation needs a medium": "Radiation does not need a medium."}
    table = md_table(["can", "time for wax to melt / s"], [["dull black", tb], ["shiny silver", ts]])
    return mkt(rng, f"the dull black can, after {tb} s, because dull black is the better absorber", wrongs,
               f"Two copper cans are placed the same distance from a radiant heater, with wax on their far sides.\n\n{table}\n\nWhich wax melts first, and why?",
               "dull black: good absorber; shiny: good reflector", [f"black: {tb} s, shiny: {ts} s → **dull black absorbs better**"],
               ["Which surface absorbs infrared best?", "Dull black.", "Its wax melts first."])


@template("c8x_blanket_loss", chapter=8, level=2, lo="8e")
def blanket_loss(rng):
    P1 = nice(rng, 100, 120, 150)
    frac = nice(rng, 0.4, 0.5, 0.6, 0.7)
    P2 = P1 * (1 - frac)
    return mk(rng, P2, [(P1 * frac, "That is the energy SAVED per second; find the new loss."), (P1, "The blanket reduces the loss."), (P1 + P1 * frac, "The loss decreases.")],
              "W", f"A shiny emergency blanket reduces the rate of energy loss from a person by radiation and convection.\n\n{md_table(['quantity', 'value'], [['rate of loss without blanket', f'{P1} W'], ['fraction of loss prevented', f'{frac:g}']])}\n\nWhat is the rate of energy loss with the blanket?",
              "new loss = (1 − fraction prevented) × old loss", [f"= {1 - frac:g} × {P1} = **{fmt(P2)} W**"],
              ["What fraction of the loss remains?", "1 − fraction prevented.", "Multiply."])


@template("c8x_double_glazing", chapter=8, level=2, lo="8e")
def double_glazing(rng):
    P1 = nice(rng, 300, 400, 500)
    P2 = P1 * nice(rng, 0.4, 0.5)
    t = 3600
    E = (P1 - P2) * t / 1000
    return mk(rng, E, [((P1 - P2) * t, "That is in J; the answer is in kJ."), ((P1 - P2) / 1000, "Multiply by the time in seconds (1 h = 3600 s)."), (P1 * t / 1000, "Use the DIFFERENCE in the rates.")],
              "kJ", f"A window is replaced with double glazing (trapped air between two panes).\n\n{md_table(['window', 'rate of energy loss / W'], [['single glazed', P1], ['double glazed', fmt(P2)]])}\n\nHow much energy is saved in one hour, in kJ?",
              "energy saved = (P₁ − P₂) × t", [f"ΔP = {P1} − {fmt(P2)} = {fmt(P1 - P2)} W", f"E = {fmt(P1 - P2)} × 3600 = {fmt((P1 - P2) * t)} J = **{fmt(E)} kJ**"],
              ["Find the reduction in power.", "Energy = power × time.", "1 hour = 3600 s; convert to kJ."])


# ================================================================== L3
@template("c8x_cooling_rate_initial", chapter=8, level=3, lo="8a")
def cooling_rate_initial(rng):
    T0 = nice(rng, 80, 90)
    d1 = nice(rng, 10, 12, 15)
    pts = [(0, T0), (2, T0 - d1), (4, T0 - d1 - d1 * 0.6), (6, T0 - d1 - d1 * 0.96), (8, T0 - d1 - d1 * 1.18)]
    rate = d1 / 2
    return mk(rng, rate, [(d1, "That is the drop in 2 minutes; divide by the time."), ((pts[0][1] - pts[-1][1]) / 8, "That is the average rate over 8 min; the question asks for the first 2 minutes."), (d1 * 2, "Divide by 2 min.")],
              "°C/min", f"Fig. 1 shows how the temperature of a beaker of hot water changes as it cools. What is the average rate of cooling over the first 2 minutes?",
              "rate = temperature drop ÷ time", [f"drop in 2 min = {T0} − {fmt(T0 - d1)} = {d1} °C", f"rate = {d1} ÷ 2 = **{fmt(rate)} °C/min**"],
              ["Read the temperatures at 0 and 2 min.", "Find the drop.", "Divide by the time."], figure=figs2.temp_time_graph(pts))


@template("c8x_conduction_temp_gradient", chapter=8, level=3, lo="8b")
def conduction_temp_gradient(rng):
    Th = nice(rng, 100, 90, 80)
    Tc = nice(rng, 20, 25, 30)
    L = nice(rng, 0.2, 0.4, 0.5)
    return mk(rng, (Th - Tc) / L, [((Th - Tc) * L, "Divide by the length."), (Th / L, "Use the temperature DIFFERENCE between the ends."), ((Th + Tc) / L, "Subtract the end temperatures.")],
              "°C/m", f"A metal bar conducts heat steadily from a hot end to a cold end.\n\n{md_table(['quantity', 'value'], [['hot end', f'{Th} °C'], ['cold end', f'{Tc} °C'], ['length', f'{fmt(L)} m']])}\n\nWhat is the temperature fall per metre along the bar?",
              "temperature gradient = (T_hot − T_cold) ÷ length", [f"= ({Th} − {Tc}) ÷ {fmt(L)} = **{fmt((Th - Tc) / L)} °C/m**"],
              ["Find the temperature difference.", "Divide by the length.", "Units °C per metre."])


@template("c8x_conductor_ratio", chapter=8, level=3, lo="8b")
def conductor_ratio(rng):
    k_cu = 400
    other = rng.choice([("glass", 1.0), ("wood", 0.15), ("iron", 80), ("water", 0.6)])
    return mk(rng, k_cu / other[1], [(other[1] / k_cu, "Copper conducts MORE: divide copper's value by the other."), (k_cu - other[1], "Find the ratio, not the difference."), (k_cu, "Divide by the other material's value.")],
              "times", f"The table gives how well materials conduct heat (larger number = better conductor).\n\n{md_table(['material', 'thermal conductivity / W per m per °C'], [['copper', k_cu], [other[0], other[1]]])}\n\nHow many times better a conductor is copper than {other[0]}?",
              "ratio = k_copper ÷ k_other", [f"{k_cu} ÷ {other[1]} = **{fmt(k_cu / other[1])}**"],
              ["Compare the two values.", "Divide.", "Copper's value on top."])


@template("c8x_convection_tank_top", chapter=8, level=3, lo="8c")
def convection_tank_top(rng):
    top = nice(rng, 60, 65, 70)
    bottom = nice(rng, 15, 18, 20)
    pos = rng.choice(["top", "bottom"])
    if pos == "top":
        ans = "only the water above the heater gets hot, because hot water rises and stays at the top"
        wrongs = {"all the water heats evenly by convection": "Hot water at the top cannot sink to set up a convection current.",
                  "the water at the bottom gets hottest": "Hot water rises, away from the bottom.",
                  "the water heats mainly by conduction downwards quickly": "Water is a poor conductor."}
        T_top, T_bottom = top, bottom
    else:
        ans = "all the water heats, because hot water rises and cooler water sinks to the heater"
        wrongs = {"only the water at the bottom gets hot": "Hot water rises, setting up a convection current.",
                  "only the water at the top gets hot": "Convection mixes the whole tank.",
                  "the water heats by radiation only": "Convection is the main process in water."}
        T_top, T_bottom = top, top - nice(rng, 2, 3)
    table = md_table(["position in tank", "temperature after 1 hour / °C"], [["top", T_top], ["bottom", T_bottom]])
    return mkt(rng, ans, wrongs, f"A hot-water tank has its immersion heater near the **{pos}**.\n\n{table}\n\nWhich explanation fits the readings?",
               "convection: hot water rises, cooler denser water sinks", [f"heater at the {pos} → **{ans}**"],
               ["Where is the heater?", "Hot water rises.", "Can a convection current form below it?"])


@template("c8x_sea_breeze", chapter=8, level=3, lo="8c")
def sea_breeze(rng):
    T_land = nice(rng, 32, 34, 36)
    T_sea = nice(rng, 26, 27, 28)
    wrongs = {"from the land to the sea, because the air over the land is denser": "Warm air over the land is LESS dense and rises.",
              "upwards over the sea": "Warmer air over the land rises; cooler air over the sea moves in.",
              "there is no breeze because both are warm": "The temperature difference drives convection."}
    table = md_table(["surface (daytime)", "temperature / °C"], [["land", T_land], ["sea", T_sea]])
    return mkt(rng, "from the sea to the land, because warm air rises over the land and cooler air flows in", wrongs,
               f"On a sunny day at the coast:\n\n{table}\n\nWhich way does the breeze at ground level blow?",
               "warm air over land rises; cooler air from over the sea flows in to replace it", [f"land warmer ({T_land} °C) → air rises → **sea breeze from sea to land**"],
               ["Which surface is warmer?", "Warm air above it rises.", "Cooler air flows in from the sea."])


@template("c8x_emitter_rate_compare", chapter=8, level=3, lo="8d")
def emitter_rate_compare(rng):
    T0 = nice(rng, 80, 85)
    d_black = nice(rng, 16, 18, 20)
    d_silver = nice(rng, 6, 8)
    t = 10
    return mk(rng, (d_black - d_silver) / t, [(d_black - d_silver, "Divide by the time to get a RATE."), (d_black / t, "Find the difference between the two rates."), ((d_black + d_silver) / t, "Subtract the rates.")],
              "°C/min", f"Two identical cans of hot water are painted differently (Fig. 1).\n\n{md_table(['can', 'start / °C', 'after 10 min / °C'], [['dull black', T0, T0 - d_black], ['shiny silver', T0, T0 - d_silver]])}\n\nHow much faster, in °C/min, does the black can cool on average?",
              "rate = drop ÷ time for each; subtract", [f"black: {d_black} ÷ 10 = {fmt(d_black / t)} °C/min; silver: {d_silver} ÷ 10 = {fmt(d_silver / t)} °C/min", f"difference = **{fmt((d_black - d_silver) / t)} °C/min**"],
              ["Find each temperature drop.", "Divide by 10 min.", "Subtract."], figure=sketches.two_cups_sketch())


@template("c8x_flask_parts", chapter=8, level=3, lo="8e")
def flask_parts(rng):
    part, process = rng.choice([("vacuum between the walls", "conduction and convection"), ("silvered surfaces", "radiation"), ("stopper", "convection and evaporation from the top")])
    allp = {"vacuum between the walls": "conduction and convection", "silvered surfaces": "radiation", "stopper": "convection and evaporation from the top"}
    wrongs = {v: f"That is reduced by the {k}." for k, v in allp.items() if v != process}
    wrongs["all heat transfer completely"] = "No single part stops every transfer."
    return mkt(rng, process, wrongs, f"Fig. 1 shows a vacuum flask. Which energy transfer(s) does the **{part}** mainly reduce?",
               "vacuum: no particles → no conduction or convection; silvering: reflects/poorly emits IR; stopper: stops convection and evaporation", [f"{part} → **{process}**"],
               ["What does each part do?", "A vacuum has no particles.", "Shiny surfaces affect radiation."], figure=sketches.flask_sketch())


@template("c8x_payback_insulation", chapter=8, level=3, lo="8e")
def payback_insulation(rng):
    cost = nice(rng, 600, 800, 1200)
    save = nice(rng, 150, 200, 240)
    return mk(rng, cost / save, [(save / cost, "Payback time = cost ÷ yearly saving."), (cost - save, "Divide, do not subtract."), (cost / save * 12, "The saving is per YEAR; give the answer in years.")],
              "years", f"A family insulates their loft.\n\n{md_table(['quantity', 'value'], [['cost of insulation', f'${cost}'], ['saving on energy bills per year', f'${save}']])}\n\nWhat is the payback time?",
              "payback time = cost ÷ saving per year", [f"= {cost} ÷ {save} = **{fmt(cost / save)} years**"],
              ["How long until the savings equal the cost?", "Divide the cost by the yearly saving.", "Answer in years."])


@template("c8x_radiation_hotter_object", chapter=8, level=3, lo="8d")
def radiation_hotter_object(rng):
    rows = [("A", 40), ("B", 60), ("C", 80), ("D", 100)]
    rng.shuffle(rows)
    ans = max(rows, key=lambda r: r[1])[0]
    wrongs = {n: "A hotter surface emits infrared at a greater rate." for n, t in rows if n != ans}
    table = md_table(["identical black block", "surface temperature / °C"], [[n, t] for n, t in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich block emits infrared radiation at the greatest rate?",
               "higher surface temperature → greater rate of emission", [f"hottest → **{ans}**"],
               ["What factors affect the rate of emission?", "Colour, texture, area and temperature.", "Only temperature differs here."])


# ================================================================== L4
@template("c8x_mix_unequal", chapter=8, level=4, lo="8a")
def mix_unequal(rng):
    m1, T1 = nice(rng, 200, 300), nice(rng, 15, 20)
    m2, T2 = nice(rng, 100, 150), nice(rng, 70, 80)
    Tf = (m1 * T1 + m2 * T2) / (m1 + m2)
    return mk(rng, Tf, [((T1 + T2) / 2, "The masses differ, so the final temperature is NOT the simple average."), ((m1 * T2 + m2 * T1) / (m1 + m2), "Pair each mass with its own temperature."), (T2 - T1, "The final temperature lies between the two.")],
              "°C", f"Cold and hot water are mixed in an insulated flask.\n\n{md_table(['sample', 'mass / g', 'temperature / °C'], [['cold', m1, T1], ['hot', m2, T2]])}\n\nWhat is the final temperature?",
              "energy lost by hot = energy gained by cold → T_f = (m₁T₁ + m₂T₂) ÷ (m₁ + m₂)", [f"T_f = ({m1}×{T1} + {m2}×{T2}) ÷ {m1 + m2}", f"= **{fmt(Tf)} °C**"],
              ["Energy lost = energy gained.", "Same substance, so weight by mass.", "Mass-weighted average."])


@template("c8x_time_to_equilibrium", chapter=8, level=4, lo="8a")
def time_to_equilibrium(rng):
    Troom = nice(rng, 25, 28, 30)
    T0 = Troom + nice(rng, 40, 50, 60)
    half = nice(rng, 5, 6, 8)
    pts = [(0, T0), (half, Troom + (T0 - Troom) / 2), (2 * half, Troom + (T0 - Troom) / 4), (3 * half, Troom + (T0 - Troom) / 8), (4 * half, Troom + (T0 - Troom) / 16)]
    return mk(rng, half, [(2 * half, "That is the time for the difference to fall to a QUARTER."), (half / 2, "Read where the excess has halved."), ((T0 - Troom) / 2, "That is a temperature, not a time.")],
              "min", f"Fig. 1 shows a cooling curve for a hot liquid in a room at **{Troom} °C**. How long does it take for the temperature difference between the liquid and the room to halve from its starting value?",
              "difference halves when T = T_room + (T₀ − T_room) ÷ 2", [f"start difference = {T0 - Troom} °C; half = {fmt((T0 - Troom) / 2)} °C → T = {fmt(Troom + (T0 - Troom) / 2)} °C", f"read off the graph: **{half} min**"],
              ["Find the starting temperature difference.", "Halve it and add the room temperature.", "Read the time from the graph."], figure=figs2.temp_time_graph(pts), dp=0)


@template("c8x_conduction_rate_area", chapter=8, level=4, lo="8b")
def conduction_rate_area(rng):
    P1 = nice(rng, 120, 150, 200)
    a = nice(rng, 2, 3)
    t = nice(rng, 2, 4)
    P2 = P1 * a / t
    return mk(rng, P2, [(P1 * a * t, "A thicker wall REDUCES the rate: divide by the thickness factor."), (P1 * t / a, "A larger area INCREASES the rate."), (P1, "Both changes affect the rate.")],
              "W", f"The rate of conduction through a wall is proportional to its area and inversely proportional to its thickness.\n\n{md_table(['wall', 'area', 'thickness', 'rate / W'], [['old', 'A', 'd', P1], ['new', f'{a}A', f'{t}d', '?']])}\n\nWhat is the rate through the new wall (same materials and temperatures)?",
              "rate ∝ A ÷ d", [f"rate = {P1} × {a} ÷ {t} = **{fmt(P2)} W**"],
              ["Area: rate ∝ A.", "Thickness: rate ∝ 1/d.", "Apply both factors."])


@template("c8x_trapped_air_layers", chapter=8, level=4, lo="8b")
def trapped_air_layers(rng):
    rows = [("1 layer of cotton", nice(rng, 30, 32)), ("2 layers of cotton", nice(rng, 24, 26)), ("wool jumper (trapped air)", nice(rng, 16, 18)), ("thin nylon", nice(rng, 34, 36))]
    base = rows[0][1]
    best = min(rows, key=lambda r: r[1])
    pct = (base - best[1]) / base * 100
    return mk(rng, pct, [((base - best[1]), "Express the reduction as a percentage of the single-layer value."), (best[1] / base * 100, "That is the percentage REMAINING."), ((base - best[1]) / best[1] * 100, "Divide by the single-layer value.")],
              "%", f"Model 'arms' of hot water are wrapped in different materials and the temperature drop in 15 min is measured.\n\n{md_table(['wrapping', 'temperature drop / °C'], [[n, d] for n, d in rows])}\n\nBy what percentage does the best wrapping reduce the drop compared with 1 layer of cotton?",
              "% reduction = (d_cotton − d_best) ÷ d_cotton × 100%", [f"best: {best[0]}, drop {best[1]} °C", f"% = ({base} − {best[1]}) ÷ {base} × 100% = **{fmt(pct)}%**"],
              ["Find the best wrapping (smallest drop).", "Find the reduction compared with cotton.", "Express as a percentage."])


@template("c8x_convection_oven_elements", chapter=8, level=4, lo="8c")
def convection_oven_elements(rng):
    rows = [("top shelf", nice(rng, 210, 220)), ("middle shelf", nice(rng, 190, 200)), ("bottom shelf", nice(rng, 160, 170))]
    diff = rows[0][1] - rows[2][1]
    return mk(rng, diff, [(rows[0][1], "Find the DIFFERENCE between the shelves."), (rows[0][1] - rows[1][1], "Compare the top and BOTTOM shelves."), (rows[0][1] + rows[2][1], "Subtract.")],
              "°C", f"An oven has its heating element at the bottom. After warming up, the shelf temperatures are:\n\n{md_table(['position', 'temperature / °C'], [[n, t] for n, t in rows])}\n\nHow much hotter is the top shelf than the bottom shelf?",
              "convection carries hot air to the top", [f"{rows[0][1]} − {rows[2][1]} = **{diff} °C**"],
              ["Read the top and bottom values.", "Subtract.", "Hot air rises by convection."], dp=0)


@template("c8x_convection_rate_dye", chapter=8, level=4, lo="8c")
def convection_rate_dye(rng):
    h = nice(rng, 8, 10, 12, 15)
    t = nice(rng, 20, 25, 30, 40)
    return mk(rng, h / t, [(t / h, "Speed = distance ÷ time."), (h * t, "Divide distance by time."), (h / t * 60, "The answer is in cm/s.")],
              "cm/s", f"A crystal of dye at the bottom of a beaker of water is heated gently. A coloured stream rises by convection (as in Fig. 1).\n\n{md_table(['quantity', 'value'], [['height risen by dye', f'{h} cm'], ['time taken', f'{t} s']])}\n\nWhat is the average speed of the rising water?",
              "speed = distance ÷ time", [f"= {h} ÷ {t} = **{fmt(h / t)} cm/s**"],
              ["Use speed = distance ÷ time.", "The dye shows the water moving.", "Divide."], figure=sketches.convection_sketch())


@template("c8x_greenhouse_temp", chapter=8, level=4, lo="8e")
def greenhouse_temp(rng):
    out = [nice(rng, 22, 24), nice(rng, 28, 30), nice(rng, 32, 34)]
    inside = [o + nice(rng, 8, 10, 12) for o in out]
    avg = sum(i - o for i, o in zip(inside, out)) / 3
    return mk(rng, avg, [(max(i - o for i, o in zip(inside, out)), "Average the three differences."), (sum(inside) / 3, "That is the average INSIDE temperature."), (sum(i - o for i, o in zip(inside, out)), "Divide by 3.")],
              "°C", f"Temperatures are measured inside and outside a greenhouse.\n\n{md_table(['time', 'outside / °C', 'inside / °C'], [[tm, o, i] for tm, o, i in zip(['9 am', '12 noon', '3 pm'], out, inside)])}\n\nOn average, how much warmer is it inside?",
              "average of (inside − outside)", [", ".join(f"{i - o}" for i, o in zip(inside, out)) + f" → average **{fmt(avg)} °C**"],
              ["Find the difference at each time.", "Add them.", "Divide by 3."])


@template("c8x_flask_energy_loss", chapter=8, level=4, lo="8e")
def flask_energy_loss(rng):
    P = nice(rng, 2, 3, 4)
    t_h = nice(rng, 4, 6, 8)
    E = P * t_h * 3600 / 1000
    return mk(rng, E, [(P * t_h, "Convert hours to seconds (× 3600)."), (P * t_h * 60 / 1000, "1 hour = 3600 s, not 60 s."), (P * t_h * 3600, "That is in J; the answer is in kJ.")],
              "kJ", f"A vacuum flask (Fig. 1) loses energy slowly.\n\n{md_table(['quantity', 'value'], [['average rate of energy loss', f'{P} W'], ['time', f'{t_h} hours']])}\n\nHow much energy does it lose, in kJ?",
              "E = P t (t in s)", [f"t = {t_h} × 3600 = {t_h * 3600} s", f"E = {P} × {t_h * 3600} = {P * t_h * 3600} J = **{fmt(E)} kJ**"],
              ["Energy = power × time.", "Time in seconds.", "Convert to kJ."], figure=sketches.flask_sketch())


# ================================================================== L5
@template("c8x_three_cans_ranking", chapter=8, level=5, lo="8e")
def three_cans_ranking(rng):
    T0 = nice(rng, 80, 85, 90)
    A, B, C = nice(rng, 12, 14), nice(rng, 20, 22), nice(rng, 6, 8)
    rows = [("A: shiny, with lid", C), ("B: dull black, no lid", B), ("C: shiny, no lid", A)]
    shuffled = rows[:]
    rng.shuffle(shuffled)
    ans = "B, C, A"
    wrongs = {"A, C, B": "That is from slowest to fastest.", "C, B, A": "Compare all three drops.", "B, A, C": "The lid on A reduces convection and evaporation, so A cools slowest."}
    table = md_table(["copper can", "start / °C", "after 10 min / °C"], [[n, T0, T0 - d] for n, d in shuffled])
    return mkt(rng, ans, wrongs, f"Three copper cans contain equal volumes of hot water.\n\n{table}\n\nWhich list orders the cans from FASTEST to SLOWEST cooling?",
               "dull black emits best; a lid reduces convection and evaporation", [f"drops: B {B} °C, C {A} °C, A {C} °C → **B, C, A**"],
               ["Find each temperature drop.", "Largest drop cools fastest.", "Order them."])


@template("c8x_mix_metal_water", chapter=8, level=5, lo="8a")
def mix_metal_water(rng):
    mw, Tw = nice(rng, 200, 250), nice(rng, 20, 22)
    Tm = 100
    Tf = Tw + nice(rng, 3, 4, 5)
    E_gain = mw / 1000 * 4200 * (Tf - Tw)
    return mk(rng, E_gain, [(mw * 4200 * (Tf - Tw), "Convert the mass to kg."), (mw / 1000 * 4200 * (Tm - Tf), "The water warms from its own start temperature to the final temperature."), (mw / 1000 * 4200 * Tf, "Use the temperature CHANGE of the water.")],
              "J", f"A hot metal block at 100 °C is dropped into water in an insulated cup and they reach thermal equilibrium.\n\n{md_table(['quantity', 'value'], [['mass of water', f'{mw} g'], ['initial water temperature', f'{Tw} °C'], ['final temperature', f'{Tf} °C'], ['energy to warm 1 kg of water by 1 °C', '4200 J']])}\n\nHow much energy did the block transfer to the water?",
              "energy gained by water = m × 4200 × ΔT (= energy lost by block)", [f"ΔT = {Tf} − {Tw} = {Tf - Tw} °C", f"E = {fmt(mw / 1000)} × 4200 × {Tf - Tw} = **{fmt(E_gain)} J**"],
              ["Energy flows until both are at the same temperature.", "The water's gain equals the block's loss.", "Use the water's mass in kg and its ΔT."])


@template("c8x_equilibrium_rate_change", chapter=8, level=5, lo="8a")
def equilibrium_rate_change(rng):
    k = nice(rng, 0.08, 0.1, 0.12)
    Troom = 25
    T1, T2 = nice(rng, 85, 75), nice(rng, 45, 35)
    r1, r2 = k * (T1 - Troom), k * (T2 - Troom)
    return mk(rng, r1 / r2, [(r2 / r1, "The HOTTER liquid cools faster; the ratio is greater than 1."), (T1 / T2, "Use the temperature DIFFERENCE from the room, not the temperatures."), ((T1 - T2) / Troom, "Rate ∝ (T − T_room).")],
              "times", f"The rate of cooling of a liquid is proportional to its temperature difference from the room (room at {Troom} °C).\n\n{md_table(['moment', 'temperature of liquid / °C'], [['earlier', T1], ['later', T2]])}\n\nHow many times faster is it cooling at the earlier moment?",
              "rate ∝ (T − T_room) → ratio = (T₁ − 25) ÷ (T₂ − 25)", [f"({T1} − 25) ÷ ({T2} − 25) = {T1 - Troom} ÷ {T2 - Troom}", f"= **{fmt(r1 / r2)}**"],
              ["What decides the rate of cooling?", "The difference from room temperature.", "Find the ratio of the differences."])


@template("c8x_wall_composite", chapter=8, level=5, lo="8b")
def wall_composite(rng):
    P_brick = nice(rng, 900, 1000, 1200)
    f_cavity = nice(rng, 0.3, 0.4, 0.5)
    f_foam = nice(rng, 0.4, 0.5)
    P = P_brick * f_cavity * f_foam
    return mk(rng, P, [(P_brick * f_cavity, "Apply BOTH reductions."), (P_brick * (1 - f_cavity) * (1 - f_foam), "The factors given are the fractions that REMAIN."), (P_brick * (f_cavity + f_foam) / 2, "Multiply the factors.")],
              "W", f"A house wall is improved in two steps.\n\n{md_table(['wall', 'fraction of previous heat loss that remains'], [['solid brick', '1 (loss = ' + str(P_brick) + ' W)'], ['add an air cavity', f'{f_cavity:g}'], ['fill cavity with foam', f'{f_foam:g}']])}\n\nWhat is the final rate of heat loss through the wall?",
              "multiply the remaining fractions", [f"P = {P_brick} × {f_cavity:g} × {f_foam:g} = **{fmt(P)} W**"],
              ["Each step leaves a fraction of the loss.", "Apply them one after the other.", "Multiply."])


@template("c8x_conduction_pan_base", chapter=8, level=5, lo="8b")
def conduction_pan_base(rng):
    k_al, k_ss = 200, 16
    d = nice(rng, 3, 4, 5)
    ratio = k_al / k_ss
    return mk(rng, ratio, [(k_ss / k_al, "Aluminium conducts better: the rate is LARGER."), (k_al - k_ss, "Find the ratio of the conductivities."), (ratio * d, "The thickness is the same, so it cancels.")],
              "times", f"Two pan bases have the same area and thickness ({d} mm) and the same temperature difference across them.\n\n{md_table(['base material', 'thermal conductivity / W per m per °C'], [['aluminium', k_al], ['stainless steel', k_ss]])}\n\nHow many times faster does energy conduct through the aluminium base?",
              "rate ∝ conductivity (same A, d, ΔT)", [f"{k_al} ÷ {k_ss} = **{fmt(ratio)}**"],
              ["What is the same for both?", "So rate ∝ conductivity.", "Divide."])


@template("c8x_convection_radiator_room", chapter=8, level=5, lo="8c")
def convection_radiator_room(rng):
    rho_c, rho_h = 1.20, nice(rng, 1.05, 1.10, 1.00)
    V = nice(rng, 0.5, 1.0, 2.0)
    m_diff = (rho_c - rho_h) * V
    W_diff = m_diff * 10
    return mk(rng, W_diff, [(m_diff, "That is the mass difference in kg; multiply by g for the weight."), (rho_h * V * 10, "Find the DIFFERENCE between cold and warm air."), (rho_c * V * 10, "Use the difference in densities.")],
              "N", f"Air heated by a radiator expands. Compare the same volume of air before and after heating.\n\n{md_table(['air', 'density / kg/m³'], [['cool', fmt(rho_c)], ['warm', fmt(rho_h)]])}\n\nFor **{fmt(V)} m³** of air, by how much does its weight decrease when warmed (g = 10 N/kg)? This is why warm air rises.",
              "Δm = Δρ × V; ΔW = Δm × g", [f"Δρ = {fmt(rho_c)} − {fmt(rho_h)} = {fmt(rho_c - rho_h)} kg/m³", f"Δm = {fmt(rho_c - rho_h)} × {fmt(V)} = {fmt(m_diff)} kg; ΔW = **{fmt(W_diff)} N**"],
              ["Find the difference in density.", "Multiply by the volume to get mass.", "Multiply by g."])


@template("c8x_convection_current_speed", chapter=8, level=5, lo="8c")
def convection_current_speed(rng):
    L = nice(rng, 3.0, 4.0, 5.0)
    H = nice(rng, 2.5, 3.0)
    t = nice(rng, 60, 80, 100)
    loop = 2 * (L + H)
    return mk(rng, loop / t, [(L / t, "The air travels round the WHOLE loop: up, across, down and back."), ((L + H) / t, "Include both the up-and-across and the down-and-back parts."), (loop * t, "Speed = distance ÷ time.")],
              "m/s", f"A heater by one wall sets up a convection current that circulates round a room: up the heater wall, across the ceiling, down the far wall and back across the floor.\n\n{md_table(['quantity', 'value'], [['width of room', f'{fmt(L)} m'], ['height of room', f'{fmt(H)} m'], ['time for one loop', f'{t} s']])}\n\nWhat is the average speed of the air?",
              "loop distance = 2 × (width + height); speed = distance ÷ time", [f"distance = 2 × ({fmt(L)} + {fmt(H)}) = {fmt(loop)} m", f"speed = {fmt(loop)} ÷ {t} = **{fmt(loop / t)} m/s**"],
              ["Trace the loop.", "Add up all four sides.", "Divide by the time."])


@template("c8x_radiation_surface_compare", chapter=8, level=5, lo="8d")
def radiation_surface_compare(rng):
    P_black = nice(rng, 40, 50, 60)
    e_silver = nice(rng, 0.1, 0.05)
    e_white = 0.9
    choice = rng.choice([("shiny silver", e_silver), ("matt white paint", e_white)])
    P = P_black * choice[1]
    return mk(rng, P, [(P_black / choice[1], "Multiply by the emissivity, which is less than 1."), (P_black, "The surface changes the rate of emission."), (P_black * (1 - choice[1]), "The value given is the fraction EMITTED compared with black.")],
              "W", f"At the same temperature and area, a surface emits a fraction of what a dull black surface emits.\n\n{md_table(['surface', 'fraction of black-surface emission'], [['dull black', '1 (emits ' + str(P_black) + ' W)'], ['matt white paint', e_white], ['shiny silver', e_silver]])}\n\nWhat is the rate of emission from the **{choice[0]}** surface?",
              "P = fraction × P_black", [f"P = {choice[1]} × {P_black} = **{fmt(P)} W**"],
              ["Find the right fraction.", "Multiply by the black-surface value.", "Shiny surfaces emit least."])


@template("c8x_radiation_temp_graph", chapter=8, level=5, lo="8d")
def radiation_temp_graph(rng):
    T0 = nice(rng, 80, 90)
    d_b = nice(rng, 30, 35, 40)
    d_s = nice(rng, 10, 15)
    curves = [("black", [(0, T0), (5, T0 - d_b * 0.55), (10, T0 - d_b * 0.85), (15, T0 - d_b)]), ("shiny", [(0, T0), (5, T0 - d_s * 0.55), (10, T0 - d_s * 0.85), (15, T0 - d_s)])]
    return mk(rng, d_b - d_s, [(d_b, "That is the black can's drop; find the difference."), (d_s, "That is the shiny can's drop."), (d_b + d_s, "Subtract the drops.")],
              "°C", f"Fig. 1 shows cooling curves for a dull black and a shiny can of hot water. After 15 min, how much more has the black can cooled than the shiny can?",
              "read each final temperature; compare the drops", [f"black drop = {d_b} °C; shiny drop = {d_s} °C", f"difference = **{d_b - d_s} °C**"],
              ["Read both temperatures at 15 min.", "Find each drop.", "Subtract."], figure=figs2.two_curves(curves, 16, 100, 5, 10), dp=0)


@template("c8x_payback_double_glazing", chapter=8, level=5, lo="8e")
def payback_double_glazing(rng):
    P_save = nice(rng, 200, 250, 300)
    hours = nice(rng, 2000, 2500, 3000)
    price = nice(rng, 0.25, 0.30)
    cost = nice(rng, 2400, 3000, 3600)
    kwh = P_save / 1000 * hours
    save = kwh * price
    return mk(rng, cost / save, [(cost / kwh, "Convert the energy saved into money first."), (cost / (P_save * hours * price), "Convert W to kW: kWh = kW × h."), (save / cost, "Payback = cost ÷ saving per year.")],
              "years", f"Double glazing reduces a home's heat loss.\n\n{md_table(['quantity', 'value'], [['reduction in rate of heat loss', f'{P_save} W'], ['hours of heating per year', hours], ['price of electricity', f'${price:.2f} per kWh'], ['cost of double glazing', f'${cost}']])}\n\nWhat is the payback time?",
              "kWh saved = kW × h; saving = kWh × price; payback = cost ÷ saving", [f"energy saved = {fmt(P_save / 1000)} × {hours} = {fmt(kwh)} kWh", f"saving = {fmt(kwh)} × {price:.2f} = ${fmt(save)} per year", f"payback = {cost} ÷ {fmt(save)} = **{fmt(cost / save)} years**"],
              ["Convert the power saved to kW.", "Find the kWh saved per year and its value.", "Divide the cost by the yearly saving."])
