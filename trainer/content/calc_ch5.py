"""Chapter 5 Pressure (6091): liquid pressure p = h rho g, hydraulic press, manometer and barometer.
(Density and pressure = force / area templates for this chapter live in calc_ch3.py, carried over from the G3 bank.)"""
from .. import figs2
from .base import fmt, nice, numeric_options, template

G = 10


# ---------------------------------------------------------------- L2
@template("c5_liquid_pressure_direct", chapter=5, level=2, lo="5e")
def liquid_pressure_direct(rng):
    h = nice(rng, 0.5, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0)
    rho = 1000
    p = h * rho * G
    opts, key, mis = numeric_options(rng, p, [
        (h * rho, "You left out g. Pressure due to a liquid column = h × ρ × g."),
        (h * G, "You left out the density of water (1000 kg/m³)."),
        (p / 1000, "That would be the answer in kPa, but the options are in Pa. 1 kPa = 1000 Pa."),
    ], unit="Pa")
    return dict(
        stem=f"Fig. 1 shows a tank of water. Point X is **{fmt(h)} m** below the surface. The density of water is 1000 kg/m³ and g = 10 N/kg. What is the pressure at X due to the water alone?",
        figure=figs2.liquid_column(f"h = {fmt(h)} m", point_label="X"),
        options=opts, key=key, misconceptions=mis,
        formula="pressure due to a liquid column = h ρ g",
        working=["p = h ρ g", f"= {fmt(h)} × 1000 × 10", f"= **{fmt(p)} Pa**"],
        hints=[
            "Which three quantities does the pressure due to a liquid depend on? (Not the area or the shape of the tank.)",
            "p = depth × density × g. All three values are given in SI units already.",
            f"p = {fmt(h)} × 1000 × 10.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c5_liquid_pressure_unit_change", chapter=5, level=3, lo="5e")
def liquid_pressure_unit_change(rng):
    h_cm = nice(rng, 20, 25, 30, 40, 50, 60, 80)
    rho_g = nice(rng, 0.8, 0.9, 1.0, 1.2, 13.6)
    liquid = {0.8: "paraffin", 0.9: "oil", 1.0: "water", 1.2: "brine", 13.6: "mercury"}[rho_g]
    p = h_cm / 100 * rho_g * 1000 * G
    opts, key, mis = numeric_options(rng, p, [
        (h_cm * rho_g * G, "You used h in cm and ρ in g/cm³ without converting. Pressure in Pa needs h in m and ρ in kg/m³."),
        (h_cm / 100 * rho_g * G, "You converted h to metres but left ρ in g/cm³. 1 g/cm³ = 1000 kg/m³."),
        (h_cm * rho_g * 1000 * G, "You converted ρ but left h in cm. Divide the depth by 100 first."),
    ], unit="Pa", sf=3)
    return dict(
        stem=f"Fig. 1 shows a container of {liquid} of density **{fmt(rho_g)} g/cm³**. Point X is **{h_cm} cm** below the surface. Taking g = 10 N/kg, what is the pressure at X due to the liquid?",
        figure=figs2.liquid_column(f"h = {h_cm} cm", liquid_label=liquid, point_label="X"),
        options=opts, key=key, misconceptions=mis,
        formula="p = h ρ g with h in m and ρ in kg/m³ (1 g/cm³ = 1000 kg/m³)",
        working=[f"h = {h_cm} cm = {fmt(h_cm / 100)} m;  ρ = {fmt(rho_g)} g/cm³ = {fmt(rho_g * 1000)} kg/m³",
                 f"p = h ρ g = {fmt(h_cm / 100)} × {fmt(rho_g * 1000)} × 10", f"= **{fmt(p, sf=3)} Pa**"],
        hints=[
            "p = h ρ g gives pascals only when every quantity is in SI units. Which two given values are not?",
            f"Change {h_cm} cm to metres (÷ 100) and {fmt(rho_g)} g/cm³ to kg/m³ (× 1000).",
            f"p = {fmt(h_cm / 100)} × {fmt(rho_g * 1000)} × 10.",
        ],
    )


@template("c5_hydraulic_press_force", chapter=5, level=3, lo="5c")
def hydraulic_press_force(rng):
    F1 = nice(rng, 20, 40, 50, 60, 80, 100)
    A1 = nice(rng, 2, 4, 5, 8, 10)
    ratio = nice(rng, 5, 8, 10, 20, 25)
    A2 = A1 * ratio
    F2 = F1 * ratio
    opts, key, mis = numeric_options(rng, F2, [
        (F1 / ratio, "You divided instead of multiplying. The large piston has the larger area, so it exerts the LARGER force."),
        (F1, "The force is not the same on both pistons: it is the PRESSURE that is the same throughout the liquid."),
        (F1 * A2, "You multiplied the force by the area. Find the pressure first (F ÷ A), then multiply by the other area."),
    ], unit="N")
    return dict(
        stem=f"Fig. 1 shows a hydraulic press. A force of **{F1} N** is applied to the small piston of area **{A1} cm²**. The large piston has an area of **{A2} cm²**. What force is exerted by the large piston?",
        figure=figs2.hydraulic_press(f"F = {F1} N", f"A = {A1} cm²", f"A = {A2} cm²", "F = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="pressure is transmitted equally through the liquid: F₁ / A₁ = F₂ / A₂",
        working=[f"pressure = F₁ / A₁ = {F1} / {A1} = {fmt(F1 / A1)} N/cm²", f"F₂ = pressure × A₂ = {fmt(F1 / A1)} × {A2}", f"= **{F2} N**"],
        hints=[
            "In a hydraulic system the liquid transmits the PRESSURE unchanged to the other piston. What is the pressure under the small piston?",
            f"pressure = {F1} ÷ {A1} N/cm². (The same unit works on both sides, so no conversion to m² is needed.)",
            f"F₂ = {fmt(F1 / A1)} × {A2}.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c5_total_pressure_depth", chapter=5, level=4, lo="5e")
def total_pressure_depth(rng):
    h = nice(rng, 2.0, 5.0, 8.0, 10.0, 12.0, 15.0, 20.0)
    patm = nice(rng, 100, 101, 102)
    p_water = h * 1000 * G / 1000       # kPa
    total = patm + p_water
    opts, key, mis = numeric_options(rng, total, [
        (p_water, "That is the pressure due to the water alone. The question asks for the TOTAL pressure, which includes the atmosphere pressing on the surface."),
        (patm, "That is atmospheric pressure alone. At depth the water adds h ρ g on top of it."),
        (patm + h * 1000 * G, "You added pascals to kilopascals. Convert h ρ g to kPa (÷ 1000) before adding."),
    ], unit="kPa", sf=3)
    return dict(
        stem=f"A diver is **{fmt(h)} m** below the surface of a lake, as shown in Fig. 1. Atmospheric pressure is **{patm} kPa**, the density of water is 1000 kg/m³ and g = 10 N/kg. What is the total pressure on the diver?",
        figure=figs2.liquid_column(f"h = {fmt(h)} m", liquid_label="water", point_label="diver", extra=f"atmospheric pressure = {patm} kPa"),
        options=opts, key=key, misconceptions=mis,
        formula="total pressure = atmospheric pressure + h ρ g",
        working=[f"pressure due to water = h ρ g = {fmt(h)} × 1000 × 10 = {fmt(h * 1000 * G)} Pa = {fmt(p_water)} kPa",
                 f"total = {patm} + {fmt(p_water)}", f"= **{fmt(total, sf=3)} kPa**"],
        hints=[
            "Two things press on the diver: the water above and the air above the water. Which formula gives the water's share?",
            f"h ρ g = {fmt(h)} × 1000 × 10 Pa. Change that to kPa so it can be added to {patm} kPa.",
            f"total = {patm} kPa + {fmt(p_water)} kPa.",
        ],
    )


@template("c5_manometer_gas_pressure", chapter=5, level=4, lo="5g")
def manometer_gas_pressure(rng):
    h_cm = nice(rng, 5, 8, 10, 12, 15, 20, 25)
    patm = nice(rng, 100, 101)
    extra = h_cm / 100 * 1000 * G       # Pa
    total = patm * 1000 + extra
    opts, key, mis = numeric_options(rng, total, [
        (patm * 1000 - extra, "The liquid is pushed DOWN on the gas side, so the gas pressure is greater than atmospheric: add h ρ g, do not subtract."),
        (extra, "That is only the pressure difference shown by the manometer. Add atmospheric pressure to get the gas pressure."),
        (patm * 1000 + h_cm * 1000 * G, "You left h in centimetres. Convert to metres first."),
    ], unit="Pa", sf=4)
    return dict(
        stem=f"Fig. 1 shows a water manometer connected to a gas supply. The difference in water levels is **{h_cm} cm**. Atmospheric pressure is **{patm} kPa**, the density of water is 1000 kg/m³ and g = 10 N/kg. What is the pressure of the gas supply?",
        figure=figs2.manometer(f"{h_cm} cm", gas_label="gas supply"),
        options=opts, key=key, misconceptions=mis,
        formula="gas pressure = atmospheric pressure + h ρ g (liquid lower on the gas side means the gas pressure is higher)",
        working=[f"h ρ g = {fmt(h_cm / 100)} × 1000 × 10 = {fmt(extra)} Pa", f"gas pressure = {patm * 1000} + {fmt(extra)}", f"= **{fmt(total, sf=4)} Pa**"],
        hints=[
            "Which side has the lower liquid level? That side is being pushed harder, so its pressure is higher.",
            f"The level difference of {h_cm} cm of water represents a pressure difference of h ρ g (with h in metres).",
            f"gas pressure = {patm} kPa + ({fmt(h_cm / 100)} × 1000 × 10) Pa.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c5_hydraulic_distance", chapter=5, level=5, lo="5c")
def hydraulic_distance(rng):
    A1 = nice(rng, 2, 4, 5, 10)
    ratio = nice(rng, 5, 10, 20, 25)
    A2 = A1 * ratio
    d1 = nice(rng, 10, 20, 25, 40, 50)
    d2 = d1 / ratio
    opts, key, mis = numeric_options(rng, d2, [
        (d1 * ratio, "The large piston moves LESS, not more: the same volume of liquid spreads over a larger area."),
        (d1, "The pistons do not move the same distance. The volume of liquid pushed out of one cylinder equals the volume pushed into the other."),
        (d1 / ratio * 2, "Check the ratio of the areas: volume moved = area × distance on each side."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"In the hydraulic press in Fig. 1 the small piston (area **{A1} cm²**) is pushed down **{d1} cm**. The large piston has an area of **{A2} cm²**. The liquid cannot be compressed. How far does the large piston move up?",
        figure=figs2.hydraulic_press("push", f"A = {A1} cm²", f"A = {A2} cm²", "moves up"),
        options=opts, key=key, misconceptions=mis,
        formula="volume of liquid moved is the same on both sides: A₁ d₁ = A₂ d₂",
        working=[f"volume moved = A₁ d₁ = {A1} × {d1} = {A1 * d1} cm³", f"d₂ = volume ÷ A₂ = {A1 * d1} ÷ {A2}", f"= **{fmt(d2, sf=3)} cm**"],
        hints=[
            "The liquid is incompressible, so the volume that leaves the small cylinder must appear in the large one. How is volume related to area and distance?",
            f"volume = {A1} × {d1} cm³ leaves the small cylinder. The same volume lifts the large piston of area {A2} cm².",
            f"d₂ = ({A1} × {d1}) ÷ {A2}.",
        ],
    )


@template("c5_depth_from_pressure", chapter=5, level=5, lo="5e")
def depth_from_pressure(rng):
    dp = nice(rng, 20, 30, 45, 60, 75, 90, 120)      # kPa difference
    rho = nice(rng, 1000, 1030)
    liquid = "sea water" if rho == 1030 else "fresh water"
    h = dp * 1000 / (rho * G)
    opts, key, mis = numeric_options(rng, h, [
        (dp / (rho * G), "You used kPa as if it were Pa. 1 kPa = 1000 Pa."),
        (dp * 1000 / rho, "You forgot to divide by g. Rearranging p = h ρ g gives h = p ÷ (ρ g)."),
        (dp * 1000 * rho * G, "You multiplied instead of dividing. Rearrange p = h ρ g to make h the subject."),
    ], unit="m", sf=3)
    return dict(
        stem=f"A pressure sensor on a submarine in {liquid} (density **{rho} kg/m³**) reads **{dp} kPa more** than it did at the surface, as shown in Fig. 1. Taking g = 10 N/kg, how deep is the submarine?",
        figure=figs2.liquid_column("h = ?", liquid_label=liquid, point_label="submarine", extra=f"pressure increase = {dp} kPa"),
        options=opts, key=key, misconceptions=mis,
        formula="p = h ρ g  →  h = p ÷ (ρ g), with p in Pa",
        working=[f"p = {dp} kPa = {dp * 1000} Pa", f"h = p ÷ (ρ g) = {dp * 1000} ÷ ({rho} × 10)", f"= **{fmt(h, sf=3)} m**"],
        hints=[
            "The extra pressure comes only from the water above. Which formula links that pressure to the depth?",
            f"Rearrange p = h ρ g for h, and change {dp} kPa into pascals first.",
            f"h = {dp * 1000} ÷ ({rho} × 10).",
        ],
    )
