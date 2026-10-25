"""Chapter 1 Physical Quantities, Units and Measurement (6091): calculation templates.
Prefix conversions, digital calipers with zero error, timing a pendulum, averaging readings, displacement, resultant of two vectors."""
import math

from .. import figs, figs2, sketches
from .base import fmt, md_table, nice, numeric_options, template

PREFIX = {"n": (1e-9, "nano"), "µ": (1e-6, "micro"), "m": (1e-3, "milli"), "c": (1e-2, "centi"), "k": (1e3, "kilo"), "M": (1e6, "mega"), "G": (1e9, "giga")}


def _sci(x):
    """'4.5 × 10⁻⁴' style string for a positive float"""
    e = int(math.floor(math.log10(x)))
    mant = x / 10 ** e
    sup = str(e).replace("-", "⁻").translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{fmt(mant, sf=2)} × 10{sup}"


# ---------------------------------------------------------------- L1
@template("c1_period_from_oscillations", chapter=1, level=1, lo="1e")
def period_from_oscillations(rng):
    n = nice(rng, 10, 20, 25, 40, 50)
    T = nice(rng, 0.8, 1.2, 1.5, 1.6, 2.0, 2.4, 2.5)
    total = round(n * T, 2)
    opts, key, mis = numeric_options(rng, T, [
        (n / total, "You divided the number of oscillations by the time. Period = time ÷ number of oscillations."),
        (total * n, "You multiplied. The period is the time for ONE oscillation, so it must be smaller than the total time."),
        (total, "That is the total time for all the oscillations, not the time for one."),
    ], unit="s")
    return dict(
        stem=f"A student times the pendulum shown in Fig. 1 and finds that it completes **{n} oscillations in {fmt(total)} s**. What is the period of the pendulum?",
        figure=sketches.pendulum_sketch(f"{n} complete oscillations in {fmt(total)} s"),
        options=opts, key=key, misconceptions=mis,
        formula="period = total time ÷ number of oscillations",
        working=["period = total time ÷ number of oscillations", f"= {fmt(total)} s ÷ {n}", f"= **{fmt(T)} s**"],
        hints=[
            "The period is the time for ONE complete oscillation. Which formula links the total time, the number of oscillations and the period?",
            f"The {fmt(total)} s is the time for {n} oscillations. You want the time for just one of them, so the answer must be smaller than {fmt(total)} s.",
            f"T = {fmt(total)} ÷ {n}. Work out the division and keep the unit s.",
        ],
    )


@template("c1_prefix_to_si", chapter=1, level=1, lo="1c")
def prefix_to_si(rng):
    sym, (mult, name) = rng.choice(list(PREFIX.items()))
    value = nice(rng, 2.5, 3.2, 4.5, 6.0, 7.5, 8.4, 9.6, 12, 25, 60)
    quantity, unit = rng.choice([("length", "m"), ("mass", "g"), ("time", "s"), ("current", "A")])
    ans = value * mult
    bigger = mult * 1000 if mult < 1 else mult / 1000
    opts, key, mis = numeric_options(rng, ans, [
        (value * bigger, f"That is the wrong power of ten for {name}. Check the prefix table: {name} ({sym}) = {_sci(mult)}."),
        (value / mult, f"You divided by the multiplier. To convert {sym}{unit} to {unit}, multiply by {_sci(mult)}."),
        (value * mult * 10, "One power of ten out. Count the zeros carefully when you write the prefix as a power of ten."),
    ], unit=unit, sf=2)
    table = md_table(["prefix", "symbol", "multiplier"], [[name, sym, _sci(mult)]])
    return dict(
        stem=f"The table shows one SI prefix.\n\n{table}\n\nA {quantity} is recorded as **{fmt(value)} {sym}{unit}**. What is this {quantity} in {unit}?",
        options=opts, key=key, misconceptions=mis,
        formula=f"{sym}{unit} → {unit}: multiply by the prefix multiplier ({name} = {_sci(mult)})",
        working=[f"{name} ({sym}) means × {_sci(mult)}", f"{fmt(value)} {sym}{unit} = {fmt(value)} × {_sci(mult)} {unit}", f"= **{fmt(ans, sf=2)} {unit}**"],
        hints=[
            "A prefix is just a multiplier written as a power of ten. Read it off the table.",
            f"Replace the prefix {sym} with its multiplier {_sci(mult)}, keeping the unit {unit}.",
            f"{fmt(value)} × {_sci(mult)} = ? Write the answer in standard form.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c1_digital_calipers_zero_error", chapter=1, level=2, lo="1e")
def digital_calipers_zero_error(rng):
    zero = rng.choice([-0.05, -0.04, -0.03, -0.02, 0.02, 0.03, 0.04, 0.06])
    true = round(rng.uniform(6.0, 24.0), 2)
    shown = round(true + zero, 2)
    obj = rng.choice(["a ball bearing", "a marble", "a coin", "a bolt head"])
    opts, key, mis = numeric_options(rng, true, [
        (shown, "That is the display reading with the object in place. The zero error has not been removed."),
        (round(shown + zero, 2), "You added the zero error instead of subtracting it. Corrected reading = display reading − zero reading."),
        (round(abs(zero), 2), "That is just the zero error itself, not the diameter."),
    ], unit="mm", dp=2)
    sign = "−" if zero < 0 else "+"
    return dict(
        stem=f"A student closes the jaws of a pair of digital calipers and the display shows a reading. {obj.capitalize()} is then placed between the jaws. Fig. 1 shows both displays. What is the diameter of {obj.split()[-1] if obj.split()[-1] != 'head' else 'the bolt head'}?".replace("diameter of bearing", "diameter of the ball bearing").replace("diameter of marble", "diameter of the marble").replace("diameter of coin", "diameter of the coin"),
        figure=figs2.caliper_pair(f"{zero:.2f}" if zero < 0 else f"{zero:.2f}", f"{shown:.2f}"),
        options=opts, key=key, misconceptions=mis,
        formula="corrected reading = display reading − zero reading",
        working=[f"zero error (jaws closed) = {sign}{abs(zero):.2f} mm", f"reading with the object = {shown:.2f} mm",
                 f"diameter = {shown:.2f} − ({sign}{abs(zero):.2f}) = **{true:.2f} mm**"],
        hints=[
            "With the jaws closed the display should read 0.00 mm. What does the first display tell you?",
            f"The jaws-closed reading ({sign}{abs(zero):.2f} mm) is the zero error. Every reading includes it, so it must be taken away.",
            f"diameter = {shown:.2f} − ({sign}{abs(zero):.2f}). Mind the sign of the zero error.",
        ],
    )


@template("c1_stopwatch_period", chapter=1, level=2, lo="1e")
def stopwatch_period(rng):
    n = nice(rng, 10, 20, 25, 30, 40, 50)
    T = nice(rng, 1.2, 1.5, 1.6, 1.8, 2.0, 2.4, 2.5, 3.0)
    total = round(n * T, 2)
    minutes, secs = int(total // 60), total - 60 * int(total // 60)
    display = f"{minutes}:{secs:05.2f}"
    misread = minutes * 100 + secs if minutes else total * 10
    opts, key, mis = numeric_options(rng, T, [
        (n / total, "You divided the number of oscillations by the time: it should be time ÷ number."),
        (misread / n, "The display shows minutes : seconds. Convert the minutes to seconds first (1 min = 60 s)." if minutes else "Check how you read the display: the digits after the colon are seconds."),
        (total / (n + 1), "You divided by one oscillation too many. Count the oscillations given in the question."),
    ], unit="s", dp=2)
    return dict(
        stem=f"A student starts a digital stopwatch as a pendulum bob passes its rest position and stops it after **{n} complete oscillations**. Fig. 1 shows the stopwatch. What is the period of the pendulum?",
        figure=figs.stopwatch(display),
        options=opts, key=key, misconceptions=mis,
        formula="period = total time ÷ number of oscillations",
        working=[f"stopwatch reading = {display} = {fmt(total)} s", f"period = {fmt(total)} ÷ {n} = **{fmt(T, dp=2)} s**"],
        hints=[
            "First read the stopwatch in seconds, then ask: how many oscillations did that time cover?",
            f"The display {display} means {minutes} min {fmt(secs)} s = {fmt(total)} s in total. That is for {n} oscillations.",
            f"Period = {fmt(total)} ÷ {n}.",
        ],
    )


@template("c1_mean_of_readings", chapter=1, level=2, lo="1e")
def mean_of_readings(rng):
    base = round(rng.uniform(1.5, 9.5), 3)
    readings = [round(base + d, 3) for d in rng.sample([-0.004, -0.003, -0.002, -0.001, 0.001, 0.002, 0.003, 0.004, 0.005], 3)]
    mean = sum(readings) / 3
    ans = round(mean, 3)
    opts, key, mis = numeric_options(rng, ans, [
        (round(sum(readings), 3), "That is the total of the three readings. Divide by the number of readings to get the mean."),
        (round(max(readings), 3), "That is the largest reading. The mean is the sum divided by three."),
        (round(mean / 10, 3), "Check your division: the mean must lie between the smallest and largest readings."),
    ], unit="mm", dp=3)
    table = md_table(["reading", "diameter / mm"], [[i + 1, f"{r:.3f}"] for i, r in enumerate(readings)])
    return dict(
        stem=f"A student measures the diameter of a wire at three places with a digital micrometer (precision 0.001 mm).\n\n{table}\n\nWhat is the mean diameter of the wire?",
        options=opts, key=key, misconceptions=mis,
        formula="mean = (sum of readings) ÷ (number of readings), given to the precision of the instrument",
        working=[f"sum = {readings[0]:.3f} + {readings[1]:.3f} + {readings[2]:.3f} = {sum(readings):.3f} mm", f"mean = {sum(readings):.3f} ÷ 3 = **{ans:.3f} mm**"],
        hints=[
            "Several readings are taken to reduce random error. How do you combine them into one value?",
            "Add the three readings and divide by three. Keep the answer to the same number of decimal places as the instrument reads.",
            f"({readings[0]:.3f} + {readings[1]:.3f} + {readings[2]:.3f}) ÷ 3 = ?",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c1_displacement_two_legs", chapter=1, level=3, lo="1g")
def displacement_two_legs(rng):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (9, 12, 15), (5, 12, 13), (8, 15, 17), (30, 40, 50), (60, 80, 100), (50, 120, 130)])
    opts, key, mis = numeric_options(rng, c, [
        (a + b, "That is the total DISTANCE walked. Displacement is the straight-line distance from start to finish."),
        (abs(a - b), "You subtracted the two legs. They are at right angles, so use Pythagoras' theorem."),
        (max(a, b), "That is just the longer leg. The straight line from start to finish is longer than either leg."),
    ], unit="m")
    return dict(
        stem=f"A student walks **{a} m due north** and then **{b} m due east**, as shown in Fig. 1. What is the magnitude of the student's displacement from the starting point?",
        figure=figs.path_figure(a, b),
        options=opts, key=key, misconceptions=mis,
        formula="displacement² = north² + east² (Pythagoras, legs at right angles)",
        working=[f"displacement = √({a}² + {b}²)", f"= √({a * a} + {b * b}) = √{a * a + b * b}", f"= **{c} m**"],
        hints=[
            "Displacement is a vector: the straight-line distance from start to finish, with a direction. What shape do the two legs and the straight line make?",
            f"The two legs are at right angles, so the straight line is the hypotenuse of a right-angled triangle with sides {a} m and {b} m.",
            f"displacement = √({a}² + {b}²) = √{a * a + b * b}.",
        ],
    )


@template("c1_resultant_perpendicular_forces", chapter=1, level=3, lo="1g")
def resultant_perpendicular_forces(rng):
    a, b, c = rng.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13)])
    opts, key, mis = numeric_options(rng, c, [
        (a + b, "You added the magnitudes. Only forces in the SAME direction add like that; these are at right angles."),
        (abs(a - b), "You subtracted. Forces at right angles combine by the parallelogram (or triangle) rule, not by subtraction."),
        (math.sqrt(a * a + b * b) * 2, "That is twice the resultant. Check the scale: 1 square = 1 N."),
    ], unit="N")
    return dict(
        stem=f"Two forces, **P = {a} N** horizontally and **Q = {b} N** vertically, act on a box at point O. Fig. 1 shows the forces drawn to scale (1 square = 1 N). What is the magnitude of the resultant force?",
        figure=figs2.vector_grid([("P", a, 0), ("Q", 0, b)], nx=max(a, 4) + 3, ny=max(b, 4) + 2, origin=(1, 1)),
        options=opts, key=key, misconceptions=mis,
        formula="resultant² = P² + Q² for two forces at right angles (or measure the diagonal of the parallelogram)",
        working=["complete the rectangle with P and Q as adjacent sides; the diagonal from O is the resultant",
                 f"resultant = √({a}² + {b}²) = √{a * a + b * b}", f"= **{c} N**"],
        hints=[
            "Draw the two forces as adjacent sides of a rectangle. Where is the resultant on that drawing?",
            f"The resultant is the diagonal from O. Count squares along it, or use Pythagoras with {a} and {b}.",
            f"√({a}² + {b}²) = √{a * a + b * b}.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c1_parallelogram_two_forces", chapter=1, level=4, lo="1g")
def parallelogram_two_forces(rng):
    a = nice(rng, 4.0, 5.0, 6.0, 8.0)
    b = nice(rng, 3.0, 5.0, 6.0, 7.0)
    ang = nice(rng, 60, 90, 120)
    R = math.sqrt(a * a + b * b + 2 * a * b * math.cos(math.radians(ang)))
    opts, key, mis = numeric_options(rng, R, [
        (a + b, "That is the resultant only if the forces are in the same direction. Here there is an angle between them, so the resultant is smaller."),
        (abs(a - b), "That is the resultant only if the forces are in opposite directions."),
        (math.sqrt(a * a + b * b), "You used Pythagoras, which only works when the angle between the forces is 90°." if ang != 90 else "Check the arithmetic of √(a² + b²)."),
    ], unit="N", sf=2)
    return dict(
        stem=f"Two forces of **{fmt(a)} N** and **{fmt(b)} N** act on an object at the same point, with an angle of **{ang}°** between them, as shown in Fig. 1. A student draws a parallelogram of forces to scale. What is the magnitude of the resultant force?",
        figure=figs2.vector_pair(f"{fmt(a)} N", f"{fmt(b)} N", ang),
        options=opts, key=key, misconceptions=mis,
        formula="scale drawing: complete the parallelogram, measure the diagonal from the point where the forces act (or R² = a² + b² + 2ab cos θ)",
        working=["draw the two forces to scale from one point, complete the parallelogram, draw the diagonal from that point",
                 f"R² = {fmt(a)}² + {fmt(b)}² + 2 × {fmt(a)} × {fmt(b)} × cos {ang}°", f"R = **{fmt(R, sf=2)} N**"],
        hints=[
            "On a scale drawing the resultant is the diagonal of the parallelogram whose sides are the two forces. Is it longer or shorter than the two forces added?",
            f"At {ang}° the resultant is between |{fmt(a)} − {fmt(b)}| N and {fmt(a + b)} N. Two options are outside that range.",
            f"R² = a² + b² + 2ab cos θ with θ = {ang}°, or measure the diagonal on the drawing.",
        ],
    )


@template("c1_sheet_thickness", chapter=1, level=4, lo="1e")
def sheet_thickness(rng):
    n = nice(rng, 20, 25, 40, 50, 80, 100)
    t_um = nice(rng, 80, 90, 100, 110, 120, 150)      # thickness of one sheet in µm
    stack_mm = n * t_um / 1000
    opts, key, mis = numeric_options(rng, t_um, [
        (stack_mm, "That is the thickness of the whole stack in mm. Divide by the number of sheets, then convert to µm."),
        (t_um / 10, "Check the conversion: 1 mm = 1000 µm."),
        (t_um * 10, "Check the conversion: 1 mm = 1000 µm, not 10 000."),
    ], unit="µm")
    return dict(
        stem=f"A single sheet of paper is too thin to measure directly, so a student measures a stack of **{n} sheets** with digital calipers, as shown in Fig. 1. What is the thickness of one sheet, in micrometres (µm)?",
        figure=figs2.digital_calipers(f"{stack_mm:.2f}", object_label=f"stack of {n} sheets"),
        options=opts, key=key, misconceptions=mis,
        formula="thickness of one sheet = stack thickness ÷ number of sheets; 1 mm = 1000 µm",
        working=[f"stack thickness = {stack_mm:.2f} mm", f"one sheet = {stack_mm:.2f} ÷ {n} = {fmt(t_um / 1000, sf=3)} mm", f"= {fmt(t_um / 1000, sf=3)} × 1000 µm = **{t_um} µm**"],
        hints=[
            "Measuring many sheets together makes the small thickness measurable. How do you get back to one sheet?",
            f"Divide the stack reading by {n}. The answer is in mm; the question wants µm.",
            f"{stack_mm:.2f} mm ÷ {n}, then × 1000 to change mm to µm.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c1_density_mixed_units", chapter=1, level=5, lo="1c")
def density_mixed_units(rng):
    rho = nice(rng, 0.8, 1.2, 2.5, 2.7, 4.0, 7.9, 8.9)        # g/cm³
    V = nice(rng, 200, 250, 400, 500, 800, 1000)              # cm³
    mass_kg = round(rho * V / 1000, 4)
    ans = rho * 1000                                          # kg/m³
    opts, key, mis = numeric_options(rng, ans, [
        (rho, "That is the density in g/cm³. The question asks for kg/m³, and 1 g/cm³ = 1000 kg/m³."),
        (rho / 10, "You used 1 m³ = 100 cm³. In fact 1 m³ = 100 × 100 × 100 = 1 000 000 cm³."),
        (rho * 1e6, "You left the mass in grams. 1 kg = 1000 g."),
    ], unit="kg/m³")
    return dict(
        stem=f"Fig. 1 shows a metal block of mass **{fmt(mass_kg, sf=4)} kg** and volume **{V} cm³**. What is the density of the metal in **kg/m³**?",
        figure=sketches.lump_sketch([f"mass = {fmt(mass_kg, sf=4)} kg", f"volume = {V} cm³"]),
        options=opts, key=key, misconceptions=mis,
        formula="density = mass ÷ volume, with mass in kg and volume in m³ (1 m³ = 1 000 000 cm³)",
        working=[f"volume = {V} cm³ = {V} ÷ 1 000 000 m³ = {fmt(V / 1e6, sf=4)} m³",
                 f"density = {fmt(mass_kg, sf=4)} ÷ {fmt(V / 1e6, sf=4)}", f"= **{fmt(ans)} kg/m³**"],
        hints=[
            "Density = mass ÷ volume, but the answer must be in kg/m³. Which of the two given quantities is NOT in an SI unit?",
            "The volume is in cm³. How many cm³ make 1 m³? (Think 100 cm × 100 cm × 100 cm.)",
            f"density = {fmt(mass_kg, sf=4)} kg ÷ ({V} ÷ 1 000 000) m³. Alternatively: {fmt(rho * V)} g ÷ {V} cm³ = {fmt(rho)} g/cm³, then × 1000.",
        ],
    )


@template("c1_boat_river_angle", chapter=1, level=5, lo="1g")
def boat_river_angle(rng):
    across, current, res = rng.choice([(4, 3, 5), (3, 4, 5), (8, 6, 10), (6, 8, 10), (12, 5, 13), (5, 12, 13)])
    angle = math.degrees(math.atan2(current, across))        # angle of the resultant from the "across" direction
    opts, key, mis = numeric_options(rng, angle, [
        (90 - angle, "That is the angle measured from the river bank, not from the line straight across. Check which line the question measures from."),
        (res * 10, "That is not an angle: it looks like the resultant speed. The question asks for the direction."),
        (45, "45° is only right when the two velocities are equal. Here they are not."),
    ], unit="°", sf=2)
    return dict(
        stem=f"A boat heads straight across a river at **{across} m/s** relative to the water. The current carries it downstream at **{current} m/s**. Fig. 1 shows the two velocities drawn to scale (1 square = 1 m/s). At what angle to the line straight across the river does the boat actually travel?",
        figure=figs2.vector_grid([("boat", 0, across), ("current", current, 0)], nx=max(current, 4) + 3, ny=max(across, 4) + 2, origin=(1, 1), scale_label="1 square = 1 m/s"),
        options=opts, key=key, misconceptions=mis,
        formula="draw the resultant (diagonal of the rectangle); tan θ = current ÷ across-speed, θ measured from the across direction",
        working=[f"resultant speed = √({across}² + {current}²) = {res} m/s", f"tan θ = {current} ÷ {across}", f"θ = **{fmt(angle, sf=2)}°** from the line straight across"],
        hints=[
            "Add the two velocities as vectors: complete the rectangle and draw the diagonal from the start. Which angle does the question want?",
            f"The angle between the diagonal and the 'straight across' side has opposite side {current} and adjacent side {across}.",
            f"θ = tan⁻¹({current} ÷ {across}). You can also measure it with a protractor on the drawing.",
        ],
    )
