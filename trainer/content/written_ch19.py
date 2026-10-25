"""Chapter 19 Electromagnetic Induction: written-answer questions, two per level (inducing an e.m.f., factors, Lenz's law,
a.c. generator and slip rings, transformer structure and action, high-voltage transmission)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w19_when_emf_induced", 19, 1, "19a",
        stem="Fig. 1 shows a magnet and a coil connected to a galvanometer. State when an e.m.f. is induced in the coil.",
        points=[P("when the magnetic field through the coil changes, e.g. when the magnet moves relative to the coil (in or out)", ["changes", "changing", "moves", "moving", "relative motion", "pushed in", "pulled out", "cuts"])],
        pitfalls=[PF(["held still", "stationary magnet", "when the magnet is still", "magnet is at rest"], "No e.m.f. is induced when the magnet is stationary: the field through the coil must be CHANGING.")],
        model_answer="An e.m.f. is induced whenever the magnetic field through the coil changes, for example while the magnet is being moved into or out of the coil.",
        hints=["What happens to the galvanometer when the magnet is stopped inside the coil?", "The e.m.f. needs something to be changing.", "State the condition."],
        keywords="magnetic field through the coil changing (relative motion)",
        figure=lambda: figs3.magnet_into_coil("in"),
        sample_pass=["When the magnet moves into or out of the coil", "whenever the magnetic field linking the coil is changing"],
        sample_fail=["When the magnet is held still inside the coil", "Only when a battery is connected"])

written("w19_transformer_parts", 19, 1, "19d",
        stem="Fig. 1 shows a simple transformer. Name its three main parts.",
        points=[P("a primary coil (input)", ["primary coil", "primary", "input coil"]),
                P("a secondary coil (output)", ["secondary coil", "secondary", "output coil"]),
                P("a (laminated) soft-iron core linking the coils", ["iron core", "soft iron", "soft-iron", "core", "laminated"])],
        model_answer="A transformer has a primary (input) coil and a secondary (output) coil, both wound on a laminated soft-iron core.",
        hints=["There are two coils and something they are both wound on.", "Name both coils and the core material.", "Primary, secondary, soft-iron core."],
        keywords="primary coil, secondary coil, soft-iron core",
        figure=lambda: figs3.transformer(),
        sample_pass=["A primary coil, a secondary coil and a soft iron core", "input coil, output coil and a laminated iron core"],
        sample_fail=["A magnet, a battery and a switch", "A commutator and brushes"])

# ---------------------------------------------------------------- L2
written("w19_emf_factors", 19, 2, "19a",
        stem="State three ways of increasing the e.m.f. induced when a magnet is moved into a coil.",
        points=[P("move the magnet faster", ["faster", "more quickly", "greater speed", "higher speed", "quicker"]),
                P("use more turns on the coil", ["more turns", "increase the number of turns", "more coils"]),
                P("use a stronger magnet", ["stronger magnet", "stronger field", "more powerful magnet"])],
        min_points=2,
        model_answer="Move the magnet faster, use a coil with more turns, and use a stronger magnet. Each makes the magnetic field through the coil change more quickly.",
        hints=["The e.m.f. depends on how fast the field through the coil changes.", "Think about the motion, the coil and the magnet.", "State three ways."],
        keywords="faster motion, more turns, stronger magnet",
        sample_pass=["Move the magnet faster, use more turns and use a stronger magnet", "a stronger magnet pushed in more quickly into a coil with more turns"],
        sample_fail=["Use a bigger galvanometer", "Use thicker wire and a slower magnet"])

written("w19_slip_rings", 19, 2, "19b",
        stem="A simple a.c. generator has a coil rotating in a magnetic field, connected to the external circuit through slip rings and brushes. State the purpose of the slip rings and brushes.",
        points=[P("they keep the rotating coil connected to the external circuit without the wires twisting", ["connected", "connection", "without twisting", "wires twisting", "tangle", "continuous contact", "rotating coil"]),
                P("each ring stays connected to the same end of the coil, so the output is alternating (it is not reversed every half turn)", ["same end", "alternating", "a.c.", "ac output", "not reversed", "each ring"])],
        model_answer="The slip rings and brushes keep the rotating coil connected to the external circuit without the wires becoming twisted. Each slip ring stays connected to the same end of the coil, so the alternating e.m.f. induced in the coil is passed on to the circuit as an alternating current.",
        hints=["How can a coil spin continuously and still be connected to stationary wires?", "How does this differ from a split-ring commutator?", "State the purpose of the rings and what kind of output results."],
        keywords="keep rotating coil connected without twisting; each ring to the same end, output a.c.",
        sample_pass=["They connect the spinning coil to the circuit without the wires twisting, and the output stays alternating", "each slip ring is always connected to the same end of the coil so the current is a.c."],
        sample_fail=["They reverse the current every half turn to give d.c.", "They make the coil spin faster"])

# ---------------------------------------------------------------- L3
written("w19_lenz_law", 19, 3, "19a",
        stem="When the N pole of a magnet is pushed into a coil, the induced current makes the end of the coil nearest the magnet a N pole. Explain why this must be so.",
        points=[P("the induced current opposes the change producing it (Lenz's law)", ["opposes the change", "oppose", "lenz", "opposes the motion"]),
                P("a N pole facing the magnet's N pole repels it, opposing the motion into the coil", ["repels", "repel", "pushes the magnet away", "opposes the motion"]),
                P("so work must be done to push the magnet in; this work is transferred to electrical energy (energy is conserved)", ["work must be done", "work is done", "energy", "conservation of energy", "conserved"])],
        min_points=2,
        model_answer="The direction of the induced current always opposes the change that produces it (Lenz's law). A N pole at the near end of the coil repels the approaching N pole, opposing the motion of the magnet into the coil. This means work must be done to push the magnet in, and that work is transferred to electrical energy in the circuit, as required by the conservation of energy.",
        hints=["State the rule about the direction of an induced current.", "What does a N pole do to an approaching N pole?", "Link this to energy: what would happen if the coil attracted the magnet instead?"],
        keywords="induced current opposes the change; N repels approaching N; work done → electrical energy (conservation)",
        sample_pass=["The induced current opposes the change, so a N pole is made to repel the incoming N pole; work is done pushing it in and becomes electrical energy",
                     "Lenz's law: the coil opposes the motion by repelling the magnet, otherwise energy would be created from nothing"],
        sample_fail=["Because the coil is made of copper which is a north material", "The coil attracts the magnet to speed it up"])

written("w19_transformer_action", 19, 3, "19d",
        stem="Explain how a transformer produces an alternating e.m.f. in its secondary coil.",
        points=[P("an alternating current in the primary coil produces an alternating (changing) magnetic field in the iron core", ["alternating current", "a.c. in the primary", "changing magnetic field", "alternating magnetic field", "varying field"]),
                P("the soft-iron core links (carries) this changing field through the secondary coil", ["iron core", "core links", "core carries", "through the secondary", "links the coils"]),
                P("the changing field through the secondary coil induces an alternating e.m.f. in it", ["induces", "induced", "e.m.f. is induced", "emf in the secondary"])],
        min_points=2,
        model_answer="An alternating current in the primary coil produces a magnetic field in the soft-iron core that is continually changing in size and direction. The core links this changing field through the secondary coil, and the changing magnetic field through the secondary induces an alternating e.m.f. across it.",
        hints=["What kind of current is in the primary, and what kind of field does it produce?", "What is the job of the iron core?", "What does a changing field through the secondary do?"],
        keywords="a.c. in primary → changing field in core; core links field to secondary; changing field induces e.m.f.",
        figure=lambda: figs3.transformer(),
        sample_pass=["The a.c. in the primary makes a changing magnetic field in the iron core which passes through the secondary and induces an alternating e.m.f.",
                     "alternating current produces a varying field, the core links it to the secondary coil where an emf is induced"],
        sample_fail=["Electrons flow from the primary coil to the secondary through the core", "The core is a magnet that pushes current into the secondary"])

# ---------------------------------------------------------------- L4
written("w19_dc_no_transformer", 19, 4, "19d",
        stem="A student connects the primary coil of a transformer to a battery. Explain why there is no output from the secondary coil except at the instants the battery is connected and disconnected.",
        points=[P("a steady direct current gives a constant (unchanging) magnetic field in the core", ["steady", "constant field", "unchanging", "does not change", "direct current", "d.c."]),
                P("an e.m.f. is induced only when the magnetic field through the secondary is changing", ["only when", "changing", "change in the field", "no change", "must change"]),
                P("when switching on or off the field grows or collapses, so a brief e.m.f. is induced", ["switch on", "switching on", "switched off", "grows", "collapses", "brief", "momentary", "instant", "moment of connection", "connection or disconnection", "connected", "disconnected"])],
        min_points=2,
        model_answer="A battery gives a steady direct current, which produces a constant magnetic field in the core. An e.m.f. is induced in the secondary only when the magnetic field through it is changing, so with a steady field there is no output. At the instants of switching on and off the field grows or collapses, so a brief e.m.f. is induced at those moments only.",
        hints=["Is the field produced by a battery current changing or steady?", "What is needed for an e.m.f. to be induced?", "What happens to the field at the moment the battery is connected or disconnected?"],
        keywords="d.c. gives steady field; e.m.f. needs a changing field; brief e.m.f. at switch-on/off as field grows/collapses",
        sample_pass=["A battery gives a steady current so the field is constant and no emf is induced; only when switching on or off does the field change, giving a brief emf",
                     "the magnetic field only changes at the moment of connection or disconnection, so only then is an e.m.f. induced"],
        sample_fail=["Batteries are too weak to work a transformer", "The battery current cannot pass through the iron core"])

written("w19_high_voltage_transmission", 19, 4, "19f",
        stem="Fig. 1 shows how electrical energy is transmitted from a power station to homes. Explain why the energy is transmitted at a very high voltage.",
        points=[P("for the same power, a higher voltage means a smaller current in the cables (P = V I)", ["smaller current", "lower current", "less current", "current is reduced", "p = vi", "p = v i"]),
                P("the power lost as heat in the cables is I² R, so a smaller current means much less energy wasted", ["i2r", "i²r", "i^2 r", "less heat", "less energy lost", "less power lost", "heating", "wasted"]),
                P("so thinner (cheaper) cables can be used and transformers step the voltage up and down again", ["thinner cables", "cheaper", "step-up", "step-down", "transformer"])],
        min_points=2,
        model_answer="For a given power, P = VI, so transmitting at a very high voltage means the current in the cables is small. The power wasted as heat in the cables is I²R, so a small current greatly reduces the energy lost, and thinner, cheaper cables can be used. A step-up transformer raises the voltage at the power station and step-down transformers lower it again for homes.",
        hints=["How is the current related to the voltage for a fixed power?", "How does the heat lost in a cable depend on the current?", "Link high voltage → low current → low I²R loss."],
        keywords="same power, higher V → smaller I; loss = I²R much smaller; transformers step up and down",
        figure=lambda: figs3.transmission(["power = 100 MW", "transmission p.d. = 400 kV"]),
        sample_pass=["At a high voltage the current is smaller for the same power, so the I²R heating loss in the cables is much less",
                     "high voltage means low current, which reduces the energy wasted as heat in the cables; transformers step it up and down"],
        sample_fail=["High voltage makes electricity travel faster to homes", "A high voltage gives the cables more energy to store"])

# ---------------------------------------------------------------- L5
written("w19_claim_transformer_free_energy", 19, 5, "19e",
        stem="A student says: 'A step-up transformer gives out more energy than it takes in, because the output voltage is higher.' Evaluate this statement.",
        points=[P("the statement is wrong: a transformer cannot create energy (conservation of energy)", ["wrong", "incorrect", "cannot create energy", "conservation of energy", "energy is conserved"]),
                P("in an ideal transformer the power out equals the power in, Vp Ip = Vs Is", ["vp ip = vs is", "power in equals power out", "power is the same", "same power"]),
                P("so if the voltage is stepped up, the current is stepped down by the same factor (and real transformers lose some energy as heat)", ["current is smaller", "current decreases", "current is stepped down", "lower current", "less current", "heat", "losses"])],
        min_points=2,
        model_answer="The statement is wrong. Energy cannot be created, so a transformer cannot give out more energy than it takes in. For an ideal transformer the output power equals the input power, Vp Ip = Vs Is, so if the voltage is stepped up the current is stepped down by the same factor. Real transformers actually give out slightly less energy than they take in, because some is wasted as heat in the coils and core.",
        hints=["Can any device give out more energy than it receives?", "For an ideal transformer, what is equal on the two sides?", "If V goes up, what must happen to I?"],
        keywords="wrong; energy conserved; Vp Ip = Vs Is; higher V means lower I; real transformers lose some energy",
        sample_pass=["Wrong, energy is conserved: the power in equals the power out, so a higher output voltage comes with a smaller current",
                     "incorrect because Vp Ip = Vs Is; stepping up the voltage steps down the current, and real transformers waste some energy as heat"],
        sample_fail=["Correct, that is why power stations use step-up transformers", "The transformer stores the extra energy in its core"])

written("w19_generator_output_changes", 19, 5, "19c",
        stem="Fig. 1 shows the output of a simple a.c. generator. Describe and explain how the graph would change if the coil were rotated twice as fast.",
        points=[P("the frequency doubles: the period halves, so twice as many cycles appear in the same time", ["frequency doubles", "twice the frequency", "period halves", "half the period", "more cycles", "twice as many cycles"]),
                P("the peak e.m.f. increases (doubles) because the field through the coil changes faster", ["peak increases", "larger amplitude", "taller peaks", "peak doubles", "higher peak", "greater e.m.f.", "bigger voltage", "e.m.f. is larger", "emf is larger", "peaks are twice as high", "peak voltage doubles", "peaks twice as high"]),
                P("since the rate of change of the magnetic field through the coil is greater", ["rate of change", "changes faster", "faster change", "cuts the field faster", "more quickly", "changes twice as fast", "field changes faster"])],
        min_points=2,
        model_answer="If the coil rotates twice as fast, each revolution takes half the time, so the period halves and the frequency doubles: twice as many cycles appear on the same time axis. The magnetic field through the coil also changes twice as fast, so the induced e.m.f. is larger and the peaks of the graph are twice as high.",
        hints=["How does the time for one revolution change? What does that do to the period and frequency?", "Does the field through the coil change faster or slower?", "Describe both the change in frequency and the change in peak e.m.f."],
        keywords="frequency doubles (period halves); peak e.m.f. doubles; faster rate of change of field",
        figure=lambda: figs3.ac_output(),
        sample_pass=["The frequency doubles so the period halves, and the peak voltage doubles because the field through the coil changes faster",
                     "twice as many cycles in the same time and taller peaks, since the rate of change of the field is greater"],
        sample_fail=["The graph stays the same because the magnet is unchanged", "The output turns into d.c."])
