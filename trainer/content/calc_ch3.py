"""Chapter 3 Force and Pressure: weight, density, pressure."""
from .. import figs, sketches
from ..config import G
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c3_weight_from_mass", chapter=3, level=1, lo="3e")
def weight_from_mass(rng):
    m = nice(rng, 0.5, 2.5, 4, 6, 12, 25, 40, 60)
    W = m * G
    opts, key, mis = numeric_options(rng, W, [
        (m / G, "You divided by g. Weight = mass × g."),
        (m, "That is the mass in kg. Weight is a force, measured in newtons: W = mg."),
        (m * G * 10, "You used g = 100 N/kg. On Earth g = 10 N/kg."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a bag of rice of mass **{fmt(m)} kg** hanging from a spring balance. Taking the gravitational field strength g = 10 N/kg, what is the reading on the balance, i.e. the weight of the bag?",
        figure=sketches.spring_balance("? N", f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="weight = mass × gravitational field strength (W = mg)",
        working=["W = mg", f"= {fmt(m)} × 10", f"= **{fmt(W)} N**"],
        hints=["Weight is the gravitational force on a mass. Which formula links weight, mass and g?",
               f"g = 10 N/kg means every kilogram is pulled with a force of 10 N. The bag has {fmt(m)} kg.",
               f"W = {fmt(m)} × 10."],
    )


@template("c5_density_direct", chapter=5, level=1, lo="5d")
def density_direct(rng):
    rho = nice(rng, 0.8, 1.2, 2.5, 2.7, 4, 7.9, 8.9)
    V = nice(rng, 10, 20, 25, 40, 50, 100)
    m = round(rho * V, 2)
    opts, key, mis = numeric_options(rng, rho, [
        (V / m, "You divided volume by mass. Density = mass ÷ volume."),
        (m * V, "You multiplied. Density = mass ÷ volume."),
        (m / V / 10, "You divided by an extra 10. Check the division."),
    ], unit="g/cm³")
    return dict(
        stem=f"Fig. 1 shows a piece of metal of mass **{fmt(m)} g** and volume **{V} cm³**. What is the density of the metal?",
        figure=sketches.lump_sketch([f"mass = {fmt(m)} g", f"volume = {V} cm³"]),
        options=opts, key=key, misconceptions=mis,
        formula="density = mass ÷ volume",
        working=["density = mass ÷ volume", f"= {fmt(m)} ÷ {V}", f"= **{fmt(rho)} g/cm³**"],
        hints=["Density tells you how much mass is packed into each unit of volume. Which formula is that?",
               f"Mass = {fmt(m)} g, volume = {V} cm³. The unit g/cm³ tells you the order: grams divided by cm³.",
               f"density = {fmt(m)} ÷ {V}."],
    )


@template("c5_pressure_direct", chapter=5, level=1, lo="5b")
def pressure_direct(rng):
    F = nice(rng, 60, 120, 200, 240, 480, 600)
    A = nice(rng, 0.02, 0.04, 0.05, 0.1, 0.2, 0.5)
    p = F / A
    opts, key, mis = numeric_options(rng, p, [
        (F * A, "You multiplied force by area. Pressure = force ÷ area."),
        (A / F, "You divided area by force, the wrong way round."),
        (F / A / 10, "Check the division: dividing by a decimal makes the answer LARGER than the force."),
    ], unit="Pa")
    return dict(
        stem=f"Fig. 1 shows a force of **{F} N** acting at right angles on a block whose base has an area of **{fmt(A)} m²**. What is the pressure the block exerts on the floor due to this force?",
        figure=sketches.pressure_block(f"F = {F} N", f"area of base = {fmt(A)} m²"),
        options=opts, key=key, misconceptions=mis,
        formula="pressure = force ÷ area (p = F/A)",
        working=["p = F ÷ A", f"= {F} ÷ {fmt(A)}", f"= **{fmt(p)} Pa**"],
        hints=["Pressure is force per unit area. Which way round is the division?",
               f"F = {F} N and A = {fmt(A)} m². Dividing by a number smaller than 1 gives a bigger number.",
               f"p = {F} ÷ {fmt(A)}."],
    )


# ---------------------------------------------------------------- L2
@template("c3_mass_from_weight", chapter=3, level=2, lo="3e")
def mass_from_weight(rng):
    m = nice(rng, 0.6, 1.5, 3.2, 4.5, 7, 15, 48, 65)
    W = m * G
    opts, key, mis = numeric_options(rng, m, [
        (W * G, "You multiplied by g. To find mass from weight, divide: m = W ÷ g."),
        (W, "That is the weight in newtons. Mass is in kilograms: m = W ÷ g."),
        (W - G, "You subtracted g. Rearrange W = mg to get m = W ÷ g."),
    ], unit="kg")
    return dict(
        stem=f"Fig. 1 shows an object hanging from a spring balance on Earth, where g = 10 N/kg. The balance reads **{fmt(W)} N**. What is the mass of the object?",
        figure=sketches.spring_balance(f"{fmt(W)} N", "mass = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="W = mg, rearranged: m = W ÷ g",
        working=["W = mg  →  m = W ÷ g", f"= {fmt(W)} ÷ 10", f"= **{fmt(m)} kg**"],
        hints=["You know the weight and g. Rearrange W = mg to make m the subject.",
               f"Every 10 N of weight comes from 1 kg of mass. How many lots of 10 N are in {fmt(W)} N?",
               f"m = {fmt(W)} ÷ 10."],
    )


@template("c5_pressure_area_cm2", chapter=5, level=2, lo="5b")
def pressure_area_cm2(rng):
    F = nice(rng, 20, 50, 80, 120, 150, 300)
    A_cm2 = nice(rng, 20, 25, 40, 50, 80, 200)
    A = A_cm2 / 10000
    p = F / A
    opts, key, mis = numeric_options(rng, p, [
        (F / A_cm2, "You left the area in cm². Pressure in pascals needs the area in m² (1 m² = 10 000 cm²)."),
        (F / (A_cm2 / 100), "You used 1 m² = 100 cm². In fact 1 m² = 100 cm × 100 cm = 10 000 cm²."),
        (F * A_cm2, "You multiplied force by area. Pressure = force ÷ area."),
    ], unit="Pa")
    return dict(
        stem=f"Fig. 1 shows a force of **{F} N** acting at right angles on a block whose base has an area of **{A_cm2} cm²**. What is the pressure on the floor due to this force, in pascals?",
        figure=sketches.pressure_block(f"F = {F} N", f"area of base = {A_cm2} cm²"),
        options=opts, key=key, misconceptions=mis,
        formula="p = F ÷ A with A in m² (cm² ÷ 10 000)",
        working=[f"A = {A_cm2} cm² = {A_cm2} ÷ 10 000 m² = {fmt(A, sf=4)} m²", f"p = {F} ÷ {fmt(A, sf=4)}", f"= **{fmt(p)} Pa**"],
        hints=["1 Pa = 1 N/m². Which of the given quantities is not yet in the right unit?",
               f"1 m = 100 cm, so 1 m² = 100 × 100 = 10 000 cm². Convert {A_cm2} cm² to m² first.",
               f"p = {F} ÷ ({A_cm2} ÷ 10 000)."],
    )


@template("c5_density_from_cylinder", chapter=5, level=2, lo="5d")
def density_from_cylinder(rng):
    V = nice(rng, 24, 36, 42, 48, 56, 64, 78)
    rho = nice(rng, 0.8, 1.2, 1.5, 2.0, 2.5)
    m = round(rho * V, 1)
    opts, key, mis = numeric_options(rng, rho, [
        (V / m, "You divided volume by mass. Density = mass ÷ volume."),
        (m / (V + 2), "Check the reading: each small division on the cylinder is 2 cm³. Read the bottom of the meniscus."),
        (m / (V - 2), "Check the reading: each small division on the cylinder is 2 cm³. Read the bottom of the meniscus."),
    ], unit="g/cm³")
    return dict(
        stem=f"A liquid of mass **{fmt(m)} g** is poured into a measuring cylinder. Fig. 1 shows the level of the liquid. What is the density of the liquid?",
        figure=figs.measuring_cylinder(V),
        options=opts, key=key, misconceptions=mis,
        formula="density = mass ÷ volume (read the volume from the cylinder, bottom of the meniscus)",
        working=[f"volume from Fig. 1 = {V} cm³ (each small division = 2 cm³)", f"density = {fmt(m)} ÷ {V}", f"= **{fmt(rho)} g/cm³**"],
        hints=["Two steps: read the volume from the cylinder, then use the density formula. What is each small division worth?",
               f"Between the numbered marks there are 5 small divisions of 2 cm³ each. The meniscus is at {V} cm³.",
               f"density = {fmt(m)} ÷ {V}."],
    )


# ---------------------------------------------------------------- L3
@template("c5_density_of_block", chapter=5, level=3, lo="5d")
def density_of_block(rng):
    a, b, c = rng.choice([(2, 5, 10), (4, 5, 10), (2, 4, 5), (5, 5, 8), (4, 10, 10), (2, 5, 20), (5, 8, 10)])
    rho = nice(rng, 0.5, 0.8, 1.2, 2.5, 2.7, 4.0, 8.0)
    V = a * b * c
    m = round(rho * V, 1)
    opts, key, mis = numeric_options(rng, rho, [
        (m / (a + b + c), "You ADDED the dimensions. Volume of a cuboid = length × breadth × height."),
        (m / (a * b), "You used the area of one face. Volume needs all three dimensions multiplied."),
        (V / m, "You divided volume by mass. Density = mass ÷ volume."),
    ], unit="g/cm³")
    return dict(
        stem=f"Fig. 1 shows a rectangular block measuring **{a} cm × {b} cm × {c} cm**. The block has a mass of **{fmt(m)} g**. What is the density of the block?",
        figure=figs.labelled_block(a, b, c),
        options=opts, key=key, misconceptions=mis,
        formula="volume = length × breadth × height, then density = mass ÷ volume",
        working=[f"volume = {a} × {b} × {c} = {V} cm³", f"density = {fmt(m)} ÷ {V}", f"= **{fmt(rho)} g/cm³**"],
        hints=["You are not given the volume directly. How do you find the volume of a rectangular block?",
               f"volume = {a} × {b} × {c} = {V} cm³. Now use density = mass ÷ volume.",
               f"density = {fmt(m)} ÷ {V}."],
    )


@template("c5_pressure_of_block", chapter=5, level=3, lo="5b")
def pressure_of_block(rng):
    a, b, c = rng.choice([(10, 20, 30), (5, 10, 20), (20, 25, 40), (10, 40, 50), (8, 25, 40), (10, 10, 25)])
    W = nice(rng, 20, 40, 60, 80, 100, 150)
    A_cm2 = a * b
    A = A_cm2 / 10000
    p = W / A
    opts, key, mis = numeric_options(rng, p, [
        (W / A_cm2, "You left the area in cm². Convert to m²: 1 m² = 10 000 cm²."),
        (W / (A_cm2 / 100), "You used 1 m² = 100 cm². It is 100 × 100 = 10 000 cm²."),
        (W / (a * c / 10000), "You used the wrong face. The block rests on the face measuring " + f"{a} cm by {b} cm."),
    ], unit="Pa")
    return dict(
        stem=f"A block of weight **{W} N** rests on a horizontal floor on its face measuring **{a} cm by {b} cm** (Fig. 1). What is the pressure exerted by the block on the floor?",
        figure=figs.labelled_block(a, b, c),
        options=opts, key=key, misconceptions=mis,
        formula="p = F ÷ A, where F is the weight and A is the area of the face in contact, in m²",
        working=[f"area in contact = {a} × {b} = {A_cm2} cm² = {fmt(A, sf=4)} m²", f"p = {W} ÷ {fmt(A, sf=4)}", f"= **{fmt(p)} Pa**"],
        hints=["Which force presses on the floor, and which face is in contact? Then p = F ÷ A.",
               f"The face in contact is {a} cm × {b} cm = {A_cm2} cm². Pressure in Pa needs m²: divide by 10 000.",
               f"p = {W} ÷ ({A_cm2} ÷ 10 000)."],
    )


# ---------------------------------------------------------------- L4
@template("c5_density_weight_pressure", chapter=5, level=4, lo="5b")
def density_weight_pressure(rng):
    a, b, c = rng.choice([(4, 10, 20), (5, 10, 20), (2, 10, 25), (4, 5, 25), (5, 20, 20), (10, 10, 40)])
    rho = nice(rng, 0.5, 2.0, 2.5, 4.0, 5.0, 8.0)
    V = a * b * c
    m_kg = rho * V / 1000
    W = m_kg * G
    dims = sorted([a, b, c])
    A_small = dims[0] * dims[1] / 10000
    A_large = dims[1] * dims[2] / 10000
    p = W / A_small
    opts, key, mis = numeric_options(rng, p, [
        (W / A_large, "You used the largest face. The pressure is greatest when the block stands on its SMALLEST face."),
        (W / (dims[0] * dims[1]), "You left the area in cm². Convert to m² (÷ 10 000)."),
        (m_kg / A_small, "You used the mass instead of the weight. The force on the floor is the weight, W = mg."),
    ], unit="Pa")
    return dict(
        stem=f"Fig. 1 shows a block measuring **{a} cm × {b} cm × {c} cm** made of a material of density **{fmt(rho)} g/cm³**. Taking g = 10 N/kg, what is the **greatest** pressure the block can exert when it rests on a horizontal floor?",
        figure=figs.labelled_block(a, b, c),
        options=opts, key=key, misconceptions=mis,
        formula="mass = density × volume; W = mg; p = W ÷ A using the smallest face (in m²)",
        working=[f"volume = {a} × {b} × {c} = {V} cm³; mass = {fmt(rho)} × {V} = {fmt(rho * V)} g = {fmt(m_kg)} kg",
                 f"weight = {fmt(m_kg)} × 10 = {fmt(W)} N",
                 f"smallest face = {dims[0]} × {dims[1]} = {dims[0] * dims[1]} cm² = {fmt(A_small, sf=4)} m²",
                 f"p = {fmt(W)} ÷ {fmt(A_small, sf=4)} = **{fmt(p)} Pa**"],
        hints=["Three steps: find the mass from the density, turn it into a weight, then divide by an area. Which face gives the GREATEST pressure?",
               f"mass = {fmt(rho)} × {V} g = {fmt(m_kg)} kg, so W = {fmt(W)} N. The smallest face is {dims[0]} cm × {dims[1]} cm.",
               f"p = {fmt(W)} ÷ ({dims[0] * dims[1]} ÷ 10 000)."],
    )


@template("c5_density_by_displacement", chapter=5, level=4, lo="5d")
def density_by_displacement(rng):
    V1 = nice(rng, 30, 36, 40, 44, 50)
    dV = nice(rng, 8, 10, 12, 16, 20, 24)
    V2 = V1 + dV
    rho = nice(rng, 2.5, 2.7, 3.0, 4.0, 7.5, 8.0)
    m = round(rho * dV, 1)
    opts, key, mis = numeric_options(rng, rho, [
        (m / V2, "You used the final reading. The stone's volume is the INCREASE in the reading, after − before."),
        (m / V1, "You used the first reading, which is the water alone."),
        (dV / m, "You divided volume by mass. Density = mass ÷ volume."),
    ], unit="g/cm³")
    return dict(
        stem=f"A stone of mass **{fmt(m)} g** is lowered into a measuring cylinder containing water. Fig. 1 shows the cylinder before and after. What is the density of the stone?",
        figure=figs.two_cylinders(V1, V2),
        options=opts, key=key, misconceptions=mis,
        formula="volume of stone = reading after − reading before; density = mass ÷ volume",
        working=[f"volume of stone = {V2} − {V1} = {dV} cm³", f"density = {fmt(m)} ÷ {dV}", f"= **{fmt(rho)} g/cm³**"],
        hints=["The stone is irregular, so its volume comes from the water it pushes aside. How do you get that from the two readings?",
               f"Before: {V1} cm³. After: {V2} cm³. The stone's volume is the difference, {dV} cm³.",
               f"density = {fmt(m)} ÷ {dV}."],
    )


# ---------------------------------------------------------------- L5
@template("c3_weight_on_moon", chapter=3, level=5, lo="3f")
def weight_on_moon(rng):
    m = nice(rng, 1.5, 2.5, 4, 6, 7.5, 12, 48, 60)
    g_moon = 1.6
    W_e = m * G
    W_m = m * g_moon
    opts, key, mis = numeric_options(rng, W_m, [
        (W_e * g_moon, "You multiplied the EARTH WEIGHT by 1.6. Find the mass first (W ÷ 10), then multiply the mass by 1.6."),
        (m, "That is the mass, which stays the same everywhere, but the question asks for the weight on the Moon."),
        (W_e / g_moon, "You divided by 1.6. Weight = mass × g, with g = 1.6 N/kg on the Moon."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a rock that has a weight of **{fmt(W_e)} N** on Earth, where g = 10 N/kg. On the Moon the gravitational field strength is **1.6 N/kg**. What is the weight of the rock on the Moon?",
        figure=sketches.two_bodies_sketch(["g = 10 N/kg", f"weight of rock = {fmt(W_e)} N"], ["g = 1.6 N/kg", "weight of rock = ?"]),
        options=opts, key=key, misconceptions=mis,
        formula="m = W ÷ g (on Earth), then W = m × g (on the Moon); mass does not change",
        working=[f"mass = {fmt(W_e)} ÷ 10 = {fmt(m)} kg (the same on the Moon)", f"weight on Moon = {fmt(m)} × 1.6", f"= **{fmt(W_m)} N**"],
        hints=["Which quantity stays the same when the rock goes to the Moon: its mass or its weight?",
               f"Find the mass from the Earth weight: m = {fmt(W_e)} ÷ 10 = {fmt(m)} kg.",
               f"weight on Moon = {fmt(m)} × 1.6."],
    )


@template("c5_density_of_mixture", chapter=5, level=5, lo="5d")
def density_of_mixture(rng):
    rho1, rho2 = rng.choice([(0.8, 1.2), (0.8, 1.0), (1.0, 1.5), (0.9, 1.3), (0.6, 1.2), (1.0, 2.0)])
    V1 = nice(rng, 100, 200, 300, 400)
    V2 = nice(rng, 100, 200, 300, 600)
    m1, m2 = rho1 * V1, rho2 * V2
    rho = (m1 + m2) / (V1 + V2)
    opts, key, mis = numeric_options(rng, rho, [
        ((rho1 + rho2) / 2, "You averaged the two densities. That only works if the volumes are equal. Use total mass ÷ total volume."),
        ((m1 + m2) / V1, "You divided the total mass by the volume of the first liquid only."),
        (rho1 + rho2, "You added the densities. Density of the mixture = total mass ÷ total volume."),
    ], unit="g/cm³")
    return dict(
        stem=f"Fig. 1 shows two liquids. **{V1} cm³** of liquid X (density **{fmt(rho1)} g/cm³**) is mixed with **{V2} cm³** of liquid Y (density **{fmt(rho2)} g/cm³**). The liquids mix completely with no change in total volume. What is the density of the mixture?",
        figure=sketches.beakers_sketch([("X", f"{V1} cm³", f"{fmt(rho1)} g/cm³"), ("Y", f"{V2} cm³", f"{fmt(rho2)} g/cm³")]),
        options=opts, key=key, misconceptions=mis,
        formula="density of mixture = total mass ÷ total volume (mass = density × volume for each liquid)",
        working=[f"mass of X = {fmt(rho1)} × {V1} = {fmt(m1)} g; mass of Y = {fmt(rho2)} × {V2} = {fmt(m2)} g",
                 f"total mass = {fmt(m1 + m2)} g; total volume = {V1 + V2} cm³",
                 f"density = {fmt(m1 + m2)} ÷ {V1 + V2} = **{fmt(rho)} g/cm³**"],
        hints=["Density of a mixture is NOT the average of the densities. Go back to the definition: what two totals do you need?",
               f"Mass of X = {fmt(rho1)} × {V1} = {fmt(m1)} g; mass of Y = {fmt(rho2)} × {V2} = {fmt(m2)} g.",
               f"density = ({fmt(m1)} + {fmt(m2)}) ÷ ({V1} + {V2})."],
    )
