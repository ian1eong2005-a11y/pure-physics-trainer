"""Chapter 15 D.C. Circuits written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w15x_series_current_rule", 15, 1, "15b",
        stem="State how the current at different points in a series circuit compares.",
        points=[P("the current is the same at every point", ["same at every point", "same everywhere", "the same", "equal everywhere", "same at all points"])],
        model_answer="The current is the same at every point in a series circuit.",
        hints=["How many paths are there?", "Is current used up?", "Compare the readings."],
        keywords="same current everywhere",
        sample_pass=["The current is the same everywhere", "it is the same at all points in the circuit"],
        sample_fail=["The current is larger near the cell", "It decreases after each lamp"])

written("w15x_parallel_current_rule", 15, 1, "15d",
        stem="State the relationship between the current from the supply and the currents in the branches of a parallel circuit.",
        points=[P("the supply current equals the sum of the branch currents", ["sum", "add up", "adds up", "total of the branch", "i = i1 + i2"])],
        model_answer="The current from the supply equals the sum of the currents in the separate branches.",
        hints=["What happens at a junction?", "The current splits.", "How do the parts compare with the total?"],
        keywords="supply current = sum of branch currents",
        sample_pass=["The supply current is the sum of the branch currents", "the branch currents add up to the total current"],
        sample_fail=["The currents are all the same", "The supply current is smaller"])

written("w15x_symbols_name", 15, 1, "15a",
        stem="Name the components represented by these circuit symbols: (a) a rectangle with a diagonal arrow through it, (b) a circle with a cross inside it.",
        points=[P("(a) variable resistor (rheostat)", ["variable resistor", "rheostat"]),
                P("(b) lamp (filament lamp / bulb)", ["lamp", "bulb"])],
        model_answer="(a) A variable resistor (rheostat). (b) A filament lamp.",
        hints=["An arrow through a component means adjustable.", "A circle with a cross gives light.", "Name both."],
        keywords="variable resistor; lamp",
        sample_pass=["(a) variable resistor (b) lamp", "a rheostat and a bulb"],
        sample_fail=["a fuse and a switch", "a cell and a diode"])

written("w15x_symbol_draw_describe", 15, 1, "15a",
        stem="Describe the circuit symbol for (a) a fixed resistor and (b) a thermistor.",
        points=[P("(a) a rectangle (oblong) in the line", ["rectangle", "oblong", "box"]),
                P("(b) a rectangle with a bent line (hockey-stick) through it", ["bent line", "hockey", "diagonal line with a bend", "line through it"])],
        model_answer="(a) A fixed resistor is a small rectangle in the circuit line. (b) A thermistor is a rectangle with a line through it that is bent at the end (like a hockey stick).",
        hints=["A resistor is a simple shape.", "A thermistor is a resistor with an extra line.", "Describe both."],
        keywords="rectangle; rectangle with bent line",
        sample_pass=["(a) a rectangle (b) a rectangle with a bent line through it", "a box, and a box with a hockey-stick line through it"],
        sample_fail=["a circle with a cross", "two parallel lines"])

written("w15x_series_pd_rule", 15, 1, "15c",
        stem="State the relationship between the e.m.f. of the supply and the p.d.s across the components in a series circuit.",
        points=[P("the p.d.s add up to the e.m.f.", ["add up", "sum", "adds up", "total", "e.m.f. = v1 + v2"])],
        model_answer="The p.d.s across the components add up to the e.m.f. of the supply.",
        hints=["How is the energy from the supply shared?", "Between the components.", "What do the p.d.s add to?"],
        keywords="sum of p.d.s = e.m.f.",
        sample_pass=["The p.d.s add up to the e.m.f.", "the sum of the voltages across the components equals the e.m.f."],
        sample_fail=["Each p.d. equals the e.m.f.", "The p.d.s are all zero"])

written("w15x_series_pd_calc_written", 15, 1, "15c",
        stem="A 12 V supply is connected to two resistors in series. The p.d. across one resistor is 5 V. State the p.d. across the other and explain.",
        points=[P("7 V", ["7"]),
                P("the p.d.s add up to the supply e.m.f. (12 − 5)", ["add up", "sum", "12 - 5", "12 − 5", "shared"])],
        model_answer="7 V, because in series the p.d.s across the components add up to the supply e.m.f.: 12 − 5 = 7 V.",
        hints=["In series, the p.d.s add up.", "To what?", "Subtract."],
        keywords="7 V; p.d.s add to e.m.f.",
        sample_pass=["7 V because the p.d.s add up to 12 V", "12 - 5 = 7 V"],
        sample_fail=["5 V", "17 V"])

written("w15x_parallel_pd_rule", 15, 1, "15e",
        stem="State how the p.d. across each branch of a parallel circuit compares with the p.d. of the supply.",
        points=[P("each branch has the same p.d. as the supply", ["same", "equal", "the same p.d.", "same as the supply"])],
        model_answer="The p.d. across each branch is the same as the supply p.d.",
        hints=["Each branch connects directly across the supply.", "Compare the p.d.s.", "Same."],
        keywords="same p.d. across each branch",
        sample_pass=["Each branch has the same p.d. as the supply", "the p.d. is equal across every branch"],
        sample_fail=["The p.d. is shared between branches", "Each branch has half the p.d."])

written("w15x_parallel_lamp_out", 15, 1, "15e",
        stem="Two lamps are connected in parallel to a cell. One lamp blows. State and explain what happens to the other lamp.",
        points=[P("the other lamp stays lit (same brightness)", ["stays lit", "stays on", "still lit", "same brightness", "keeps working", "still works"]),
                P("it is on a separate branch with its own complete path to the cell", ["separate branch", "own path", "own branch", "still complete", "parallel"])],
        model_answer="The other lamp stays lit at the same brightness, because it is on its own branch, which still forms a complete path to the cell with the full p.d.",
        hints=["Is the other branch affected?", "Does it still form a complete loop?", "What about its p.d.?"],
        keywords="stays lit; separate complete branch",
        sample_pass=["It stays lit because it is on a separate branch with its own complete path", "the other lamp still works since it has its own branch"],
        sample_fail=["It goes out", "It gets brighter"])

# ---------------------------------------------------------------- L2
written("w15x_series_resistance_rule", 15, 2, "15f",
        stem="State the formula for the combined resistance of resistors in series, and explain why it is larger than any single resistor.",
        points=[P("R = R₁ + R₂ + …", ["r1 + r2", "add", "sum", "added"]),
                P("the current must pass through every resistor in turn", ["every resistor", "each resistor", "all of them", "in turn", "one after another", "only one path"])],
        model_answer="R = R₁ + R₂ + R₃ + … (the resistances add). It is larger than any single resistor because the current must pass through every resistor in turn along the only path.",
        hints=["Do series resistances add?", "Why?", "The current goes through all of them."],
        keywords="R = R₁ + R₂; current passes through each",
        sample_pass=["R = R1 + R2, because the current must pass through every resistor", "add them, since there is only one path through all of them"],
        sample_fail=["1/R = 1/R1 + 1/R2", "Multiply them"])

written("w15x_ldr_written", 15, 2, "15i",
        stem="Describe how the resistance of an LDR changes from bright light to darkness, and suggest one use.",
        points=[P("resistance is low in bright light and high in darkness", ["low in bright", "high in dark", "increases in the dark", "increases as light decreases", "higher in the dark"]),
                P("use: automatic street lights / light sensor / burglar alarm", ["street light", "light sensor", "alarm", "automatic", "camera"])],
        model_answer="An LDR's resistance is low in bright light and increases greatly in darkness. It is used as a light sensor, for example to switch street lights on automatically at night.",
        hints=["Bright light: low or high?", "Darkness?", "Where is a light sensor useful?"],
        keywords="low in light, high in dark; street lights",
        sample_pass=["Its resistance is low in bright light and high in the dark; used in street lights", "resistance increases in the dark, used as a light sensor"],
        sample_fail=["Its resistance is high in bright light", "It measures temperature"])

written("w15x_series_ammeters_written", 15, 2, "15b",
        stem="A student places ammeters before and after a lamp in a series circuit and expects the second to read less. Explain what the readings will show.",
        points=[P("both ammeters read the same", ["same", "equal", "both read"]),
                P("charge is conserved / current is not used up; energy is converted in the lamp", ["conserved", "not used up", "energy", "same charge"])],
        model_answer="Both ammeters read the same, because charge is conserved: the current is not used up by the lamp. It is the energy carried by the charge that is converted in the lamp.",
        hints=["Is current used up?", "What is converted in the lamp?", "Compare the readings."],
        keywords="same readings; current not used up",
        sample_pass=["Both read the same because current is not used up, only energy is", "the readings are equal since charge is conserved"],
        sample_fail=["The second reads less", "The second reads zero"])

written("w15x_series_one_lamp_out", 15, 2, "15b",
        stem="Three lamps are connected in series. One lamp is unscrewed. State and explain what happens to the other two.",
        points=[P("the other two go out", ["go out", "goes out", "switch off", "stop working", "turn off"]),
                P("the circuit is broken, so there is no complete path and no current", ["broken", "no complete path", "no current", "open circuit", "incomplete"])],
        model_answer="The other two lamps go out, because removing one lamp breaks the only path: the circuit is incomplete, so no current flows.",
        hints=["How many paths are there?", "What does removing a lamp do?", "What happens to the current?"],
        keywords="others go out; circuit broken, no current",
        sample_pass=["They go out because the circuit is broken so no current flows", "the others switch off since there is no complete path"],
        sample_fail=["They get brighter", "Nothing happens"])

written("w15x_series_lamps_dimmer", 15, 2, "15c",
        stem="A second identical lamp is added in series with a lamp connected to a cell. Explain why both lamps are dimmer than the single lamp.",
        points=[P("the supply p.d. is shared between the two lamps (each gets half)", ["shared", "half", "split", "divided"]),
                P("so the current (and power) in each lamp is less", ["less current", "current is smaller", "current decreases", "less power", "less energy"])],
        model_answer="The supply p.d. is now shared between the two lamps, so each has only half the p.d. The total resistance has doubled, so the current is smaller and each lamp converts less energy per second.",
        hints=["How is the p.d. shared?", "What happens to the total resistance?", "And the current?"],
        keywords="p.d. shared; current smaller",
        sample_pass=["The p.d. is shared so each gets half, and the current is smaller", "the voltage is split between them and less current flows"],
        sample_fail=["The cell is weaker", "Each lamp gets double the p.d."])

written("w15x_series_pd_ratio_written", 15, 2, "15c",
        stem="Two resistors of 2 Ω and 6 Ω are in series with an 8 V supply. Explain how the p.d. is shared and calculate the p.d. across each.",
        points=[P("the p.d. divides in the ratio of the resistances (1 : 3)", ["ratio", "1 : 3", "proportion", "v = i r", "same current"]),
                P("2 V across the 2 Ω and 6 V across the 6 Ω", ["2 v", "6 v"])],
        model_answer="The same current flows through both, so the p.d. divides in the ratio of the resistances, 2 : 6 = 1 : 3. The 2 Ω resistor has 2 V and the 6 Ω resistor has 6 V (total 8 V).",
        hints=["Same current in series.", "V = I R.", "Share 8 V in the ratio 2 : 6."],
        keywords="ratio of resistances; 2 V and 6 V",
        sample_pass=["It divides in the ratio of the resistances: 2 V and 6 V", "same current so V = IR gives 2 V across 2 Ω and 6 V across 6 Ω"],
        sample_fail=["4 V each", "8 V each"])

written("w15x_parallel_branch_currents", 15, 2, "15d",
        stem="Two resistors of different values are connected in parallel. Explain which resistor carries the larger current.",
        points=[P("the smaller resistor carries the larger current", ["smaller resistor", "smaller resistance", "lower resistance"]),
                P("both have the same p.d., and I = V ÷ R", ["same p.d.", "same voltage", "i = v / r", "v / r"])],
        model_answer="The smaller resistor carries the larger current: both have the same p.d. across them, and I = V ÷ R, so a smaller R gives a larger I.",
        hints=["What is the same for both?", "I = V ÷ R.", "Which R gives the larger I?"],
        keywords="smaller R → larger I; same p.d.",
        sample_pass=["The smaller resistor, because both have the same p.d. and I = V / R", "the lower resistance carries more current with the same voltage"],
        sample_fail=["The larger resistor", "They carry the same current"])

written("w15x_parallel_ammeter_main", 15, 2, "15d",
        stem="In a parallel circuit, an ammeter in one branch reads 0.4 A and in the other 0.6 A. State the reading on an ammeter next to the cell and explain.",
        points=[P("1.0 A", ["1.0", "1 a"]),
                P("the branch currents add up to the current from the cell (charge conserved)", ["add", "sum", "conserved", "0.4 + 0.6"])],
        model_answer="1.0 A, because the branch currents add up to the current from the cell: 0.4 + 0.6 = 1.0 A (charge is conserved at the junctions).",
        hints=["What happens at the junctions?", "The current splits and rejoins.", "Add."],
        keywords="1.0 A; branch currents add",
        sample_pass=["1.0 A because the branch currents add up", "0.4 + 0.6 = 1.0 A"],
        sample_fail=["0.5 A", "0.2 A"])

# ---------------------------------------------------------------- L3
written("w15x_parallel_lower_r_l3", 15, 3, "15f",
        stem="Explain why adding a resistor in parallel with another decreases the total resistance of the circuit.",
        points=[P("it provides an extra path for the current", ["extra path", "another path", "more paths", "additional path"]),
                P("so more current flows for the same p.d. (total current increases)", ["more current", "current increases", "larger current", "total current"])],
        model_answer="The extra resistor provides another path for the current. For the same p.d., more total current flows, so the combined resistance (V ÷ I) is smaller.",
        hints=["What does a parallel resistor add?", "A path.", "What happens to the current?"],
        keywords="extra path; more current for same p.d.",
        sample_pass=["It provides an extra path so more current flows, lowering the resistance", "another path means the total current increases for the same voltage"],
        sample_fail=["It makes the wire thicker", "Parallel resistors add up"])

written("w15x_parallel_formula", 15, 3, "15f",
        stem="State the formula for the combined resistance R of two resistors R₁ and R₂ in parallel, and calculate R for 6 Ω and 3 Ω.",
        points=[P("1/R = 1/R₁ + 1/R₂ (or R = R₁R₂ ÷ (R₁ + R₂))", ["1/r", "1 / r", "reciprocal", "product over sum", "r1 r2"]),
                P("R = 2 Ω", ["2 ω", "2 ohm", "= 2", "2.0"])],
        model_answer="1/R = 1/R₁ + 1/R₂. For 6 Ω and 3 Ω: 1/R = 1/6 + 1/3 = 1/2, so R = 2 Ω.",
        hints=["Use reciprocals.", "Add 1/6 and 1/3.", "Invert."],
        keywords="1/R = 1/R₁ + 1/R₂; 2 Ω",
        sample_pass=["1/R = 1/R1 + 1/R2, so R = 2 ohm", "using product over sum, 18 ÷ 9 = 2.0 Ω"],
        sample_fail=["R = 9 Ω", "R = 4.5 Ω"])

written("w15x_ldr_divider_explain", 15, 3, "15i",
        stem="An LDR is in series with a fixed resistor across a supply. Explain what happens to the current in the circuit when it gets dark.",
        points=[P("the LDR's resistance increases in the dark", ["resistance increases", "higher resistance", "resistance rises"]),
                P("the total resistance increases, so the current decreases", ["current decreases", "less current", "current falls", "smaller current"])],
        model_answer="In the dark the LDR's resistance increases, so the total resistance of the circuit increases and the current decreases (I = V ÷ R).",
        hints=["How does the LDR change in the dark?", "What happens to the total resistance?", "And the current?"],
        keywords="LDR R rises; current falls",
        sample_pass=["The LDR's resistance increases so the current decreases", "higher resistance in the dark gives less current"],
        sample_fail=["The current increases", "Nothing changes"])

written("w15x_thermistor_current_explain", 15, 3, "15i",
        stem="A thermistor is in series with a lamp and a cell. Explain what happens to the brightness of the lamp as the thermistor is warmed.",
        points=[P("the thermistor's resistance decreases as it warms", ["resistance decreases", "resistance falls", "lower resistance"]),
                P("so the current increases and the lamp gets brighter", ["current increases", "brighter", "more current"])],
        model_answer="As the thermistor warms, its resistance decreases, so the total resistance falls and the current increases: the lamp gets brighter.",
        hints=["How does a thermistor change when warm?", "What happens to the current?", "And to the lamp?"],
        keywords="thermistor R falls; current rises; lamp brighter",
        sample_pass=["The thermistor's resistance decreases, so more current flows and the lamp is brighter", "lower resistance when warm, the current increases"],
        sample_fail=["The lamp gets dimmer", "The thermistor gives out light"])

written("w15x_combined_method", 15, 3, "15g",
        stem="Describe how to calculate the current from the supply in a circuit where a resistor is in series with two resistors in parallel.",
        points=[P("find the combined resistance of the parallel pair", ["parallel pair", "combined resistance", "1/r", "product over sum"]),
                P("add the series resistor to get the total resistance", ["add the series", "total resistance", "add"]),
                P("current = supply p.d. ÷ total resistance", ["i = v / r", "v / r", "divide", "p.d. ÷"])],
        min_points=2,
        model_answer="First find the combined resistance of the parallel pair (1/R = 1/R₁ + 1/R₂). Add the series resistor to get the total resistance. Then the current from the supply = supply p.d. ÷ total resistance.",
        hints=["Simplify the parallel part first.", "Then add the series resistor.", "Then I = V ÷ R."],
        keywords="parallel pair → add series → I = V ÷ R",
        sample_pass=["Find the combined resistance of the parallel pair, add the series resistor, then I = V / R", "combine the parallel pair, get the total resistance, divide the p.d. by it"],
        sample_fail=["Add all three resistances", "Multiply the resistances"])

written("w15x_combined_pd_share", 15, 3, "15g",
        stem="In a circuit, a 4 Ω resistor is in series with two 4 Ω resistors in parallel across 6 V. Explain which part has the larger p.d. across it.",
        points=[P("the parallel pair has a combined resistance of 2 Ω", ["2 ω", "2 ohm", "combined resistance of 2", "2.0"]),
                P("the series 4 Ω resistor has the larger p.d. (4 V vs 2 V)", ["4 v", "series resistor", "larger p.d.", "4 ω resistor"])],
        model_answer="The parallel pair has a combined resistance of 2 Ω, less than the 4 Ω series resistor. The same current flows through both parts, so the p.d. divides in the ratio 4 : 2: the series resistor has 4 V and the parallel pair 2 V.",
        hints=["Find the resistance of the parallel pair.", "Compare with 4 Ω.", "Share 6 V in that ratio."],
        keywords="pair = 2 Ω; series resistor has larger p.d.",
        sample_pass=["The parallel pair is 2 ohm, so the series 4 Ω resistor gets the larger p.d., 4 V", "4 V across the series resistor and 2 V across the pair"],
        sample_fail=["They have equal p.d.s", "The parallel pair has 6 V"])

written("w15x_lighting_circuit_house", 15, 3, "15e",
        stem="Explain two advantages of connecting the lamps in a house in parallel rather than in series.",
        points=[P("each lamp gets the full mains p.d. (works at full brightness)", ["full", "same p.d.", "230", "full brightness", "full voltage"]),
                P("each lamp can be switched on and off independently", ["independently", "separately", "own switch"]),
                P("if one lamp fails, the others keep working", ["others keep working", "others stay on", "still work", "one fails"])],
        min_points=2,
        model_answer="In parallel, each lamp has the full mains p.d., so it works at its proper brightness; each can be switched on and off independently; and if one lamp fails, the others keep working.",
        hints=["What p.d. does each lamp get?", "Can they be switched separately?", "What if one fails?"],
        keywords="full p.d.; independent switching; others keep working",
        sample_pass=["Each lamp gets the full p.d. and can be switched independently", "if one fails the others still work, and each has its own switch"],
        sample_fail=["It uses less wire", "The lamps share the voltage"])

written("w15x_divider_explain_l3", 15, 3, "15h",
        stem="Explain how two resistors in series can be used to obtain an output p.d. that is a fixed fraction of the supply.",
        points=[P("the same current flows through both resistors", ["same current"]),
                P("the supply p.d. is shared in the ratio of their resistances", ["ratio", "shared", "proportion", "divided"]),
                P("the output is taken across one resistor: V_out = V × R₂ ÷ (R₁ + R₂)", ["across one", "r2 / (r1 + r2)", "output", "v out"])],
        min_points=2,
        model_answer="The same current flows through both resistors, so the supply p.d. is shared between them in the ratio of their resistances. Taking the output across one resistor gives V_out = V × R₂ ÷ (R₁ + R₂), a fixed fraction of the supply.",
        hints=["What is the same through both?", "How is the p.d. shared?", "Where is the output taken?"],
        keywords="same current; p.d. shared in ratio; output across one resistor",
        sample_pass=["The same current flows so the p.d. is shared in the ratio of the resistances; the output is across one resistor", "the same current flows, so the voltage divides in proportion to the resistances and the output is across one of them"],
        sample_fail=["The resistors increase the voltage", "The current is different in each"])

# ---------------------------------------------------------------- L4
written("w15x_divider_change_r", 15, 4, "15h",
        stem="In a potential divider, the output is taken across R₂. Explain what happens to the output p.d. if R₂ is replaced by a larger resistor.",
        points=[P("the output p.d. increases", ["increases", "larger", "rises", "goes up"]),
                P("R₂ now takes a larger share of the supply p.d. (larger fraction of the total resistance)", ["larger share", "bigger share", "larger fraction", "bigger fraction", "ratio", "more of the p.d."])],
        model_answer="The output p.d. increases, because R₂ is now a larger fraction of the total resistance and so takes a larger share of the supply p.d. (V_out = V × R₂ ÷ (R₁ + R₂)).",
        hints=["How is the p.d. shared?", "In the ratio of resistances.", "What if R₂ grows?"],
        keywords="output increases; larger share",
        sample_pass=["The output increases because R2 takes a larger share of the p.d.", "it rises as R2 is a bigger fraction of the total resistance"],
        sample_fail=["The output decreases", "No change"])

written("w15x_divider_variable_output", 15, 4, "15h",
        stem="Explain how a potentiometer can provide a variable output p.d. from a fixed supply.",
        points=[P("a sliding contact moves along a resistance track connected across the supply", ["slider", "sliding contact", "track", "moves"]),
                P("the output is taken between one end and the slider", ["one end", "between", "slider"]),
                P("moving the slider changes the fraction of the track (resistance) and so the output", ["fraction", "changes", "varies", "from 0", "more of the track"])],
        min_points=2,
        model_answer="A potentiometer is a resistance track connected across the supply, with a sliding contact. The output is taken between one end and the slider; moving the slider changes the fraction of the track between them, so the output varies from 0 V up to the full supply p.d.",
        hints=["What is a potentiometer made of?", "Where is the output taken?", "What does moving the slider do?"],
        keywords="track across supply; output from end to slider; fraction changes",
        sample_pass=["A slider moves along a track across the supply; the output between one end and the slider changes as it moves", "moving the sliding contact changes the fraction of the track, varying the output from 0 V"],
        sample_fail=["It increases the supply voltage", "It changes the current only"])

written("w15x_parallel_pd_independent", 15, 4, "15e",
        stem="A 6 V battery is connected to two resistors in parallel, 3 Ω and 6 Ω. Explain why the p.d. across each is 6 V, and calculate the current in each.",
        points=[P("each branch is connected directly across the battery terminals", ["directly across", "across the battery", "same p.d.", "parallel"]),
                P("I = 2 A in the 3 Ω and 1 A in the 6 Ω", ["2 a", "1 a", "2.0", "1.0"])],
        model_answer="Each branch is connected directly across the battery terminals, so each has the full 6 V. The currents are 6 ÷ 3 = 2 A and 6 ÷ 6 = 1 A.",
        hints=["How are the branches connected?", "What p.d. does each get?", "I = V ÷ R."],
        keywords="directly across battery; 2 A and 1 A",
        sample_pass=["Each is connected directly across the battery so has 6 V; currents are 2 A and 1 A", "same p.d. in parallel, so 2.0 A and 1.0 A"],
        sample_fail=["3 V each", "1.5 A each"])

written("w15x_parallel_more_appliances", 15, 4, "15e",
        stem="Explain why the current drawn from the mains increases as more appliances are switched on in a house.",
        points=[P("the appliances are connected in parallel", ["parallel"]),
                P("each extra appliance adds another branch current to the total", ["adds", "another branch", "extra current", "sum", "add up"]),
                P("the total resistance decreases", ["total resistance decreases", "resistance falls", "lower total resistance"])],
        min_points=2,
        model_answer="Household appliances are connected in parallel. Each appliance switched on adds another branch with its own current, so the total current, the sum of the branch currents, increases (the total resistance decreases).",
        hints=["How are appliances connected?", "What does each add?", "What happens to the total?"],
        keywords="parallel; each adds a branch current; total R falls",
        sample_pass=["They are in parallel, so each appliance adds another branch current to the total", "more parallel branches means the currents add up and the total resistance falls"],
        sample_fail=["The voltage increases", "The appliances share the current"])

written("w15x_series_parallel_compare", 15, 4, "15f",
        stem="Two identical resistors are connected first in series and then in parallel across the same supply. Compare the total current in the two cases.",
        points=[P("series: total resistance 2R; parallel: R ÷ 2", ["2r", "r/2", "r ÷ 2", "double", "half", "quarter"]),
                P("the parallel current is four times the series current", ["four times", "4 times", "×4", "x4", "quadruple"])],
        model_answer="In series the total resistance is 2R; in parallel it is R ÷ 2, a quarter of the series value. So the current from the supply in parallel is four times the current in series.",
        hints=["Find R_total in each case.", "Compare them.", "I = V ÷ R."],
        keywords="2R vs R/2; parallel current 4×",
        sample_pass=["Series is 2R and parallel is R/2, so the parallel current is four times larger", "the parallel resistance is a quarter, giving 4 times the current"],
        sample_fail=["They are the same", "The series current is larger"])

written("w15x_parallel_add_effect", 15, 4, "15f",
        stem="A third resistor is added in parallel to two resistors already in parallel across a battery. State and explain the effect on the total resistance and on the current in the original resistors.",
        points=[P("the total resistance decreases", ["total resistance decreases", "decreases", "smaller total resistance", "falls"]),
                P("the current in each original resistor is unchanged (same p.d.)", ["unchanged", "stays the same", "same current", "same p.d."])],
        model_answer="The total resistance decreases, because there is an extra path. The current in each of the original resistors is unchanged, because each still has the full battery p.d. across it.",
        hints=["What does an extra parallel path do to R?", "Does the p.d. across the others change?", "So their current?"],
        keywords="total R falls; original branch currents unchanged",
        sample_pass=["The total resistance decreases but the current in the original resistors stays the same as they keep the same p.d.", "R falls; each original branch current is unchanged"],
        sample_fail=["The total resistance increases", "The original currents halve"])

written("w15x_series_pd_measure", 15, 4, "15c",
        stem="Describe how you would show experimentally that the p.d.s across two lamps in series add up to the supply e.m.f.",
        points=[P("connect a voltmeter across each lamp in turn (in parallel)", ["voltmeter across each", "voltmeter in parallel", "across each lamp", "across"]),
                P("connect a voltmeter across the supply", ["across the supply", "across the cell", "across the battery"]),
                P("add the lamp readings and compare with the supply reading", ["add", "compare", "sum", "equal"])],
        min_points=2,
        model_answer="Connect a voltmeter across each lamp in turn and then across the supply. Add the two lamp readings and compare with the supply reading; they should be equal.",
        hints=["How is a voltmeter connected?", "What readings are needed?", "How are they compared?"],
        keywords="voltmeter across each lamp and the supply; add and compare",
        sample_pass=["Put a voltmeter across each lamp and across the cell, then add the lamp readings and compare", "measure the p.d. across each lamp and the supply; the sum should equal the supply"],
        sample_fail=["Use an ammeter in series", "Measure the current only"])

written("w15x_series_unequal_lamps", 15, 4, "15c",
        stem="Two lamps with different resistances are connected in series. Explain which lamp has the larger p.d. across it.",
        points=[P("the lamp with the larger resistance has the larger p.d.", ["larger resistance", "higher resistance", "bigger resistance"]),
                P("the same current flows through both, and V = I R", ["same current", "v = i r", "v = ir"])],
        model_answer="The lamp with the larger resistance has the larger p.d., because the same current flows through both lamps and V = I R.",
        hints=["What is the same through both?", "V = I R.", "Which gets more p.d.?"],
        keywords="larger R → larger p.d.; same current",
        sample_pass=["The lamp with the larger resistance, because the same current flows and V = IR", "the higher resistance lamp has more p.d. since the current is the same"],
        sample_fail=["The smaller resistance lamp", "They have equal p.d."])

# ---------------------------------------------------------------- L5
written("w15x_eval_series_lamps_claim", 15, 5, "15c",
        stem="A student says: 'If I add more lamps in series to a battery, each lamp gets the full battery p.d.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("in series the battery's p.d. is shared between the lamps", ["shared", "divided", "split", "add up"]),
                P("so each lamp gets less p.d. and is dimmer (it is true in parallel)", ["less", "dimmer", "parallel"])],
        min_points=2,
        model_answer="The statement is wrong. In series the battery p.d. is shared between the lamps, so each lamp gets less p.d. and is dimmer. Each lamp would get the full p.d. only if connected in parallel.",
        hints=["How is p.d. shared in series?", "What does each lamp get?", "When would each get the full p.d.?"],
        keywords="wrong; p.d. shared; full p.d. only in parallel",
        sample_pass=["Wrong, in series the p.d. is shared so each lamp gets less and is dimmer; that is only true in parallel", "incorrect: the voltage is divided between the lamps"],
        sample_fail=["Correct, each lamp gets the full p.d.", "Correct, series lamps are brighter"])

written("w15x_eval_divider_design_light", 15, 5, "15j",
        stem="A designer wants a circuit whose output p.d. RISES when it gets dark. Using an LDR and a fixed resistor, explain where the output should be taken and why.",
        points=[P("take the output across the LDR", ["across the ldr"]),
                P("in the dark the LDR's resistance increases", ["resistance increases", "higher resistance", "resistance rises"]),
                P("so it takes a larger share of the supply p.d.", ["larger share", "bigger share", "more of the p.d.", "larger fraction"])],
        min_points=2,
        model_answer="The output should be taken across the LDR. In the dark the LDR's resistance increases, so it takes a larger share of the supply p.d., and the output rises.",
        hints=["How does the LDR change in the dark?", "Which component then gets more p.d.?", "Take the output there."],
        keywords="output across LDR; R rises in dark; larger share",
        sample_pass=["Across the LDR, because its resistance increases in the dark so it takes a larger share of the p.d.", "take it across the LDR; in darkness its resistance rises"],
        sample_fail=["Across the fixed resistor", "It does not matter"])

written("w15x_eval_divider_meter", 15, 5, "15h",
        stem="A student measures the output of a potential divider made of two 100 kΩ resistors across 10 V with a voltmeter of resistance 100 kΩ, and gets 3.3 V instead of 5 V. Explain this.",
        points=[P("the voltmeter is in parallel with the lower resistor", ["parallel", "across the lower"]),
                P("this lowers the combined resistance of that part (to 50 kΩ)", ["50", "lowers", "reduces", "combined resistance"]),
                P("so it takes a smaller share of the p.d. (10 × 50 ÷ 150 = 3.3 V)", ["smaller share", "less of the p.d.", "3.3", "ratio"])],
        min_points=2,
        model_answer="The voltmeter is in parallel with the lower resistor, so the combined resistance of that part falls to 50 kΩ. That part then takes a smaller share of the supply: 10 × 50 ÷ 150 = 3.3 V. A voltmeter with a much higher resistance should be used.",
        hints=["How is the voltmeter connected?", "What does that do to the resistance there?", "How does the share change?"],
        keywords="voltmeter in parallel lowers resistance; smaller share",
        sample_pass=["The voltmeter is in parallel with the lower resistor, lowering its resistance to 50 kΩ, so it gets a smaller share, 3.3 V", "it reduces the combined resistance, so less of the p.d. is across it"],
        sample_fail=["The battery is flat", "The voltmeter adds p.d."])

written("w15x_eval_divider_choice", 15, 5, "15h",
        stem="A student needs a 3 V output from a 12 V supply using a potential divider. Evaluate the choice of R₁ = 3 kΩ (top) and R₂ = 1 kΩ (output across R₂).",
        points=[P("the choice works", ["works", "correct", "gives 3", "3 v"]),
                P("V_out = 12 × 1 ÷ (3 + 1) = 3 V", ["12 × 1", "1 / 4", "ratio 1 : 3", "quarter", "3 v"])],
        model_answer="The choice works: the p.d. divides in the ratio 3 : 1, so V_out = 12 × 1 ÷ (3 + 1) = 3 V across R₂.",
        hints=["Use V_out = V × R₂ ÷ (R₁ + R₂).", "Substitute.", "Is it 3 V?"],
        keywords="works; 12 × 1 ÷ 4 = 3 V",
        sample_pass=["It works: V out = 12 × 1 / 4 = 3 V", "correct, R2 gets a quarter of 12 V, so 3 V"],
        sample_fail=["It gives 9 V", "It gives 4 V"])

written("w15x_eval_combined_claim", 15, 5, "15g",
        stem="A student says that in a circuit with a resistor in series with a parallel pair, the full supply p.d. is across the parallel pair. Evaluate this.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("the supply p.d. is shared between the series resistor and the parallel pair", ["shared", "divided", "split"]),
                P("the p.d. across the pair = supply − p.d. across the series resistor", ["supply minus", "subtract", "minus", "v - "])],
        min_points=2,
        model_answer="The statement is wrong. The series resistor and the parallel pair are in series, so the supply p.d. is shared between them; the p.d. across the pair equals the supply p.d. minus the p.d. across the series resistor.",
        hints=["Is the pair in series with the resistor?", "How is the p.d. shared?", "How do you find the pair's p.d.?"],
        keywords="wrong; p.d. shared; pair p.d. = supply − series p.d.",
        sample_pass=["Wrong, the p.d. is shared between the series resistor and the pair, so the pair gets the supply minus the series resistor's p.d.", "incorrect: the voltage is divided, subtract the series resistor's p.d."],
        sample_fail=["Correct, parallel parts always get the full p.d.", "Correct because of the junction"])

written("w15x_eval_combined_design", 15, 5, "15g",
        stem="A designer wants a total resistance of 8 Ω using a 6 Ω resistor and two other identical resistors. Evaluate using the two identical resistors as 4 Ω each in parallel, in series with the 6 Ω resistor.",
        points=[P("the parallel pair of 4 Ω gives 2 Ω", ["2 ω", "2 ohm", "gives 2", "2.0"]),
                P("total = 6 + 2 = 8 Ω, so the design works", ["8", "works", "correct"])],
        model_answer="Two 4 Ω resistors in parallel give 4 ÷ 2 = 2 Ω. In series with 6 Ω the total is 6 + 2 = 8 Ω, so the design works.",
        hints=["Find the parallel pair's resistance.", "Add the series resistor.", "Is it 8 Ω?"],
        keywords="4 ∥ 4 = 2 Ω; 6 + 2 = 8 Ω; works",
        sample_pass=["The pair gives 2 ohm, so the total is 6 + 2 = 8 Ω; it works", "4 and 4 in parallel is 2.0 Ω, plus 6 gives 8"],
        sample_fail=["Total is 14 Ω", "Total is 2 Ω"])

written("w15x_eval_thermistor_claim", 15, 5, "15i",
        stem="A student says: 'All resistors have a higher resistance when they get hotter.' Evaluate this statement.",
        points=[P("the statement is wrong / not always true", ["wrong", "not always", "incorrect", "not true"]),
                P("metal wires and filament lamps do increase in resistance when hot", ["metal", "filament", "wire", "increase"]),
                P("NTC thermistors decrease in resistance when hot", ["thermistor", "decrease", "falls", "lower"])],
        min_points=2,
        model_answer="The statement is not always true. Metal wires and filament lamps do have a higher resistance when hotter, but an NTC thermistor's resistance decreases as its temperature rises.",
        hints=["What happens to a metal wire?", "What happens to a thermistor?", "Is the statement always true?"],
        keywords="not always; metals increase; thermistors decrease",
        sample_pass=["Not always: metals increase in resistance when hot, but a thermistor's resistance decreases", "wrong, thermistors have lower resistance when hotter"],
        sample_fail=["Correct, all resistors behave the same", "Correct because atoms vibrate more"])

written("w15x_eval_ldr_claim", 15, 5, "15i",
        stem="A student says that an LDR in a dark box conducts better than in sunlight. Evaluate this statement and explain the behaviour of an LDR.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("in the dark an LDR has a very high resistance (conducts poorly)", ["high resistance", "conducts poorly", "resistance increases"]),
                P("light frees more charge carriers, lowering its resistance in sunlight", ["light", "charge carriers", "free electrons", "lower resistance", "decreases"])],
        min_points=2,
        model_answer="The statement is wrong. In the dark an LDR has a very high resistance, so it conducts poorly. Light releases more charge carriers in the material, so in sunlight its resistance is low and it conducts much better.",
        hints=["Dark: high or low resistance?", "What does light do?", "So when does it conduct better?"],
        keywords="wrong; high R in dark; light lowers R",
        sample_pass=["Wrong, in the dark it has a high resistance; light frees more charge carriers so it conducts better in sunlight", "incorrect: its resistance decreases in light"],
        sample_fail=["Correct, LDRs conduct in the dark", "LDRs do not depend on light"])

written("w15x_eval_heater_switch", 15, 5, "15j",
        stem="A greenhouse heater switches on when the input p.d. RISES above a set value. The circuit uses a thermistor and a fixed resistor. Evaluate which component the input should be taken across.",
        points=[P("across the thermistor", ["across the thermistor"]),
                P("when it gets colder, the thermistor's resistance increases", ["resistance increases", "colder", "higher resistance"]),
                P("so its share of the p.d. rises and the heater switches on", ["share", "rises", "switches on", "larger fraction"])],
        min_points=2,
        model_answer="The input should be taken across the thermistor. When the greenhouse gets colder, the thermistor's resistance increases, so it takes a larger share of the p.d.; the input rises above the set value and the heater switches on.",
        hints=["When should the heater switch on?", "What happens to the thermistor then?", "Which p.d. rises?"],
        keywords="across thermistor; colder → R up → share up → on",
        sample_pass=["Across the thermistor, because when it is colder its resistance increases and its share of the p.d. rises", "take the input across the thermistor: in the cold its resistance rises so the p.d. across it rises"],
        sample_fail=["Across the fixed resistor", "It does not matter"])
