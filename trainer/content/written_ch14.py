"""Chapter 14 Current of Electricity: written-answer questions, two per level (current, e.m.f., p.d., conventional current,
resistance and its dependence on length, area and temperature; I-V graphs; evaluating claims; planning)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w14_define_current", 14, 1, "14a",
        stem="State what is meant by an electric current, and give its unit.",
        points=[P("the rate of flow of (electric) charge", ["rate of flow of charge", "charge flowing per second", "charge per unit time", "charge per second", "flow of charge per", "coulombs per second", "rate of flow of electrons"]),
                P("measured in amperes (A)", ["ampere", "amp", "amperes", "amps"])],
        pitfalls=[PF(["flow of voltage", "voltage flowing", "rate of flow of energy"], "Current is the rate of flow of CHARGE, not of voltage or energy.")],
        model_answer="An electric current is the rate of flow of electric charge, i.e. the charge passing a point per second. It is measured in amperes (A).",
        hints=["Current is a RATE: something per second. What is the something?",
               "Charge is measured in coulombs; current is coulombs per second.",
               "State the definition and the unit."],
        keywords="rate of flow of charge; ampere",
        sample_pass=["The rate of flow of charge, measured in amperes", "charge passing per second, measured in amps"],
        sample_fail=["The flow of voltage through a wire, measured in volts", "The energy carried by electrons, in joules"])

written("w14_define_emf", 14, 1, "14d",
        stem="Define the electromotive force (e.m.f.) of a source such as a cell, and state its unit.",
        points=[P("the work done (energy transferred) per unit charge by the source", ["work done per unit charge", "work done per coulomb", "energy per unit charge", "energy per coulomb", "work done by the source per", "joules per coulomb", "energy transferred per unit charge"]),
                P("in driving charge around a complete circuit", ["complete circuit", "round the circuit", "around the circuit", "whole circuit", "driving charge", "driving the charge"]),
                P("unit: volt (V)", ["volt", "volts", "unit v"])],
        min_points=2,
        model_answer="The e.m.f. of a source is the work done per unit charge by the source in driving charge around a complete circuit. Its unit is the volt (V).",
        hints=["E.m.f. is not a force. It is a certain amount of work per coulomb.",
               "Who does the work, and where is the charge driven?",
               "Work done per unit charge by the source, round a complete circuit; unit volt."],
        keywords="work done per unit charge by the source driving charge round a complete circuit; volt",
        sample_pass=["The work done per unit charge by the cell in driving charge around the complete circuit, in volts", "energy transferred per coulomb by the source round the whole circuit; unit V"],
        sample_fail=["The force that pushes electrons, measured in newtons", "The current supplied by the cell"])

# ---------------------------------------------------------------- L2
written("w14_define_pd", 14, 2, "14f",
        stem="State what is meant by the potential difference across a component, and explain how it differs from the e.m.f. of a cell.",
        points=[P("p.d. = work done per unit charge in driving charge through the component", ["work done per unit charge", "energy per unit charge", "work done per coulomb", "energy per coulomb", "joules per coulomb"]),
                P("p.d. refers to energy transferred by charge passing through a component; e.m.f. refers to energy supplied by the source to the charge (for the whole circuit)", ["through the component", "in the component", "source", "supplied by the cell", "whole circuit", "complete circuit", "given to the charge"])],
        model_answer="The potential difference across a component is the work done per unit charge in driving charge through that component (energy transferred per coulomb in the component). The e.m.f. of a cell is the work done per unit charge by the source in driving charge around the whole circuit: e.m.f. is energy given to the charge by the source, while p.d. is energy transferred by the charge in a component.",
        hints=["Both are measured in volts and both are 'per unit charge'. What differs is where the energy is going.",
               "E.m.f.: energy given to each coulomb by the source. P.d.: energy given up by each coulomb in a component.",
               "Define p.d., then contrast with e.m.f."],
        keywords="p.d.: work done per unit charge through the component; e.m.f.: work done per unit charge by the source round the whole circuit",
        sample_pass=["P.d. is the work done per coulomb driving charge through the component, whereas e.m.f. is the work done per coulomb by the source round the complete circuit",
                     "energy per unit charge transferred in the component; emf is energy per unit charge supplied by the cell"],
        sample_fail=["Potential difference is the current through the component", "They are the same thing with different names"])

written("w14_conventional_current", 14, 2, "14b",
        stem="Distinguish between conventional current and electron flow in a metal wire.",
        points=[P("conventional current is taken to flow from the positive terminal to the negative terminal", ["positive to negative", "positive terminal to the negative", "from positive", "+ to -", "+ to −"]),
                P("electrons (the actual charge carriers in a metal) flow from the negative terminal to the positive terminal, i.e. opposite to conventional current", ["negative to positive", "negative terminal to the positive", "from negative", "opposite direction", "opposite to the conventional", "- to +", "− to +"])],
        model_answer="Conventional current is taken to flow from the positive terminal of the supply, through the circuit, to the negative terminal. In a metal the charge carriers are electrons, which are negative, so electron flow is in the opposite direction: from the negative terminal to the positive terminal.",
        hints=["Which terminal does conventional current leave the cell from?",
               "Electrons are negatively charged. Which terminal attracts them?",
               "State both directions."],
        keywords="conventional: + to −; electrons: − to +",
        sample_pass=["Conventional current goes from positive to negative but electrons flow from negative to positive", "electron flow is from the negative terminal to the positive, opposite to the conventional current direction"],
        sample_fail=["They flow in the same direction", "Conventional current is faster than electron flow"])

# ---------------------------------------------------------------- L3
written("w14_resistance_length_area", 14, 3, "14i",
        stem="Fig. 1 shows a length of resistance wire. Explain how the resistance of a wire depends on its length and on its cross-sectional area.",
        points=[P("resistance is directly proportional to length: doubling the length doubles the resistance", ["proportional to length", "longer wire", "doubling the length doubles", "increases with length", "longer the wire the greater", "directly proportional to the length"]),
                P("resistance is inversely proportional to cross-sectional area: doubling the area halves the resistance (thicker wire, lower resistance)", ["inversely proportional to", "thicker", "larger area", "doubling the area halves", "decreases as the area", "greater the area the smaller", "halves the resistance"])],
        pitfalls=[PF(["directly proportional to the area", "directly proportional to area", "thicker wire has more resistance", "thicker wire more resistance", "larger area more resistance", "increases with area", "increases as the area", "does not depend on length", "does not depend on the length"], "A THICKER wire has LESS resistance (inversely proportional to the cross-sectional area), and a longer wire has MORE.")],
        model_answer="The resistance of a wire is directly proportional to its length: doubling the length doubles the resistance, because the electrons have twice as far to travel through the lattice. The resistance is inversely proportional to the cross-sectional area: doubling the area halves the resistance, because there are more paths for the electrons to flow along.",
        hints=["Think of the wire as a road for electrons: a longer road and a wider road.",
               "Longer: more resistance in proportion. Wider (larger area): less resistance in proportion.",
               "State both relationships with the words 'proportional' and 'inversely proportional'."],
        keywords="R ∝ length; R ∝ 1/area",
        figure=lambda: figs3.wire_sketch("length L", "area A"),
        sample_pass=["Resistance is proportional to the length and inversely proportional to the cross-sectional area", "a longer wire has more resistance in proportion, a thicker wire has less: doubling the area halves R"],
        sample_fail=["Resistance is proportional to the area and does not depend on length", "A thicker wire has more resistance because it has more metal"])

written("w14_filament_resistance_rises", 14, 3, "14j",
        stem="Fig. 1 shows the I-V graph of a filament lamp. Explain, in terms of the metal filament, why the resistance of the lamp increases as the p.d. increases.",
        points=[P("a larger current makes the filament hotter (higher temperature)", ["hotter", "temperature rises", "heats up", "higher temperature", "temperature increases", "gets hot"]),
                P("the metal ions / atoms vibrate more vigorously (with larger amplitude)", ["vibrate more", "vibrations increase", "ions vibrate", "atoms vibrate", "lattice vibrat", "vibrate faster", "vibrate with larger"]),
                P("so the free electrons collide with them more often, which opposes the flow of charge more: resistance increases", ["collide more", "more collisions", "collisions increase", "frequent collisions", "harder for electrons", "obstruct", "impede"])],
        min_points=2,
        model_answer="As the p.d. increases the current increases and the filament gets hotter. At a higher temperature the metal ions vibrate more vigorously, so the free electrons moving through the filament collide with them more often. This opposes the flow of charge more, so the resistance of the filament increases.",
        hints=["What happens to the temperature of the filament as more current flows?",
               "How does a higher temperature affect the metal ions in the filament, and how does that affect the electrons?",
               "Link temperature, ion vibrations, electron collisions and resistance."],
        keywords="hotter filament; ions vibrate more; more collisions with electrons; resistance rises",
        figure=lambda: figs3.iv_graph("lamp"),
        sample_pass=["The filament gets hotter so the metal ions vibrate more and the electrons collide with them more often, increasing the resistance",
                     "higher temperature means more vigorous vibration of the atoms, so electrons are obstructed more"],
        sample_fail=["The electrons get bigger and cannot fit through the wire", "The lamp uses up the current so less flows"])

# ---------------------------------------------------------------- L4
written("w14_ohmic_graph_meaning", 14, 4, "14k",
        stem="Fig. 1 shows the I-V graph for a metal wire at constant temperature. Describe the graph, state what it shows about the wire, and explain how the resistance can be found from it.",
        points=[P("a straight line through the origin", ["straight line", "through the origin", "linear", "passes through zero"]),
                P("current is directly proportional to p.d., so the wire is an ohmic conductor with constant resistance", ["directly proportional", "proportional", "ohmic", "constant resistance", "obeys ohm"]),
                P("resistance = V ÷ I for any point on the line (the reciprocal of the gradient of the I-V graph)", ["v divided by i", "v / i", "v over i", "p.d. divided by current", "1 / gradient", "reciprocal of the gradient", "inverse of the gradient", "gradient"])],
        min_points=2,
        model_answer="The graph is a straight line through the origin, so the current is directly proportional to the p.d.: the wire is an ohmic conductor and its resistance is constant. The resistance can be found by taking any point on the line and dividing the p.d. by the current, R = V ÷ I; this equals 1 ÷ (gradient of the I-V line).",
        hints=["Describe the shape first: straight or curved? Through the origin?",
               "What does a straight line through the origin tell you about I and V?",
               "How do you get R from a pair of values read off the line?"],
        keywords="straight line through origin; I ∝ V, ohmic, constant R; R = V/I = 1/gradient",
        figure=lambda: figs3.iv_graph("ohmic", R=4.0),
        sample_pass=["A straight line through the origin, so current is proportional to p.d. and the resistance is constant; R is V divided by I for any point",
                     "linear through zero, the wire is ohmic; resistance is 1 over the gradient"],
        sample_fail=["A curve that gets flatter, so the resistance decreases", "The gradient of the line is the resistance in ohms"])

written("w14_diode_behaviour", 14, 4, "14k",
        stem="Fig. 1 shows the I-V characteristic of a semiconductor diode. Describe how the current depends on the p.d., and state what this means for the way the diode is used.",
        points=[P("in the forward direction, almost no current flows until the p.d. reaches a small threshold (about 0.6 V), after which the current rises steeply", ["forward", "threshold", "0.6", "0.7", "rises steeply", "sharply", "very little current until"]),
                P("in the reverse direction the current is (almost) zero: the diode has a very high resistance", ["reverse", "negative p.d.", "no current", "zero current", "very high resistance", "does not conduct", "blocks"]),
                P("so a diode allows current in one direction only, used e.g. to convert a.c. to d.c. (rectification) or to protect circuits from reversed connections", ["one direction", "one way", "rectif", "a.c. to d.c.", "ac to dc", "protect", "reversed"])],
        min_points=2,
        model_answer="In the forward direction almost no current flows until the p.d. reaches about 0.6 V; beyond that the current increases steeply, so the forward resistance becomes very small. In the reverse direction the current is almost zero, so the resistance is very high. A diode therefore conducts in one direction only, which is used to change a.c. into d.c. (rectification) and to protect circuits against a reversed supply.",
        hints=["Describe the forward part of the graph and the reverse part separately.",
               "What is special about the current when the p.d. is reversed?",
               "What can a one-way device be used for?"],
        keywords="forward: little current until ~0.6 V then steep rise; reverse: no current; one-way conduction, rectification",
        figure=lambda: figs3.iv_graph("diode", vmax=2.0),
        sample_pass=["Forward: no current until about 0.6 V, then it rises steeply; reverse: no current. So it conducts one way only and can turn a.c. into d.c.",
                     "the diode blocks current in the reverse direction and conducts in the forward direction above a threshold, so it is used for rectification"],
        sample_fail=["The current is proportional to the p.d. in both directions", "A diode stores charge like a battery"])

# ---------------------------------------------------------------- L5
written("w14_claim_voltage_flows", 14, 5, "14f",
        stem="A student writes: 'The 6 V from the battery flows through the lamp and is used up, so there is no current left after the lamp.' Identify and correct the mistakes in this statement.",
        points=[P("voltage (p.d.) does not flow; it is the energy transferred per unit charge (across the lamp), measured across the component", ["does not flow", "doesn't flow", "voltage is not a flow", "energy per unit charge", "energy per coulomb", "across the lamp", "measured across"]),
                P("current is not used up: the same current flows into and out of the lamp (charge is conserved)", ["not used up", "same current", "current is the same", "charge is conserved", "current flows out", "same before and after", "conserved"]),
                P("it is energy that is transferred in the lamp (to light and thermal energy); the charges keep flowing", ["energy is transferred", "energy is used", "transferred to light", "light and heat", "thermal energy", "electrons keep moving", "charges keep"])],
        min_points=2,
        model_answer="Voltage does not flow: the p.d. of 6 V across the lamp means that each coulomb of charge transfers 6 J of energy in the lamp. Current is not used up: the same current flows out of the lamp as flows into it, because charge is conserved. What is transferred in the lamp is energy, to light and thermal energy, while the charges continue round the circuit.",
        hints=["Is voltage something that flows along the wire, or something measured across a component?",
               "If current were used up, what would an ammeter after the lamp read? What does it actually read?",
               "Separate the ideas of charge (which flows and is conserved) and energy (which is transferred)."],
        keywords="p.d. is energy per unit charge, measured across; current/charge is conserved, same on both sides; energy is what is transferred",
        sample_pass=["Voltage does not flow, it is the energy per coulomb across the lamp; the current is the same on both sides because charge is conserved, it is energy that is transferred to light and heat",
                     "mistakes: p.d. is not a flow and current is not used up; the same current leaves the lamp, only energy is transferred"],
        sample_fail=["The student is right because the battery goes flat", "Voltage flows but current does not"])

written("w14_plan_resistance_length", 14, 5, "14i",
        stem="Plan an experiment to find out how the resistance of a wire depends on its length. State the measurements you would take, what you would keep constant, and how you would use your results.",
        points=[P("connect a known length of the wire in series with a cell/power supply and an ammeter, with a voltmeter across the wire; measure V and I (and the length with a metre rule)", ["ammeter", "voltmeter", "measure the current", "measure the p.d.", "metre rule", "measure the length", "in series", "across the wire"]),
                P("calculate R = V ÷ I for each length, repeating for at least five different lengths (e.g. by moving a crocodile clip)", ["r = v / i", "v divided by i", "v over i", "calculate the resistance", "five", "several lengths", "different lengths", "crocodile clip", "vary the length", "repeat"]),
                P("keep the material, thickness (cross-sectional area) and temperature constant (small current, switch off between readings)", ["same material", "same wire", "thickness", "diameter", "cross-sectional area", "temperature constant", "switch off", "small current", "same wire throughout"]),
                P("plot resistance against length; a straight line through the origin shows R is proportional to length", ["plot", "graph", "straight line", "through the origin", "proportional"])],
        min_points=3,
        model_answer="Connect the wire in series with a power supply, a switch and an ammeter, and connect a voltmeter across the wire. Use a crocodile clip to connect a measured length of wire (measured with a metre rule), close the switch, record V and I, and calculate R = V ÷ I. Repeat for at least five different lengths. Use the same wire throughout so the material and cross-sectional area are constant, and keep the current small and switch off between readings so the temperature does not change. Plot a graph of resistance against length: a straight line through the origin shows that resistance is directly proportional to length.",
        hints=["What two meters do you need to find a resistance, and how are they connected?",
               "What should you change, what should you measure, and what must stay the same for a fair test?",
               "How would a graph show the relationship?"],
        keywords="ammeter in series, voltmeter across; R = V/I for five lengths; same wire (material, area), temperature constant; plot R against L, straight line through origin",
        sample_pass=["Put the wire in series with an ammeter and a voltmeter across it, measure V and I for at least five lengths with a metre rule, calculate R = V/I, keep the same wire and a small current so the temperature is constant, and plot R against length to see a straight line through the origin",
                     "vary the length with a crocodile clip, record current and p.d., work out resistance each time, keep thickness and material the same, graph resistance against length"],
        sample_fail=["Connect the wire to the mains and see if it glows", "Measure the mass of different lengths of wire and compare"])
