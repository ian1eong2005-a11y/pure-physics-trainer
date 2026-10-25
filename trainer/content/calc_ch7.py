"""Chapter 7 Kinetic Particle Model of Matter (6091): data-reading 'calculation' templates (teacher's choice, 25 Oct 2026):
states from melting/boiling data, compressibility tables, gas pressure proportional reasoning, pressure-temperature graphs."""
from .. import figs, figs2
from .base import fmt, md_table, nice, numeric_options, template, text_options


# ---------------------------------------------------------------- L1
@template("c7_state_from_table", chapter=7, level=1, lo="7a")
def state_from_table(rng):
    subs = [("W", -39, 357), ("X", 0, 100), ("Y", 98, 883), ("Z", -210, -196)]
    rng.shuffle(subs)
    name, mp, bp = rng.choice(subs)
    temp = rng.choice([t for t in (-220, -100, -20, 25, 60, 150, 400, 900) if t != mp and t != bp])
    state = "solid" if temp < mp else "liquid" if temp < bp else "gas"
    wrongs = {s: "" for s in ("solid", "liquid", "gas") if s != state}
    msgs = {"solid": f"{name} is a solid only below its melting point ({mp} °C).",
            "liquid": f"{name} is a liquid only between its melting point ({mp} °C) and its boiling point ({bp} °C).",
            "gas": f"{name} is a gas only above its boiling point ({bp} °C)."}
    wrongs = {s: msgs[s] for s in wrongs}
    wrongs["cannot be determined"] = "The table gives both the melting and boiling points, which is enough to decide."
    opts, key, mis = text_options(rng, state, wrongs)
    table = md_table(["substance", "melting point / °C", "boiling point / °C"], [[n, m, b] for n, m, b in subs])
    return dict(
        stem=f"The table gives the melting and boiling points of four substances.\n\n{table}\n\nWhat is the state of substance **{name}** at **{temp} °C**?",
        options=opts, key=key, misconceptions=mis,
        formula="below the melting point: solid; between melting and boiling points: liquid; above the boiling point: gas",
        working=[f"{name}: melting point {mp} °C, boiling point {bp} °C", f"{temp} °C is {'below the melting point' if state == 'solid' else 'between the melting and boiling points' if state == 'liquid' else 'above the boiling point'}", f"state = **{state}**"],
        hints=[
            "Find the row for the substance and note its two temperatures.",
            "Compare the given temperature with the melting point first, then with the boiling point.",
            f"Is {temp} °C below {mp} °C, between {mp} and {bp} °C, or above {bp} °C?",
        ],
    )


@template("c7_compressibility_table", chapter=7, level=1, lo="7a")
def compressibility_table(rng):
    names = ["P", "Q", "R", "S"]
    gas = rng.choice(names)
    rows, change = [], {}
    for n in names:
        v0 = nice(rng, 50, 60, 80, 100)
        v1 = round(v0 * (rng.choice([0.40, 0.45, 0.50, 0.55]) if n == gas else rng.choice([0.998, 0.999, 1.0])), 1)
        rows.append([n, fmt(v0), fmt(v1)])
        change[n] = round((v0 - v1) / v0 * 100, 1)
    wrongs = {n: f"Sample {n} changed volume by only {change[n]}%: it is a liquid or a solid, whose particles are already close together." for n in names if n != gas}
    opts, key, mis = text_options(rng, gas, wrongs)
    table = md_table(["sample", "volume before / cm³", "volume after / cm³"], rows)
    return dict(
        stem=f"The same large force is applied to four sealed samples. The table shows the volume of each sample before and after the force is applied.\n\n{table}\n\nWhich sample is a gas?",
        options=opts, key=key, misconceptions=mis,
        formula="gases are easily compressed (large % change in volume) because their particles are far apart; liquids and solids are almost incompressible",
        working=[f"percentage change for {gas} = {change[gas]}%, far larger than the others", "a large change in volume under pressure means the particles were far apart", f"sample **{gas}** is the gas"],
        hints=[
            "Which state of matter can be squashed into a much smaller volume? Why, in terms of the spacing of its particles?",
            "Work out roughly how much each volume fell. Three samples barely changed.",
            "The sample whose volume roughly halved is the gas.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c7_pressure_more_particles", chapter=7, level=2, lo="7e")
def pressure_more_particles(rng):
    p1 = nice(rng, 100, 120, 150, 200, 250)
    k = nice(rng, 2, 3, 4)
    p2 = p1 * k
    opts, key, mis = numeric_options(rng, p2, [
        (p1, "More molecules in the same volume at the same temperature means more collisions with the walls each second, so the pressure must rise."),
        (p1 / k, "You divided. Adding molecules INCREASES the number of collisions per second, so the pressure goes up, not down."),
        (p1 * k * k, f"The pressure is proportional to the number of molecules: {k} times as many molecules gives {k} times the pressure, not {k * k} times."),
    ], unit="kPa")
    table = md_table(["", "number of molecules", "pressure / kPa"], [["before", "N", p1], ["after", f"{k}N", "?"]])
    return dict(
        stem=f"A rigid container holds a gas at **{p1} kPa**. More gas is pumped in at the same temperature until it holds **{k} times** as many molecules.\n\n{table}\n\nWhat is the new pressure?",
        options=opts, key=key, misconceptions=mis,
        formula="at constant volume and temperature, pressure ∝ number of molecules (more molecules → proportionally more collisions per second with the walls)",
        working=[f"{k} times as many molecules → {k} times as many collisions with the walls each second", f"pressure = {k} × {p1}", f"= **{p2} kPa**"],
        hints=[
            "Gas pressure comes from molecules colliding with the walls. What happens to the number of collisions per second if there are more molecules in the same space?",
            f"The average speed is unchanged (same temperature), so the number of collisions per second simply scales with the number of molecules: × {k}.",
            f"new pressure = {k} × {p1} kPa.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c7_pressure_from_wall_force", chapter=7, level=3, lo="7e")
def pressure_from_wall_force(rng):
    F = nice(rng, 150, 200, 240, 300, 360, 450)
    A_cm2 = nice(rng, 20, 25, 30, 40, 50, 60)
    p = F / (A_cm2 / 1e4)
    opts, key, mis = numeric_options(rng, p, [
        (F / A_cm2, "You used the area in cm². Pressure in Pa needs the area in m² (1 m² = 10 000 cm²)."),
        (F * A_cm2 / 1e4, "You multiplied force by area. Pressure = force ÷ area."),
        (F / (A_cm2 / 100), "1 m² = 10 000 cm², not 100 cm²."),
    ], unit="Pa", sf=3)
    return dict(
        stem=f"Fig. 1 shows gas trapped in a syringe. The collisions of the gas molecules with the piston exert an average total force of **{F} N** on the piston face, which has an area of **{A_cm2} cm²**. What is the pressure of the gas?",
        figure=figs2.gas_syringe([f"total force on piston = {F} N", f"piston area = {A_cm2} cm²"]),
        options=opts, key=key, misconceptions=mis,
        formula="pressure = total force from the collisions ÷ area of the wall (area in m²)",
        working=[f"area = {A_cm2} cm² = {fmt(A_cm2 / 1e4, sf=3)} m²", f"pressure = {F} ÷ {fmt(A_cm2 / 1e4, sf=3)}", f"= **{fmt(p, sf=3)} Pa**"],
        hints=[
            "The molecules' collisions add up to a steady force on the piston. Pressure is that force spread over the piston's area.",
            f"Convert {A_cm2} cm² to m² first: divide by 10 000.",
            f"p = {F} ÷ {fmt(A_cm2 / 1e4, sf=3)}.",
        ],
    )


@template("c7_volume_temperature_table", chapter=7, level=3, lo="7b")
def volume_temperature_table(rng):
    v20 = nice(rng, 100, 120, 150, 200)
    step = nice(rng, 4, 5, 6, 8)        # cm³ per 10 °C
    temps = [20, 40, 60, 80]
    vols = [v20 + step * (t - 20) / 10 for t in temps]
    ask = rng.choice([30, 50, 70])
    ans = v20 + step * (ask - 20) / 10
    opts, key, mis = numeric_options(rng, ans, [
        (ans + step, "That is the volume 10 °C higher. Read the table more carefully: the asked temperature is halfway between two rows."),
        (ans - step, "That is the volume 10 °C lower. The asked temperature is halfway between two rows."),
        (ans * 2, "Check your reading: the volume changes only slowly with temperature here."),
    ], unit="cm³", sf=3)
    table = md_table(["temperature / °C", "volume / cm³"], [[t, fmt(v)] for t, v in zip(temps, vols)])
    return dict(
        stem=f"A fixed mass of gas is trapped in a syringe whose piston can move freely, so the pressure stays constant. The table shows how the volume changes with temperature.\n\n{table}\n\nThe pattern is uniform. What is the volume at **{ask} °C**?",
        options=opts, key=key, misconceptions=mis,
        formula="read between two rows of a uniform table: the value halfway between two temperatures is halfway between the two volumes",
        working=[f"volume rises by {fmt(step * 2)} cm³ for every 20 °C, i.e. {fmt(step)} cm³ per 10 °C", f"{ask} °C is 10 °C above {ask - 10} °C, so volume = {fmt(v20 + step * (ask - 30) / 10)} + {fmt(step)}", f"= **{fmt(ans, sf=3)} cm³**"],
        hints=[
            "Look at how much the volume changes between neighbouring rows. Is the change the same each time?",
            f"{ask} °C lies exactly halfway between two of the temperatures in the table.",
            "The volume at the halfway temperature is the average of the two neighbouring volumes.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c7_pressure_temperature_graph", chapter=7, level=4, lo="7e")
def pressure_temperature_graph(rng):
    p0 = nice(rng, 100, 120, 150)
    slope = nice(rng, 0.3, 0.4, 0.5)
    ask = nice(rng, 20, 40, 60, 80)
    ans = p0 + slope * ask
    pts = [(0, p0), (100, p0 + slope * 100)]
    opts, key, mis = numeric_options(rng, ans, [
        (p0, "That is the pressure at 0 °C. Read up from the asked temperature to the line, then across to the pressure axis."),
        (ans + slope * 20, "You read the graph 20 °C too high. Find the asked temperature on the horizontal axis carefully."),
        (slope * ask, "That is only the INCREASE in pressure. Add it to the pressure at 0 °C, or simply read the value off the graph."),
    ], unit="kPa", sf=3)
    return dict(
        stem=f"A fixed mass of gas is sealed in a rigid container and heated. Fig. 1 shows how its pressure changes with temperature. What is the pressure at **{ask} °C**?",
        figure=figs.graph(pts, 100, 200, 20, 20, xlabel="temperature / °C", ylabel="pressure / kPa"),
        options=opts, key=key, misconceptions=mis,
        formula="read the graph: find the temperature on the horizontal axis, go up to the line, then across to the pressure axis",
        working=[f"at 0 °C the pressure is {p0} kPa; the line rises {fmt(slope * 100)} kPa over 100 °C ({fmt(slope)} kPa per °C)", f"at {ask} °C: {p0} + {fmt(slope)} × {ask}", f"= **{fmt(ans, sf=3)} kPa**"],
        hints=[
            "This is a reading question: the molecules move faster when heated, hitting the walls harder and more often, so the pressure rises steadily.",
            f"Find {ask} °C on the horizontal axis. Go straight up to the line and straight across to the vertical axis.",
            f"The line starts at {p0} kPa and gains {fmt(slope * 20)} kPa for every 20 °C.",
        ],
    )


@template("c7_pressure_volume_doubled", chapter=7, level=4, lo="7e")
def pressure_volume_doubled(rng):
    p1 = nice(rng, 120, 150, 180, 200, 240, 300)
    k = nice(rng, 2, 3, 4)
    p2 = p1 / k
    opts, key, mis = numeric_options(rng, p2, [
        (p1 * k, "You multiplied. Spreading the same molecules through a larger volume means FEWER collisions per second on each part of the wall, so the pressure falls."),
        (p1, "The temperature is unchanged, but the molecules now hit each square centimetre of wall less often, so the pressure does change."),
        (p1 / (k * k), f"Pressure falls in proportion to the volume increase: {k} times the volume gives 1/{k} of the pressure."),
    ], unit="kPa", sf=3)
    table = md_table(["", "volume", "pressure / kPa"], [["before", "V", p1], ["after", f"{k}V", "?"]])
    return dict(
        stem=f"A fixed mass of gas at **{p1} kPa** is allowed to expand at constant temperature into a container **{k} times** the volume.\n\n{table}\n\nWhat is the new pressure?",
        options=opts, key=key, misconceptions=mis,
        formula="same molecules, same speeds, larger volume → collisions with each unit area of wall are proportionally less frequent: pressure ∝ 1 / volume",
        working=[f"the molecules are spread through {k} times the volume, so each part of the wall is hit 1/{k} as often", f"pressure = {p1} ÷ {k}", f"= **{fmt(p2, sf=3)} kPa**"],
        hints=[
            "The temperature is the same, so the molecules move just as fast. What changes is how often they reach the walls.",
            f"With {k} times the space, the number of collisions per second on any part of the wall drops to 1/{k}.",
            f"new pressure = {p1} ÷ {k}.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c7_pressure_two_changes", chapter=7, level=5, lo="7e")
def pressure_two_changes(rng):
    p1 = nice(rng, 100, 120, 150, 200)
    kn = nice(rng, 2, 3)        # molecules multiplied
    kv = nice(rng, 2, 4)        # volume divided
    p2 = p1 * kn * kv
    opts, key, mis = numeric_options(rng, p2, [
        (p1 * kn, "You allowed for the extra molecules but not for the smaller volume. Both changes increase the pressure."),
        (p1 * kv, "You allowed for the smaller volume but not for the extra molecules. Both changes increase the pressure."),
        (p1 * kn / kv, "Halving the volume INCREASES the pressure (collisions become more frequent), it does not decrease it."),
    ], unit="kPa")
    table = md_table(["", "number of molecules", "volume", "pressure / kPa"], [["before", "N", "V", p1], ["after", f"{kn}N", f"V/{kv}", "?"]])
    return dict(
        stem=f"A gas at **{p1} kPa** is compressed to **1/{kv}** of its volume and, at the same time, the number of molecules is increased to **{kn} times** the original. The temperature is kept constant.\n\n{table}\n\nWhat is the new pressure?",
        options=opts, key=key, misconceptions=mis,
        formula="at constant temperature, pressure ∝ (number of molecules) ÷ (volume): each change multiplies the collision rate per unit area",
        working=[f"{kn} times the molecules → × {kn}", f"1/{kv} of the volume → × {kv}", f"pressure = {p1} × {kn} × {kv} = **{p2} kPa**"],
        hints=[
            "Treat the two changes one at a time. Each one changes how often molecules hit a given area of wall.",
            f"More molecules: × {kn}. Smaller volume: molecules reach the walls more often, × {kv}.",
            f"{p1} × {kn} × {kv} = ?",
        ],
    )


@template("c7_brownian_displacement", chapter=7, level=5, lo="7c")
def brownian_displacement(rng):
    legs = rng.choice([[(3, 0), (0, 4)], [(0, 3), (4, 0)], [(6, 0), (0, 8)], [(5, 0), (0, 12)], [(4, 0), (0, 3)]])
    dist = sum(abs(a) + abs(b) for a, b in legs)
    dx, dy = sum(a for a, _ in legs), sum(b for _, b in legs)
    disp = (dx * dx + dy * dy) ** 0.5
    opts, key, mis = numeric_options(rng, disp, [
        (dist, "That is the total DISTANCE along the path. The question asks how far the particle ends up from where it started (its displacement)."),
        (abs(dx - dy), "You subtracted the two legs. They are at right angles, so use Pythagoras for the straight-line distance."),
        (max(abs(dx), abs(dy)), "That is one leg only. The straight line from start to finish is the hypotenuse."),
    ], unit="µm")
    return dict(
        stem=f"Through a microscope a student watches a smoke particle being jolted by air molecules. In one second it makes the two jumps shown in Fig. 1 (1 square = 1 µm). How far is the particle from its starting point after the two jumps?",
        figure=figs2.vector_grid([("1st", legs[0][0], legs[0][1]), ("2nd", legs[1][0], legs[1][1])] if False else [("1st jump", legs[0][0], legs[0][1])], nx=max(dx, 4) + 3, ny=max(dy, 4) + 2, origin=(1, 1), scale_label="1 square = 1 µm", resultant=None, name_origin="start")
        if False else figs2.vector_grid([("1st jump", legs[0][0], legs[0][1])], nx=max(dx, 4) + 3, ny=max(dy, 4) + 2, origin=(1, 1), scale_label=f"1 square = 1 µm; 2nd jump: {abs(legs[1][0] + legs[1][1])} squares {'up' if legs[1][1] else 'right'} from the end of the 1st", name_origin="start"),
        options=opts, key=key, misconceptions=mis,
        formula="Brownian motion is random: the straight-line displacement after several jolts is much less than the distance moved (Pythagoras for legs at right angles)",
        working=[f"path length = {dist} µm, but the jumps are at right angles", f"displacement = √({abs(dx)}² + {abs(dy)}²) = √{dx * dx + dy * dy}", f"= **{fmt(disp)} µm**"],
        hints=[
            "The two jumps are at right angles. Draw the straight line from the start to the finish.",
            "That straight line is the hypotenuse of a right-angled triangle whose sides are the two jumps.",
            f"√({abs(dx)}² + {abs(dy)}²).",
        ],
    )
