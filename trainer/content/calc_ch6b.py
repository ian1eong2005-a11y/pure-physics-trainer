"""Chapter 6 Energy (6091 additions): efficiency (LO 6f)."""
from .. import sketches
from .base import fmt, md_table, nice, numeric_options, template


@template("c6_efficiency_percent", chapter=6, level=2, lo="6f")
def efficiency_percent(rng):
    total = nice(rng, 500, 800, 1000, 1200, 2000)
    eff = nice(rng, 0.25, 0.30, 0.40, 0.60, 0.75)
    useful = total * eff
    opts, key, mis = numeric_options(rng, eff * 100, [
        ((1 - eff) * 100, "That is the percentage WASTED. Efficiency is the useful output as a percentage of the input."),
        (total / useful, "You divided input by output. Efficiency = useful output ÷ total input × 100%."),
        (eff, "You forgot to multiply by 100 to get a percentage."),
    ], unit="%", sf=3)
    table = md_table(["", "energy / J"], [["electrical energy supplied to the motor", fmt(total)], ["useful work done lifting the load", fmt(useful)], ["energy wasted as thermal energy", fmt(total - useful)]])
    return dict(
        stem=f"The table shows the energy transfers for an electric motor lifting a load.\n\n{table}\n\nWhat is the efficiency of the motor?",
        options=opts, key=key, misconceptions=mis,
        formula="efficiency = useful energy output ÷ total energy input × 100%",
        working=["efficiency = useful output ÷ total input × 100%", f"= {fmt(useful)} ÷ {fmt(total)} × 100", f"= **{fmt(eff * 100, sf=3)}%**"],
        hints=[
            "Efficiency compares the USEFUL energy out with the TOTAL energy in.",
            f"useful = {fmt(useful)} J, total = {fmt(total)} J.",
            f"{fmt(useful)} ÷ {fmt(total)} × 100 = ?",
        ],
    )


@template("c6_input_from_efficiency", chapter=6, level=4, lo="6f")
def input_from_efficiency(rng):
    m = nice(rng, 20, 40, 50, 80, 100)
    h = nice(rng, 2.0, 3.0, 5.0, 8.0)
    eff = nice(rng, 0.20, 0.25, 0.40, 0.50)
    useful = m * 10 * h
    total = useful / eff
    opts, key, mis = numeric_options(rng, total, [
        (useful, "That is the useful work (gain in gravitational potential energy). The motor needs MORE than this, because it is not 100% efficient."),
        (useful * eff, "You multiplied by the efficiency. Input = useful output ÷ efficiency, which gives a LARGER number."),
        (m * h / eff, "You forgot g: gravitational potential energy = m g h with g = 10 N/kg."),
    ], unit="J", sf=3)
    return dict(
        stem=f"Fig. 1 shows a motor lifting a load of mass **{m} kg** through a height of **{fmt(h)} m**. The motor is **{round(eff * 100)}% efficient**. Taking g = 10 N/kg, how much electrical energy must be supplied to the motor?",
        figure=sketches.lift_sketch(f"{fmt(h)} m", body_label=f"{m} kg", extra=f"motor efficiency {round(eff * 100)}%"),
        options=opts, key=key, misconceptions=mis,
        formula="useful output = m g h; efficiency = useful ÷ input, so input = useful ÷ efficiency",
        working=[f"useful energy = m g h = {m} × 10 × {fmt(h)} = {fmt(useful)} J", f"input = useful ÷ efficiency = {fmt(useful)} ÷ {fmt(eff)}", f"= **{fmt(total, sf=3)} J**"],
        hints=[
            "First find the useful energy: the gain in gravitational potential energy of the load.",
            f"Only {round(eff * 100)}% of the input becomes useful. So the input must be larger than {fmt(useful)} J.",
            f"input = {fmt(useful)} ÷ {fmt(eff)}.",
        ],
    )
