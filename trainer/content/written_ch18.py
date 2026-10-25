"""Chapter 18 Electromagnetism: written-answer questions, two per level (field of a wire and a solenoid, electromagnets,
circuit breaker, force on a conductor, Fleming's left-hand rule, the d.c. motor and its commutator)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w18_wire_field_pattern", 18, 1, "18a",
        stem="Fig. 1 shows a straight wire carrying a current out of the page. Describe the pattern of the magnetic field around the wire.",
        points=[P("concentric circles centred on the wire", ["concentric circles", "circles", "circular", "rings around the wire"]),
                P("lines further apart (field weaker) further from the wire; direction given by the right-hand grip rule (anticlockwise here)", ["further apart", "weaker further", "spread out", "anticlockwise", "right-hand grip", "right hand grip"])],
        model_answer="The field lines are concentric circles centred on the wire. They get further apart with distance from the wire, showing the field becomes weaker, and their direction (anticlockwise here, for current out of the page) is given by the right-hand grip rule.",
        hints=["What shape are the field lines around a straight wire?", "How does their spacing change, and which rule gives their direction?", "Describe the shape, the spacing and the direction."],
        keywords="concentric circles; further apart further away; right-hand grip rule",
        figure=lambda: figs3.wire_field("out"),
        sample_pass=["Concentric circles around the wire that get further apart further away, going anticlockwise", "circular field lines centred on the wire, direction from the right-hand grip rule"],
        sample_fail=["Straight lines going out from the wire", "Lines from the north end of the wire to the south end"])

written("w18_electromagnet_strength", 18, 1, "18b",
        stem="State two ways of increasing the strength of an electromagnet.",
        points=[P("increase the current in the coil", ["increase the current", "more current", "larger current", "bigger current"]),
                P("increase the number of turns (or use a soft-iron core)", ["more turns", "increase the number of turns", "more coils", "soft iron core", "iron core", "add an iron core"])],
        model_answer="Increase the current in the coil, and increase the number of turns of wire on the coil. (Putting a soft-iron core inside also strengthens it greatly.)",
        hints=["What flows in the coil, and how much wire is wound on it?", "Both can be increased.", "State two ways."],
        keywords="more current; more turns (soft-iron core)",
        sample_pass=["Increase the current and use more turns", "add more coils of wire and pass a larger current"],
        sample_fail=["Use a thinner core made of copper", "Reverse the current"])

# ---------------------------------------------------------------- L2
written("w18_solenoid_field", 18, 2, "18a",
        stem="Fig. 1 shows a solenoid carrying a current. Describe the magnetic field inside and outside the solenoid, and state what happens to the field when the current is reversed.",
        points=[P("inside: strong, uniform field with parallel field lines along the axis", ["uniform", "parallel", "strong inside", "straight lines inside", "along the axis"]),
                P("outside: like the field of a bar magnet, with N and S poles at the ends", ["bar magnet", "like a magnet", "poles at the ends", "north and south poles", "n and s"]),
                P("reversing the current reverses the direction of the field (the poles swap)", ["reverses the field", "field reverses", "poles swap", "poles change", "opposite direction", "poles are reversed"])],
        min_points=2,
        model_answer="Inside the solenoid the field is strong and uniform, with parallel field lines along its axis. Outside, the field is like that of a bar magnet, with a N pole at one end and a S pole at the other. Reversing the current reverses the direction of the field, so the poles swap ends.",
        hints=["Compare the field lines inside with those outside.", "What magnet does the outside pattern resemble?", "What does reversing the current do?"],
        keywords="uniform parallel field inside; bar-magnet pattern outside with poles; reversing current reverses field",
        figure=lambda: figs3.solenoid(),
        sample_pass=["Inside the field is strong and uniform with parallel lines, outside it is like a bar magnet, and reversing the current swaps the poles",
                     "a uniform field along the axis inside, bar magnet shape outside; reversing the current reverses the field"],
        sample_fail=["There is no field inside a solenoid", "Reversing the current makes the field stronger"])

written("w18_fleming_rule", 18, 2, "18d",
        stem="State Fleming's left-hand rule and say what it is used for.",
        points=[P("first finger: field; second finger: current; thumb: force (motion), all at right angles", ["first finger", "forefinger", "second finger", "thumb", "at right angles", "field current", "motion"]),
                P("used to find the direction of the force on a current-carrying conductor (e.g. in a motor) in a magnetic field", ["direction of the force", "force on a current", "force on a wire", "motor", "direction of motion"])],
        model_answer="Hold the thumb, first finger and second finger of the left hand at right angles: the first finger points along the magnetic field (N to S), the second finger along the conventional current, and the thumb then gives the direction of the force (motion). It is used to find the direction of the force on a current-carrying conductor in a magnetic field, as in an electric motor.",
        hints=["Three fingers, three quantities, all at right angles.", "First finger = Field, seCond finger = Current, thuMb = Motion.", "State the rule and its use."],
        keywords="first finger field, second finger current, thumb force/motion; direction of force on a current in a field",
        sample_pass=["First finger field, second finger current, thumb gives the force, used to find the direction of the force on a wire in a magnetic field",
                     "on the left hand the forefinger is the field, the second finger the current and the thumb the motion; it gives the direction a motor turns"],
        sample_fail=["Right hand: thumb is the current, fingers curl round the field", "It gives the direction of the induced current in a generator"])

# ---------------------------------------------------------------- L3
written("w18_circuit_breaker", 18, 3, "18b",
        stem="Explain how an electromagnetic circuit breaker cuts off the current when the current becomes too large.",
        points=[P("the current passes through an electromagnet (coil) in the circuit", ["electromagnet", "coil", "solenoid", "current flows through the coil"]),
                P("if the current exceeds the set value, the electromagnet becomes strong enough to attract the iron armature / catch", ["strong enough", "attracts the iron", "attracts the armature", "pulls the iron", "too large a current", "exceeds", "stronger"]),
                P("the catch is released and a spring pulls the contacts apart, breaking the circuit; it can be reset", ["contacts separate", "contacts open", "spring", "breaks the circuit", "switch opens", "trips", "reset"])],
        min_points=2,
        model_answer="The current flows through an electromagnet in the circuit breaker. If the current rises above the set value, the electromagnet becomes strong enough to attract an iron armature, which releases a catch; a spring then pulls the contacts apart, breaking the circuit. Once the fault is cleared the breaker can be reset with a switch.",
        hints=["What device in the breaker gets stronger as the current increases?", "What does it attract once it is strong enough?", "How are the contacts separated, and how is it reset?"],
        keywords="current through electromagnet; too large → attracts iron armature; catch released, spring opens contacts; can be reset",
        sample_pass=["The current goes through an electromagnet; a large current makes it strong enough to pull the iron catch, so a spring opens the contacts and breaks the circuit",
                     "when the current is too big the coil attracts the armature and the switch trips, and it can be reset afterwards"],
        sample_fail=["A thin wire melts and must be replaced", "The circuit breaker lowers the voltage"])

written("w18_force_on_conductor_factors", 18, 3, "18c",
        stem="A wire carrying a current is placed between the poles of a magnet, at right angles to the field, as shown in Fig. 1. The wire moves. Explain why it moves, and describe the effect of reversing (i) the current and (ii) the field.",
        points=[P("the magnetic field of the current interacts with the field of the magnet, producing a force on the wire", ["interact", "fields combine", "field of the current", "force on the wire", "experiences a force", "catapult"]),
                P("reversing the current reverses the direction of the force (and the motion)", ["reversing the current reverses", "current is reversed the force", "opposite direction", "moves the other way"]),
                P("reversing the field also reverses the force; reversing both leaves it unchanged", ["reversing the field", "field is reversed", "both are reversed", "reversing both", "unchanged", "swap the poles"])],
        min_points=2,
        model_answer="The current produces its own magnetic field around the wire, which interacts with the field of the magnet, so the wire experiences a force at right angles to both the current and the field. Reversing the current reverses the direction of the force; reversing the field also reverses it. If both are reversed, the force is in the original direction.",
        hints=["The current in the wire has a field of its own. What happens when two fields interact?", "What happens to the force when one of them is reversed?", "And when both are reversed?"],
        keywords="current's field interacts with magnet's field → force; reversing current or field reverses force; both → unchanged",
        figure=lambda: figs3.flemings_lhr(),
        sample_pass=["The field of the current interacts with the magnet's field to give a force; reversing the current or the field reverses the force",
                     "the wire feels a force because the two fields interact; reversing either the current or the poles makes it move the other way"],
        sample_fail=["The wire is attracted because copper is magnetic", "Reversing the current makes the force bigger"])

# ---------------------------------------------------------------- L4
written("w18_motor_how_it_turns", 18, 4, "18e",
        stem="Fig. 1 shows a simple d.c. motor. Explain why the coil experiences a turning effect when a current flows.",
        points=[P("the current in sides AB and CD is in opposite directions", ["opposite directions", "opposite way", "ab and cd", "two sides", "one side up"]),
                P("so the forces on the two sides (Fleming's left-hand rule) are in opposite directions, one up and one down", ["forces in opposite directions", "one up and one down", "one side up and the other down", "opposite forces", "fleming"]),
                P("these two forces form a couple / produce a moment about the axle, so the coil turns", ["moment", "couple", "turning effect", "rotate", "turns", "torque"])],
        min_points=2,
        model_answer="The current flows in opposite directions in the two sides of the coil, AB and CD, which are at right angles to the magnetic field. By Fleming's left-hand rule the forces on the two sides are therefore in opposite directions, one upwards and one downwards. These two forces produce a moment about the axle, so the coil turns.",
        hints=["Compare the direction of the current in the two sides of the coil next to the poles.", "What does that mean for the forces on those sides?", "Two opposite forces on either side of an axle produce what?"],
        keywords="current opposite in the two sides; forces opposite (one up, one down); moment/couple turns the coil",
        figure=lambda: figs3.motor_diagram(),
        sample_pass=["The current goes opposite ways in AB and CD, so by Fleming's rule one side is pushed up and the other down, giving a moment that turns the coil",
                     "opposite currents in the two sides give opposite forces, a turning effect about the axle"],
        sample_fail=["The magnet attracts the copper coil", "The coil turns because it gets hot"])

written("w18_commutator_role", 18, 4, "18f",
        stem="Explain the purpose of the split-ring commutator in a simple d.c. motor, and why a soft-iron cylinder is placed inside the coil.",
        points=[P("the commutator reverses the current in the coil every half turn (when the coil is vertical)", ["reverses the current", "every half turn", "half a turn", "when the coil is vertical", "changes the direction of the current"]),
                P("so the forces keep turning the coil in the same direction (continuous rotation) instead of the coil rocking back", ["same direction", "keeps turning", "continuous", "continues to rotate", "instead of stopping", "keeps rotating one way"]),
                P("the soft-iron cylinder concentrates the magnetic field (makes it stronger and radial), increasing the turning effect", ["concentrates", "stronger field", "strengthens", "increases the turning", "radial", "more force"])],
        min_points=2,
        model_answer="The split-ring commutator reverses the direction of the current in the coil every half turn, as the coil passes the vertical position. This keeps the forces on each side acting so that the coil continues to turn in the same direction, instead of rocking back. The soft-iron cylinder inside the coil concentrates the magnetic field, making it stronger, so the turning effect on the coil is increased.",
        hints=["What would the coil do after half a turn if the current did not change direction?", "When and how does the commutator change the current?", "What does soft iron do to the magnetic field?"],
        keywords="commutator reverses current every half turn so rotation continues one way; soft iron concentrates/strengthens field",
        figure=lambda: figs3.motor_diagram(),
        sample_pass=["The commutator reverses the current every half turn so the coil keeps turning the same way; the soft iron makes the field stronger",
                     "it changes the direction of the current when the coil is vertical, giving continuous rotation; the iron core concentrates the field and increases the turning effect"],
        sample_fail=["The commutator stores charge for the motor", "The iron cylinder makes the coil lighter"])

# ---------------------------------------------------------------- L5
written("w18_claim_more_magnets_faster", 18, 5, "18e",
        stem="A student says: 'To make a model motor turn faster, I should reverse the battery.' Evaluate this suggestion and suggest two changes that would work.",
        points=[P("the suggestion is wrong: reversing the battery reverses the current, which reverses the direction of rotation but not the size of the turning effect", ["wrong", "incorrect", "reverses the direction", "turn the other way", "opposite direction", "not faster"]),
                P("increase the current (more cells / lower resistance)", ["increase the current", "more current", "more cells", "larger current", "higher voltage"]),
                P("increase the number of turns on the coil, or use a stronger magnet / soft-iron core", ["more turns", "increase the number of turns", "stronger magnet", "soft iron", "iron core", "stronger field"])],
        min_points=2,
        model_answer="The suggestion is wrong: reversing the battery reverses the current, so the motor simply turns the other way at the same speed. To make it turn faster, increase the current (for example by adding cells) or increase the number of turns on the coil; using a stronger magnet or a soft-iron core also increases the turning effect.",
        hints=["What does reversing the current do to the force on the coil: its size or its direction?", "What factors increase the turning effect on the coil?", "Judge the suggestion and give two correct changes."],
        keywords="reversing battery only reverses rotation; increase current; more turns; stronger field",
        sample_pass=["Wrong, reversing the battery just makes it spin the other way; increase the current and use more turns on the coil",
                     "it would turn in the opposite direction, not faster; a stronger magnet and a bigger current would work"],
        sample_fail=["Correct, reversing the battery doubles the speed", "Use a weaker magnet so the coil is free to spin"])

written("w18_beam_deflection_explain", 18, 5, "18c",
        stem="A beam of electrons in a vacuum tube passes between the poles of a magnet and is deflected. Explain why the beam is deflected, and describe how Fleming's left-hand rule must be applied to find the direction.",
        points=[P("a moving beam of charged particles is an electric current, so it experiences a force in the magnetic field", ["beam is a current", "moving charges", "acts as a current", "current", "force on moving charge", "experiences a force"]),
                P("electrons are negative, so the conventional current is in the opposite direction to the beam", ["opposite direction", "opposite to the electrons", "conventional current is opposite", "negative", "reverse the direction"]),
                P("apply the rule with the second finger along the conventional current (opposite to the electron motion) and the first finger along the field; the thumb gives the deflection", ["second finger", "first finger along the field", "thumb gives", "fleming", "left hand"])],
        min_points=2,
        model_answer="A moving beam of electrons is an electric current, so like a current-carrying wire it experiences a force when it crosses a magnetic field, and the beam is deflected. Because electrons are negative, the conventional current is in the opposite direction to the beam's motion. In Fleming's left-hand rule, point the first finger along the field (N to S) and the second finger along this conventional current, opposite to the electrons; the thumb then gives the direction of the deflection.",
        hints=["Why should a beam of moving charges behave like a current in a wire?", "Electrons are negative: which way is the conventional current?", "How do you set up your fingers for the rule?"],
        keywords="moving charges = current, force in field; electrons negative so conventional current is opposite; second finger along conventional current",
        sample_pass=["The beam is a current so it feels a force; because electrons are negative the conventional current is opposite to their motion, so the second finger points opposite to the beam",
                     "moving charges experience a force in a magnetic field; use Fleming's left-hand rule with the current direction reversed for electrons"],
        sample_fail=["The beam is attracted to the north pole because electrons are magnetic", "The beam is deflected by gravity"])
