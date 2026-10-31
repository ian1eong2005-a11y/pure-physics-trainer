"""O level 2026 MCQ practice, Ch 1-10: learning outcomes the SEAB specimen Paper 1 does not reach, adapted from schools' 2024-2026
6091 Paper 1 prelims (added 31 Oct 2026). Same context and skill as the source question; numbers changed; figures redrawn.
Where no 6091 paper on file tests an outcome, the item is adapted from a 2024 Science (Physics) 5086 prelim or an SEAB O-Level
Paper 1 (noted in the source)."""
import math

from .. import figs, figs2, sketches
from .base import calc_q, explain_mcqs, fmt, md_table, nice, sci, template, text_options

CAT = "olevel"


def cite(text):
    return f"_Adapted from {text}._"


# ================================================================== Ch 1 Measurement
explain_mcqs([
    dict(id="o26s_magnitude_unit", chapter=1, level=1, lo="1a", source="BGSS 2024 prelim (5086) MCQ 1",
         stem="Length, time and mass are all physical quantities. What does every physical quantity have?",
         correct="a numerical magnitude and a unit",
         wrongs={"a numerical magnitude, a direction and a unit": "Only VECTOR quantities have a direction. Length, time and mass are scalars.",
                 "a numerical magnitude only": "A number on its own says nothing: '5' could be 5 m or 5 km. The unit is part of the quantity.",
                 "a unit only": "The unit tells you what is measured; the magnitude tells you how much. Both are needed."},
         hints=["How would you write down the length of your desk?", "You write a number and something after it.", "Vectors also have a direction, but not every physical quantity is a vector."]),
    dict(id="o26s_base_quantity", chapter=1, level=1, lo="1b", source="NAS 2025 prelim MCQ 1",
         stem="Which physical quantity is a base quantity?",
         correct="temperature",
         wrongs={"energy": "Energy is derived: joule = kg m²/s².", "velocity": "Velocity is derived from length ÷ time.",
                 "charge": "Charge is derived from current × time (C = A s). Current is the base quantity."},
         hints=["The six base quantities are mass, length, time, current, temperature and amount of substance.",
                "Every other quantity is built from them.", "Which option is on the list itself?"]),
    dict(id="o26s_base_units_list", chapter=1, level=2, lo="1b", source="ACSBR 2024 prelim MCQ 1",
         stem="Which list contains SI base units only?",
         correct="kelvin, kilogram, mole, second",
         wrongs={"ampere, kilogram, hour, volt": "The hour is not an SI unit (the second is) and the volt is a derived unit.",
                 "ampere, metre, kilometre, second": "The kilometre is a multiple of the metre, not a base unit.",
                 "kelvin, metre, newton, second": "The newton is derived: 1 N = 1 kg m/s²."},
         hints=["The SI base units are kg, m, s, A, K and mol.", "A prefix (kilo-, milli-) on a unit does not make a new base unit, except the kilogram itself.",
                "Newton, volt and joule are all built from base units."]),
    dict(id="o26s_virus_order", chapter=1, level=1, lo="1d", source="HGV 2024 prelim MCQ 1",
         stem="What is a suitable estimate for the diameter of a bacterium?",
         correct="1 × 10⁻⁶ m",
         wrongs={"1 × 10⁻³ m": "10⁻³ m is 1 mm: a grain of sand, easily visible.", "1 × 10⁻¹⁰ m": "10⁻¹⁰ m is the size of an atom; a bacterium is made of millions of atoms.",
                 "1 × 10⁻²⁰ m": "Nothing in the syllabus is that small: even a nucleus is about 10⁻¹⁵ m."},
         hints=["A bacterium can only be seen with a microscope, so it is smaller than 0.1 mm (10⁻⁴ m).", "An atom is about 10⁻¹⁰ m; a bacterium is much larger than an atom.",
                "Pick the power of ten between those two."]),
    dict(id="o26s_instruments_pair", chapter=1, level=2, lo="1e", source="QTSS 2026 prelim MCQ 2 and XMSS 2024 prelim MCQ 1",
         stem="A student must measure the circumference of a round flask and the diameter of a thin copper wire. Which pair of instruments is most suitable?",
         correct="measuring tape for the circumference; digital micrometer for the wire",
         wrongs={"digital calipers for the circumference; digital micrometer for the wire": "Calipers measure a straight distance between their jaws; they cannot follow a curved circumference.",
                 "metre rule for the circumference; digital calipers for the wire": "A rigid rule cannot be wrapped round a flask, and calipers (0.01 mm) are less precise than a micrometer for a thin wire.",
                 "measuring tape for the circumference; metre rule for the wire": "A metre rule reads to 1 mm only: far too coarse for a wire a fraction of a millimetre thick."},
         hints=["A circumference is a curved length: which instrument bends?", "The wire is under a millimetre thick: which instrument reads to 0.001 mm?",
                "Match the instrument to both the shape and the size of what is measured."]),
    dict(id="o26s_vector_list", chapter=1, level=1, lo="1f", source="QTSS 2026 prelim MCQ 1 and HGV 2024 prelim MCQ 2",
         stem="Which list contains vector quantities only?",
         correct="displacement, weight, acceleration",
         wrongs={"energy, mass, acceleration": "Energy and mass have no direction: they are scalars.", "speed, force, time": "Speed and time are scalars; only force is a vector here.",
                 "distance, velocity, power": "Distance and power are scalars (distance has no direction; displacement does)."},
         hints=["A vector has a size AND a direction.", "Weight acts downwards, acceleration has a direction, displacement points from start to finish.",
                "Energy, mass, time, speed, distance and power have no direction."]),
], category=CAT)


@template("o26s_nano_atoms", chapter=1, level=3, lo="1c", category=CAT)
def nano_atoms(rng):
    n = nice(rng, 8, 5, 4, 20)
    d_m = 1e-9 / n
    d_um = d_m * 1e6
    correct = f"{sci(d_um, 2)} µm"
    wrongs = {f"{sci(d_um, 2)} mm": "That is 1000 times too big: 1 nm = 10⁻⁹ m = 10⁻⁶ mm, not 10⁻³ mm.",
              f"{sci(d_um, 2)} cm": "1 nm = 10⁻⁷ cm, so dividing by the number of atoms gives a smaller power of ten in cm.",
              f"{sci(d_um * 1e3, 2)} µm": "That forgets to divide by the number of atoms placed side by side in the 1 nm space."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"Nanotechnology works at the nanometre scale. In a space of **1 nanometre**, **{n} hydrogen atoms** fit side by side. "
                     "What is the approximate diameter of one hydrogen atom?",
                options=opts, key=key, misconceptions=mis, formula="1 nm = 10⁻⁹ m; 1 µm = 10⁻⁶ m",
                working=[f"Diameter = 1 nm ÷ {n} = {sci(d_m, 2)} m", f"= {sci(d_um, 2)} µm (since 1 µm = 10⁻⁶ m)", f"Correct answer: **{correct}**",
                         cite("ACSBR 2024 prelim MCQ 2")],
                hints=["nano = 10⁻⁹, micro = 10⁻⁶, milli = 10⁻³, centi = 10⁻².", f"Divide 1 nm by {n} to get the diameter of one atom in metres.",
                       "Change metres into micrometres: multiply by 10⁶."])


explain_mcqs([
    dict(id="o26s_balance_two_forces", chapter=1, level=3, lo="1g", source="NAS 2025 prelim MCQ 2",
         stem="Fig. 1 shows two forces acting at a point O. A third force is to be added so that the point is in equilibrium. Which force is needed?",
         correct="a force equal in size to the resultant of the two forces, in the opposite direction to that resultant",
         wrongs={"a force equal in size to the resultant of the two forces, in the same direction as that resultant": "Adding a force along the resultant doubles the unbalance; the third force must CANCEL the resultant.",
                 "a force equal in size to the larger of the two forces, opposite to it": "That cancels only one force and leaves the other acting: not equilibrium.",
                 "a force equal to the sum of the two sizes, pointing between them": "Forces add as vectors (parallelogram or tip-to-tail), not by adding their sizes."},
         hints=["First find the resultant of the two forces with a parallelogram or tip-to-tail drawing.", "In equilibrium the total force is zero.",
                "What single force added to the resultant gives zero?"],
         figure=lambda: figs2.vector_pair("6 N", "8 N", 60)),
], category=CAT)


# ================================================================== Ch 2 Kinematics
explain_mcqs([
    dict(id="o26s_speed_vs_velocity", chapter=2, level=2, lo="2a", source="PRSS 2024 prelim (5086) MCQ 2",
         stem="A car goes round a circular track at a steady 20 m/s. Which statement is correct?",
         correct="Its speed is constant but its velocity is changing, because its direction keeps changing.",
         wrongs={"Its speed and its velocity are both constant.": "Velocity is speed in a stated direction. On a circle the direction changes all the time, so the velocity changes.",
                 "Its velocity is constant but its speed is changing.": "The speedometer reads a steady 20 m/s, so the speed is constant; it is the velocity (which includes direction) that changes.",
                 "Its speed and its velocity are both changing.": "The size of the velocity, 20 m/s, is the speed, and that is constant."},
         hints=["Speed is a scalar: size only. Velocity is a vector: size and direction.", "Does the car's direction change as it goes round?",
                "A changing direction means a changing velocity even at steady speed."]),
    dict(id="o26s_free_fall_pq", chapter=2, level=1, lo="2i", source="XMSS 2024 prelim MCQ 6",
         stem="A mango falls freely from a tree. P is the point where it starts to fall and Q is just before it hits the ground. Air resistance is negligible. "
              "What is its acceleration at P and at Q?",
         correct="10 m/s² at P and 10 m/s² at Q",
         wrongs={"0 at P and 10 m/s² at Q": "At P the mango is momentarily at rest, but gravity already acts on it: its acceleration is 10 m/s² from the first instant.",
                 "10 m/s² at P and 0 at Q": "The acceleration of free fall is constant; the mango does not stop accelerating just because it is near the ground.",
                 "0 at P and 0 at Q": "The mango speeds up as it falls, so its acceleration is not zero."},
         hints=["Acceleration is the rate of change of velocity, not the velocity itself.", "Near the Earth the acceleration of free fall is constant.",
                "Being at rest for an instant (at P) does not mean zero acceleration."]),
], category=CAT)


@template("o26s_average_speed_graph", chapter=2, level=3, lo="2b", category=CAT)
def average_speed_graph(rng):
    d1, t1, t2, d2, t3 = nice(rng, (6.0, 4, 6, 10.0, 8), (8.0, 4, 6, 14.0, 10), (5.0, 2, 5, 12.0, 8), (9.0, 3, 5, 15.0, 10))
    v = d2 / t3
    return calc_q(rng, "Fig. 1 shows how the displacement of a toy car varies with time along a straight track. What is the average speed of the car over the whole journey?", v,
                  [(d1 / t1, "That is the speed of the FIRST section only. Average speed uses the total distance and the total time, including the stop."),
                   ((d2 - d1) / (t3 - t2), "That is the speed of the LAST section only."),
                   (d2 / (t3 - (t2 - t1)), "The time the car was stationary still counts in the total time.")],
                  "m/s", "average speed = total distance / total time",
                  [f"Total distance = {fmt(d2)} m; total time = {t3} s (including the {t2 - t1} s at rest)", f"average speed = {fmt(d2)} / {t3} = **{fmt(v)} m/s**",
                   cite("ACSBR 2024 prelim MCQ 3")],
                  ["Average speed is not the average of the speeds.", "Read the total distance at the end and the total time at the end.", "Divide one by the other."],
                  figure=figs.graph([(0, 0), (t1, d1), (t2, d1), (t3, d2)], t3, math.ceil(d2 / 2) * 2 + 2, 2, 2, xlabel="time / s", ylabel="displacement / m"))


@template("o26s_car_reach_speed", chapter=2, level=3, lo="2c", category=CAT)
def car_reach_speed(rng):
    m, F, v = nice(rng, (800, 2400, 24.0), (900, 2700, 21.0), (1200, 3000, 25.0), (750, 3000, 30.0))
    a = F / m
    t = v / a
    return calc_q(rng, f"A car of mass **{m} kg** starts from rest on a level road. Friction is negligible and the driving force is **{F} N**. "
                  f"How long does the car take to reach **{fmt(v)} m/s**?", t,
                  [(v / a / 2, "Halving the time is wrong: t = v / a with v the final velocity."),
                   (v * a, "That multiplies velocity by acceleration. Rearrange a = (v − u) / t to get t = v / a."),
                   (F / v, "Force ÷ velocity is not a time. Find the acceleration first (F = m a), then the time.")],
                  "s", "a = F / m; a = (v − u) / t ⇒ t = v / a",
                  [f"a = F / m = {F} / {m} = {fmt(a)} m/s²", f"t = (v − u) / a = ({fmt(v)} − 0) / {fmt(a)} = **{fmt(t)} s**", cite("HGV 2024 prelim MCQ 9")],
                  ["Newton's second law gives the acceleration: a = F / m.", "Acceleration = change in velocity ÷ time.", "The car starts from rest, so the change in velocity is the final velocity."])


explain_mcqs([
    dict(id="o26s_decreasing_accel_vt", chapter=2, level=3, lo="2d", source="NAS 2025 prelim MCQ 4 and QTSS 2026 prelim MCQ 3",
         stem="Fig. 1 is the velocity-time graph of a skydiver before the parachute opens. Which statement describes the motion?",
         correct="The velocity increases while the acceleration decreases.",
         wrongs={"The velocity increases at a constant rate.": "A constant rate of increase would be a straight line. This line curves, getting less steep.",
                 "The velocity and the acceleration both decrease.": "The graph still rises, so the velocity is increasing; only its gradient (the acceleration) is falling.",
                 "The velocity is constant and the acceleration is zero.": "Only the final part is level. Before that the velocity is still rising."},
         hints=["On a velocity-time graph the gradient is the acceleration.", "Is the line getting steeper or less steep as time goes on?",
                "The curve rising but flattening means a positive acceleration that is shrinking."],
         figure=lambda: figs.graph([(t, 50 * (1 - math.exp(-t / 4))) for t in range(0, 17)], 16, 60, 2, 10, xlabel="time / s", ylabel="velocity / m/s")),
    dict(id="o26s_dt_curve_then_flat", chapter=2, level=3, lo="2e", source="HGV 2024 prelim MCQ 3",
         stem="Fig. 1 is the displacement-time graph of a lift. Which statement describes the motion?",
         correct="The lift moves with increasing velocity, then stops.",
         wrongs={"The lift moves with decreasing velocity, then stops.": "The gradient of the curve gets STEEPER before the flat part, so the velocity was increasing.",
                 "The lift moves with increasing velocity, then at a constant velocity.": "The final part is horizontal: the displacement is not changing, so the lift is at rest.",
                 "The lift accelerates throughout.": "In the horizontal section the displacement is constant: the lift is stationary, not accelerating."},
         hints=["On a displacement-time graph the gradient is the velocity.", "A curve that gets steeper means the velocity is increasing.",
                "A horizontal line means zero velocity: at rest."],
         figure=lambda: figs.graph([(t, 0.5 * t * t) for t in range(0, 7)] + [(8, 18), (10, 18)], 10, 20, 2, 5, xlabel="time / s", ylabel="displacement / m")),
    dict(id="o26s_stone_up_cliff_vt", chapter=2, level=4, lo="2g", source="HGV 2024 prelim MCQ 4",
         stem="A stone is thrown vertically upwards from the top of a cliff. Taking upwards as positive, its velocity is recorded:\n\n"
              + md_table(["time / s", "0", "1.0", "2.0", "3.0", "4.0"], [["velocity / m/s", "+10", "0", "−10", "−20", "−30"]])
              + "\n\nIt reaches the bottom of the cliff at 4.0 s. Which statement about the motion is correct?",
         correct="The acceleration is 10 m/s² downwards throughout, and the stone is at its highest point at 1.0 s.",
         wrongs={"The acceleration is zero at 1.0 s, when the velocity is zero.": "The velocity is momentarily zero at the top, but it is still CHANGING by 10 m/s every second: the acceleration stays 10 m/s².",
                 "The acceleration is 10 m/s² upwards while the stone rises and 10 m/s² downwards while it falls.": "Gravity always acts downwards, so the acceleration is downwards the whole time; rising just means the velocity is upwards.",
                 "The stone is at its highest point at 2.0 s, when the velocity is −10 m/s.": "At the highest point the velocity is zero, which happens at 1.0 s. At 2.0 s the stone is already falling."},
         hints=["Acceleration = change in velocity ÷ time. How much does the velocity change each second?", "The velocity changes by the same amount every second, in the same sense.",
                "At the highest point the stone is momentarily at rest: find when v = 0."]),
], category=CAT)


# ================================================================== Ch 3 Dynamics
explain_mcqs([
    dict(id="o26s_contact_forces_ramp", chapter=3, level=2, lo="3a", source="QTSS 2026 prelim MCQ 4",
         stem="A block rests on a rough sloping ramp. Three forces act on it: its weight W, the friction F from the ramp and the normal force N from the ramp. "
              "Which of these are contact forces?",
         correct="F and N only",
         wrongs={"W only": "Weight is the gravitational pull of the Earth: it acts without touching, so it is a NON-contact force.",
                 "W, F and N": "Weight needs no contact; the Earth pulls the block from a distance.",
                 "N only": "Friction also acts where the two surfaces touch, so it is a contact force too."},
         hints=["A contact force acts only where two objects touch.", "Which force would still act if the ramp were removed and the block fell?",
                "Friction and the normal force both come from the ramp's surface."]),
    dict(id="o26s_mass_statement", chapter=3, level=1, lo="3b", source="SEAB O-Level (5076) 2016 MCQ 4",
         stem="Which statement about the mass of a body is **not** correct?",
         correct="Its mass becomes smaller when it is taken to the Moon.",
         wrongs={"Its mass is a measure of the amount of matter in it.": "That IS the definition of mass, so the statement is correct.",
                 "Its mass is measured in kilograms.": "Correct: the kilogram is the SI base unit of mass.",
                 "Its mass is the same everywhere.": "Correct: the amount of matter does not change from place to place; only the weight changes."},
         hints=["Mass is the amount of matter in a body.", "Does the amount of matter change when the body is moved?", "The quantity that changes on the Moon is the weight."]),
    dict(id="o26s_grav_field_region", chapter=3, level=1, lo="3c", source="SEAB O-Level (5076) 2018 MCQ 5",
         stem="A gravitational field is a region in which a mass experiences a force. Which statement about this force is correct?",
         correct="It acts on the mass even when the mass is not touching anything.",
         wrongs={"It acts only when the mass is resting on a surface.": "Gravity pulls a falling object too; it is a non-contact force.",
                 "It acts only on masses that are moving.": "A stationary book on a table still has weight: the field acts whether or not the mass moves.",
                 "It pushes the mass away from the Earth.": "Gravitational force is always attractive: it pulls masses together."},
         hints=["Gravitational force is a non-contact force.", "Think of a ball in mid-air: is gravity acting?", "Which direction does gravity act: towards or away from the Earth?"]),
    dict(id="o26s_moon_mass_weight", chapter=3, level=2, lo="3e", source="Punggol 2024 prelim MCQ 5",
         stem="A probe is taken from the Earth to Mars, where the gravitational field strength is about 0.4 of the Earth's. How do its mass and weight on Mars compare with those on the Earth?",
         correct="same mass; weight about 0.4 times",
         wrongs={"mass about 0.4 times; weight about 0.4 times": "Mass is the amount of matter in the probe: it does not change with location.",
                 "same mass; same weight": "Weight = m g, and g on Mars is smaller, so the weight is smaller.",
                 "mass about 0.4 times; same weight": "It is the other way round: mass stays the same, weight falls with g."},
         hints=["W = m g.", "Which of m and g changes when you go to Mars?", "The quantity that changes in proportion to g is the weight."]),
    dict(id="o26s_coin_falls_forces", chapter=3, level=3, lo="3g", source="XMSS 2024 prelim MCQ 5",
         stem="A coin falls from rest through the air and eventually reaches a constant speed. Two forces act on it: its weight and the air resistance P. "
              "Before the coin reaches constant speed, what happens to P and to the resultant force?",
         correct="P increases; the resultant force decreases",
         wrongs={"P increases; the resultant force increases": "As P grows it cancels more of the weight, so the resultant (weight − P) gets SMALLER.",
                 "P decreases; the resultant force decreases": "Air resistance grows with speed, and the coin is speeding up, so P increases.",
                 "P stays the same; the resultant force stays the same": "Air resistance depends on speed; while the speed rises, so does P."},
         hints=["Air resistance increases as the speed increases.", "Resultant force = weight − air resistance.", "What happens to that difference as air resistance grows?"]),
    dict(id="o26s_action_reaction_weight", chapter=3, level=3, lo="3g", source="BRD 2024 prelim MCQ 5 and BGSS 2024 prelim MCQ 5",
         stem="A student sits on a bench. Two forces act on the student: the weight W and the normal contact force N from the bench. Which force forms an action-reaction pair with W?",
         correct="the gravitational force of the student on the Earth",
         wrongs={"the normal contact force N on the student by the bench": "W and N act on the SAME body (the student). An action-reaction pair acts on two different bodies and is of the same type.",
                 "the force of the student on the bench": "That is the partner of N (the contact pair), not of the weight.",
                 "the force of the bench on the Earth": "The bench pushing on the Earth is not the reaction to the Earth pulling on the student."},
         hints=["Action and reaction are the same TYPE of force, acting on two DIFFERENT bodies.", "W is the Earth pulling the student (gravitational).",
                "So the partner is the student pulling the Earth."]),
    dict(id="o26s_fbd_block_ramp", chapter=3, level=3, lo="3h", source="QTSS 2026 prelim MCQ 4",
         stem="A block of wood is at rest on a rough sloping ramp. Which free-body diagram of the block is correct?",
         correct="weight W vertically downwards, normal force N perpendicular to the ramp surface, friction F along the ramp pointing up the slope",
         wrongs={"weight W perpendicular to the ramp surface, normal force N vertically upwards, friction F down the slope": "Weight always acts vertically downwards, and the normal force is perpendicular to the surface, not vertical.",
                 "weight W vertically downwards, normal force N vertically upwards, friction F along the ramp pointing down the slope": "N is perpendicular to the ramp, not vertical, and friction opposes the tendency to slide (down the slope), so it points UP the slope.",
                 "weight W vertically downwards, normal force N perpendicular to the ramp, friction F along the ramp pointing down the slope": "The block would slide DOWN the ramp without friction, so friction acts UP the ramp."},
         hints=["Weight always acts vertically downwards towards the Earth's centre.", "A normal force is at right angles to the surface.",
                "Friction opposes the direction the block would slide."]),
    dict(id="o26s_tablecloth_inertia", chapter=3, level=2, lo="3k", source="NAS 2025 prelim MCQ 5",
         stem="Some plates rest on a tablecloth. The cloth is jerked swiftly off the table. The plates stay almost where they were. Which statement best explains this?",
         correct="The plates stay in place because of their inertia.",
         wrongs={"The plates move with the cloth because of friction.": "The plates do NOT move with the cloth; the brief friction from a fast jerk is too small to overcome their inertia.",
                 "The plates stay in place because of the pull of gravity.": "Gravity acts downwards; it does not stop the plates sliding sideways. Their resistance to a change in motion is inertia.",
                 "The plates stay in place because they are heavier than the cloth.": "It is the plates' MASS (inertia) that resists the change in motion, not a comparison with the cloth's weight."},
         hints=["Inertia is the reluctance of a mass to change its state of motion.", "The plates are at rest and 'want' to stay at rest.",
                "A quick jerk gives friction almost no time to act on them."]),
    dict(id="o26s_friction_shoe", chapter=3, level=3, lo="3l", source="NAS 2025 prelim MCQ 7",
         stem="A sprinter's shoe pushes backwards on the track at the start of a race. In which direction does the frictional force of the track act on the shoe?",
         correct="forwards, in the direction the sprinter moves",
         wrongs={"backwards, opposite to the direction the sprinter moves": "Friction opposes the SLIDING of the shoe. The shoe pushes backwards, so friction on the shoe is forwards: that is what accelerates the sprinter.",
                 "vertically upwards": "The upward force on the shoe is the normal contact force, not friction.",
                 "vertically downwards": "No force from the track acts downwards on the shoe; friction acts along the surface."},
         hints=["Friction acts along the surface and opposes the relative sliding.", "Which way does the shoe push (or try to slide) on the track?",
                "Friction on the shoe is opposite to that push."]),
    dict(id="o26s_terminal_resultant", chapter=3, level=2, lo="3m", source="BGSS 2024 prelim MCQ 3 and NAS 2025 prelim MCQ 6",
         stem="A ball bearing is released in a tall jar of oil. It sinks and reaches terminal velocity. What is the resultant force on the ball while it moves at terminal velocity?",
         correct="zero",
         wrongs={"constant and downwards": "A constant downward resultant would keep the ball accelerating; at terminal velocity the velocity is constant.",
                 "decreasing": "The resultant decreases BEFORE terminal velocity, while the drag is still growing. At terminal velocity it has reached zero.",
                 "equal to the weight": "The weight is balanced by the upward drag (and upthrust), so the resultant is zero, not the weight."},
         hints=["Terminal velocity means a constant velocity.", "Constant velocity means zero acceleration.", "Newton's first law: zero acceleration means zero resultant force."]),
    dict(id="o26s_vacuum_vs_air_fall", chapter=3, level=4, lo="3m", source="Punggol 2024 prelim MCQ 4",
         stem="Two balls X and Y have the same size and shape but X has the larger mass. They are dropped together from a great height, first in a vacuum and then in air. "
              "Which row is correct?",
         correct="in a vacuum they land together; in air X lands first",
         wrongs={"in a vacuum X lands first; in air they land together": "In a vacuum there is no air resistance, so both accelerate at g and land together.",
                 "they land together in both cases": "In air both feel the same drag at a given speed, but drag is a smaller fraction of X's larger weight, so X reaches a higher terminal velocity.",
                 "X lands first in both cases": "Without air there is nothing to slow either ball differently: both fall with the same acceleration."},
         hints=["In a vacuum every object has the same acceleration of free fall.", "In air, the drag on two objects of the same size and shape is the same at the same speed.",
                "Compare that drag with each ball's weight: which ball reaches a higher terminal velocity?"]),
], category=CAT)


@template("o26s_mars_weight", chapter=3, level=4, lo="3d", category=CAT)
def mars_weight(rng):
    m, u, t = nice(rng, (60, 8.0, 2.0), (70, 7.4, 2.0), (65, 9.0, 2.5), (80, 6.0, 1.5))
    g = u / t
    W = m * g
    return calc_q(rng, f"An astronaut of mass **{m} kg** lands on a planet. A stone thrown straight up at **{fmt(u)} m/s** takes **{fmt(t)} s** to reach its highest point. "
                  "What is the astronaut's weight on this planet?", W,
                  [(m * 10, "That uses the Earth's g. The stone's motion shows this planet's gravitational field strength is different."),
                   (m * g / 2, "g = u / t, not u / (2t): the stone loses its whole upward velocity in the time given."),
                   (m * u * t, "Multiplying mass by speed and time does not give a force. Find g (in N/kg) first.")],
                  "N", "g = Δv / t (free fall); W = m g (g in N/kg = m/s²)",
                  [f"The stone's velocity falls from {fmt(u)} m/s to 0 in {fmt(t)} s: g = {fmt(u)} / {fmt(t)} = {fmt(g)} m/s² = {fmt(g)} N/kg",
                   f"W = m g = {m} × {fmt(g)} = **{fmt(W)} N**", cite("HGV 2024 prelim MCQ 17")],
                  ["The stone decelerates at g until it stops at the top.", "g = change in velocity ÷ time, in m/s², which is the same as N/kg.",
                   "Gravitational field strength is the force per unit mass: W = m g."])


@template("o26s_three_force_tension", chapter=3, level=3, lo="3i", category=CAT)
def three_force_tension(rng):
    W, F = nice(rng, (40, 30), (30, 40), (60, 80), (80, 60), (24, 10))
    T = math.hypot(W, F)
    return calc_q(rng, f"A pendulum bob of weight **{W} N** hangs on a string. It is pulled sideways by a horizontal force of **{F} N** and held at rest. "
                  "Fig. 1 shows the three forces on the bob (weight, horizontal pull and the tension T in the string), which are in equilibrium. What is the tension T?", T,
                  [(W + F, "The forces are at right angles, so they do not simply add. Draw the vector triangle: T is the hypotenuse."),
                   (abs(W - F), "Subtracting treats the forces as if they were along one line. They are perpendicular."),
                   (max(W, F), "The tension must balance BOTH the weight and the horizontal pull, so it is larger than either.")],
                  "N", "closed vector triangle: T² = W² + F² (weight and pull are perpendicular)",
                  [f"Weight (down) and pull (horizontal) are at right angles; the tension closes the triangle.", f"T = √({W}² + {F}²) = **{fmt(T)} N**",
                   cite("HGV 2024 prelim MCQ 6")],
                  ["Three forces in equilibrium form a closed triangle when drawn tip to tail.", "The weight is vertical and the pull horizontal: a right-angled triangle.",
                   "The tension is the hypotenuse: use Pythagoras (or a scale drawing)."],
                  figure=figs.force_diagram([(f"{W} N", "down", 1.2), (f"{F} N", "left", 1.0), ("T", math.degrees(math.atan2(W, F)), 1.4)],
                                            label_body="bob", ground=False))


# ================================================================== Ch 4 Turning effects
@template("o26s_lift_bar_end", chapter=4, level=3, lo="4b", category=CAT)
def lift_bar_end(rng):
    m = nice(rng, 30, 24, 36, 40)
    W = m * 10
    F = W / 2
    return calc_q(rng, f"A uniform metal bar of mass **{m} kg** lies on the ground. A student pulls straight up on one end with a force F so that the bar pivots about the other end. "
                  "What is the value of F when the lifted end just leaves the ground?", F,
                  [(W, "That is the whole weight. The bar's weight acts at its centre, half as far from the pivot as F, so F needs only half the weight."),
                   (W / 4, "The weight acts at the mid-point, at HALF the distance of F from the pivot, not a quarter."),
                   (m / 2, "That halves the mass in kg. Convert to weight (× 10 N/kg) first.")],
                  "N", "principle of moments about the pivot end: F × L = W × L/2",
                  [f"W = {m} × 10 = {W} N, acting at the centre of the bar (L/2 from the pivot).", f"F × L = {W} × L/2 ⇒ F = **{fmt(F)} N**", cite("XMSS 2024 prelim MCQ 8")],
                  ["The weight of a uniform bar acts at its mid-point.", "Take moments about the end on the ground.", "F acts at distance L; the weight acts at L/2."])


explain_mcqs([
    dict(id="o26s_equilibrium_conditions", chapter=4, level=1, lo="4c", source="SEAB 5086 specimen paper 2024 MCQ 4",
         stem="A beam is in equilibrium under several forces. Which statement must be true?",
         correct="The resultant force is zero, and the total clockwise moment about any pivot equals the total anticlockwise moment about that pivot.",
         wrongs={"The resultant force is zero; the moments need not balance.": "With unbalanced moments the beam would start to rotate: not equilibrium.",
                 "The moments balance; the resultant force need not be zero.": "With a resultant force the beam would accelerate in a straight line: not equilibrium.",
                 "All the forces must be equal in size.": "The forces can be different sizes; what matters is that they and their moments cancel out."},
         hints=["Equilibrium means no acceleration of any kind.", "No linear acceleration needs zero resultant force.", "No rotation needs the principle of moments to hold."]),
    dict(id="o26s_lamina_hole_cg", chapter=4, level=3, lo="4e", source="XMSS 2024 prelim MCQ 9",
         stem="A uniform circular card has a hole cut out near its right-hand edge. Where is the centre of gravity of the card now?",
         correct="to the left of the centre of the circle, away from the hole",
         wrongs={"at the centre of the circle": "Removing material from the right shifts the balance point towards the heavier left side.",
                 "at the centre of the hole": "There is no card at the hole, and the remaining card is mostly on the other side.",
                 "to the right of the centre, towards the hole": "The side with the hole has LESS mass, so the centre of gravity moves away from it."},
         hints=["The centre of gravity is the point where the whole weight seems to act.", "Which side of the card now has more mass?",
                "The centre of gravity moves towards the side with more mass."]),
], category=CAT)


@template("o26s_rule_two_balances", chapter=4, level=5, lo="4d", category=CAT)
def rule_two_balances(rng):
    a, b = nice(rng, (10, 70), (20, 80), (10, 90), (30, 70))
    Wr, Wm = 2.0, 1.0
    R = (Wr + Wm) / 2
    # moments about support a: R (b - a) = Wr (50 - a) + Wm (x - a)
    x = a + (R * (b - a) - Wr * (50 - a)) / Wm
    return calc_q(rng, f"A uniform metre rule of weight **2.0 N** hangs horizontally from two identical spring balances attached at the **{a} cm** and **{b} cm** marks. "
                  "A **1.0 N** weight is hung on the rule so that the two balances read the same. At which mark is the weight hung?", x,
                  [(50, "At the 50 cm mark the weight sits with the rule's own weight; the balances would then share equally only if they were symmetrical about 50 cm."),
                   ((a + b) / 2, "The mid-point of the supports is where the COMBINED centre of gravity must be, not where the 1.0 N weight goes."),
                   (x + 10 if x + 10 <= 100 else x - 10, "Check the moment of the rule's own weight: it acts at the 50 cm mark, not at a support.")],
                  "cm mark", "equal readings ⇒ each balance = (2.0 + 1.0)/2; then take moments about one support",
                  [f"Each balance reads ({Wr} + {Wm}) / 2 = {R} N.",
                   f"Moments about the {a} cm support: {R} × {b - a} = {Wr} × {50 - a} + {Wm} × (x − {a})  ⇒  x = **{fmt(x)} cm**", cite("HGV 2024 prelim MCQ 11")],
                  ["Equal readings: the two balances share the total weight equally.", "The rule's own weight acts at the 50 cm mark.",
                   "Take moments about one of the supports and solve for the position."],
                  sf=3)


# ================================================================== Ch 5 Pressure
explain_mcqs([
    dict(id="o26s_tiles_force_pressure", chapter=5, level=2, lo="5a", source="BGSS 2024 prelim MCQ 11",
         stem="Two identical heavy stone slabs rest on soft ground, one standing on its edge and the other lying flat. How do the force and the pressure they exert on the ground compare?",
         correct="same force; different pressure",
         wrongs={"same force; same pressure": "Pressure = force ÷ area. The same weight on a smaller area gives a LARGER pressure.",
                 "different force; same pressure": "The force on the ground is each slab's weight, and the slabs are identical.",
                 "different force; different pressure": "The weights are equal, so the forces are equal; only the contact areas differ."},
         hints=["The force on the ground is the weight of the slab.", "Pressure is force per unit area.", "Which slab has the smaller area in contact with the ground?"]),
    dict(id="o26s_hydraulic_statement", chapter=5, level=2, lo="5c", source="HGV 2024 prelim MCQ 13",
         stem="Fig. 1 shows a simple hydraulic lift: a small force F on the narrow piston P supports a heavy load on the wide piston Q. Which statement is correct?",
         correct="The pressure on piston P equals the pressure on piston Q.",
         wrongs={"Force F is larger than the weight of the load.": "F is SMALLER: the same pressure on a larger area gives a larger force at Q.",
                 "Force F equals the weight of the load.": "The forces differ because the areas differ; it is the pressures that are equal.",
                 "The pressure on piston P is smaller than the pressure on piston Q.": "Pressure is transmitted equally throughout the enclosed liquid."},
         hints=["In an enclosed liquid, pressure is transmitted equally to every part.", "p = F / A on each piston.", "Equal pressure with a bigger area means a bigger force."],
         figure=lambda: figs2.hydraulic_press("F", "small area", "large area", "load")),
    dict(id="o26s_barometer_xy", chapter=5, level=3, lo="5f", source="HGV 2024 prelim MCQ 14",
         stem="Fig. 1 shows a simple mercury barometer. X is a point in the mercury near the bottom of the tube and Y is in the space above the mercury column. "
              "The atmospheric pressure falls. What happens to the pressure at X and at Y?",
         correct="pressure at X decreases; pressure at Y stays the same",
         wrongs={"pressure at X stays the same; pressure at Y decreases": "Y is a vacuum: its pressure is zero and stays zero. X is below the surface, where the pressure follows the atmosphere.",
                 "both decrease": "The space Y is a vacuum, so there is nothing there whose pressure can fall.",
                 "both stay the same": "The mercury column falls when the atmospheric pressure falls, so the pressure at X, which is atmospheric pressure plus the small depth below the surface, falls too."},
         hints=["What is in the space at the top of a barometer tube?", "The pressure at the open surface of the dish is atmospheric pressure.",
                "The pressure at X is set by the atmosphere pushing on the dish plus the small depth of mercury above X."],
         figure=lambda: figs2.barometer("h", liquid="mercury")),
], category=CAT)


@template("o26s_manometer_gas", chapter=5, level=3, lo="5g", category=CAT)
def manometer_gas(rng):
    atm, h = nice(rng, (756, 58), (760, 42), (752, 64), (758, 36))
    P = atm + h
    return calc_q(rng, f"Fig. 1 shows a mercury manometer. The right-hand arm is open to the atmosphere and the left-hand arm is connected to a container of gas. "
                  f"The mercury in the open arm stands **{h} mm** higher than in the gas arm. Atmospheric pressure is **{atm} mm Hg**. What is the pressure of the gas?", P,
                  [(atm - h, "The open side is HIGHER, so the gas pushes the mercury down on its side: the gas pressure is greater than atmospheric, so ADD h."),
                   (h, "The height difference is the EXCESS of the gas pressure over atmospheric, not the gas pressure itself."),
                   (atm + 2 * h, "Use the difference in levels once; it is already the full height difference between the two arms.")],
                  "mm Hg", "gas pressure = atmospheric pressure ± h (plus when the open arm is higher)",
                  [f"The mercury is pushed down on the gas side, so p_gas > p_atm.", f"p_gas = {atm} + {h} = **{P} mm Hg**", cite("QTSS 2026 prelim MCQ 5")],
                  ["Which side has the higher mercury level? The gas pushes the mercury away from itself.", "A higher level on the open side means the gas pressure is above atmospheric.",
                   "Gas pressure = atmospheric pressure + the height difference (in mm Hg)."],
                  figure=figs2.manometer(f"{h} mm", gas_label="gas", left_higher=False))


# ================================================================== Ch 6 Energy
@template("o26s_gpe_ke_ratio", chapter=6, level=3, lo="6b", category=CAT)
def gpe_ke_ratio(rng):
    H, h = nice(rng, (80, 20), (60, 15), (100, 25), (90, 30))
    gpe, ke = h, H - h
    g = math.gcd(gpe, ke)
    correct = f"{gpe // g} : {ke // g}"
    wrongs = {f"{ke // g} : {gpe // g}": "That is the ratio the other way round: GPE is proportional to the height ABOVE the ground, which is now small.",
              f"{h} : {H}": "That compares the remaining height with the full height, which is GPE : total energy, not GPE : KE.",
              f"{H - h} : {H}": "That is KE : total energy. The question asks for GPE : KE."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A ball is dropped from a height of **{H} m**. Air resistance is negligible. When the ball is **{h} m** above the ground, what is the ratio of the energy "
                     "in its gravitational potential store to the energy in its kinetic store?",
                options=opts, key=key, misconceptions=mis, formula="GPE ∝ height above ground; KE = GPE lost = m g (H − h)",
                working=[f"GPE at {h} m = m g × {h}; KE = GPE lost = m g × ({H} − {h}) = m g × {H - h}.", f"GPE : KE = {h} : {H - h} = **{correct}**",
                         cite("HGV 2024 prelim MCQ 7")],
                hints=["The GPE left is proportional to the height still above the ground.", "The KE gained equals the GPE lost from the start (no air resistance).",
                       f"Compare {h} m with ({H} − {h}) m."])


@template("o26s_ball_ke_friction", chapter=6, level=4, lo="6c", category=CAT)
def ball_ke_friction(rng):
    m, h, v, Wf = nice(rng, (0.40, 2.0, 3.0, 1.8), (0.50, 2.0, 2.0, 1.5), (0.40, 3.0, 2.0, 2.4), (0.60, 1.5, 3.0, 2.1))
    ke0 = 0.5 * m * v * v
    gpe = m * 10 * h
    ke = ke0 + gpe - Wf
    return calc_q(rng, f"A ball of mass **{fmt(m)} kg** rolls down a slope. When it is **{fmt(h)} m** above the bottom its speed is **{fmt(v)} m/s**. "
                  f"The work done against friction on the way down is **{fmt(Wf)} J**. What is the kinetic energy of the ball at the bottom?", ke,
                  [(ke0 + gpe, "That ignores the energy transferred to the internal store by friction."),
                   (gpe - Wf, "The ball already had kinetic energy at the start; add ½ m v²."),
                   (ke0 + gpe + Wf, "Friction REMOVES energy from the ball's stores; subtract the work done against it.")],
                  "J", "KE at bottom = initial KE + GPE lost − work done against friction",
                  [f"Initial KE = ½ × {fmt(m)} × {fmt(v)}² = {fmt(ke0)} J; GPE lost = {fmt(m)} × 10 × {fmt(h)} = {fmt(gpe)} J",
                   f"KE at bottom = {fmt(ke0)} + {fmt(gpe)} − {fmt(Wf)} = **{fmt(ke)} J**", cite("XMSS 2024 prelim MCQ 14")],
                  ["Energy is conserved: add up what the ball has at the start.", "Its gravitational potential energy becomes kinetic energy as it descends.",
                   "Friction transfers some of that energy to the surroundings: subtract it."])


@template("o26s_ramp_friction_work", chapter=6, level=4, lo="6d", category=CAT)
def ramp_friction_work(rng):
    W, F, L, h = nice(rng, (50, 60, 10, 4.0), (40, 50, 8.0, 3.0), (60, 75, 10, 5.0), (80, 90, 12, 6.0))
    f = (F * L - W * h) / L
    return calc_q(rng, f"A box of weight **{W} N** is pulled at constant velocity from the bottom to the top of a ramp by a force of **{F} N** acting along the ramp. "
                  f"The ramp is **{fmt(L)} m** long and its top is **{fmt(h)} m** above the bottom. What is the size of the friction along the ramp?", f,
                  [(F - W, "The weight does not act along the ramp, so it cannot be subtracted from the pull directly. Use work done."),
                   (F * L - W * h, "That is the WORK done against friction in joules. Divide by the ramp length to get the force."),
                   (W * h / L, "That is the component of the weight along the ramp, which the pull must overcome IN ADDITION to friction.")],
                  "N", "work by pull = gain in GPE + work against friction: F L = W h + f L",
                  [f"Work done by the pull = {F} × {fmt(L)} = {fmt(F * L)} J; GPE gained = {W} × {fmt(h)} = {fmt(W * h)} J",
                   f"Work against friction = {fmt(F * L)} − {fmt(W * h)} = {fmt(F * L - W * h)} J; friction = {fmt(F * L - W * h)} / {fmt(L)} = **{fmt(f)} N**",
                   cite("NAS 2025 prelim MCQ 10")],
                  ["Constant velocity: all the work done by the pull goes into GPE and heat from friction.", "Work done by the pull = force × distance along the ramp.",
                   "Work against friction = friction × distance along the ramp."])


@template("o26s_solar_efficiency", chapter=6, level=3, lo="6f", category=CAT)
def solar_efficiency(rng):
    A, Pout, S = nice(rng, (7.2, 1.0, 800), (6.0, 0.90, 750), (8.0, 1.2, 800), (5.0, 0.80, 900))
    Pin = A * S
    eff = Pout * 1000 / Pin * 100
    return calc_q(rng, f"Solar panels of total area **{fmt(A)} m²** produce **{fmt(Pout)} kW** of electrical power. Each square metre receives **{S} J** of energy from the Sun every second. "
                  "What is the efficiency of the panels?", eff,
                  [(Pout * 1000 / S, "That divides by the energy on ONE square metre. The panels receive S × area joules every second."),
                   (Pout / S * 100, "The output is in kW: change it to W (× 1000) before comparing with the input in J/s."),
                   (Pin / (Pout * 1000), "That is input ÷ output. Efficiency = useful output ÷ total input.")],
                  "%", "efficiency = useful power output / total power input × 100%",
                  [f"Power input = {S} × {fmt(A)} = {fmt(Pin)} W; output = {fmt(Pout * 1000)} W", f"efficiency = {fmt(Pout * 1000)} / {fmt(Pin)} × 100% = **{fmt(eff)} %**",
                   cite("QTSS 2026 prelim MCQ 9")],
                  ["J per second is W: the input power per square metre.", "Total input = input per square metre × area.", "Efficiency = output ÷ input × 100%."], sf=3)


@template("o26s_motor_efficiency", chapter=6, level=4, lo="6f", category=CAT)
def motor_efficiency(rng):
    m, P, t, v = nice(rng, (1000, 200, 20, 2.0), (800, 250, 16, 2.5), (1200, 300, 20, 2.0), (500, 150, 10, 2.0))
    ke = 0.5 * m * v * v
    Ein = P * t
    eff = ke / Ein * 100
    return calc_q(rng, f"A winch motor with a power input of **{P} W** pulls a stationary car of mass **{m} kg** along level ground. After **{t} s** the car is moving at **{fmt(v)} m/s**. "
                  "What is the efficiency of the motor?", eff,
                  [(m * v / Ein * 100, "Kinetic energy is ½ m v², not m v."),
                   (ke / P * 100, "The input ENERGY is power × time, not the power alone."),
                   (Ein / ke, "That is input ÷ output. Efficiency = useful output ÷ input.")],
                  "%", "efficiency = KE gained / (P × t) × 100%",
                  [f"Useful output = KE = ½ × {m} × {fmt(v)}² = {fmt(ke)} J; input = {P} × {t} = {fmt(Ein)} J",
                   f"efficiency = {fmt(ke)} / {fmt(Ein)} × 100% = **{fmt(eff)} %**", cite("NAS 2025 prelim MCQ 11")],
                  ["Energy input = power × time.", "Useful output is the kinetic energy the car gains: ½ m v².", "Efficiency = useful output ÷ total input × 100%."], sf=2)


explain_mcqs([
    dict(id="o26s_renewable_count", chapter=6, level=2, lo="6g", source="BRD 2024 prelim MCQ 12",
         stem="Here are seven energy resources: biofuels, geothermal energy, nuclear fuel, tides, fossil fuels, hydroelectric power, wind. How many of them are renewable?",
         correct="5",
         wrongs={"4": "Biofuels, geothermal, tides, hydroelectric and wind are ALL renewable: that makes five.",
                 "6": "Nuclear fuel (uranium) is not replaced as it is used, so it is non-renewable, like fossil fuels.",
                 "3": "Tides and geothermal energy are renewable as well as wind, hydroelectric and biofuels."},
         hints=["A renewable resource is replaced naturally as fast as it is used.", "Fossil fuels and nuclear fuel are mined and used up.",
                "Count the others."]),
], category=CAT)


# ================================================================== Ch 7 Kinetic particle model
explain_mcqs([
    dict(id="o26s_liquid_description", chapter=7, level=1, lo="7a", source="BRD 2024 prelim MCQ 16",
         stem="Which description fits a substance in the liquid state?",
         correct="It has a fixed volume, and its particles move around freely and randomly.",
         wrongs={"It has no fixed volume, and its particles move very fast with large spaces between them.": "No fixed volume describes a GAS.",
                 "It has a fixed volume, and its particles are arranged in a regular pattern.": "A regular arrangement describes a SOLID.",
                 "It has a fixed volume, and its particles only vibrate about fixed positions.": "Particles vibrating about fixed positions describes a solid; liquid particles can slide past one another."},
         hints=["A liquid cannot be compressed much: fixed volume.", "A liquid can be poured: its particles are not held in fixed positions.",
                "Pick the row with both properties."]),
    dict(id="o26s_brownian_cause", chapter=7, level=2, lo="7c", source="QTSS 2026 prelim MCQ 12 and NAS 2025 prelim MCQ 13",
         stem="Pollen grains suspended in water are viewed through a microscope. The water is at a steady temperature, yet the grains are seen to jerk about at random. What causes this motion?",
         correct="water molecules bombarding the pollen grains unevenly from different directions",
         wrongs={"convection currents in the water": "The water is at a uniform temperature, so there are no convection currents.",
                 "the pollen grains colliding with one another": "The grains are far apart; it is the invisible water molecules that hit them.",
                 "evaporation of water near the grains": "Evaporation at the surface does not jerk grains inside the water about at random."},
         hints=["This is Brownian motion.", "What is in the water that you cannot see through the microscope?",
                "The random motion of the grains is evidence of the random motion of those molecules."]),
    dict(id="o26s_gas_heated_ke_pe", chapter=7, level=3, lo="7d", source="NAS 2025 prelim MCQ 12",
         stem="A fixed mass of gas is trapped in a rigid metal cylinder. The cylinder is heated and the temperature of the gas rises. What happens to the average kinetic energy "
              "and the potential energy of the gas particles?",
         correct="kinetic energy increases; potential energy unchanged",
         wrongs={"kinetic energy increases; potential energy increases": "The cylinder is rigid, so the particles' average separation does not change; their potential energy stays the same.",
                 "kinetic energy unchanged; potential energy increases": "A rise in temperature IS a rise in the average kinetic energy of the particles.",
                 "kinetic energy decreases; potential energy increases": "Heating raises, not lowers, the average kinetic energy."},
         hints=["Temperature is a measure of the average kinetic energy of the particles.", "Potential energy depends on the separation of the particles.",
                "A rigid cylinder keeps the volume, and so the average separation, fixed."]),
], category=CAT)


# ================================================================== Ch 8 Thermal processes
explain_mcqs([
    dict(id="o26s_thermal_equilibrium_xyz", chapter=8, level=3, lo="8a", source="BRD 2024 prelim MCQ 17",
         stem="Solid X is in thermal equilibrium with solid Y. Solid Y is at the same temperature as solid Z. The three solids are different materials with different masses. Which statement is true?",
         correct="There is no net transfer of energy when X is placed in thermal contact with Z.",
         wrongs={"X and Y have the same specific heat capacity.": "Thermal equilibrium says the temperatures are equal; it says nothing about the materials' specific heat capacities.",
                 "Y and Z have the same internal energy.": "Internal energy depends on mass and material as well as temperature, so equal temperatures do not mean equal internal energy.",
                 "Y is not in thermal equilibrium with Z.": "Two bodies at the same temperature ARE in thermal equilibrium: no net energy flows between them."},
         hints=["Thermal equilibrium means the two bodies are at the same temperature.", "X, Y and Z are therefore all at the same temperature.",
                "Energy only flows by heating from a higher temperature to a lower one."]),
    dict(id="o26s_paper_copper_rod", chapter=8, level=3, lo="8b", source="NAS 2025 prelim MCQ 14 and BGSS 2024 prelim MCQ 17",
         stem="A sheet of paper is wrapped tightly round a thick copper rod and held in a candle flame. The paper does not catch fire, even after some time. Which statement best explains this?",
         correct="Copper is a good thermal conductor and transfers energy quickly away from the heated part of the paper.",
         wrongs={"Paper is a poor thermal conductor, so it cannot get hot.": "Paper alone in the flame burns at once; it is the copper underneath that keeps it cool.",
                 "Paper is a poor absorber of radiation.": "The flame heats the paper by direct contact, not mainly by radiation.",
                 "The candle flame is too cool to set paper alight.": "A candle flame readily burns paper on its own."},
         hints=["What is directly behind the heated paper?", "Metals conduct thermal energy quickly through their free electrons and lattice vibrations.",
                "Energy is carried away along the rod before the paper gets hot enough to burn."]),
    dict(id="o26s_conduction_mechanism", chapter=8, level=2, lo="8b", source="SHSS 2024 prelim MCQ 15",
         stem="One end of a copper bar is heated. How is thermal energy conducted along the bar?",
         correct="by the vibration of the copper atoms and the movement of free electrons along the bar",
         wrongs={"by the copper atoms moving from the hot end to the cold end": "In a solid the atoms stay in their lattice positions; they vibrate but do not travel.",
                 "by convection currents of copper inside the bar": "Convection needs a fluid that can flow. Copper is a solid.",
                 "by infrared radiation passing through the bar": "Radiation travels through transparent media and vacuum, not through an opaque metal bar."},
         hints=["Copper is a metal: it has free electrons.", "Atoms at the hot end vibrate more and pass the energy to their neighbours.",
                "Free electrons move through the metal and carry energy quickly."]),
    dict(id="o26s_campfire_children", chapter=8, level=3, lo="8d", source="XMSS 2024 prelim MCQ 17",
         stem="Two children warm their hands at a campfire, at the same distance from the flames. Child 1 holds her hands in front of the fire; child 2 holds his hands above it. "
              "How does the energy from the fire reach each child's hands?",
         correct="child 1: radiation only; child 2: convection and radiation",
         wrongs={"child 1: convection only; child 2: radiation only": "Hot air rises, so convection cannot reach hands held to the SIDE of the fire; those hands are warmed by radiation.",
                 "child 1: radiation only; child 2: convection only": "Radiation travels in all directions, so it reaches the hands above the fire as well.",
                 "both: convection and radiation": "Convection carries hot air upwards only, so it does not reach hands held beside the fire."},
         hints=["Infrared radiation travels out from the fire in every direction.", "Convection currents of hot air rise upwards only.",
                "Which child's hands are in the rising air?"]),
    dict(id="o26s_cups_coolest", chapter=8, level=2, lo="8d", source="SHSS 2024 prelim MCQ 16",
         stem="Four identical cups are filled with the same volume of water at 80 °C. Two have dull black outer surfaces and two are polished silver; two of each are left uncovered "
              "and the other two have lids. After 5 minutes in a cool room, which cup contains the coolest water?",
         correct="the dull black cup without a lid",
         wrongs={"the polished silver cup without a lid": "A polished silver surface is a poor emitter of radiation, so it loses energy more slowly than dull black.",
                 "the dull black cup with a lid": "The lid cuts down convection and evaporation from the surface, so this cup keeps its energy better than the open black cup.",
                 "the polished silver cup with a lid": "This cup loses energy most SLOWLY: a poor emitter and a lid."},
         hints=["Dull black surfaces are good emitters of infrared radiation.", "An open top lets warm air and vapour escape by convection and evaporation.",
                "The coolest cup loses energy by the most routes."]),
    dict(id="o26s_igloo_cold_sink", chapter=8, level=3, lo="8e", source="QTSS 2026 prelim MCQ 13",
         stem="An igloo's entrance tunnel is dug lower than the sleeping platform, forming a 'cold sink'. Which statement best describes how the cold sink helps keep the people inside warm?",
         correct="Cold air is denser and stays in the low cold sink, so it does not reach the sleeping platform.",
         wrongs={"Warm air in the cold sink expands, becomes denser and rises.": "Warm air that expands becomes LESS dense; and the cold sink holds cold air, not warm.",
                 "Warm air in the igloo is less dense, contracts and rises.": "Warm air expands rather than contracts; and this does not explain the purpose of the lower tunnel.",
                 "The cold air in the sink is heated by radiation from the Sun.": "The sink is inside, below the sleeping area; the point is that cold, dense air sinks and stays low."},
         hints=["Cold air is denser than warm air.", "Dense air sinks to the lowest part of a space.", "The sleeping platform is higher than the tunnel."]),
    dict(id="o26s_vacuum_flask", chapter=8, level=3, lo="8e", source="HGV 2024 prelim MCQ 20",
         stem="Three statements are made about a vacuum flask:\n\n1 The silvered surfaces reduce energy loss by radiation.\n\n2 The vacuum reduces energy loss by radiation.\n\n"
              "3 The stopper reduces energy loss by convection and evaporation.\n\nWhich statements are correct?",
         correct="1 and 3 only",
         wrongs={"1 and 2 only": "The vacuum stops CONDUCTION and CONVECTION (no particles); radiation crosses a vacuum easily, which is why the silvering is needed.",
                 "2 and 3 only": "The silvered surfaces do reduce radiation: shiny surfaces are poor emitters and good reflectors of infrared.",
                 "1, 2 and 3": "Statement 2 is wrong: a vacuum cannot stop radiation."},
         hints=["Radiation can travel through a vacuum; conduction and convection cannot.", "Shiny silver surfaces are poor emitters and absorbers of infrared.",
                "The stopper closes the top, where warm air and vapour would escape."]),
], category=CAT)


# ================================================================== Ch 9 Thermal properties
explain_mcqs([
    dict(id="o26s_liquid_heated_internal", chapter=9, level=2, lo="9a", source="XMSS 2024 prelim MCQ 18",
         stem="A liquid is heated and its temperature rises. Which statement about the particles of the liquid is correct?",
         correct="The average kinetic energy of the particles increases and the internal energy of the liquid increases.",
         wrongs={"The average kinetic energy increases but the internal energy stays constant.": "Internal energy is the total of the particles' kinetic and potential energies, so it rises when their kinetic energy rises.",
                 "The average kinetic energy stays constant but the internal energy increases.": "A temperature rise means the average kinetic energy of the particles has increased.",
                 "Both stay constant.": "Heating transfers energy INTO the liquid, raising its internal energy."},
         hints=["Internal energy = total kinetic energy + total potential energy of the particles.", "A rise in temperature means the particles' average kinetic energy rises.",
                "If the kinetic part goes up, what happens to the total?"]),
    dict(id="o26s_heat_capacity_blocks", chapter=9, level=4, lo="9b", source="SHSS 2024 prelim MCQ 18",
         stem="Two copper blocks P and Q are each given the same amount of thermal energy H. The mass of P is half the mass of Q, and the temperature rise of Q is half the "
              "temperature rise of P. Which statement is correct?",
         correct="The heat capacity of P is half the heat capacity of Q.",
         wrongs={"The heat capacity of P is twice the heat capacity of Q.": "Heat capacity = energy ÷ temperature rise. P's temperature rises MORE for the same energy, so its heat capacity is SMALLER.",
                 "The specific heat capacity of P is half that of Q.": "Both blocks are copper: the same material has the same specific heat capacity.",
                 "The specific heat capacity of P is twice that of Q.": "Specific heat capacity is a property of the material, and both are copper."},
         hints=["Heat capacity C = energy supplied ÷ temperature rise.", "Same energy, double the temperature rise means half the heat capacity.",
                "Specific heat capacity (per kg) depends only on the material."]),
    dict(id="o26s_latent_heat_definition", chapter=9, level=1, lo="9f", source="FHSS 2025 prelim Paper 2 Q9(a)",
         stem="Which statement correctly defines the specific latent heat of vaporisation of a substance?",
         correct="the energy needed to change unit mass of the substance from liquid to gas without a change in temperature",
         wrongs={"the energy needed to raise the temperature of unit mass of the substance by 1 °C": "That is the specific heat capacity, which involves a temperature change.",
                 "the energy needed to change unit mass of the substance from solid to liquid without a change in temperature": "That is the specific latent heat of FUSION (melting).",
                 "the energy needed to raise the temperature of the substance to its boiling point": "Latent heat is the energy for the change of state itself, AT the boiling point, with no temperature change."},
         hints=["'Latent' heat is energy taken in without any change of temperature.", "'Vaporisation' is the change from liquid to gas.",
                "'Specific' means per unit mass (per kg)."]),
    dict(id="o26s_latent_vs_shc", chapter=9, level=3, lo="9h", source="BGSS 2024 prelim MCQ 19",
         stem="Why is the specific latent heat of vaporisation of water much larger than the energy needed to raise 1 kg of water by 1 °C?",
         correct="Much more energy is needed to separate the molecules completely when the liquid becomes a gas than to make them move a little faster.",
         wrongs={"The water loses mass when it vaporises, so more energy is needed per kilogram.": "Mass is conserved in a change of state; the same molecules just spread out.",
                 "More energy is lost to the surroundings while the water boils.": "Energy losses to the surroundings are not part of the definition of latent heat.",
                 "Latent heat includes the energy needed to heat the water up to its boiling point.": "Latent heat is only the energy for the change of state at the boiling point; the heating beforehand is separate."},
         hints=["During boiling the temperature does not change: the energy is not raising the kinetic energy of the molecules.", "The energy goes into the potential energy of the molecules as they are pulled apart against attractive forces.",
                "Breaking the molecules completely apart takes far more energy than a small rise in their speed."]),
], category=CAT)


@template("o26s_heater_power_block", chapter=9, level=3, lo="9c", category=CAT)
def heater_power_block(rng):
    m, c, rate = nice(rng, (3.0, 620, 5.0), (2.0, 450, 6.0), (2.5, 900, 4.0), (4.0, 380, 3.0))
    P = m * c * rate / 60
    return calc_q(rng, f"A heater is embedded in a **{fmt(m)} kg** block of metal of specific heat capacity **{c} J/(kg °C)**. The temperature of the block rises by **{fmt(rate)} °C every minute**. "
                  "What is the power of the heater?", P,
                  [(m * c * rate, "That is the energy supplied per MINUTE. Power is energy per second: divide by 60."),
                   (c * rate / 60, "The mass has been left out: energy = m c Δθ."),
                   (m * c * rate * 60, "The rate is per minute, so divide by 60 to get per second, do not multiply.")],
                  "W", "E = m c Δθ per minute; P = E / 60 s",
                  [f"Energy each minute = {fmt(m)} × {c} × {fmt(rate)} = {fmt(m * c * rate)} J", f"P = {fmt(m * c * rate)} / 60 = **{fmt(P)} W**", cite("HGV 2024 prelim MCQ 22")],
                  ["Find the energy needed for one minute's temperature rise: m c Δθ.", "One minute is 60 seconds.", "Power = energy ÷ time in seconds."])


@template("o26s_cooling_curve_latent", chapter=9, level=4, lo="9i", category=CAT)
def cooling_curve_latent(rng):
    m, rate, plateau = nice(rng, (400, 8000, 6), (500, 6000, 10), (250, 5000, 8), (400, 9000, 4))
    L = rate * plateau / m
    t_melt = 4
    pts = [(0, 80), (t_melt, 60), (t_melt + plateau, 60), (t_melt + plateau + 4, 40)]
    return calc_q(rng, f"Fig. 1 is the cooling curve of **{m} g** of liquid wax that loses energy to the surroundings at a steady **{rate} J per minute**. "
                  "What is the specific latent heat of fusion of the wax?", L,
                  [(rate / m, "That uses one minute of energy only. Multiply the rate by the length of the flat section of the graph."),
                   (rate * plateau, "That is the total energy given out while freezing, in joules. Divide by the mass to get J/g."),
                   (rate * (t_melt + plateau) / m, "Only the FLAT part of the curve is the change of state; the sloping part before it is the liquid cooling.")],
                  "J/g", "L = (rate of energy loss × time of the flat section) / mass",
                  [f"The flat section (freezing at 60 °C) lasts {plateau} min: energy given out = {rate} × {plateau} = {fmt(rate * plateau)} J",
                   f"L = {fmt(rate * plateau)} / {m} = **{fmt(L)} J/g**", cite("QTSS 2026 prelim MCQ 15")],
                  ["During a change of state the temperature stays constant: find the flat part of the curve.", "Energy given out during freezing = rate × duration of the flat part.",
                   "Specific latent heat = energy ÷ mass."],
                  figure=figs2.temp_time_graph(pts, labels=None, xlabel="time / min", ymax=100, xstep=2))


# ================================================================== Ch 10 General wave properties
explain_mcqs([
    dict(id="o26s_wave_speed_meaning", chapter=10, level=2, lo="10a", source="XMSS 2024 prelim MCQ 21",
         stem="A ripple tank is used to study water waves. A wave crest is marked and watched. What is the speed of the wave?",
         correct="the distance travelled horizontally by the crest in one second",
         wrongs={"the distance travelled vertically by the crest in one second": "The water surface moves up and down, but the WAVE moves along the tank; the wave speed is the horizontal travel of the crest.",
                 "the number of crests passing a point in one second": "That is the frequency of the wave.",
                 "the time taken for a crest to make one complete vibration": "That is the period."},
         hints=["Wave speed is how fast the wave pattern travels along.", "Follow one crest: how far does it move along the tank each second?",
                "Frequency and period describe the vibration, not the travel."]),
    dict(id="o26s_wave_energy_not_matter", chapter=10, level=2, lo="10b", source="HYSS 2024 prelim (5086) MCQ 12",
         stem="A cork floats on a pond. A wave passes under it. The cork bobs up and down but does not travel along with the wave. What does this show about the wave?",
         correct="The wave transfers energy without transferring matter.",
         wrongs={"The wave transfers matter without transferring energy.": "The water (matter) stays where it is; what moves along is the energy that lifts the cork.",
                 "The wave transfers both energy and matter along the pond.": "If the water travelled with the wave, the cork would be carried along too.",
                 "The wave transfers neither energy nor matter.": "The cork gains energy to move up and down, so energy is being carried by the wave."},
         hints=["Does the water itself travel along the pond?", "The cork gains energy to move, so something is transferred.",
                "Waves carry energy; the medium's particles oscillate about fixed positions."]),
    dict(id="o26s_transverse_refracted", chapter=10, level=3, lo="10e", source="QTSS 2026 prelim MCQ 19",
         stem="Which example describes a **transverse** wave being **refracted**?",
         correct="light from an object entering a magnifying glass",
         wrongs={"infrared pulses travelling along an optical fibre": "Infrared is transverse, but in a fibre it is kept in by total internal REFLECTION, not refraction.",
                 "ultrasound being used to clean jewellery": "Ultrasound is a LONGITUDINAL wave, and cleaning involves vibration rather than refraction.",
                 "water waves bouncing off a barrier in a ripple tank": "Water waves are transverse, but bouncing off a barrier is REFLECTION."},
         hints=["Light and water waves are transverse; sound and ultrasound are longitudinal.", "Refraction is the change of direction when a wave passes into a different medium at an angle.",
                "Which option has a transverse wave passing into a new medium?"]),
    dict(id="o26s_sound_speeds_media", chapter=10, level=2, lo="10f", source="NAS 2025 prelim MCQ 20",
         stem="Sound needs a medium to travel through. Which row gives approximate speeds of sound in air, in water and in steel?",
         correct="air 330 m/s; water 1500 m/s; steel 6000 m/s",
         wrongs={"air 330 m/s; water 6000 m/s; steel 1500 m/s": "Sound travels fastest in solids, whose particles are closest together and most strongly bonded.",
                 "air 6000 m/s; water 1500 m/s; steel 330 m/s": "That is the order reversed: sound is SLOWEST in gases.",
                 "air 3 × 10⁸ m/s; water 1500 m/s; steel 6000 m/s": "3 × 10⁸ m/s is the speed of LIGHT, not sound."},
         hints=["Sound is passed on by particles colliding with their neighbours.", "The closer and more tightly bound the particles, the faster the sound.",
                "Order: gas slowest, liquid, solid fastest."]),
    dict(id="o26s_ultrasound_period", chapter=10, level=3, lo="10j", source="NAS 2025 prelim MCQ 21",
         stem="Which of these sounds is an example of ultrasound?",
         correct="a sound whose particles vibrate with a period of 4.0 µs",
         wrongs={"a sound of very low loudness": "Ultrasound is defined by frequency (above 20 kHz), not by how quiet it is.",
                 "a sound of frequency 12 kHz": "12 kHz is within the human hearing range (20 Hz to 20 kHz), so it is audible sound.",
                 "a sound of very large amplitude": "Amplitude sets loudness, not whether a sound is ultrasonic."},
         hints=["Ultrasound has a frequency above 20 000 Hz.", "frequency = 1 / period.", "1 / (4.0 × 10⁻⁶ s) = 250 000 Hz."]),
    dict(id="o26s_spring_amplitude_lambda", chapter=10, level=2, lo="10c", source="BGSS 2024 prelim MCQ 24",
         stem="The end of a long spring is pushed back and forth, sending a longitudinal wave along it. The end moves between two points **1.6 cm** apart, and successive compressions "
              "along the spring are **12.5 cm** apart. What are the amplitude and the wavelength of the wave?",
         correct="amplitude 0.8 cm; wavelength 12.5 cm",
         wrongs={"amplitude 1.6 cm; wavelength 12.5 cm": "The amplitude is the maximum displacement from the CENTRE, so it is half the total distance between the two extreme points.",
                 "amplitude 0.8 cm; wavelength 25 cm": "The wavelength is the distance between successive compressions, not twice it.",
                 "amplitude 1.6 cm; wavelength 6.25 cm": "Both are wrong: halve the swing for the amplitude, and keep the compression spacing as the wavelength."},
         hints=["Amplitude is measured from the rest position to one extreme.", "The end swings 1.6 cm from one extreme to the other.",
                "Wavelength is the distance between successive compressions (or rarefactions)."]),
], category=CAT)


@template("o26s_radio_wavelength", chapter=10, level=2, lo="10d", category=CAT)
def radio_wavelength(rng):
    f_mhz = nice(rng, 200, 150, 250, 120)
    lam = 3e8 / (f_mhz * 1e6)
    return calc_q(rng, f"A radio wave has a frequency of **{f_mhz} MHz** and travels at **3 × 10⁸ m/s**. What is its wavelength?", lam,
                  [(3e8 / f_mhz, "MHz means 10⁶ Hz: the frequency must be changed into hertz first."),
                   (lam / 2, "Check the arithmetic: λ = v / f with no factor of 2."),
                   (2 * lam, "Check the arithmetic: λ = v / f with no factor of 2.")],
                  "m", "v = f λ ⇒ λ = v / f",
                  [f"f = {f_mhz} MHz = {sci(f_mhz * 1e6, 2)} Hz", f"λ = v / f = 3 × 10⁸ / {sci(f_mhz * 1e6, 2)} = **{fmt(lam)} m**", cite("QTSS 2026 prelim MCQ 20")],
                  ["Mega means a million: write the frequency in Hz.", "v = f λ.", "Rearrange: λ = v ÷ f."])


@template("o26s_wavefronts_speed", chapter=10, level=3, lo="10d", category=CAT)
def wavefronts_speed(rng):
    f, n, span = nice(rng, (5, 4, 12.0), (4, 5, 15.0), (6, 3, 7.5), (5, 6, 18.0))
    lam = span / n
    v = f * lam
    return calc_q(rng, f"Fig. 1 shows the wavefronts produced by a dipper in a ripple tank. The dipper makes **{f} oscillations every second**. "
                  f"The distance across **{n} wavelengths** is marked. What is the speed of the wave?", v,
                  [(f * span, "The marked distance covers several wavelengths; divide it by the number of wavelengths first."),
                   (lam / f, "Speed = frequency × wavelength, not wavelength ÷ frequency."),
                   (span / n, "That is the wavelength. Multiply by the frequency to get the speed.")],
                  "cm/s", "v = f λ, λ = marked distance ÷ number of wavelengths",
                  [f"λ = {fmt(span)} / {n} = {fmt(lam)} cm", f"v = f λ = {f} × {fmt(lam)} = **{fmt(v)} cm/s**", cite("NAS 2025 prelim MCQ 18")],
                  ["Count how many wavelengths the marked distance covers.", "Wavelength = that distance ÷ the number of wavelengths.", "v = f λ."],
                  figure=sketches.wavefronts_sketch(n, f"{fmt(span)} cm"))
