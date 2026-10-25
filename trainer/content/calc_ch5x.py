"""Chapter 5 Pressure (6091) bank extension: calculation templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2016-2025: porcelain tile, cement mixer on a board, thumb tack, aeroplane window,
syringe with a capped nozzle, salt blocks, oil and water in a U-tube, tracked vehicle on marshy ground)."""
from .. import figs2
from .base import fmt, md_table, mk, mkt, nice, template

G = 10
RHO_W, RHO_HG = 1000, 13600


# ================================================================== L1
@template("c5x_box_pressure", chapter=5, level=1, lo="5b")
def box_pressure(rng):
    W = nice(rng, 200, 300, 400, 600, 900)
    A = nice(rng, 0.2, 0.25, 0.4, 0.5)
    p = W / A
    return mk(rng, p, [(W * A, "Pressure = force ÷ area, not × area."), (A / W, "Pressure = force ÷ area: the force goes on top."), (W, "Divide the weight by the area.")],
              "Pa", f"A box rests on the floor.\n\n{md_table(['quantity', 'value'], [['weight of box', f'{W} N'], ['area in contact with the floor', f'{fmt(A)} m²']])}\n\nWhat pressure does it exert on the floor?",
              "p = F ÷ A", [f"p = {W} ÷ {fmt(A)} = **{fmt(p)} Pa**"],
              ["Pressure = force ÷ area.", "The force is the weight of the box.", "Divide."])


@template("c5x_density_simple", chapter=5, level=1, lo="5d")
def density_simple(rng):
    m = nice(rng, 54, 81, 108, 135, 270)
    V = nice(rng, 20, 30, 40, 50)
    rho = m / V
    return mk(rng, rho, [(V / m, "Density = mass ÷ volume, not volume ÷ mass."), (m * V, "Divide mass by volume."), (m / V * 1000, "The answer is in g/cm³; no conversion is needed.")],
              "g/cm³", f"A small metal block is measured.\n\n{md_table(['quantity', 'value'], [['mass', f'{m} g'], ['volume', f'{V} cm³']])}\n\nWhat is its density?",
              "ρ = m ÷ V", [f"ρ = {m} ÷ {V} = **{fmt(rho)} g/cm³**"],
              ["Density = mass ÷ volume.", "Both values are in g and cm³.", "Divide."])


@template("c5x_pool_bottom", chapter=5, level=1, lo="5e")
def pool_bottom(rng):
    h = nice(rng, 1.2, 1.5, 1.8, 2.0, 2.5)
    p = h * RHO_W * G
    return mk(rng, p, [(h * RHO_W, "Include g = 10 N/kg: p = h ρ g."), (h * G, "Include the density of water, 1000 kg/m³."), (p * 10, "Check the multiplication: h × 1000 × 10.")],
              "Pa", f"Fig. 1 shows a swimming pool of water that is **{fmt(h)} m** deep at point X on the bottom. The density of water is 1000 kg/m³ and g = 10 N/kg. What is the pressure at X due to the water?",
              "p = h ρ g", [f"p = {fmt(h)} × 1000 × 10 = **{fmt(p)} Pa**"],
              ["Pressure in a liquid depends on depth, density and g.", "p = h ρ g.", "Multiply the three."], figure=figs2.liquid_column(f"{fmt(h)} m", "water", "X"))


@template("c5x_greatest_pressure_point", chapter=5, level=1, lo="5e")
def greatest_pressure_point(rng):
    rows = [("P", nice(rng, 2.0, 2.5), 800), ("Q", nice(rng, 1.5, 1.8), 1000), ("R", nice(rng, 1.0, 1.2), 1200), ("S", nice(rng, 0.4, 0.5), 13600)]
    rng.shuffle(rows)
    ps = {n: h * r * G for n, h, r in rows}
    best = max(ps, key=ps.get)
    deepest = max(rows, key=lambda t: t[1])[0]
    wrongs = {n: ("That point is the deepest, but the density of the liquid matters too." if n == deepest else "Work out h × ρ for each point and compare.") for n in ps if n != best}
    table = md_table(["point", "depth / m", "density of liquid / kg/m³"], [[n, fmt(h), r] for n, h, r in rows])
    return mkt(rng, best, wrongs, f"Four points are in different liquids.\n\n{table}\n\nAt which point is the pressure due to the liquid greatest?",
               "p = h ρ g: compare h × ρ", [", ".join(f"{n}: {fmt(ps[n])} Pa" for n, _, _ in rows), f"greatest: **{best}**"],
               ["Pressure depends on depth AND density.", "Work out h × ρ × g for each.", "Pick the largest."])


@template("c5x_barometer_reading", chapter=5, level=1, lo="5f")
def barometer_reading(rng):
    top = nice(rng, 755, 760, 765, 770, 780)
    surf = nice(rng, 10, 15, 20, 25)
    h = top - surf
    return mk(rng, h, [(top, "Measure from the mercury surface in the dish, not from the zero of the scale."), (top + surf, "Subtract the dish level from the top of the column."), (h / 10, "The answer is in mm Hg.")],
              "mm Hg", f"A metre rule is held beside a mercury barometer.\n\n{md_table(['level', 'scale reading / mm'], [['top of mercury column', top], ['mercury surface in dish', surf]])}\n\nWhat is the atmospheric pressure in mm of mercury?",
              "h = vertical height of the column above the mercury surface in the dish", [f"h = {top} − {surf} = **{h} mm Hg**"],
              ["The pressure is measured by the vertical height of mercury.", "Height above the surface in the dish.", "Subtract."], dp=0)


@template("c5x_atmos_force_lid", chapter=5, level=1, lo="5f")
def atmos_force_lid(rng):
    p = 1.0e5
    A = nice(rng, 0.01, 0.02, 0.05, 0.1)
    F = p * A
    return mk(rng, F, [(p / A, "Force = pressure × area."), (A, "Multiply the area by the pressure."), (F / 10, "Check: 1.0 × 10⁵ × area.")],
              "N", f"Atmospheric pressure acts on the outside of a lid.\n\n{md_table(['quantity', 'value'], [['atmospheric pressure', '1.0 × 10⁵ Pa'], ['area of lid', f'{fmt(A)} m²']])}\n\nWhat force does the atmosphere exert on the lid?",
              "F = p A", [f"F = 1.0 × 10⁵ × {fmt(A)} = **{fmt(F)} N**"],
              ["Rearrange p = F ÷ A.", "F = p × A.", "Multiply."])


@template("c5x_hydraulic_same_pressure", chapter=5, level=1, lo="5c")
def hydraulic_same_pressure(rng):
    F1 = nice(rng, 20, 40, 50, 80)
    A1 = nice(rng, 0.002, 0.004, 0.005)
    A2 = A1 * nice(rng, 10, 20, 25)
    p = F1 / A1
    return mk(rng, p, [(F1 / A2, "The pressure is produced by the small piston; use its area."), (F1 * A1, "p = F ÷ A."), (p * A2 / A1, "Pressure is transmitted unchanged: it is the same at both pistons.")],
              "Pa", f"In the hydraulic press of Fig. 1, a force of **{F1} N** pushes on the small piston of area **{fmt(A1)} m²**. The large piston has area **{fmt(A2)} m²**. What is the pressure on the large piston?",
              "pressure is transmitted equally through the liquid: p = F₁ ÷ A₁", [f"p = {F1} ÷ {fmt(A1)} = **{fmt(p)} Pa**, the same at both pistons"],
              ["Liquids transmit pressure equally.", "Find the pressure at the small piston.", "It is the same at the large one."], figure=figs2.hydraulic_press(f"{F1} N", f"{fmt(A1)} m²", f"{fmt(A2)} m²", "?"))


@template("c5x_hydraulic_force_from_p", chapter=5, level=1, lo="5c")
def hydraulic_force_from_p(rng):
    p = nice(rng, 2.0e4, 4.0e4, 5.0e4, 8.0e4)
    A2 = nice(rng, 0.05, 0.1, 0.2)
    F2 = p * A2
    return mk(rng, F2, [(p / A2, "Force = pressure × area."), (p, "That is the pressure; multiply by the area."), (F2 / 10, "Check the multiplication.")],
              "N", f"The pressure in the liquid of a hydraulic lift (Fig. 1) is **{fmt(p)} Pa**. The large piston has area **{fmt(A2)} m²**. What upward force acts on it?",
              "F = p A", [f"F = {fmt(p)} × {fmt(A2)} = **{fmt(F2)} N**"],
              ["The pressure acts on the whole piston.", "F = p × A.", "Multiply."], figure=figs2.hydraulic_press("", "", f"{fmt(A2)} m²", "F = ?"))


# ================================================================== L2
@template("c5x_thumb_tack", chapter=5, level=2, lo="5b")
def thumb_tack(rng):
    F = nice(rng, 12, 15, 18, 20)
    a_mm = nice(rng, 0.2, 0.4, 0.5)
    p = F / (a_mm * 1e-6)
    return mk(rng, p, [(F / a_mm, "Convert mm² to m²: 1 mm² = 1 × 10⁻⁶ m²."), (F / (a_mm * 1e-3), "1 mm² = 10⁻⁶ m², not 10⁻³ m²."), (F * a_mm * 1e-6, "Pressure = force ÷ area.")],
              "Pa", f"A thumb tack is pushed into a notice board.\n\n{md_table(['quantity', 'value'], [['force on tack', f'{F} N'], ['area of the point', f'{fmt(a_mm)} mm²']])}\n\nWhat pressure does the point exert on the board?",
              "p = F ÷ A, with A in m² (1 mm² = 10⁻⁶ m²)", [f"A = {fmt(a_mm)} × 10⁻⁶ m²", f"p = {F} ÷ ({fmt(a_mm)} × 10⁻⁶) = **{fmt(p)} Pa**"],
              ["Convert the area to m².", "1 mm² = 10⁻⁶ m².", "Then p = F ÷ A."])


@template("c5x_mass_from_density", chapter=5, level=2, lo="5d")
def mass_from_density(rng):
    rho = nice(rng, 2.7, 7.9, 8.9, 11.3)
    V = nice(rng, 20, 25, 40, 50)
    m = rho * V
    return mk(rng, m, [(V / rho, "m = ρ × V, not V ÷ ρ."), (rho / V, "Multiply density by volume."), (m / 1000, "The answer is in grams.")],
              "g", f"A metal sample is cut from a block.\n\n{md_table(['quantity', 'value'], [['density of metal', f'{fmt(rho)} g/cm³'], ['volume of sample', f'{V} cm³']])}\n\nWhat is the mass of the sample?",
              "m = ρ V", [f"m = {fmt(rho)} × {V} = **{fmt(m)} g**"],
              ["Rearrange ρ = m ÷ V.", "m = ρ × V.", "Multiply."])


@template("c5x_pressure_difference_depths", chapter=5, level=2, lo="5e")
def pressure_difference_depths(rng):
    h1 = nice(rng, 0.5, 1.0, 1.5)
    h2 = h1 + nice(rng, 1.0, 1.5, 2.0, 2.5)
    rho = nice(rng, 1000, 1030)
    dp = (h2 - h1) * rho * G
    return mk(rng, dp, [(h2 * rho * G, "That is the pressure at the deeper point; find the DIFFERENCE."), ((h1 + h2) * rho * G, "Subtract the depths, not add."), ((h2 - h1) * rho, "Include g.")],
              "Pa", f"Two points are in a tank of liquid of density **{rho} kg/m³**.\n\n{md_table(['point', 'depth below surface / m'], [['A', fmt(h1)], ['B', fmt(h2)]])}\n\nWhat is the difference in pressure between A and B? (g = 10 N/kg)",
              "Δp = Δh ρ g", [f"Δh = {fmt(h2)} − {fmt(h1)} = {fmt(h2 - h1)} m", f"Δp = {fmt(h2 - h1)} × {rho} × 10 = **{fmt(dp)} Pa**"],
              ["Pressure increases with depth.", "Only the difference in depth matters.", "Δp = Δh ρ g."])


@template("c5x_hydraulic_area_ratio", chapter=5, level=2, lo="5c")
def hydraulic_area_ratio(rng):
    F1 = nice(rng, 25, 40, 50, 60)
    r = nice(rng, 10, 20, 30, 50)
    F2 = F1 * r
    return mk(rng, F2, [(F1 / r, "The LARGE piston gives the larger force."), (F1, "The pressure is the same, not the force."), (F1 * r * r, "Force scales with area, which is r times larger.")],
              "N", f"In the hydraulic jack in Fig. 1, the large piston has **{r} times** the area of the small piston. A force of **{F1} N** is applied to the small piston. What force acts on the large piston?",
              "same pressure: F₂ = F₁ × A₂ ÷ A₁", [f"F₂ = {F1} × {r} = **{fmt(F2)} N**"],
              ["The pressure is the same at both pistons.", "F = p × A.", "Larger area → proportionally larger force."], figure=figs2.hydraulic_press(f"{F1} N", "A", f"{r}A", "F = ?"))


@template("c5x_hydraulic_find_area", chapter=5, level=2, lo="5c")
def hydraulic_find_area(rng):
    F1 = nice(rng, 50, 100, 200)
    A1 = nice(rng, 2, 4, 5)
    F2 = F1 * nice(rng, 15, 20, 40)
    A2 = F2 * A1 / F1
    return mk(rng, A2, [(F1 * A1 / F2, "The large force needs the LARGE area."), (A1, "The areas must differ to give different forces."), (F2 / A1, "Use A₂ = F₂ A₁ ÷ F₁.")],
              "cm²", f"A hydraulic press (Fig. 1) must give an output force of **{F2} N** when **{F1} N** is applied to a piston of area **{A1} cm²**. What area must the output piston have?",
              "F₁ ÷ A₁ = F₂ ÷ A₂ → A₂ = F₂ A₁ ÷ F₁", [f"A₂ = {F2} × {A1} ÷ {F1} = **{fmt(A2)} cm²**"],
              ["The pressures at the two pistons are equal.", "F₁/A₁ = F₂/A₂.", "Solve for A₂ (cm² is fine on both sides)."], figure=figs2.hydraulic_press(f"{F1} N", f"{A1} cm²", "A = ?", f"{F2} N"))


@template("c5x_manometer_pressure_diff", chapter=5, level=2, lo="5g")
def manometer_pressure_diff(rng):
    h_cm = nice(rng, 12, 15, 20, 25, 30)
    dp = h_cm / 100 * RHO_W * G
    return mk(rng, dp, [(h_cm * RHO_W * G, "Convert cm to m first."), (h_cm / 100 * RHO_W, "Include g."), (dp + 1e5, "The question asks for the difference from atmospheric pressure, not the total.")],
              "Pa", f"A water manometer is connected to a gas supply (Fig. 1). The difference in water levels is **{h_cm} cm**. By how much is the gas pressure greater than atmospheric pressure? (density of water 1000 kg/m³, g = 10 N/kg)",
              "excess pressure = h ρ g", [f"h = {fmt(h_cm / 100)} m", f"Δp = {fmt(h_cm / 100)} × 1000 × 10 = **{fmt(dp)} Pa**"],
              ["The level difference measures the pressure difference.", "Δp = h ρ g with h in m.", "Calculate."], figure=figs2.manometer(f"{h_cm} cm"))


@template("c5x_manometer_levels", chapter=5, level=2, lo="5g")
def manometer_levels(rng):
    left = nice(rng, 8.0, 10.0, 12.0)
    right = left + nice(rng, 14.0, 16.0, 18.0, 22.0)
    h = right - left
    return mk(rng, h, [(right, "Use the difference between the two levels."), (left + right, "Subtract the levels."), (h / 2, "The pressure difference is given by the FULL level difference.")],
              "cm of water", f"A water manometer is connected to a gas supply on its left arm; the right arm is open.\n\n{md_table(['arm', 'water level / cm'], [['left (gas side)', fmt(left)], ['right (open)', fmt(right)]])}\n\nBy how many cm of water is the gas pressure above atmospheric pressure?",
              "excess pressure = difference in levels", [f"h = {fmt(right)} − {fmt(left)} = **{fmt(h)} cm of water**"],
              ["The liquid is pushed down on the high-pressure side.", "The excess pressure equals the level difference.", "Subtract."])


# ================================================================== L3
@template("c5x_block_max_pressure", chapter=5, level=3, lo="5b")
def block_max_pressure(rng):
    a, b, c = rng.choice([(0.1, 0.2, 0.4), (0.05, 0.1, 0.2), (0.1, 0.1, 0.3), (0.2, 0.25, 0.5)])
    W = nice(rng, 80, 120, 160, 200)
    p_max = W / (a * b)
    p_min = W / (b * c)
    return mk(rng, p_max, [(p_min, "That is the SMALLEST pressure (on the largest face)."), (W / (a * c), "The maximum pressure is on the face with the smallest area."), (W * a * b, "p = F ÷ A.")],
              "Pa", f"A rectangular block of weight **{W} N** measures {fmt(a)} m × {fmt(b)} m × {fmt(c)} m.\n\n{md_table(['face', 'area / m²'], [['face 1', fmt(a * b)], ['face 2', fmt(a * c)], ['face 3', fmt(b * c)]])}\n\nWhat is the maximum pressure it can exert on the floor?",
              "maximum pressure on the smallest face: p = W ÷ A_min", [f"A_min = {fmt(a)} × {fmt(b)} = {fmt(a * b)} m²", f"p = {W} ÷ {fmt(a * b)} = **{fmt(p_max)} Pa**"],
              ["Which face gives the largest pressure?", "The one with the smallest area.", "p = W ÷ A."])


@template("c5x_syringe_cap", chapter=5, level=3, lo="5c")
def syringe_cap(rng):
    F = nice(rng, 60, 80, 100, 120)
    A_cm = nice(rng, 1.5, 2.0, 2.5, 4.0)
    p = F / (A_cm * 1e-4)
    return mk(rng, p, [(F / A_cm, "Convert cm² to m²: 1 cm² = 10⁻⁴ m²."), (F / (A_cm * 1e-2), "1 cm² = 10⁻⁴ m², not 10⁻² m²."), (F * A_cm * 1e-4, "p = F ÷ A.")],
              "Pa", f"Water fills a syringe whose nozzle is closed by a cap.\n\n{md_table(['quantity', 'value'], [['force on piston', f'{F} N'], ['area of piston', f'{fmt(A_cm)} cm²']])}\n\nWhat pressure (above atmospheric) does the water exert on the cap?",
              "pressure is transmitted through the water: p = F ÷ A_piston", [f"A = {fmt(A_cm)} × 10⁻⁴ m²", f"p = {F} ÷ {fmt(A_cm * 1e-4)} = **{fmt(p)} Pa**"],
              ["The water transmits the pressure from the piston to the cap.", "Convert cm² to m².", "p = F ÷ A."])


@template("c5x_tile_density", chapter=5, level=3, lo="5d")
def tile_density(rng):
    L = nice(rng, 0.5, 0.6, 0.61)
    t = nice(rng, 0.008, 0.0086, 0.01)
    m = nice(rng, 6.5, 7.0, 7.7)
    V = L * L * t
    rho = m / V
    return mk(rng, rho, [(m / (L * L), "Volume = length × width × thickness."), (V / m, "ρ = m ÷ V."), (m / (L * t), "Use all three dimensions.")],
              "kg/m³", f"A square floor tile is measured.\n\n{md_table(['quantity', 'value'], [['length', f'{fmt(L)} m'], ['width', f'{fmt(L)} m'], ['thickness', f'{fmt(t)} m'], ['mass', f'{fmt(m)} kg']])}\n\nWhat is the density of the tile?",
              "V = l × w × t; ρ = m ÷ V", [f"V = {fmt(L)} × {fmt(L)} × {fmt(t)} = {fmt(V)} m³", f"ρ = {fmt(m)} ÷ {fmt(V)} = **{fmt(rho)} kg/m³**"],
              ["Find the volume first.", "Multiply the three dimensions.", "Then ρ = m ÷ V."])


@template("c5x_sea_water_kpa", chapter=5, level=3, lo="5e")
def sea_water_kpa(rng):
    h = nice(rng, 15, 20, 25, 30, 40)
    p = h * 1030 * G / 1000
    return mk(rng, p, [(h * 1030 * G, "That is in Pa; the answer is in kPa."), (h * 1000 * G / 1000, "Use the density of SEA water, 1030 kg/m³."), (h * 1030 / 1000, "Include g.")],
              "kPa", f"A diver is at point X, **{h} m** below the surface of the sea (Fig. 1). The density of sea water is 1030 kg/m³ and g = 10 N/kg. What is the pressure at X due to the water, in kPa?",
              "p = h ρ g, then ÷ 1000 for kPa", [f"p = {h} × 1030 × 10 = {fmt(p * 1000)} Pa", f"= **{fmt(p)} kPa**"],
              ["p = h ρ g.", "Use the sea-water density.", "Convert Pa to kPa."], figure=figs2.liquid_column(f"{h} m", "sea water", "X"))


@template("c5x_water_barometer", chapter=5, level=3, lo="5f")
def water_barometer(rng):
    p = nice(rng, 0.95e5, 1.0e5, 1.02e5)
    rho = nice(rng, 1000, 800)
    h = p / (rho * G)
    liquid = "water" if rho == 1000 else "oil"
    return mk(rng, h, [(p / (RHO_HG * G), "That is the height of a MERCURY column; this barometer uses a lighter liquid."), (p / rho, "Include g: h = p ÷ (ρ g)."), (h * 10, "h = p ÷ (ρ g).")],
              "m", f"A barometer (Fig. 1) is made using {liquid} of density **{rho} kg/m³**. Atmospheric pressure is **{fmt(p)} Pa** and g = 10 N/kg. How tall is the {liquid} column?",
              "p = h ρ g → h = p ÷ (ρ g)", [f"h = {fmt(p)} ÷ ({rho} × 10) = **{fmt(h)} m**"],
              ["The column's pressure equals atmospheric pressure.", "Rearrange p = h ρ g.", "h = p ÷ (ρ g)."], figure=figs2.barometer("h = ?", liquid))


@template("c5x_mercury_to_pa", chapter=5, level=3, lo="5f")
def mercury_to_pa(rng):
    h_mm = nice(rng, 740, 750, 760, 770)
    p = h_mm / 1000 * RHO_HG * G
    return mk(rng, p, [(h_mm * RHO_HG * G, "Convert mm to m."), (h_mm / 100 * RHO_HG * G, "1 mm = 0.001 m, not 0.01 m."), (h_mm / 1000 * RHO_W * G, "Use the density of mercury, 13 600 kg/m³.")],
              "Pa", f"The mercury barometer in Fig. 1 has a column **{h_mm} mm** high. The density of mercury is 13 600 kg/m³ and g = 10 N/kg. What is the atmospheric pressure?",
              "p = h ρ g with h in m", [f"h = {fmt(h_mm / 1000)} m", f"p = {fmt(h_mm / 1000)} × 13 600 × 10 = **{fmt(p)} Pa**"],
              ["The mercury column is held up by the atmosphere.", "p = h ρ g.", "Convert mm to m first."], figure=figs2.barometer(f"{h_mm} mm"))


# ================================================================== L4
@template("c5x_aeroplane_window", chapter=5, level=4, lo="5b")
def aeroplane_window(rng):
    A = nice(rng, 0.12, 0.15, 0.16, 0.2)
    pin = nice(rng, 75, 80, 85)
    pout = nice(rng, 25, 30, 40, 50)
    F = (pin - pout) * 1000 * A
    return mk(rng, F, [(pin * 1000 * A, "Use the DIFFERENCE in pressure across the window."), ((pin + pout) * 1000 * A, "The pressures push in opposite directions: subtract."), ((pin - pout) * A, "Convert kPa to Pa.")],
              "N", f"An aeroplane window is at altitude.\n\n{md_table(['quantity', 'value'], [['area of window', f'{fmt(A)} m²'], ['pressure inside', f'{pin} kPa'], ['pressure outside', f'{pout} kPa']])}\n\nWhat is the resultant force on the window due to the air?",
              "F = (p_in − p_out) × A", [f"Δp = {pin} − {pout} = {pin - pout} kPa = {(pin - pout) * 1000} Pa", f"F = {(pin - pout) * 1000} × {fmt(A)} = **{fmt(F)} N** outwards"],
              ["The two pressures push in opposite directions.", "Find the pressure difference in Pa.", "F = Δp × A."])


@template("c5x_identify_metal", chapter=5, level=4, lo="5d")
def identify_metal(rng):
    metals = [("aluminium", 2.7), ("iron", 7.9), ("copper", 8.9), ("lead", 11.3)]
    name, rho = rng.choice(metals)
    V = nice(rng, 12, 15, 18, 20)
    v1 = nice(rng, 40, 50, 60)
    m = round(rho * V, 1)
    wrongs = {n: ("You may have used the final reading as the volume; subtract the readings first." if abs(r - m / (v1 + V)) < abs(r - rho) else "Calculate m ÷ (V₂ − V₁) and compare with the table.") for n, r in metals if n != name}
    table = md_table(["metal", "density / g/cm³"], [[n, r] for n, r in metals])
    return mkt(rng, name, wrongs, f"A metal ball of mass **{fmt(m)} g** is lowered into a measuring cylinder. The water level rises from **{v1} cm³** to **{v1 + V} cm³**.\n\n{table}\n\nWhich metal is the ball made of?",
               "V = V₂ − V₁; ρ = m ÷ V; match with the table", [f"V = {v1 + V} − {v1} = {V} cm³", f"ρ = {fmt(m)} ÷ {V} = {fmt(m / V)} g/cm³ → **{name}**"],
               ["Find the volume by displacement.", "Then the density.", "Compare with the table."])


@template("c5x_submarine_hatch", chapter=5, level=4, lo="5e")
def submarine_hatch(rng):
    h = nice(rng, 50, 80, 100, 120)
    A = nice(rng, 0.3, 0.4, 0.5)
    F = h * 1030 * G * A
    return mk(rng, F, [(h * 1030 * G, "That is the pressure; multiply by the area for the force."), (h * 1030 * A, "Include g."), (h * 1030 * G / A, "F = p × A.")],
              "N", f"A submarine has air at atmospheric pressure inside. Its hatch is at depth in the sea.\n\n{md_table(['quantity', 'value'], [['depth of hatch', f'{h} m'], ['area of hatch', f'{fmt(A)} m²'], ['density of sea water', '1030 kg/m³']])}\n\nWhat resultant force does the water exert on the hatch? (g = 10 N/kg; the atmospheric pressures inside and on the sea surface cancel.)",
              "p = h ρ g; F = p A", [f"p = {h} × 1030 × 10 = {fmt(h * 1030 * G)} Pa", f"F = {fmt(h * 1030 * G)} × {fmt(A)} = **{fmt(F)} N**"],
              ["Find the water pressure at that depth.", "p = h ρ g.", "Multiply by the area."])


@template("c5x_mercury_manometer_pa", chapter=5, level=4, lo="5g")
def mercury_manometer_pa(rng):
    h_cm = nice(rng, 8, 10, 12, 15)
    patm = nice(rng, 1.00e5, 1.01e5)
    p = patm + h_cm / 100 * RHO_HG * G
    return mk(rng, p, [(h_cm / 100 * RHO_HG * G, "That is only the EXCESS; add atmospheric pressure."), (patm - h_cm / 100 * RHO_HG * G, "The liquid is lower on the gas side, so the gas pressure is ABOVE atmospheric."), (patm + h_cm * RHO_HG * G, "Convert cm to m.")],
              "Pa", f"A mercury manometer is connected to a gas cylinder (Fig. 1). The level difference is **{h_cm} cm**. Atmospheric pressure is **{fmt(patm)} Pa**, the density of mercury is 13 600 kg/m³ and g = 10 N/kg. What is the pressure of the gas?",
              "p_gas = p_atm + h ρ g", [f"h ρ g = {fmt(h_cm / 100)} × 13 600 × 10 = {fmt(h_cm / 100 * RHO_HG * G)} Pa", f"p = {fmt(patm)} + {fmt(h_cm / 100 * RHO_HG * G)} = **{fmt(p)} Pa**"],
              ["Is the gas pressure above or below atmospheric?", "The mercury is pushed down on the gas side.", "Add h ρ g to atmospheric pressure."], figure=figs2.manometer(f"{h_cm} cm", "gas cylinder"))


@template("c5x_car_lift", chapter=5, level=4, lo="5c")
def car_lift(rng):
    m = nice(rng, 1000, 1200, 1500)
    A1 = nice(rng, 0.002, 0.004, 0.005)
    A2 = nice(rng, 0.2, 0.25, 0.4)
    F1 = m * G * A1 / A2
    return mk(rng, F1, [(m * A1 / A2, "Use the car's WEIGHT (m g), not its mass."), (m * G * A2 / A1, "The small piston needs the SMALL force."), (m * G, "The hydraulic system multiplies the force.")],
              "N", f"A hydraulic lift (Fig. 1) raises a car of mass **{m} kg** on a piston of area **{fmt(A2)} m²**. The small piston has area **{fmt(A1)} m²**. What force on the small piston supports the car? (g = 10 N/kg)",
              "W = m g; F₁ = W × A₁ ÷ A₂", [f"W = {m} × 10 = {m * G} N", f"F₁ = {m * G} × {fmt(A1)} ÷ {fmt(A2)} = **{fmt(F1)} N**"],
              ["Find the car's weight.", "The pressure is the same at both pistons.", "F₁ = W A₁ ÷ A₂."], figure=figs2.hydraulic_press("F = ?", f"{fmt(A1)} m²", f"{fmt(A2)} m²", f"{m * G} N"))


@template("c5x_brake_pads", chapter=5, level=4, lo="5c")
def brake_pads(rng):
    F1 = nice(rng, 100, 150, 200)
    A1 = nice(rng, 2.0, 2.5, 4.0)
    A2 = nice(rng, 8.0, 10.0, 12.0)
    n = 2
    F2 = F1 * A2 / A1
    return mk(rng, F2, [(F1 * A1 / A2, "The brake piston is LARGER, so it gives a larger force."), (F2 * n, "Each piston has area A₂; find the force on ONE piston."), (F1, "The pressure is the same, not the force.")],
              "N", f"In a car's hydraulic brakes, the pedal pushes a master piston; the pressure is transmitted to two brake pistons.\n\n{md_table(['quantity', 'value'], [['force on master piston', f'{F1} N'], ['area of master piston', f'{fmt(A1)} cm²'], ['area of EACH brake piston', f'{fmt(A2)} cm²']])}\n\nWhat force acts on each brake piston?",
              "same pressure: F₂ = F₁ × A₂ ÷ A₁", [f"p = {F1} ÷ {fmt(A1)} = {fmt(F1 / A1)} N/cm²", f"F₂ = {fmt(F1 / A1)} × {fmt(A2)} = **{fmt(F2)} N**"],
              ["Find the pressure in the brake fluid.", "It is the same at every piston.", "F = p × A for one brake piston."])


# ================================================================== L5
@template("c5x_jack_lever", chapter=5, level=5, lo="5c")
def jack_lever(rng):
    E = nice(rng, 100, 150, 200)
    k = nice(rng, 5, 6, 8)
    A1 = nice(rng, 2.0, 4.0, 5.0)
    A2 = nice(rng, 100, 160, 200)
    F2 = E * k * A2 / A1
    return mk(rng, F2, [(E * A2 / A1, "The lever first multiplies the effort; include it."), (E * k, "That is only the force on the small piston; the hydraulics multiply it again."), (E * k * A1 / A2, "The large piston gives the larger force.")],
              "N", f"A car jack has a lever that pushes the small piston of a hydraulic system.\n\n{md_table(['quantity', 'value'], [['effort on lever', f'{E} N'], ['force on small piston ÷ effort (from moments)', k], ['area of small piston', f'{fmt(A1)} cm²'], ['area of large piston', f'{A2} cm²']])}\n\nWhat force does the large piston exert?",
              "F₁ = k E; F₂ = F₁ × A₂ ÷ A₁", [f"F₁ = {k} × {E} = {k * E} N", f"F₂ = {k * E} × {A2} ÷ {fmt(A1)} = **{fmt(F2)} N**"],
              ["First find the force on the small piston.", "Then use equal pressures.", "F₂ = F₁ A₂ ÷ A₁."])


@template("c5x_oil_water_utube", chapter=5, level=5, lo="5d")
def oil_water_utube(rng):
    ho = nice(rng, 10.0, 12.0, 12.5, 15.0, 20.0)
    rho_o = nice(rng, 800, 850, 900)
    hw = ho * rho_o / 1000
    return mk(rng, rho_o, [(1000 * ho / hw * ho / hw, "At the level of the interface the pressures are equal: ρ_o h_o = ρ_w h_w."), (1000 * ho / hw, "The oil column is TALLER, so oil is LESS dense: ρ_o = ρ_w h_w ÷ h_o."), (1000 - rho_o + 1000, "Use ρ_o h_o = ρ_w h_w.")],
              "kg/m³", f"Oil is poured into one arm of a U-tube containing water. Measured from the oil–water boundary:\n\n{md_table(['column', 'height above the level of the boundary / cm'], [['oil', fmt(ho)], ['water (other arm)', fmt(hw)]])}\n\nThe density of water is 1000 kg/m³. What is the density of the oil?",
              "pressures equal at the boundary level: ρ_o h_o g = ρ_w h_w g", [f"ρ_o = 1000 × {fmt(hw)} ÷ {fmt(ho)}", f"= **{fmt(rho_o)} kg/m³**"],
              ["At the level of the boundary, the pressure is the same in both arms.", "h ρ g is equal on both sides.", "ρ_o = ρ_w h_w ÷ h_o."])


@template("c5x_diver_limit", chapter=5, level=5, lo="5e")
def diver_limit(rng):
    pmax = nice(rng, 400, 450, 500, 600)
    patm = 100
    h = (pmax - patm) * 1000 / (1030 * G)
    return mk(rng, h, [(pmax * 1000 / (1030 * G), "Subtract atmospheric pressure: the water supplies only the extra pressure."), ((pmax + patm) * 1000 / (1030 * G), "Subtract atmospheric pressure, do not add it."), ((pmax - patm) * 1000 / (1000 * G), "Use the density of sea water, 1030 kg/m³.")],
              "m", f"A diver's equipment is safe up to a total pressure of **{pmax} kPa**.\n\n{md_table(['quantity', 'value'], [['atmospheric pressure', f'{patm} kPa'], ['density of sea water', '1030 kg/m³'], ['g', '10 N/kg']])}\n\nWhat is the greatest safe depth?",
              "p_total = p_atm + h ρ g → h = (p_total − p_atm) ÷ (ρ g)", [f"h ρ g = {pmax} − {patm} = {pmax - patm} kPa", f"h = {(pmax - patm) * 1000} ÷ (1030 × 10) = **{fmt(h)} m**"],
              ["Total pressure = atmospheric + water.", "Find the water's share.", "h = p ÷ (ρ g)."])


@template("c5x_mixer_board", chapter=5, level=5, lo="5b")
def mixer_board(rng):
    W = nice(rng, 4000, 5000, 6000)
    a = nice(rng, 0.01, 0.02, 0.025)
    B = nice(rng, 2.0, 3.0, 4.0)
    factor = B / (4 * a)
    return mk(rng, factor, [(B / a, "The mixer has FOUR wheels: the contact area is 4a."), (4 * a / B, "The board has the LARGER area, so the pressure falls by B ÷ 4a."), (W / B, "That is the pressure on the board's ground, not the factor.")],
              "times", f"A cement mixer stands on soft ground on four wheels, then on a large flat board.\n\n{md_table(['quantity', 'value'], [['weight of mixer', f'{W} N'], ['contact area of EACH wheel', f'{fmt(a)} m²'], ['area of board', f'{fmt(B)} m²']])}\n\nBy what factor does the board reduce the pressure on the ground? (Ignore the board's weight.)",
              "p = W ÷ A; factor = A_board ÷ A_wheels", [f"wheels: A = 4 × {fmt(a)} = {fmt(4 * a)} m², p = {fmt(W / (4 * a))} Pa", f"board: p = {fmt(W / B)} Pa", f"factor = {fmt(W / (4 * a))} ÷ {fmt(W / B)} = **{fmt(factor)}**"],
              ["Same force, different areas.", "Remember there are four wheels.", "Factor = ratio of the areas."])


@template("c5x_salt_block", chapter=5, level=5, lo="5b")
def salt_block(rng):
    a, c = nice(rng, 9.0, 10.0), nice(rng, 25.0, 27.0, 30.0)
    rho = nice(rng, 2.0, 2.2)
    m = rho * a * a * c / 1000
    W = m * G
    p = W / (a * a * 1e-4)
    return mk(rng, p, [(W / (a * c * 1e-4), "The greatest pressure is on the SMALLEST face, a × a."), (W / (a * a), "Convert cm² to m²."), (m / (a * a * 1e-4), "Use the weight in N (m g), not the mass.")],
              "Pa", f"A block of salt has a square end.\n\n{md_table(['quantity', 'value'], [['dimensions', f'{fmt(a)} cm × {fmt(a)} cm × {fmt(c)} cm'], ['density of salt', f'{fmt(rho)} g/cm³'], ['g', '10 N/kg']])}\n\nWhat is the greatest pressure the block can exert on a table?",
              "m = ρ V; W = m g; p = W ÷ A_smallest", [f"V = {fmt(a * a * c)} cm³, m = {fmt(rho)} × {fmt(a * a * c)} = {fmt(m * 1000)} g = {fmt(m)} kg", f"W = {fmt(W)} N; A = {fmt(a * a)} cm² = {fmt(a * a * 1e-4)} m²", f"p = **{fmt(p)} Pa**"],
              ["Find the mass, then the weight.", "The greatest pressure is on the smallest face.", "Convert the area to m²."])


@template("c5x_manometer_liquid_change", chapter=5, level=5, lo="5g")
def manometer_liquid_change(rng):
    hw = nice(rng, 16, 20, 24, 32)
    rho = nice(rng, 800, 1250, 13600)
    h = hw * 1000 / rho
    name = {800: "oil", 1250: "glycerine", 13600: "mercury"}[rho]
    return mk(rng, h, [(hw * rho / 1000, "A DENSER liquid needs a SHORTER column for the same pressure."), (hw, "The level difference depends on the density of the liquid."), (hw * 1000 / rho / 10, "h₂ = h₁ ρ₁ ÷ ρ₂ (keep cm).")],
              "cm", f"A gas supply gives a level difference of **{hw} cm** on a water manometer (Fig. 1). The water is replaced by {name} of density **{rho} kg/m³**. What is the new level difference for the same gas pressure?",
              "same pressure: h₁ ρ₁ = h₂ ρ₂", [f"h₂ = {hw} × 1000 ÷ {rho}", f"= **{fmt(h)} cm**"],
              ["The gas pressure has not changed.", "h ρ g is the same for both liquids.", "Solve for the new h."], figure=figs2.manometer(f"{hw} cm (water)"))


@template("c5x_manometer_below_atm", chapter=5, level=5, lo="5g")
def manometer_below_atm(rng):
    h_cm = nice(rng, 20, 25, 30, 40)
    patm = 1.0e5
    p = patm - h_cm / 100 * RHO_W * G
    return mk(rng, p, [(patm + h_cm / 100 * RHO_W * G, "The water is HIGHER on the gas side, so the gas pressure is BELOW atmospheric."), (h_cm / 100 * RHO_W * G, "That is the difference; subtract it from atmospheric pressure."), (patm - h_cm * RHO_W * G / 1000, "Convert cm to m: h = h_cm ÷ 100.")],
              "Pa", f"A water manometer is connected to a container from which some air has been pumped out (Fig. 1). The water is **{h_cm} cm** higher on the container side. Atmospheric pressure is 1.0 × 10⁵ Pa and g = 10 N/kg. What is the pressure in the container?",
              "liquid higher on the gas side → p = p_atm − h ρ g", [f"h ρ g = {fmt(h_cm / 100)} × 1000 × 10 = {fmt(h_cm / 100 * RHO_W * G)} Pa", f"p = 1.0 × 10⁵ − {fmt(h_cm / 100 * RHO_W * G)} = **{fmt(p)} Pa**"],
              ["Which side has the higher pressure?", "The liquid is pushed UP towards the lower pressure.", "Subtract h ρ g."], figure=figs2.manometer(f"{h_cm} cm", "container", left_higher=True))
