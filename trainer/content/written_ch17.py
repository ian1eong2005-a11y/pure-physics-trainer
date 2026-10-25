"""Chapter 17 Magnetism: written-answer questions, two per level (properties of magnets, field direction, induced magnetism,
iron vs steel, plotting fields, testing for a magnet, field patterns, magnetising and demagnetising, evaluation and design)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w17_properties_of_magnets", 17, 1, "17a",
        stem="State three properties of a bar magnet.",
        points=[P("it has two poles, N and S, where the magnetism is strongest", ["two poles", "north and south", "n and s", "poles at the ends", "strongest at the poles"]),
                P("like poles repel and unlike poles attract", ["like poles repel", "unlike poles attract", "opposite poles attract", "same poles repel", "repel", "attract"]),
                P("it attracts magnetic materials (iron, steel, nickel, cobalt) and, when freely suspended, points north-south", ["attracts magnetic materials", "attracts iron", "attracts steel", "points north", "north-south", "freely suspended", "acts as a compass"])],
        min_points=2,
        model_answer="A bar magnet has two poles, north and south, where its magnetism is strongest. Like poles repel and unlike poles attract. It attracts magnetic materials such as iron, steel, nickel and cobalt, and when freely suspended it comes to rest pointing north-south.",
        hints=["Think about its ends, how two magnets interact, and what it does to a paper clip.", "Poles; repulsion and attraction; magnetic materials; compass behaviour.", "State any three."],
        keywords="two poles; like repel, unlike attract; attracts magnetic materials; points N-S when free",
        sample_pass=["It has two poles, like poles repel and unlike poles attract, and it attracts iron", "N and S poles; opposite poles attract; it points north-south when suspended"],
        sample_fail=["It is made of copper and conducts electricity", "It attracts all metals including aluminium"])

written("w17_field_direction", 17, 1, "17d",
        stem="State what is meant by the direction of a magnetic field at a point, and describe how a compass can be used to find it.",
        points=[P("the direction of the force on a free N pole (the direction a N pole would move), i.e. from N to S outside the magnet", ["force on a north pole", "free north pole", "n pole would move", "north pole would move", "from north to south", "n to s", "away from the north pole"]),
                P("place a plotting compass at the point: the direction its N pole points is the field direction", ["compass", "n pole of the compass points", "needle points", "direction the needle", "compass needle"])],
        model_answer="The direction of a magnetic field at a point is the direction of the force on a free north pole placed there, which outside a magnet is from its N pole towards its S pole. A plotting compass placed at the point lines up with the field, and the direction its N pole points is the direction of the field.",
        hints=["The direction is defined by which way a particular pole would be pushed.", "A compass needle is a small magnet that lines up with the field.", "Define the direction, then describe the compass."],
        keywords="direction of force on a free N pole; compass N points along the field",
        sample_pass=["The direction a free north pole would move; a compass needle's N end points that way", "it is the direction of the force on a north pole, found from where the N end of a compass needle points"],
        sample_fail=["The direction of the electric current in the magnet", "The direction the magnet is moving"])

# ---------------------------------------------------------------- L2
written("w17_induced_magnetism", 17, 2, "17b",
        stem="Fig. 1 shows an iron bar near the N pole of a magnet. Explain why the bar is attracted to the magnet, and state what happens when the magnet is removed.",
        points=[P("the iron becomes an induced magnet with its near end an S pole (opposite to the magnet's N pole)", ["induced magnet", "induced magnetism", "becomes magnetised", "near end becomes a south", "near end is s", "opposite pole", "s pole nearest"]),
                P("unlike poles attract, so the bar is pulled towards the magnet", ["unlike poles attract", "opposite poles attract", "attracted because", "n and s attract"]),
                P("when the magnet is removed the iron loses its magnetism (iron is a temporary magnet)", ["loses its magnetism", "demagnetised", "no longer magnetic", "temporary", "returns to normal", "stops being a magnet"])],
        min_points=2,
        model_answer="The magnet's field magnetises the iron: it becomes an induced magnet with an S pole at the end nearest the magnet's N pole and an N pole at the far end. Unlike poles attract, so the bar is pulled towards the magnet. Iron is a temporary magnetic material, so when the magnet is removed the bar loses its magnetism.",
        hints=["What happens to a magnetic material placed in a magnetic field?", "Which pole forms nearest the magnet, and why does that cause attraction?", "Iron is a soft (temporary) magnetic material: what happens when the field is removed?"],
        keywords="induced magnet, S pole nearest; unlike poles attract; iron loses magnetism when magnet removed",
        figure=lambda: figs3.induced_magnetism("iron"),
        sample_pass=["The iron becomes an induced magnet with a south pole nearest the magnet, so unlike poles attract; when the magnet is removed the iron loses its magnetism",
                     "induced magnetism gives the near end an S pole which is attracted; iron is temporary so it demagnetises afterwards"],
        sample_fail=["The iron is attracted because all metals are attracted to magnets", "The iron stays a strong permanent magnet for ever"])

written("w17_iron_vs_steel", 17, 2, "17c",
        stem="Compare iron and steel as magnetic materials, and give one use of each.",
        points=[P("iron is easily magnetised but easily loses its magnetism (a temporary / soft magnetic material)", ["easily magnetised", "loses its magnetism easily", "temporary", "soft magnetic", "iron loses", "does not keep"]),
                P("steel is harder to magnetise but keeps its magnetism (a permanent / hard magnetic material)", ["keeps its magnetism", "retains its magnetism", "permanent", "hard magnetic", "harder to magnetise", "stays magnetised"]),
                P("uses: iron for electromagnet cores / transformer cores / relay armatures; steel for permanent magnets, compass needles, fridge magnets", ["electromagnet", "core", "transformer", "relay", "permanent magnet", "compass needle", "fridge magnet", "bar magnet"])],
        min_points=2,
        model_answer="Iron is easily magnetised but loses its magnetism easily, so it is a temporary magnetic material, used for the cores of electromagnets and transformers. Steel is harder to magnetise but keeps its magnetism, so it is a permanent magnetic material, used for permanent bar magnets and compass needles.",
        hints=["One material keeps its magnetism, the other does not.", "Which would you want in an electromagnet that must switch off? Which in a compass needle?", "Compare the two and give a use for each."],
        keywords="iron: temporary, easily magnetised and demagnetised, electromagnet cores; steel: permanent, keeps magnetism, permanent magnets",
        sample_pass=["Iron is a temporary magnet that loses its magnetism easily and is used in electromagnet cores; steel keeps its magnetism and is used for permanent magnets",
                     "steel retains magnetism so it makes compass needles, iron is easily magnetised and demagnetised so it is used as a transformer core"],
        sample_fail=["Iron is heavier than steel so it is a better magnet", "Steel cannot be magnetised at all"])

# ---------------------------------------------------------------- L3
written("w17_plot_field_compass", 17, 3, "17d",
        stem="Describe how to use a small plotting compass to draw the magnetic field pattern around a bar magnet on a sheet of paper.",
        points=[P("place the magnet on the paper and draw round it; put the compass near one pole and mark dots at both ends of the needle", ["draw round", "outline", "place the compass near", "mark a dot", "mark the position", "dots at the ends of the needle", "mark where the needle points"]),
                P("move the compass so that its tail (S end) is at the previous dot made by its N end, mark again, and repeat until the other pole or the edge of the paper is reached", ["move the compass", "repeat", "previous dot", "where the n pole pointed", "until it reaches", "keep going", "series of dots"]),
                P("join the dots to form a field line and mark arrows from N to S; repeat starting at other points round the magnet", ["join the dots", "smooth line", "arrows", "from n to s", "north to south", "repeat from other", "several lines"])],
        min_points=2,
        model_answer="Place the bar magnet in the middle of the paper and draw round it. Put the plotting compass near the N pole and mark a dot at each end of the needle. Move the compass so that the S end of the needle is over the dot made by the N end, mark the new position of the N end, and repeat until the S pole or the edge of the paper is reached. Join the dots with a smooth line and put arrows on it pointing from N to S. Repeat from other starting points around the magnet.",
        hints=["Start near one pole with the compass and mark where the needle points.", "How do you move the compass to follow the line?", "What do you do with the dots at the end, and which way do the arrows go?"],
        keywords="dots at needle ends; move compass to previous dot; repeat; join dots, arrows N to S; repeat from other points",
        sample_pass=["Draw round the magnet, put the compass near the N pole, mark dots at the needle ends, move the compass so its tail is on the last dot and repeat, then join the dots with arrows from N to S",
                     "mark where the needle points, move the compass along, repeat to the S pole, join the dots into lines with arrows"],
        sample_fail=["Sprinkle iron filings and blow them away", "Hold the compass in the air above the magnet and spin it"])

written("w17_test_for_magnet", 17, 3, "17a",
        stem="A student has two identical-looking steel bars. One is a magnet and the other is unmagnetised. Describe how, using only a known bar magnet, the student can find out which bar is the magnet. Explain why the test works.",
        points=[P("bring each end of the known magnet's N pole (or S pole) near each end of the bar in turn", ["bring", "each end", "both ends", "near each end", "in turn", "close to"]),
                P("if one end of the bar is repelled, the bar is a magnet; the unmagnetised bar is attracted at both ends", ["repelled", "repulsion", "attracted at both ends", "both ends attract", "pushed away"]),
                P("repulsion is the only sure test, because an unmagnetised steel bar is attracted (by induced magnetism) but can never be repelled", ["only sure test", "only test", "induced magnetism", "never repelled", "cannot be repelled", "attraction is not enough", "attraction does not prove"])],
        min_points=2,
        model_answer="Bring the N pole of the known magnet close to each end of the first bar in turn, then do the same with the second bar. If either end of a bar is repelled, that bar is a magnet. The unmagnetised bar is attracted at both ends, because the known magnet induces the opposite pole in it. Repulsion is the only certain test for a magnet, since an unmagnetised bar can be attracted but never repelled.",
        hints=["What is the only effect that an unmagnetised bar can never show?", "Test both ends of each bar with one pole of the known magnet.", "Describe the test and explain why attraction alone is not enough."],
        keywords="bring known pole to each end; repulsion shows a magnet; unmagnetised bar attracted at both ends (induced), never repelled",
        sample_pass=["Bring the N pole of the known magnet to each end of each bar; the bar that is repelled at one end is the magnet, because an unmagnetised bar is only ever attracted",
                     "repulsion is the only sure test, so look for the bar with an end that is pushed away"],
        sample_fail=["Weigh the bars; the magnet is heavier", "The magnet is the one that attracts the known magnet"])

# ---------------------------------------------------------------- L4
written("w17_field_patterns_two_magnets", 17, 4, "17e",
        stem="Fig. 1 shows two bar magnets with like poles facing. Describe the field pattern between the poles, and explain how it differs from the pattern when unlike poles face each other.",
        points=[P("like poles: the field lines from each pole curve away from each other (repel) and do not cross the gap", ["curve away", "bend away", "repel each other", "do not cross", "spread away", "pushed apart", "do not join"]),
                P("there is a neutral point midway between the poles where the two fields cancel and the resultant field is zero", ["neutral point", "cancel", "zero field", "no resultant field", "field is zero"]),
                P("unlike poles: lines run straight across the gap from N to S, giving a strong, nearly uniform field", ["straight across", "from n to s", "across the gap", "uniform", "strong field", "join the poles", "run from the north pole to the south"])],
        min_points=2,
        model_answer="With like poles facing, the field lines leaving each pole curve away from each other and do not cross the gap, and midway between the poles there is a neutral point where the two fields cancel so the resultant field is zero. With unlike poles facing, the field lines run straight across the gap from the N pole to the S pole, giving a strong and almost uniform field between them.",
        hints=["Do field lines from two N poles join up or push apart?", "What is special about the point exactly between two like poles?", "Describe the like-pole pattern, the neutral point, and the unlike-pole pattern."],
        keywords="like poles: lines curve away, neutral point (zero field); unlike poles: lines straight across N to S, strong uniform field",
        figure=lambda: figs3.two_magnets("NN"),
        sample_pass=["Between like poles the lines bend away from each other and there is a neutral point where the field is zero; between unlike poles the lines go straight across from N to S",
                     "like poles repel so the field lines curve apart with a neutral point in the middle, unlike poles give a strong uniform field across the gap"],
        sample_fail=["The lines go straight from one N pole to the other", "There is no field at all between any two magnets"])

written("w17_magnetise_demagnetise", 17, 4, "17b",
        stem="Describe how a steel bar can be magnetised using a solenoid, and give two ways in which a magnet can be demagnetised.",
        points=[P("place the steel bar inside a solenoid and pass a large direct current through the coil (the field of the solenoid magnetises the bar; the right-hand grip rule gives the poles)", ["inside a solenoid", "inside the coil", "direct current", "d.c.", "dc current", "large current", "switch on the current", "field of the solenoid"]),
                P("demagnetise by placing it in a solenoid carrying alternating current and slowly withdrawing it (or reducing the a.c. to zero)", ["alternating current", "a.c.", "ac current", "slowly withdraw", "reduce the current", "east-west"]),
                P("or by heating it strongly / hammering it (while pointing east-west) / dropping it repeatedly", ["heat", "hammer", "drop", "strike", "hit", "red hot"])],
        min_points=2,
        model_answer="Place the steel bar inside a solenoid and pass a large direct current through the coil; the strong magnetic field inside the solenoid magnetises the steel, with the poles given by the right-hand grip rule. To demagnetise a magnet, place it inside a solenoid carrying alternating current and slowly withdraw it, or heat it strongly, or hammer it repeatedly while it lies east-west.",
        hints=["What kind of current, and where should the bar be?", "For demagnetising, think of a.c. in a coil, heat, and rough treatment.", "Give the magnetising method and two demagnetising methods."],
        keywords="steel in solenoid with d.c.; demagnetise with a.c. solenoid and withdraw, heating, hammering",
        sample_pass=["Put the steel inside a solenoid and pass a direct current through it; demagnetise by using alternating current and withdrawing the bar, or by heating it",
                     "a large d.c. in a coil around the bar magnetises it; hammering or an a.c. solenoid demagnetises it"],
        sample_fail=["Rub the bar with a piece of copper", "Leave the bar in the fridge to magnetise it"])

# ---------------------------------------------------------------- L5
written("w17_claim_iron_permanent", 17, 5, "17c",
        stem="A student says: 'Iron would be the best material for a permanent fridge magnet, because it is attracted to magnets more strongly than steel is.' Evaluate this statement.",
        points=[P("the statement is wrong: iron is a temporary (soft) magnetic material that loses its magnetism once the magnetising field is removed", ["wrong", "incorrect", "not suitable", "temporary", "loses its magnetism", "does not keep", "soft magnetic"]),
                P("steel (a hard magnetic material) keeps its magnetism, so it is the right choice for a permanent magnet", ["steel keeps", "retains", "permanent", "hard magnetic", "steel is better", "steel should be used", "stays magnetised"]),
                P("being easily magnetised is useful for electromagnet cores, not for permanent magnets; strength of attraction is not the deciding factor", ["electromagnet", "core", "easily magnetised", "not the deciding", "not what matters", "irrelevant"])],
        min_points=2,
        model_answer="The statement is wrong. Iron is easily magnetised, but it is a temporary (soft) magnetic material and loses its magnetism as soon as the magnetising field is removed, so an iron fridge magnet would not stay magnetic. Steel is harder to magnetise but keeps its magnetism, so steel (or another hard magnetic material) is the correct choice. Being easily magnetised makes iron ideal for electromagnet cores, not for permanent magnets.",
        hints=["What does 'permanent magnet' require of the material after it has been magnetised?", "Which material keeps its magnetism, iron or steel?", "Judge the claim and give the correct material with the reason."],
        keywords="wrong: iron is temporary, loses magnetism; steel retains magnetism, so steel for permanent magnets; iron suits electromagnet cores",
        sample_pass=["The student is wrong: iron loses its magnetism when the field is removed, so steel, which keeps its magnetism, should be used for a permanent magnet",
                     "incorrect, iron is a temporary magnetic material; steel retains magnetism so it is the right choice"],
        sample_fail=["The student is right because iron is the strongest magnetic material", "Neither iron nor steel can be made into a magnet"])

written("w17_design_electromagnet_crane", 17, 5, "17c",
        stem="A scrapyard crane uses an electromagnet to lift and release cars. Explain why the core of the electromagnet is made of iron rather than steel, and suggest two ways of making the electromagnet stronger.",
        points=[P("iron is a temporary magnetic material: it magnetises strongly when the current flows and loses its magnetism when the current is switched off, so the car can be released", ["temporary", "loses its magnetism when the current", "switched off", "release", "let go", "drop the car", "demagnetises"]),
                P("steel would keep its magnetism (permanent) so the car would stay stuck to the magnet", ["steel would keep", "steel retains", "stay stuck", "would not release", "remain magnetised", "permanent magnet"]),
                P("make it stronger by increasing the current or increasing the number of turns on the coil (or using a larger iron core)", ["increase the current", "more current", "larger current", "more turns", "increase the number of turns", "more coils", "bigger core"])],
        min_points=2,
        model_answer="Iron is a temporary magnetic material: it becomes a strong magnet while the current flows and loses its magnetism as soon as the current is switched off, so the crane can release the car. A steel core would keep its magnetism when the current stopped, so the car would stay stuck to the magnet. The electromagnet can be made stronger by increasing the current in the coil and by increasing the number of turns of wire on the core.",
        hints=["The crane must be able to switch the magnetism off. Which material loses its magnetism when the current stops?", "What would go wrong with a steel core?", "What two things about the coil can be changed to increase the field?"],
        keywords="iron temporary, demagnetises when current off (release); steel stays magnetised; stronger: more current, more turns",
        sample_pass=["Iron loses its magnetism when the current is switched off so the car can be released, whereas steel would stay magnetised; use more turns and a larger current to make it stronger",
                     "a temporary iron core lets go of the load when the current stops; increase the current or the number of turns to strengthen it"],
        sample_fail=["Steel is used because it is stronger than iron", "Make it stronger by painting the core red"])
