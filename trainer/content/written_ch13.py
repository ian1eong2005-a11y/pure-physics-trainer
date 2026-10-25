"""Chapter 13 Static Electricity: written-answer questions, two per level (charges and fields, charging by rubbing and induction,
hazards and the electrostatic precipitator)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w13_two_charges_unit", 13, 1, "13a",
        stem="State the two types of electric charge and the unit in which charge is measured.",
        points=[P("positive and negative", ["positive and negative", "positive negative", "negative and positive", "+ and -", "plus and minus"]),
                P("the coulomb (C)", ["coulomb", "coulombs", "unit c"])],
        model_answer="Charge can be positive or negative, and it is measured in coulombs (C).",
        hints=["There are exactly two kinds of charge.",
               "The unit is named after a French scientist; its symbol is C.",
               "Name both types and the unit."],
        keywords="positive, negative; coulomb (C)",
        sample_pass=["Positive and negative, measured in coulombs", "charge is + or - and its unit is the coulomb C"],
        sample_fail=["North and south, measured in amperes", "Static and current, measured in volts"])

written("w13_define_electric_field", 13, 1, "13c",
        stem="State what is meant by an electric field.",
        points=[P("a region in which an electric charge experiences a force", ["region", "space", "area"]),
                P("a charge in it experiences an (electric) force", ["charge experiences a force", "charge feels a force", "force acts on a charge", "force on a charge", "charge experiences", "charged object experiences", "charge placed in it experiences", "exerts a force on a charge", "charge feels"])],
        pitfalls=[PF(["magnetic material", "magnet experiences", "a magnet feels", "force due to a magnet", "pole experiences"], "That describes a MAGNETIC field. An electric field acts on electric charges.")],
        model_answer="An electric field is a region in which an electric charge experiences a force.",
        hints=["It is defined as a region of space with a particular property.",
               "What happens to a charge placed in that region?",
               "A region where a charge ... what?"],
        keywords="region where a charge experiences a force",
        sample_pass=["A region in which a charge experiences a force", "the space around a charged object where another charge feels an electric force"],
        sample_fail=["A region where a magnet experiences a force", "The flow of electrons in a wire"])

# ---------------------------------------------------------------- L2
written("w13_field_pattern_point_charge", 13, 2, "13d",
        stem="Fig. 1 shows the electric field of an isolated positive point charge. Describe the pattern of the field lines and state what their direction represents.",
        points=[P("straight lines radiating outwards from the charge in all directions (radial)", ["radial", "radiat", "outwards", "straight lines", "away from the charge", "spread out from"]),
                P("the arrows give the direction of the force on a positive test charge", ["positive test charge", "positive charge placed", "force on a positive", "direction of the force", "small positive charge"])],
        model_answer="The field lines are straight and radiate outwards from the charge in all directions, with arrows pointing away from the positive charge. The direction of a field line is the direction of the force that would act on a small positive test charge placed at that point.",
        hints=["Describe the shape: are the lines straight or curved, and where do they start?",
               "The arrows show the force on a particular kind of charge. Which sign?",
               "Describe the pattern, then state the meaning of the arrows."],
        keywords="radial, straight lines outwards; direction of force on a positive test charge",
        figure=lambda: figs3.point_charge_field("+"),
        sample_pass=["Straight lines radiating outwards from the charge; the arrows show the direction of the force on a positive test charge", "radial lines pointing away from the charge, showing which way a small positive charge would be pushed"],
        sample_fail=["Circles around the charge showing the direction a compass points", "Parallel lines going from left to right"])

written("w13_like_unlike_rule", 13, 2, "13b",
        stem="A student brings a negatively charged rod close to a light ball hanging on a thread. The ball moves away from the rod. State what this shows about the charge on the ball, and explain how you know.",
        points=[P("the ball is negatively charged", ["negatively charged", "negative charge", "ball is negative", "same charge as the rod", "same sign"]),
                P("because like charges repel (the ball is pushed away)", ["like charges repel", "repel", "repulsion", "same charges repel", "pushed away because"]),
                P("repulsion is the only certain test: attraction could also happen with an uncharged ball (by induction)", ["only sure test", "only certain", "uncharged ball would be attracted", "induction", "attraction is not proof", "neutral"])],
        min_points=2,
        model_answer="The ball must be negatively charged. The rod is negative and the ball is repelled, and only like charges repel. Repulsion is the only sure test for charge, because an uncharged ball would also be attracted to the rod by induction.",
        hints=["The ball moved AWAY. Is that attraction or repulsion?",
               "Which charges repel each other?",
               "State the ball's charge, give the rule, and say why repulsion is a reliable test."],
        keywords="ball negative; like charges repel; repulsion is the only sure test",
        sample_pass=["The ball is negative because like charges repel", "it has the same negative charge as the rod since it is repelled, and only repulsion proves a charge"],
        sample_fail=["The ball is positive because opposite charges repel", "The ball is uncharged"])

# ---------------------------------------------------------------- L3
written("w13_rubbing_transfers_electrons", 13, 3, "13f",
        stem="A polythene rod becomes negatively charged when rubbed with a woollen cloth. Explain, in terms of electrons, how the rod and the cloth become charged.",
        points=[P("friction/rubbing transfers electrons from the cloth to the rod", ["electrons are transferred", "electrons move", "electrons transfer", "transfer of electrons", "electrons from the cloth", "gains electrons", "electrons rubbed"]),
                P("the rod gains electrons so has an excess of negative charge", ["gains electrons", "extra electrons", "excess of electrons", "more electrons than protons", "rod becomes negative", "polythene becomes negative", "becomes negative", "negatively charged", "rod is negative", "polythene is negative"]),
                P("the cloth loses electrons and becomes positively charged with an equal and opposite charge", ["cloth loses electrons", "loses electrons", "cloth becomes positive", "wool becomes positive", "becomes positive", "positively charged", "equal and opposite", "fewer electrons", "cloth is positive", "wool is positive"])],
        pitfalls=[PF(["protons move", "protons are transferred", "positive charges move", "protons transfer"], "Only ELECTRONS move when insulators are rubbed. Protons are fixed in the nuclei.")],
        min_points=2,
        model_answer="Rubbing transfers electrons from the woollen cloth to the polythene rod. The rod now has more electrons than protons, so it carries a negative charge. The cloth has lost the same number of electrons, so it is left with an equal and opposite positive charge. The protons remain fixed in the nuclei; only the electrons are able to leave one surface for the other.",
        hints=["Which particles can move between two insulators when they are rubbed together?",
               "The rod ends up negative. Did it gain or lose electrons? What happened to the cloth?",
               "Explain the electron transfer and the charge on each object."],
        keywords="electrons transferred from cloth to rod; rod gains electrons (negative); cloth loses electrons (positive)",
        sample_pass=["Electrons are rubbed off the cloth onto the rod, so the rod gains electrons and is negative while the cloth loses electrons and is positive",
                     "the friction transfers electrons from the wool to the polythene which becomes negative; the wool becomes positive"],
        sample_fail=["Protons move from the rod to the cloth", "The rod creates new negative charges by friction"])

written("w13_induction_method", 13, 3, "13g",
        stem="Fig. 1 shows a negatively charged rod held near two touching metal spheres on insulating stands. Describe how to use this arrangement to give the spheres equal and opposite charges, and state the sign of the charge on each sphere.",
        points=[P("the rod repels free electrons to the far sphere, leaving the near sphere short of electrons", ["repels electrons", "electrons move to the far", "electrons are pushed", "electrons repelled", "free electrons move", "electrons move away"]),
                P("separate the spheres while the rod is still in place, then remove the rod", ["separate the spheres", "move the spheres apart", "while the rod is still", "rod still near", "then remove the rod", "before removing the rod"]),
                P("the near sphere is positive and the far sphere is negative", ["near sphere positive", "nearer sphere is positive", "sphere nearest the rod is positive", "far sphere negative", "further sphere is negative", "a positive b negative", "a is positive"])],
        pitfalls=[PF(["remove the rod first", "take the rod away then separate", "remove the rod before"], "If the rod is removed first, the electrons flow back and both spheres become neutral again. Separate the spheres FIRST, then remove the rod.")],
        min_points=2,
        model_answer="The negative rod repels free electrons in the metal to the far sphere, so the near sphere is left with a shortage of electrons. With the rod still in place, separate the two spheres; then take the rod away. The sphere that was nearer the rod is positively charged and the far sphere is negatively charged, with equal and opposite charges.",
        hints=["What does the negative rod do to the free electrons in the metal?",
               "In what order should the spheres be separated and the rod removed? Why does the order matter?",
               "Describe the electron movement, the steps, and the final charges."],
        keywords="electrons repelled to the far sphere; separate spheres with rod present; remove rod; near +, far −",
        figure=lambda: figs3.induction_spheres(1, rod_sign="-"),
        sample_pass=["The rod pushes electrons to the far sphere; separate the spheres while the rod is there, then remove it: the near sphere is positive and the far one negative",
                     "electrons are repelled away from the rod, the spheres are moved apart before the rod is removed, leaving the nearer sphere + and the further sphere -"],
        sample_fail=["Touch the rod on the spheres to transfer charge", "Remove the rod first, then separate the spheres"])

# ---------------------------------------------------------------- L4
written("w13_refuelling_hazard", 13, 4, "13h",
        stem="When an aircraft is refuelled, the aircraft and the fuel tanker are connected to each other and to the ground by a metal wire before fuel starts to flow. Explain why this is necessary.",
        points=[P("fuel flowing through the pipe (and the aircraft moving through air) causes friction that separates charge, so static charge builds up", ["friction", "fuel flowing", "rubbing", "builds up", "static charge", "becomes charged", "charge accumulates"]),
                P("a large charge could cause a spark as it discharges", ["spark", "discharge", "jump", "sparks"]),
                P("a spark could ignite the fuel vapour causing a fire or explosion", ["ignite", "fire", "explosion", "explode", "burn", "fuel vapour"]),
                P("the wire earths the aircraft so charge flows safely away to the ground (no potential difference builds up)", ["earth", "flows to the ground", "flows safely", "conducts the charge away", "same potential", "no potential difference"])],
        min_points=3,
        model_answer="Fuel rubbing against the pipe, and the aircraft moving through the air, separate charge by friction, so static charge builds up on the aircraft and tanker. If enough charge built up it could discharge as a spark, and a spark could ignite the fuel vapour, causing a fire or explosion. The metal wire earths the aircraft and tanker so that any charge flows safely away to the ground and no spark can form.",
        hints=["How could static charge build up during refuelling?",
               "What can a large static charge do, and why is that dangerous near fuel?",
               "Explain the build-up, the danger, and what the wire does."],
        keywords="friction builds up static charge; spark; ignites fuel vapour; wire earths it so charge flows away safely",
        sample_pass=["Fuel flowing through the pipe builds up static charge by friction; a spark could ignite the fuel vapour, so the wire earths the aircraft and lets the charge flow safely away",
                     "static charge from friction could discharge as a spark and cause an explosion, the earth wire conducts the charge to the ground"],
        sample_fail=["The wire stops the aircraft rolling away", "The wire carries electricity to power the fuel pump"])

written("w13_precipitator_explain", 13, 4, "13i",
        stem="Fig. 1 shows an electrostatic precipitator fitted inside a factory chimney. Explain how it removes dust and smoke particles from the waste gases.",
        points=[P("the central wire is at a high (negative) voltage and charges the dust particles passing it (by giving them electrons)", ["high voltage", "wire charges", "particles become charged", "negatively charged", "gives them electrons", "charged by the wire", "particles are charged"]),
                P("the charged particles are attracted to the oppositely charged (earthed/positive) plates", ["attracted to the plates", "attracted to the oppositely", "opposite charge", "plates are positive", "move to the plates", "stick to the plates"]),
                P("the particles stick to the plates, which are shaken or knocked periodically so the dust falls and is collected, leaving cleaner gas", ["stick", "collect", "knocked", "shaken", "falls", "removed", "cleaner"])],
        min_points=2,
        model_answer="The wire in the middle of the chimney is kept at a high negative voltage, so dust and smoke particles passing it gain electrons and become negatively charged. The charged particles are then attracted to the positively charged (earthed) plates, where they stick. The plates are knocked or shaken from time to time so the dust falls into a collector, and the gas leaving the chimney is much cleaner.",
        hints=["First the particles must be given a charge. How?",
               "Once charged, where do the particles go, and why?",
               "Describe charging, attraction to the plates, and collection."],
        keywords="high-voltage wire charges particles; attracted to oppositely charged plates; stick and are collected",
        figure=lambda: figs3.precipitator(),
        sample_pass=["The high-voltage wire charges the dust particles negatively, they are attracted to the positive plates and stick there, and the plates are knocked so the dust falls off and is collected",
                     "particles become charged as they pass the wire and are then attracted to the oppositely charged plates where they collect"],
        sample_fail=["A fan blows the dust back down the chimney", "The plates are magnets that attract the iron in the dust"])

# ---------------------------------------------------------------- L5
written("w13_evaluate_attraction_proof", 13, 5, "13b",
        stem="A student says: 'My plastic ruler attracts small pieces of paper, so the paper must be charged.' Evaluate this statement.",
        points=[P("the conclusion is not justified: attraction does not prove the paper is charged", ["not justified", "wrong", "incorrect", "does not prove", "not necessarily", "cannot conclude", "not valid"]),
                P("the charged ruler induces charges in the neutral paper: the side nearer the ruler gets the opposite charge, so it is attracted", ["induc", "opposite charge on the near side", "separates the charges", "near side", "redistribut", "electrons in the paper move"]),
                P("only repulsion is a sure test for charge (a neutral object is never repelled)", ["repulsion", "repel", "only sure test", "never repelled"])],
        min_points=2,
        model_answer="The conclusion does not follow. The charged ruler induces charge in the uncharged paper: electrons in the paper are pushed or pulled so that the side nearer the ruler carries the opposite charge, and this side is attracted more strongly than the far side is repelled. Attraction therefore happens with neutral paper. Only repulsion is a sure test for charge, because a neutral object can never be repelled.",
        hints=["Can an uncharged object be attracted to a charged one? Think about what the ruler's charge does to the electrons in the paper.",
               "Which effect, attraction or repulsion, is the only sure sign that an object is charged?",
               "Judge the statement, explain induction, and give the sure test."],
        keywords="attraction not proof; induction gives the near side the opposite charge; only repulsion proves charge",
        sample_pass=["The student is wrong: the charged ruler induces an opposite charge on the near side of the neutral paper, so attraction happens anyway; only repulsion proves a charge",
                     "not justified, uncharged paper is attracted by induction; repulsion would be the real test"],
        sample_fail=["The student is right, only charged objects can be attracted", "The paper must be magnetic"])

written("w13_antistatic_design", 13, 5, "13h",
        stem="Technicians who assemble computer circuit boards wear a wrist strap connected to earth by a wire containing a large resistor. Explain why the strap is worn, and suggest why the wire contains a resistor rather than being a plain copper wire.",
        points=[P("the technician's body can become charged by friction (e.g. with clothing or the chair), and a discharge/spark through a component could damage it", ["charged by friction", "static", "build up charge", "discharge", "spark", "damage the components", "damage the circuit", "destroy"]),
                P("the strap earths the body so charge flows away continuously and no high potential builds up", ["earth", "flows away", "flows to earth", "conducts the charge", "keeps the body at zero", "same potential", "prevents a build"]),
                P("the resistor limits the current so that, if the technician touches a live supply, a dangerous current cannot flow through the body to earth (it still lets static leak away slowly)", ["limits the current", "small current", "safe current", "live", "mains", "electric shock", "shock", "slowly"])],
        min_points=2,
        model_answer="The technician's body can become charged by friction with clothing or the chair. If that charge discharged as a spark through a sensitive component it could destroy it. The wrist strap earths the technician so charge leaks away continuously and no potential difference builds up. The resistor limits the current: static charge can still leak away through it, but if the technician accidentally touches a live supply the resistor stops a dangerous current flowing through the body to earth.",
        hints=["How might a person become charged, and why would that matter near delicate electronics?",
               "What does connecting the body to earth achieve?",
               "If the wire were plain copper and the technician touched something live, what would happen? How does a resistor help?"],
        keywords="body charged by friction; spark damages components; strap earths the body; resistor limits current if a live part is touched",
        sample_pass=["The body picks up static by friction and a spark could destroy the chips; the strap lets the charge flow to earth, and the resistor limits the current so the technician is not electrocuted if they touch a live wire",
                     "earthing stops charge building up on the technician; the resistor keeps any current through the body small for safety while still letting static leak away"],
        sample_fail=["The strap stops the technician dropping the board", "The resistor makes the strap heat up to keep the hand warm"])
