"""Chapter 4 Turning Effects of Forces written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs2
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w4x_moment_formula", 4, 1, "4b",
        stem="Write down the equation for the moment of a force about a pivot, saying what each term means.",
        points=[P("moment = force × perpendicular distance", ["force × perpendicular distance", "force x perpendicular distance", "force times perpendicular distance", "f × d", "f x d", "moment = f d"]),
                P("distance is from the pivot to the line of action of the force", ["from the pivot", "to the line of action", "line of action", "from the pivot to the force"])],
        model_answer="Moment = force × perpendicular distance, where the distance is measured from the pivot to the line of action of the force.",
        hints=["Which two quantities are multiplied?", "Which distance is used?", "From the pivot to the line of action."],
        keywords="moment = force × perpendicular distance from pivot to line of action",
        sample_pass=["Moment = force × perpendicular distance from the pivot to the line of action of the force", "moment = F x d, where d is the perpendicular distance from the pivot to the force"],
        sample_fail=["Moment = mass × acceleration", "Moment = force ÷ area"])

written("w4x_equilibrium_two_conditions", 4, 1, "4c",
        stem="State the two conditions for a body to be in equilibrium.",
        points=[P("the resultant force is zero", ["resultant force is zero", "resultant force zero", "no resultant force", "net force is zero", "forces are balanced", "forces balance"]),
                P("the resultant moment is zero (clockwise moments = anticlockwise moments)", ["resultant moment is zero", "no resultant moment", "clockwise moments equal anticlockwise", "clockwise moment equals anticlockwise", "moments balance", "moments are balanced", "net moment is zero"])],
        model_answer="The resultant force on the body is zero, and the resultant moment about any point is zero (the sum of clockwise moments equals the sum of anticlockwise moments).",
        hints=["One condition stops it accelerating.", "The other stops it turning.", "Forces and moments."],
        keywords="resultant force zero; resultant moment zero",
        sample_pass=["The resultant force is zero and the resultant moment is zero", "forces balance and clockwise moments equal anticlockwise moments"],
        sample_fail=["It must be stationary on the floor", "All the forces must be the same size"])

written("w4x_cg_uniform_shapes", 4, 1, "4e",
        stem="State where the centre of gravity is for (a) a uniform metre rule and (b) a uniform rectangular sheet.",
        points=[P("rule: at its midpoint (50 cm mark)", ["50 cm", "midpoint", "middle of the rule", "centre of the rule", "half way"]),
                P("sheet: where the diagonals cross (its centre)", ["diagonals cross", "diagonals meet", "intersection of the diagonals", "centre of the sheet", "middle of the sheet", "centre of the rectangle"])],
        model_answer="(a) At the midpoint, the 50 cm mark. (b) At the centre of the sheet, where its diagonals cross.",
        hints=["Uniform means the mass is spread evenly.", "Think of the middle.", "For a rectangle, use the diagonals."],
        keywords="midpoint (50 cm); where the diagonals cross",
        sample_pass=["(a) at the 50 cm mark (b) where the diagonals cross", "the midpoint of the rule and the centre of the sheet"],
        sample_fail=["at one end of each", "at the bottom edge"])

written("w4x_two_stability_factors", 4, 1, "4f",
        stem="State two ways of making an object more stable.",
        points=[P("lower its centre of gravity", ["lower its centre of gravity", "lower the centre of gravity", "low centre of gravity", "lower centre of gravity", "mass at the bottom", "heavier base"]),
                P("widen its base", ["wider base", "widen the base", "wide base", "larger base", "bigger base", "base wider"])],
        model_answer="Lower its centre of gravity (for example by putting more mass near the bottom) and make its base wider.",
        hints=["Think of a racing car.", "Where is its mass? How wide is it?", "Low G, wide base."],
        keywords="lower centre of gravity; wider base",
        sample_pass=["Lower the centre of gravity and make the base wider", "give it a heavier base and a larger base area"],
        sample_fail=["Make it taller", "Paint it a darker colour"])

written("w4x_topple_rule", 4, 1, "4f",
        stem="When will a tilted object topple over?",
        points=[P("when the line of action of its weight (through G) falls outside the base", ["outside the base", "outside its base", "beyond the base", "past the edge of the base", "beyond the edge"]),
                P("the weight then has a moment that turns it further over", ["moment", "turns it over", "turning effect", "tips it over", "turns it further"])],
        model_answer="It topples when the vertical line through its centre of gravity falls outside its base, because the weight then has a moment about the edge that turns it further over.",
        hints=["Where does the weight act?", "Compare the weight's line with the base.", "Outside the base → it tips."],
        keywords="weight's line of action outside base → moment tips it over",
        sample_pass=["When the weight acts outside the base, so its moment turns it over", "when the line through the centre of gravity is beyond the edge of the base, giving a turning effect"],
        sample_fail=["When it is pushed", "When it is heavy"])

# ---------------------------------------------------------------- L2
written("w4x_unit_and_vector", 4, 2, "4b",
        stem="A force of 30 N acts at right angles to a lever, 0.40 m from the pivot. Calculate the moment and give its unit.",
        points=[P("moment = 30 × 0.40 = 12", ["12"]),
                P("unit N m", ["n m", "nm", "newton metre", "newton metres"])],
        pitfalls=[PF(["75"], "Multiply force by distance; do not divide.")],
        model_answer="Moment = 30 × 0.40 = 12 N m.",
        hints=["Moment = F × d.", "Use metres.", "Give the unit."],
        keywords="M = F d = 12 N m",
        sample_pass=["12 N m", "moment = 30 x 0.40 = 12 newton metres"],
        sample_fail=["75 N", "30.4 N"])

written("w4x_seesaw_explain", 4, 2, "4d",
        stem="A heavy adult and a light child want to balance on a see-saw. Explain where each should sit.",
        points=[P("the adult sits closer to the pivot", ["adult closer to the pivot", "adult nearer the pivot", "adult sits closer", "heavier person closer", "heavy one closer", "adult near the pivot"]),
                P("so that the moments (W × d) on each side are equal", ["moments are equal", "moments equal", "moments balance", "equal moments", "clockwise moment equals anticlockwise", "principle of moments"])],
        model_answer="The adult should sit closer to the pivot and the child further away, so that the adult's weight × distance equals the child's weight × distance and the moments balance.",
        hints=["Which person has the larger weight?", "Moment = W × d.", "Make the moments equal."],
        keywords="heavier person closer to pivot; moments equal",
        sample_pass=["The adult sits closer to the pivot so that the moments are equal", "the heavy one closer and the child far away so the moments balance"],
        sample_fail=["They sit at equal distances", "The child sits closer to the pivot"])

written("w4x_cg_lamina_steps", 4, 2, "4e",
        stem="Outline how you would find the centre of gravity of an irregular piece of card using a plumb line.",
        points=[P("hang the card from a pin so it swings freely", ["hang", "swings freely", "suspend", "from a pin", "pin through a hole"]),
                P("hang a plumb line from the pin and draw the vertical line on the card", ["plumb line", "draw the line", "mark the line", "trace the line", "vertical line"]),
                P("repeat from another hole; G is where the lines cross", ["repeat", "another hole", "second hole", "lines cross", "intersection", "where they meet", "lines meet"])],
        min_points=2,
        model_answer="Hang the card from a pin through a hole so it swings freely. Hang a plumb line from the same pin and draw its vertical line on the card. Repeat from a second hole: the centre of gravity is where the two lines cross.",
        hints=["How is the card supported?", "What does the plumb line show?", "Why use a second hole?"],
        keywords="hang freely; plumb line; repeat; intersection",
        sample_pass=["Hang the card from a pin, use a plumb line to draw a vertical line, repeat from another hole, the lines cross at G", "suspend it so it swings freely and trace the plumb line; do this from a second hole and the intersection is the centre of gravity"],
        sample_fail=["Weigh the card", "Cut it in half"])

written("w4x_racing_car", 4, 2, "4f",
        stem="Racing cars are built very low and with wheels far apart. Explain how this makes them more stable.",
        points=[P("low centre of gravity", ["low centre of gravity", "lower centre of gravity", "centre of gravity is low", "low g"]),
                P("wide base", ["wide base", "wider base", "wheels far apart", "wide wheel base", "wide wheelbase"]),
                P("must tilt a large angle before the weight acts outside the base", ["large angle", "tilt more", "further before", "outside the base", "tilted further", "big tilt"])],
        min_points=2,
        model_answer="Being low gives a low centre of gravity and the wheels far apart give a wide base, so the car must tilt through a large angle before the line of its weight falls outside the base and it topples.",
        hints=["What does 'low' do to G?", "What do wide wheels do to the base?", "Link both to toppling."],
        keywords="low G; wide base; large tilt needed before weight outside base",
        sample_pass=["It has a low centre of gravity and a wide base so it must tilt a large angle before toppling", "the wheels far apart and low centre of gravity mean the weight stays inside the base"],
        sample_fail=["It is fast", "It is light"])

written("w4x_bottle_full_empty", 4, 2, "4f",
        stem="A plastic bottle with water in the bottom half is harder to knock over than the same bottle when empty. Explain why.",
        points=[P("the water lowers the centre of gravity", ["lowers the centre of gravity", "lower centre of gravity", "centre of gravity is lower", "centre of gravity lower", "low centre of gravity"]),
                P("so a larger tilt is needed before the weight acts outside the base", ["larger tilt", "tilt further", "larger angle", "outside the base", "more before toppling", "tilted more"])],
        model_answer="The water at the bottom lowers the centre of gravity, so the bottle must be tilted further before the line of its weight falls outside the base.",
        hints=["Where is most of the mass now?", "What happens to G?", "Link to the tilt needed to topple."],
        keywords="water lowers G; larger tilt needed",
        sample_pass=["The water lowers the centre of gravity so it must tilt further before toppling", "the centre of gravity is lower, so a larger angle is needed before the weight is outside the base"],
        sample_fail=["The water makes it heavier so gravity holds it down", "Water is sticky"])

# ---------------------------------------------------------------- L3
written("w4x_angled_push", 4, 3, "4b",
        stem="A student pushes on a door at its handle, but at an angle to the door rather than at right angles. Explain why the door is harder to open.",
        points=[P("the perpendicular distance from the hinge to the line of action is smaller", ["perpendicular distance is smaller", "perpendicular distance smaller", "smaller perpendicular distance", "perpendicular distance decreases", "perpendicular distance is less", "less perpendicular distance"]),
                P("so the moment is smaller for the same force", ["moment is smaller", "smaller moment", "less moment", "moment decreases", "moment is less", "less turning effect"])],
        model_answer="When pushed at an angle, the perpendicular distance from the hinge is smaller (the line of action of the force passes closer to the hinge), so the same force produces a smaller moment.",
        hints=["Which distance is used for a moment?", "What happens to it when the push is at an angle?", "Link to the moment."],
        keywords="perpendicular distance smaller → moment smaller",
        sample_pass=["The perpendicular distance from the hinge is smaller so the moment is smaller", "less perpendicular distance means a smaller turning effect for the same force"],
        sample_fail=["The force is bigger at an angle", "The door is heavier"])

written("w4x_cg_hang_rest", 4, 3, "4e",
        stem="A picture frame hangs from a single nail and comes to rest. Explain why its centre of gravity is directly below the nail.",
        points=[P("if G is not below the nail, its weight has a moment about the nail", ["moment about the nail", "has a moment", "turning effect", "turns it", "weight has a moment"]),
                P("it swings until the weight acts through the nail, so the moment is zero", ["moment is zero", "zero moment", "no moment", "through the nail", "through the pivot", "directly below"])],
        model_answer="If the centre of gravity is not directly below the nail, the weight has a moment about the nail that turns the frame. It swings until the weight acts vertically through the nail, where its moment is zero and it is in equilibrium.",
        hints=["Where does the weight act?", "What happens if it is to one side of the nail?", "When is the moment zero?"],
        keywords="weight has a moment unless G below nail; rest when moment zero",
        sample_pass=["If G is to one side, the weight has a moment and turns it until the weight acts through the nail with no moment", "it swings until the moment is zero, which is when G is directly below the pivot"],
        sample_fail=["Because the nail pulls it down", "Because pictures are flat"])

written("w4x_wide_vs_narrow_vase", 4, 3, "4f",
        stem="Two vases have the same height and the same weight. Vase A has a narrow base and vase B a wide base. Explain which is more stable.",
        points=[P("B is more stable", ["b is more stable", "vase b", "b is", "b more stable", "the wide one"]),
                P("B must be tilted further before the line of its weight falls outside the base", ["tilted further", "tilt further", "larger angle", "outside the base", "more tilt", "bigger angle"])],
        pitfalls=[PF(["a is more stable"], "The narrow base makes A easier to topple.")],
        model_answer="Vase B is more stable: with a wider base it must be tilted through a larger angle before the vertical line through its centre of gravity falls outside its base.",
        hints=["Which has the wider base?", "How far must each tilt before toppling?", "Wider base → larger tilt."],
        keywords="B; wider base needs larger tilt before weight outside base",
        sample_pass=["B is more stable because it must tilt further before the weight is outside the base", "vase B, since a larger angle is needed before G is outside its base"],
        sample_fail=["A is more stable because it is thinner", "They are equally stable"])

written("w4x_tap_handle", 4, 3, "4a",
        stem="Taps for people with weak hands often have long lever handles instead of small round knobs. Explain why.",
        points=[P("the force acts further from the pivot (axis of the tap)", ["further from the pivot", "further from the axis", "larger distance", "longer distance", "greater distance", "further away"]),
                P("so a smaller force gives the moment needed", ["smaller force", "less force", "same moment", "larger moment", "bigger moment", "greater turning effect"])],
        model_answer="A long lever handle means the force is applied further from the pivot, so a smaller force produces the moment needed to turn the tap.",
        hints=["Where is the pivot of a tap?", "How does the lever change the distance?", "Link distance to the force needed."],
        keywords="larger distance from pivot → smaller force for same moment",
        sample_pass=["The force is applied further from the pivot so less force gives the same moment", "a longer distance from the axis gives a larger moment for the same force"],
        sample_fail=["Lever handles look nicer", "They let more water through"])

written("w4x_bottle_opener", 4, 3, "4a",
        stem="Explain, in terms of moments, why a bottle opener with a longer handle makes it easier to lift off a bottle cap.",
        points=[P("the hand is further from the pivot", ["further from the pivot", "larger distance", "greater distance", "longer distance", "hand further"]),
                P("so the same force produces a larger moment (or less force is needed)", ["larger moment", "bigger moment", "greater moment", "less force", "smaller force", "more turning effect"])],
        model_answer="With a longer handle the hand is further from the pivot, so the same force produces a larger moment, and less force is needed to lift the cap.",
        hints=["Where is the pivot?", "What does a longer handle change?", "Moment = F × d."],
        keywords="larger distance → larger moment / less force",
        sample_pass=["The hand is further from the pivot so the moment is larger", "a greater distance means less force is needed"],
        sample_fail=["The handle is stronger", "It pulls the cap straight up"])

# ---------------------------------------------------------------- L4
written("w4x_spanner_pipe", 4, 4, "4b",
        stem="A mechanic slides a pipe over a spanner handle to double its length. Explain the effect on the force needed to loosen a nut, assuming the force is applied at right angles at the end.",
        points=[P("the perpendicular distance doubles", ["distance doubles", "doubles the distance", "twice the distance", "distance is doubled", "double the distance"]),
                P("so the force needed is halved for the same moment", ["force is halved", "half the force", "halves the force", "force halves", "half as much force"])],
        pitfalls=[PF(["force doubles"], "A longer lever needs LESS force for the same moment.")],
        model_answer="The perpendicular distance from the nut doubles, so for the same moment (M = F d) only half the force is needed.",
        hints=["What changes when the pipe is added?", "The moment needed is the same.", "F = M ÷ d."],
        keywords="distance doubles → force halves",
        sample_pass=["The distance doubles so the force is halved", "twice the distance means half the force for the same moment"],
        sample_fail=["The force doubles", "No change, the nut is the same"])

written("w4x_cg_add_mass", 4, 4, "4e",
        stem="A uniform plank is pivoted at its centre and balances. A small weight is now fixed to one end. Explain what happens and where the new centre of gravity of plank and weight is.",
        points=[P("the end with the weight goes down (it is no longer balanced)", ["goes down", "tips", "turns", "falls", "no longer balanced", "not balanced"]),
                P("the combined centre of gravity moves towards the weight, away from the pivot", ["towards the weight", "moves towards", "shifts towards", "closer to the weight", "nearer the weight", "towards that end"])],
        model_answer="The plank turns so that the end with the weight goes down, because the combined centre of gravity has moved from the pivot towards the weighted end; the combined weight now has a moment about the pivot.",
        hints=["Is it still balanced?", "Where does the combined weight now act?", "It moves towards the extra mass."],
        keywords="end goes down; combined G moves towards weight",
        sample_pass=["That end goes down because the centre of gravity moves towards the weight", "it is no longer balanced; the combined centre of gravity shifts towards the weighted end"],
        sample_fail=["Nothing happens", "The centre of gravity stays at the pivot"])

written("w4x_cg_find_rule", 4, 4, "4e",
        stem="Describe how you could find the position of the centre of gravity of a non-uniform rod using only a knife-edge.",
        points=[P("balance the rod on the knife-edge, moving it until it balances horizontally", ["balance", "balances", "move it until", "horizontal", "knife-edge", "knife edge"]),
                P("G is directly above the knife-edge at the balance point; read its position", ["directly above", "above the knife", "balance point", "at that point", "that position", "mark the point"])],
        model_answer="Place the rod on the knife-edge and move it until it balances horizontally. Its centre of gravity is directly above the knife-edge at that balance point, so mark or read off that position.",
        hints=["What happens when the pivot is under G?", "Move the rod until it balances.", "G is then above the pivot."],
        keywords="balance on knife-edge; G above balance point",
        sample_pass=["Move the rod on the knife edge until it balances; G is directly above the knife edge", "find the balance point on the knife-edge and mark that point as the centre of gravity"],
        sample_fail=["Measure its length and halve it", "Weigh it on a balance"])

written("w4x_hammer_nail", 4, 4, "4a",
        stem="A claw hammer is used to pull a nail out of wood. Explain why holding the hammer near the end of its handle makes this easier.",
        points=[P("the hand is further from the pivot (where the hammer rests on the wood)", ["further from the pivot", "larger distance", "greater distance", "far from the pivot", "longer distance"]),
                P("the same force gives a larger moment, so a large force acts on the nail", ["larger moment", "bigger moment", "greater moment", "large force on the nail", "larger force on the nail", "less force"])],
        model_answer="The hammer turns about the point where its head rests on the wood. Holding the end puts the hand further from this pivot, so the same force gives a larger moment and a large force is applied to the nail, which is close to the pivot.",
        hints=["Where is the pivot?", "Compare the distances of the hand and the nail.", "Link to the moments."],
        keywords="hand far from pivot → large moment → large force on nail",
        sample_pass=["The hand is further from the pivot so the moment is larger and a large force acts on the nail", "a greater distance from the pivot means less force is needed to pull the nail"],
        sample_fail=["The hammer is heavier at the end", "Because the nail is loose"])

written("w4x_steering_wheel", 4, 4, "4a",
        stem="Buses and lorries have larger steering wheels than small cars. Explain why.",
        points=[P("a larger wheel means the driver's hands are further from the axis", ["further from the axis", "further from the centre", "larger distance", "greater distance", "larger radius", "further from the pivot"]),
                P("so a smaller force gives the larger moment needed to turn the heavy steering", ["smaller force", "less force", "larger moment", "bigger moment", "greater turning effect", "more turning effect"])],
        model_answer="A larger steering wheel puts the driver's hands further from the axis, so the same force gives a larger moment; a smaller force is enough to turn the heavy steering of a bus.",
        hints=["Where is the pivot of a steering wheel?", "What does a larger wheel change?", "Link to the moment."],
        keywords="larger radius → larger moment / less force",
        sample_pass=["The hands are further from the centre so less force is needed for the moment", "a larger radius gives a bigger moment for the same force"],
        sample_fail=["Big wheels look better", "The bus is faster"])

# ---------------------------------------------------------------- L5
written("w4x_claim_heavier_wins", 4, 5, "4c",
        stem="A student says: 'On a see-saw, the heavier child always goes down.' Evaluate this statement using the principle of moments.",
        points=[P("the statement is wrong / not always true", ["wrong", "not always", "incorrect", "not true", "disagree"]),
                P("what matters is the moment, weight × distance from the pivot", ["moment", "weight × distance", "weight x distance", "force × distance", "distance from the pivot"]),
                P("a heavier child close to the pivot can balance or be lifted by a lighter child far away", ["closer to the pivot", "nearer the pivot", "further away", "lighter child further", "can balance", "far from the pivot"])],
        min_points=2,
        model_answer="The statement is not always true. The side that goes down is the side with the larger moment (weight × distance from the pivot), so a heavier child sitting close to the pivot can be balanced or even lifted by a lighter child sitting further away.",
        hints=["What decides which way it turns?", "Moment, not force.", "Give a counter-example."],
        keywords="not always; moment = W d decides; heavy child near pivot can be lifted",
        sample_pass=["Wrong, because it depends on the moment, weight x distance; a lighter child further away can lift a heavier child closer to the pivot", "not always true: the moments decide, and a heavier child near the pivot can balance a lighter one far from the pivot"],
        sample_fail=["Correct, heavier things always fall", "Yes because gravity is stronger on them"])

written("w4x_tightrope_long_pole", 4, 5, "4f",
        stem="A tightrope walker carries a long pole that droops down at both ends. Explain how this helps them stay balanced.",
        points=[P("the drooping pole lowers the combined centre of gravity", ["lowers the centre of gravity", "lower centre of gravity", "centre of gravity lower", "centre of gravity is lowered", "below the rope"]),
                P("small tilts can be corrected / they need a larger tilt before toppling", ["larger tilt", "tilt further", "correct", "restoring moment", "turns back", "harder to topple"])],
        model_answer="The heavy drooping ends lower the combined centre of gravity of walker and pole, so a larger tilt is needed before they topple, and the pole's ends give a restoring moment that helps correct small tilts.",
        hints=["Where is the pole's mass?", "What happens to the combined G?", "Link to toppling."],
        keywords="pole lowers combined G; restoring moment; harder to topple",
        sample_pass=["The pole lowers the centre of gravity so they can tilt further before toppling", "the drooping ends lower the combined centre of gravity and give a restoring moment to correct a tilt"],
        sample_fail=["The pole is light", "It helps them walk faster"])

written("w4x_cg_crane_counterweight_position", 4, 5, "4e",
        stem="A tower crane lifts a heavy load far out on its jib. Explain why, without a counterweight, the crane could topple, using the idea of centre of gravity.",
        points=[P("the load moves the combined centre of gravity towards the load", ["towards the load", "moves the centre of gravity", "shifts the centre of gravity", "centre of gravity moves", "centre of gravity shifts"]),
                P("if it moves outside the base, the weight's moment topples the crane", ["outside the base", "beyond the base", "past the base", "moment", "topple"]),
                P("a counterweight on the other side keeps the combined G above the base", ["counterweight", "other side", "keeps the centre of gravity", "within the base", "above the base"])],
        min_points=2,
        model_answer="The heavy load far out on the jib moves the combined centre of gravity towards the load. If it moves beyond the edge of the base, the combined weight has a moment about that edge and the crane topples. A counterweight on the other side keeps the combined centre of gravity above the base.",
        hints=["Where is the combined G when the load is lifted?", "What happens if it passes the base?", "What does the counterweight do?"],
        keywords="combined G moves towards load; outside base → topples; counterweight keeps G over base",
        sample_pass=["The load moves the centre of gravity towards it and outside the base so the crane topples; the counterweight keeps it above the base", "the combined centre of gravity shifts beyond the base and the moment topples it; a counterweight on the other side prevents this"],
        sample_fail=["The crane is too tall", "The load is too light"])

written("w4x_cg_lamina_errors", 4, 5, "4e",
        stem="A student finds the centre of gravity of a card with a plumb line, but the lines from three holes form a small triangle instead of meeting at a point. Suggest two reasons and one improvement.",
        points=[P("friction at the pin so the card did not swing freely", ["friction", "not swing freely", "did not hang freely", "not free to swing", "stuck"]),
                P("the plumb line was not still or the line was drawn inaccurately", ["not still", "moving", "drawn inaccurately", "thick line", "parallax", "not accurately marked", "line was not accurate"]),
                P("improvement: make the holes larger / let it settle / use a fine pencil and view at eye level", ["larger holes", "bigger holes", "let it settle", "wait", "fine pencil", "sharp pencil", "eye level"])],
        min_points=2,
        model_answer="The card may not have swung freely because of friction at the pin, and the plumb line may not have been still or the line may have been marked inaccurately (for example from a parallax error). Use larger holes so the card swings freely, wait until the plumb line is still, and mark the line with a sharp pencil viewed at eye level.",
        hints=["What could stop the card hanging properly?", "What could make the line inaccurate?", "Suggest a fix for each."],
        keywords="friction at pin; plumb line moving / inaccurate marking; larger holes, wait, sharp pencil",
        sample_pass=["Friction at the pin stopped it swinging freely and the line was drawn inaccurately; use larger holes and a sharp pencil", "the card was not free to swing and the plumb line was moving; let it settle before marking"],
        sample_fail=["The card was too light", "Use a ruler to measure the card"])

written("w4x_design_mobile", 4, 5, "4d",
        stem="Explain how you would make a toy mobile with a 2 N model and a 3 N model hang level from a light rod, and state the ratio of their distances from the supporting thread.",
        points=[P("hang the 3 N model closer to the thread than the 2 N model", ["3 n closer", "heavier closer", "3 n nearer", "heavier one closer", "3 n model closer"]),
                P("so the moments are equal: 2 × d₁ = 3 × d₂", ["moments are equal", "moments equal", "moments balance", "principle of moments", "2 × d", "2 x d"]),
                P("ratio of distances 2 N : 3 N = 3 : 2", ["3 : 2", "3:2", "1.5"])],
        min_points=2,
        model_answer="Hang the 3 N model closer to the thread so that the moments balance: 2 × d₁ = 3 × d₂. The distance of the 2 N model to that of the 3 N model must be 3 : 2.",
        hints=["Which model must be closer?", "Use the principle of moments.", "Find d₁ : d₂."],
        keywords="heavier closer; 2 d₁ = 3 d₂; ratio 3 : 2",
        sample_pass=["Hang the 3 N model closer so the moments are equal; distances in the ratio 3:2", "heavier one closer to the thread, moments balance, 2 N at 1.5 times the distance of the 3 N"],
        sample_fail=["Hang them at equal distances", "Hang the 2 N model closer"])
