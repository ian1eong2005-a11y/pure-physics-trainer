"""Chapter 15 D.C. Circuits (6091): series and parallel resistors, current and p.d. rules, combined circuits, potential dividers
with LDRs and thermistors."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template

PAR = [(6, 3), (4, 12), (10, 10), (6, 12), (3, 6), (20, 5), (8, 8), (2, 2)]      # pairs with whole-number parallel results


def par(a, b):
    return a * b / (a + b)


# ---------------------------------------------------------------- L1
@template("c15_series_total_resistance", chapter=15, level=1, lo="15f")
def series_total_resistance(rng):
    r1, r2 = nice(rng, 2, 3, 4, 5, 6, 8, 10), nice(rng, 2, 3, 4, 5, 6, 8, 10, 12)
    total = r1 + r2
    opts, key, mis = numeric_options(rng, total, [
        (par(r1, r2), "That is the PARALLEL combination. These resistors are in series: just add them."),
        (abs(r1 - r2) or r1 * 2, "You subtracted. Resistors in series add up."),
        (r1 * r2, "You multiplied. Series resistances add."),
    ], unit="Ω", sf=3)
    return dict(
        stem=f"Fig. 1 shows two resistors of **{r1} Ω** and **{r2} Ω** connected in series. What is their combined resistance?",
        figure=figs3.circuit(top=[("R", f"{r1} Ω"), ("R", f"{r2} Ω")]),
        options=opts, key=key, misconceptions=mis,
        formula="in series: R = R₁ + R₂",
        working=["R = R₁ + R₂", f"= {r1} + {r2}", f"= **{total} Ω**"],
        hints=[
            "The current has to pass through both resistors one after the other.",
            "Resistances in series simply add.",
            f"{r1} + {r2} = ?",
        ],
    )


@template("c15_parallel_branch_current", chapter=15, level=1, lo="15e")
def parallel_branch_current(rng):
    V = nice(rng, 6, 9, 12)
    r1, r2 = rng.choice(PAR)
    I1 = V / r1
    opts, key, mis = numeric_options(rng, I1, [
        (V / (r1 + r2), "You used the two resistors added together. In parallel each branch has the FULL supply p.d. across it."),
        (V / r2, f"That is the current in the other branch ({r2} Ω)."),
        (V / par(r1, r2), "That is the TOTAL current from the supply, not the current in this one branch."),
    ], unit="A", sf=3)
    return dict(
        stem=f"Fig. 1 shows two resistors in parallel across a **{V} V** supply. What is the current in the **{r1} Ω** resistor?",
        figure=figs3.circuit(emf=f"{V} V", branches=[[("R", f"{r1} Ω")], [("R", f"{r2} Ω")]]),
        options=opts, key=key, misconceptions=mis,
        formula="in parallel the p.d. across each branch equals the supply p.d.; I = V ÷ R for that branch",
        working=[f"p.d. across the {r1} Ω resistor = {V} V (same as the supply)", f"I = V ÷ R = {V} ÷ {r1}", f"= **{fmt(I1, sf=3)} A**"],
        hints=[
            "What is the p.d. across each branch of a parallel circuit?",
            f"The full {V} V is across the {r1} Ω resistor on its own.",
            f"I = {V} ÷ {r1}.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c15_series_current", chapter=15, level=2, lo="15g")
def series_current(rng):
    V = nice(rng, 6, 9, 12)
    r1, r2 = nice(rng, 2, 3, 4, 6, 8), nice(rng, 2, 4, 6, 8, 10)
    I = V / (r1 + r2)
    opts, key, mis = numeric_options(rng, I, [
        (V / r1, "You used only one resistor. In series the current is limited by the TOTAL resistance."),
        (V / par(r1, r2), "You used the parallel combination. These resistors are in series."),
        (V * (r1 + r2), "You multiplied. I = V ÷ R."),
    ], unit="A", sf=3)
    return dict(
        stem=f"Fig. 1 shows a **{V} V** battery connected to resistors of **{r1} Ω** and **{r2} Ω** in series. What is the reading on the ammeter?",
        figure=figs3.circuit(emf=f"{V} V", top=[("R", f"{r1} Ω"), ("R", f"{r2} Ω")], bottom=[("A", "")]),
        options=opts, key=key, misconceptions=mis,
        formula="series: R = R₁ + R₂; I = V ÷ R (the same current everywhere in a series circuit)",
        working=[f"R = {r1} + {r2} = {r1 + r2} Ω", f"I = V ÷ R = {V} ÷ {r1 + r2}", f"= **{fmt(I, sf=3)} A**"],
        hints=[
            "First find the total resistance of the series circuit.",
            f"R = {r1} + {r2} Ω. The same current flows through the whole loop.",
            f"I = {V} ÷ {r1 + r2}.",
        ],
    )


@template("c15_parallel_effective_resistance", chapter=15, level=2, lo="15f")
def parallel_effective_resistance(rng):
    r1, r2 = rng.choice(PAR)
    R = par(r1, r2)
    opts, key, mis = numeric_options(rng, R, [
        (r1 + r2, "You added the resistors, which is the SERIES rule. In parallel the combined resistance is less than either resistor."),
        ((r1 + r2) / 2, "You averaged them. Use 1/R = 1/R₁ + 1/R₂."),
        (1 / (1 / r1 + 1 / r2) * 2 if r1 != r2 else r1, "Check the final step: after adding 1/R₁ + 1/R₂, you must take the reciprocal."),
    ], unit="Ω", sf=3)
    return dict(
        stem=f"Fig. 1 shows resistors of **{r1} Ω** and **{r2} Ω** connected in parallel. What is their effective resistance?",
        figure=figs3.circuit(branches=[[("R", f"{r1} Ω")], [("R", f"{r2} Ω")]], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="in parallel: 1/R = 1/R₁ + 1/R₂  (or R = R₁R₂ ÷ (R₁ + R₂) for two resistors)",
        working=[f"1/R = 1/{r1} + 1/{r2} = {fmt(1 / r1 + 1 / r2, sf=3)}", f"R = 1 ÷ {fmt(1 / r1 + 1 / r2, sf=3)}", f"= **{fmt(R, sf=3)} Ω**"],
        hints=[
            "Parallel resistors give MORE paths for the current, so the combined resistance is smaller than either one.",
            f"1/R = 1/{r1} + 1/{r2}.",
            "Add the fractions, then turn the answer upside down.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c15_series_pd_share", chapter=15, level=3, lo="15c")
def series_pd_share(rng):
    V = nice(rng, 6, 9, 12)
    r1, r2 = rng.choice([(2, 4), (4, 8), (3, 6), (6, 6), (2, 10), (4, 2), (9, 3), (5, 10)])
    V2 = V * r2 / (r1 + r2)
    opts, key, mis = numeric_options(rng, V2, [
        (V * r1 / (r1 + r2), f"That is the p.d. across the {r1} Ω resistor. The p.d.s are shared in the ratio of the resistances."),
        (V, "The whole supply p.d. is shared between the two resistors; only in PARALLEL does each get the full p.d."),
        (V / 2, "Equal shares happen only when the resistors are equal." if r1 != r2 else "Check the arithmetic: equal resistors share the p.d. equally."),
    ], unit="V", sf=3)
    return dict(
        stem=f"Fig. 1 shows a **{V} V** supply connected to resistors of **{r1} Ω** and **{r2} Ω** in series. What is the reading on the voltmeter connected across the **{r2} Ω** resistor?",
        figure=figs3.circuit(emf=f"{V} V", top=[("R", f"{r1} Ω"), ("R", f"{r2} Ω")], volt_across=1),
        options=opts, key=key, misconceptions=mis,
        formula="series: I = V ÷ (R₁ + R₂); V₂ = I R₂  (the p.d. is shared in proportion to the resistances)",
        working=[f"I = {V} ÷ ({r1} + {r2}) = {fmt(V / (r1 + r2), sf=3)} A", f"V₂ = I R₂ = {fmt(V / (r1 + r2), sf=3)} × {r2}", f"= **{fmt(V2, sf=3)} V**"],
        hints=[
            "Find the current first: it is the same through both resistors.",
            f"I = {V} ÷ {r1 + r2} A. Then V = I R for the {r2} Ω resistor.",
            f"V₂ = {fmt(V / (r1 + r2), sf=3)} × {r2}.",
        ],
    )


@template("c15_parallel_total_current", chapter=15, level=3, lo="15d")
def parallel_total_current(rng):
    V = nice(rng, 6, 9, 12)
    r1, r2 = rng.choice(PAR)
    I1, I2 = V / r1, V / r2
    I = I1 + I2
    opts, key, mis = numeric_options(rng, I, [
        (V / (r1 + r2), "You added the resistances as if in series. In parallel, find each branch current and add the CURRENTS."),
        (max(I1, I2), "That is the current in one branch only. The supply current is the sum of both branch currents."),
        (I / 2, "You halved the total. The ammeter in the main part of the circuit reads the sum of the branch currents."),
    ], unit="A", sf=3)
    return dict(
        stem=f"Fig. 1 shows resistors of **{r1} Ω** and **{r2} Ω** in parallel across a **{V} V** supply. What is the reading on the ammeter in the main circuit?",
        figure=figs3.circuit(emf=f"{V} V", top=[("A", "")], branches=[[("R", f"{r1} Ω")], [("R", f"{r2} Ω")]]),
        options=opts, key=key, misconceptions=mis,
        formula="parallel: each branch has the supply p.d.; branch currents I = V ÷ R; total current = sum of the branch currents",
        working=[f"I₁ = {V} ÷ {r1} = {fmt(I1, sf=3)} A;  I₂ = {V} ÷ {r2} = {fmt(I2, sf=3)} A", f"total = {fmt(I1, sf=3)} + {fmt(I2, sf=3)}", f"= **{fmt(I, sf=3)} A**"],
        hints=[
            "Work out the current in each branch separately. What p.d. is across each?",
            f"Each branch has {V} V across it: I₁ = {V} ÷ {r1}, I₂ = {V} ÷ {r2}.",
            "The main ammeter reads the sum of the two branch currents.",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c15_series_parallel_combined", chapter=15, level=4, lo="15g")
def series_parallel_combined(rng):
    V = nice(rng, 6, 9, 12)
    r1 = nice(rng, 2, 3, 4, 6)
    r2, r3 = rng.choice(PAR)
    Rp = par(r2, r3)
    Rt = r1 + Rp
    I = V / Rt
    opts, key, mis = numeric_options(rng, I, [
        (V / (r1 + r2 + r3), "You added all three resistors. The two in parallel must be combined with the parallel rule first."),
        (V / r1, "You ignored the parallel pair. They add to the total resistance."),
        (V / Rp, "You left out the series resistor."),
    ], unit="A", sf=3)
    return dict(
        stem=f"Fig. 1 shows a **{V} V** battery connected to a **{r1} Ω** resistor in series with a parallel pair of **{r2} Ω** and **{r3} Ω**. What is the current from the battery?",
        figure=figs3.circuit(emf=f"{V} V", top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]], bottom=[("A", "")]),
        options=opts, key=key, misconceptions=mis,
        formula="combine the parallel pair (1/R = 1/R₂ + 1/R₃), add the series resistor, then I = V ÷ R_total",
        working=[f"parallel pair: R = ({r2} × {r3}) ÷ ({r2} + {r3}) = {fmt(Rp, sf=3)} Ω", f"total = {r1} + {fmt(Rp, sf=3)} = {fmt(Rt, sf=3)} Ω", f"I = {V} ÷ {fmt(Rt, sf=3)} = **{fmt(I, sf=3)} A**"],
        hints=[
            "Reduce the circuit step by step: first replace the parallel pair by a single resistor.",
            f"The pair gives {fmt(Rp, sf=3)} Ω. Now add the {r1} Ω in series.",
            f"I = {V} ÷ {fmt(Rt, sf=3)}.",
        ],
    )


@template("c15_potential_divider_output", chapter=15, level=4, lo="15h")
def potential_divider_output(rng):
    V = nice(rng, 6, 9, 12)
    r1, r2 = rng.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 4), (4, 2), (1, 5), (5, 1)])
    r1k, r2k = r1 * 1000, r2 * 1000
    Vout = V * r2 / (r1 + r2)
    opts, key, mis = numeric_options(rng, Vout, [
        (V * r1 / (r1 + r2), "That is the p.d. across R₁. The output is taken across R₂."),
        (V, "The output is only PART of the supply p.d.; the rest is across R₁."),
        (V / 2, "The p.d. divides equally only when the two resistors are equal." if r1 != r2 else "Check the arithmetic."),
    ], unit="V", sf=3)
    return dict(
        stem=f"Fig. 1 shows a potential divider connected to a **{V} V** supply. R₁ = **{r1} kΩ** and R₂ = **{r2} kΩ**. What is the output p.d. across R₂?",
        figure=figs3.potential_divider(vin=f"{V} V", r1=f"R₁ = {r1} kΩ", r2=f"R₂ = {r2} kΩ"),
        options=opts, key=key, misconceptions=mis,
        formula="V_out = V_in × R₂ ÷ (R₁ + R₂)",
        working=[f"V_out = {V} × {r2} ÷ ({r1} + {r2})", f"= {V} × {fmt(r2 / (r1 + r2), sf=3)}", f"= **{fmt(Vout, sf=3)} V**"],
        hints=[
            "The two resistors in series share the supply p.d. in the ratio of their resistances.",
            f"R₂ is {r2} parts out of {r1 + r2}.",
            f"V_out = {V} × {r2}/{r1 + r2}.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c15_thermistor_divider_change", chapter=15, level=5, lo="15j")
def thermistor_divider_change(rng):
    V = nice(rng, 6, 9, 12)
    Rf = nice(rng, 2, 4, 5)                           # fixed resistor, kΩ
    Rcold, Rhot = rng.choice([(8, 2), (10, 2), (6, 1), (12, 3), (20, 4)])
    Vcold = V * Rf / (Rf + Rcold)
    Vhot = V * Rf / (Rf + Rhot)
    opts, key, mis = numeric_options(rng, Vhot, [
        (Vcold, "That is the output when the thermistor is COLD. When it warms up its resistance falls, so the share across the fixed resistor rises."),
        (V * Rhot / (Rf + Rhot), "That is the p.d. across the thermistor. The output is across the fixed resistor."),
        (V - Vcold, "That is the p.d. across the thermistor when cold. Recalculate with the hot resistance."),
    ], unit="V", sf=3)
    table = md_table(["", "resistance of thermistor"], [["cold (20 °C)", f"{Rcold} kΩ"], ["hot (80 °C)", f"{Rhot} kΩ"]])
    return dict(
        stem=f"Fig. 1 shows a temperature sensor: an NTC thermistor in series with a fixed **{Rf} kΩ** resistor across a **{V} V** supply, with the output taken across the fixed resistor.\n\n{table}\n\nWhat is the output p.d. when the thermistor is hot?",
        figure=figs3.potential_divider(vin=f"{V} V", r1="thermistor", r2=f"{Rf} kΩ", top_kind="therm"),
        options=opts, key=key, misconceptions=mis,
        formula="V_out = V × R_fixed ÷ (R_fixed + R_thermistor); an NTC thermistor's resistance falls as it gets hotter",
        working=[f"hot: R_thermistor = {Rhot} kΩ", f"V_out = {V} × {Rf} ÷ ({Rf} + {Rhot})", f"= **{fmt(Vhot, sf=3)} V**  (cold: {fmt(Vcold, sf=3)} V)"],
        hints=[
            "Which value of the thermistor's resistance applies when it is hot? (NTC: resistance falls with temperature.)",
            f"Use the divider formula with R_thermistor = {Rhot} kΩ and the output across the {Rf} kΩ resistor.",
            f"V_out = {V} × {Rf} ÷ ({Rf} + {Rhot}).",
        ],
    )


@template("c15_branch_current_with_series_resistor", chapter=15, level=5, lo="15g")
def branch_current_with_series_resistor(rng):
    V = nice(rng, 6, 9, 12)
    r1 = nice(rng, 1, 2, 3)
    r2, r3 = rng.choice([(6, 3), (4, 12), (6, 12), (3, 6), (20, 5)])
    Rp = par(r2, r3)
    I = V / (r1 + Rp)
    Vp = I * Rp
    I2 = Vp / r2
    opts, key, mis = numeric_options(rng, I2, [
        (V / r2, "You used the full supply p.d. across the branch, but some p.d. is dropped across the series resistor first."),
        (I, "That is the TOTAL current from the battery. Only part of it goes through this branch."),
        (Vp / r3, f"That is the current in the other branch ({r3} Ω)."),
    ], unit="A", sf=3)
    return dict(
        stem=f"In Fig. 1 a **{V} V** battery drives current through a **{r1} Ω** resistor in series with a parallel pair of **{r2} Ω** and **{r3} Ω**. What is the current in the **{r2} Ω** resistor?",
        figure=figs3.circuit(emf=f"{V} V", top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]]),
        options=opts, key=key, misconceptions=mis,
        formula="total R → total I → p.d. across the parallel pair (I × R_parallel) → branch current = that p.d. ÷ branch resistance",
        working=[f"R_parallel = {fmt(Rp, sf=3)} Ω; total R = {r1} + {fmt(Rp, sf=3)} = {fmt(r1 + Rp, sf=3)} Ω; I = {V} ÷ {fmt(r1 + Rp, sf=3)} = {fmt(I, sf=3)} A",
                 f"p.d. across the pair = {fmt(I, sf=3)} × {fmt(Rp, sf=3)} = {fmt(Vp, sf=3)} V", f"current in {r2} Ω = {fmt(Vp, sf=3)} ÷ {r2} = **{fmt(I2, sf=3)} A**"],
        hints=[
            "You cannot use the full battery p.d. across the branch: the series resistor takes some of it. Find the total current first.",
            f"Total current = {V} ÷ ({r1} + {fmt(Rp, sf=3)}). The p.d. across the parallel pair is that current × {fmt(Rp, sf=3)} Ω.",
            f"Branch current = (p.d. across the pair) ÷ {r2}.",
        ],
    )
