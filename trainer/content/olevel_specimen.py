"""O level 2026 MCQ practice: every MCQ of the SEAB 6091 specimen Paper 1 (2024), adapted (added 31 Oct 2026).
Same context, skill and answer logic as the SEAB question; figures redrawn; numbers changed and varied on every serve;
picture options turned into word options."""
from .. import figs, figs2, figs3, sketches, sketches5 as k5
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template, text_options

CAT = "olevel"


def src(n, *more):
    s = f"SEAB 6091 specimen paper 2024 MCQ {n}"
    for m in more:
        s += f" and MCQ {m}"
    return s


def cite(n, *more):
    return f"_Adapted from {src(n, *more)}._"


# ================================================================== Ch 2 Kinematics
@template("o26_cyclist_stops", chapter=2, level=3, lo="2h", category=CAT)
def cyclist_stops(rng):
    v, s = nice(rng, (5.0, 3.0), (4.0, 3.0), (6.0, 4.5), (8.0, 6.0))
    t = 2 * s / v
    return calc_q(rng, f"A cyclist riding at **{fmt(v)} m/s** brakes with uniform deceleration and stops in a distance of **{fmt(s)} m**. "
                  "How long does the cyclist take to stop?", t,
                  [(s / v, "distance ÷ speed only works for a CONSTANT speed. Here the speed falls steadily from v to 0, so the average speed is v/2."),
                   (s, "That is the stopping distance in metres, not a time."),
                   (s / v / 2, "Halving the time is the wrong way round: the average speed is halved, so the time is DOUBLED compared with s/v.")],
                  "s", "distance = average speed × time = ½ v t  ⇒  t = 2 s / v",
                  [f"Uniform deceleration from {fmt(v)} m/s to rest: average speed = ½ × {fmt(v)} = {fmt(v / 2)} m/s",
                   f"t = s / average speed = {fmt(s)} / {fmt(v / 2)} = **{fmt(t)} s**", cite(1)],
                  ["The speed is not constant: it drops steadily from the starting value to zero.",
                   "For uniform deceleration the average speed is half the starting speed (the area under a v-t triangle).",
                   "time = distance ÷ average speed."])


explain_mcqs([
    dict(id="o26_parachute_dt", chapter=2, level=3, lo="2f", source=src(2),
         stem="Fig. 1 shows how the height of a parachutist above the ground varies with time. Which description of the motion is correct?",
         correct="falls at a constant speed, then at a lower constant speed after the parachute opens",
         wrongs={"falls at a constant speed, then at a higher constant speed after the parachute opens": "The second section is LESS steep, so the height is changing more slowly: a lower speed.",
                 "falls with a steadily increasing speed throughout": "A steadily increasing speed gives a curve that gets steeper and steeper, not two straight lines.",
                 "falls at a constant speed, then stays at rest in the air for a while": "At rest the graph would be horizontal. The second section still slopes down, so the parachutist is still descending."},
         hints=["On a displacement-time graph the gradient is the velocity.", "A straight line means a constant speed; a steeper line means a higher speed.",
                "Compare the gradients of the two straight sections."],
         figure=lambda: figs.graph([(0, 120), (4, 40), (12, 0)], 12, 140, 2, 20, xlabel="time / s", ylabel="height above ground / m")),
], category=CAT)


# ================================================================== Ch 3 Dynamics
@template("o26_rock_moon", chapter=3, level=2, lo="3f", category=CAT)
def rock_moon(rng):
    m = nice(rng, 8, 10, 12, 15)
    g_moon = 1.6
    correct = f"Its mass on the Moon is {m} kg."
    wrongs = {f"Its mass on the Moon is {fmt(m * g_moon / 10)} kg.": "Mass is the amount of matter in the rock: it is the same everywhere. Only the weight changes with g.",
              "Its weight on the Moon is zero.": "The Moon has a gravitational field (1.6 N/kg), so the rock has a weight there: W = m g = " + f"{fmt(m * g_moon)} N.",
              f"Its weight on the Earth is {m} N.": f"Weight = m g = {m} × 10 = {m * 10} N on the Earth. {m} is the mass in kg, not the weight in N."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"The gravitational field strength is 1.6 N/kg on the Moon and 10 N/kg on the Earth. A rock has a mass of **{m} kg** "
                     "on the Earth. Which statement about the rock is correct?",
                options=opts, key=key, misconceptions=mis, formula="W = m g; mass does not change from place to place",
                working=[f"Mass is the amount of matter: {m} kg everywhere. Weight on Earth = {m} × 10 = {m * 10} N; weight on the Moon = {m} × 1.6 = {fmt(m * g_moon)} N.",
                         f"Correct answer: **{correct}**", cite(3)],
                hints=["Mass measures the amount of matter in a body. Does moving the rock change how much matter it has?",
                       "Weight = mass × gravitational field strength, and g is different on the Moon.",
                       f"Work out the weight on the Earth: {m} kg × 10 N/kg."])


@template("o26_push_friction", chapter=3, level=2, lo="3j", category=CAT)
def push_friction(rng):
    F, f, m = nice(rng, (20.0, 5.0, 5.0), (24.0, 6.0, 6.0), (30.0, 6.0, 8.0), (18.0, 4.0, 7.0))
    a = (F - f) / m
    return calc_q(rng, f"A force of **{fmt(F)} N** pushes an object of mass **{fmt(m)} kg** along a rough horizontal surface. The frictional force on "
                  f"the object is **{fmt(f)} N**. What is the acceleration of the object?", a,
                  [(F / m, "That uses the push alone. Friction acts against the motion, so the RESULTANT force is push − friction."),
                   ((F + f) / m, "Friction opposes the motion: subtract it from the push, do not add it."),
                   (f / m, "That uses the friction alone as if it were the resultant force.")],
                  "m/s²", "resultant force = m a  ⇒  a = (F − f) / m",
                  [f"Resultant force = {fmt(F)} − {fmt(f)} = {fmt(F - f)} N", f"a = {fmt(F - f)} / {fmt(m)} = **{fmt(a)} m/s²**", cite(5)],
                  ["Find the resultant force first: the push forwards minus the friction backwards.",
                   "Newton's second law: resultant force = mass × acceleration.", f"a = ({fmt(F)} − {fmt(f)}) ÷ {fmt(m)}."])


# ================================================================== Ch 4 Turning effects
explain_mcqs([
    dict(id="o26_couple_rod", chapter=4, level=2, lo="4a", source=src(4),
         stem="Two forces of equal size act on a rod at its two ends, as shown in Fig. 1: one downwards at the left end and one upwards at the "
              "right end. Which effect do these two forces produce?",
         correct="rotation only",
         wrongs={"both rotation and movement in a straight line": "The two forces are equal and opposite, so the resultant force is zero: no movement in a straight line.",
                 "no effect because the forces are balanced": "The forces balance (zero resultant force) but they act along different lines, so their moments do not cancel: the rod turns.",
                 "movement in a straight line only": "Equal and opposite forces give zero resultant force, so there is no acceleration in a straight line."},
         hints=["Add the two forces: what is the resultant force?", "Take moments about the centre of the rod: do the two moments cancel or add?",
                "Zero resultant force with a non-zero resultant moment produces one kind of motion only."],
         figure=lambda: k5.couple_rod("5.0 N")),
], category=CAT)


@template("o26_bus_topple", chapter=4, level=4, lo="4f", category=CAT)
def bus_topple(rng):
    letters = ("P", "Q", "R", "S")
    idx = rng.randrange(4)
    correct = letters[idx]
    wrongs = {L: ("That point is not vertically above the lower wheels. If the centre of gravity were there, the weight's line of action would "
                  "already fall outside the base, or still well inside it: the bus would not be JUST about to topple.") for L in letters if L != correct}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="The stability of a bus is tested by tilting it on a ramp. Fig. 1 shows the bus at the moment it is just about to topple over. "
                     "Four points P, Q, R and S are marked. At which point is the centre of gravity of the bus?",
                options=opts, key=key, misconceptions=mis, formula="toppling begins when the vertical line through the centre of gravity passes through the edge of the base",
                working=["A body is just about to topple when the vertical line through its centre of gravity passes through the pivot (the lower edge of the base).",
                         f"The point vertically above the lower wheels is **{correct}**.", cite(6)],
                hints=["The bus pivots about its lower wheels on the ramp.", "Draw a vertical line straight up from that pivot.",
                       "The centre of gravity is on that vertical line when the bus is just about to topple."],
                figure=k5.tilted_box_points(letters, idx))


# ================================================================== Ch 5 Pressure
@template("o26_statue_base", chapter=5, level=3, lo="5b", category=CAT)
def statue_base(rng):
    L, W, H, weight = nice(rng, (2.0, 0.80, 2.5, 96_000), (2.5, 0.80, 2.0, 120_000), (2.0, 1.0, 3.0, 150_000), (1.5, 0.60, 2.5, 72_000))
    p = weight / (L * W)
    return calc_q(rng, f"Fig. 1 shows the stone base for a statue resting on level ground. It is **{fmt(L)} m** long, **{fmt(H)} m** high and "
                  f"**{fmt(W)} m** wide, and its weight is **{weight:,} N**. What is the pressure on the ground due to the base?".replace(",", " "),
                  p / 1000,
                  [(weight / (L * H) / 1000, "That divides by the area of the FRONT face (length × height). Only the bottom face presses on the ground."),
                   (weight / (W * H) / 1000, "That divides by the area of the SIDE face (width × height), which is not in contact with the ground."),
                   (weight / (L * W * H) / 1000, "That divides by the volume. Pressure is force per unit AREA.")],
                  "kPa", "p = F / A, with A the area of the face on the ground",
                  [f"Area on the ground = {fmt(L)} × {fmt(W)} = {fmt(L * W)} m²", f"p = {weight} / {fmt(L * W)} = {fmt(p)} Pa = **{fmt(p / 1000)} kPa**", cite(7)],
                  ["Which face of the block touches the ground? Its area is length × width.", "pressure = force ÷ area, with the force being the weight.",
                   "1 kPa = 1000 Pa."],
                  figure=figs.labelled_block(L, W, H, unit="m"))


@template("o26_block_density", chapter=5, level=2, lo="5d", category=CAT)
def block_density(rng):
    a, b, c, m = nice(rng, (5.0, 4.0, 2.0, 100), (6.0, 4.0, 2.5, 120), (5.0, 3.0, 2.0, 90), (8.0, 5.0, 2.0, 200))
    V = a * b * c
    rho = m / V
    return calc_q(rng, f"Fig. 1 shows a solid block with dimensions **{fmt(a)} cm × {fmt(b)} cm × {fmt(c)} cm**. Its mass is **{m} g**. "
                  "What is the density of the solid?", rho,
                  [(m / (a * b), "That divides by the area of one face. Density needs the VOLUME: all three dimensions multiplied."),
                   (V / m, "That is volume ÷ mass, the wrong way up. Density = mass ÷ volume."),
                   (m / (a + b + c), "The dimensions must be multiplied to give the volume, not added.")],
                  "g/cm³", "ρ = m / V, V = a × b × c",
                  [f"V = {fmt(a)} × {fmt(b)} × {fmt(c)} = {fmt(V)} cm³", f"ρ = {m} / {fmt(V)} = **{fmt(rho)} g/cm³**", cite(8)],
                  ["Find the volume of the cuboid first: multiply the three dimensions.", "density = mass ÷ volume.",
                   f"ρ = {m} ÷ {fmt(V)}."],
                  figure=figs.labelled_block(a, b, c))


explain_mcqs([
    dict(id="o26_dam_pressure", chapter=5, level=2, lo="5e", source=src(9),
         stem="Fig. 1 shows water held in a reservoir by a dam wall. X is a point in the water at the foot of the wall. Which factor determines "
              "the pressure of the water at X?",
         correct="the depth of X below the water surface",
         wrongs={"the surface area of the reservoir": "p = h ρ g: the pressure at a depth depends only on the depth, the density of the liquid and g, not on how wide the reservoir is.",
                 "the weight of the dam wall": "The wall holds the water back; its weight does not push on the water at X.",
                 "the thickness of the dam wall": "The wall's thickness matters for the wall's strength, not for the pressure in the water."},
         hints=["Pressure in a liquid: p = h ρ g.", "Which quantity in that formula can change from one point in the water to another?",
                "The size and shape of the container do not appear in the formula."],
         figure=lambda: figs2.liquid_column("h", liquid_label="water", point_label="X")),
], category=CAT)


# ================================================================== Ch 6 Energy
@template("o26_stairs_power", chapter=6, level=2, lo="6e", category=CAT)
def stairs_power(rng):
    W, h, t = nice(rng, (500, 5.0, 10), (450, 4.0, 8.0), (600, 5.0, 12), (550, 6.0, 15))
    P = W * h / t
    return calc_q(rng, f"A girl of weight **{W} N** runs up a flight of stairs in **{fmt(t)} s**. Fig. 1 shows the stairs; their vertical height is "
                  f"**{fmt(h)} m**. What is the average useful power developed by the girl?", P,
                  [(W * h, "That is the work done (energy gained) in joules. Power is energy per second: divide by the time."),
                   (W / t, "Weight ÷ time is not an energy per second. The work done is weight × height, THEN divide by time."),
                   (W * t / h, "Time and height are the wrong way round: power = W × h ÷ t.")],
                  "W", "P = W / t = (weight × height) / time",
                  [f"Work done against gravity = {W} × {fmt(h)} = {fmt(W * h)} J", f"P = {fmt(W * h)} / {fmt(t)} = **{fmt(P)} W**", cite(10)],
                  ["The useful work is lifting her weight through the vertical height of the stairs.", "work done = force × distance = weight × height.",
                   "power = work done ÷ time taken."],
                  figure=k5.stairs(f"{fmt(h)} m"))


explain_mcqs([
    dict(id="o26_parachute_energy", chapter=6, level=3, lo="6a", source=src(11),
         stem="A parachutist opens the parachute and then falls to the ground at a constant speed. What is the main energy transfer taking place "
              "while the parachutist falls at this constant speed?",
         correct="gravitational potential store to internal store of energy",
         wrongs={"gravitational potential store to kinetic store of energy": "At a CONSTANT speed the kinetic energy does not change, so the kinetic store is not gaining energy.",
                 "kinetic store to internal store of energy": "The kinetic store stays the same at constant speed. The store that is being emptied is the gravitational potential store (the height is falling).",
                 "kinetic store to gravitational potential store of energy": "The parachutist is moving DOWN, so gravitational potential energy is decreasing, not increasing."},
         hints=["At a constant speed, which energy store stays the same?", "The parachutist is losing height. Which store is that emptying?",
                "Where does that energy go when air resistance acts? Think about heating of the air and parachute."]),
], category=CAT)


# ================================================================== Ch 7 Kinetic particle model
explain_mcqs([
    dict(id="o26_liquid_particles", chapter=7, level=2, lo="7b", source=src(12),
         stem="According to the kinetic particle model, matter is made up of very small particles in constant motion. Which row describes the "
              "forces between the particles and the motion of the particles in the **liquid** state?\n\n"
              + md_table(["", "forces between particles", "motion of particles"],
                         [["solid", "strong", "vibrate about fixed positions"], ["liquid", "?", "?"], ["gas", "very weak", "move randomly at high speed"]]),
         correct="fairly strong forces; the particles vibrate and slide over one another",
         wrongs={"fairly strong forces; the particles move randomly at high speed": "Moving randomly at high speed with large separation describes a GAS.",
                 "fairly strong forces; the particles vibrate about fixed positions": "Fixed positions describe a SOLID. Liquid particles can change places and flow.",
                 "very weak forces; the particles move randomly at high speed": "Very weak forces and fast random motion describe a gas, which fills its container; a liquid does not."},
         hints=["A liquid keeps its volume but takes the shape of its container.", "Keeping its volume means the forces between particles are still fairly strong.",
                "Taking the shape of the container means the particles can slide past one another."]),
    dict(id="o26_gas_heated_pressure", chapter=7, level=3, lo="7e", source=src(13),
         stem="Why does the pressure of a fixed mass of gas increase when it is heated at constant volume?",
         correct="The average speed of the particles increases, so they hit the walls harder and more often.",
         wrongs={"More particles are created by the heating.": "Heating does not create particles: the mass of gas is fixed, so the number of particles stays the same.",
                 "The average mass of the particles increases.": "The particles are the same molecules before and after heating; their mass does not change.",
                 "The average separation of the particles increases.": "The volume is constant, so the average separation of the particles cannot change."},
         hints=["Gas pressure comes from particles colliding with the container walls.", "Heating raises the average kinetic energy of the particles.",
                "Faster particles collide with the walls harder and more frequently."]),
], category=CAT)


# ================================================================== Ch 8 Thermal processes
explain_mcqs([
    dict(id="o26_beaker_convection", chapter=8, level=3, lo="8c", source=src(14),
         stem="Fig. 1 shows a beaker of water at room temperature. X is near the top of the water on one side and Y is near the bottom on the other side. "
              "Which action sets up a convection current in the water?",
         correct="cooling the water at X",
         wrongs={"cooling the water at Y": "Cooled water at the bottom becomes denser and simply stays at the bottom: nothing moves.",
                 "stirring the water at X": "Stirring moves the water mechanically, but a convection current is a flow caused by DENSITY differences from heating or cooling.",
                 "stirring the water at Y": "Stirring is not convection: no part of the water becomes denser or less dense."},
         hints=["Convection needs a density difference: part of the fluid must become denser or less dense.", "Cooled water contracts, becomes denser and sinks.",
                "Where must the water be cooled so that denser water can sink through less dense water?"],
         figure=lambda: k5.beaker_xy("X", "Y")),
], category=CAT)


# ================================================================== Ch 9 Thermal properties
explain_mcqs([
    dict(id="o26_condensation_arrow", chapter=9, level=1, lo="9d", source=src(15),
         stem="Fig. 1 shows the three states of matter with four changes of state labelled P, Q, R and S. Which arrow shows condensation?",
         correct="S",
         wrongs={"P": "P goes from solid to liquid: that is melting.", "Q": "Q goes from liquid to gas: that is boiling (or evaporation).",
                 "R": "R goes from liquid to solid: that is solidification (freezing)."},
         hints=["Condensation is the change from a gas to a liquid.", "Find the arrow that starts at the gas box.", "It must end at the liquid box."],
         figure=lambda: k5.state_arrows()),
    dict(id="o26_sulfur_solidifies", chapter=9, level=2, lo="9d", source=src(16),
         stem="Which statement describes what happens while molten sulfur solidifies?",
         correct="Energy is transferred out of the sulfur but its temperature does not change.",
         wrongs={"Energy is transferred out of the sulfur and its temperature falls.": "During a change of state the temperature stays constant: the energy given out is the latent heat, not a loss of kinetic energy.",
                 "No energy is transferred and the temperature does not change.": "Energy IS given out as the sulfur solidifies (the latent heat of fusion), even though the temperature stays the same.",
                 "No energy is transferred but the temperature falls.": "A falling temperature would need energy to leave, and during solidification the temperature does not fall anyway."},
         hints=["Solidifying is a change of state.", "During a change of state the temperature stays constant.",
                "Latent heat is still given out as the particles settle into fixed positions."]),
    dict(id="o26_evaporation_cools", chapter=9, level=2, lo="9e", source=src(17),
         stem="A liquid evaporates rapidly. Why does this cause the liquid to cool?",
         correct="Some of the most energetic molecules leave the liquid, so the average kinetic energy of those left behind falls.",
         wrongs={"Energy is lost from the liquid by conduction.": "Conduction is not what evaporation is. The cooling comes from WHICH molecules escape from the surface.",
                 "Energy is lost from the liquid by convection currents.": "Convection moves warm liquid around; it does not explain why evaporation itself cools the liquid.",
                 "The molecules left behind have less room to move around.": "The molecules do not become crowded. The liquid cools because the fastest molecules are the ones that escape."},
         hints=["Which molecules can escape from the surface of a liquid: the slow ones or the fast ones?",
                "Temperature depends on the AVERAGE kinetic energy of the molecules.", "If the fastest molecules leave, what happens to the average of those left?"]),
], category=CAT)


@template("o26_ice_melt_time", chapter=9, level=3, lo="9g", category=CAT)
def ice_melt_time(rng):
    m, P = nice(rng, (7.50, 1.25), (6.00, 1.50), (8.00, 1.25), (5.00, 2.00))
    L = 334.0
    t = m * L / P
    return calc_q(rng, f"An ice cube of mass **{fmt(m)} g** is at 0 °C. The specific latent heat of fusion of ice is **{L:.0f} J/g**. Energy from the "
                  f"surroundings is transferred to the ice at an average rate of **{fmt(P)} J/s**. How long does it take for the ice to melt completely?", t,
                  [(L / (m * P), "That divides L by both the mass and the power. The energy needed is m × L (multiply), then divide by the power."),
                   (P * L / m, "Power and mass are the wrong way round: time = energy ÷ power = m L ÷ P."),
                   (m * L, "That is the energy needed in joules. Divide it by the rate of energy transfer to get the time.")],
                  "s", "E = m L; t = E / P",
                  [f"Energy needed = m L = {fmt(m)} × {L:.0f} = {fmt(m * L)} J", f"t = {fmt(m * L)} / {fmt(P)} = **{fmt(t)} s**", cite(18)],
                  ["First find the energy needed to melt the ice: mass × specific latent heat.", "The surroundings supply energy at a fixed rate (J per second).",
                   "time = energy needed ÷ rate of energy transfer."])


# ================================================================== Ch 10 Waves
@template("o26_rope_wavelength", chapter=10, level=2, lo="10c", category=CAT)
def rope_wavelength(rng):
    lam, amp_cm = nice(rng, (1.6, 30), (1.2, 20), (2.0, 25), (0.8, 15))
    return calc_q(rng, "A long rope lies on the floor. One end is shaken and Fig. 1 shows the shape of the rope at one instant. What is the wavelength of the wave?",
                  lam,
                  [(lam / 2, "That is the distance from a crest to the next trough: half a wavelength."),
                   (2 * lam, "That is two complete waves."),
                   (amp_cm / 100, "That is the amplitude (the maximum displacement) converted to metres, not the wavelength.")],
                  "m", "wavelength = distance between two successive crests (or troughs)",
                  [f"Successive crests are {fmt(lam)} m apart on the distance axis.", f"λ = **{fmt(lam)} m**", cite(19)],
                  ["Wavelength is measured along the distance axis, not the displacement axis.", "Find two successive crests (or two successive troughs).",
                   "Read the distance between them."],
                  figure=sketches.wave_graph(amp_cm, lam, kind="distance_m"))


explain_mcqs([
    dict(id="o26_compressions_air", chapter=10, level=1, lo="10g", source=src(20),
         stem="Which waves travel through the air as a series of compressions and rarefactions?",
         correct="sound waves",
         wrongs={"light waves": "Light is a transverse electromagnetic wave: it does not compress the air.",
                 "microwaves": "Microwaves are transverse electromagnetic waves and need no medium at all.",
                 "radio waves": "Radio waves are transverse electromagnetic waves; they do not squash and stretch the air."},
         hints=["Compressions and rarefactions are regions where the medium is squashed and stretched along the direction of travel.",
                "That is the definition of a longitudinal wave.", "Which of the options is longitudinal and needs a medium?"]),
    dict(id="o26_two_sound_traces", chapter=10, level=3, lo="10h", source=src(21),
         stem="Fig. 1 shows the displacement-time traces of two sound waves P and Q drawn on identical grids. How do the frequency and the pitch of P "
              "compare with those of Q?",
         correct="frequency of P greater than Q; pitch of P higher than Q",
         wrongs={"frequency of P greater than Q; pitch of P the same as Q": "Pitch depends on frequency: a higher frequency means a higher pitch, so the pitches cannot be the same.",
                 "frequency of P the same as Q; pitch of P higher than Q": "P fits more complete waves into the same time, so its frequency is higher, not the same.",
                 "frequency of P the same as Q; pitch of P the same as Q": "Count the waves in the same width of grid: P has more, so P has the higher frequency and pitch. (P's larger amplitude affects loudness, not pitch.)"},
         hints=["Count how many complete waves each trace fits into the same length of time axis.", "More waves in the same time means a higher frequency.",
                "Pitch is set by frequency; loudness is set by amplitude."],
         figure=lambda: k5.two_traces()),
], category=CAT)


@template("o26_echo_knocks", chapter=10, level=4, lo="10i", category=CAT)
def echo_knocks(rng):
    d, f = nice(rng, (50, 3), (55, 3), (60, 3), (40, 4))
    v = 2 * d * f
    return calc_q(rng, f"A student stands **{d} m** from a large wall and knocks two wooden blocks together **{f} times every second**. The echo of each "
                  "knock is heard at the same instant as the next knock. What value does this give for the speed of sound?", v,
                  [(d * f, "The sound travels to the wall AND back: the distance for one echo is 2d, not d."),
                   (d / f, "Distance ÷ frequency is not a speed. The time for one echo is 1/f seconds and the distance is 2d."),
                   (4 * d * f, "The sound goes there and back once (2d) between knocks, not twice.")],
                  "m/s", "v = 2d / t, with t = time between knocks = 1 / f",
                  [f"Time between knocks = 1/{f} s = {fmt(1 / f)} s, which is the time for the sound to go to the wall and back.",
                   f"v = 2 × {d} / {fmt(1 / f)} = **{fmt(v)} m/s**", cite(22)],
                  ["The echo arrives exactly one knock-interval after the knock. How long is that interval?", "In that time the sound travels to the wall and back: 2d.",
                   "speed = distance ÷ time."])


# ================================================================== Ch 11 EM spectrum
explain_mcqs([
    dict(id="o26_tv_remote", chapter=11, level=1, lo="11c", source=src(23),
         stem="Which waves does a television remote controller use to send its signal to the television?",
         correct="infrared waves",
         wrongs={"microwaves": "Microwaves are used for satellite TV and mobile phones, not for a hand-held remote.",
                 "ultrasound waves": "Ultrasound is a sound wave, not part of the electromagnetic spectrum, and remotes use light-like pulses.",
                 "ultraviolet waves": "Ultraviolet is used for sterilising and detecting forged banknotes, not for remote controls."},
         hints=["The remote has a small LED at the front that you cannot see glowing.", "It sends pulses of a wave just beyond the red end of visible light.",
                "That region of the spectrum is also used for night-vision cameras and thermal imaging."]),
], category=CAT)


# ================================================================== Ch 12 Light
explain_mcqs([
    dict(id="o26_mirror_image_point", chapter=12, level=3, lo="12b", source=src(24),
         stem="Fig. 1 shows a ray of light from a point on a lamp striking a plane mirror. P is a point behind the mirror, as far behind it as the lamp "
              "is in front; R is a point in front of the mirror. Which statement describes the image of the point on the lamp?",
         correct="The image is at P and is virtual.",
         wrongs={"The image is at P and is real.": "The reflected rays only APPEAR to come from P; no light reaches P behind the mirror, so the image cannot be formed on a screen: it is virtual.",
                 "The image is at R and is real.": "R is in front of the mirror. A plane mirror's image is as far BEHIND the mirror as the object is in front.",
                 "The image is at R and is virtual.": "The image is virtual, but it lies behind the mirror, directly opposite the object, not at R."},
         hints=["A plane mirror forms its image as far behind the mirror as the object is in front, on the normal through the object.",
                "Light does not actually pass through the mirror to the image position.",
                "An image that light only appears to come from is called virtual."],
         figure=lambda: k5.mirror_points("R", "P")),
    dict(id="o26_prism_tir", chapter=12, level=4, lo="12f", source=src(25),
         stem="Fig. 1 shows a glass prism with angles of 45°, 90° and 45°. The critical angle of the glass is 42°. A narrow beam enters the prism at right "
              "angles to one of the short faces. What happens when the beam reaches the long face?",
         correct="It is totally internally reflected, because its angle of incidence (45°) is greater than the critical angle.",
         wrongs={"It passes straight out of the prism without bending, because it meets the face at 45°.": "A ray only passes a boundary without bending when it is along the normal (angle of incidence 0°), not at 45°.",
                 "It refracts out of the prism, bending away from the normal, because 45° is less than the critical angle.": "45° is GREATER than 42°, so no refracted ray can leave: the light is all reflected.",
                 "It is partly reflected and partly refracted, as at every glass-air boundary.": "Partial reflection and refraction happen only when the angle of incidence is LESS than the critical angle."},
         hints=["Entering at right angles to a face, the beam is not bent at that face.", "Inside the prism the beam meets the long face at 45° to the normal.",
                "Compare 45° with the critical angle, 42°."],
         figure=lambda: k5.prism_beam()),
], category=CAT)


# ================================================================== Ch 13 Static electricity
explain_mcqs([
    dict(id="o26_rubbed_plastic", chapter=13, level=2, lo="13f", source=src(26),
         stem="A plastic rod is rubbed with a cloth. The rod becomes negatively charged and the cloth becomes positively charged. What happens to the rod "
              "and to the cloth to cause this?",
         correct="The rod gains electrons; the cloth loses electrons.",
         wrongs={"The rod gains electrons; the cloth gains protons.": "Protons are fixed in the nuclei of atoms and never move during rubbing. Only electrons are transferred.",
                 "The rod loses protons; the cloth gains protons.": "Protons cannot leave their nuclei. A negative charge comes from GAINING electrons, not losing protons.",
                 "The rod loses protons; the cloth loses electrons.": "The cloth does lose electrons, but the rod becomes negative by gaining those electrons, not by losing protons."},
         hints=["Charging by rubbing only ever transfers electrons.", "A negative charge means extra electrons.", "The electrons the rod gains must have come from the cloth."]),
    dict(id="o26_sphere_induction", chapter=13, level=4, lo="13g", source=src(27),
         stem="A negatively charged sphere X is brought close to an identical uncharged metal sphere Y on an insulating stand; they do not touch. "
              "Y is then earthed for a moment by touching it with a finger. The finger is removed, and then X is taken away. What is the final charge on Y?",
         correct="positive all over",
         wrongs={"negative all over": "Electrons in Y were repelled by X and ran to earth through the finger. Y is left SHORT of electrons, so it is positive.",
                 "uncharged": "Y was earthed while X was still near, so electrons left it. Removing the finger first traps that deficit, so Y keeps a charge.",
                 "positive on the side nearer X and negative on the far side": "That is the arrangement WHILE X is near. Once X is removed the remaining charge spreads evenly over the sphere."},
         hints=["X is negative: which way does it push the free electrons in Y?", "While the finger touches Y, those pushed-away electrons can escape to earth.",
                "Remove the finger first, then X: what charge is left, and how does it spread over a conductor?"]),
], category=CAT)


# ================================================================== Ch 14 Current of electricity
@template("o26_pd_from_charge_energy", chapter=14, level=3, lo="14f", category=CAT)
def pd_from_charge_energy(rng):
    Q, t, E = nice(rng, (60, 120, 5.0), (90, 180, 6.0), (40, 80, 3.0), (120, 60, 8.0))
    I = Q / t
    V = E / I
    return calc_q(rng, f"A charge of **{Q} C** passes through a resistor in **{t} s**. In each second, **{fmt(E)} J** of energy is transferred in the resistor. "
                  "What is the potential difference across the resistor?", V,
                  [(E, "That treats the energy per second (the power, in W) as if it were the p.d. in volts."),
                   (E * Q / t, "That multiplies power by current. p.d. = power ÷ current."),
                   (E * t, "That is the energy transferred in the whole time, in joules, not a p.d.")],
                  "V", "I = Q / t;  P = V I  ⇒  V = P / I",
                  [f"I = Q / t = {Q} / {t} = {fmt(I)} A", f"P = {fmt(E)} W, so V = P / I = {fmt(E)} / {fmt(I)} = **{fmt(V)} V**", cite(28)],
                  ["First find the current: charge ÷ time.", "Energy per second is the power.", "p.d. = power ÷ current (from P = V I)."])


explain_mcqs([
    dict(id="o26_filament_r_i", chapter=14, level=3, lo="14j", source=src(30),
         stem="A filament lamp is switched on. As the filament heats up, its resistance changes. Which pair of statements describes how the resistance R "
              "of the filament and the current I in the lamp change with time after switching on?",
         correct="R rises and then levels off; I falls and then levels off.",
         wrongs={"R rises and then levels off; I rises and then levels off.": "With a fixed supply p.d., a RISING resistance means a FALLING current (I = V/R).",
                 "R falls and then levels off; I falls and then levels off.": "The resistance of a metal INCREASES as its temperature rises; it does not fall.",
                 "R falls and then levels off; I rises and then levels off.": "A hotter metal filament has a higher resistance, not a lower one."},
         hints=["How does the resistance of a metal change as it gets hotter?", "The supply p.d. stays the same: use I = V / R.",
                "Both quantities settle once the filament reaches its steady working temperature."]),
], category=CAT)


# ================================================================== Ch 15 D.C. circuits
@template("o26_voltmeter_series_parallel", chapter=15, level=4, lo="15g", category=CAT)
def voltmeter_series_parallel(rng):
    R1, R2, I1, I2, Rs = nice(rng, (2.0, 5.0, 5.0, 2.0, 1.0), (3.0, 6.0, 4.0, 2.0, 1.0), (2.0, 4.0, 4.0, 2.0, 2.0), (4.0, 6.0, 3.0, 2.0, 1.0))
    Vp = I1 * R1
    I = I1 + I2
    V = Vp + I * Rs
    return calc_q(rng, f"Fig. 1 shows a **{fmt(Rs)} Ω** resistor in series with a parallel pair: a **{fmt(R1)} Ω** resistor carrying **{fmt(I1)} A** and a "
                  f"**{fmt(R2)} Ω** resistor carrying **{fmt(I2)} A**. A voltmeter is connected across the battery. What is its reading?", V,
                  [(Vp, "That is the p.d. across the parallel pair only. The series resistor also has a p.d. across it."),
                   (Vp + I1 * Rs, "The series resistor carries the TOTAL current (both branch currents added), not just one branch's current."),
                   (I * (Rs + R1), "The parallel pair is not simply R1 in series: use its p.d. (I1 × R1) and add the series p.d. (I × Rs).")],
                  "V", "V_total = V_parallel + I_total × R_series",
                  [f"p.d. across the parallel pair = {fmt(I1)} × {fmt(R1)} = {fmt(Vp)} V (check: {fmt(I2)} × {fmt(R2)} = {fmt(I2 * R2)} V)",
                   f"Total current = {fmt(I1)} + {fmt(I2)} = {fmt(I)} A; p.d. across the {fmt(Rs)} Ω = {fmt(I)} × {fmt(Rs)} = {fmt(I * Rs)} V",
                   f"Voltmeter reading = {fmt(Vp)} + {fmt(I * Rs)} = **{fmt(V)} V**", cite(29)],
                  ["Find the p.d. across the parallel pair from either branch: V = I R.", "The series resistor carries the sum of the two branch currents.",
                   "The battery p.d. is the sum of the p.d.s across the series resistor and the parallel pair."],
                  figure=figs3.circuit(top=[("R", f"{fmt(Rs)} Ω")], branches=[[("A", f"{fmt(I1)} A"), ("R", f"{fmt(R1)} Ω")], [("A", f"{fmt(I2)} A"), ("R", f"{fmt(R2)} Ω")]],
                                       emf="", left_kind="battery"))


explain_mcqs([
    dict(id="o26_smallest_current", chapter=15, level=3, lo="15d", source=src(31),
         stem="Fig. 1 shows a 2.0 Ω resistor in series with a parallel pair of resistors, 1.0 Ω and 3.0 Ω. Which statement about the current is correct?",
         correct="The current in the 3.0 Ω resistor is the smallest.",
         wrongs={"The current in the 1.0 Ω resistor is the smallest.": "The two branches have the same p.d., so the SMALLER resistance takes the LARGER current.",
                 "The current in the 2.0 Ω resistor is the smallest.": "The 2.0 Ω resistor is in the main circuit: it carries the whole current, which is the largest in the circuit.",
                 "The current is the same at every point in the circuit.": "That is only true for a series circuit. Here the current splits between two branches."},
         hints=["The series resistor carries the total current.", "At the junction the current splits; both branches have the same p.d.",
                "I = V / R: which branch has the larger resistance?"],
         figure=lambda: figs3.circuit(top=[("R", "2.0 Ω")], branches=[[("R", "1.0 Ω")], [("R", "3.0 Ω")]], emf="6.0 V")),
    dict(id="o26_divider_parallel_r", chapter=15, level=5, lo="15h", source=src(32),
         stem="A potential divider is made of two equal fixed resistors in series across a battery. Voltmeter V₁ reads the p.d. across the upper resistor "
              "and V₂ the p.d. across the lower resistor. A variable resistor R is connected in parallel with the LOWER resistor only. The resistance "
              "of R is now increased. What happens to the voltmeter readings?",
         correct="V₁ decreases and V₂ increases.",
         wrongs={"V₁ increases and V₂ decreases.": "Increasing R makes the lower (parallel) combination's resistance LARGER, so it takes a bigger share of the battery p.d.: V₂ goes up.",
                 "V₁ decreases and V₂ decreases.": "The two readings always add up to the battery p.d., so they cannot both fall.",
                 "V₁ increases and V₂ increases.": "The two readings add up to the fixed battery p.d., so if one rises the other must fall."},
         hints=["A resistor in parallel with the lower resistor LOWERS the combined resistance of that section; raising R brings it back up.",
                "In a series chain the p.d. is shared in proportion to resistance.", "V₁ + V₂ = battery p.d., which does not change."]),
], category=CAT)


# ================================================================== Ch 16 Practical electricity
@template("o26_cooker_cost", chapter=16, level=3, lo="16c", category=CAT)
def cooker_cost(rng):
    P1, t1, P2, t2, c = nice(rng, (1500, 1.0, 2000, 3.0, 24), (1200, 2.0, 2500, 2.0, 25), (1500, 2.0, 2000, 2.5, 30), (1000, 1.5, 3000, 2.0, 20))
    kwh = P1 / 1000 * t1 + P2 / 1000 * t2
    cost = kwh * c
    return calc_q(rng, f"An electric cooker has a hotplate rated at **{P1} W** and an oven rated at **{P2} W**. In one day the hotplate is on for **{fmt(t1)} h** "
                  f"and the oven for **{fmt(t2)} h**. Electricity costs **{c} cents per kW h**. What is the cost of using the cooker for the day?", cost,
                  [((P1 + P2) / 1000 * c, "That charges for 1 hour of both together. Each appliance's energy is its power × ITS OWN time."),
                   ((P1 + P2) / 1000 * (t1 + t2) * c, "That runs both appliances for the total of both times. Multiply each power by its own time."),
                   ((P1 * t1 + P2 * t2) / 1000 * c / 10, "The energy is in kW h already (power in kW × hours): no extra factor of 10.")],
                  "cents", "energy (kW h) = power (kW) × time (h); cost = kW h × price per kW h",
                  [f"Hotplate: {P1 / 1000} kW × {fmt(t1)} h = {fmt(P1 / 1000 * t1)} kW h; oven: {P2 / 1000} kW × {fmt(t2)} h = {fmt(P2 / 1000 * t2)} kW h",
                   f"Total = {fmt(kwh)} kW h; cost = {fmt(kwh)} × {c} = **{fmt(cost)} cents**", cite(33)],
                  ["Change each power into kW (divide by 1000).", "Energy in kW h = kW × hours, for each appliance separately.", "Add the two energies, then multiply by the price per kW h."])


explain_mcqs([
    dict(id="o26_live_touches_case", chapter=16, level=3, lo="16f", source=src(34),
         stem="The metal case of an electric heater is earthed and its plug has a 5 A fuse. The heater normally takes 4.0 A. The insulation of the cable wears "
              "away so that the live wire touches the metal case. What happens?",
         correct="A large current flows through the earth wire, so the fuse melts and switches the circuit off.",
         wrongs={"There is a large current in the earth wire, and the fuse is not affected.": "The large current to earth also passes through the live wire and the fuse in the plug, so the fuse blows.",
                 "The metal case becomes live and dangerous.": "That is what would happen WITHOUT an earth wire. The earth wire gives the current an easy path and the fuse then cuts the supply.",
                 "The metal case becomes very hot.": "The fault current flows through the low-resistance earth wire for only a moment before the fuse melts; the case does not heat up."},
         hints=["The earth wire has a very low resistance and connects the case to the ground.", "A low-resistance path from live to earth lets a very large current flow.",
                "That current passes through the fuse in the live wire: what does a fuse do with a current above its rating?"]),
], category=CAT)


# ================================================================== Ch 17 Magnetism
@template("o26_three_bars", chapter=17, level=3, lo="17b", category=CAT)
def three_bars(rng):
    x_poles = nice(rng, ("N", "S"), ("S", "N"))
    y_poles = ("N", "S")
    attract_x = x_poles[1] != y_poles[0]
    fx = "attraction" if attract_x else "repulsion"
    correct = f"force on X: {fx}; force on Z: attraction"
    wrongs = {f"force on X: {fx}; force on Z: repulsion": "Soft iron is unmagnetised: the magnet induces the OPPOSITE pole in the near end of Z, so the iron is always attracted.",
              f"force on X: {'repulsion' if attract_x else 'attraction'}; force on Z: attraction":
                  f"X's {x_poles[1]} pole faces Y's {y_poles[0]} pole: {'unlike poles attract' if attract_x else 'like poles repel'}.",
              f"force on X: {'repulsion' if attract_x else 'attraction'}; force on Z: repulsion": "Both parts are wrong: check which poles of X and Y face each other, and remember soft iron is always attracted."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="Fig. 1 shows three bars in a line. X and Y are bar magnets with the poles shown. Z is a bar of soft iron. What are the magnetic forces "
                     "on X and on Z due to magnet Y?",
                options=opts, key=key, misconceptions=mis, formula="like poles repel, unlike poles attract; a magnet always attracts unmagnetised iron (induced magnetism)",
                working=[f"X's {x_poles[1]} pole faces Y's {y_poles[0]} pole → {fx}.", "Y's S pole induces an N pole in the near end of the soft iron Z → attraction.",
                         f"Correct answer: **{correct}**", cite(35)],
                hints=["Look at the two poles that face each other across the gap between X and Y.", "Soft iron is not a magnet until a magnet is near it.",
                       "A magnet induces the opposite pole in the nearest end of a piece of iron."],
                figure=k5.three_bars((x_poles, y_poles)))


# ================================================================== Ch 18 Electromagnetism
explain_mcqs([
    dict(id="o26_two_wires_field", chapter=18, level=4, lo="18a", source=src(36),
         stem="Fig. 1 is a cross-section through two long parallel wires. Wire 1 carries a current into the page and wire 2 carries an equal current out of the "
              "page. Which statement about the magnetic field in the region between the wires is correct?",
         correct="The fields of the two wires point the same way there, so the field between the wires is stronger than on the outside.",
         wrongs={"The fields of the two wires point in opposite directions there, so they cancel between the wires.": "Use the right-hand grip rule on each wire: with opposite currents, the two circular fields run the SAME way in the gap between them.",
                 "The field lines between the wires are straight lines parallel to the wires.": "The field of a straight wire is circles around the wire; between the wires the lines curve, they are not parallel to the wires.",
                 "There is no magnetic field between the wires because the currents are equal and opposite.": "Each wire produces its own field whatever the other does; equal and opposite currents reinforce the field between the wires."},
         hints=["Use the right-hand grip rule on wire 1 (current into the page): clockwise circles.", "Do the same for wire 2 (current out of the page): anticlockwise circles.",
                "In the gap between the wires, which way does each field point?"],
         figure=lambda: k5.two_wires_section(opposite=True)),
], category=CAT)


# ================================================================== Ch 19 Electromagnetic induction
explain_mcqs([
    dict(id="o26_generator_output", chapter=19, level=2, lo="19c", source=src(37),
         stem="A coil is rotated steadily between the poles of a magnet. Its ends are connected through slip rings and brushes to an output. "
              "Which graph describes the output voltage V against time t?",
         correct="a smooth wave that is alternately positive and negative, repeating regularly",
         wrongs={"a series of humps that are all positive": "Humps that are all positive are the output of a generator with a split-ring commutator (a d.c. generator), not slip rings.",
                 "a constant value that does not change with time": "A steady voltage would need a steady rate of change of flux. The coil's rate of cutting field lines changes continuously as it turns.",
                 "zero at all times": "The coil cuts the field lines as it turns, so an e.m.f. IS induced; it is zero only at the instants the coil is perpendicular to the field."},
         hints=["Slip rings keep each end of the coil connected to the same brush all the time.", "Every half turn the coil's sides swap direction through the field, so the e.m.f. reverses.",
                "The e.m.f. is greatest when the coil cuts the field fastest and zero when it moves along the field lines."]),
], category=CAT)


@template("o26_transformer_lamp", chapter=19, level=2, lo="19e", category=CAT)
def transformer_lamp(rng):
    Np, Ns, Vp = nice(rng, (40, 200, 12.0), (50, 200, 12.0), (40, 160, 6.0), (60, 240, 12.0))
    Vs = Vp * Ns / Np
    return calc_q(rng, f"Fig. 1 shows a lamp connected to the secondary coil of a transformer. The primary coil has **{Np} turns** and is connected to a "
                  f"**{fmt(Vp)} V** a.c. supply; the secondary coil has **{Ns} turns**. What is the potential difference across the lamp?", Vs,
                  [(Vp * Np / Ns, "The turns ratio is upside down: V_s / V_p = N_s / N_p, so more turns on the secondary means a HIGHER voltage."),
                   (Vp, "A transformer changes the voltage: the secondary p.d. equals the primary p.d. only when the coils have the same number of turns."),
                   (Vp * (Ns - Np) / Np, "The turns are compared as a RATIO N_s / N_p, not as a difference.")],
                  "V", "V_s / V_p = N_s / N_p",
                  [f"V_s = V_p × N_s / N_p = {fmt(Vp)} × {Ns} / {Np} = **{fmt(Vs)} V**", cite(38)],
                  ["For an ideal transformer the voltages are in the same ratio as the numbers of turns.", "More turns on the secondary → a step-up transformer.",
                   f"V_s = {fmt(Vp)} × ({Ns} ÷ {Np})."],
                  figure=figs3.transformer(np_label=f"{Np} turns", ns_label=f"{Ns} turns", vp_label=f"{fmt(Vp)} V a.c.", vs_label="lamp", n_p=4, n_s=10))


# ================================================================== Ch 20 Radioactivity
@template("o26_nuclide_statement", chapter=20, level=3, lo="20c", category=CAT)
def nuclide_statement(rng):
    A, Z, X = nice(rng, (205, 81, "Tl"), (207, 82, "Pb"), (209, 83, "Bi"), (201, 80, "Hg"))
    N = A - Z
    correct = f"There are {N - Z} more neutrons than electrons in the atom."
    wrongs = {f"There are {Z} electrons in the nucleus of the atom.": "Electrons are outside the nucleus. The nucleus holds protons and neutrons only.",
              f"There are {A} neutrons in the nucleus of the atom.": f"{A} is the nucleon number: protons AND neutrons together. Neutrons = {A} − {Z} = {N}.",
              f"There are {N} protons in the nucleus of the atom.": f"The proton number is the lower number, {Z}. {N} is the number of neutrons."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"Fig. 1 shows the nuclide notation of a neutral atom of {X}. Which statement about this atom is correct?",
                options=opts, key=key, misconceptions=mis, formula="A = nucleon number, Z = proton number; neutrons = A − Z; electrons = Z in a neutral atom",
                working=[f"Protons = Z = {Z}; neutrons = A − Z = {A} − {Z} = {N}; electrons = {Z} (neutral atom).",
                         f"Neutrons − electrons = {N} − {Z} = {N - Z}.", f"Correct answer: **{correct}**", cite(39)],
                hints=["The upper number is the nucleon number A (protons + neutrons); the lower number is the proton number Z.",
                       "Neutrons = A − Z.", "In a neutral atom the number of electrons equals the number of protons."],
                figure=figs3.nuclide(A, Z, X))


@template("o26_beam_splits_field", chapter=20, level=5, lo="20e", category=CAT)
def beam_splits_field(rng):
    curve_up = rng.random() < 0.5
    charged = "α-particles" if curve_up else "β-particles"
    other = "β-particles" if curve_up else "α-particles"
    correct = f"{charged} and γ-rays only"
    wrongs = {f"{other} and γ-rays only": f"The curved path bends {'upwards' if curve_up else 'downwards'}. With the field into the page, Fleming's left-hand rule gives that direction for a "
                                           f"{'positive' if curve_up else 'negative'} charge, so the curved path is {charged}, not {other}.",
              "α-particles and β-particles only": "The path that is NOT deflected must be uncharged radiation: γ-rays. Two charged types would give two curved paths.",
              "α-particles, β-particles and γ-rays": "Three types would leave three paths: two curved (in opposite directions) and one straight. Only one curved path is seen."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="A beam of radiation from a source enters a region of very strong uniform magnetic field directed into the page, in a vacuum. "
                     "Fig. 1 shows that the beam splits into a straight path and ONE curved path. What types of radiation are in the beam?",
                options=opts, key=key, misconceptions=mis, formula="γ: uncharged, not deflected; α positive and β negative are deflected in opposite directions (Fleming's left-hand rule)",
                working=["The straight path is undeflected, so it is uncharged radiation: γ-rays.",
                         f"Only one curved path, so only one charged type is present. It curves {'upwards' if curve_up else 'downwards'}: for a field into the page and a beam moving to the right, "
                         f"Fleming's left-hand rule gives an upward force on a POSITIVE charge, so this is {'α (positive)' if curve_up else 'β (negative, pushed the opposite way)'}.",
                         f"Correct answer: **{correct}**", cite(40)],
                hints=["Which type of radiation is not deflected by a magnetic field at all?", "A charged particle moving across a magnetic field is pushed sideways: use Fleming's left-hand rule (conventional current = direction a positive charge moves).",
                       "How many charged types can there be if there is only one curved path?"],
                figure=k5.beam_in_field(curve_up))
