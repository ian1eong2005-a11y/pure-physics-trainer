"""Chapter 15 D.C. Circuits (6091) bank extension: calculation and data-reading templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2016-2025: lamps in series and parallel, ammeter readings at different points,
potential dividers with a thermistor or LDR, combined series-parallel networks; school papers 2024-2025)."""
from .. import figs3
from .base import fmt, md_table, mk, mkt, nice, template

PAIRS = [(6, 3), (4, 4), (12, 6), (20, 30), (10, 40), (6, 12), (3, 6), (10, 10), (12, 4), (30, 60)]


def par(a, b):
    return a * b / (a + b)


# ================================================================== L1
@template("c15x_series_current_same", chapter=15, level=1, lo="15b")
def series_current_same(rng):
    I = nice(rng, 0.2, 0.3, 0.5, 1.2)
    return mk(rng, I, [(I / 2, "The current is the SAME everywhere in a series circuit."), (2 * I, "Current is not shared or doubled in series."), (I + 0.1, "Series: the same current flows through every component.")],
              "A", f"In the series circuit of Fig. 1, the ammeter next to the cell reads **{fmt(I)} A**. What is the current through the second resistor?",
              "series: I is the same at every point", [f"I = **{fmt(I)} A** everywhere"],
              ["Is there any branch?", "There is only one path.", "The current is the same everywhere."], figure=figs3.circuit(top=[("R", "R₁"), ("R", "R₂")], bottom=[("A", f"{fmt(I)} A")]))


@template("c15x_series_two_ammeters", chapter=15, level=1, lo="15b")
def series_two_ammeters(rng):
    I = nice(rng, 0.15, 0.25, 0.4, 0.6)
    return mk(rng, I, [(0, "Charge is not used up; the current is the same after the lamps."), (I / 2, "The current is not halved by passing through two lamps."), (2 * I, "Series current is the same everywhere.")],
              "A", f"Two lamps are in series with a battery.\n\n{md_table(['ammeter position', 'reading / A'], [['before the first lamp', fmt(I)], ['after the second lamp', '?']])}\n\nWhat does the second ammeter read?",
              "series: same current everywhere (charge conserved)", [f"**{fmt(I)} A**"],
              ["Is current used up?", "No, charge is conserved.", "Same reading."])


@template("c15x_series_pd_sum_simple", chapter=15, level=1, lo="15c")
def series_pd_sum_simple(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    V1 = nice(rng, 2.0, 2.5, 4.0)
    return mk(rng, V - V1, [(V, "The e.m.f. is SHARED between the components."), (V + V1, "Subtract, do not add."), (V1, "That is the p.d. across the first resistor.")],
              "V", f"Two resistors are in series with a **{fmt(V)} V** supply (Fig. 1). The p.d. across the first resistor is **{fmt(V1)} V**. What is the p.d. across the second?",
              "series: e.m.f. = sum of p.d.s", [f"V₂ = {fmt(V)} − {fmt(V1)} = **{fmt(V - V1)} V**"],
              ["The p.d.s add up to the e.m.f.", "Subtract.", "Answer in V."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("R", f"{fmt(V1)} V"), ("R", "?")]))


@template("c15x_series_three_lamps_pd", chapter=15, level=1, lo="15c")
def series_three_lamps_pd(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    n = 3
    return mk(rng, V / n, [(V, "The supply p.d. is shared between the three lamps."), (V * n, "Divide, do not multiply."), (V / 2, "There are three identical lamps.")],
              "V", f"{md_table(['quantity', 'value'], [['supply e.m.f.', f'{fmt(V)} V'], ['identical lamps in series', n]])}\n\nWhat is the p.d. across each lamp?",
              "identical components in series share the p.d. equally", [f"V = {fmt(V)} ÷ 3 = **{fmt(V / n)} V**"],
              ["The p.d.s add to the e.m.f.", "The lamps are identical.", "Divide by 3."])


@template("c15x_parallel_current_sum", chapter=15, level=1, lo="15d")
def parallel_current_sum(rng):
    I1 = nice(rng, 0.2, 0.3, 0.5)
    I2 = nice(rng, 0.4, 0.6, 0.8)
    return mk(rng, I1 + I2, [(abs(I2 - I1), "In parallel, the branch currents ADD."), (I2, "Include both branches."), ((I1 + I2) / 2, "Add, do not average.")],
              "A", f"Two lamps are in parallel (Fig. 1).\n\n{md_table(['branch', 'current / A'], [['lamp 1', fmt(I1)], ['lamp 2', fmt(I2)]])}\n\nWhat is the current from the cell?",
              "parallel: I_total = I₁ + I₂", [f"I = {fmt(I1)} + {fmt(I2)} = **{fmt(I1 + I2)} A**"],
              ["The current splits at the junction.", "It rejoins after.", "Add the branch currents."], figure=figs3.circuit(top=[("A", "?")], branches=[[("lamp", "")], [("lamp", "")]]))


@template("c15x_parallel_missing_branch", chapter=15, level=1, lo="15d")
def parallel_missing_branch(rng):
    I = nice(rng, 1.0, 1.2, 1.5, 2.0)
    I1 = nice(rng, 0.3, 0.4, 0.5)
    return mk(rng, I - I1, [(I + I1, "Subtract the known branch current from the total."), (I, "That is the total current."), (I / 2, "The branches need not carry equal currents.")],
              "A", f"{md_table(['ammeter position', 'reading / A'], [['main circuit', fmt(I)], ['branch 1', fmt(I1)], ['branch 2', '?']])}\n\nWhat is the current in branch 2 of this two-branch parallel circuit?",
              "I_total = I₁ + I₂", [f"I₂ = {fmt(I)} − {fmt(I1)} = **{fmt(I - I1)} A**"],
              ["The branch currents add to the total.", "Subtract.", "Answer in A."])


@template("c15x_parallel_pd_same", chapter=15, level=1, lo="15e")
def parallel_pd_same(rng):
    V = nice(rng, 3.0, 6.0, 12.0)
    return mk(rng, V, [(V / 2, "Each parallel branch has the FULL supply p.d. across it."), (2 * V, "The p.d. is not doubled."), (V / 3, "Parallel components share the same p.d.")],
              "V", f"Two different resistors are connected in parallel across a **{fmt(V)} V** supply (Fig. 1). What is the p.d. across the second resistor?",
              "parallel: same p.d. across each branch", [f"**{fmt(V)} V**"],
              ["Each branch is connected directly across the supply.", "Same p.d.", "Answer."], figure=figs3.circuit(emf=f"{fmt(V)} V", branches=[[("R", "R₁")], [("R", "R₂")]]))


@template("c15x_series_total_r_simple", chapter=15, level=1, lo="15f")
def series_total_r_simple(rng):
    r1, r2 = nice(rng, 4, 6, 10, 15), nice(rng, 5, 8, 20, 30)
    return mk(rng, r1 + r2, [(par(r1, r2), "That is for PARALLEL; in series, add."), (abs(r1 - r2), "Add the resistances."), (r1 * r2, "Add, do not multiply.")],
              "Ω", f"Resistors of **{r1} Ω** and **{r2} Ω** are connected in series (Fig. 1). What is the combined resistance?",
              "series: R = R₁ + R₂", [f"R = {r1} + {r2} = **{r1 + r2} Ω**"],
              ["Series resistances add.", "R = R₁ + R₂.", "Add."], figure=figs3.circuit(top=[("R", f"{r1} Ω"), ("R", f"{r2} Ω")]), dp=0)


# ================================================================== L2
@template("c15x_parallel_two_equal", chapter=15, level=2, lo="15f")
def parallel_two_equal(rng):
    R = nice(rng, 10, 20, 40, 100)
    n = nice(rng, 2, 4, 5)
    return mk(rng, R / n, [(R * n, "In parallel the combined resistance is SMALLER."), (R, "Adding parallel paths lowers the resistance."), (R / n ** 2, "For n equal resistors in parallel, R_total = R ÷ n.")],
              "Ω", f"{md_table(['quantity', 'value'], [['number of identical resistors in parallel', n], ['resistance of each', f'{R} Ω']])}\n\nWhat is the combined resistance?",
              "n equal resistors in parallel: R ÷ n", [f"R = {R} ÷ {n} = **{fmt(R / n)} Ω**"],
              ["More paths → less resistance.", "Equal resistors share equally.", "R ÷ n."])


@template("c15x_series_current_from_total", chapter=15, level=2, lo="15g")
def series_current_from_total(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    r1, r2 = rng.choice([(2, 4), (5, 10), (10, 20), (4, 8), (6, 12)])
    I = V / (r1 + r2)
    return mk(rng, I, [(V / r1, "Use the TOTAL resistance in series."), (V / par(r1, r2), "These are in series, not parallel."), (V * (r1 + r2), "I = V ÷ R.")],
              "A", f"Resistors of **{r1} Ω** and **{r2} Ω** are in series with a **{fmt(V)} V** supply (Fig. 1). What current flows?",
              "R_total = R₁ + R₂; I = V ÷ R_total", [f"R = {r1} + {r2} = {r1 + r2} Ω", f"I = {fmt(V)} ÷ {r1 + r2} = **{fmt(I)} A**"],
              ["Find the total resistance.", "Add for series.", "I = V ÷ R."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("R", f"{r1} Ω"), ("R", f"{r2} Ω")], bottom=[("A", "?")]))


@template("c15x_pd_each_series", chapter=15, level=2, lo="15c")
def pd_each_series(rng):
    V = nice(rng, 6.0, 12.0)
    r1, r2 = rng.choice([(2, 4), (10, 20), (4, 8), (5, 15), (3, 9)])
    I = V / (r1 + r2)
    V2 = I * r2
    return mk(rng, V2, [(I * r1, "That is the p.d. across the OTHER resistor."), (V / 2, "The p.d. divides in the ratio of the resistances."), (V, "The supply p.d. is shared.")],
              "V", f"Resistors of **{r1} Ω** and **{r2} Ω** are in series with a **{fmt(V)} V** supply. A voltmeter is across the **{r2} Ω** resistor (Fig. 1). What does it read?",
              "I = V ÷ (R₁ + R₂); V₂ = I R₂", [f"I = {fmt(V)} ÷ {r1 + r2} = {fmt(I)} A", f"V₂ = {fmt(I)} × {r2} = **{fmt(V2)} V**"],
              ["Find the current.", "Same current in each.", "V = I R for the second resistor."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("R", f"{r1} Ω"), ("R", f"{r2} Ω")], volt_across=1))


@template("c15x_series_pd_ratio", chapter=15, level=2, lo="15c")
def series_pd_ratio(rng):
    r1, k = nice(rng, 100, 200), nice(rng, 2, 3, 4)
    r2 = r1 * k
    V1 = nice(rng, 1.5, 2.0, 3.0)
    return mk(rng, V1 * k, [(V1 / k, "The LARGER resistor has the larger p.d. in series."), (V1, "The p.d.s are in the ratio of the resistances."), (V1 + k, "Multiply by the resistance ratio.")],
              "V", f"Two resistors in series carry the same current.\n\n{md_table(['resistor', 'resistance / Ω', 'p.d. / V'], [['A', r1, fmt(V1)], ['B', r2, '?']])}\n\nWhat is the p.d. across B?",
              "series: V ∝ R (same I)", [f"V_B = {fmt(V1)} × {k} = **{fmt(V1 * k)} V**"],
              ["Same current through both.", "V = I R.", "V ∝ R."])


@template("c15x_parallel_three_branches", chapter=15, level=2, lo="15d")
def parallel_three_branches(rng):
    Is = [nice(rng, 0.1, 0.2), nice(rng, 0.3, 0.4), nice(rng, 0.5, 0.6)]
    tot = sum(Is)
    return mk(rng, tot, [(max(Is), "Add ALL the branch currents."), (tot / 3, "Add, do not average."), (Is[0] + Is[1], "Include all three branches.")],
              "A", f"Three lamps are connected in parallel.\n\n{md_table(['lamp', 'current / A'], [[i + 1, fmt(x)] for i, x in enumerate(Is)])}\n\nWhat is the total current from the supply?",
              "I_total = sum of branch currents", [f"I = {' + '.join(fmt(x) for x in Is)} = **{fmt(tot)} A**"],
              ["Current splits into branches.", "It all comes from the supply.", "Add them."])


@template("c15x_parallel_branch_from_r", chapter=15, level=2, lo="15d")
def parallel_branch_from_r(rng):
    V = nice(rng, 6.0, 12.0)
    r1, r2 = rng.choice([(6, 12), (4, 12), (10, 20), (3, 6), (12, 24)])
    I = V / r1 + V / r2
    return mk(rng, I, [(V / (r1 + r2), "These are in parallel: each branch has the full p.d."), (V / r1, "Add the current in the other branch too."), (V / r2, "Add both branch currents.")],
              "A", f"Resistors of **{r1} Ω** and **{r2} Ω** are in parallel across a **{fmt(V)} V** supply (Fig. 1). What is the total current from the supply?",
              "I₁ = V ÷ R₁; I₂ = V ÷ R₂; I = I₁ + I₂", [f"I₁ = {fmt(V)} ÷ {r1} = {fmt(V / r1)} A; I₂ = {fmt(V)} ÷ {r2} = {fmt(V / r2)} A", f"I = **{fmt(I)} A**"],
              ["Same p.d. across each branch.", "Find each branch current.", "Add."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("A", "")], branches=[[("R", f"{r1} Ω")], [("R", f"{r2} Ω")]]))


@template("c15x_series_ammeter_lamps", chapter=15, level=2, lo="15b")
def series_ammeter_lamps(rng):
    V = nice(rng, 6.0, 12.0)
    R = nice(rng, 4, 6, 8, 12)
    n = nice(rng, 2, 3)
    I = V / (n * R)
    return mk(rng, I, [(V / R, "There are several lamps in series: add their resistances."), (V / R / n * n * n, "R_total = n × R."), (V * n / R, "More lamps in series → LESS current.")],
              "A", f"{md_table(['quantity', 'value'], [['supply', f'{fmt(V)} V'], ['identical lamps in series', n], ['resistance of each lamp', f'{R} Ω']])}\n\nWhat current flows through each lamp?",
              "R_total = n R; I = V ÷ R_total (same through each)", [f"R = {n} × {R} = {n * R} Ω", f"I = {fmt(V)} ÷ {n * R} = **{fmt(I)} A**"],
              ["Find the total resistance.", "The current is the same through each.", "I = V ÷ R."])


@template("c15x_series_current_after_adding", chapter=15, level=2, lo="15b")
def series_current_after_adding(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    R = nice(rng, 10, 20, 30)
    I1 = V / R
    I2 = V / (2 * R)
    return mk(rng, I2, [(I1, "Adding a second resistor in series increases R, so the current falls."), (2 * I1, "More resistance → LESS current."), (I1 / 4, "Total R doubles, so I halves.")],
              "A", f"A **{R} Ω** resistor is across a **{fmt(V)} V** supply. A second identical resistor is added in **series**.\n\n{md_table(['circuit', 'total resistance / Ω', 'current / A'], [['one resistor', R, fmt(I1)], ['two in series', 2 * R, '?']])}\n\nWhat is the new current?",
              "R doubles → I halves", [f"I = {fmt(V)} ÷ {2 * R} = **{fmt(I2)} A**"],
              ["Series resistances add.", "Total R doubles.", "I = V ÷ R."])


# ================================================================== L3
@template("c15x_parallel_pair", chapter=15, level=3, lo="15f")
def parallel_pair(rng):
    r1, r2 = rng.choice(PAIRS)
    R = par(r1, r2)
    return mk(rng, R, [(r1 + r2, "That is for SERIES; in parallel use 1/R = 1/R₁ + 1/R₂."), ((r1 + r2) / 2, "Do not average the resistances."), (1 / R, "Remember to take the reciprocal at the end.")],
              "Ω", f"Resistors of **{r1} Ω** and **{r2} Ω** are connected in parallel (Fig. 1). What is their combined resistance?",
              "1/R = 1/R₁ + 1/R₂ (or R = R₁R₂ ÷ (R₁ + R₂))", [f"R = {r1} × {r2} ÷ ({r1} + {r2})", f"= **{fmt(R)} Ω**"],
              ["Use the parallel formula.", "Product over sum works for two.", "The answer is less than either."], figure=figs3.circuit(branches=[[("R", f"{r1} Ω")], [("R", f"{r2} Ω")]], emf=""))


@template("c15x_parallel_less_than_smallest", chapter=15, level=3, lo="15f")
def parallel_less_than_smallest(rng):
    r1, r2, r3 = rng.choice([(6, 6, 6), (4, 12, 6), (10, 10, 5), (12, 12, 6)])
    R = 1 / (1 / r1 + 1 / r2 + 1 / r3)
    return mk(rng, R, [(r1 + r2 + r3, "Parallel: add the RECIPROCALS."), (1 / R, "Take the reciprocal at the end."), (min(r1, r2, r3), "The combined resistance is LESS than the smallest.")],
              "Ω", f"Three resistors of **{r1} Ω**, **{r2} Ω** and **{r3} Ω** are connected in parallel.\n\n{md_table(['resistor', 'resistance / Ω'], [['1', r1], ['2', r2], ['3', r3]])}\n\nWhat is the combined resistance?",
              "1/R = 1/R₁ + 1/R₂ + 1/R₃", [f"1/R = 1/{r1} + 1/{r2} + 1/{r3} = {fmt(1 / R, sf=3)}", f"R = **{fmt(R)} Ω**"],
              ["Add the reciprocals.", "Then invert.", "It is less than the smallest resistor."])


@template("c15x_series_parallel_simple", chapter=15, level=3, lo="15g")
def series_parallel_simple(rng):
    r1 = nice(rng, 2, 4, 5)
    r2, r3 = rng.choice([(6, 3), (4, 4), (12, 6), (6, 12)])
    R = r1 + par(r2, r3)
    return mk(rng, R, [(r1 + r2 + r3, "Combine the parallel pair first."), (par(r1 + r2, r3), "Only R₂ and R₃ are in parallel."), (par(r2, r3), "Add the series resistor.")],
              "Ω", f"In Fig. 1, a **{r1} Ω** resistor is in series with a parallel pair of **{r2} Ω** and **{r3} Ω**. What is the total resistance?",
              "parallel pair first, then add series", [f"parallel: {r2} × {r3} ÷ ({r2} + {r3}) = {fmt(par(r2, r3))} Ω", f"total = {r1} + {fmt(par(r2, r3))} = **{fmt(R)} Ω**"],
              ["Find the parallel pair's resistance.", "Then add the series resistor.", "Combine."], figure=figs3.circuit(top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]], emf=""))


@template("c15x_series_parallel_current", chapter=15, level=3, lo="15g")
def series_parallel_current(rng):
    V = nice(rng, 6.0, 12.0)
    r1 = nice(rng, 2, 4)
    r2, r3 = rng.choice([(6, 3), (4, 4), (12, 6)])
    R = r1 + par(r2, r3)
    I = V / R
    return mk(rng, I, [(V / (r1 + r2 + r3), "Combine the parallel pair first; it is not all in series."), (V / r1, "Use the TOTAL resistance."), (V / par(r2, r3), "Include the series resistor.")],
              "A", f"In Fig. 1, a **{r1} Ω** resistor is in series with **{r2} Ω** and **{r3} Ω** in parallel, across **{fmt(V)} V**. What current does the ammeter read?",
              "R_total = R₁ + R₂∥R₃; I = V ÷ R_total", [f"R = {r1} + {fmt(par(r2, r3))} = {fmt(R)} Ω", f"I = {fmt(V)} ÷ {fmt(R)} = **{fmt(I)} A**"],
              ["Find the total resistance.", "Parallel pair first.", "I = V ÷ R."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]], bottom=[("A", "")]))


@template("c15x_divider_simple", chapter=15, level=3, lo="15h")
def divider_simple(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    r1, r2 = rng.choice([(1, 2), (2, 1), (3, 1), (1, 3), (2, 2), (4, 2)])
    Vout = V * r2 / (r1 + r2)
    return mk(rng, Vout, [(V * r1 / (r1 + r2), "That is the p.d. across R₁; the output is across R₂."), (V / 2, "The p.d. splits in the ratio of the resistances."), (V * r2 / r1, "Divide by the TOTAL resistance.")],
              "V", f"Fig. 1 shows a potential divider across **{fmt(V)} V** with R₁ = **{r1} kΩ** and R₂ = **{r2} kΩ**. What is the output p.d. across R₂?",
              "V_out = V × R₂ ÷ (R₁ + R₂)", [f"V_out = {fmt(V)} × {r2} ÷ {r1 + r2} = **{fmt(Vout)} V**"],
              ["The p.d. divides in the ratio of the resistances.", "V_out = V × R₂ ÷ (R₁ + R₂).", "Calculate."], figure=figs3.potential_divider(vin=f"{fmt(V)} V", r1=f"R₁ = {r1} kΩ", r2=f"R₂ = {r2} kΩ"))


@template("c15x_divider_find_r", chapter=15, level=3, lo="15h")
def divider_find_r(rng):
    V = nice(rng, 9.0, 12.0)
    r1 = nice(rng, 2, 4, 6)
    Vout = nice(rng, 3.0, 4.0, 6.0)
    r2 = Vout * r1 / (V - Vout)
    return mk(rng, r2, [(r1 * (V - Vout) / Vout, "R₂ ÷ R₁ = V_out ÷ (V − V_out)."), (r1, "The output is not half unless the resistors are equal."), (Vout * r1 / V, "Use the p.d. across R₁ = V − V_out.")],
              "kΩ", f"A potential divider uses R₁ = **{r1} kΩ** at the top and R₂ at the bottom across **{fmt(V)} V**.\n\n{md_table(['quantity', 'value'], [['required output across R₂', f'{fmt(Vout)} V'], ['R₁', f'{r1} kΩ']])}\n\nWhat must R₂ be?",
              "V₂ ÷ V₁ = R₂ ÷ R₁", [f"V₁ = {fmt(V)} − {fmt(Vout)} = {fmt(V - Vout)} V", f"R₂ = {r1} × {fmt(Vout)} ÷ {fmt(V - Vout)} = **{fmt(r2)} kΩ**"],
              ["Find the p.d. across R₁.", "p.d.s are in the ratio of resistances.", "Solve for R₂."])


@template("c15x_series_lamp_count_pd", chapter=15, level=3, lo="15c")
def series_lamp_count_pd(rng):
    V = 230
    v_lamp = nice(rng, 11.5, 23, 46)
    n = round(V / v_lamp)
    return mk(rng, n, [(V * v_lamp, "n = supply ÷ p.d. per lamp."), (n / 2, "The p.d.s must add to 230 V."), (n + 1, "Divide 230 by the p.d. per lamp.")],
              "lamps", f"A string of identical decorative lamps is connected in series to the 230 V mains.\n\n{md_table(['quantity', 'value'], [['p.d. across each lamp', f'{fmt(v_lamp)} V']])}\n\nHow many lamps are in the string?",
              "series: p.d.s add to the supply", [f"n = 230 ÷ {fmt(v_lamp)} = **{n}**"],
              ["The p.d.s add to 230 V.", "Each lamp has the same p.d.", "Divide."], dp=0)


@template("c15x_parallel_current_split", chapter=15, level=3, lo="15d")
def parallel_current_split(rng):
    I = nice(rng, 0.9, 1.2, 1.5, 3.0)
    r1, r2 = rng.choice([(2, 1), (1, 2), (3, 6), (4, 12)])
    I1 = I * r2 / (r1 + r2)
    return mk(rng, I1, [(I * r1 / (r1 + r2), "The SMALLER resistance takes the LARGER current."), (I / 2, "The currents are only equal if the resistances are equal."), (I, "The total is shared between the branches.")],
              "A", f"A current of **{fmt(I)} A** divides between two parallel resistors.\n\n{md_table(['branch', 'resistance / Ω'], [['1', r1], ['2', r2]])}\n\nWhat current flows through branch 1?",
              "parallel: I ∝ 1/R; I₁ = I × R₂ ÷ (R₁ + R₂)", [f"I₁ = {fmt(I)} × {r2} ÷ ({r1} + {r2}) = **{fmt(I1)} A**"],
              ["Same p.d. across both.", "I = V ÷ R, so smaller R → larger I.", "Share in inverse ratio."])


# ================================================================== L4
@template("c15x_parallel_add_resistor", chapter=15, level=4, lo="15f")
def parallel_add_resistor(rng):
    R1 = nice(rng, 12, 20, 30)
    R2 = R1
    V = nice(rng, 6.0, 12.0)
    I1 = V / R1
    I2 = V / par(R1, R2)
    return mk(rng, I2, [(I1, "Adding a parallel path LOWERS the total resistance, so the total current rises."), (I1 / 2, "Parallel paths increase the current."), (I1 * 4, "R halves, so I doubles.")],
              "A", f"A **{R1} Ω** resistor is across a **{fmt(V)} V** supply. An identical resistor is added in **parallel**.\n\n{md_table(['circuit', 'current from supply / A'], [['one resistor', fmt(I1)], ['two in parallel', '?']])}\n\nWhat is the new current from the supply?",
              "two equal in parallel: R halves → I doubles", [f"R = {R1} ÷ 2 = {fmt(R1 / 2)} Ω", f"I = {fmt(V)} ÷ {fmt(R1 / 2)} = **{fmt(I2)} A**"],
              ["What does a parallel path do to R?", "Lowers it.", "I = V ÷ R."])


@template("c15x_find_parallel_resistor", chapter=15, level=4, lo="15f")
def find_parallel_resistor(rng):
    r1, r2 = rng.choice([(6, 3), (12, 6), (20, 30), (10, 40), (6, 12)])
    R = par(r1, r2)
    return mk(rng, r2, [(R, "That is the combined value; find the unknown resistor."), (r1 - R, "Use 1/R₂ = 1/R − 1/R₁."), (r1 + R, "Parallel: work with reciprocals.")],
              "Ω", f"A **{r1} Ω** resistor is in parallel with an unknown resistor. The combined resistance is **{fmt(R)} Ω**.\n\n{md_table(['quantity', 'value'], [['known resistor', f'{r1} Ω'], ['combined resistance', f'{fmt(R)} Ω']])}\n\nWhat is the unknown resistance?",
              "1/R₂ = 1/R − 1/R₁", [f"1/R₂ = 1/{fmt(R)} − 1/{r1} = {fmt(1 / r2, sf=3)}", f"R₂ = **{r2} Ω**"],
              ["Use the parallel formula.", "Subtract the known reciprocal.", "Invert."])


@template("c15x_branch_current_combined", chapter=15, level=4, lo="15g")
def branch_current_combined(rng):
    V = nice(rng, 12.0)
    r1 = nice(rng, 2, 4)
    r2, r3 = rng.choice([(6, 3), (12, 6), (6, 6)])
    R = r1 + par(r2, r3)
    I = V / R
    Vp = I * par(r2, r3)
    I2 = Vp / r2
    return mk(rng, I2, [(I, "That is the total current; find the share through the {r2} Ω branch.".replace("{r2}", str(r2))), (Vp / r3, "That is the current in the OTHER branch."), (V / r2, "The full 12 V is not across the parallel part.")],
              "A", f"In Fig. 1, **{r1} Ω** is in series with **{r2} Ω** and **{r3} Ω** in parallel, across **{fmt(V)} V**. What current flows through the **{r2} Ω** resistor?",
              "find I total, then p.d. across the parallel part, then I = V ÷ R", [f"R = {r1} + {fmt(par(r2, r3))} = {fmt(R)} Ω; I = {fmt(I)} A", f"p.d. across parallel part = {fmt(I)} × {fmt(par(r2, r3))} = {fmt(Vp)} V", f"I₂ = {fmt(Vp)} ÷ {r2} = **{fmt(I2)} A**"],
              ["Find the total current.", "Find the p.d. across the parallel pair.", "I = V ÷ R for that branch."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]]))


@template("c15x_pd_series_part", chapter=15, level=4, lo="15g")
def pd_series_part(rng):
    V = nice(rng, 9.0, 12.0)
    r1 = nice(rng, 3, 4, 6)
    r2, r3 = rng.choice([(6, 3), (12, 6), (6, 6), (4, 4)])
    R = r1 + par(r2, r3)
    I = V / R
    V1 = I * r1
    return mk(rng, V1, [(V - V1, "That is the p.d. across the PARALLEL part."), (V / 2, "The p.d. divides in the ratio of the resistances."), (V * r1 / (r1 + r2 + r3), "Combine the parallel pair first.")],
              "V", f"In Fig. 1, **{r1} Ω** is in series with **{r2} Ω** and **{r3} Ω** in parallel, across **{fmt(V)} V**. What is the p.d. across the **{r1} Ω** resistor?",
              "I = V ÷ R_total; V₁ = I R₁", [f"R = {r1} + {fmt(par(r2, r3))} = {fmt(R)} Ω", f"I = {fmt(I)} A; V₁ = {fmt(I)} × {r1} = **{fmt(V1)} V**"],
              ["Find the total current.", "Use V = I R for the series resistor.", "Check: the rest is across the pair."], figure=figs3.circuit(emf=f"{fmt(V)} V", top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]]))


@template("c15x_ldr_divider_output", chapter=15, level=4, lo="15j")
def ldr_divider_output(rng):
    V = 6.0
    Rf = nice(rng, 2, 5, 10)
    cond, Rl = rng.choice([("bright", 1), ("dim", 10), ("dark", 50)])
    Vout = V * Rl / (Rl + Rf)
    return mk(rng, Vout, [(V * Rf / (Rl + Rf), "The output is across the LDR, not the fixed resistor."), (V / 2, "The output depends on the ratio of resistances."), (V * Rl / Rf, "Divide by the TOTAL resistance.")],
              "V", f"An LDR and a fixed **{Rf} kΩ** resistor form a potential divider across **6.0 V**, with the output taken across the LDR.\n\n{md_table(['light level', 'LDR resistance / kΩ'], [['bright', 1], ['dim', 10], ['dark', 50]])}\n\nWhat is the output p.d. when it is **{cond}**?",
              "V_out = V × R_LDR ÷ (R_LDR + R_fixed)", [f"V_out = 6.0 × {Rl} ÷ ({Rl} + {Rf}) = **{fmt(Vout)} V**"],
              ["Find the LDR resistance.", "The output is across the LDR.", "Use the divider formula."])


@template("c15x_thermistor_divider_temp", chapter=15, level=4, lo="15j")
def thermistor_divider_temp(rng):
    V = 9.0
    Rf = nice(rng, 3, 6)
    T, Rt = rng.choice([(10, 12), (25, 6), (50, 3)])
    Vout = V * Rf / (Rt + Rf)
    return mk(rng, Vout, [(V * Rt / (Rt + Rf), "The output is across the FIXED resistor."), (V / 2, "Use the ratio of resistances."), (V * Rf / Rt, "Divide by the total resistance.")],
              "V", f"A thermistor (top) and a fixed **{Rf} kΩ** resistor (bottom) form a potential divider across **9.0 V** (Fig. 1). The output is across the fixed resistor.\n\n{md_table(['temperature / °C', 'thermistor resistance / kΩ'], [[10, 12], [25, 6], [50, 3]])}\n\nWhat is the output at **{T} °C**?",
              "V_out = V × R_fixed ÷ (R_therm + R_fixed)", [f"V_out = 9.0 × {Rf} ÷ ({Rt} + {Rf}) = **{fmt(Vout)} V**"],
              ["Find the thermistor's resistance.", "The output is across the fixed resistor.", "Use the divider formula."], figure=figs3.potential_divider(vin="9.0 V", r1="thermistor", r2=f"{Rf} kΩ", top_kind="therm"))


@template("c15x_parallel_lamps_house", chapter=15, level=4, lo="15e")
def parallel_lamps_house(rng):
    P = nice(rng, 60, 100)
    n = nice(rng, 3, 4, 5, 6)
    I_each = P / 230
    return mk(rng, n * I_each, [(I_each, "Add the currents of ALL the lamps (they are in parallel)."), (I_each / n, "Parallel currents add."), (n * P, "That is the total power, not current.")],
              "A", f"Identical lamps in a house are wired in parallel to the 230 V mains.\n\n{md_table(['quantity', 'value'], [['current in each lamp', f'{fmt(I_each, sf=3)} A'], ['number of lamps switched on', n]])}\n\nWhat is the total current from the mains?",
              "parallel: currents add", [f"I = {n} × {fmt(I_each, sf=3)} = **{fmt(n * I_each, sf=3)} A**"],
              ["Each lamp has the full 230 V.", "Each draws the same current.", "Add them."], sf=3)


@template("c15x_parallel_one_fails", chapter=15, level=4, lo="15e")
def parallel_one_fails(rng):
    V = nice(rng, 6.0, 12.0)
    R = nice(rng, 6, 12, 24)
    n = nice(rng, 3, 4)
    I_before = n * V / R
    I_after = (n - 1) * V / R
    return mk(rng, I_after, [(I_before, "One branch has broken: its current stops."), (0, "The other lamps stay lit in parallel."), (I_before / n, "That is the current in ONE lamp.")],
              "A", f"**{n}** identical lamps ({R} Ω each) are in parallel across **{fmt(V)} V**. One lamp's filament breaks.\n\n{md_table(['', 'current from supply / A'], [['before', fmt(I_before)], ['after', '?']])}\n\nWhat is the current from the supply now?",
              "parallel: other branches unaffected; total = sum of remaining branches", [f"each lamp: {fmt(V)} ÷ {R} = {fmt(V / R)} A", f"remaining {n - 1} lamps: **{fmt(I_after)} A**"],
              ["Does a broken branch affect the others?", "No, each has the full p.d.", "Add the remaining currents."])


@template("c15x_divider_range", chapter=15, level=4, lo="15h")
def divider_range(rng):
    V = nice(rng, 9.0, 12.0)
    r1 = nice(rng, 2, 4)
    lo, hi = 0, nice(rng, 4, 6, 8)
    vmax = V * hi / (r1 + hi)
    return mk(rng, vmax, [(V, "R₁ is still in the circuit, so the output cannot reach the full supply p.d."), (V * r1 / (r1 + hi), "That is the p.d. across R₁ at the maximum setting."), (V * hi / r1, "Divide by the TOTAL resistance.")],
              "V", f"A potential divider has a fixed resistor R₁ = **{r1} kΩ** at the top and a variable resistor R₂ (0 to {hi} kΩ) at the bottom, across **{fmt(V)} V**. The output is across R₂.\n\n{md_table(['R₂ setting', 'resistance / kΩ'], [['minimum', lo], ['maximum', hi]])}\n\nWhat is the MAXIMUM output p.d.?",
              "V_out = V × R₂ ÷ (R₁ + R₂) with R₂ at its maximum", [f"V_out = {fmt(V)} × {hi} ÷ ({r1} + {hi}) = **{fmt(vmax)} V** (minimum is 0 V)"],
              ["When is the output largest?", "When R₂ is largest.", "Use the divider formula."])


# ================================================================== L5
@template("c15x_parallel_to_target", chapter=15, level=5, lo="15f")
def parallel_to_target(rng):
    r1, r2 = rng.choice([(12, 6), (20, 30), (10, 40), (6, 3), (30, 60)])
    target = par(r1, r2)
    return mk(rng, r2, [(r1 - target, "Use reciprocals: 1/R₂ = 1/R_target − 1/R₁."), (target, "That is the target combined value."), (r1 * target, "Use 1/R₂ = 1/R − 1/R₁.")],
              "Ω", f"An engineer has a **{r1} Ω** resistor but needs a combined resistance of **{fmt(target)} Ω**.\n\n{md_table(['quantity', 'value'], [['resistor available', f'{r1} Ω'], ['combined resistance needed', f'{fmt(target)} Ω']])}\n\nWhat resistor must be connected in parallel with it?",
              "1/R₂ = 1/R − 1/R₁", [f"1/R₂ = 1/{fmt(target)} − 1/{r1} = {fmt(1 / r2, sf=3)}", f"R₂ = **{r2} Ω**"],
              ["A parallel resistor lowers the total.", "Subtract reciprocals.", "Invert."])


@template("c15x_series_or_parallel_choice", chapter=15, level=5, lo="15f")
def series_or_parallel_choice(rng):
    r = nice(rng, 10, 20, 30)
    target_kind = rng.choice(["series", "parallel"])
    target = 2 * r if target_kind == "series" else r / 2
    ans = "connect them in series" if target_kind == "series" else "connect them in parallel"
    wrongs = {("connect them in parallel" if target_kind == "series" else "connect them in series"): f"That gives {fmt(r / 2) if target_kind == 'series' else fmt(2 * r)} Ω.",
              "use only one of them": f"One alone gives {r} Ω.", "it cannot be done with two of them": "One of the two arrangements works."}
    return mkt(rng, ans, wrongs, f"A student has two identical **{r} Ω** resistors and needs a total of **{fmt(target)} Ω**.\n\n{md_table(['arrangement', 'total resistance'], [['series', '2R'], ['parallel', 'R ÷ 2']])}\n\nHow should the resistors be connected?",
               "series: 2R; parallel: R ÷ 2", [f"needed {fmt(target)} Ω = {'2R' if target_kind == 'series' else 'R ÷ 2'} → **{ans}**"],
               ["What does each arrangement give?", "Series adds; parallel halves.", "Match the target."])


@template("c15x_divider_load", chapter=15, level=5, lo="15h")
def divider_load(rng):
    V = 12.0
    R = nice(rng, 4, 6, 10)
    Rload = R
    Vout = V * par(R, Rload) / (R + par(R, Rload))
    return mk(rng, Vout, [(V / 2, "The load is in PARALLEL with the lower resistor, lowering its resistance."), (V * R / (R + R + Rload), "Combine the load and lower resistor in parallel."), (V / 4, "Use the divider formula with the combined resistance.")],
              "V", f"A potential divider of two **{R} kΩ** resistors is connected across **12.0 V**. A **{Rload} kΩ** load is then connected across the lower resistor.\n\n{md_table(['part', 'resistance / kΩ'], [['upper resistor', R], ['lower resistor', R], ['load (parallel with lower)', Rload]])}\n\nWhat is the new output p.d. across the lower resistor?",
              "lower ∥ load, then divider", [f"lower ∥ load = {fmt(par(R, Rload))} kΩ", f"V_out = 12.0 × {fmt(par(R, Rload))} ÷ ({R} + {fmt(par(R, Rload))}) = **{fmt(Vout)} V**"],
              ["The load is in parallel with the lower resistor.", "Find their combined resistance.", "Then use the divider rule."])


@template("c15x_potentiometer_slider", chapter=15, level=5, lo="15h")
def potentiometer_slider(rng):
    V = nice(rng, 6.0, 9.0, 12.0)
    frac = nice(rng, 0.25, 0.4, 0.6, 0.75)
    return mk(rng, V * frac, [(V * (1 - frac), "Measure from the end the output is taken to."), (V, "The slider takes only a fraction of the p.d."), (V * frac / 2, "The output is proportional to the fraction of the track.")],
              "V", f"A potentiometer (uniform resistance track) is connected across **{fmt(V)} V**. The output is taken between the bottom end and the slider.\n\n{md_table(['quantity', 'value'], [['fraction of track below the slider', f'{frac:g}']])}\n\nWhat is the output p.d.?",
              "uniform track: V_out = fraction × V", [f"V_out = {frac:g} × {fmt(V)} = **{fmt(V * frac)} V**"],
              ["A uniform track divides p.d. by length.", "What fraction is below the slider?", "Multiply."])


@template("c15x_network_total_power_current", chapter=15, level=5, lo="15f")
def network_total_power_current(rng):
    r = nice(rng, 6, 12)
    R = r + r / 2
    return mk(rng, R, [(3 * r, "Only two of the three are in series; the pair is in parallel."), (r / 3, "Two are in parallel and one in series."), (2 * r, "Parallel pair = r ÷ 2.")],
              "Ω", f"Three identical **{r} Ω** resistors: two are connected in parallel, and this pair is connected in series with the third.\n\n{md_table(['part', 'resistance'], [['parallel pair', 'r ÷ 2'], ['series resistor', 'r']])}\n\nWhat is the total resistance?",
              "R = r + r ÷ 2", [f"R = {r} + {fmt(r / 2)} = **{fmt(R)} Ω**"],
              ["Find the parallel pair.", "Add the series one.", "Total."])


@template("c15x_combined_find_emf", chapter=15, level=5, lo="15g")
def combined_find_emf(rng):
    r1 = nice(rng, 4, 6)
    r2, r3 = rng.choice([(6, 3), (12, 6), (4, 4)])
    I = nice(rng, 0.5, 1.0, 1.5)
    V = I * (r1 + par(r2, r3))
    return mk(rng, V, [(I * r1, "Use the TOTAL resistance."), (I * (r1 + r2 + r3), "The pair is in parallel."), (I * par(r2, r3), "Include the series resistor.")],
              "V", f"In Fig. 1, **{r1} Ω** is in series with **{r2} Ω** and **{r3} Ω** in parallel. The ammeter in the main circuit reads **{fmt(I)} A**. What is the e.m.f. of the supply (no internal resistance)?",
              "V = I × R_total", [f"R = {r1} + {fmt(par(r2, r3))} = {fmt(r1 + par(r2, r3))} Ω", f"V = {fmt(I)} × {fmt(r1 + par(r2, r3))} = **{fmt(V)} V**"],
              ["Find the total resistance.", "V = I R.", "Multiply."], figure=figs3.circuit(emf="?", top=[("R", f"{r1} Ω")], branches=[[("R", f"{r2} Ω")], [("R", f"{r3} Ω")]], bottom=[("A", f"{fmt(I)} A")]))


@template("c15x_thermistor_switch_temp", chapter=15, level=5, lo="15j")
def thermistor_switch_temp(rng):
    V = 6.0
    Rf = nice(rng, 2, 4)
    Vtrig = 4.0
    Rt_needed = Rf * (V - Vtrig) / Vtrig
    rows = [(10, 8), (20, 4), (30, 2), (40, 1)]
    T = next(t for t, r in rows if abs(r - Rt_needed) < 1e-9) if any(abs(r - Rt_needed) < 1e-9 for t, r in rows) else None
    if T is None:
        Rf = 4
        Rt_needed = 2
        T = 30
    return mk(rng, T, [(T - 10, "Find the thermistor resistance that gives 4.0 V across the fixed resistor."), (T + 10, "Check the resistance needed."), (Rt_needed, "That is the resistance, not the temperature.")],
              "°C", f"A thermistor (top) and a fixed **{Rf} kΩ** resistor (bottom) form a divider across **6.0 V**. An alarm sounds when the p.d. across the fixed resistor reaches **4.0 V**.\n\n{md_table(['temperature / °C', 'thermistor resistance / kΩ'], rows)}\n\nAt what temperature does the alarm sound?",
              "V_fixed ÷ V_therm = R_fixed ÷ R_therm", [f"p.d. across thermistor = 6.0 − 4.0 = 2.0 V", f"R_therm = {Rf} × 2.0 ÷ 4.0 = {fmt(Rf * 0.5)} kΩ → **{T} °C**"],
              ["Find the p.d. across the thermistor.", "Use the ratio to find its resistance.", "Read the temperature from the table."], dp=0)


@template("c15x_ldr_resistance_from_output", chapter=15, level=5, lo="15i")
def ldr_resistance_from_output(rng):
    V = 9.0
    Rf = nice(rng, 3, 6)
    Vout = nice(rng, 3.0, 6.0)
    Rl = Rf * Vout / (V - Vout)
    return mk(rng, Rl, [(Rf * (V - Vout) / Vout, "The output is across the LDR: R_LDR ÷ R_fixed = V_out ÷ (V − V_out)."), (Rf, "The resistances are only equal if the p.d.s are equal."), (Rf * Vout / V, "Use the p.d. across the fixed resistor, V − V_out.")],
              "kΩ", f"An LDR and a **{Rf} kΩ** resistor are in series across **9.0 V**. The voltmeter across the LDR reads **{fmt(Vout)} V**.\n\n{md_table(['quantity', 'value'], [['supply', '9.0 V'], ['p.d. across LDR', f'{fmt(Vout)} V'], ['fixed resistor', f'{Rf} kΩ']])}\n\nWhat is the resistance of the LDR?",
              "series: V ∝ R → R_LDR = R_fixed × V_LDR ÷ V_fixed", [f"V_fixed = 9.0 − {fmt(Vout)} = {fmt(V - Vout)} V", f"R_LDR = {Rf} × {fmt(Vout)} ÷ {fmt(V - Vout)} = **{fmt(Rl)} kΩ**"],
              ["Find the p.d. across the fixed resistor.", "Same current: V ∝ R.", "Solve."])


@template("c15x_thermistor_current_change", chapter=15, level=5, lo="15i")
def thermistor_current_change(rng):
    V = 6.0
    Rf = 1.0
    R_cold, R_hot = nice(rng, 5, 7), nice(rng, 1, 2)
    I_cold = V / (R_cold + Rf)
    I_hot = V / (R_hot + Rf)
    return mk(rng, I_hot - I_cold, [(I_hot, "Find the INCREASE in current."), (I_cold, "That is the cold current."), (V / R_hot - V / R_cold, "Include the fixed resistor in each total.")],
              "mA", f"A thermistor is in series with a **1.0 kΩ** resistor across **6.0 V**. The thermistor is warmed.\n\n{md_table(['condition', 'thermistor resistance / kΩ'], [['cold', R_cold], ['warm', R_hot]])}\n\nBy how much does the current increase, in mA?",
              "I = V ÷ (R_th + R_f) in each case; subtract (kΩ → mA)", [f"cold: 6.0 ÷ {R_cold + Rf} = {fmt(I_cold)} mA; warm: 6.0 ÷ {R_hot + Rf} = {fmt(I_hot)} mA", f"increase = **{fmt(I_hot - I_cold)} mA**"],
              ["Find each total resistance.", "V ÷ kΩ gives mA.", "Subtract."])
