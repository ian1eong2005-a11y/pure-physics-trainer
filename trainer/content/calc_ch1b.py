"""Chapter 1 (6091) bank extension: 10 calculation templates per level, each learning outcome at least twice.
Contexts adapted from the question bank (SEAB 2014-2024 and school papers 2024); numbers are generated, never copied."""
import math

from .. import figs, figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, sci, template

PFX = {"n": (1e-9, "nano"), "µ": (1e-6, "micro"), "m": (1e-3, "milli"), "c": (1e-2, "centi"), "k": (1e3, "kilo"), "M": (1e6, "mega"), "G": (1e9, "giga")}


# ================================================================== L1
@template("c1b_si_to_prefix", chapter=1, level=1, lo="1c")
def si_to_prefix(rng):
    sym, (mult, name) = rng.choice([("m", PFX["m"]), ("c", PFX["c"]), ("k", PFX["k"]), ("µ", PFX["µ"])])
    v = nice(rng, 2.4, 3.6, 4.8, 7.5, 12, 15, 25)
    si = v * mult
    unit = "m" if sym != "k" else rng.choice(["m", "g"])
    return mk(rng, v, [(v * 1000 if mult < 1 else v / 1000, f"Wrong power of ten. {name} means × {sci(mult)}, so divide the SI value by {sci(mult)}."),
                       (si * mult, f"You multiplied by the multiplier again. To go from {unit} to {sym}{unit}, DIVIDE by {sci(mult)}."),
                       (v * 10, "One power of ten out: check the prefix multiplier.")],
              f"{sym}{unit}",
              f"A quantity is measured in SI units.\n\n{md_table(['quantity', 'value'], [['reading', f'{sci(si)} {unit}']])}\n\nWhat is this reading in **{sym}{unit}**?",
              f"value in {sym}{unit} = value in {unit} ÷ {sci(mult)}",
              [f"{name} ({sym}) = {sci(mult)}", f"{sci(si)} {unit} ÷ {sci(mult)} = **{fmt(v)} {sym}{unit}**"],
              ["Each prefix stands for a power of ten. Which one is this?", f"1 {sym}{unit} = {sci(mult)} {unit}. How many of those fit into the reading?", f"Divide {sci(si)} by {sci(mult)}."])


@template("c1b_time_prefix", chapter=1, level=1, lo="1c")
def time_prefix(rng):
    sym, (mult, name) = rng.choice([("n", PFX["n"]), ("µ", PFX["µ"]), ("m", PFX["m"])])
    v = nice(rng, 2, 4, 5, 8, 15, 25, 40)
    ans = v * mult
    return mk(rng, ans, [(v * mult * 1000, f"{name} is {sci(mult)}, one power of a thousand smaller than you used."),
                         (v * mult / 1000, f"{name} is {sci(mult)}, one power of a thousand larger than you used."),
                         (v / mult, "You divided by the multiplier instead of multiplying.")],
              "s",
              f"An electronic timer records a time interval.\n\n{md_table(['event', 'time'], [['pulse length', f'{v} {sym}s']])}\n\nWhat is this time in seconds?",
              f"1 {sym}s = {sci(mult)} s", [f"{v} {sym}s = {v} × {sci(mult)} s", f"= **{sci(ans)} s**"],
              ["Replace the prefix by its power of ten.", f"{name} = {sci(mult)}.", f"{v} × {sci(mult)}."], sf=2)


@template("c1b_stopwatch_difference", chapter=1, level=1, lo="1e")
def stopwatch_difference(rng):
    s0 = round(rng.uniform(2, 12), 2)
    d = round(rng.uniform(20, 55), 2)
    s1 = round(s0 + d, 2)
    opts = mk(rng, d, [(s1, "That is the finishing reading. The race time is the DIFFERENCE between the two readings."),
                       (s1 + s0, "You added the readings; subtract the start reading from the finish reading."),
                       (round(d + 1, 2), "Check the subtraction digit by digit.")],
              "s", f"A digital stopwatch is not reset before a race. Fig. 1 shows the reading at the end; at the start it read **{s0:.2f} s**. How long did the race take?",
              "time taken = final reading − initial reading", [f"{s1:.2f} − {s0:.2f} = **{d:.2f} s**"],
              ["The watch already showed a time at the start. What must you do with it?", "Take the start reading away from the finish reading.", f"{s1:.2f} − {s0:.2f}."],
              figure=figs.stopwatch(figs2.stopwatch_text(s1)), dp=2)
    return opts


@template("c1b_half_swing_period", chapter=1, level=1, lo="1e")
def half_swing_period(rng):
    t = nice(rng, 0.4, 0.5, 0.6, 0.75, 0.8, 1.0, 1.2)
    return mk(rng, 2 * t, [(t, "X to Y is only HALF an oscillation. A full oscillation is X → Y → back to X."),
                           (t / 2, "You halved it. The period is longer than one swing from side to side, not shorter."),
                           (4 * t, "X to Y and back is two swings, not four.")],
              "s", f"Fig. 1 shows a pendulum swinging between its end points. It takes **{fmt(t)} s** to swing from one end to the other end. What is its period?",
              "one oscillation = end → other end → back; period = 2 × (time for one swing across)",
              [f"one swing across = half an oscillation = {fmt(t)} s", f"T = 2 × {fmt(t)} = **{fmt(2 * t)} s**"],
              ["What counts as ONE complete oscillation?", "It must return to where it started, moving the same way.", f"Double {fmt(t)} s."],
              figure=sketches.pendulum_sketch(f"end to end: {fmt(t)} s"))


@template("c1b_rule_between_marks", chapter=1, level=1, lo="1e")
def rule_between_marks(rng):
    a = round(rng.uniform(0.5, 4.0), 1)
    L = round(rng.uniform(3.0, 9.5), 1)
    b = round(a + L, 1)
    return mk(rng, L, [(b, "That is the reading at the right-hand end. The object does not start at 0 cm."),
                       (a + b, "Subtract the readings at the two ends; do not add them."),
                       (L + 1, "Check the subtraction.")],
              "cm", f"A pencil is laid against a rule (Fig. 1). Its left end is at **{a:.1f} cm** and its right end is at **{b:.1f} cm**. What is the length of the pencil?",
              "length = reading at one end − reading at the other end", [f"{b:.1f} − {a:.1f} = **{L:.1f} cm**"],
              ["Does the pencil start at the zero mark?", "Read both ends; the length is the difference.", f"{b:.1f} − {a:.1f}."],
              figure=figs2.rule_object(a, b), dp=1)


@template("c1b_stack_count", chapter=1, level=1, lo="1e")
def stack_count(rng):
    n = nice(rng, 20, 25, 40, 50, 100)
    t = nice(rng, 0.10, 0.08, 0.12, 0.05)
    tot = n * t
    return mk(rng, t, [(tot, "That is the thickness of the whole stack, not of one coin."),
                       (tot * n, "You multiplied. Divide the stack thickness by the number of coins."),
                       (n / tot, "Thickness of one = stack ÷ number, not number ÷ stack.")],
              "cm", f"A student cannot measure the thickness of one thin plastic counter accurately, so she measures a stack.\n\n{md_table(['number of counters', 'height of stack / cm'], [[n, fmt(tot)]])}\n\nWhat is the thickness of one counter?",
              "thickness of one = height of stack ÷ number in the stack", [f"{fmt(tot)} ÷ {n} = **{fmt(t)} cm**"],
              ["Why measure a stack instead of one counter?", "The stack contains many identical thicknesses.", f"{fmt(tot)} ÷ {n}."])


@template("c1b_collinear_same", chapter=1, level=1, lo="1g")
def collinear_same(rng):
    a, b = nice(rng, 3, 4, 5, 6, 8), nice(rng, 2, 3, 5, 7, 9)
    return mk(rng, a + b, [(abs(a - b) or 1, "Both forces point the SAME way, so they add."),
                           (math.hypot(a, b), "Pythagoras is only for forces at right angles. These act along the same line."),
                           ((a + b) / 2, "Do not average forces; add them when they point the same way.")],
              "N", f"Fig. 1 shows two students pushing a box in the same direction with forces of **{a} N** and **{b} N**. What is the resultant force on the box?",
              "forces in the same direction: resultant = sum", [f"{a} + {b} = **{a + b} N** in the direction of the pushes"],
              ["Are the forces in the same or opposite directions?", "Same direction: they add.", f"{a} + {b}."],
              figure=figs2.forces_on_line([(f"{a} N", "right", a), (f"{b} N", "right", b)]))


@template("c1b_collinear_opposite", chapter=1, level=1, lo="1g")
def collinear_opposite(rng):
    a = nice(rng, 12, 15, 20, 25, 30)
    b = nice(rng, 4, 5, 8, 9, 10)
    return mk(rng, a - b, [(a + b, "The forces act in OPPOSITE directions, so subtract."),
                           (math.hypot(a, b), "Pythagoras is only for forces at right angles."),
                           (b, "That is just the smaller force.")],
              "N", f"Fig. 1 shows a box pulled to the right with **{a} N** while friction acts to the left with **{b} N**. What is the magnitude of the resultant force?",
              "forces in opposite directions: resultant = larger − smaller, in the direction of the larger", [f"{a} − {b} = **{a - b} N** to the right"],
              ["Which way does each force act?", "Opposite directions: subtract.", f"{a} − {b}."],
              figure=figs2.forces_on_line([(f"{a} N", "right", a), (f"{b} N", "left", b)]))


@template("c1b_three_collinear", chapter=1, level=1, lo="1g")
def three_collinear(rng):
    a, b, c = nice(rng, 10, 12, 15), nice(rng, 6, 8, 9), nice(rng, 3, 4, 5)
    r = a + c - b
    return mk(rng, r, [(a + b + c, "One force acts the OTHER way; it must be subtracted."),
                       (a - b - c if a - b - c > 0 else a + b - c, "Check which forces act to the right and which to the left."),
                       (a, "You must combine all three forces.")],
              "N", f"Three forces act along a straight line on a trolley: **{a} N** to the right, **{c} N** to the right and **{b} N** to the left (Fig. 1). What is the magnitude of the resultant force?",
              "add the forces in one direction, subtract those in the other", [f"right: {a} + {c} = {a + c} N; left: {b} N", f"resultant = {a + c} − {b} = **{r} N** to the right"],
              ["Group the forces by direction.", f"Total to the right = {a + c} N.", f"{a + c} − {b}."],
              figure=figs2.forces_on_line([(f"{a} N", "right", a), (f"{c} N", "right", c), (f"{b} N", "left", b)], body="trolley"))


# ================================================================== L2
@template("c1b_area_cm2_to_m2", chapter=1, level=2, lo="1c")
def area_cm2_to_m2(rng):
    a = nice(rng, 250, 400, 600, 750, 1200, 2500)
    ans = a / 1e4
    return mk(rng, ans, [(a / 100, "1 m² = 100 cm × 100 cm = 10 000 cm², not 100 cm²."),
                         (a / 1e6, "That is the cm³ → m³ factor. For an AREA use 10 000."),
                         (a * 1e4, "Going from cm² to m² the number gets SMALLER.")],
              "m²", f"A block rests on the floor on one of its faces.\n\n{md_table(['face', 'area'], [['contact face', f'{a} cm²']])}\n\nWhat is the area in m²?",
              "1 m² = 10 000 cm²", [f"{a} cm² ÷ 10 000 = **{fmt(ans)} m²**"],
              ["How many cm are in 1 m? An area uses that factor twice.", "100 × 100 = 10 000 cm² in 1 m².", f"{a} ÷ 10 000."])


@template("c1b_volume_cm3_to_m3", chapter=1, level=2, lo="1c")
def volume_cm3_to_m3(rng):
    v = nice(rng, 200, 250, 500, 750, 1500, 2400)
    ans = v / 1e6
    return mk(rng, ans, [(v / 100, "For a volume the factor is 100 × 100 × 100 = 1 000 000."),
                         (v / 1e4, "10 000 is the area factor. A volume needs 1 000 000."),
                         (v / 1e3, "1000 cm³ is a litre, not a cubic metre.")],
              "m³", f"A container holds some water.\n\n{md_table(['quantity', 'value'], [['volume of water', f'{v} cm³']])}\n\nWhat is the volume in m³?",
              "1 m³ = 1 000 000 cm³", [f"{v} ÷ 1 000 000 = **{sci(ans)} m³**"],
              ["A volume has three length dimensions.", "1 m³ = (100 cm)³.", f"{v} ÷ 1 000 000."], sf=3)


@template("c1b_kmh_to_ms", chapter=1, level=2, lo="1c")
def kmh_to_ms(rng):
    v = nice(rng, 36, 54, 72, 90, 108, 18)
    ans = v / 3.6
    return mk(rng, ans, [(v * 3.6, "You multiplied by 3.6. km/h → m/s is ÷ 3.6 (× 1000 m, ÷ 3600 s)."),
                         (v * 1000 / 60, "There are 3600 s in an hour, not 60."),
                         (v / 1000, "You converted km to m the wrong way.")],
              "m/s", f"A car's speedometer reads **{v} km/h** (Fig. 1). What is this speed in m/s?",
              "1 km/h = 1000 m ÷ 3600 s", [f"{v} × 1000 ÷ 3600 = **{fmt(ans)} m/s**"],
              ["Change km to m and hours to seconds.", "× 1000 for km → m, ÷ 3600 for h → s.", f"{v} × 1000 ÷ 3600."],
              figure=figs2.digital_display(f"{v}", "km/h", "speedometer"))


@template("c1b_atoms_across", chapter=1, level=2, lo="1d")
def atoms_across(rng):
    L_mm = nice(rng, 1.0, 0.5, 2.0, 0.1)
    d = 1e-10
    n = L_mm * 1e-3 / d
    return mk(rng, n, [(L_mm * 1e-2 / d, "You used 1 mm = 10⁻² m. 1 mm = 10⁻³ m."),
                       (L_mm / d, "Change mm into m before dividing by the atom's diameter in m."),
                       (n / 1000, "Check the powers of ten.")],
              "", f"Atoms have a diameter of about **10⁻¹⁰ m**.\n\n{md_table(['object', 'size'], [['line drawn with a pen', f'{fmt(L_mm)} mm long'], ['typical atom', '1 × 10⁻¹⁰ m across']])}\n\nAbout how many atoms placed side by side would stretch along the line?",
              "number = length ÷ diameter of one atom (both in m)", [f"{fmt(L_mm)} mm = {sci(L_mm * 1e-3)} m", f"{sci(L_mm * 1e-3)} ÷ 10⁻¹⁰ = **{sci(n)}**"],
              ["Put both lengths in metres.", "Divide the length by one atom's width.", "Subtract the powers of ten."], sf=2)


@template("c1b_hairs_per_cm", chapter=1, level=2, lo="1d")
def hairs_per_cm(rng):
    w_um = nice(rng, 50, 80, 100, 40)
    L_cm = nice(rng, 1, 2, 5)
    n = L_cm * 1e-2 / (w_um * 1e-6)
    return mk(rng, n, [(L_cm * 1e-2 / (w_um * 1e-3), "µm is 10⁻⁶ m, not 10⁻³ m."),
                       (L_cm / w_um, "Convert both lengths to metres first."),
                       (n * 10, "Check the powers of ten.")],
              "", f"A human hair is about **{w_um} µm** thick.\n\n{md_table(['quantity', 'value'], [['width of one hair', f'{w_um} µm'], ['length to fill', f'{L_cm} cm']])}\n\nHow many hairs laid side by side would fill this length?",
              "number = length ÷ width of one hair (same units)", [f"{L_cm} cm = {sci(L_cm * 1e-2)} m; {w_um} µm = {sci(w_um * 1e-6)} m", f"n = **{fmt(n)}**"],
              ["Use the same unit for both lengths.", "1 µm = 10⁻⁶ m; 1 cm = 10⁻² m.", "Divide."])


@template("c1b_missing_force", chapter=1, level=2, lo="1g")
def missing_force(rng):
    R = nice(rng, 5, 6, 8, 10, 12)
    F2 = nice(rng, 3, 4, 7, 9)
    F1 = R + F2
    return mk(rng, F1, [(R - F2 if R > F2 else R + 2 * F2, "The unknown force must OVERCOME the opposing force AND leave the resultant."),
                        (R, "That is the resultant. The pull must be bigger, because friction acts against it."),
                        (F2, "That is the friction force.")],
              "N", f"A sledge is pulled to the right. Friction of **{F2} N** acts to the left and the resultant force is **{R} N** to the right (Fig. 1). What is the size of the pull?",
              "resultant = pull − friction → pull = resultant + friction", [f"pull = {R} + {F2} = **{F1} N**"],
              ["Write the resultant in terms of the two forces.", "R = P − F.", f"P = {R} + {F2}."],
              figure=figs2.forces_on_line([("pull = ?", "right", R + F2), (f"{F2} N", "left", F2)], body="sledge"))


@template("c1b_net_displacement_line", chapter=1, level=2, lo="1g")
def net_displacement_line(rng):
    a, b = nice(rng, 80, 120, 150, 200), nice(rng, 30, 40, 50, 60)
    return mk(rng, a - b, [(a + b, "That is the DISTANCE walked. Displacement takes direction into account."),
                           (b, "That is the second leg only."),
                           ((a + b) / 2, "Do not average; combine the two legs with their directions.")],
              "m", f"A runner jogs **{a} m east** and then turns back and jogs **{b} m west** (Fig. 1). What is the magnitude of the runner's displacement from the start?",
              "displacement along a line = east legs − west legs", [f"{a} − {b} = **{a - b} m** east of the start"],
              ["Displacement is a vector: direction matters.", "The west leg cancels part of the east leg.", f"{a} − {b}."],
              figure=sketches.motion_sketch("start", "turn", f"{a} m east, then {b} m west", body="box"))


# ================================================================== L3
@template("c1b_density_gcm3_to_kgm3", chapter=1, level=3, lo="1c")
def density_gcm3_to_kgm3(rng):
    m_g = nice(rng, 54, 81, 135, 158, 216, 39)
    V = nice(rng, 20, 30, 50, 60, 80)
    rho = m_g / V
    ans = rho * 1000
    return mk(rng, ans, [(rho, "That is in g/cm³. Multiply by 1000 for kg/m³."),
                         (rho * 100, "1 g/cm³ = 1000 kg/m³, not 100."),
                         (rho * 1e6, "You converted the volume but not the mass.")],
              "kg/m³", f"A small metal block is weighed and its volume measured.\n\n{md_table(['quantity', 'value'], [['mass', f'{m_g} g'], ['volume', f'{V} cm³']])}\n\nWhat is its density in kg/m³?",
              "ρ = m ÷ V, then g/cm³ × 1000 = kg/m³", [f"ρ = {m_g} ÷ {V} = {fmt(rho)} g/cm³", f"= **{fmt(ans)} kg/m³**"],
              ["Find the density in g/cm³ first.", "1 g/cm³ = 1000 kg/m³.", f"({m_g} ÷ {V}) × 1000."])


@template("c1b_cuboid_volume_mm", chapter=1, level=3, lo="1c")
def cuboid_volume_mm(rng):
    a, b, c = nice(rng, 20, 25, 40, 50), nice(rng, 10, 15, 20), nice(rng, 5, 8, 10)
    ans = a * b * c / 1000
    return mk(rng, ans, [(a * b * c, "That is the volume in mm³. 1 cm³ = 1000 mm³."),
                         (a * b * c / 100, "1 cm = 10 mm, so 1 cm³ = 10 × 10 × 10 = 1000 mm³."),
                         (a * b * c / 10, "Divide by 1000, not 10.")],
              "cm³", f"Fig. 1 shows a block measured with digital calipers: **{a} mm × {b} mm × {c} mm**. What is its volume in cm³?",
              "V = l × w × h; 1 cm³ = 1000 mm³", [f"V = {a} × {b} × {c} = {a * b * c} mm³", f"= {a * b * c} ÷ 1000 = **{fmt(ans)} cm³**"],
              ["Multiply the three sides.", "The answer is in mm³; convert to cm³.", "Divide by 1000."],
              figure=figs.labelled_block(a, b, c, unit="mm"))


@template("c1b_displacement_cylinder", chapter=1, level=3, lo="1e")
def displacement_cylinder(rng):
    v0 = nice(rng, 30, 40, 50, 56, 60)
    dv = nice(rng, 12, 14, 16, 18, 20, 24)
    return mk(rng, dv, [(v0 + dv, "That is the final reading. The stone's volume is the RISE in the level."),
                        (v0, "That is the water alone."),
                        (dv / 2, "The rise in level equals the full volume of the stone.")],
              "cm³", "Fig. 1 shows a measuring cylinder before and after a stone is lowered into it. What is the volume of the stone?",
              "volume of solid = final reading − initial reading", [f"{v0 + dv} − {v0} = **{dv} cm³**"],
              ["Read both levels at the bottom of the meniscus.", "The stone pushes up the water by its own volume.", "Subtract the readings."],
              figure=figs.two_cylinders(v0, v0 + dv))


@template("c1b_wire_coil_diameter", chapter=1, level=3, lo="1e")
def wire_coil_diameter(rng):
    n = nice(rng, 20, 25, 30, 40, 50)
    d = nice(rng, 0.40, 0.50, 0.60, 0.80)
    L = n * d / 10
    return mk(rng, d, [(L, "That is the width of all the turns in cm. Divide by the number of turns, and change to mm."),
                       (L / n, "That is the diameter in cm. The answer is in mm (× 10)."),
                       (d * 2, "Each turn is one wire diameter, not two.")],
              "mm", f"A student winds a thin wire tightly round a pencil and measures the width of the turns with a rule.\n\n{md_table(['number of turns', 'width of turns / cm'], [[n, fmt(L)]])}\n\nWhat is the diameter of the wire in mm?",
              "diameter = width of turns ÷ number of turns", [f"{fmt(L)} cm ÷ {n} = {fmt(L / n)} cm", f"= **{fmt(d)} mm**"],
              ["Each turn adds one wire diameter.", f"Divide {fmt(L)} cm by {n}.", "Change cm to mm (× 10)."])


@template("c1b_micrometer_mean_corrected", chapter=1, level=3, lo="1e")
def micrometer_mean_corrected(rng):
    z = rng.choice([0.002, 0.003, -0.002, -0.004])
    true = round(rng.uniform(0.3, 1.2), 3)
    rs = [round(true + z + e, 3) for e in rng.sample([-0.002, -0.001, 0.0, 0.001, 0.002], 3)]
    mean = sum(rs) / 3
    ans = round(mean - z, 3)
    return mk(rng, ans, [(round(mean, 3), "You averaged but did not remove the zero error."),
                         (round(mean + z, 3), "Subtract the zero reading; do not add it."),
                         (round(sum(rs) - z, 3), "Divide the total by 3 to get the mean.")],
              "mm", f"A digital micrometer reads **{z:+.3f} mm** with its jaws closed. It is then used three times on a wire.\n\n{md_table(['reading', 'diameter / mm'], [[i + 1, f'{r:.3f}'] for i, r in enumerate(rs)])}\n\nWhat is the corrected mean diameter?",
              "mean of readings, then subtract the zero reading", [f"mean = {sum(rs):.3f} ÷ 3 = {mean:.4f} mm", f"corrected = {mean:.4f} − ({z:+.3f}) = **{ans:.3f} mm**"],
              ["Two steps: average, then correct.", "Corrected = reading − zero reading.", "Mind the sign of the zero reading."], dp=3)


@template("c1b_period_from_passes", chapter=1, level=3, lo="1e")
def period_from_passes(rng):
    T = nice(rng, 1.2, 1.4, 1.5, 1.6, 2.0)
    k = nice(rng, 10, 15, 20)
    passes = 2 * k + 1
    t = k * T
    return mk(rng, T, [(t / passes, f"{passes} passes through the centre is NOT {passes} oscillations. The bob passes the centre twice per oscillation."),
                       (t / (passes - 1), "Counting from the first pass, there are passes − 1 HALF-oscillations, so divide by half that."),
                       (t / k / 2, "You halved twice.")],
              "s", f"A stopwatch is started as a pendulum bob passes the centre of its swing and stopped as it passes the centre for the **{passes}th time** (counting the start as the 1st). The stopwatch reads **{fmt(t)} s** (Fig. 1). What is the period?",
              "passes through the centre: 2 per oscillation; oscillations = (passes − 1) ÷ 2", [f"oscillations = ({passes} − 1) ÷ 2 = {k}", f"T = {fmt(t)} ÷ {k} = **{fmt(T)} s**"],
              ["How many times does the bob pass the centre in one full oscillation?", "Twice. Between the 1st and the last pass there are (passes − 1) half-oscillations.", f"T = {fmt(t)} ÷ {k}."],
              figure=figs.stopwatch(figs2.stopwatch_text(t)))


@template("c1b_earth_atom_ratio", chapter=1, level=3, lo="1d")
def earth_atom_ratio(rng):
    a, b, la, lb = rng.choice([(1e7, 1e-10, "the Earth", "an atom"), (1e7, 1e-4, "the Earth", "a human hair"), (1e-4, 1e-10, "a sheet of paper", "an atom"), (1, 1e-6, "a person", "a bacterium")])
    r = a / b
    return mk(rng, r, [(b / a, "You divided the smaller by the larger. The ratio asked for is greater than 1."),
                       (math.log10(a) - math.log10(b), "That is the difference in the powers of ten, not the ratio itself."),
                       (r / 1000, "Check the subtraction of the powers of ten.")],
              "", f"The table gives typical orders of magnitude of sizes.\n\n{md_table(['object', 'size / m'], [[la, sci(a)], [lb, sci(b)]])}\n\nAbout how many times bigger is {la} than {lb}?",
              "ratio = larger size ÷ smaller size; subtract the powers of ten", [f"{sci(a)} ÷ {sci(b)} = **{sci(r)}**"],
              ["Divide the larger size by the smaller.", "Dividing powers of ten: subtract the indices.", f"{int(math.log10(a))} − ({int(math.log10(b))})."], sf=1)


@template("c1b_cells_across", chapter=1, level=3, lo="1d")
def cells_across(rng):
    cell = nice(rng, 10, 20, 25, 50)        # µm
    L = nice(rng, 1, 2, 5)                  # mm
    n = L * 1e-3 / (cell * 1e-6)
    return mk(rng, n, [(L / cell, "Change both to the same unit: 1 mm = 1000 µm."),
                       (L * 1e-2 / (cell * 1e-6), "1 mm is 10⁻³ m, not 10⁻² m."),
                       (n / 10, "Check the conversion of µm.")],
              "", f"A typical skin cell is about **{cell} µm** across.\n\n{md_table(['quantity', 'value'], [['width of a cell', f'{cell} µm'], ['length of skin sample', f'{L} mm']])}\n\nAbout how many cells lie side by side across the sample?",
              "number = length ÷ width (same units); 1 mm = 1000 µm", [f"{L} mm = {L * 1000} µm", f"n = {L * 1000} ÷ {cell} = **{fmt(n)}**"],
              ["Put both lengths in µm.", "1 mm = 1000 µm.", "Divide."])


# ================================================================== L4
@template("c1b_resultant_direction", chapter=1, level=4, lo="1g")
def resultant_direction(rng):
    a, b = rng.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6)])
    ang = math.degrees(math.atan2(b, a))
    return mk(rng, ang, [(90 - ang, "That angle is measured from the OTHER force. Read the question: the angle is from the horizontal force."),
                         (45, "45° only if the forces are equal."),
                         (math.degrees(math.atan2(a, b)) + 90, "The resultant lies BETWEEN the two forces, so the angle is less than 90°.")],
              "°", f"Fig. 1 shows two forces on a 1 N grid: **{a} N** horizontally and **{b} N** vertically. What is the angle between the resultant and the horizontal force?",
              "tan θ = vertical ÷ horizontal (resultant is the diagonal of the rectangle)", [f"tan θ = {b} ÷ {a}", f"θ = **{fmt(ang, sf=3)}°**"],
              ["Draw the resultant as the diagonal of the rectangle.", "The angle at O has opposite side b and adjacent side a.", f"θ = tan⁻¹({b}/{a})."],
              figure=figs2.vector_grid([("H", a, 0), ("V", 0, b)], nx=max(a, 4) + 3, ny=max(b, 4) + 2, origin=(1, 1)), sf=3)


@template("c1b_plane_crosswind", chapter=1, level=4, lo="1g")
def plane_crosswind(rng):
    v, w, r = rng.choice([(120, 50, 130), (160, 120, 200), (240, 70, 250), (90, 120, 150), (200, 150, 250)])
    return mk(rng, r, [(v + w, "The wind is at RIGHT ANGLES to the heading, so the velocities do not simply add."),
                       (v - w if v > w else w - v, "Subtracting applies only to opposite directions."),
                       (v, "The wind changes the resultant velocity.")],
              "km/h", f"A light aircraft heads north at **{v} km/h** relative to the air while a wind blows towards the east at **{w} km/h**. Fig. 1 shows the velocities to scale. What is the aircraft's resultant speed over the ground?",
              "perpendicular velocities: resultant² = v² + w² (diagonal of the rectangle)", [f"√({v}² + {w}²) = √{v * v + w * w}", f"= **{r} km/h**"],
              ["Draw the two velocities tip-to-tail.", "They are at right angles.", f"√({v}² + {w}²)."],
              figure=figs2.vector_pair(f"wind {w} km/h", f"heading {v} km/h", 90))


@template("c1b_counting_trap_zero", chapter=1, level=4, lo="1e")
def counting_trap_zero(rng):
    T = nice(rng, 1.2, 1.5, 1.8, 2.0, 2.4)
    n_said = nice(rng, 20, 25, 30)
    t = (n_said - 1) * T
    return mk(rng, T, [(t / n_said, f"The student said 'one' when starting, so only {n_said - 1} oscillations were timed, not {n_said}."),
                       (t / (n_said + 1), "Counting from 'one' gives FEWER oscillations, not more."),
                       (t / (2 * (n_said - 1)), "Each count is a full oscillation here, not a half.")],
              "s", f"A student starts a stopwatch and says 'one' at the same moment, then counts each complete oscillation, stopping the watch on '**{n_said}**'. The watch reads **{fmt(t)} s** (Fig. 1). What is the true period?",
              "starting the count at 'one' means (n − 1) oscillations were timed", [f"oscillations timed = {n_said} − 1 = {n_said - 1}", f"T = {fmt(t)} ÷ {n_said - 1} = **{fmt(T)} s**"],
              ["When the student said 'one', had any oscillation been completed?", f"No: the count should have started at zero, so only {n_said - 1} were timed.", f"Divide by {n_said - 1}."],
              figure=figs.stopwatch(figs2.stopwatch_text(t)))


@template("c1b_wire_volume_mixed", chapter=1, level=4, lo="1e")
def wire_volume_mixed(rng):
    d = nice(rng, 0.50, 0.60, 0.80, 1.00)
    L = nice(rng, 50, 80, 100, 120)
    V = math.pi * (d / 20) ** 2 * L
    return mk(rng, V, [(math.pi * (d / 2) ** 2 * L, "You used the diameter in mm with the length in cm. Use the same unit for both."),
                       (math.pi * (d / 10) ** 2 * L, "Use the RADIUS (half the diameter)."),
                       (math.pi * (d / 20) * L, "Area of a circle uses r², not r.")],
              "cm³", f"The diameter of a wire is measured with a digital micrometer and its length with a metre rule.\n\n{md_table(['quantity', 'value'], [['diameter', f'{fmt(d)} mm'], ['length', f'{L} cm']])}\n\nWhat is the volume of the wire in cm³?",
              "V = π r² L with r and L in cm", [f"r = {fmt(d)} ÷ 2 = {fmt(d / 2)} mm = {fmt(d / 20)} cm", f"V = π × {fmt(d / 20)}² × {L} = **{fmt(V, sf=3)} cm³**"],
              ["Change the diameter to cm and halve it.", "V = π r² L.", f"π × ({fmt(d / 20)})² × {L}."])


@template("c1b_pressure_nm2_ncm2", chapter=1, level=4, lo="1c")
def pressure_nm2_ncm2(rng):
    p = nice(rng, 2000, 5000, 12000, 25000, 40000)
    ans = p / 1e4
    return mk(rng, ans, [(p / 100, "1 m² = 10 000 cm², so N/m² → N/cm² is ÷ 10 000."),
                         (p * 1e4, "Per cm² is a SMALLER area, so the number gets smaller."),
                         (p / 1e6, "Use the area factor 10 000, not the volume factor.")],
              "N/cm²", f"A brick exerts a pressure on the ground.\n\n{md_table(['quantity', 'value'], [['pressure', f'{p} N/m²']])}\n\nWhat is this pressure in N/cm²?",
              "1 m² = 10 000 cm²: N/m² ÷ 10 000 = N/cm²", [f"{p} ÷ 10 000 = **{fmt(ans)} N/cm²**"],
              ["One square metre contains how many square centimetres?", "10 000. Each cm² carries 1/10 000 of the force on 1 m².", f"{p} ÷ 10 000."])


@template("c1b_light_speed_km", chapter=1, level=4, lo="1c")
def light_speed_km(rng):
    d_Gm = nice(rng, 0.384, 150, 228, 0.036)
    t = d_Gm * 1e9 / 3e8
    return mk(rng, t, [(d_Gm * 1e6 / 3e8, "Giga is 10⁹, not 10⁶."),
                       (d_Gm / 3e8, "Convert Gm to m before dividing."),
                       (d_Gm * 1e9 / 3e5, "Use the speed in m/s (3 × 10⁸), not km/s, with the distance in m.")],
              "s", f"Distances in space are often given with the prefix giga.\n\n{md_table(['quantity', 'value'], [['distance', f'{fmt(d_Gm)} Gm'], ['speed of light', '3.0 × 10⁸ m/s']])}\n\nHow long does light take to travel this distance?",
              "t = d ÷ v, with d in m (1 Gm = 10⁹ m)", [f"d = {fmt(d_Gm)} × 10⁹ m", f"t = {sci(d_Gm * 1e9)} ÷ 3.0 × 10⁸ = **{fmt(t, sf=3)} s**"],
              ["Change Gm into m.", "giga = 10⁹.", "Divide by 3.0 × 10⁸."])


@template("c1b_atoms_in_bacterium", chapter=1, level=4, lo="1d")
def atoms_in_bacterium(rng):
    b_um = nice(rng, 1, 2, 3, 5)
    a_nm = nice(rng, 0.1, 0.2, 0.25)
    n = b_um * 1e-6 / (a_nm * 1e-9)
    return mk(rng, n, [(b_um / a_nm, "µm and nm are different prefixes: 1 µm = 1000 nm."),
                       (n / 1000, "Check: 1 µm = 10⁻⁶ m and 1 nm = 10⁻⁹ m."),
                       (n * 1000, "Check the prefix values.")],
              "", f"A bacterium is about **{b_um} µm** long and an atom about **{fmt(a_nm)} nm** across.\n\n{md_table(['object', 'size'], [['bacterium', f'{b_um} µm'], ['atom', f'{fmt(a_nm)} nm']])}\n\nAbout how many atoms placed in a line would be as long as the bacterium?",
              "n = length ÷ atom width (same units; 1 µm = 1000 nm)", [f"{b_um} µm = {b_um * 1000} nm", f"n = {b_um * 1000} ÷ {fmt(a_nm)} = **{fmt(n)}**"],
              ["Put both in nm.", "1 µm = 1000 nm.", "Divide."])


@template("c1b_paper_thickness_order", chapter=1, level=4, lo="1d")
def paper_thickness_order(rng):
    n = nice(rng, 500, 250, 200, 400)
    h_cm = round(n * nice(rng, 0.008, 0.01, 0.012), 1)
    t = h_cm / 100 / n
    return mk(rng, t, [(h_cm / n, "That is in cm. Convert to metres."),
                       (h_cm / 1000 / n, "1 cm = 10⁻² m, not 10⁻³ m."),
                       (h_cm / 100, "Divide by the number of sheets.")],
              "m", f"A ream of paper is measured.\n\n{md_table(['number of sheets', 'thickness of ream / cm'], [[n, fmt(h_cm)]])}\n\nWhat is the thickness of one sheet in metres (its order of magnitude is about 10⁻⁴ m)?",
              "one sheet = ream ÷ number; cm → m ÷ 100", [f"{fmt(h_cm)} ÷ {n} = {fmt(h_cm / n)} cm", f"= **{sci(t)} m**"],
              ["Find one sheet's thickness in cm.", "Convert to m.", "Check it is about 10⁻⁴ m."], sf=2)


# ================================================================== L5
@template("c1b_density_mm_to_kgm3", chapter=1, level=5, lo="1c")
def density_mm_to_kgm3(rng):
    a, b, c = nice(rng, 20, 25, 40), nice(rng, 20, 10, 15), nice(rng, 5, 10)
    rho = nice(rng, 2700, 7800, 8900, 1200)
    m_g = rho * a * b * c * 1e-9 * 1000
    ans = rho
    V_m3 = a * b * c * 1e-9
    return mk(rng, ans, [(m_g / (a * b * c), "You used mass in g and volume in mm³. Convert to kg and m³."),
                         (m_g / 1000 / (a * b * c * 1e-6), "1 mm³ = 10⁻⁹ m³ (not 10⁻⁶)."),
                         (m_g / (a * b * c / 1000), "That is g/cm³. Multiply by 1000 for kg/m³.")],
              "kg/m³", f"A block is measured with digital calipers and weighed on a balance (Fig. 1).\n\n{md_table(['quantity', 'value'], [['dimensions', f'{a} mm × {b} mm × {c} mm'], ['mass', f'{fmt(m_g, sf=4)} g']])}\n\nWhat is the density of the block in kg/m³?",
              "ρ = m ÷ V with m in kg and V in m³ (1 mm³ = 10⁻⁹ m³)", [f"V = {a * b * c} mm³ = {sci(V_m3)} m³", f"m = {fmt(m_g, sf=4)} g = {fmt(m_g / 1000, sf=4)} kg", f"ρ = **{fmt(ans)} kg/m³**"],
              ["Two conversions: g → kg and mm³ → m³.", "1 mm = 10⁻³ m, so 1 mm³ = 10⁻⁹ m³.", "Divide mass in kg by volume in m³."],
              figure=figs.labelled_block(a, b, c, unit="mm"))


@template("c1b_heading_upstream", chapter=1, level=5, lo="1g")
def heading_upstream(rng):
    boat, cur = rng.choice([(5.0, 3.0), (10.0, 6.0), (2.5, 1.5), (13.0, 5.0), (10.0, 8.0)])
    ang = math.degrees(math.asin(cur / boat))
    across = math.sqrt(boat ** 2 - cur ** 2)
    return mk(rng, ang, [(math.degrees(math.atan(cur / boat)), "The boat's speed is the HYPOTENUSE here (the resultant must point straight across), so use sin, not tan."),
                         (90 - ang, "That is measured from the bank. The question asks for the angle from the line straight across."),
                         (math.degrees(math.atan(boat / cur)), "Check which side is opposite the angle.")],
              "°", f"A boat can move at **{fmt(boat)} m/s** relative to the water. The river flows at **{fmt(cur)} m/s**. At what angle upstream from the line straight across must the boat point so that it travels straight across (Fig. 1)?",
              "resultant straight across: boat velocity is the hypotenuse, current the opposite side: sin θ = current ÷ boat speed",
              [f"sin θ = {fmt(cur)} ÷ {fmt(boat)}", f"θ = **{fmt(ang, sf=3)}°**", f"(speed across = √({fmt(boat)}² − {fmt(cur)}²) = {fmt(across)} m/s)"],
              ["Draw the triangle: boat velocity + current = resultant (straight across).", "The boat velocity is the longest side.", "sin θ = opposite ÷ hypotenuse."],
              figure=figs2.vector_pair("current", "boat", 90 + round(ang)), sf=3)


@template("c1b_irregular_density_si", chapter=1, level=5, lo="1e")
def irregular_density_si(rng):
    v0 = nice(rng, 40, 50, 60)
    dv = nice(rng, 10, 12, 15, 20)
    rho_g = nice(rng, 2.6, 2.7, 3.0)
    m = rho_g * dv
    ans = rho_g * 1000
    return mk(rng, ans, [(m / (v0 + dv) * 1000, "You used the final reading as the volume. The stone's volume is the RISE in the level."),
                         (rho_g, "That is in g/cm³. Convert to kg/m³."),
                         (m / v0 * 1000, "The stone's volume is the change in reading, not the initial reading.")],
              "kg/m³", f"A stone of mass **{fmt(m)} g** is lowered into the measuring cylinder in Fig. 1. What is the density of the stone in kg/m³?",
              "V = rise in reading; ρ = m ÷ V; × 1000 for kg/m³", [f"V = {v0 + dv} − {v0} = {dv} cm³", f"ρ = {fmt(m)} ÷ {dv} = {fmt(rho_g)} g/cm³", f"= **{fmt(ans)} kg/m³**"],
              ["First find the stone's volume from the two readings.", "Then divide the mass by that volume.", "Convert g/cm³ to kg/m³ (× 1000)."],
              figure=figs.two_cylinders(v0, v0 + dv))


@template("c1b_negative_zero_mean", chapter=1, level=5, lo="1e")
def negative_zero_mean(rng):
    z = rng.choice([-0.03, -0.02, -0.04])
    true = round(rng.uniform(10, 25), 2)
    rs = [round(true + z + e, 2) for e in rng.sample([-0.02, -0.01, 0.0, 0.01, 0.02], 3)]
    mean = sum(rs) / 3
    ans = round(mean - z, 2)
    return mk(rng, ans, [(round(mean + z, 2), "A NEGATIVE zero error means the calipers read too LOW; subtracting a negative adds it back."),
                         (round(mean, 2), "You averaged but forgot the zero error."),
                         (round(rs[0] - z, 2), "Use the mean of all three readings, not just the first.")],
              "mm", f"Digital calipers read **{z:.2f} mm** with the jaws closed. Three readings of a bottle cap are then taken.\n\n{md_table(['reading', 'diameter / mm'], [[i + 1, f'{r:.2f}'] for i, r in enumerate(rs)])}\n\nWhat is the corrected mean diameter?",
              "corrected = mean reading − zero reading (zero reading is negative here)", [f"mean = {sum(rs):.2f} ÷ 3 = {mean:.3f} mm", f"corrected = {mean:.3f} − ({z:.2f}) = **{ans:.2f} mm**"],
              ["Average the three readings.", "Corrected = reading − zero reading.", f"Subtracting {z:.2f} means adding {abs(z):.2f}."], dp=2)


@template("c1b_coil_on_pencil_rule", chapter=1, level=5, lo="1e")
def coil_on_pencil_rule(rng):
    n = nice(rng, 20, 25, 40, 50)
    d = nice(rng, 0.25, 0.30, 0.40, 0.50)
    L_cm = n * d / 10
    return mk(rng, d * 1e-3, [(L_cm / n, "That is in cm. The answer is asked in metres."),
                              (L_cm / n / 10, "1 cm = 10⁻² m, so cm → m is ÷ 100."),
                              (L_cm / 100, "Divide by the number of turns as well.")],
              "m", f"A thin wire is wound in close turns round a pencil.\n\n{md_table(['number of turns', 'width covered on the rule / cm'], [[n, fmt(L_cm)]])}\n\nWhat is the diameter of the wire in metres?",
              "d = width ÷ turns; then cm → m", [f"d = {fmt(L_cm)} ÷ {n} = {fmt(L_cm / n)} cm", f"= **{sci(d * 1e-3)} m**"],
              ["Each turn adds one diameter.", "Divide the width by the number of turns.", "Convert cm to m (÷ 100)."], sf=2)


@template("c1b_scale_model_earth", chapter=1, level=5, lo="1d")
def scale_model_earth(rng):
    model_cm = nice(rng, 1, 2, 5)
    ans = 1e7 * (model_cm * 1e-2 / 1e-10)
    return mk(rng, ans, [(1e7 * model_cm / 1e-10, "Change the model size to metres before scaling."),
                         (1e7 * (model_cm * 1e-2) / 1e-7, "An atom is about 10⁻¹⁰ m, not 10⁻⁷ m."),
                         (ans / 1e3, "Check the powers of ten.")],
              "m", f"An atom (about 10⁻¹⁰ m) is drawn as a circle **{model_cm} cm** across. The Earth is about 10⁷ m across.\n\n{md_table(['object', 'real size / m'], [['atom', '1 × 10⁻¹⁰'], ['Earth', '1 × 10⁷']])}\n\nTo the same scale, how big would the Earth be?",
              "scale factor = model size ÷ real size; apply the same factor to the Earth", [f"scale factor = {model_cm} × 10⁻² ÷ 10⁻¹⁰ = {sci(model_cm * 1e-2 / 1e-10)}", f"Earth = 10⁷ × that = **{sci(ans)} m**"],
              ["Find the magnification that turns an atom into the drawing.", "Use metres throughout.", "Multiply the Earth's size by the same factor."], sf=1)


@template("c1b_nucleus_marble", chapter=1, level=5, lo="1d")
def nucleus_marble(rng):
    marble_cm = nice(rng, 1, 2)
    ans_m = marble_cm * 1e-2 * (1e-10 / 1e-15)
    return mk(rng, ans_m, [(marble_cm * (1e-10 / 1e-15), "Convert the marble size to metres."),
                           (marble_cm * 1e-2 * 1e-5, "The atom is BIGGER than the nucleus, so multiply by 10⁵."),
                           (ans_m / 100, "Check the conversion of cm.")],
              "m", f"A nucleus is about 10⁻¹⁵ m across and an atom about 10⁻¹⁰ m. If the nucleus were a marble **{marble_cm} cm** across, how wide would the atom be on the same scale?\n\n{md_table(['object', 'size / m'], [['nucleus', '1 × 10⁻¹⁵'], ['atom', '1 × 10⁻¹⁰']])}",
              "atom ÷ nucleus = 10⁵; multiply the marble size by 10⁵", [f"ratio = 10⁻¹⁰ ÷ 10⁻¹⁵ = 10⁵", f"atom = {marble_cm} × 10⁻² m × 10⁵ = **{fmt(ans_m)} m**"],
              ["How many times bigger is the atom than its nucleus?", "10⁵ times.", f"Multiply {marble_cm} cm (in m) by 10⁵."], sf=2)


@template("c1b_reaction_percent_error", chapter=1, level=5, lo="1e")
def reaction_percent_error(rng):
    T = nice(rng, 1.2, 1.5, 2.0, 2.5)
    n = nice(rng, 10, 20, 25, 40)
    rt = nice(rng, 0.2, 0.3)
    pct = rt / (n * T) * 100
    return mk(rng, pct, [(rt / T * 100, f"That is the error for timing ONE oscillation. The error is shared over {n} oscillations."),
                         (rt / (n * T), "Multiply by 100 to give a percentage."),
                         (rt * n / T * 100, "The total time is n × T; the error is divided by it, not multiplied.")],
              "%", f"A pendulum has a period of about **{fmt(T)} s**. A student's reaction time is about **{fmt(rt)} s**.\n\n{md_table(['oscillations timed', 'reaction-time error / s'], [[n, fmt(rt)]])}\n\nWhat is the percentage error in the measured period caused by the reaction time?",
              "% error = reaction-time error ÷ total time measured × 100%, total time = n T",
              [f"total time = {n} × {fmt(T)} = {fmt(n * T)} s", f"% error = {fmt(rt)} ÷ {fmt(n * T)} × 100 = **{fmt(pct, sf=2)}%**"],
              ["The reaction-time error happens once for the whole timing.", f"The whole timing lasts {n} periods.", "Divide the error by the total time, × 100."], sf=2)
