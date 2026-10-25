"""Chapter 14 Current of Electricity written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w14x_current_equation", 14, 1, "14a",
        stem="Write down the equation linking current, charge and time, and state the unit of each quantity.",
        points=[P("I = Q ÷ t (or Q = I t)", ["i = q / t", "q = i t", "q = it", "i = q/t", "current = charge / time", "charge / time"]),
                P("units: A, C, s", ["ampere", "coulomb", "second", "a, c", "amp"])],
        model_answer="I = Q ÷ t, where I is the current in amperes (A), Q is the charge in coulombs (C) and t is the time in seconds (s).",
        hints=["Current is the rate of flow of charge.", "Write it as an equation.", "Give units."],
        keywords="I = Q ÷ t; A, C, s",
        sample_pass=["I = Q / t, with current in amperes, charge in coulombs and time in seconds", "Q = I t: coulomb, ampere, second"],
        sample_fail=["V = I R", "Current = voltage × time"])

written("w14x_emf_meaning_l1", 14, 1, "14d",
        stem="A cell has an e.m.f. of 1.5 V. State what this means.",
        points=[P("1.5 J of energy is supplied (converted from chemical energy)", ["1.5 j", "1.5 joules", "energy"]),
                P("to each coulomb of charge driven round the circuit", ["per coulomb", "each coulomb", "for every coulomb", "per unit charge", "1 c"])],
        model_answer="The cell supplies 1.5 J of energy (converted from its chemical store) to each coulomb of charge it drives round a complete circuit.",
        hints=["e.m.f. is energy per unit charge.", "What does 1.5 V mean in J/C?", "Energy supplied by the cell."],
        keywords="1.5 J per coulomb supplied",
        sample_pass=["The cell gives 1.5 J of energy to each coulomb of charge", "1.5 joules of energy per coulomb driven round the circuit"],
        sample_fail=["The cell gives 1.5 A of current", "The cell has 1.5 Ω resistance"])

written("w14x_conventional_vs_electrons_l1", 14, 1, "14b",
        stem="On a circuit diagram, state the direction of conventional current and the direction in which electrons flow.",
        points=[P("conventional current: from positive to negative terminal (outside the cell)", ["current flows from positive", "current from positive", "current flows from the positive", "current from the positive"]),
                P("electrons: from negative to positive terminal", ["electrons flow from negative", "electrons from negative", "electrons flow from the negative", "electrons from the negative"])],
        model_answer="Conventional current flows from the positive terminal to the negative terminal around the circuit; electrons flow the opposite way, from the negative terminal to the positive terminal.",
        hints=["Which terminal does conventional current leave?", "Electrons are negative.", "Opposite directions."],
        keywords="conventional + → −; electrons − → +",
        sample_pass=["Conventional current flows from positive to negative and electrons from negative to positive", "conventional current flows from positive to negative; electrons flow from negative to positive"],
        sample_fail=["Both flow from positive to negative", "Electrons flow from positive to negative"])

written("w14x_electron_flow_reason", 14, 1, "14b",
        stem="Explain why electrons flow towards the positive terminal of a cell.",
        points=[P("electrons are negatively charged", ["negative", "negatively charged"]),
                P("they are attracted to the positive terminal (and repelled by the negative)", ["attracted to the positive", "attracted", "repelled by the negative", "unlike charges attract"])],
        model_answer="Electrons are negatively charged, so they are attracted towards the positive terminal (and repelled by the negative terminal).",
        hints=["What is the charge of an electron?", "What attracts it?", "Unlike charges attract."],
        keywords="electrons negative; attracted to +",
        sample_pass=["Electrons are negative so they are attracted to the positive terminal", "they are negatively charged and unlike charges attract"],
        sample_fail=["Electrons are positive", "The cell pushes protons"])

written("w14x_ohms_relation", 14, 1, "14h",
        stem="Write down the equation that defines resistance, and state its unit.",
        points=[P("R = V ÷ I", ["r = v / i", "r = v/i", "v = i r", "v = ir", "voltage / current", "p.d. / current"]),
                P("unit: ohm (Ω)", ["ohm", "ω", "v/a"])],
        model_answer="R = V ÷ I, the p.d. across the component divided by the current through it; unit: ohm (Ω).",
        hints=["Which two quantities?", "Which is on top?", "Name the unit."],
        keywords="R = V ÷ I; ohm",
        sample_pass=["R = V / I, measured in ohms", "resistance = p.d. / current, unit ohm"],
        sample_fail=["R = I ÷ V, in volts", "R = V × I"])

written("w14x_r_calc_l1", 14, 1, "14h",
        stem="A current of 0.5 A flows through a resistor when the p.d. across it is 6.0 V. Calculate the resistance, showing your working.",
        points=[P("R = V ÷ I = 6.0 ÷ 0.5", ["6.0 / 0.5", "6 / 0.5", "v / i", "6.0 ÷ 0.5"]),
                P("R = 12 Ω", ["12"])],
        model_answer="R = V ÷ I = 6.0 ÷ 0.5 = 12 Ω.",
        hints=["R = V ÷ I.", "Substitute.", "Unit Ω."],
        keywords="R = 6.0 ÷ 0.5 = 12 Ω",
        sample_pass=["R = 6.0 / 0.5 = 12 Ω", "v / i = 12 ohms"],
        sample_fail=["R = 3 Ω", "R = 0.08 Ω"])

written("w14x_cells_series_written", 14, 1, "14e",
        stem="Four 1.5 V cells are connected in series, all facing the same way. State the total e.m.f. and explain.",
        points=[P("6.0 V", ["6.0", "6 v"]),
                P("e.m.f.s of cells in series add up", ["add", "added", "sum", "4 × 1.5", "4 x 1.5"])],
        model_answer="The total e.m.f. is 6.0 V, because the e.m.f.s of cells connected in series (the same way round) add up: 4 × 1.5 V = 6.0 V.",
        hints=["What happens to e.m.f.s in series?", "They add.", "4 × 1.5."],
        keywords="6.0 V; e.m.f.s add",
        sample_pass=["6.0 V because the e.m.f.s add", "4 x 1.5 = 6 V"],
        sample_fail=["1.5 V", "0.375 V"])

written("w14x_cells_parallel_written", 14, 1, "14e",
        stem="Two identical 1.5 V cells are connected in parallel. State the combined e.m.f. and one advantage of this arrangement.",
        points=[P("1.5 V", ["1.5"]),
                P("the cells last longer (each supplies part of the current)", ["last longer", "longer", "share the current", "half the current", "more energy"])],
        model_answer="The combined e.m.f. is 1.5 V (the same as one cell); the advantage is that the cells last longer because each supplies only part of the current.",
        hints=["Do parallel e.m.f.s add?", "No, it stays the same.", "What is the benefit?"],
        keywords="1.5 V; last longer",
        sample_pass=["1.5 V, and the cells last longer", "same e.m.f. of 1.5 V but they share the current"],
        sample_fail=["3.0 V", "0.75 V"])

# ---------------------------------------------------------------- L2
written("w14x_why_two_conventions", 14, 2, "14b",
        stem="Explain why conventional current is in the opposite direction to the flow of electrons in a wire.",
        points=[P("conventional current was defined as positive charge flowing from + to −", ["positive charge", "defined", "convention", "agreed"]),
                P("before electrons (negative charge carriers) were discovered", ["before electrons", "discovered", "were not known"])],
        model_answer="Conventional current was defined as the flow of positive charge from + to − before it was discovered that the charge carriers in metals are negative electrons, which flow from − to +.",
        hints=["When was conventional current defined?", "What was not known then?", "Which way do electrons go?"],
        keywords="defined as positive flow before electrons discovered",
        sample_pass=["It was defined as positive charge flowing before electrons were discovered", "the convention was agreed before anyone knew electrons carry the current"],
        sample_fail=["Electrons are positive", "Current flows backwards at night"])

written("w14x_pd_meaning_l2", 14, 2, "14f",
        stem="The p.d. across a lamp is 3.0 V. State what this means.",
        points=[P("3.0 J of electrical energy is converted (to light and thermal energy)", ["3.0 j", "3 j", "3.0 joules", "3 joules", "joules", "energy"]),
                P("for each coulomb of charge passing through the lamp", ["per coulomb", "each coulomb", "for every coulomb", "per unit charge"])],
        model_answer="3.0 J of electrical energy is converted into light and thermal energy for each coulomb of charge that passes through the lamp.",
        hints=["p.d. = energy per unit charge.", "Where is the energy converted?", "In the lamp."],
        keywords="3.0 J per coulomb converted in the lamp",
        sample_pass=["3.0 J of energy is converted for each coulomb passing through the lamp", "3 joules per coulomb are changed to light and heat"],
        sample_fail=["3.0 A flows through it", "The lamp has 3 Ω resistance"])

written("w14x_charge_calc_l2", 14, 2, "14c",
        stem="A current of 0.20 A flows through a lamp for 5.0 minutes. Calculate the charge that passes, showing your working.",
        points=[P("t = 300 s", ["300"]),
                P("Q = I t = 0.20 × 300 = 60 C", ["60"])],
        model_answer="t = 5.0 × 60 = 300 s; Q = I t = 0.20 × 300 = 60 C.",
        hints=["Convert minutes to seconds.", "Q = I t.", "Multiply."],
        keywords="t = 300 s; Q = 60 C",
        sample_pass=["t = 300 s so Q = 0.2 × 300 = 60 C", "300 seconds, 60 coulombs"],
        sample_fail=["Q = 1.0 C", "Q = 1500 C"])

written("w14x_charge_vs_current", 14, 2, "14c",
        stem="Explain the difference between charge and current.",
        points=[P("charge is the quantity of electricity, measured in coulombs", ["coulomb", "quantity", "amount of charge"]),
                P("current is the rate of flow of charge (charge per second), in amperes", ["rate", "per second", "ampere", "flow of charge"])],
        model_answer="Charge is a quantity of electricity, measured in coulombs. Current is the rate of flow of charge, that is the charge passing a point per second, measured in amperes.",
        hints=["What is charge measured in?", "What is current?", "A rate."],
        keywords="charge: coulombs; current: rate of flow, amperes",
        sample_pass=["Charge is measured in coulombs; current is the rate of flow of charge in amperes", "current is the charge per second, charge is the amount in coulombs"],
        sample_fail=["They are the same thing", "Current is measured in volts"])

written("w14x_r_area_explain", 14, 2, "14i",
        stem="Explain why a thick wire has a lower resistance than a thin wire of the same material and length.",
        points=[P("a thick wire has a larger cross-sectional area", ["larger area", "bigger area", "larger cross-sectional", "more area"]),
                P("so there are more paths (more free electrons) for the charge to flow", ["more paths", "more electrons", "easier", "more room", "more space"])],
        model_answer="A thick wire has a larger cross-sectional area, so there are more paths (more free electrons) for the charge to flow through, and the resistance is lower (R ∝ 1/A).",
        hints=["What is different about a thick wire?", "Its area.", "How does that help the current?"],
        keywords="larger area; more paths for charge",
        sample_pass=["It has a larger cross-sectional area so there are more paths for the charge", "bigger area means more electrons can flow, so less resistance"],
        sample_fail=["A thick wire is longer", "Thick wires are hotter"])

written("w14x_r_length_explain", 14, 2, "14i",
        stem="Explain why a longer wire has a higher resistance than a shorter wire of the same material and thickness.",
        points=[P("the electrons have to travel further through the wire", ["further", "longer distance", "travel more"]),
                P("so they make more collisions with the metal ions", ["more collisions", "collide more", "more obstacles"])],
        model_answer="In a longer wire, the electrons have to travel further, so they make more collisions with the metal ions, giving a higher resistance (R ∝ L).",
        hints=["What do electrons collide with?", "How far do they travel in a long wire?", "More collisions."],
        keywords="travel further; more collisions",
        sample_pass=["The electrons travel further and make more collisions with the ions", "a longer distance means more collisions"],
        sample_fail=["Longer wires are thinner", "Long wires have fewer electrons"])

written("w14x_ohmic_graph_shape", 14, 2, "14k",
        stem="Describe the I-V graph of an ohmic conductor at constant temperature, and state what it shows.",
        points=[P("a straight line through the origin", ["straight line", "through the origin", "origin"]),
                P("current is directly proportional to p.d. / resistance is constant", ["directly proportional", "proportional", "constant resistance", "resistance is constant", "resistance stays the same"])],
        model_answer="It is a straight line through the origin, showing that the current is directly proportional to the p.d., so the resistance is constant.",
        hints=["What shape?", "Does it pass through the origin?", "What does it tell you about R?"],
        keywords="straight line through origin; I ∝ V; R constant",
        sample_pass=["A straight line through the origin showing current is proportional to p.d.", "straight line through the origin, so the resistance is constant"],
        sample_fail=["A curve", "A horizontal line"],
        figure=lambda: figs3.iv_graph("ohmic", R=4.0))

written("w14x_diode_graph_shape", 14, 2, "14k",
        stem="Describe the I-V characteristic of a semiconductor diode.",
        points=[P("no (almost no) current in the reverse direction", ["no current", "reverse", "zero current", "almost no current"]),
                P("current rises steeply once the forward p.d. exceeds about 0.6–0.7 V", ["0.6", "0.7", "rises steeply", "increases rapidly", "forward"])],
        model_answer="In the reverse direction almost no current flows. In the forward direction, very little current flows until the p.d. is about 0.6–0.7 V, after which the current rises steeply.",
        hints=["What happens in reverse?", "What happens forward?", "Is there a threshold?"],
        keywords="no reverse current; steep rise after ~0.7 V forward",
        sample_pass=["No current in reverse; in the forward direction the current rises steeply after about 0.7 V", "almost no current until 0.6 V forward, then it increases rapidly"],
        sample_fail=["A straight line through the origin", "Current is the same in both directions"],
        figure=lambda: figs3.iv_graph("diode", vmax=3.0))

# ---------------------------------------------------------------- L3
written("w14x_resistivity_meaning", 14, 3, "14i",
        stem="Write down the equation linking resistance, resistivity, length and area, and use it to explain why heating elements use nichrome rather than copper.",
        points=[P("R = ρ L ÷ A", ["ρ l / a", "rho l / a", "r = ρ", "resistivity × length", "resistivity x length"]),
                P("nichrome has a much higher resistivity than copper", ["higher resistivity", "high resistivity", "larger resistivity"]),
                P("so a reasonable length gives a high resistance, producing heating", ["high resistance", "heating", "heat", "large resistance"])],
        min_points=2,
        model_answer="R = ρ L ÷ A. Nichrome has a much higher resistivity than copper, so a practical length of nichrome wire has a high resistance and converts electrical energy to thermal energy effectively.",
        hints=["Write the resistivity equation.", "Compare ρ for nichrome and copper.", "Link to heating."],
        keywords="R = ρL/A; nichrome high ρ → high R → heating",
        sample_pass=["R = ρL/A; nichrome has a higher resistivity so it has a high resistance and heats up", "nichrome's high resistivity gives a large resistance for heating"],
        sample_fail=["Copper melts", "Nichrome is cheaper"])

written("w14x_filament_heat_written", 14, 3, "14j",
        stem="Explain, in terms of particles, why the resistance of a metal wire increases as its temperature rises.",
        points=[P("the metal ions (atoms) vibrate more", ["vibrate more", "vibrate faster", "larger vibrations", "vibrate with larger"]),
                P("so the free electrons collide with them more often", ["collide more", "more collisions", "collisions"])],
        model_answer="As the temperature rises, the metal ions vibrate more vigorously, so the free electrons collide with them more often, which makes it harder for the current to flow: the resistance increases.",
        hints=["What do the ions do when hotter?", "How does that affect electrons?", "Link to resistance."],
        keywords="ions vibrate more; more collisions",
        sample_pass=["The ions vibrate more, so the electrons collide with them more often", "larger vibrations of the atoms cause more collisions with free electrons"],
        sample_fail=["The electrons get bigger", "The wire gets shorter"])

written("w14x_lamp_curve_explain", 14, 3, "14k",
        stem="Fig. 1 shows the I-V graph of a filament lamp. Explain why the graph is a curve that becomes less steep at higher p.d.",
        points=[P("as the p.d. increases, the current heats the filament", ["heats", "hotter", "temperature rises", "gets hot"]),
                P("so the resistance of the filament increases", ["resistance increases", "higher resistance", "resistance rises"]),
                P("so the current increases less for each extra volt", ["less steep", "increases less", "smaller increase", "current rises more slowly"])],
        min_points=2,
        model_answer="As the p.d. increases, the larger current heats the filament. Its resistance increases with temperature, so each extra volt produces a smaller increase in current, and the graph becomes less steep.",
        hints=["What happens to the filament as V rises?", "How does its resistance change?", "How does that affect the slope?"],
        keywords="filament heats; resistance increases; less steep",
        sample_pass=["The filament heats up, its resistance increases, so the current rises less and the graph gets less steep", "the lamp gets hotter so its resistance rises"],
        sample_fail=["The lamp is a diode", "The resistance decreases"],
        figure=lambda: figs3.iv_graph("lamp", R=2.0))

written("w14x_diode_use", 14, 3, "14k",
        stem="State and explain one use of a diode in a circuit.",
        points=[P("allows current in one direction only", ["one direction", "only one way", "one way"]),
                P("e.g. protecting a circuit from a battery connected the wrong way / converting a.c. to d.c. (rectification)", ["protect", "wrong way", "rectif", "a.c. to d.c.", "ac to dc", "reverse"])],
        model_answer="A diode lets current flow in one direction only, so it can protect a circuit from damage if the battery is connected the wrong way round (or convert a.c. to d.c.).",
        hints=["What does a diode do to current?", "Where is that useful?", "Give one use."],
        keywords="one-way current; protection / rectification",
        sample_pass=["It only lets current flow one way, so it protects a circuit if the battery is put in the wrong way", "it allows current in one direction only, used to change ac to dc"],
        sample_fail=["It makes light", "It increases the voltage"])

written("w14x_emf_vs_pd_written", 14, 3, "14d",
        stem="Explain the difference between the e.m.f. of a cell and the p.d. across a resistor in the circuit.",
        points=[P("e.m.f. is the energy supplied per unit charge by the cell (source)", ["supplied", "source", "cell gives", "given to"]),
                P("p.d. is the energy converted per unit charge in the resistor (component)", ["converted", "used", "component", "resistor", "transferred"])],
        model_answer="The e.m.f. is the energy supplied by the cell to each coulomb of charge it drives round the circuit; the p.d. across the resistor is the energy converted from electrical to other forms for each coulomb passing through the resistor.",
        hints=["Where is energy given to the charge?", "Where is it converted?", "Both are per coulomb."],
        keywords="e.m.f.: energy supplied per C by source; p.d.: energy converted per C in component",
        sample_pass=["The e.m.f. is the energy supplied per coulomb by the cell; the p.d. is the energy converted per coulomb in the resistor", "e.m.f. is energy given to the charge by the source, p.d. is energy used in a component"],
        sample_fail=["They are the same", "e.m.f. is a force"])

written("w14x_emf_work_written", 14, 3, "14d",
        stem="A battery of e.m.f. 9.0 V drives 20 C of charge round a circuit. Calculate the energy it supplies and explain your method.",
        points=[P("W = e.m.f. × Q (energy per coulomb × number of coulombs)", ["9.0 × 20", "9 × 20", "9.0 x 20", "e.m.f. × q", "w = q v", "w = qv"]),
                P("W = 180 J", ["180"])],
        model_answer="The e.m.f. is the energy supplied per coulomb, so W = e.m.f. × Q = 9.0 × 20 = 180 J.",
        hints=["e.m.f. = energy per coulomb.", "Multiply by the number of coulombs.", "Calculate."],
        keywords="W = 9.0 × 20 = 180 J",
        sample_pass=["W = QV = 9.0 × 20 = 180 J", "9 x 20 = 180 J of energy"],
        sample_fail=["0.45 J", "29 J"])

written("w14x_pd_energy_written", 14, 3, "14f",
        stem="A charge of 15 C passes through a motor and 90 J of energy is converted. Calculate the p.d. across the motor, explaining what the answer means.",
        points=[P("V = W ÷ Q = 90 ÷ 15 = 6.0 V", ["6.0", "6 v", "90 / 15", "90 ÷ 15"]),
                P("6.0 J of energy is converted per coulomb", ["per coulomb", "each coulomb", "6 j", "6.0 j"])],
        model_answer="V = W ÷ Q = 90 ÷ 15 = 6.0 V, meaning 6.0 J of electrical energy is converted in the motor for each coulomb of charge.",
        hints=["p.d. = energy ÷ charge.", "Divide.", "Explain what 6 V means."],
        keywords="V = 90 ÷ 15 = 6.0 V; 6 J per C",
        sample_pass=["V = 90 / 15 = 6.0 V, so 6 J is converted per coulomb", "6 V: 6.0 J for each coulomb"],
        sample_fail=["1350 V", "0.17 V"])

written("w14x_pd_series_ammeter_voltmeter", 14, 3, "14f",
        stem="Describe how an ammeter and a voltmeter are connected to measure the current through and the p.d. across a resistor.",
        points=[P("the ammeter is connected in series with the resistor", ["ammeter in series", "ammeter is in series", "series"]),
                P("the voltmeter is connected in parallel (across) the resistor", ["voltmeter in parallel", "voltmeter across", "parallel", "across the resistor"])],
        model_answer="The ammeter is connected in series with the resistor so the same current passes through both; the voltmeter is connected in parallel, across the resistor.",
        hints=["Which meter measures what flows through?", "Which measures across?", "Series or parallel?"],
        keywords="ammeter series; voltmeter parallel",
        sample_pass=["Ammeter in series with the resistor and voltmeter in parallel across it", "the ammeter is in series; the voltmeter is across the resistor"],
        sample_fail=["Both in series", "Ammeter in parallel"])

# ---------------------------------------------------------------- L4
written("w14x_thermistor_explain", 14, 4, "14j",
        stem="Describe how the resistance of a thermistor changes with temperature, and suggest one use.",
        points=[P("its resistance decreases as temperature increases", ["decreases as temperature increases", "falls as temperature rises", "lower when hot", "decreases", "falls"]),
                P("use: temperature sensor / fire alarm / thermostat", ["sensor", "fire alarm", "thermostat", "thermometer", "temperature"])],
        pitfalls=[PF(["increases as temperature increases", "rises as temperature rises"], "A thermistor's resistance FALLS as it gets hotter.")],
        model_answer="As the temperature increases, the resistance of a thermistor decreases. It is used as a temperature sensor, for example in a fire alarm or thermostat.",
        hints=["How does R change when hotter?", "Opposite to a metal.", "Where is a temperature sensor useful?"],
        keywords="R falls as T rises; temperature sensor",
        sample_pass=["Its resistance decreases as the temperature increases; used in a fire alarm", "resistance falls when hot; used as a temperature sensor"],
        sample_fail=["Its resistance increases when hot", "It detects light"])

written("w14x_ldr_explain", 14, 4, "14j",
        stem="Describe how the resistance of an LDR changes with light intensity, and suggest one use.",
        points=[P("its resistance decreases as light intensity increases", ["decreases as light", "falls as light", "lower in bright", "decreases", "falls"]),
                P("use: automatic street lights / light sensor / camera exposure", ["street light", "light sensor", "automatic", "security light", "camera"])],
        pitfalls=[PF(["increases as light"], "An LDR's resistance FALLS in brighter light.")],
        model_answer="As the light intensity increases, the resistance of an LDR decreases. It is used as a light sensor, for example to switch street lights on automatically at dusk.",
        hints=["How does R change in bright light?", "It falls.", "Where would a light sensor help?"],
        keywords="R falls as light increases; light sensor",
        sample_pass=["Its resistance decreases as the light gets brighter; used in automatic street lights", "resistance falls in bright light; a light sensor"],
        sample_fail=["Its resistance increases in bright light", "It detects temperature"])

written("w14x_current_not_used", 14, 4, "14a",
        stem="A student thinks the current leaving a lamp is smaller than the current entering it. Explain why this is wrong and what is 'used up'.",
        points=[P("the current is the same everywhere in a series circuit (charge is conserved)", ["same", "conserved", "not used up", "equal"]),
                P("it is energy that is converted in the lamp (to light and heat)", ["energy", "converted", "transferred"])],
        model_answer="Charge is conserved, so the current (rate of flow of charge) is the same entering and leaving the lamp. What is 'used up' is energy: the electrical energy carried by the charge is converted into light and thermal energy in the lamp.",
        hints=["Is charge destroyed in the lamp?", "So what about the current?", "What does the lamp convert?"],
        keywords="current same (charge conserved); energy converted",
        sample_pass=["The current is the same because charge is conserved; it is energy that is converted in the lamp", "the charge is not used up, only its energy is transferred to light and heat"],
        sample_fail=["The lamp uses up some current", "The current doubles after the lamp"])

written("w14x_current_meter_explain", 14, 4, "14a",
        stem="Explain what an ammeter reading of 0.4 A means in terms of charge.",
        points=[P("0.4 C of charge passes a point", ["0.4 c", "0.4 coulomb", "0.4 coulombs"]),
                P("every second", ["each second", "per second", "every second", "in one second"])],
        model_answer="A current of 0.4 A means that 0.4 C of charge passes the ammeter (any point in that part of the circuit) every second.",
        hints=["1 A = 1 C/s.", "What is 0.4 A?", "Charge per second."],
        keywords="0.4 C per second",
        sample_pass=["0.4 C of charge passes the point every second", "0.4 coulombs per second"],
        sample_fail=["0.4 J per coulomb", "0.4 V across it"])

written("w14x_cells_design_torch", 14, 4, "14e",
        stem="A torch lamp needs 3.0 V and must work for a long time. Using 1.5 V cells, describe and explain a suitable arrangement.",
        points=[P("two cells in series to give 3.0 V", ["two in series", "2 in series", "series", "3.0 v"]),
                P("with further identical pairs in parallel to last longer", ["parallel", "last longer", "more pairs", "share the current"])],
        model_answer="Connect two 1.5 V cells in series to give 3.0 V. To make it last longer, connect another identical pair of series cells in parallel with the first pair; the e.m.f. stays 3.0 V but each pair supplies only part of the current.",
        hints=["How do you get 3.0 V from 1.5 V cells?", "How do you make them last longer?", "Combine series and parallel."],
        keywords="two in series → 3.0 V; pairs in parallel → longer life",
        sample_pass=["Two cells in series for 3.0 V, with another pair in parallel so they last longer", "put cells in series for 3 V and add parallel pairs to share the current"],
        sample_fail=["Four cells in series", "One cell only"])

written("w14x_cells_wrong_way", 14, 4, "14e",
        stem="A remote control needs four 1.5 V cells in series but does not work. One cell has been put in the wrong way round. Explain the effect on the e.m.f.",
        points=[P("the reversed cell opposes the others / subtracts its e.m.f.", ["opposes", "subtracts", "cancels", "reversed cell"]),
                P("total e.m.f. = 3.0 V instead of 6.0 V", ["3.0", "3 v", "half"])],
        model_answer="The reversed cell opposes the other three, so its e.m.f. subtracts instead of adding: the total is (3 − 1) × 1.5 = 3.0 V instead of 6.0 V, which is too low for the device.",
        hints=["What does a reversed cell do?", "It opposes.", "Calculate the new total."],
        keywords="reversed cell subtracts; 3.0 V not 6.0 V",
        sample_pass=["The reversed cell opposes the others so the e.m.f. is 3.0 V instead of 6.0 V", "it subtracts, giving only 3 V"],
        sample_fail=["It gives 4.5 V", "It gives 6.0 V"])

written("w14x_r_measure_method", 14, 4, "14h",
        stem="Describe how to measure the resistance of a resistor using an ammeter, a voltmeter and a variable resistor.",
        points=[P("ammeter in series and voltmeter in parallel with the resistor", ["ammeter in series", "voltmeter in parallel", "series", "parallel"]),
                P("take several readings of V and I, changing the variable resistor", ["several readings", "change the variable resistor", "different currents", "repeat", "vary"]),
                P("R = V ÷ I for each (or gradient of a V-I graph) and average", ["v / i", "v ÷ i", "average", "gradient", "graph"])],
        min_points=2,
        model_answer="Connect the ammeter in series and the voltmeter in parallel with the resistor. Use the variable resistor to take several pairs of V and I readings. Calculate R = V ÷ I for each and average, or plot V against I and find the gradient.",
        hints=["How are the meters connected?", "Why use a variable resistor?", "How is R found?"],
        keywords="meters connected correctly; several readings; R = V ÷ I averaged",
        sample_pass=["Ammeter in series, voltmeter in parallel; take several readings with the variable resistor and average V/I", "vary the current, record V and I, and find the gradient of the graph"],
        sample_fail=["Measure the length of the resistor", "Connect both meters in series"])

written("w14x_r_ohms_law_check", 14, 4, "14h",
        stem="Explain how you could use a table of V and I readings to check whether a component obeys Ohm's law.",
        points=[P("calculate V ÷ I for each reading", ["v / i", "v ÷ i", "calculate r", "resistance for each"]),
                P("if V ÷ I is constant (or I-V graph is a straight line through the origin), it obeys Ohm's law", ["constant", "straight line", "through the origin", "same value"])],
        min_points=1,
        model_answer="Calculate V ÷ I for each pair of readings. If the value is constant (or the I-V graph is a straight line through the origin), the current is proportional to the p.d. and the component obeys Ohm's law.",
        hints=["What does Ohm's law say about R?", "Constant.", "How can you check?"],
        keywords="V ÷ I constant / straight line through origin",
        sample_pass=["Work out V / I for each reading; if it is constant it obeys Ohm's law", "plot I against V; a straight line through the origin shows it is ohmic"],
        sample_fail=["Check the current is large", "Measure the temperature only"])

# ---------------------------------------------------------------- L5
written("w14x_eval_battery_claim", 14, 5, "14f",
        stem="A student says: 'A 12 V battery pushes 12 A through any lamp.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("12 V means 12 J per coulomb, not a current", ["12 j per coulomb", "energy per coulomb", "not a current", "per coulomb"]),
                P("the current depends on the resistance: I = V ÷ R", ["depends on the resistance", "i = v / r", "resistance"])],
        min_points=2,
        model_answer="The statement is wrong. 12 V means the battery transfers 12 J of energy per coulomb; it is not a current. The current depends on the resistance of the lamp: I = V ÷ R.",
        hints=["What does 12 V mean?", "Is volts the same as amperes?", "What decides the current?"],
        keywords="wrong; V = energy per C; I = V ÷ R",
        sample_pass=["Wrong, 12 V is energy per coulomb; the current depends on the resistance, I = V / R", "not true: the current depends on the lamp's resistance"],
        sample_fail=["Correct, volts equal amps", "Correct for all lamps"])

written("w14x_eval_wire_experiment", 14, 5, "14i",
        stem="A student investigates how the resistance of a wire depends on its length. Their results are inconsistent. Suggest two reasons and two improvements.",
        points=[P("the wire heated up, changing its resistance", ["heated", "temperature", "hot", "heating"]),
                P("poor contact / length measured inaccurately / kinks in the wire", ["contact", "length measured", "kinks", "crocodile clips", "inaccurate"]),
                P("improvement: use a small current / switch off between readings / repeat and average", ["small current", "switch off", "repeat", "average", "low current"])],
        min_points=2,
        model_answer="The wire may have heated up, which changes its resistance, and the length may have been measured inaccurately or the clips made poor contact. Use a small current and switch off between readings so the wire stays cool, measure the length carefully from clip to clip, and repeat and average.",
        hints=["What does a current do to a wire?", "What else could go wrong?", "How can each be fixed?"],
        keywords="heating; poor contact/length errors; small current, switch off, repeat",
        sample_pass=["The wire heated up and the length was measured badly; use a small current and repeat readings", "the temperature changed; switch off between readings and average"],
        sample_fail=["Use a thicker battery", "The wire was too clean"])

written("w14x_eval_thermistor_sensor", 14, 5, "14j",
        stem="An engineer must choose between a thermistor and a copper wire as a temperature sensor. Evaluate which is better.",
        points=[P("the thermistor is better", ["thermistor is better", "thermistor", "use the thermistor"]),
                P("its resistance changes much more for each degree of temperature change", ["changes much more", "large change", "more sensitive", "big change"]),
                P("a copper wire's resistance changes only slightly with temperature", ["only slightly", "small change", "changes little"])],
        min_points=2,
        model_answer="The thermistor is the better sensor: its resistance changes by a large amount for a small change in temperature (it is very sensitive), whereas the resistance of a copper wire changes only slightly.",
        hints=["How sensitive is each to temperature?", "Which gives a larger change?", "Choose."],
        keywords="thermistor; large change in R; copper changes little",
        sample_pass=["The thermistor, because its resistance changes much more with temperature than copper's", "thermistor: more sensitive, while copper changes only slightly"],
        sample_fail=["Copper, because it conducts better", "They are the same"])

written("w14x_eval_ldr_vs_thermistor", 14, 5, "14j",
        stem="A student uses a thermistor to make a light-operated switch for a garden lamp. Evaluate this choice.",
        points=[P("the choice is wrong / poor", ["wrong", "poor", "not suitable", "should use an ldr", "unsuitable"]),
                P("a thermistor responds to temperature, not light", ["temperature", "not light"]),
                P("an LDR should be used, as its resistance changes with light intensity", ["ldr", "light-dependent", "light dependent"])],
        min_points=2,
        model_answer="It is a poor choice: a thermistor's resistance depends on temperature, not light, so it would not switch the lamp at dusk reliably. An LDR should be used, because its resistance rises greatly as the light level falls.",
        hints=["What does a thermistor respond to?", "What is needed here?", "Which component should be used?"],
        keywords="wrong; thermistor senses temperature; use LDR",
        sample_pass=["Poor choice, a thermistor responds to temperature not light; an LDR should be used", "it should use an LDR because its resistance changes with light"],
        sample_fail=["Good choice, thermistors detect light", "Use a diode instead"])

written("w14x_eval_lamp_ohmic", 14, 5, "14k",
        stem="A student says that a filament lamp obeys Ohm's law because R = V ÷ I can be used to find its resistance. Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "does not obey", "not ohmic"]),
                P("R = V ÷ I defines resistance at any point, for any component", ["defines", "any component", "any point", "always"]),
                P("Ohm's law needs constant resistance (I ∝ V); a lamp's resistance rises as it heats", ["constant resistance", "proportional", "resistance increases", "rises", "heats"])],
        min_points=2,
        model_answer="The statement is wrong. R = V ÷ I defines the resistance at any point for any component. Ohm's law requires the resistance to stay constant (I ∝ V), but a filament lamp's resistance increases as it heats up, so it does not obey Ohm's law.",
        hints=["Is R = V ÷ I the same as Ohm's law?", "What does Ohm's law require?", "Does the lamp's R stay constant?"],
        keywords="wrong; R = V/I always defines R; Ohm's law needs constant R",
        sample_pass=["Wrong, R = V/I defines resistance for any component, but Ohm's law needs constant resistance and the lamp's resistance increases as it heats", "it does not obey Ohm's law because its resistance rises"],
        sample_fail=["Correct, all lamps are ohmic", "Correct because R = V / I"])

written("w14x_eval_diode_claim", 14, 5, "14k",
        stem="A student connects a diode in a circuit and the lamp does not light. They conclude the diode is broken. Evaluate this conclusion.",
        points=[P("the diode may simply be reverse-biased (connected the wrong way round)", ["reverse", "wrong way", "reverse-biased", "reverse biased"]),
                P("a diode only conducts in the forward direction", ["one direction", "forward", "one way"]),
                P("test: reverse the diode; if the lamp then lights, it is working", ["reverse the diode", "turn it round", "swap", "test"])],
        min_points=2,
        model_answer="The conclusion may be wrong. A diode only conducts in the forward direction, so it may simply be reverse-biased. Turning the diode round would test this: if the lamp then lights, the diode is working.",
        hints=["How does a diode conduct?", "Could it be the wrong way round?", "How could you test it?"],
        keywords="maybe reverse-biased; conducts one way; reverse to test",
        sample_pass=["It may be connected the wrong way round; a diode conducts one way only, so reverse it and see if the lamp lights", "it could be reverse-biased, so turn it round to test"],
        sample_fail=["The diode must be broken", "Diodes never conduct"])

written("w14x_eval_conventional_claim", 14, 5, "14b",
        stem="A student says that because electrons flow from − to +, conventional current is 'wrong' and should be abandoned. Evaluate this statement.",
        points=[P("conventional current is not wrong: it is an agreed convention", ["convention", "agreed", "not wrong"]),
                P("a flow of positive charge one way is equivalent to negative charge the other way", ["equivalent", "same effect", "opposite direction", "same current"]),
                P("all rules (e.g. circuit symbols, left-hand rule) are based on it, so it is kept", ["rules", "left-hand", "symbols", "diode", "kept", "consistent"])],
        min_points=2,
        model_answer="Conventional current is not wrong; it is an agreed convention. A flow of positive charge in one direction has the same effect as negative charge flowing the other way, and many rules (such as diode symbols and Fleming's left-hand rule) are based on it, so it is kept.",
        hints=["Is it a mistake or a convention?", "Do the two descriptions give the same effects?", "Why keep it?"],
        keywords="convention; equivalent; rules based on it",
        sample_pass=["It is an agreed convention, and positive charge one way is equivalent to negative charge the other way, so it is kept", "not wrong: the left-hand rule and diode symbols use it"],
        sample_fail=["Correct, it should be abandoned", "Electrons flow from + to −"])

written("w14x_eval_electron_speed", 14, 5, "14b",
        stem="A lamp lights the moment a switch is closed, yet electrons drift through wires at only about 1 mm/s. Explain this.",
        points=[P("the wires are already full of free electrons", ["already full", "already in the wire", "throughout the circuit", "everywhere"]),
                P("when the circuit is closed, an electric field is set up almost instantly and all electrons start moving at once", ["at once", "together", "instantly", "electric field", "simultaneously"])],
        model_answer="The wires are already full of free electrons throughout the circuit. When the switch is closed, an electric field is set up around the circuit almost instantly, so all the electrons, including those in the lamp, start to drift at the same time.",
        hints=["Are there electrons in the lamp already?", "What happens when the switch closes?", "Do they all move together?"],
        keywords="wires already full of electrons; all start moving at once",
        sample_pass=["The wires are already full of electrons and they all start moving at once when the field is set up", "electrons throughout the circuit move together instantly"],
        sample_fail=["Electrons travel at the speed of light", "The battery fires electrons very fast"])
