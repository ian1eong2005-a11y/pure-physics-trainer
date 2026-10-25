"""Chapter 15 D.C. Circuits: written-answer questions, two per level (series and parallel rules, effective resistance,
LDRs and thermistors, potential dividers, household wiring in parallel, evaluating and designing)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w15_series_rules", 15, 1, "15b",
        stem="State two rules about current and potential difference in a series circuit.",
        points=[P("the current is the same at every point in the circuit", ["current is the same", "same current", "current same", "same at every point", "same everywhere", "current does not change"]),
                P("the sum of the p.d.s across the components equals the p.d. across the whole circuit (the e.m.f. of the supply)", ["sum of the p.d", "p.d.s add up", "pds add", "voltages add", "add up to the supply", "equals the supply", "total p.d.", "shared between", "sum of the voltages"])],
        pitfalls=[PF(["current is shared", "current splits", "current is used up"], "In a SERIES circuit the current is the same everywhere; it is the p.d. that is shared.")],
        model_answer="In a series circuit the current is the same at every point. The potential differences across the separate components add up to the potential difference across the whole circuit, which equals the e.m.f. of the supply.",
        hints=["One rule is about current: compare the current at different points.",
               "The other is about p.d.: how do the p.d.s across the components relate to the supply?",
               "State both rules."],
        keywords="same current everywhere; p.d.s add up to the supply p.d.",
        sample_pass=["The current is the same everywhere and the p.d.s across the components add up to the supply p.d.", "same current at every point; the voltages across the parts sum to the total voltage"],
        sample_fail=["The current is shared between the components and the p.d. is the same across each", "The current gets smaller after each component"])

written("w15_parallel_rules", 15, 1, "15d",
        stem="State two rules about current and potential difference in a parallel circuit.",
        points=[P("the p.d. across each branch is the same (equal to the p.d. across the whole parallel section / supply)", ["p.d. across each branch is the same", "same p.d.", "same voltage", "same potential difference", "p.d. is the same across", "voltage across each branch is the same", "equal p.d."]),
                P("the sum of the currents in the branches equals the current from the source (entering the junction)", ["sum of the currents", "currents add up", "currents add", "currents in the branches add", "equals the current from the source", "main current", "total current", "current splits", "current divides"])],
        pitfalls=[PF(["current is the same in each branch", "same current in every branch", "current is the same everywhere"], "In PARALLEL the branch currents can differ; it is the p.d. across each branch that is the same.")],
        model_answer="In a parallel circuit the potential difference across each branch is the same. The sum of the currents in the separate branches equals the current from the source, i.e. the current that enters a junction equals the current that leaves it.",
        hints=["One rule is about p.d.: compare the branches.",
               "The other is about current: what happens at the junctions?",
               "State both rules."],
        keywords="same p.d. across each branch; branch currents add up to the source current",
        sample_pass=["The p.d. across each branch is the same and the branch currents add up to the current from the battery", "each branch has the same voltage; the currents in the branches sum to the main current"],
        sample_fail=["The current is the same in each branch and the p.d. is shared", "The branch with more resistance gets more current"])

# ---------------------------------------------------------------- L2
written("w15_parallel_lower_resistance", 15, 2, "15f",
        stem="Two resistors are connected in parallel. Explain why their combined resistance is less than the resistance of either resistor on its own.",
        points=[P("connecting in parallel provides more paths (a greater total cross-section) for the current", ["more paths", "extra path", "another path", "more routes", "additional path", "more ways", "greater area", "wider"]),
                P("so for the same p.d. the total current is larger", ["total current is larger", "more current flows", "current increases", "greater current", "larger current", "current is bigger"]),
                P("since R = V ÷ I, a larger current for the same p.d. means a smaller resistance", ["r = v / i", "v divided by i", "resistance = v", "smaller resistance", "lower resistance", "less resistance", "resistance decreases"])],
        min_points=2,
        model_answer="Connecting a second resistor in parallel gives the current an additional path, so for the same p.d. across the combination the total current is larger than through either resistor alone. Since R = V ÷ I, a larger current for the same p.d. means a smaller effective resistance.",
        hints=["What does adding a parallel branch do to the number of routes the current can take?",
               "More routes means more total current for the same p.d. What does that do to V ÷ I?",
               "Link extra paths, larger current, smaller resistance."],
        keywords="extra path for current; larger total current for the same p.d.; R = V/I so resistance is smaller",
        sample_pass=["There is an extra path for the current so more current flows for the same p.d., and R = V/I gives a smaller resistance", "the current has more routes so the total current is bigger and the resistance lower"],
        sample_fail=["The resistors cancel each other out", "Electrons are shared so each resistor has less to do"])

written("w15_ldr_thermistor_behaviour", 15, 2, "15i",
        stem="Describe how the resistance of (a) a light-dependent resistor (LDR) and (b) an NTC thermistor changes with its surroundings.",
        points=[P("LDR: resistance decreases as the light intensity increases (high resistance in the dark)", ["decreases as the light", "falls as the light", "lower in bright", "less in the light", "high in the dark", "large in the dark", "decreases when brighter", "brighter the light the lower", "decreases brighter", "falls brighter", "ldr decreases light", "ldr falls light", "ldr lower light"]),
                P("NTC thermistor: resistance decreases as the temperature increases (high resistance when cold)", ["decreases as the temperature", "falls as the temperature", "lower when hot", "less when hot", "high when cold", "large when cold", "decreases when heated", "hotter the lower", "decreases hotter", "falls hotter", "decreases warmer", "thermistor decreases temperature", "thermistor falls temperature", "thermistor lower hot"])],
        pitfalls=[PF(["ldr resistance increases with light", "resistance increases as the light", "higher in bright light", "thermistor resistance increases with temperature", "increases as the temperature", "higher when hot"], "Both devices have resistance that DECREASES: the LDR as light increases, the NTC thermistor as temperature increases.")],
        model_answer="(a) The resistance of an LDR decreases as the light intensity increases: it is very high in the dark and low in bright light. (b) The resistance of an NTC thermistor decreases as its temperature increases: it is high when cold and low when hot.",
        hints=["For each device, name the quantity that affects it (light or temperature).",
               "Both resistances go DOWN as that quantity goes up.",
               "Describe both, stating the direction of change."],
        keywords="LDR: resistance falls as light increases; NTC thermistor: resistance falls as temperature increases",
        sample_pass=["LDR resistance decreases as the light gets brighter; thermistor resistance decreases as it gets hotter", "an LDR has high resistance in the dark and low in light, an NTC thermistor has high resistance when cold and low when hot"],
        sample_fail=["Both resistances increase with light and temperature", "An LDR measures temperature and a thermistor measures light"])

# ---------------------------------------------------------------- L3
written("w15_lamps_parallel_home", 15, 3, "15e",
        stem="Lamps in a house are connected in parallel rather than in series. Give two reasons why.",
        points=[P("each lamp receives the full mains p.d., so each works at its normal brightness", ["full p.d.", "full voltage", "same p.d.", "mains voltage", "230", "normal brightness", "full brightness", "same voltage"]),
                P("each lamp can be switched on and off independently of the others", ["independently", "separately", "own switch", "switch one off without", "without affecting", "individually"]),
                P("if one lamp fails (breaks), the others keep working", ["one lamp fails", "one breaks", "blows", "others still work", "others keep working", "rest still", "others stay on"])],
        min_points=2,
        model_answer="In parallel each lamp has the full mains p.d. across it, so every lamp is at its normal brightness. Each lamp can be switched on and off independently, and if one lamp fails the circuit through the others is unbroken, so they keep working.",
        hints=["Think about the p.d. across each lamp in parallel compared with in series.",
               "What happens to the other lamps when one is switched off or breaks?",
               "Give two advantages."],
        keywords="full p.d. across each lamp; independent switching; others keep working if one fails",
        figure=lambda: figs3.circuit(emf="230 V", branches=[[("lamp", "")], [("lamp", "")], [("lamp", "")]], branch_gap=0.9),
        sample_pass=["Each lamp gets the full voltage and can be switched independently", "if one lamp blows the others still work, and each has the full mains p.d. so it is at normal brightness"],
        sample_fail=["Parallel circuits use less electricity", "Series circuits would make the lamps too bright"])

written("w15_potential_divider_action", 15, 3, "15h",
        stem="Fig. 1 shows two resistors in series across a supply, with the output taken across the lower resistor. Explain how this arrangement acts as a potential divider, and state how the output p.d. changes if the lower resistance is increased.",
        points=[P("the same current flows through both resistors, and the supply p.d. is shared between them in the ratio of their resistances", ["shared", "divided", "split", "ratio of their resistances", "proportion", "same current"]),
                P("the output p.d. across R₂ is V × R₂ ÷ (R₁ + R₂)", ["r2 / (r1 + r2)", "r₂ ÷ (r₁ + r₂)", "fraction", "share of the supply", "v out =", "v_out", "output is the p.d. across"]),
                P("increasing the lower resistance gives it a larger share, so the output p.d. increases", ["output increases", "output rises", "larger share", "bigger share", "greater fraction", "output p.d. goes up", "output gets bigger"])],
        min_points=2,
        model_answer="The same current flows through the two resistors in series, so the supply p.d. is shared between them in the ratio of their resistances: the output across R₂ is V × R₂ ÷ (R₁ + R₂). If R₂ is increased it takes a larger share of the supply p.d., so the output p.d. increases.",
        hints=["Two resistors in series share the supply p.d. How is the share decided?",
               "Write the output as a fraction of the supply.",
               "If R₂ gets bigger, does its share get bigger or smaller?"],
        keywords="p.d. shared in ratio of resistances; V_out = V R₂/(R₁+R₂); larger R₂ gives larger output",
        figure=lambda: figs3.potential_divider(r1="R₁", r2="R₂"),
        sample_pass=["The supply p.d. is divided between the resistors in proportion to their resistances, the output is the share across R2, and increasing R2 increases the output",
                     "same current through both so the voltage splits in the ratio of the resistances; a bigger lower resistor takes a bigger share so the output rises"],
        sample_fail=["The output is always half the supply", "Increasing the lower resistance makes the output fall to zero"])

# ---------------------------------------------------------------- L4
written("w15_thermistor_sensor_explain", 15, 4, "15j",
        stem="Fig. 1 shows an NTC thermistor in series with a fixed resistor across a supply. The output is taken across the fixed resistor. Explain what happens to the output p.d. when the temperature of the thermistor rises.",
        points=[P("when the temperature rises the resistance of the NTC thermistor falls", ["resistance falls", "resistance decreases", "resistance drops", "lower resistance", "less resistance", "resistance of the thermistor decreases"]),
                P("the total resistance falls so the current in the circuit increases", ["current increases", "more current", "larger current", "current rises", "total resistance falls", "total resistance decreases"]),
                P("the p.d. across the fixed resistor (V = I R) increases, so the output p.d. rises (the thermistor's share falls)", ["output increases", "output rises", "output goes up", "output is higher", "output gets bigger", "output p.d. increases", "larger share", "smaller share", "p.d. across the fixed resistor increases", "voltage across the resistor rises", "across the resistor goes up", "v = ir", "thermistor's share falls"])],
        pitfalls=[PF(["resistance increases", "resistance rises", "resistance goes up", "output falls", "output decreases", "output drops"], "An NTC thermistor's resistance FALLS when it gets hotter, so the current rises and the output across the fixed resistor RISES.")],
        min_points=2,
        model_answer="When the temperature rises, the resistance of the NTC thermistor falls. The total resistance of the series circuit therefore falls and the current increases. The p.d. across the fixed resistor, V = IR, increases, so the output p.d. rises; the thermistor now takes a smaller share of the supply p.d.",
        hints=["What happens to the thermistor's resistance when it gets hotter?",
               "How does that change the current, and therefore the p.d. across the fixed resistor?",
               "Chain: resistance falls → current rises → output p.d. rises."],
        keywords="thermistor resistance falls; current increases; p.d. across fixed resistor (output) increases",
        figure=lambda: figs3.potential_divider(r1="thermistor", r2="R", top_kind="therm"),
        sample_pass=["The thermistor's resistance falls, so the current increases and the p.d. across the fixed resistor, which is the output, increases",
                     "hotter thermistor has lower resistance, it takes a smaller share of the supply, so the output across the resistor goes up"],
        sample_fail=["The thermistor's resistance increases so the output falls", "The output stays the same because the supply voltage is fixed"])

written("w15_ldr_streetlight_design", 15, 4, "15j",
        stem="A street lamp must switch on automatically when it gets dark. A potential divider containing an LDR and a fixed resistor provides the input to the switching circuit, which turns the lamp on when the input p.d. is high. Explain how the LDR and resistor should be arranged, and why.",
        points=[P("take the output across the LDR (LDR in the lower position), with the fixed resistor in series above it", ["output across the ldr", "across the ldr", "ldr at the bottom", "ldr in the lower", "p.d. across the ldr", "output taken from the ldr"]),
                P("in the dark the LDR's resistance becomes very high", ["resistance increases", "high resistance", "resistance rises", "very large resistance", "dark the resistance", "resistance goes up"]),
                P("so the LDR takes a larger share of the supply p.d. and the output rises, switching the lamp on; in daylight its resistance is low so the output is low", ["larger share", "bigger share", "output rises", "output increases", "high output", "switches the lamp on", "turns on", "low in daylight", "output is low"])],
        min_points=2,
        model_answer="Connect the fixed resistor and the LDR in series across the supply and take the output p.d. across the LDR. When it gets dark the resistance of the LDR rises steeply, so the LDR takes a larger share of the supply p.d. and the output rises, switching the lamp on. In daylight the LDR's resistance is low, its share of the p.d. is small, and the output is too low to switch the lamp on.",
        hints=["The lamp must come on when the output is HIGH in the dark. Which component should the output be taken across?",
               "What happens to the LDR's resistance in the dark, and to its share of the supply p.d.?",
               "Describe the arrangement and explain the output in the dark and in daylight."],
        keywords="output across the LDR; dark → LDR resistance high → larger share → output high → lamp on",
        figure=lambda: figs3.potential_divider(r1="R", r2="LDR", bottom_kind="LDR"),
        sample_pass=["Put the output across the LDR; in the dark its resistance rises so it takes a bigger share of the voltage and the output goes high, turning the lamp on",
                     "LDR at the bottom of the divider: high resistance in the dark gives a high output across it"],
        sample_fail=["Put the LDR in parallel with the lamp so it shorts it out in daylight", "The LDR produces electricity when light shines on it"])

# ---------------------------------------------------------------- L5
written("w15_claim_more_lamps_brighter", 15, 5, "15c",
        stem="A student connects one lamp to a cell and then adds a second identical lamp in series. She predicts that both lamps will be as bright as the first lamp was on its own. Evaluate her prediction.",
        points=[P("the prediction is wrong: both lamps will be dimmer", ["wrong", "incorrect", "dimmer", "less bright", "not as bright"]),
                P("in series the total resistance doubles, so the current (the same through both lamps) halves", ["resistance doubles", "total resistance increases", "more resistance", "current halves", "less current", "smaller current", "current decreases", "same current through both"]),
                P("the e.m.f. is shared, so each lamp has only half the p.d. across it (and so less power, P = VI)", ["half the p.d.", "shared", "half the voltage", "p.d. is split", "less p.d.", "half the emf", "less power"])],
        min_points=2,
        model_answer="Her prediction is wrong: both lamps will be dimmer than the single lamp was. Adding a second lamp in series doubles the total resistance, so the current, which is the same through both lamps, is halved. The e.m.f. of the cell is now shared between the two lamps, so each has only half the p.d. across it and transfers much less power.",
        hints=["What happens to the total resistance when a second lamp is added in series?",
               "How does that affect the current, and how is the cell's e.m.f. shared?",
               "Judge the prediction and explain using current and p.d."],
        keywords="dimmer; total resistance doubles so current halves; e.m.f. shared, half p.d. each",
        sample_pass=["She is wrong, both lamps are dimmer because the total resistance doubles, the current halves and each lamp only gets half the p.d.",
                     "incorrect: in series the voltage is shared and the current is smaller, so each lamp is dimmer"],
        sample_fail=["She is right because each lamp has its own current", "The second lamp will be brighter than the first"])

written("w15_design_divider_direction", 15, 5, "15j",
        stem="A greenhouse heater must switch on when the temperature falls below a set value. The control circuit switches the heater on when its input p.d. rises above 3 V. Design a potential divider using an NTC thermistor and a variable resistor to provide this input, explaining your choice of arrangement and the purpose of the variable resistor.",
        points=[P("thermistor in series with the variable resistor across the supply, output taken across the THERMISTOR", ["across the thermistor", "output across the thermistor", "thermistor at the bottom", "thermistor in the lower", "p.d. across the thermistor"]),
                P("when the temperature falls the thermistor's resistance rises, so it takes a larger share of the supply and the output rises above 3 V, switching the heater on", ["resistance rises", "resistance increases", "larger share", "bigger share", "output rises", "output increases", "above 3", "switches on", "turns on"]),
                P("the variable resistor sets the temperature at which the output reaches 3 V (adjusts the switching point)", ["set the temperature", "adjust the temperature", "switching point", "threshold", "change the point", "calibrate", "set the value", "adjust when it switches"])],
        min_points=2,
        model_answer="Connect the NTC thermistor and the variable resistor in series across the supply and take the output across the thermistor. When the temperature falls, the thermistor's resistance rises, so it takes a larger share of the supply p.d.; the output rises above 3 V and the heater switches on. When it is warm the thermistor's resistance is low and the output is below 3 V. The variable resistor is adjusted to set the temperature at which the output reaches 3 V, i.e. the switching temperature.",
        hints=["The output must be HIGH when it is COLD. Which component's resistance is high when cold, and which component should the output be taken across?",
               "Explain the output when cold and when warm.",
               "What can be changed by turning the variable resistor?"],
        keywords="output across the thermistor; cold → high resistance → large share → output > 3 V; variable resistor sets switching temperature",
        sample_pass=["Take the output across the thermistor; when cold its resistance is high so it gets a bigger share and the output goes above 3 V turning the heater on; the variable resistor adjusts the switching temperature",
                     "thermistor at the bottom of the divider so the output rises when cold; the variable resistor sets the threshold"],
        sample_fail=["Connect the thermistor directly to the heater so it heats up", "Use an LDR instead because greenhouses need light"])
