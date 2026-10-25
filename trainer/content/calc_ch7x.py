"""Chapter 7 Kinetic Particle Model of Matter (6091) bank extension: calculation and data-reading templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2015-2025: gas under a frictionless piston, gold
solidifying in a mould, anti-freeze for aircraft wings, ice cubes shrinking in a freezer; school papers 2024-2025)."""
import math

from .. import figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, sci, template

STATES = ["solid", "liquid", "gas"]


def state_at(T, mp, bp):
    return "solid" if T < mp else ("liquid" if T < bp else "gas")


SUBSTANCES = [("ethanol", -114, 78), ("mercury", -39, 357), ("oxygen", -218, -183), ("lead", 327, 1749), ("water", 0, 100), ("bromine", -7, 59), ("sulfur", 115, 445), ("ammonia", -78, -33)]


# ================================================================== L1
@template("c7x_identify_state_fig", chapter=7, level=1, lo="7b")
def identify_state_fig(rng):
    st = rng.choice(STATES)
    desc = {"solid": "closely packed in a regular pattern, vibrating about fixed positions",
            "liquid": "close together but irregularly arranged, sliding past one another",
            "gas": "far apart, moving randomly at high speed"}
    wrongs = {s: f"In a {s} the particles are {desc[s]}." for s in STATES if s != st}
    wrongs["plasma"] = "Only solids, liquids and gases are in this model."
    return mkt(rng, st, wrongs, "Fig. 1 shows the arrangement of particles in a sample. What state is the sample in?",
               "solid: regular, touching; liquid: touching, irregular; gas: far apart", [f"the particles are {desc[st]} → **{st}**"],
               ["Are the particles touching?", "Are they in a regular pattern?", "Match with solid, liquid or gas."], figure=sketches.particles(st))


@template("c7x_spacing_order", chapter=7, level=1, lo="7b")
def spacing_order(rng):
    order = STATES[:]
    rng.shuffle(order)
    names = ("X", "Y", "Z")
    gas_name = names[order.index("gas")]
    wrongs = {n: ("These particles are packed closely." if order[i] != "gas" else "") for i, n in enumerate(names) if n != gas_name}
    wrongs["all have the same spacing"] = "The spacing differs a lot between states."
    return mkt(rng, gas_name, wrongs, "Fig. 1 shows the particles in three samples X, Y and Z. In which sample are the particles furthest apart on average?",
               "gas particles are far apart compared with their size", [f"**{gas_name}** is the gas"],
               ["Look for the sample with most empty space.", "That is the gas.", "Pick its letter."], figure=sketches.three_states(tuple(order), names))


@template("c7x_hottest_sample_ke", chapter=7, level=1, lo="7d")
def hottest_sample_ke(rng):
    temps = rng.sample([5, 18, 25, 37, 42, 60, 75, 90], 4)
    names = ["P", "Q", "R", "S"]
    best = names[temps.index(max(temps))]
    wrongs = {n: "Average kinetic energy is greatest at the HIGHEST temperature." for n in names if n != best}
    table = md_table(["sample of water", "temperature / °C"], [[n, t] for n, t in zip(names, temps)])
    return mkt(rng, best, wrongs, f"Four samples of water are at different temperatures.\n\n{table}\n\nIn which sample do the particles have the greatest average kinetic energy?",
               "higher temperature → greater average kinetic energy of the particles", [f"highest temperature: {max(temps)} °C → **{best}**"],
               ["What does temperature tell you about the particles?", "Higher temperature → faster particles.", "Pick the hottest sample."])


@template("c7x_temp_rise_ke", chapter=7, level=1, lo="7d")
def temp_rise_ke(rng):
    T1, T2 = rng.choice([(20, 60), (15, 45), (30, 80), (40, 10), (70, 25)])
    ans = "increases" if T2 > T1 else "decreases"
    other = "decreases" if ans == "increases" else "increases"
    wrongs = {other: "The particles speed up when it warms and slow down when it cools.", "stays the same": "Average kinetic energy changes with temperature.",
              "becomes zero": "The particles always have some kinetic energy at these temperatures."}
    table = md_table(["", "temperature / °C"], [["start", T1], ["end", T2]])
    return mkt(rng, ans, wrongs, f"The temperature of a block of copper changes.\n\n{table}\n\nWhat happens to the average kinetic energy of its particles?",
               "temperature rises → average KE of particles rises", [f"{T1} °C → {T2} °C: the average kinetic energy **{ans}**"],
               ["Is the block warming or cooling?", "Temperature is linked to average particle KE.", "Match the change."])


@template("c7x_boyle_simple", chapter=7, level=1, lo="7e")
def boyle_simple(rng):
    p1 = nice(rng, 100, 120, 150, 200)
    V1 = nice(rng, 40, 60, 80, 120)
    V2 = V1 / 2
    p2 = p1 * V1 / V2
    return mk(rng, p2, [(p1 / 2, "Halving the volume makes the pressure LARGER."), (p1, "The pressure changes when the volume changes."), (p1 * 4, "pV is constant: halving V doubles p.")],
              "kPa", f"A gas in a syringe is squashed slowly at constant temperature.\n\n{md_table(['', 'volume / cm³', 'pressure / kPa'], [['before', V1, p1], ['after', fmt(V2), '?']])}\n\nWhat is the new pressure?",
              "fixed mass, constant temperature: p₁V₁ = p₂V₂", [f"p₂ = {p1} × {V1} ÷ {fmt(V2)} = **{fmt(p2)} kPa**"],
              ["Is the temperature constant?", "Then p × V stays the same.", "Half the volume → double the pressure."])


@template("c7x_pressure_heat_rigid", chapter=7, level=1, lo="7e")
def pressure_heat_rigid(rng):
    p1 = nice(rng, 100, 120, 150)
    T1, T2 = rng.choice([(20, 60), (25, 80), (15, 50)])
    wrongs = {"decreases": "Faster particles hit the walls harder and more often.", "stays the same": "The particles speed up, so the pressure changes.",
              "falls to zero": "The gas is still in the can."}
    table = md_table(["", "temperature / °C", "pressure / kPa"], [["before", T1, p1], ["after", T2, "?"]])
    return mkt(rng, "increases", wrongs, f"A sealed rigid can of gas is heated.\n\n{table}\n\nWhat happens to the pressure of the gas?",
               "higher temperature, same volume → more frequent and harder collisions → higher pressure", ["the particles move faster, hitting the walls more often and harder → pressure **increases**"],
               ["What happens to the particles' speed?", "How do they hit the walls?", "More often and harder."])


@template("c7x_brownian_cause", chapter=7, level=1, lo="7c")
def brownian_cause(rng):
    medium = rng.choice(["air (in a smoke cell)", "water (pollen grains)"])
    speck = "smoke particles" if "air" in medium else "pollen grains"
    mol = "air molecules" if "air" in medium else "water molecules"
    wrongs = {f"convection currents in the {medium.split(' ')[0]}": "Convection would carry all the specks the same way; the motion is random.",
              f"the {speck} are alive and swimming": "Smoke and dead pollen show the same motion.",
              f"the {speck} attracting each other": "The jiggling is caused by collisions, not attraction."}
    return mkt(rng, f"uneven bombardment by fast-moving {mol}", wrongs,
               f"Fig. 1 shows the zig-zag path of a speck in Brownian motion, observed in {medium}. What causes the motion of the {speck}?",
               "Brownian motion: random collisions from invisible, fast-moving fluid molecules", [f"**uneven bombardment by fast-moving {mol}**"],
               ["Can you see the fluid molecules?", "They are tiny and fast.", "They hit the speck unevenly."], figure=figs2.brownian_cell(rng.randint(1, 9)))


@template("c7x_brownian_path_length", chapter=7, level=1, lo="7c")
def brownian_path_length(rng):
    steps = [nice(rng, 0.02, 0.03, 0.04, 0.05) for _ in range(5)]
    tot = sum(steps)
    return mk(rng, tot, [(max(steps), "Add ALL the steps along the path."), (tot / len(steps), "That is the average step; the question asks for the total path."), (steps[0] * 5, "Add the actual step lengths.")],
              "mm", f"A smoke particle in a smoke cell is watched through a microscope. The lengths of five straight steps of its path are recorded.\n\n{md_table(['step', 'length / mm'], [[i + 1, fmt(s)] for i, s in enumerate(steps)])}\n\nWhat is the total length of its path?",
              "total path = sum of the step lengths", [" + ".join(fmt(s) for s in steps) + f" = **{fmt(tot)} mm**"],
              ["The path is made of straight steps.", "Add them all.", "Total distance travelled."])


# ================================================================== L2
@template("c7x_state_at_temperature", chapter=7, level=2, lo="7a")
def state_at_temperature(rng):
    subs = rng.sample(SUBSTANCES, 4)
    T = nice(rng, -50, 20, 25, 100)
    target = rng.choice(STATES)
    chosen = [s for s in subs if state_at(T, s[1], s[2]) == target]
    if not chosen:
        target = state_at(T, subs[0][1], subs[0][2])
        chosen = [subs[0]]
    ans = chosen[0][0]
    wrongs = {n: f"At {T} °C it is a {state_at(T, mp, bp)}." for n, mp, bp in subs if n != ans}
    if len(chosen) > 1:
        subs = [s for s in subs if s[0] == ans or state_at(T, s[1], s[2]) != target]
        wrongs = {n: f"At {T} °C it is a {state_at(T, mp, bp)}." for n, mp, bp in subs if n != ans}
        while len(wrongs) < 3:
            extra = next(s for s in SUBSTANCES if s[0] not in wrongs and s[0] != ans and state_at(T, s[1], s[2]) != target)
            wrongs[extra[0]] = f"At {T} °C it is a {state_at(T, extra[1], extra[2])}."
            subs.append(extra)
    table = md_table(["substance", "melting point / °C", "boiling point / °C"], [[n, mp, bp] for n, mp, bp in subs])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"{table}\n\nWhich substance is a **{target}** at **{T} °C**?",
               "solid below the melting point, liquid between melting and boiling points, gas above the boiling point", [f"{ans}: m.p. {chosen[0][1]} °C, b.p. {chosen[0][2]} °C → **{target}** at {T} °C"],
               ["Compare the temperature with each melting point.", "And with each boiling point.", "Solid < m.p. < liquid < b.p. < gas."])


@template("c7x_compress_percent", chapter=7, level=2, lo="7a")
def compress_percent(rng):
    V1 = nice(rng, 50, 60, 80, 100)
    V2 = V1 * nice(rng, 0.4, 0.5, 0.6, 0.75)
    pct = (V1 - V2) / V1 * 100
    return mk(rng, pct, [(V2 / V1 * 100, "That is the percentage REMAINING; find the decrease."), (V1 - V2, "That is the change in cm³; express it as a percentage."), ((V1 - V2) / V2 * 100, "Divide by the ORIGINAL volume.")],
              "%", f"A sealed syringe of air is compressed.\n\n{md_table(['', 'volume / cm³'], [['before', V1], ['after', fmt(V2)]])}\n\nBy what percentage has the volume decreased? (A syringe of water would hardly change.)",
              "% decrease = (V₁ − V₂) ÷ V₁ × 100%", [f"decrease = {V1} − {fmt(V2)} = {fmt(V1 - V2)} cm³", f"% = {fmt(V1 - V2)} ÷ {V1} × 100% = **{fmt(pct)}%**"],
              ["Find the decrease in volume.", "Divide by the original volume.", "× 100%."])


@template("c7x_properties_table", chapter=7, level=2, lo="7b")
def properties_table(rng):
    rows = [("fixed", "fixed", "solid"), ("not fixed", "fixed", "liquid"), ("not fixed", "not fixed", "gas")]
    shape, vol, ans = rng.choice(rows)
    wrongs = {s: f"A {s} has shape {dict((r[2], r[0]) for r in rows)[s]} and volume {dict((r[2], r[1]) for r in rows)[s]}." for s in STATES if s != ans}
    wrongs["any of the three states"] = "Each state has a different combination."
    table = md_table(["property of sample", "observation"], [["shape", shape], ["volume", vol]])
    return mkt(rng, ans, wrongs, f"A sample is tested at constant temperature.\n\n{table}\n\nWhich state is it, and so how are its particles arranged?",
               "solid: fixed shape and volume; liquid: fixed volume only; gas: neither", [f"shape {shape}, volume {vol} → **{ans}**"],
               ["Which state keeps its shape?", "Which keeps its volume but not its shape?", "Match the table."])


@template("c7x_density_states", chapter=7, level=2, lo="7b")
def density_states(rng):
    rho_l = nice(rng, 1000, 800, 1260)
    ratio = nice(rng, 800, 1000, 1200, 1600)
    rho_g = rho_l / ratio
    return mk(rng, ratio, [(rho_g, "That is the density of the vapour; find how many times smaller it is."), (math.cbrt(ratio), "That is the ratio of particle SPACINGS; the question asks about volumes."), (ratio / 1000, "Divide the two densities.")],
              "times", f"A liquid boils to form a vapour.\n\n{md_table(['state', 'density / kg/m³'], [['liquid', rho_l], ['vapour', fmt(rho_g)]])}\n\nThe same mass of particles takes up how many times more volume as a vapour?",
              "same mass: V ∝ 1/ρ → V_gas ÷ V_liquid = ρ_liquid ÷ ρ_gas", [f"ratio = {rho_l} ÷ {fmt(rho_g)} = **{fmt(ratio)}**"],
              ["The mass is the same.", "Volume = mass ÷ density.", "Ratio of densities."])


@template("c7x_magnified_brownian", chapter=7, level=2, lo="7c")
def magnified_brownian(rng):
    mag = nice(rng, 100, 200, 400, 500)
    img = nice(rng, 8, 10, 12, 20)
    actual = img / mag * 1000
    return mk(rng, actual, [(img * mag, "Divide by the magnification."), (img / mag, "That is in mm; the answer is in µm."), (img, "That is the size on the image.")],
              "µm", f"A smoke particle is watched through a microscope.\n\n{md_table(['quantity', 'value'], [['magnification', f'× {mag}'], ['distance moved on the magnified image', f'{img} mm']])}\n\nHow far did the particle actually move, in micrometres (1 mm = 1000 µm)?",
              "actual = image ÷ magnification", [f"actual = {img} ÷ {mag} = {fmt(img / mag)} mm", f"= **{fmt(actual)} µm**"],
              ["The image is enlarged.", "Divide by the magnification.", "Convert mm to µm."])


@template("c7x_brownian_speed", chapter=7, level=2, lo="7c")
def brownian_speed(rng):
    d = nice(rng, 0.12, 0.15, 0.2, 0.24)
    t = nice(rng, 3, 4, 5, 6)
    return mk(rng, d / t, [(d * t, "Speed = distance ÷ time."), (t / d, "Distance goes on top."), (d, "Divide by the time.")],
              "mm/s", f"A smoke particle travels along a zig-zag path in a smoke cell.\n\n{md_table(['quantity', 'value'], [['total path length', f'{fmt(d)} mm'], ['time', f'{t} s']])}\n\nWhat is its average speed?",
              "average speed = total distance ÷ time", [f"= {fmt(d)} ÷ {t} = **{fmt(d / t)} mm/s**"],
              ["Average speed = distance ÷ time.", "Use the total path length.", "Divide."])


@template("c7x_speed_temperature_table", chapter=7, level=2, lo="7d")
def speed_temperature_table(rng):
    temps = [0, 50, 100, 150]
    v0 = nice(rng, 460, 480, 500)
    speeds = [round(v0 * math.sqrt((t + 273) / 273)) for t in temps]
    k = rng.randrange(1, 4)
    hidden = speeds[k]
    return mk(rng, hidden, [(speeds[k - 1], "The speed INCREASES with temperature; pick the next value."), (v0, "That is the speed at 0 °C."), (speeds[k] * 2, "The speed does not double; it rises gradually.")],
              "m/s", f"The table gives the average speed of oxygen molecules at different temperatures; one value is missing.\n\n{md_table(['temperature / °C', 'average speed / m/s'], [[t, (s if i != k else '?')] for i, (t, s) in enumerate(zip(temps, speeds))])}\n\nWhich value best fits the missing entry?",
              "higher temperature → faster particles (speed rises steadily)", [f"the pattern rises smoothly → **{hidden} m/s**"],
              ["How does speed change with temperature?", "It increases smoothly.", "Pick the value between its neighbours."], dp=0)


@template("c7x_ke_molecule", chapter=7, level=2, lo="7d")
def ke_molecule(rng):
    m = nice(rng, 4.8e-26, 5.3e-26, 6.6e-27)
    v = nice(rng, 400, 450, 500, 1200)
    KE = 0.5 * m * v * v
    return mk(rng, KE, [(m * v * v, "Include the ½."), (0.5 * m * v, "Square the speed."), (KE * 1000, "Check the powers of ten.")],
              "J", f"A gas molecule moves at the average speed for its temperature.\n\n{md_table(['quantity', 'value'], [['mass of molecule', f'{sci(m)} kg'], ['speed', f'{v} m/s']])}\n\nWhat is its kinetic energy?",
              "KE = ½ m v²", [f"KE = ½ × {sci(m)} × {v}²", f"= **{sci(KE)} J**"],
              ["Use KE = ½ m v².", "Square the speed first.", "Keep the powers of ten."])


@template("c7x_boyle_double_pressure", chapter=7, level=2, lo="7e")
def boyle_double_pressure(rng):
    V1 = nice(rng, 60, 90, 120, 150)
    k = nice(rng, 2, 3, 4)
    V2 = V1 / k
    return mk(rng, V2, [(V1 * k, "Increasing the pressure DECREASES the volume."), (V1, "The volume changes."), (V1 / (k * k), "pV is constant: p × k → V ÷ k.")],
              "cm³", f"The pressure on a fixed mass of gas is increased at constant temperature.\n\n{md_table(['', 'pressure', 'volume / cm³'], [['before', 'p', V1], ['after', f'{k}p', '?']])}\n\nWhat is the new volume?",
              "p₁V₁ = p₂V₂", [f"V₂ = {V1} ÷ {k} = **{fmt(V2)} cm³**"],
              ["Temperature constant → p V constant.", f"The pressure is {k} times larger.", f"The volume is {k} times smaller."])


# ================================================================== L3
@template("c7x_state_change_temp", chapter=7, level=3, lo="7a")
def state_change_temp(rng):
    n, mp, bp = rng.choice(SUBSTANCES)
    T1 = mp - nice(rng, 10, 20)
    T2 = bp + nice(rng, 10, 30)
    wrongs = {"solid → liquid only": "It is heated above its boiling point too.", "liquid → gas only": f"It starts below its melting point ({mp} °C), so it is solid at first.",
              "gas → liquid → solid": "Heating takes it the other way."}
    table = md_table(["", "value / °C"], [["melting point", mp], ["boiling point", bp], ["start temperature", T1], ["end temperature", T2]])
    return mkt(rng, "solid → liquid → gas", wrongs, f"A sample of {n} is heated steadily.\n\n{table}\n\nWhich changes of state happen?",
               "compare start and end temperatures with m.p. and b.p.", [f"starts at {T1} °C (< {mp}: solid), ends at {T2} °C (> {bp}: gas) → **solid → liquid → gas**"],
               ["What is the state at the start?", "What is the state at the end?", "List the states in between."])


@template("c7x_antifreeze_choice", chapter=7, level=3, lo="7a")
def antifreeze_choice(rng):
    lo_T = nice(rng, -40, -30, -50)
    hi_T = nice(rng, 40, 50, 60)
    cands = [("A", lo_T + 10, hi_T + 60), ("B", lo_T - 20, hi_T + 30), ("C", lo_T - 30, hi_T - 15), ("D", lo_T + 25, hi_T + 100)]
    rng.shuffle(cands)
    ans = next(n for n, mp, bp in cands if mp < lo_T and bp > hi_T)
    wrongs = {n: (f"It freezes at {mp} °C, above {lo_T} °C." if mp >= lo_T else f"It boils at {bp} °C, below {hi_T} °C.") for n, mp, bp in cands if n != ans}
    table = md_table(["substance", "melting point / °C", "boiling point / °C"], [[n, mp, bp] for n, mp, bp in cands])
    return mkt(rng, ans, wrongs, f"An anti-freeze for aircraft wings must stay LIQUID from **{lo_T} °C** to **{hi_T} °C**.\n\n{table}\n\nWhich substance is suitable?",
               "liquid range: melting point < lowest temperature and boiling point > highest temperature", [f"**{ans}** melts below {lo_T} °C and boils above {hi_T} °C"],
               ["A liquid lies between its m.p. and b.p.", "The m.p. must be below the lowest temperature.", "The b.p. must be above the highest."])


@template("c7x_spacing_ratio", chapter=7, level=3, lo="7b")
def spacing_ratio(rng):
    ratio = nice(rng, 1000, 1331, 1728, 2197)
    s = round(ratio ** (1 / 3))
    return mk(rng, s, [(ratio, "That is the VOLUME ratio; spacing is a length, so take the cube root."), (math.sqrt(ratio), "Volume scales with spacing CUBED: take the cube root."), (ratio / 3, "Take the cube root, not divide by 3.")],
              "times", f"When a liquid boils, the same particles take up more volume.\n\n{md_table(['quantity', 'value'], [['volume of vapour ÷ volume of liquid', ratio]])}\n\nAbout how many times further apart are the particles in the vapour?",
              "volume ∝ (spacing)³ → spacing ratio = ∛(volume ratio)", [f"∛{ratio} = **{s}**"],
              ["Each particle takes up a little cube of space.", "Volume of a cube = side³.", "Take the cube root."], dp=0)


@template("c7x_brownian_smaller_faster", chapter=7, level=3, lo="7c")
def brownian_smaller_faster(rng):
    rows = [("P", 0.5), ("Q", 1.0), ("R", 2.0), ("S", 4.0)]
    rng.shuffle(rows)
    ans = min(rows, key=lambda r: r[1])[0]
    wrongs = {n: ("Larger specks are hit by more molecules at once, so the pushes cancel more and the motion is smaller." if d > 0.5 else "") for n, d in rows if n != ans}
    table = md_table(["speck", "diameter / µm"], [[n, fmt(d)] for n, d in rows])
    return mkt(rng, ans, wrongs, f"Specks of different sizes are suspended in water and watched through a microscope (as in Fig. 1).\n\n{table}\n\nWhich speck shows the most vigorous Brownian motion?",
               "smaller specks: fewer, less balanced collisions and smaller mass → more vigorous motion", [f"smallest speck **{ans}** jiggles most"],
               ["What causes the jiggling?", "Uneven bombardment by molecules.", "Smaller specks are pushed about more."], figure=figs2.brownian_cell(rng.randint(1, 9)))


@template("c7x_brownian_temperature", chapter=7, level=3, lo="7c")
def brownian_temperature(rng):
    T1, T2 = rng.choice([(20, 60), (15, 45), (10, 50)])
    wrongs = {"it becomes less vigorous": "Warmer air molecules move FASTER and hit harder.", "it stops": "The molecules move faster, not slower.",
              "it is unchanged": "The molecules' speed depends on temperature."}
    table = md_table(["", "temperature of air in smoke cell / °C"], [["first observation", T1], ["second observation", T2]])
    return mkt(rng, "it becomes more vigorous", wrongs, f"A smoke cell is observed twice.\n\n{table}\n\nHow does the Brownian motion of the smoke particles change?",
               "higher temperature → faster air molecules → harder, more frequent collisions", ["air molecules move faster at the higher temperature → **more vigorous** motion"],
               ["What causes the motion?", "How does temperature affect the air molecules?", "Faster molecules → more vigorous jiggling."])


@template("c7x_ke_ratio_speed", chapter=7, level=3, lo="7d")
def ke_ratio_speed(rng):
    v1 = nice(rng, 400, 450, 500)
    k = nice(rng, 1.1, 1.2, 1.5)
    v2 = v1 * k
    ratio = k * k
    return mk(rng, ratio, [(k, "KE ∝ v²; square the speed ratio."), (v2 - v1, "That is the speed change, not the KE ratio."), (2 * k, "Square the ratio.")],
              "times", f"Heating a gas raises the average speed of its molecules.\n\n{md_table(['', 'average speed / m/s'], [['before', v1], ['after', fmt(v2)]])}\n\nBy what factor has the average kinetic energy of the molecules increased?",
              "KE ∝ v² → factor = (v₂ ÷ v₁)²", [f"v₂ ÷ v₁ = {fmt(k)}", f"factor = {fmt(k)}² = **{fmt(ratio)}**"],
              ["KE = ½ m v².", "The mass is unchanged.", "Square the speed ratio."])


@template("c7x_ke_temperature_compare", chapter=7, level=3, lo="7d")
def ke_temperature_compare(rng):
    names = ["iron block at 80 °C", "water at 30 °C", "air at 50 °C", "ice at −5 °C"]
    temps = [80, 30, 50, -5]
    idx = list(range(4))
    rng.shuffle(idx)
    ans_i = min(range(4), key=lambda i: temps[i])
    wrongs = {names[i]: ("Being a solid does not by itself mean low particle energy: compare temperatures." if "iron" in names[i] else "Compare the temperatures; the lowest temperature has the lowest average KE.") for i in range(4) if i != ans_i}
    table = md_table(["sample", "temperature / °C"], [[names[i], temps[i]] for i in idx])
    return mkt(rng, names[ans_i], wrongs, f"{table}\n\nIn which sample do the particles have the LOWEST average kinetic energy?",
               "average particle KE depends on temperature, not on state or material", [f"lowest temperature → **{names[ans_i]}**"],
               ["What decides average particle KE?", "Temperature.", "Pick the coldest."])


@template("c7x_boyle_find_volume", chapter=7, level=3, lo="7e")
def boyle_find_volume(rng):
    p1 = nice(rng, 100, 120, 150)
    V1 = nice(rng, 2.0, 3.0, 4.0, 6.0)
    p2 = nice(rng, 200, 250, 300, 400)
    V2 = p1 * V1 / p2
    return mk(rng, V2, [(p2 * V1 / p1, "Higher pressure → SMALLER volume: V₂ = p₁V₁ ÷ p₂."), (V1 * (p2 - p1) / p1, "Use p₁V₁ = p₂V₂."), (V1, "The volume changes.")],
              "m³", f"A weather balloon's gas is compressed at constant temperature.\n\n{md_table(['', 'pressure / kPa', 'volume / m³'], [['before', p1, fmt(V1)], ['after', p2, '?']])}\n\nWhat is the new volume?",
              "p₁V₁ = p₂V₂", [f"V₂ = {p1} × {fmt(V1)} ÷ {p2} = **{fmt(V2)} m³**"],
              ["Is the temperature constant?", "p₁V₁ = p₂V₂.", "Solve for V₂."])


@template("c7x_gas_piston_heated", chapter=7, level=3, lo="7b")
def gas_piston_heated(rng):
    V1 = nice(rng, 100, 150, 200)
    T1, T2 = rng.choice([(20, 80), (27, 127), (0, 60)])
    wrongs = {"its volume decreases": "Faster particles push the piston out.", "its pressure doubles and volume is unchanged": "A frictionless piston moves; the pressure stays equal to the outside pressure.",
              "its particles expand": "The particles themselves do not get bigger; they move faster and further apart."}
    table = md_table(["", "temperature / °C", "volume / cm³"], [["start", T1, V1], ["end", T2, "?"]])
    return mkt(rng, "its volume increases as the particles move faster and spread further apart", wrongs,
               f"A gas is trapped by a frictionless piston and is heated.\n\n{table}\n\nWhich statement is correct?",
               "at constant pressure, a hotter gas expands", ["faster particles push the piston out until the pressure balances → **volume increases**"],
               ["What happens to the particles' speed?", "The piston can move freely.", "The gas expands."])


# ================================================================== L4
@template("c7x_gold_solidifies", chapter=7, level=4, lo="7a")
def gold_solidifies(rng):
    metal, T = rng.choice([("gold", 1064), ("silver", 962), ("copper", 1085), ("aluminium", 660), ("lead", 327)])
    up, down = nice(rng, 20, 26, 30), nice(rng, 18, 24, 28)
    wrongs = {"the temperature falls steadily while it solidifies": "During a change of state the temperature stays constant.",
              "the particles stop moving": "Particles in a solid still vibrate.",
              "the particles move further apart": "Solidifying brings the particles into a fixed, closely packed arrangement."}
    table = md_table(["time / min", "0", "1", "2", "3", "4"], [["temperature / °C", T + up, T, T, T, T - down]])
    return mkt(rng, "the temperature stays constant while the particles take up fixed positions", wrongs,
               f"Molten {metal} is poured into a mould and cools.\n\n{table}\n\nWhich statement describes the {metal} from 1 to 3 minutes?",
               "change of state at constant temperature; particles become fixed in a lattice", [f"the temperature stays at {T} °C (the melting point) → **constant temperature while the particles take up fixed positions**"],
               ["Which part of the table is constant?", "That is a change of state.", "Liquid → solid."])


@template("c7x_ice_sublimes_mass", chapter=7, level=4, lo="7a")
def ice_sublimes_mass(rng):
    m1 = nice(rng, 25, 30, 40)
    m2 = m1 - nice(rng, 2, 3, 4, 5)
    days = nice(rng, 5, 10, 14)
    rate = (m1 - m2) / days
    return mk(rng, rate, [(m1 - m2, "Divide the mass lost by the number of days."), (m2 / days, "Use the mass LOST."), ((m1 - m2) * days, "Divide by the time.")],
              "g per day", f"Ice cubes left in a freezer slowly lose mass because some ice changes directly to water vapour.\n\n{md_table(['', 'mass / g'], [['day 0', m1], [f'day {days}', m2]])}\n\nWhat is the average rate of loss of mass?",
              "rate = mass lost ÷ time", [f"mass lost = {m1} − {m2} = {m1 - m2} g", f"rate = {m1 - m2} ÷ {days} = **{fmt(rate)} g per day**"],
              ["Find the mass lost.", "Divide by the number of days.", "Units: g per day."])


@template("c7x_particles_in_volume", chapter=7, level=4, lo="7b")
def particles_in_volume(rng):
    n_l = nice(rng, 3.3e28, 3.0e28)
    ratio = nice(rng, 1000, 1250, 1700)
    n_g = n_l / ratio
    return mk(rng, n_g, [(n_l * ratio, "The vapour is LESS dense: fewer particles per m³."), (n_l / math.cbrt(ratio), "Divide by the volume ratio, not its cube root."), (n_l, "The number per m³ changes.")],
              "per m³", f"When water boils, its volume increases greatly.\n\n{md_table(['quantity', 'value'], [['particles per m³ in liquid water', sci(n_l)], ['volume of steam ÷ volume of the same mass of water', ratio]])}\n\nHow many particles are there in each m³ of steam?",
              "same particles spread through ratio × the volume → number per m³ ÷ ratio", [f"n = {sci(n_l)} ÷ {ratio} = **{sci(n_g)} per m³**"],
              ["The number of particles is unchanged.", "They fill a larger volume.", "Divide by the volume ratio."])


@template("c7x_expansion_rod", chapter=7, level=4, lo="7b")
def expansion_rod(rng):
    L = nice(rng, 1.0, 2.0, 5.0)
    dT = nice(rng, 50, 80, 100)
    a = nice(rng, 1.2e-5, 1.7e-5, 2.3e-5)
    dL = L * a * dT * 1000
    return mk(rng, dL, [(L * a * dT, "That is in metres; the answer is in mm."), (a * dT * 1000, "Multiply by the original length too."), (dL * 10, "Check the conversion to mm.")],
              "mm", f"A metal rod expands when heated because its particles vibrate more and move slightly further apart.\n\n{md_table(['quantity', 'value'], [['original length', f'{fmt(L)} m'], ['temperature rise', f'{dT} °C'], ['increase in length per metre per °C', f'{sci(a)} m'], ])}\n\nBy how many mm does the rod lengthen?",
              "ΔL = L × (increase per m per °C) × ΔT", [f"ΔL = {fmt(L)} × {sci(a)} × {dT} = {sci(L * a * dT)} m", f"= **{fmt(dL)} mm**"],
              ["Multiply the three quantities.", "That gives metres.", "× 1000 for mm."])


@template("c7x_brownian_displacement_grid", chapter=7, level=4, lo="7c")
def brownian_displacement_grid(rng):
    e = nice(rng, 3, 4, 6, 8)
    n = nice(rng, 4, 3, 6, 8)
    disp = math.hypot(e, n)
    path = e + n + nice(rng, 6, 8, 10)
    return mk(rng, disp, [(path, "That is the PATH length; displacement is the straight-line distance from start to end."), (e + n, "Use Pythagoras for the straight-line distance."), (abs(e - n), "Use √(east² + north²).")],
              "µm", f"A pollen grain's start and end positions are recorded through a microscope.\n\n{md_table(['quantity', 'value'], [['total path length', f'{path} µm'], ['net movement east', f'{e} µm'], ['net movement north', f'{n} µm']])}\n\nWhat is the size of its displacement?",
              "displacement = √(east² + north²)", [f"√({e}² + {n}²) = **{fmt(disp)} µm**"],
              ["Displacement is the straight line from start to finish.", "The two components are at right angles.", "Use Pythagoras."])


@template("c7x_brownian_mass_speed", chapter=7, level=4, lo="7c")
def brownian_mass_speed(rng):
    m_air = 4.8e-26
    v_air = nice(rng, 400, 480, 500)
    m_smoke = nice(rng, 1e-17, 2e-17, 5e-17)
    v = v_air * math.sqrt(m_air / m_smoke)
    return mk(rng, v, [(v_air, "The heavy smoke particle has the same average KE but moves much more slowly."), (v_air * m_air / m_smoke, "Equal KE: v ∝ 1/√m, so take the square root of the mass ratio."), (v * 1000, "Check the powers of ten.")],
              "m/s", f"In a smoke cell, a smoke particle ends up with the same average kinetic energy as an air molecule.\n\n{md_table(['particle', 'mass / kg', 'average speed / m/s'], [['air molecule', sci(m_air), v_air], ['smoke particle', sci(m_smoke), '?']])}\n\nWhat is the average speed of the smoke particle?",
              "½ m₁ v₁² = ½ m₂ v₂² → v₂ = v₁ √(m₁ ÷ m₂)", [f"v₂ = {v_air} × √({sci(m_air)} ÷ {sci(m_smoke)})", f"= **{fmt(v, sf=2)} m/s**"],
              ["Set the kinetic energies equal.", "Rearrange for the smoke particle's speed.", "Take the square root of the mass ratio."], sf=2)


@template("c7x_ke_total_gas", chapter=7, level=4, lo="7d")
def ke_total_gas(rng):
    N = nice(rng, 2.4e22, 3.0e22, 6.0e22)
    ke = nice(rng, 6.0e-21, 6.2e-21, 8.0e-21)
    E = N * ke
    return mk(rng, E, [(ke, "Multiply by the number of molecules."), (N, "Multiply by the KE of each molecule."), (E / 1000, "Check the powers of ten.")],
              "J", f"A sample of gas is at room temperature.\n\n{md_table(['quantity', 'value'], [['number of molecules', sci(N)], ['average kinetic energy of one molecule', f'{sci(ke)} J']])}\n\nWhat is the total kinetic energy of the molecules?",
              "total KE = number × average KE", [f"= {sci(N)} × {sci(ke)} = **{fmt(E)} J**"],
              ["Each molecule has, on average, this KE.", "Multiply by the number of molecules.", "Watch the powers of ten."])


@template("c7x_ke_mix_temperatures", chapter=7, level=4, lo="7d")
def ke_mix_temperatures(rng):
    m1, T1 = nice(rng, 100, 200), nice(rng, 20, 30)
    m2, T2 = nice(rng, 100, 300), nice(rng, 60, 80)
    Tf = (m1 * T1 + m2 * T2) / (m1 + m2)
    return mk(rng, Tf, [((T1 + T2) / 2, "The masses differ: weight each temperature by its mass."), (T2, "Energy spreads until both reach the same temperature."), (T1 + T2, "The final temperature lies BETWEEN the two.")],
              "°C", f"Two samples of water are mixed in an insulated flask. Particles collide until their average kinetic energies are equal.\n\n{md_table(['sample', 'mass / g', 'temperature / °C'], [['cold', m1, T1], ['hot', m2, T2]])}\n\nWhat is the final temperature? (No energy is lost.)",
              "same substance: T_f = (m₁T₁ + m₂T₂) ÷ (m₁ + m₂)", [f"T_f = ({m1}×{T1} + {m2}×{T2}) ÷ {m1 + m2}", f"= **{fmt(Tf)} °C**"],
              ["Energy flows from hot to cold.", "The final temperature is the same for both.", "Use a mass-weighted average."])


# ================================================================== L5
@template("c7x_boyle_bubble_rise", chapter=7, level=5, lo="7e")
def boyle_bubble_rise(rng):
    h = nice(rng, 10, 20, 30)
    V1 = nice(rng, 2.0, 3.0, 4.0)
    p_atm = 100
    p1 = p_atm + h * 1000 * 10 / 1000
    V2 = p1 * V1 / p_atm
    return mk(rng, V2, [(V1 * p_atm / p1, "The pressure FALLS as the bubble rises, so its volume increases."), (V1, "The pressure changes, so the volume changes."), (p1 * V1 / (h * 10), "At the surface the pressure is atmospheric only.")],
              "cm³", f"An air bubble rises from the bottom of a lake to the surface at constant temperature.\n\n{md_table(['quantity', 'value'], [['depth of lake', f'{h} m'], ['volume at the bottom', f'{fmt(V1)} cm³'], ['atmospheric pressure', '100 kPa'], ['water adds', '10 kPa per metre of depth']])}\n\nWhat is its volume at the surface?",
              "p at bottom = 100 + 10 h kPa; p₁V₁ = p₂V₂", [f"p₁ = 100 + 10 × {h} = {fmt(p1)} kPa", f"V₂ = {fmt(p1)} × {fmt(V1)} ÷ 100 = **{fmt(V2)} cm³**"],
              ["Find the total pressure at the bottom.", "At the surface it is 100 kPa.", "Use p₁V₁ = p₂V₂."])


@template("c7x_density_phase_compare", chapter=7, level=5, lo="7a")
def density_phase_compare(rng):
    m = nice(rng, 9.0, 18.0, 27.0)
    Vs = m / 0.92
    Vl = m / 1.00
    pct = (Vs - Vl) / Vl * 100
    return mk(rng, pct, [((Vs - Vl) / Vs * 100, "Divide by the volume of the WATER (the starting volume)."), (Vs - Vl, "That is the change in cm³; give a percentage."), (8.0, "Calculate from the densities.")],
              "%", f"Water is unusual: it expands when it freezes.\n\n{md_table(['state', 'density / g/cm³'], [['liquid water', '1.00'], ['ice', '0.92']])}\n\nA mass of **{fmt(m)} g** of water freezes. By what percentage does its volume increase?",
              "V = m ÷ ρ for each state; % = (V_ice − V_water) ÷ V_water × 100%", [f"V_water = {fmt(Vl)} cm³; V_ice = {fmt(m)} ÷ 0.92 = {fmt(Vs)} cm³", f"% increase = **{fmt(pct, sf=2)}%**"],
              ["Find the volume in each state.", "V = m ÷ ρ.", "Percentage change from the water's volume."], sf=2)


@template("c7x_state_from_heating_table", chapter=7, level=5, lo="7a")
def state_from_heating_table(rng):
    mp = nice(rng, 40, 45, 55, 60)
    bp = mp + nice(rng, 60, 80)
    temps = [mp - 30, mp - 10, mp, mp, mp + 30, bp, bp]
    tmin = rng.choice([2, 3, 5])
    ans = {2: "solid and liquid together", 3: "solid and liquid together", 5: "liquid and gas together"}[tmin]
    wrongs = {o: "Find where the temperature is constant and compare it with the melting and boiling points." for o in ["solid only", "liquid only", "gas only", "solid and liquid together", "liquid and gas together"] if o != ans}
    table = md_table(["time / min"] + [str(i) for i in range(7)], [["temperature / °C"] + [str(t) for t in temps]])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"A solid substance is heated steadily and its temperature is recorded every minute.\n\n{table}\n\nWhat is the state of the substance at **{tmin} min**?",
               "a constant temperature shows a change of state: lower plateau = melting, upper plateau = boiling", [f"at {tmin} min the temperature is on the {'first' if tmin < 4 else 'second'} plateau ({temps[tmin]} °C) → **{ans}**"],
               ["Where is the temperature constant?", "The first plateau is melting, the second boiling.", "During a change of state two states coexist."])


@template("c7x_spacing_from_density", chapter=7, level=5, lo="7b")
def spacing_from_density(rng):
    rho_l, rho_g = rng.choice([(1000, 0.6), (790, 1.6), (1000, 0.8)])
    ratio = rho_l / rho_g
    s = ratio ** (1 / 3)
    return mk(rng, s, [(ratio, "That is the VOLUME ratio; take the cube root for spacing."), (math.sqrt(ratio), "Volume scales with spacing CUBED."), (rho_l - rho_g, "Divide the densities, then take the cube root.")],
              "times", f"{md_table(['state', 'density / kg/m³'], [['liquid', rho_l], ['vapour at its boiling point', fmt(rho_g)]])}\n\nUsing these densities, estimate how many times further apart the particles are in the vapour than in the liquid.",
              "spacing ratio = ∛(ρ_liquid ÷ ρ_vapour)", [f"volume ratio = {rho_l} ÷ {fmt(rho_g)} = {fmt(ratio)}", f"spacing ratio = ∛{fmt(ratio)} = **{fmt(s, sf=2)}**"],
              ["Same mass: volume ∝ 1/density.", "Volume ∝ spacing³.", "Cube root of the density ratio."], sf=2)


@template("c7x_gas_spacing_size", chapter=7, level=5, lo="7b")
def gas_spacing_size(rng):
    n = nice(rng, 2.5e25, 3.0e25)
    d_mol = nice(rng, 3e-10, 4e-10)
    s = (1 / n) ** (1 / 3)
    ratio = s / d_mol
    return mk(rng, ratio, [(1 / n / d_mol, "The volume per molecule is 1/n; take its cube root to get the spacing."), (s, "That is the spacing in m; compare it with the molecule's size."), (ratio ** 3, "Take the cube root.")],
              "times", f"Air at room temperature:\n\n{md_table(['quantity', 'value'], [['molecules per m³', sci(n)], ['diameter of a molecule', f'{sci(d_mol)} m']])}\n\nEach molecule has a cube of space of volume 1/n. About how many molecular diameters apart are the molecules?",
              "spacing = ∛(1 ÷ n); ratio = spacing ÷ diameter", [f"spacing = ∛(1 ÷ {sci(n)}) = {sci(s)} m", f"ratio = {sci(s)} ÷ {sci(d_mol)} = **{fmt(ratio, sf=2)}**"],
              ["Find the volume per molecule.", "Its cube root is the spacing.", "Divide by the diameter."], sf=2)


@template("c7x_brownian_rms_time", chapter=7, level=5, lo="7c")
def brownian_rms_time(rng):
    d1 = nice(rng, 2.0, 3.0, 4.0)
    t1 = nice(rng, 10, 20)
    k = nice(rng, 4, 9, 16)
    d2 = d1 * math.sqrt(k)
    return mk(rng, d2, [(d1 * k, "Random-walk displacement grows with √time, not time."), (d1, "The particle wanders further given more time."), (d1 * k / 2, "Use √(time ratio).")],
              "µm", f"For a speck in Brownian motion, the typical distance from its start grows with the square root of the time.\n\n{md_table(['time / s', 'typical distance from start / µm'], [[t1, fmt(d1)], [t1 * k, '?']])}\n\nWhat is the typical distance after the longer time?",
              "distance ∝ √t → d₂ = d₁ √(t₂ ÷ t₁)", [f"√({t1 * k} ÷ {t1}) = √{k} = {fmt(math.sqrt(k))}", f"d₂ = {fmt(d1)} × {fmt(math.sqrt(k))} = **{fmt(d2)} µm**"],
              ["The path is random, so it does not move steadily away.", "Distance ∝ √time.", "Multiply by √(time ratio)."])


@template("c7x_ke_heavier_gas", chapter=7, level=5, lo="7d")
def ke_heavier_gas(rng):
    v_h = nice(rng, 1800, 1900, 2000)
    k = 16
    v_o = v_h / math.sqrt(k)
    return mk(rng, v_o, [(v_h / k, "Equal KE: v ∝ 1/√m, so divide by √16 = 4."), (v_h, "The heavier molecules move more slowly at the same temperature."), (v_h * 4, "Heavier molecules are SLOWER.")],
              "m/s", f"Hydrogen and oxygen are at the same temperature, so their molecules have the same average kinetic energy.\n\n{md_table(['gas', 'mass of molecule (relative)', 'average speed / m/s'], [['hydrogen', 1, v_h], ['oxygen', 16, '?']])}\n\nWhat is the average speed of the oxygen molecules?",
              "½ m_H v_H² = ½ m_O v_O² → v_O = v_H ÷ √(m_O ÷ m_H)", [f"v_O = {v_h} ÷ √16 = {v_h} ÷ 4", f"= **{fmt(v_o)} m/s**"],
              ["Same temperature → same average KE.", "KE = ½ m v².", "v ∝ 1/√m."])


@template("c7x_ke_from_temperature_k", chapter=7, level=5, lo="7d")
def ke_from_temperature_k(rng):
    E1 = 6.0e-21
    T1 = 27
    T2 = nice(rng, 127, 227, 327)
    E2 = E1 * (T2 + 273) / (T1 + 273)
    return mk(rng, E2, [(E1 * T2 / T1, "Use the absolute (kelvin) temperature: T(K) = θ(°C) + 273."), (E1, "The average KE increases with temperature."), (E1 * (T2 - T1) / (T1 + 273), "That is only the INCREASE in KE.")],
              "J", f"The average kinetic energy of gas molecules is proportional to the absolute (kelvin) temperature, T = θ + 273.\n\n{md_table(['temperature / °C', 'average KE / J'], [[T1, sci(E1)], [T2, '?']])}\n\nWhat is the average kinetic energy at the higher temperature?",
              "KE ∝ T(K) → KE₂ = KE₁ × T₂ ÷ T₁", [f"T₁ = 300 K, T₂ = {T2 + 273} K", f"KE₂ = {sci(E1)} × {T2 + 273} ÷ 300 = **{sci(E2)} J**"],
              ["Convert both temperatures to kelvin.", "KE is proportional to T in kelvin.", "Scale by T₂ ÷ T₁."])
