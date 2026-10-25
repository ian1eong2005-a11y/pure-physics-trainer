"""Chapter 9 Thermal Properties of Matter (6091): Q = m c Δθ, Q = m L, heater power and time, heating curves, mixtures, efficiency."""
from .. import figs2, sketches
from .base import fmt, md_table, nice, numeric_options, template

C_WATER = 4200
L_ICE = 334000
L_STEAM = 2260000


# ---------------------------------------------------------------- L1
@template("c9_energy_to_heat_water", chapter=9, level=1, lo="9c")
def energy_to_heat_water(rng):
    m = nice(rng, 0.5, 1.0, 1.5, 2.0, 2.5)
    dt = nice(rng, 10, 15, 20, 25, 30, 40, 50)
    Q = m * C_WATER * dt
    opts, key, mis = numeric_options(rng, Q, [
        (C_WATER * dt, "You left out the mass. Energy = mass × specific heat capacity × temperature change."),
        (m * dt, "You left out the specific heat capacity (4200 J/(kg K))."),
        (m * C_WATER, "You left out the temperature change."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows **{fmt(m)} kg** of water being heated. Its temperature rises by **{dt} °C**. The specific heat capacity of water is 4200 J/(kg K). How much energy is transferred to the water?",
        figure=figs2.beaker_heater([f"mass = {fmt(m)} kg", f"temperature rise = {dt} °C", "c = 4200 J/(kg K)"]),
        options=opts, key=key, misconceptions=mis,
        formula="energy transferred = m c Δθ",
        working=["Q = m c Δθ", f"= {fmt(m)} × 4200 × {dt}", f"= **{fmt(Q)} J**"],
        hints=[
            "Which formula links energy, mass, specific heat capacity and temperature change?",
            "Q = m c Δθ. All three values are given in the right units.",
            f"{fmt(m)} × 4200 × {dt} = ?",
        ],
    )


@template("c9_energy_to_melt", chapter=9, level=1, lo="9g")
def energy_to_melt(rng):
    m = nice(rng, 0.2, 0.25, 0.5, 0.8, 1.0, 1.5, 2.0)
    Q = m * L_ICE
    opts, key, mis = numeric_options(rng, Q, [
        (L_ICE, "That is the energy to melt 1 kg. Multiply by the mass."),
        (m * C_WATER, "You used the specific heat capacity. Melting at 0 °C involves LATENT heat: Q = m L."),
        (m * L_STEAM, "You used the latent heat of vaporisation (boiling). Melting uses the latent heat of fusion."),
    ], unit="J", sf=3)
    table = md_table(["quantity", "value"], [["mass of ice", f"{fmt(m)} kg"], ["temperature of ice", "0 °C"], ["specific latent heat of fusion of ice", "334 000 J/kg"]])
    return dict(
        stem=f"A block of ice at 0 °C melts completely to water at 0 °C.\n\n{table}\n\nHow much energy is absorbed by the ice as it melts?",
        options=opts, key=key, misconceptions=mis,
        formula="energy for a change of state = m L (no temperature change)",
        working=["Q = m L", f"= {fmt(m)} × 334 000", f"= **{fmt(Q, sf=3)} J**"],
        hints=[
            "The temperature does not change, so this is a latent-heat question, not a specific-heat-capacity question.",
            "Q = m × specific latent heat of fusion.",
            f"{fmt(m)} × 334 000 = ?",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c9_shc_from_data", chapter=9, level=2, lo="9c")
def shc_from_data(rng):
    c = nice(rng, 380, 450, 500, 900, 2400)
    m = nice(rng, 0.5, 1.0, 2.0)
    dt = nice(rng, 10, 15, 20, 25, 40)
    Q = m * c * dt
    opts, key, mis = numeric_options(rng, c, [
        (Q / dt, "You forgot to divide by the mass as well: c = Q ÷ (m Δθ)."),
        (Q / m, "You forgot to divide by the temperature change as well: c = Q ÷ (m Δθ)."),
        (Q * m * dt, "You multiplied. Rearrange Q = m c Δθ to make c the subject."),
    ], unit="J/(kg K)")
    return dict(
        stem=f"Fig. 1 shows a heater in a metal block of mass **{fmt(m)} kg**. The heater supplies **{fmt(Q)} J** and the temperature of the block rises by **{dt} °C**. No energy is lost. What is the specific heat capacity of the metal?",
        figure=figs2.heater_block([f"mass = {fmt(m)} kg", f"energy supplied = {fmt(Q)} J", f"temperature rise = {dt} °C"]),
        options=opts, key=key, misconceptions=mis,
        formula="Q = m c Δθ  →  c = Q ÷ (m Δθ)",
        working=["c = Q ÷ (m Δθ)", f"= {fmt(Q)} ÷ ({fmt(m)} × {dt})", f"= **{c} J/(kg K)**"],
        hints=[
            "Start from Q = m c Δθ and make c the subject.",
            f"c = Q ÷ (m × Δθ) = {fmt(Q)} ÷ ({fmt(m)} × {dt}).",
            f"{fmt(m)} × {dt} = {fmt(m * dt)}; now divide {fmt(Q)} by that.",
        ],
    )


@template("c9_mass_boiled_away", chapter=9, level=2, lo="9g")
def mass_boiled_away(rng):
    P = nice(rng, 1130, 1500, 2000, 2260, 3000)
    t_min = nice(rng, 2, 3, 4, 5)
    Q = P * t_min * 60
    m = Q / L_STEAM
    opts, key, mis = numeric_options(rng, m, [
        (P * t_min / L_STEAM, "You used the time in minutes. Energy = power × time needs the time in SECONDS."),
        (Q / L_ICE, "You used the latent heat of fusion (melting). Boiling uses the latent heat of vaporisation, 2 260 000 J/kg."),
        (Q / C_WATER, "You used the specific heat capacity. The water is already at 100 °C, so the energy goes into changing state: Q = m L."),
    ], unit="kg", sf=3)
    return dict(
        stem=f"Fig. 1 shows a **{P} W** heater in boiling water at 100 °C. It is left on for **{t_min} minutes**. The specific latent heat of vaporisation of water is 2 260 000 J/kg. What mass of water is turned into steam?",
        figure=figs2.beaker_heater([f"power = {P} W", f"time = {t_min} min", "water at 100 °C"], liquid="boiling water"),
        options=opts, key=key, misconceptions=mis,
        formula="energy = P t (t in seconds); m = energy ÷ L",
        working=[f"energy = P t = {P} × {t_min * 60} = {fmt(Q)} J", f"m = Q ÷ L = {fmt(Q)} ÷ 2 260 000", f"= **{fmt(m, sf=3)} kg**"],
        hints=[
            "Two steps: how much energy does the heater supply, and how much water does that energy boil away?",
            f"energy = power × time = {P} × ({t_min} × 60) J.",
            f"m = {fmt(Q)} ÷ 2 260 000.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c9_heater_time", chapter=9, level=3, lo="9c")
def heater_time(rng):
    P = nice(rng, 500, 800, 1000, 1500, 2000)
    m = nice(rng, 0.5, 1.0, 1.5, 2.0)
    dt = nice(rng, 20, 30, 40, 50, 60, 80)
    Q = m * C_WATER * dt
    t = Q / P
    opts, key, mis = numeric_options(rng, t, [
        (Q / P / 60, "That is the time in minutes. The options are in seconds."),
        (P / (m * dt), "You divided the wrong things. Find the energy needed first (m c Δθ), then time = energy ÷ power."),
        (Q * P, "You multiplied energy by power. Power = energy ÷ time, so time = energy ÷ power."),
    ], unit="s", sf=3)
    return dict(
        stem=f"Fig. 1 shows a **{P} W** heater in **{fmt(m)} kg** of water. How long does it take to raise the temperature of the water by **{dt} °C**? Assume no energy is lost. (c of water = 4200 J/(kg K))",
        figure=figs2.beaker_heater([f"power = {P} W", f"mass = {fmt(m)} kg", f"temperature rise = {dt} °C"]),
        options=opts, key=key, misconceptions=mis,
        formula="energy needed = m c Δθ; time = energy ÷ power",
        working=[f"Q = m c Δθ = {fmt(m)} × 4200 × {dt} = {fmt(Q)} J", f"t = Q ÷ P = {fmt(Q)} ÷ {P}", f"= **{fmt(t, sf=3)} s**"],
        hints=[
            "First work out how much energy the water needs. Then ask how long the heater takes to supply it.",
            f"Q = {fmt(m)} × 4200 × {dt} J. Power tells you joules per second.",
            f"t = {fmt(Q)} ÷ {P}.",
        ],
    )


@template("c9_heating_curve_melting_time", chapter=9, level=3, lo="9d")
def heating_curve_melting_time(rng):
    mp = nice(rng, 40, 50, 60, 80)
    t_start = nice(rng, 2, 3, 4)
    dur = nice(rng, 3, 4, 5, 6)
    pts = [(0, 20), (t_start, mp), (t_start + dur, mp), (t_start + dur + 3, mp + 30)]
    opts, key, mis = numeric_options(rng, dur, [
        (t_start + dur, "That is the time when melting FINISHES. Melting lasts from the start of the flat section to its end."),
        (t_start, "That is when melting STARTS. The question asks how long it lasts."),
        (mp, "That is the melting point in °C, not a time."),
    ], unit="min")
    return dict(
        stem="Fig. 1 shows the heating curve of a solid that is heated at a steady rate. For how long is the substance melting?",
        figure=sketches.heating_curve(pts),
        options=opts, key=key, misconceptions=mis,
        formula="during melting the temperature stays constant: the flat section of the curve lasts for the melting time",
        working=[f"the temperature stays at {mp} °C (the melting point) from {t_start} min to {t_start + dur} min", f"melting time = {t_start + dur} − {t_start}", f"= **{dur} min**"],
        hints=[
            "Which part of the curve shows the substance melting? Think about what happens to the temperature during a change of state.",
            "Energy supplied during the flat section goes into separating the particles (latent heat), not into raising the temperature.",
            "Read the time at the start and end of the flat section and subtract.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c9_ice_to_warm_water", chapter=9, level=4, lo="9g")
def ice_to_warm_water(rng):
    m = nice(rng, 0.1, 0.2, 0.25, 0.5)
    final = nice(rng, 10, 20, 25, 30, 40)
    Q1 = m * L_ICE
    Q2 = m * C_WATER * final
    Q = Q1 + Q2
    opts, key, mis = numeric_options(rng, Q, [
        (Q1, "That is only the energy to MELT the ice. The water then has to be warmed from 0 °C to the final temperature."),
        (Q2, "That is only the energy to warm the water. The ice must first be melted (latent heat)."),
        (m * L_ICE + m * L_ICE * final, "You used the latent heat for the warming stage too. Warming uses m c Δθ."),
    ], unit="J", sf=3)
    table = md_table(["quantity", "value"], [["mass of ice", f"{fmt(m)} kg"], ["initial temperature", "0 °C"], ["final temperature", f"{final} °C"], ["L of fusion of ice", "334 000 J/kg"], ["c of water", "4200 J/(kg K)"]])
    return dict(
        stem=f"Ice at 0 °C is turned into water at **{final} °C**.\n\n{table}\n\nHow much energy is needed in total?",
        options=opts, key=key, misconceptions=mis,
        formula="two stages: melt the ice (m L) then warm the water (m c Δθ); add them",
        working=[f"melting: Q₁ = m L = {fmt(m)} × 334 000 = {fmt(Q1)} J", f"warming: Q₂ = m c Δθ = {fmt(m)} × 4200 × {final} = {fmt(Q2)} J", f"total = {fmt(Q1)} + {fmt(Q2)} = **{fmt(Q, sf=3)} J**"],
        hints=[
            "The ice goes through two different processes. Name them, and say which formula each one uses.",
            "Stage 1: solid → liquid at 0 °C (latent heat). Stage 2: water from 0 °C up to the final temperature (specific heat capacity).",
            f"{fmt(m)} × 334 000 + {fmt(m)} × 4200 × {final}.",
        ],
    )


@template("c9_power_from_heating_curve", chapter=9, level=4, lo="9c")
def power_from_heating_curve(rng):
    m = nice(rng, 0.5, 1.0, 2.0)
    c = nice(rng, 2400, 4200)
    liquid = "water" if c == 4200 else "ethanol"
    rate = nice(rng, 2, 3, 4, 5)         # °C per minute
    pts = [(0, 20), (10, 20 + 10 * rate)]
    P = m * c * rate / 60
    opts, key, mis = numeric_options(rng, P, [
        (m * c * rate, "You used the temperature rise per MINUTE as if it were per second. Divide by 60."),
        (m * c * 10 * rate, "That is the total energy supplied in 10 minutes, in joules. Power is energy per second."),
        (c * rate / 60, "You left out the mass."),
    ], unit="W", sf=3)
    return dict(
        stem=f"A heater warms **{fmt(m)} kg** of {liquid} (c = {c} J/(kg K)). Fig. 1 shows the temperature-time graph. No energy is lost. What is the power of the heater?",
        figure=figs2.temp_time_graph(pts, xstep=2, ymax=(int((20 + 10 * rate) / 20) + 1) * 20),
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time = m c (Δθ ÷ Δt), with Δt in seconds",
        working=[f"gradient = {rate} °C per minute, so in 10 min Δθ = {10 * rate} °C", f"energy in 10 min = m c Δθ = {fmt(m)} × {c} × {10 * rate} = {fmt(m * c * 10 * rate)} J", f"power = {fmt(m * c * 10 * rate)} ÷ 600 s = **{fmt(P, sf=3)} W**"],
        hints=[
            "Read how much the temperature rises in a known time, then work out the energy that took, then divide by the time in seconds.",
            f"In 10 minutes the temperature rises by {10 * rate} °C. Energy = m c Δθ.",
            f"P = ({fmt(m)} × {c} × {10 * rate}) ÷ 600.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c9_mixing_final_temperature", chapter=9, level=5, lo="9c")
def mixing_final_temperature(rng):
    m_hot = nice(rng, 0.2, 0.3, 0.5)
    m_cold = nice(rng, 0.2, 0.3, 0.5, 1.0)
    hot = nice(rng, 70, 80, 90)
    cold = nice(rng, 10, 20, 25)
    final = (m_hot * hot + m_cold * cold) / (m_hot + m_cold)
    opts, key, mis = numeric_options(rng, final, [
        ((hot + cold) / 2, "That is the simple average, correct only for equal masses." if m_hot != m_cold else "Check the arithmetic."),
        ((m_cold * hot + m_hot * cold) / (m_hot + m_cold) if m_hot != m_cold else final - 7, "You swapped the masses: the larger mass pulls the final temperature towards its own." if m_hot != m_cold else "The final temperature must lie between the two starting temperatures."),
        (hot - cold, "That is the temperature difference, not the final temperature."),
    ], unit="°C", sf=3)
    table = md_table(["water", "mass / kg", "temperature / °C"], [["hot", fmt(m_hot), hot], ["cold", fmt(m_cold), cold]])
    return dict(
        stem=f"Hot water is poured into cold water in an insulated cup.\n\n{table}\n\nAssuming no energy is lost to the cup or the surroundings, what is the final temperature of the mixture?",
        options=opts, key=key, misconceptions=mis,
        formula="energy lost by hot water = energy gained by cold water:  m_hot c (θ_hot − θ) = m_cold c (θ − θ_cold)",
        working=[f"{fmt(m_hot)} × 4200 × ({hot} − θ) = {fmt(m_cold)} × 4200 × (θ − {cold})", f"θ = ({fmt(m_hot)} × {hot} + {fmt(m_cold)} × {cold}) ÷ ({fmt(m_hot)} + {fmt(m_cold)})", f"= **{fmt(final, sf=3)} °C**"],
        hints=[
            "Energy lost by the hot water equals energy gained by the cold water. Write both as m c Δθ with the same unknown final temperature θ.",
            "c cancels from both sides, leaving m_hot (hot − θ) = m_cold (θ − cold).",
            f"θ = ({fmt(m_hot)} × {hot} + {fmt(m_cold)} × {cold}) ÷ {fmt(m_hot + m_cold)}.",
        ],
    )


@template("c9_kettle_efficiency", chapter=9, level=5, lo="9c")
def kettle_efficiency(rng):
    P = nice(rng, 2000, 2200, 2400, 3000)
    m = nice(rng, 1.0, 1.5)
    dt = nice(rng, 60, 70, 75, 80)
    useful = m * C_WATER * dt
    eff = nice(rng, 0.80, 0.84, 0.90)
    t = round(useful / (P * eff))
    actual_eff = useful / (P * t) * 100
    opts, key, mis = numeric_options(rng, actual_eff, [
        (100, "Not all the electrical energy ends up in the water: some warms the kettle and the air. The efficiency must be below 100%."),
        (useful / P / t, "You found the fraction but forgot to multiply by 100 for a percentage."),
        (P * t / useful * 100, "You divided input by output. Efficiency = useful output ÷ total input × 100%."),
    ], unit="%", sf=3)
    table = md_table(["quantity", "value"], [["power rating of kettle", f"{P} W"], ["mass of water", f"{fmt(m)} kg"], ["temperature rise", f"{dt} °C"], ["time taken", f"{t} s"]])
    return dict(
        stem=f"A kettle heats water. The table gives the measurements.\n\n{table}\n\nTaking the specific heat capacity of water as 4200 J/(kg K), what is the efficiency of the kettle?",
        options=opts, key=key, misconceptions=mis,
        formula="efficiency = useful energy to the water (m c Δθ) ÷ electrical energy supplied (P t) × 100%",
        working=[f"useful energy = m c Δθ = {fmt(m)} × 4200 × {dt} = {fmt(useful)} J", f"energy supplied = P t = {P} × {t} = {fmt(P * t)} J", f"efficiency = {fmt(useful)} ÷ {fmt(P * t)} × 100 = **{fmt(actual_eff, sf=3)}%**"],
        hints=[
            "Two energies are needed: the useful energy that went into the water, and the total electrical energy the kettle used.",
            f"Useful: m c Δθ. Supplied: power × time = {P} × {t} J.",
            f"efficiency = {fmt(useful)} ÷ {fmt(P * t)} × 100.",
        ],
    )
