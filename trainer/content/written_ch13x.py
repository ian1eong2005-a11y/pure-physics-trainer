"""Chapter 13 Static Electricity written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w13x_electron_proton_charge", 13, 1, "13a",
        stem="State the charge carried by a proton and by an electron.",
        points=[P("proton: positive", ["proton is positive", "proton: positive", "protons are positive", "positive proton", "proton positive"]),
                P("electron: negative", ["electron is negative", "electron: negative", "electrons are negative", "negative electron", "electron negative"])],
        model_answer="A proton is positive (+1.6 × 10⁻¹⁹ C) and an electron is negative (−1.6 × 10⁻¹⁹ C).",
        hints=["Which particle is in the nucleus?", "Which orbits it?", "Give each sign."],
        keywords="proton +; electron −",
        sample_pass=["The proton is positive and the electron is negative", "protons are positive, electrons are negative"],
        sample_fail=["Both are positive", "The proton is negative"])

written("w13x_field_where", 13, 1, "13c",
        stem="State what is meant by an electric field, and what feels a force in it.",
        points=[P("a region where an electric charge experiences a force", ["region", "area", "space"]),
                P("a charge feels the force", ["charge", "charged"])],
        model_answer="An electric field is a region in which an electric charge experiences an electric force.",
        hints=["It is a region.", "What experiences a force?", "A charge."],
        keywords="region where a charge feels a force",
        sample_pass=["A region where a charge experiences a force", "an area in which charged objects feel a force"],
        sample_fail=["A region where a magnet feels a force", "A wire carrying current"])

written("w13x_like_repel", 13, 1, "13b",
        stem="State the rule for the forces between electric charges.",
        points=[P("like charges repel", ["like charges repel", "same charges repel", "like repel"]),
                P("unlike charges attract", ["unlike charges attract", "opposite charges attract", "unlike attract", "opposites attract"])],
        model_answer="Like charges repel; unlike charges attract.",
        hints=["What do two positive charges do?", "And a positive and a negative?", "State both."],
        keywords="like repel; unlike attract",
        sample_pass=["Like charges repel and unlike charges attract", "same charges repel, opposite charges attract"],
        sample_fail=["Like charges attract", "All charges attract"])

written("w13x_two_balls_predict", 13, 1, "13b",
        stem="Two balloons are both rubbed on the same jumper and hung side by side. State and explain what happens.",
        points=[P("they move apart (repel)", ["repel", "move apart", "push apart", "push each other away"]),
                P("because they have the same (like) charge", ["same charge", "like charge", "both negative", "both have the same"])],
        model_answer="They repel and move apart, because they both gain the same type of charge (like charges) from the jumper.",
        hints=["Do they get the same or different charges?", "What do like charges do?", "Predict."],
        keywords="repel; like charges",
        sample_pass=["They repel because they have the same charge", "they move apart since both are negative"],
        sample_fail=["They attract", "Nothing happens"])

written("w13x_charging_friction", 13, 1, "13f",
        stem="State what moves when two insulators are rubbed together and become charged.",
        points=[P("electrons move (are transferred)", ["electrons"]),
                P("from one material to the other", ["from one", "to the other", "from the cloth", "onto the rod", "between"])],
        pitfalls=[PF(["protons"], "Protons stay in the nuclei; only electrons move.")],
        model_answer="Electrons are transferred from one material to the other.",
        hints=["Which particles can move?", "Not protons.", "Electrons."],
        keywords="electrons transferred",
        sample_pass=["Electrons move from one material to the other", "electrons are transferred from the cloth onto the rod"],
        sample_fail=["Protons move", "Heat moves"])

written("w13x_rod_negative_explain", 13, 1, "13f",
        stem="A plastic comb becomes negatively charged when used on dry hair. Explain why.",
        points=[P("electrons move from the hair to the comb", ["from the hair", "to the comb", "gains electrons", "electrons move", "electrons transferred"]),
                P("the comb has more electrons than protons", ["more electrons", "extra electrons", "excess electrons"])],
        model_answer="Friction transfers electrons from the hair to the comb, so the comb has more electrons than protons and is negatively charged.",
        hints=["What moves when rubbing?", "Which way?", "What does extra electrons mean?"],
        keywords="electrons from hair to comb; excess electrons",
        sample_pass=["Electrons move from the hair to the comb, so it has extra electrons", "the comb gains electrons from the hair, so it has extra electrons"],
        sample_fail=["The comb gains protons", "The comb loses electrons"])

written("w13x_field_pattern_negative", 13, 1, "13d",
        stem="Describe the electric field pattern around an isolated negative point charge.",
        points=[P("radial straight lines", ["radial", "straight lines", "spokes"]),
                P("pointing inwards towards the charge", ["inwards", "towards the charge", "into the charge", "pointing in"])],
        model_answer="The field lines are straight and radial, pointing inwards towards the negative charge.",
        hints=["What shape are the lines?", "Which way do they point?", "Towards or away?"],
        keywords="radial; inwards",
        sample_pass=["Radial lines pointing inwards towards the charge", "straight lines like spokes, pointing into the charge"],
        sample_fail=["Lines pointing outwards", "Circles around the charge"],
        figure=lambda: figs3.point_charge_field("-"))

written("w13x_field_line_arrow", 13, 1, "13d",
        stem="State what the arrow on an electric field line shows.",
        points=[P("the direction of the force on a (small) positive charge", ["positive charge", "positive test charge", "force on a positive"])],
        model_answer="It shows the direction of the force that would act on a small positive charge placed on the line.",
        hints=["Imagine a test charge.", "Is it positive or negative?", "Force direction."],
        keywords="force on a positive test charge",
        sample_pass=["The direction of the force on a positive charge", "which way a small positive test charge would be pushed"],
        sample_fail=["The direction electrons move", "The direction of current only"])

# ---------------------------------------------------------------- L2
written("w13x_paper_attract", 13, 2, "13b",
        stem="A charged comb attracts small pieces of neutral paper. Explain why.",
        points=[P("the comb induces an opposite charge on the near side of the paper", ["induce", "opposite charge", "near side", "nearer side", "closest side"]),
                P("the attraction to the near side is stronger than the repulsion from the far side (closer)", ["closer", "stronger", "nearer", "attraction is greater"])],
        model_answer="The comb induces an opposite charge on the near side of the paper (and a like charge on the far side). The near side is closer to the comb, so the attraction is stronger than the repulsion, and the paper is attracted.",
        hints=["Is the paper charged?", "What happens to its charges?", "Which side is closer?"],
        keywords="induced opposite charge near side; closer → stronger attraction",
        sample_pass=["The comb induces an opposite charge on the near side, which is closer, so attraction is stronger", "opposite charge is induced on the nearer side of the paper"],
        sample_fail=["The paper is magnetic", "The paper is positively charged"])

written("w13x_field_two_plates", 13, 2, "13d",
        stem="Describe the electric field between two parallel metal plates, one positive and one negative.",
        points=[P("straight, parallel, evenly spaced lines (uniform field)", ["parallel", "evenly spaced", "uniform", "straight"]),
                P("from the positive plate to the negative plate", ["positive to negative", "from the positive", "towards the negative", "+ to -"])],
        model_answer="Between the plates the field is uniform: the lines are straight, parallel and evenly spaced, pointing from the positive plate to the negative plate.",
        hints=["What do the lines look like?", "How are they spaced?", "Which way do they point?"],
        keywords="uniform, parallel lines; + to −",
        sample_pass=["Parallel evenly spaced lines from the positive plate to the negative plate", "a uniform field from + to -"],
        sample_fail=["Circles around the plates", "From negative to positive"])

written("w13x_cloth_charge", 13, 2, "13f",
        stem="A polythene rod is rubbed with a cloth and gains a charge of −50 nC. State the charge on the cloth and explain.",
        points=[P("+50 nC", ["+50", "50 nc", "positive 50"]),
                P("electrons lost by the cloth were gained by the rod (charge conserved)", ["lost electrons", "electrons from the cloth", "conserved", "equal and opposite", "gained by the rod"])],
        model_answer="The cloth has a charge of +50 nC, because the electrons gained by the rod came from the cloth: charge is conserved, so the charges are equal and opposite.",
        hints=["Where did the rod's electrons come from?", "Is charge created?", "Equal and opposite."],
        keywords="+50 nC; electrons from cloth; conserved",
        sample_pass=["+50 nC because the cloth lost the electrons the rod gained", "positive 50 nC, equal and opposite since charge is conserved"],
        sample_fail=["−50 nC", "0 nC"])

written("w13x_metal_not_charge", 13, 2, "13f",
        stem="Explain why a metal rod held in the hand cannot be charged by rubbing, but can be if it has an insulating handle.",
        points=[P("metal is a conductor, so charge flows through it and the body to earth", ["conductor", "conducts", "flows away", "to earth", "through the body"]),
                P("an insulating handle stops the charge flowing away", ["insulating handle", "insulator", "stops", "cannot flow"])],
        model_answer="Metal is a conductor, so any charge produced flows through the rod and the person's body to earth. With an insulating handle, the charge cannot flow away, so the rod stays charged.",
        hints=["Is metal a conductor?", "Where does the charge go?", "What does an insulating handle do?"],
        keywords="conductor → charge to earth; insulating handle prevents this",
        sample_pass=["Metal conducts the charge through the body to earth; an insulating handle stops it flowing away", "the charge flows away through the hand unless the handle is an insulator"],
        sample_fail=["Metals cannot gain electrons", "Metals are too heavy"])

written("w13x_induction_two_spheres_written", 13, 2, "13g",
        stem="Fig. 1 shows a positively charged rod held near two touching metal spheres. Describe how the spheres can be given opposite charges.",
        points=[P("electrons are attracted to the near sphere", ["electrons are attracted", "electrons move to the near", "near sphere becomes negative", "electrons move towards"]),
                P("separate the spheres while the rod is still near", ["separate", "pull apart", "move apart", "while the rod"]),
                P("then remove the rod: near sphere negative, far sphere positive", ["near sphere negative", "far sphere positive", "remove the rod", "opposite charges"])],
        min_points=2,
        model_answer="The positive rod attracts electrons into the near sphere, leaving the far sphere positive. Separate the spheres while the rod is still near, then remove the rod: the near sphere is negative and the far sphere is positive.",
        hints=["Which way do electrons move?", "When must the spheres be separated?", "What are the final charges?"],
        keywords="electrons attracted to near sphere; separate first; remove rod",
        sample_pass=["Electrons are attracted to the near sphere; separate the spheres then remove the rod, so the near one is negative and the far one positive", "separate them while the rod is near; the near sphere becomes negative"],
        sample_fail=["Touch the rod to the spheres", "Rub the spheres"],
        figure=lambda: figs3.induction_spheres(1, "+"))

written("w13x_induction_no_contact", 13, 2, "13g",
        stem="State what is meant by charging by induction, and why the charged rod keeps its charge.",
        points=[P("charging an object without touching it, by bringing a charged object near", ["without touching", "without contact", "not touching", "near"]),
                P("the rod does not touch, so no charge is transferred from it", ["no charge is transferred", "does not touch", "keeps its charge", "not transferred"])],
        model_answer="Charging by induction means charging a conductor without touching it, by holding a charged object near it. The rod never touches the object, so none of its charge is transferred and it keeps its charge.",
        hints=["Does the rod touch?", "So can charge transfer from it?", "Define induction."],
        keywords="charging without contact; rod keeps its charge",
        sample_pass=["Charging without touching by bringing a charged rod near; the rod does not touch so it keeps its charge", "the object is charged without contact, so no charge is transferred from the rod"],
        sample_fail=["Charging by rubbing", "The rod gives its charge to the sphere"])

written("w13x_coulomb_define", 13, 2, "13a",
        stem="State the SI unit of charge and what it is equal to in terms of current and time.",
        points=[P("the coulomb (C)", ["coulomb"]),
                P("1 C = 1 A × 1 s (the charge passing in 1 s at 1 A)", ["1 a", "ampere", "a s", "a × s", "current × time", "1 s"])],
        model_answer="The coulomb (C); 1 C is the charge that passes a point when a current of 1 A flows for 1 s (1 C = 1 A s).",
        hints=["Name the unit.", "Q = I t.", "Combine the units."],
        keywords="coulomb; 1 C = 1 A s",
        sample_pass=["The coulomb, which is 1 ampere for 1 second", "coulomb: 1 A × 1 s"],
        sample_fail=["The ampere", "The volt"])

written("w13x_electron_count_written", 13, 2, "13a",
        stem="A balloon has a charge of −3.2 × 10⁻⁹ C. Calculate how many extra electrons it carries. (e = 1.6 × 10⁻¹⁹ C)",
        points=[P("n = Q ÷ e", ["q / e", "q ÷ e", "3.2 × 10", "1.6 × 10", "divide"]),
                P("n = 2.0 × 10¹⁰", ["2.0 × 10", "2 × 10", "2.0 x 10", "2 x 10", "20 000 000 000", "2e10"])],
        model_answer="n = Q ÷ e = 3.2 × 10⁻⁹ ÷ 1.6 × 10⁻¹⁹ = 2.0 × 10¹⁰ electrons.",
        hints=["Each electron carries e.", "n = Q ÷ e.", "Standard form."],
        keywords="n = Q ÷ e = 2.0 × 10¹⁰",
        sample_pass=["n = Q ÷ e = 2.0 × 10¹⁰", "3.2 × 10⁻⁹ / 1.6 × 10⁻¹⁹ = 2 × 10¹⁰ electrons"],
        sample_fail=["5.1 × 10⁻²⁸", "200"])

# ---------------------------------------------------------------- L3
written("w13x_rubbing_both_written", 13, 3, "13f",
        stem="Explain, in terms of electrons, why a rod and the cloth used to rub it end up with equal and opposite charges.",
        points=[P("electrons are transferred from one to the other", ["transferred", "move from", "lost by", "gained by"]),
                P("the number lost by one equals the number gained by the other (charge conserved)", ["number lost", "equal number", "same number", "conserved", "as many"])],
        model_answer="During rubbing, electrons are transferred from one object to the other. The number of electrons lost by one equals the number gained by the other, because charge is conserved, so the charges are equal in size and opposite in sign.",
        hints=["What moves?", "Are electrons created or destroyed?", "So how do the charges compare?"],
        keywords="electrons transferred; number lost = number gained",
        sample_pass=["Electrons are transferred, and the number lost by one equals the number gained by the other", "charge is conserved, so the electrons lost by the cloth are gained by the rod"],
        sample_fail=["Both gain electrons", "Protons move"])

written("w13x_induction_earth_written", 13, 3, "13g",
        stem="Describe how to charge a single insulated metal sphere positively using a negatively charged rod and an earth connection.",
        points=[P("hold the negative rod near the sphere", ["hold the rod near", "bring the rod near", "rod near"]),
                P("earth the sphere: electrons are repelled and flow to earth", ["earth", "touch", "flow to earth", "repelled"]),
                P("remove the earth connection, then remove the rod", ["remove the earth", "then remove the rod", "earth first", "before the rod"])],
        min_points=2,
        model_answer="Hold the negatively charged rod near the sphere. Touch the sphere briefly (earth it): electrons are repelled and flow away to earth. Remove the earth connection, then remove the rod; the sphere is left positively charged.",
        hints=["Where is the rod placed?", "Which way do electrons flow when earthed?", "In which order are things removed?"],
        keywords="rod near; earth → electrons to earth; remove earth then rod",
        sample_pass=["Hold the rod near, earth the sphere so electrons flow to earth, remove the earth then the rod", "bring the rod near, touch the sphere, then remove the finger before the rod"],
        sample_fail=["Touch the rod to the sphere", "Rub the sphere with the rod"])

written("w13x_lightning_conductor_written", 13, 3, "13h",
        stem="Explain how a lightning conductor protects a tall building.",
        points=[P("it is a thick metal strip from the top of the building to the ground", ["metal", "copper", "strip", "rod", "conductor"]),
                P("it provides an easy (low-resistance) path for charge to flow to earth", ["low resistance", "easy path", "to earth", "to the ground", "conducts"]),
                P("so the charge does not pass through the building, preventing damage or fire", ["not through the building", "prevents damage", "protects", "safely", "fire"])],
        min_points=2,
        model_answer="A lightning conductor is a thick metal strip running from the top of the building to the ground. It provides a low-resistance path, so charge from a lightning strike flows safely to earth instead of through the building, preventing damage and fires.",
        hints=["What is it made of?", "Where does it lead?", "What does it prevent?"],
        keywords="metal strip to ground; low-resistance path; protects building",
        sample_pass=["A copper strip gives an easy path for the charge to flow to the ground safely", "a metal conductor carries the lightning safely to earth, protecting the building"],
        sample_fail=["It stops lightning from forming", "It stores the charge"])

written("w13x_tanker_written", 13, 3, "13h",
        stem="Explain why a fuel tanker must be connected to earth before fuel is pumped out.",
        points=[P("fuel flowing through the pipes causes friction, building up charge", ["friction", "rubbing", "builds up", "charge builds"]),
                P("a spark could ignite the fuel vapour and cause an explosion", ["spark", "ignite", "explosion", "fire"]),
                P("earthing lets the charge flow safely away", ["flow to earth", "earthing", "flows away", "safely"])],
        min_points=2,
        model_answer="Friction between the flowing fuel and the pipes builds up charge on the tanker. If enough builds up, a spark could jump and ignite the fuel vapour, causing an explosion. Earthing lets the charge flow safely away to earth.",
        hints=["How does charge build up?", "What is the danger?", "How does earthing help?"],
        keywords="friction → charge; spark ignites vapour; earthing removes charge",
        sample_pass=["Friction builds up charge which could cause a spark and explosion, so earthing lets it flow away", "a spark could ignite the fuel; the earth wire removes the charge safely"],
        sample_fail=["To stop the fuel spilling", "To keep the fuel cold"])

written("w13x_precipitator_written", 13, 3, "13i",
        stem="Fig. 1 shows an electrostatic precipitator. Describe how it cleans the waste gases from a chimney.",
        points=[P("the smoke/ash particles pass through charged wires/grid and become charged", ["charged", "become charged", "gain charge", "wire", "grid"]),
                P("they are attracted to the oppositely charged (earthed) plates", ["attracted", "opposite", "plates", "earthed"]),
                P("the plates are knocked/shaken so the ash falls and is collected", ["shaken", "knocked", "falls", "collected", "tapped"])],
        min_points=2,
        model_answer="The ash particles pass through a charged wire grid and become charged. They are then attracted to the oppositely charged (earthed) collecting plates, where they stick. The plates are knocked regularly so the ash falls into a hopper and is collected.",
        hints=["What happens to the particles first?", "What attracts them?", "How is the ash removed?"],
        keywords="particles charged; attracted to plates; ash shaken off",
        sample_pass=["The particles become charged and are attracted to the oppositely charged plates, which are shaken to collect the ash", "charged ash sticks to the earthed plates"],
        sample_fail=["It filters smoke through cloth", "It burns the smoke"],
        figure=lambda: figs3.precipitator())

written("w13x_photocopier_written", 13, 3, "13i",
        stem="Outline how static electricity is used in a photocopier.",
        points=[P("a drum is charged and an image of the page is projected onto it", ["drum", "charged", "image", "projected"]),
                P("light discharges the white areas, leaving charge where the dark parts are", ["light discharges", "discharged", "white areas", "dark", "charge remains"]),
                P("toner is attracted to the charged areas and transferred to paper, then heated", ["toner", "attracted", "paper", "heated", "fixed"])],
        min_points=2,
        model_answer="A drum is charged and an image of the page is projected onto it. Light discharges the areas matching the white parts, so charge remains where the page is dark. Oppositely charged toner powder sticks to the charged areas and is transferred onto paper, where it is fixed by heating.",
        hints=["What is charged first?", "What does light do?", "How does the toner end up on the paper?"],
        keywords="charged drum; light discharges white areas; toner attracted to charged areas",
        sample_pass=["The drum is charged, light discharges the white areas, and toner is attracted to the charged dark areas then put on paper", "toner sticks to the parts of the drum that are still charged"],
        sample_fail=["It uses magnets to print", "It uses ink jets"])

written("w13x_field_definition_written", 13, 3, "13c",
        stem="Explain how you could show that there is an electric field around a charged dome, without touching the dome.",
        points=[P("bring a small charged object (test charge) near the dome", ["small charged", "test charge", "charged ball", "charged object"]),
                P("it experiences a force (moves/deflects) even without contact", ["force", "deflects", "moves", "attracted", "repelled"])],
        model_answer="Bring a small charged object, such as a charged ball on a thread, near the dome. If it experiences a force and is deflected without touching the dome, there must be an electric field around the dome.",
        hints=["What does an electric field act on?", "How could you see the force?", "No contact needed."],
        keywords="test charge near dome; experiences a force",
        sample_pass=["Bring a small charged ball near; it feels a force and is deflected", "a test charge near the dome will be attracted or repelled"],
        sample_fail=["Use a compass", "Measure its temperature"])

written("w13x_field_noncontact", 13, 3, "13c",
        stem="Explain why the electric force is described as a non-contact force.",
        points=[P("charges exert forces on each other without touching", ["without touching", "without contact", "at a distance", "not touching"]),
                P("through the electric field around each charge", ["field", "electric field"])],
        model_answer="Charged objects exert forces on each other without touching, because each charge is surrounded by an electric field that acts on other charges at a distance.",
        hints=["Do the charges need to touch?", "What carries the force?", "Name it."],
        keywords="acts at a distance; via electric field",
        sample_pass=["Charges exert forces without touching through their electric fields", "the force acts at a distance through the field"],
        sample_fail=["It needs a wire", "It only acts when objects touch"])

# ---------------------------------------------------------------- L4
written("w13x_aircraft_refuel_written", 13, 4, "13h",
        stem="Explain why aircraft are connected to earth by a cable while being refuelled.",
        points=[P("friction between flowing fuel and the hose/air builds up charge on the aircraft", ["friction", "builds up", "charge"]),
                P("a spark could ignite the fuel vapour", ["spark", "ignite", "explosion", "fire"]),
                P("the cable conducts the charge safely to earth", ["cable", "conducts", "to earth", "flows away", "safely"])],
        min_points=2,
        model_answer="As fuel flows through the hose, friction builds up charge on the aircraft (which also gains charge from friction with the air in flight). A spark could ignite the fuel vapour, so the earthing cable conducts the charge safely to earth.",
        hints=["How does charge build up?", "What is the risk?", "What does the cable do?"],
        keywords="friction → charge; spark → ignition; cable to earth",
        sample_pass=["Friction from the fuel builds up charge that could make a spark ignite the fuel; the cable lets it flow to earth", "the earth cable removes static charge so no spark occurs"],
        sample_fail=["To stop the plane moving", "To measure the fuel"])

written("w13x_paint_spray_written", 13, 4, "13i",
        stem="Explain how electrostatic spraying gives a car an even coat of paint with little waste.",
        points=[P("the paint droplets are given the same charge, so they repel and spread out", ["repel", "spread out", "same charge", "fine spray"]),
                P("the car is given the opposite charge (or earthed), so the droplets are attracted to it", ["opposite charge", "attracted", "earthed"]),
                P("droplets reach hidden surfaces and less paint misses the car", ["hidden", "even", "less waste", "all surfaces", "behind"])],
        min_points=2,
        model_answer="The paint droplets are all given the same charge, so they repel each other and spread into a fine, even spray. The car is given the opposite charge (or earthed), so the droplets are attracted to it, even reaching hidden surfaces, and little paint misses the car.",
        hints=["How are the droplets charged?", "How is the car charged?", "Why is there less waste?"],
        keywords="droplets same charge → spread; car opposite → attraction; even coat, less waste",
        sample_pass=["The droplets have the same charge so they spread out, and the oppositely charged car attracts them, so less is wasted", "the car is earthed so the charged paint is attracted to all surfaces"],
        sample_fail=["The paint is heated", "Magnets pull the paint"])

written("w13x_induction_electron_flow", 13, 4, "13g",
        stem="When a positively charged rod is held near an earthed metal sphere, the sphere becomes negatively charged. Explain the movement of electrons.",
        points=[P("the positive rod attracts electrons", ["attracts electrons", "electrons are attracted"]),
                P("electrons flow from the earth into the sphere", ["from the earth", "from earth", "into the sphere", "up from"])],
        model_answer="The positive rod attracts electrons, so electrons flow up from the earth into the sphere. When the earth connection is removed (before the rod), the sphere keeps these extra electrons and is negative.",
        hints=["Does a positive rod attract or repel electrons?", "Where can extra electrons come from?", "Via the earth."],
        keywords="rod attracts electrons; electrons flow from earth into sphere",
        sample_pass=["The positive rod attracts electrons which flow from the earth into the sphere", "electrons are attracted up from earth into the sphere"],
        sample_fail=["Protons flow out of the sphere", "Electrons flow from the rod"])

written("w13x_induction_why_conductor", 13, 4, "13g",
        stem="Explain why charging by induction works with a metal sphere but not with a plastic sphere.",
        points=[P("metal has free electrons that can move through it", ["free electrons", "electrons can move", "electrons are free", "conductor"]),
                P("in plastic (an insulator) electrons cannot move, so charges cannot separate or flow to earth", ["insulator", "cannot move", "fixed", "cannot flow"])],
        model_answer="Metal is a conductor with free electrons, which can move through it so the charges separate and can flow to or from earth. Plastic is an insulator: its electrons cannot move freely, so induction does not work.",
        hints=["What must move for induction?", "Can it move in metal?", "In plastic?"],
        keywords="metal: free electrons move; plastic: electrons fixed",
        sample_pass=["Metal has free electrons that can move, but in plastic the electrons cannot move", "metal is a conductor, but plastic is an insulator so the charges cannot separate"],
        sample_fail=["Plastic is too light", "Metal is magnetic"])

written("w13x_field_two_like", 13, 4, "13d",
        stem="Two equal positive charges are placed near each other. Describe the electric field pattern between them.",
        points=[P("field lines point away from both charges", ["away from both", "outwards", "from both"]),
                P("the lines curve away from each other and do not join", ["curve away", "do not join", "repel", "bend away"]),
                P("there is a neutral point midway where the field is zero", ["neutral point", "zero", "midway", "no field"])],
        min_points=2,
        model_answer="The lines point away from both charges and curve away from each other without joining. Midway between them there is a neutral point where the field is zero.",
        hints=["Which way do lines point from + charges?", "Do lines join between like charges?", "Is there a point of zero field?"],
        keywords="outwards from both; curve away; neutral point midway",
        sample_pass=["The lines go outwards from both charges and curve away, with a neutral point in the middle", "away from both, not joining; zero field midway"],
        sample_fail=["Lines go from one charge to the other", "Circles around both charges"],
        figure=lambda: figs3.two_charges_field(("+", "+")))

written("w13x_field_strength_lines", 13, 4, "13d",
        stem="Explain how a field-line diagram shows where an electric field is strongest.",
        points=[P("the field is strongest where the lines are closest together", ["closest", "closer together", "most concentrated", "densest", "close together"]),
                P("e.g. near the charges / where the lines converge", ["near the charge", "near the charges", "converge", "close to"])],
        min_points=1,
        model_answer="The field is strongest where the field lines are closest together, for example near the charges where the lines crowd together.",
        hints=["What does the spacing of lines show?", "Close lines…", "…strong field."],
        keywords="closest lines = strongest field",
        sample_pass=["Where the lines are closest together, near the charges", "the field is strongest where the lines are most concentrated"],
        sample_fail=["Where the lines are far apart", "Where there are no lines"])

written("w13x_rubbing_series_explain", 13, 4, "13f",
        stem="When glass is rubbed with silk, the glass becomes positive. When polythene is rubbed with silk, the polythene becomes negative. Explain what this shows about how easily these materials lose electrons.",
        points=[P("glass loses electrons more easily than silk", ["glass loses electrons", "glass gives up electrons", "glass loses"]),
                P("silk loses electrons more easily than polythene (polythene gains them)", ["polythene gains", "silk loses electrons to polythene", "polythene holds electrons", "silk gives electrons"]),
                P("so the order is glass, silk, polythene", ["glass, silk, polythene", "order", "series"])],
        min_points=2,
        model_answer="Glass becomes positive, so it loses electrons to silk: glass loses electrons more easily than silk. Polythene becomes negative, so it gains electrons from silk: silk loses electrons more easily than polythene. The order (most easily losing first) is glass, silk, polythene.",
        hints=["Which loses electrons in each pair?", "Positive means lost electrons.", "Put them in order."],
        keywords="glass loses to silk; silk loses to polythene; order glass, silk, polythene",
        sample_pass=["Glass loses electrons to silk, and polythene gains electrons from silk, so the order is glass, silk, polythene", "glass loses electrons more easily than silk; polythene gains them"],
        sample_fail=["Silk is always positive", "Protons move from the glass"])

written("w13x_humidity_static", 13, 4, "13f",
        stem="Experiments with static electricity work poorly on humid days. Explain why.",
        points=[P("water vapour in the air makes the air (and surfaces) slightly conducting", ["water", "moisture", "conduct", "conducting"]),
                P("so charge leaks away from the charged objects", ["leaks", "leak away", "flows away", "lost", "escapes"])],
        model_answer="On humid days a thin layer of moisture forms on surfaces and the air contains more water vapour, which slightly conducts. Charge therefore leaks away from the objects, so they do not stay charged.",
        hints=["What is in humid air?", "Does it conduct?", "What happens to the charge?"],
        keywords="moisture conducts; charge leaks away",
        sample_pass=["Moisture in the air conducts, so the charge leaks away", "water on surfaces lets the charge flow away"],
        sample_fail=["Humid air is too hot", "Rubbing creates no electrons when it is humid"])

# ---------------------------------------------------------------- L5
written("w13x_eval_charge_new", 13, 5, "13b",
        stem="A student says: 'When I rub a balloon on my hair, I create negative charge.' Evaluate this statement.",
        points=[P("the statement is wrong: charge is not created", ["wrong", "not created", "incorrect", "cannot be created"]),
                P("electrons are transferred from the hair to the balloon", ["transferred", "from the hair", "to the balloon", "electrons move"]),
                P("the hair becomes equally positive, so the total charge is still zero", ["hair becomes positive", "equal", "total is zero", "conserved", "hair positive"])],
        min_points=2,
        model_answer="The statement is wrong: charge is not created. Electrons are transferred from the hair to the balloon, so the balloon becomes negative and the hair becomes equally positive; the total charge remains zero (charge is conserved).",
        hints=["Can charge be created?", "What actually moves?", "What happens to the hair?"],
        keywords="wrong; electrons transferred; hair equally positive",
        sample_pass=["Wrong, charge is not created; electrons are transferred from the hair, which becomes positive", "incorrect: charge is conserved, electrons move from hair to balloon"],
        sample_fail=["Correct, rubbing makes charge", "The balloon gains protons"])

written("w13x_eval_static_design_floor", 13, 5, "13h",
        stem="In a hospital operating theatre, floors are made slightly conducting and staff wear conducting shoes. Evaluate why this is done.",
        points=[P("static charge could build up on people and equipment by friction", ["build up", "friction", "static"]),
                P("a spark could ignite flammable gases (e.g. oxygen, anaesthetics) or damage equipment", ["spark", "ignite", "explosion", "fire", "flammable", "damage"]),
                P("conducting floors and shoes let charge flow safely to earth", ["conducting", "flow to earth", "earth", "safely"])],
        min_points=2,
        model_answer="Friction can build up static charge on people and equipment. A spark could ignite flammable gases such as oxygen or anaesthetics, or damage sensitive equipment. Conducting floors and shoes let the charge flow safely to earth, so it never builds up.",
        hints=["How could charge build up?", "Why are sparks dangerous here?", "How do the floors help?"],
        keywords="charge builds up; sparks ignite gases; conduct charge to earth",
        sample_pass=["Charge could build up and a spark could ignite the oxygen, so the conducting floor lets it flow to earth", "to prevent sparks by letting static flow away to earth"],
        sample_fail=["To keep the floor clean", "To make the floor warm"])

written("w13x_eval_precipitator_design", 13, 5, "13i",
        stem="A factory's electrostatic precipitator removes only 70% of the ash. Suggest and explain two changes to improve it.",
        points=[P("use larger collecting plates / more plates", ["larger plates", "more plates", "bigger plates", "larger area"]),
                P("increase the charge given to the particles (higher voltage)", ["higher voltage", "more charge", "stronger charge", "increase the charge"]),
                P("slow the gas flow so particles spend longer between the plates / knock plates more often", ["slow", "longer", "knock", "shake", "clean the plates"])],
        min_points=2,
        model_answer="Use larger (or more) collecting plates so more particles reach a plate, and use a higher voltage to give the particles more charge so they are attracted more strongly. Slowing the gas flow gives the particles longer between the plates, and knocking the plates more often stops the ash layer building up.",
        hints=["What attracts the particles?", "How could the attraction be stronger?", "How long are the particles between the plates?"],
        keywords="larger plates; more charge/higher voltage; slower gas flow",
        sample_pass=["Use larger plates and a higher voltage so the particles are more strongly charged and attracted", "slow the gas flow and increase the charge on the particles"],
        sample_fail=["Make the chimney taller", "Heat the gas more"])

written("w13x_eval_spray_crop", 13, 5, "13i",
        stem="Farmers can spray crops with charged droplets of pesticide. Evaluate the advantages of charging the droplets.",
        points=[P("droplets with the same charge repel and spread out evenly", ["repel", "spread", "evenly", "same charge"]),
                P("they are attracted to the plants (induced charge), covering the undersides of leaves", ["attracted", "induced", "underside", "both sides", "all surfaces"]),
                P("less pesticide is wasted / drifts away, reducing cost and pollution", ["less waste", "less pesticide", "less drift", "pollution", "cheaper"])],
        min_points=2,
        model_answer="Droplets with the same charge repel each other and spread out evenly. They are attracted to the plants by induced charges, so they coat all surfaces, even the undersides of leaves. Less pesticide is wasted or drifts away, reducing cost and pollution.",
        hints=["What do like-charged droplets do?", "Why are they attracted to plants?", "What are the benefits?"],
        keywords="spread evenly; attracted to plants; less waste/drift",
        sample_pass=["The droplets repel and spread evenly, are attracted to the leaves, so less pesticide is wasted", "even coverage of both sides of the leaves and less drift"],
        sample_fail=["The pesticide becomes stronger", "Charged droplets kill more insects by shock"])

written("w13x_eval_induction_claim_written", 13, 5, "13g",
        stem="A student says: 'In charging by induction, the rod's charge jumps across to the sphere.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("the rod does not touch or lose charge", ["does not touch", "no contact", "keeps its charge", "does not lose"]),
                P("the charges in the sphere separate, and electrons flow to or from earth", ["separate", "earth", "electrons flow", "electrons move"]),
                P("the sphere ends with the opposite charge to the rod", ["opposite charge", "opposite sign"])],
        min_points=2,
        model_answer="The statement is wrong. The rod does not touch the sphere and keeps all its charge. Its field makes the charges in the sphere separate, and when the sphere is earthed electrons flow to or from earth, so the sphere ends with the opposite charge to the rod.",
        hints=["Does the rod touch the sphere?", "Where do electrons come from?", "What is the final sign?"],
        keywords="wrong; rod keeps charge; charges separate, flow via earth; opposite charge",
        sample_pass=["Wrong, the rod does not touch so it keeps its charge; electrons flow to or from earth, giving the opposite charge", "incorrect: the sphere's charges separate and it ends with the opposite sign"],
        sample_fail=["Correct, charge jumps from the rod", "The sphere gets the same charge"])

written("w13x_eval_induction_test", 13, 5, "13g",
        stem="After charging a sphere by induction with a negative rod, a student wants to check that it is positive. Evaluate two possible tests.",
        points=[P("bringing a known positive object near: repulsion proves the sphere is positive", ["known positive", "positive rod", "repel", "repulsion"]),
                P("attraction to a negative object is not proof, since neutral objects are also attracted", ["attraction is not proof", "neutral objects are attracted", "not proof", "could be neutral"]),
                P("a gold-leaf electroscope or charge sensor could also show the sign", ["electroscope", "sensor", "coulombmeter", "meter"])],
        min_points=2,
        model_answer="Bringing a known positively charged object near is a good test: repulsion proves the sphere is positive. Seeing it attracted to a negative rod is not proof, because neutral objects are also attracted by induction. A charge sensor (coulombmeter) or electroscope could also confirm the sign.",
        hints=["Which effect only happens with a charge?", "Why is attraction not proof?", "Is there an instrument?"],
        keywords="repulsion by known + proves it; attraction not proof; sensor/electroscope",
        sample_pass=["Repulsion from a known positive rod proves it is positive, but attraction to a negative rod is not proof", "use a coulombmeter, or check that it repels a positive object"],
        sample_fail=["Touch it to feel a shock", "Weigh it"])

written("w13x_eval_field_vs_gravity_written", 13, 5, "13c",
        stem="Compare an electric field with a gravitational field, giving one similarity and two differences.",
        points=[P("similarity: both are regions where a force acts at a distance (non-contact)", ["both", "at a distance", "non-contact", "region"]),
                P("electric fields act on charges; gravitational fields act on masses", ["charges", "masses", "mass"]),
                P("electric forces can attract or repel; gravity only attracts", ["repel", "only attracts", "attract or repel"])],
        min_points=2,
        model_answer="Both are regions in which a force acts at a distance without contact. However, an electric field acts on charges while a gravitational field acts on masses, and electric forces can attract or repel while gravity only attracts.",
        hints=["How are they similar?", "What does each act on?", "Can each repel?"],
        keywords="both non-contact regions; charge vs mass; repel vs only attract",
        sample_pass=["Both act at a distance, but electric fields act on charges and can repel, while gravity acts on masses and only attracts", "both are non-contact; gravity only attracts"],
        sample_fail=["They are exactly the same", "Gravity acts on charges"])

written("w13x_eval_field_mapping", 13, 5, "13c",
        stem="A student uses a large charged ball to investigate the field around a charged dome. Evaluate this method.",
        points=[P("a large charge has its own strong field that changes (distorts) the field being measured", ["its own field", "distort", "changes the field", "affects the field", "alters"]),
                P("a small test charge should be used instead", ["small test charge", "small charge", "smaller"])],
        model_answer="It is a poor method: a large charged ball has its own strong electric field, which would alter the field being measured (and could even change the charge on the dome). A very small test charge should be used.",
        hints=["Does the ball have its own field?", "Would it change what is measured?", "What should be used?"],
        keywords="large charge distorts field; use small test charge",
        sample_pass=["A large charge distorts the field it is measuring, so a small test charge should be used", "its own field changes the field; use a smaller charge"],
        sample_fail=["It is a perfect method", "Large charges have no field"])
