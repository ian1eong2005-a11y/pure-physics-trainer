"""Chapter 17 Magnetism written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w17x_magnetic_materials", 17, 1, "17a",
        stem="Name two magnetic materials and one non-magnetic metal.",
        points=[P("magnetic: two of iron, steel, nickel, cobalt", ["iron", "steel", "nickel", "cobalt"]),
                P("non-magnetic metal: e.g. copper, aluminium, brass, gold, silver", ["copper", "aluminium", "brass", "gold", "silver", "lead", "zinc"])],
        model_answer="Magnetic: iron and nickel (also steel and cobalt). Non-magnetic metal: copper (also aluminium or brass).",
        hints=["Which metals does a magnet attract?", "Which metals does it not attract?", "Give examples."],
        keywords="iron, steel, nickel, cobalt; copper, aluminium",
        sample_pass=["Iron and nickel are magnetic; copper is not", "steel and cobalt; aluminium"],
        sample_fail=["copper and gold are magnetic", "wood and plastic"])

written("w17x_compass_points", 17, 1, "17d",
        stem="State which way a plotting compass points when placed near the N pole of a bar magnet, and why.",
        points=[P("it points away from the N pole", ["away from the n pole", "away from the north pole", "away from n", "away"]),
                P("because the field lines go out of the N pole (like poles repel)", ["field lines", "like poles repel", "repel", "out of the n"])],
        model_answer="The compass N pole points away from the magnet's N pole, because the field lines leave the N pole (and like poles repel).",
        hints=["Which way do field lines go at an N pole?", "Outwards.", "The compass follows the field."],
        keywords="away from N pole; field leaves N",
        sample_pass=["It points away from the N pole because like poles repel", "away from the north pole, along the field lines coming out of it"],
        sample_fail=["It points towards the N pole", "It points up"])

written("w17x_induced_explain_l1", 17, 1, "17b",
        stem="State what is meant by induced magnetism.",
        points=[P("magnetism produced in a magnetic material", ["magnetic material", "iron", "steel", "material becomes a magnet", "becomes magnetised"]),
                P("when it is placed near (or in contact with) a magnet", ["near a magnet", "close to a magnet", "next to a magnet", "touching a magnet", "in a magnetic field"])],
        model_answer="Induced magnetism is the magnetism produced in a magnetic material, such as iron, when it is placed near a magnet (in its field).",
        hints=["What kind of material?", "Where is it placed?", "Put it together."],
        keywords="magnetism in a magnetic material near a magnet",
        sample_pass=["A magnetic material becomes magnetised when placed near a magnet", "iron becomes a magnet when it is close to a magnet"],
        sample_fail=["Magnetism caused by heating", "A magnet losing its magnetism"])

written("w17x_magnetise_solenoid_l1", 17, 1, "17b",
        stem="Describe how to magnetise a steel bar using electricity.",
        points=[P("place the bar inside a solenoid (coil)", ["solenoid", "coil"]),
                P("pass a direct current (d.c.) through the coil", ["direct current", "d.c.", "dc", "battery"])],
        model_answer="Place the steel bar inside a solenoid and pass a large direct current (d.c.) through the coil for a short time; then switch off and remove the bar.",
        hints=["What device makes a strong field?", "Which kind of current?", "Describe the method."],
        keywords="solenoid; direct current",
        sample_pass=["Put it inside a solenoid and pass a direct current through it", "place the bar in a coil connected to a d.c. battery"],
        sample_fail=["Heat it in a flame", "Put it in a coil with a.c. and pull it out slowly"])

written("w17x_demagnetise_l1", 17, 1, "17b",
        stem="State two ways of demagnetising a magnet.",
        points=[P("one method: heating strongly / hammering / a.c. coil and slowly withdrawing", ["heat", "hammer", "a.c.", "alternating", "drop"]),
                P("a second, different method", ["heat", "hammer", "a.c.", "alternating", "drop", "pull it out slowly"])],
        min_points=2,
        model_answer="Heat it strongly, or place it in a coil carrying a.c. and slowly pull it out (hammering it also works).",
        hints=["What upsets the domains?", "Heat or vibration.", "A reversing field."],
        keywords="heating; hammering; a.c. coil",
        sample_pass=["Heat it strongly or hammer it", "put it in a coil with alternating current and pull it out slowly, or heat it"],
        sample_fail=["Stroke it with a magnet", "Put it in a coil with d.c."])

written("w17x_iron_temporary_written", 17, 1, "17c",
        stem="State what is meant by a temporary magnet and give an example of a material that forms one.",
        points=[P("a magnet that loses its magnetism when the magnetising field is removed", ["loses its magnetism", "loses magnetism", "not permanent", "only while"]),
                P("example: (soft) iron", ["iron"])],
        model_answer="A temporary magnet is magnetised only while it is in a magnetic field and loses its magnetism when the field is removed; soft iron is an example.",
        hints=["How long does it stay magnetised?", "Only while near a magnet.", "Which material?"],
        keywords="loses magnetism when field removed; soft iron",
        sample_pass=["It loses its magnetism when the magnet is removed, like soft iron", "iron, which is only magnetised while near a magnet"],
        sample_fail=["Steel, which keeps its magnetism", "A magnet that lasts for ever"])

written("w17x_steel_permanent_written", 17, 1, "17c",
        stem="State what is meant by a permanent magnet and give an example of a material that forms one.",
        points=[P("a magnet that keeps its magnetism after the magnetising field is removed", ["keeps its magnetism", "retains", "stays magnetised", "keeps magnetism"]),
                P("example: steel", ["steel"])],
        model_answer="A permanent magnet keeps its magnetism after the magnetising field is removed; steel is an example.",
        hints=["Does it keep its magnetism?", "Yes.", "Which material?"],
        keywords="keeps magnetism; steel",
        sample_pass=["It keeps its magnetism after being magnetised, for example steel", "steel, which stays magnetised"],
        sample_fail=["Soft iron", "A magnet that switches off"])

written("w17x_iron_vs_steel_use", 17, 1, "17c",
        stem="State one use of soft iron and one use of steel in magnetism, and the property that makes each suitable.",
        points=[P("soft iron: electromagnet core / relay / transformer core, because it is easily magnetised and demagnetised", ["electromagnet", "relay", "transformer", "core"]),
                P("steel: permanent magnets / compass needles, because it keeps its magnetism", ["permanent magnet", "compass", "fridge magnet", "loudspeaker"])],
        model_answer="Soft iron is used for electromagnet cores because it is easily magnetised and loses its magnetism when switched off. Steel is used for permanent magnets (e.g. compass needles) because it keeps its magnetism.",
        hints=["Which must switch off?", "Which must stay magnetised?", "Match the uses."],
        keywords="iron: electromagnet core; steel: permanent magnet",
        sample_pass=["Soft iron for electromagnet cores; steel for permanent magnets like compass needles", "iron in a relay because it demagnetises easily; steel for fridge magnets"],
        sample_fail=["Steel for electromagnet cores", "Iron for permanent magnets"])

# ---------------------------------------------------------------- L2
written("w17x_chain_clips", 17, 2, "17b",
        stem="Explain why a chain of iron paper clips can hang from one pole of a magnet.",
        points=[P("each clip is magnetised by induction", ["induction", "induced", "becomes a magnet", "magnetised"]),
                P("and attracts the next clip below it", ["attracts the next", "next clip", "attracts another", "each attracts"])],
        model_answer="The first clip is magnetised by induction and becomes a magnet itself; it then attracts and magnetises the next clip, and so on down the chain.",
        hints=["What happens to the first clip?", "What can it then do?", "Down the chain."],
        keywords="induced magnetism; each clip attracts the next",
        sample_pass=["Each clip is magnetised by induction and attracts the next one", "the clips become induced magnets that attract the next clip"],
        sample_fail=["The clips are glued", "Gravity holds them"])

written("w17x_compass_steel_needle", 17, 2, "17c",
        stem="Explain why compass needles are made of steel rather than iron.",
        points=[P("steel keeps its magnetism (permanent magnet)", ["keeps its magnetism", "permanent", "stays magnetised", "retains"]),
                P("iron would lose its magnetism, so the needle would stop working", ["iron would lose", "iron loses", "lose its magnetism", "temporary"])],
        model_answer="Steel keeps its magnetism, so the needle stays magnetised and keeps working. An iron needle would soon lose its magnetism.",
        hints=["Must the needle stay magnetised?", "Which material keeps magnetism?", "Compare with iron."],
        keywords="steel permanent; iron would lose magnetism",
        sample_pass=["Steel keeps its magnetism but iron would lose it", "steel is a permanent magnet while iron is temporary"],
        sample_fail=["Steel is lighter", "Iron is not magnetic"])

written("w17x_three_properties", 17, 2, "17a",
        stem="Describe what happens when (a) two N poles and (b) an N and an S pole are brought close together.",
        points=[P("(a) like poles repel", ["repel", "push apart"]),
                P("(b) unlike poles attract", ["attract", "pull together"])],
        model_answer="(a) Two N poles (like poles) repel each other. (b) An N and an S pole (unlike poles) attract each other.",
        hints=["Like or unlike?", "Like repel.", "Unlike attract."],
        keywords="like repel; unlike attract",
        sample_pass=["(a) they repel (b) they attract", "like poles push apart and unlike poles pull together"],
        sample_fail=["Both attract", "Both repel"])

written("w17x_why_repulsion_test", 17, 2, "17a",
        stem="Explain why repulsion, and not attraction, is the test for whether an object is a magnet.",
        points=[P("a magnet attracts unmagnetised magnetic materials too (by induction)", ["unmagnetised", "induction", "any magnetic material", "also attracted"]),
                P("only two magnets can repel each other", ["only", "repel", "two magnets"])],
        model_answer="A magnet attracts any magnetic material, even unmagnetised iron, by induced magnetism, so attraction does not prove an object is a magnet. Only two magnets can repel each other, so repulsion is the sure test.",
        hints=["What else does a magnet attract?", "Can an unmagnetised bar repel?", "So which test is sure?"],
        keywords="attraction also with unmagnetised materials; only magnets repel",
        sample_pass=["A magnet also attracts unmagnetised iron by induction, but only two magnets can repel", "attraction happens with any magnetic material, so only repulsion proves it is a magnet"],
        sample_fail=["Attraction is stronger", "Repulsion makes a noise"])

written("w17x_field_direction_rule", 17, 2, "17d",
        stem="Describe the direction of the magnetic field lines around a bar magnet.",
        points=[P("the lines leave the N pole and enter the S pole (outside the magnet)", ["n pole to the s pole", "from n to s", "leave the n", "north to south", "n to s"]),
                P("they form closed curves (loops) around the magnet", ["loops", "closed", "curves", "curve round"])],
        model_answer="Outside the magnet the field lines come out of the N pole, curve round and go into the S pole, forming closed loops.",
        hints=["Where do lines start?", "Where do they end?", "What shape?"],
        keywords="N → S outside; closed loops",
        sample_pass=["The lines go from the N pole to the S pole in curved loops", "they leave the north pole and curve round to the south pole"],
        sample_fail=["From S to N in straight lines", "In circles round the middle"])

written("w17x_earth_compass", 17, 2, "17d",
        stem="Explain why a compass needle points north when it is far from any magnets.",
        points=[P("the needle is a magnet that lines up with the Earth's magnetic field", ["earth's magnetic field", "earth's field", "lines up", "aligns"]),
                P("its N pole is attracted towards the Earth's magnetic pole near geographic north", ["attracted", "magnetic pole", "geographic north", "south pole"])],
        model_answer="The needle is a small magnet that lines up with the Earth's magnetic field; its N pole is attracted towards the Earth's magnetic pole near the geographic North Pole (which is a magnetic south pole).",
        hints=["What field is everywhere on Earth?", "The needle is a magnet.", "What attracts its N pole?"],
        keywords="aligns with Earth's field; N pole attracted north",
        sample_pass=["It lines up with the Earth's magnetic field, its N pole attracted towards the magnetic pole in the north", "the needle aligns with the earth's field, and its N pole is attracted to the magnetic pole in the geographic north"],
        sample_fail=["Gravity pulls it north", "The Sun attracts it"])

written("w17x_field_strength_written", 17, 2, "17e",
        stem="Explain how the spacing of field lines on a diagram shows the strength of a magnetic field.",
        points=[P("closer lines show a stronger field", ["closer", "close together", "closest", "dense"]),
                P("so the field is strongest at the poles, where the lines are most crowded", ["at the poles", "near the poles", "most crowded", "strongest"])],
        model_answer="The closer together the field lines, the stronger the field. Around a bar magnet the lines are most crowded at the poles, so the field is strongest there.",
        hints=["What does line spacing show?", "Close lines…", "…strong field."],
        keywords="closer lines → stronger; strongest at poles",
        sample_pass=["Closer lines mean a stronger field, so it is strongest at the poles", "where the lines are close together the field is strong, so it is strongest at the poles"],
        sample_fail=["Lines far apart mean a strong field", "Longer lines are stronger"])

written("w17x_field_unlike_poles", 17, 2, "17e",
        stem="Describe the field pattern between the N pole of one magnet and the S pole of another placed close together.",
        points=[P("field lines go across from the N pole to the S pole", ["n pole to the s pole", "from n to s", "across", "n to s"]),
                P("the lines are close together and nearly straight (strong field)", ["close together", "straight", "strong", "parallel"])],
        model_answer="The field lines go straight across the gap from the N pole to the S pole; they are close together, showing a strong field.",
        hints=["Unlike poles.", "Which way do the lines go?", "How are they spaced?"],
        keywords="N → S across; close, straight lines",
        sample_pass=["The lines go straight across from N to S and are close together", "strong field lines across the gap from the N pole to the S pole"],
        sample_fail=["The lines curve away with a neutral point", "There is no field"],
        figure=lambda: figs3.two_magnets("NS"))

# ---------------------------------------------------------------- L3
written("w17x_test_magnet_method", 17, 3, "17a",
        stem="You have an iron bar, a magnet and a piece of copper that all look alike. Describe how a known magnet can be used to identify each.",
        points=[P("the magnet repels one end of the unknown magnet", ["repel", "repels"]),
                P("the iron bar is attracted at both ends but never repelled", ["attracted at both", "both ends", "never repelled", "only attracted"]),
                P("the copper is not attracted at all", ["not attracted", "no effect", "nothing happens"])],
        min_points=2,
        model_answer="Bring a pole of the known magnet near each end of each object. The unknown magnet is repelled at one end. The iron bar is attracted at both ends but never repelled. The copper is not attracted at all.",
        hints=["What shows a magnet?", "What shows a magnetic material?", "What shows a non-magnetic one?"],
        keywords="repulsion → magnet; attraction only → iron; no effect → copper",
        sample_pass=["The magnet is repelled at one end, iron is attracted at both ends, copper is not attracted", "the magnet repels one end, the iron is attracted at both ends, and copper is not attracted"],
        sample_fail=["Weigh them all", "The heaviest is the magnet"])

written("w17x_cut_magnet", 17, 3, "17a",
        stem="A bar magnet is cut in half across its middle. Describe and explain what is obtained.",
        points=[P("two smaller magnets, each with an N and an S pole", ["two magnets", "each has", "n and s", "both poles", "two smaller magnets"]),
                P("magnetic poles always come in pairs (each piece's domains are still aligned)", ["pairs", "domains", "cannot have one pole", "single pole"])],
        model_answer="Two smaller magnets are obtained, each with its own N and S pole, because magnetic poles always come in pairs: the domains in each half are still aligned.",
        hints=["Can a magnet have one pole?", "What about each half?", "Explain with domains."],
        keywords="two magnets each with N and S; poles in pairs",
        sample_pass=["Two smaller magnets, each with N and S poles, because poles always come in pairs", "each half is a magnet with both poles, because poles always come in pairs"],
        sample_fail=["One N pole and one S pole", "Two non-magnetic pieces"])

written("w17x_induction_far_end_written", 17, 3, "17b",
        stem="Fig. 1 shows an iron bar near the N pole of a magnet. State the poles induced at each end of the bar and explain why the bar is attracted.",
        points=[P("the near end becomes S and the far end N", ["near end s", "near end is s", "s pole at the near", "near end becomes s", "far end n"]),
                P("unlike poles (N and S) attract, and the near end is closer, so attraction wins", ["unlike poles attract", "attract", "closer"])],
        model_answer="The end nearest the magnet's N pole becomes an S pole and the far end becomes an N pole. Unlike poles attract, and the attracting S end is closer than the repelling N end, so the bar is attracted.",
        hints=["What pole is induced near the N pole?", "And at the far end?", "Why does attraction win?"],
        keywords="near end S, far end N; unlike attract, closer",
        sample_pass=["The near end becomes S and the far end N; unlike poles attract and the S end is closer", "an S pole at the near end, which attracts the magnet's N pole"],
        sample_fail=["The near end becomes N", "The bar is repelled"],
        figure=lambda: figs3.induced_magnetism("iron"))

written("w17x_domains_explain", 17, 3, "17b",
        stem="Use the idea of magnetic domains to explain the difference between a magnetised and an unmagnetised piece of iron.",
        points=[P("unmagnetised: domains point in random directions, so their effects cancel", ["random", "cancel", "different directions"]),
                P("magnetised: domains are lined up in the same direction", ["lined up", "aligned", "same direction"])],
        model_answer="In unmagnetised iron, the domains point in random directions, so their magnetic effects cancel. In magnetised iron, most domains are lined up in the same direction, so their effects add to make a magnet.",
        hints=["What are domains?", "How are they arranged when unmagnetised?", "When magnetised?"],
        keywords="random (cancel) vs aligned",
        sample_pass=["Unmagnetised: domains are random and cancel; magnetised: they are lined up in the same direction", "the domains are aligned in a magnet but random otherwise"],
        sample_fail=["Magnets have more iron", "Unmagnetised iron has no domains"])

written("w17x_relay_core_written", 17, 3, "17c",
        stem="Explain why the core of the electromagnet in an electric bell is made of soft iron, not steel.",
        points=[P("soft iron magnetises when the current flows and loses its magnetism when it stops", ["loses its magnetism", "demagnetises", "temporary", "loses magnetism"]),
                P("so the armature is released each time and the bell keeps ringing; steel would stay magnetised", ["released", "springs back", "steel would stay", "stay magnetised", "keeps ringing"])],
        model_answer="Soft iron is magnetised while the current flows and loses its magnetism as soon as it stops, so the armature is released each time and the bell keeps ringing. A steel core would stay magnetised and hold the armature.",
        hints=["How does a bell work?", "Must the core release the armature?", "Iron or steel?"],
        keywords="iron demagnetises → armature released; steel would stay magnetised",
        sample_pass=["Soft iron loses its magnetism when the current stops, so the armature is released; steel would stay magnetised", "iron is temporary so the armature springs back each time"],
        sample_fail=["Steel is better for bells", "Iron is cheaper only"])

written("w17x_magnet_storage", 17, 3, "17c",
        stem="Permanent bar magnets are stored in pairs with soft iron 'keepers' across their ends. Explain why.",
        points=[P("the keepers become induced magnets and complete the magnetic loop", ["induced", "complete", "loop", "closed"]),
                P("this helps the magnets keep their magnetism (domains stay aligned)", ["keep their magnetism", "keep magnetism", "stay aligned", "do not lose", "retain"])],
        model_answer="The soft iron keepers are magnetised by induction and complete a closed magnetic loop between the poles. This keeps the domains aligned, so the magnets do not slowly lose their magnetism.",
        hints=["What happens to the soft iron keepers?", "What do they do to the field?", "Why does that help?"],
        keywords="keepers induced, close loop; magnets keep magnetism",
        sample_pass=["The keepers are induced magnets that complete the loop, so the magnets keep their magnetism", "they close the magnetic loop so the magnets keep their magnetism"],
        sample_fail=["To make them heavier", "To stop them rusting"])

written("w17x_plot_compass_l3", 17, 3, "17d",
        stem="Describe how to use a plotting compass to find the direction of the field at a point near a bar magnet.",
        points=[P("place the compass at the point", ["place the compass", "put the compass", "at the point"]),
                P("the direction in which its N pole points is the field direction", ["n pole points", "n end points", "north pole of the compass", "direction of the needle"])],
        model_answer="Place the plotting compass at the point; when the needle settles, the direction its N pole points is the direction of the magnetic field there.",
        hints=["Where is the compass placed?", "Which end of the needle shows the field?", "Its N pole."],
        keywords="compass at the point; N pole shows direction",
        sample_pass=["Place the compass there; the direction its N pole points is the field direction", "put the compass at the point and see where the north pole of the compass points"],
        sample_fail=["The S pole points along the field", "Use iron filings to measure the angle"])

written("w17x_compass_reverse_written", 17, 3, "17d",
        stem="A plotting compass sits near the end of a solenoid. The current in the solenoid is reversed. Describe and explain what happens to the compass.",
        points=[P("the compass needle turns round to point the opposite way", ["turns round", "opposite way", "reverses", "points the other way", "180"]),
                P("reversing the current reverses the magnetic field (swaps the poles)", ["reverses the field", "field reverses", "poles swap", "swaps the poles", "field is reversed"])],
        model_answer="The compass needle turns round to point the opposite way, because reversing the current reverses the solenoid's magnetic field, swapping its N and S poles.",
        hints=["What does the current direction decide?", "The poles.", "What happens to the compass?"],
        keywords="needle reverses; field (poles) reversed",
        sample_pass=["The needle turns round because the field reverses and the poles swap", "it points the opposite way since the field is reversed"],
        sample_fail=["Nothing happens", "The compass loses its magnetism"])

written("w17x_neutral_point_written", 17, 3, "17e",
        stem="Two identical bar magnets are placed with their N poles facing. Describe the field between them and explain what is found midway.",
        points=[P("field lines from each N pole curve away from each other (do not join)", ["curve away", "do not join", "away from each other", "repel"]),
                P("midway there is a neutral point where the fields cancel (zero field)", ["neutral point", "cancel", "zero", "no field"])],
        model_answer="The field lines from each N pole curve away from each other and do not join. Midway between them is a neutral point, where the two equal and opposite fields cancel, so the field is zero.",
        hints=["Do lines join between like poles?", "What happens midway?", "Name the point."],
        keywords="lines curve away; neutral point midway",
        sample_pass=["The lines curve away from each other and there is a neutral point midway where the fields cancel", "the lines curve away from each other, with a neutral point of zero field in the middle"],
        sample_fail=["Lines go straight across", "The field is strongest midway"],
        figure=lambda: figs3.two_magnets("NN"))

written("w17x_iron_filings", 17, 3, "17e",
        stem="Describe how iron filings can be used to show the magnetic field pattern of a bar magnet, and what the pattern shows.",
        points=[P("place paper over the magnet, sprinkle filings and tap gently", ["sprinkle", "tap", "paper", "filings"]),
                P("the filings line up along the field lines", ["line up", "along the field lines", "align"]),
                P("they crowd together at the poles, showing the field is strongest there", ["poles", "strongest", "crowd", "concentrated"])],
        min_points=2,
        model_answer="Place a sheet of paper over the magnet, sprinkle iron filings on it and tap the paper gently. The filings line up along the field lines, crowding together at the poles, which shows the field is strongest there.",
        hints=["How are the filings applied?", "What do they do?", "Where do they crowd?"],
        keywords="paper, sprinkle, tap; filings line up; crowd at poles",
        sample_pass=["Sprinkle filings on paper over the magnet and tap; they line up along the field and crowd at the poles", "the filings align with the field lines, densest at the poles"],
        sample_fail=["Weigh the filings", "Heat the filings"])

# ---------------------------------------------------------------- L4
written("w17x_electromagnet_advantages", 17, 4, "17b",
        stem="Give two advantages of an electromagnet over a permanent magnet, with a use that relies on each.",
        points=[P("it can be switched on and off (e.g. scrapyard crane releasing cars)", ["switched on and off", "switch off", "turned off", "release"]),
                P("its strength can be changed by changing the current (e.g. sorting metals, MRI)", ["strength can be changed", "change the current", "adjust", "stronger"])],
        model_answer="An electromagnet can be switched on and off, which lets a scrapyard crane pick up and drop cars; and its strength can be changed by changing the current or the number of turns, which allows control in devices such as relays and lifting magnets.",
        hints=["What can you do with the current?", "Switch it…", "…and change it."],
        keywords="switch on/off; adjustable strength",
        sample_pass=["It can be switched off so a crane can release the scrap, and its strength can be changed by changing the current", "you can turn it off and adjust how strong it is"],
        sample_fail=["It never needs power", "It is always weaker"])

written("w17x_field_compare_patterns", 17, 4, "17e",
        stem="Compare the magnetic field pattern between two N poles facing each other with that between an N and an S pole facing each other.",
        points=[P("N–N: lines curve away from each other with a neutral point between", ["curve away", "neutral point", "do not join"]),
                P("N–S: lines go straight across the gap from N to S", ["straight across", "from n to s", "join", "go across"])],
        model_answer="Between two N poles the lines curve away from each other and there is a neutral point midway. Between an N and an S pole the lines go straight across the gap from N to S.",
        hints=["Like poles: what happens to the lines?", "Unlike poles?", "Compare."],
        keywords="NN: curve away, neutral point; NS: straight across",
        sample_pass=["Between N and N the lines curve away with a neutral point; between N and S they go straight across", "like poles give a neutral point, unlike poles have lines joining from N to S"],
        sample_fail=["Both patterns are the same", "NN lines go straight across"])

written("w17x_attract_both_ends", 17, 4, "17a",
        stem="A student finds that a metal bar is attracted to both poles of a magnet. Explain what this shows about the bar.",
        points=[P("the bar is a magnetic material (e.g. iron/steel)", ["magnetic material", "magnetic", "iron", "steel"]),
                P("it is not a magnet: it is attracted by induction and never repelled", ["not a magnet", "unmagnetised", "induction", "not magnetised", "never repelled"])],
        model_answer="It shows the bar is made of a magnetic material but is not itself a magnet: it is attracted to both poles by induced magnetism, and a magnet would be repelled by one of the poles.",
        hints=["Would a magnet be attracted to both poles?", "So what is the bar?", "Explain with induction."],
        keywords="magnetic material; not a magnet (induction)",
        sample_pass=["It is a magnetic material but not a magnet, attracted by induction", "the bar is unmagnetised iron, since a magnet would repel one pole"],
        sample_fail=["It is a strong magnet", "It is non-magnetic"])

written("w17x_two_bars_identify", 17, 4, "17a",
        stem="Two identical-looking steel bars attract each other at every pair of ends. Explain what this shows, and how you could find out which (if either) is a magnet using only the two bars.",
        points=[P("at least one bar is not a magnet (two magnets would repel at some ends)", ["not a magnet", "would repel", "at least one", "only one"]),
                P("place the end of bar A against the middle of bar B: if attracted, A is the magnet", ["middle", "centre"]),
                P("a magnet's middle has almost no field, so it does not attract", ["no field", "weak", "middle has", "no attraction"])],
        min_points=2,
        model_answer="If they attract at every pair of ends, they cannot both be magnets (two magnets would repel for like poles), so only one is a magnet. Touch the end of bar A to the middle of bar B: if A attracts B's middle strongly, A is the magnet, because the middle of a magnet has almost no field.",
        hints=["Would two magnets ever repel?", "Where is a magnet's field weakest?", "Use the middle of a bar."],
        keywords="not both magnets; test end against middle",
        sample_pass=["Only one can be a magnet; touch the end of one to the middle of the other — the magnet's end attracts the other's middle", "they would repel if both were magnets; use the middle of the bar, where a magnet has no field"],
        sample_fail=["Both are magnets", "Weigh the bars"])

written("w17x_crane_core_written", 17, 4, "17c",
        stem="Explain why the electromagnet of a scrapyard crane has a soft iron core and not a steel core.",
        points=[P("soft iron is easily magnetised, giving a strong magnet when the current is on", ["easily magnetised", "strong", "concentrates"]),
                P("soft iron loses its magnetism when the current is switched off, so the scrap is released", ["loses its magnetism", "released", "drops", "demagnetises"]),
                P("steel would stay magnetised and keep holding the scrap", ["steel would stay", "stay magnetised", "keep holding"])],
        min_points=2,
        model_answer="Soft iron is easily magnetised, so the electromagnet is strong when the current is on, and it loses its magnetism when the current is switched off, so the scrap is released. A steel core would stay magnetised and keep holding the scrap.",
        hints=["What must the crane do with the scrap?", "Pick up and release.", "Iron or steel?"],
        keywords="iron easily magnetised and demagnetised; steel would hold on",
        sample_pass=["Soft iron loses its magnetism when switched off so the scrap is released; steel would stay magnetised", "iron is a strong temporary magnet, so the cars drop when the current stops"],
        sample_fail=["Steel is stronger so it is better", "Iron is lighter"])

written("w17x_steel_vs_iron_data", 17, 4, "17c",
        stem="An iron bar and a steel bar are magnetised by touching a magnet. While touching, iron holds 30 pins and steel 18. After removal, iron holds 1 pin and steel 14. Explain what these results show.",
        points=[P("iron is magnetised more easily (holds more pins while touching)", ["iron is magnetised more easily", "iron holds more", "easier to magnetise", "more strongly magnetised"]),
                P("iron loses its magnetism (temporary) while steel keeps it (permanent)", ["iron loses", "steel keeps", "temporary", "permanent"])],
        model_answer="Iron is magnetised more easily (30 pins against 18), but it loses almost all its magnetism when the magnet is removed (1 pin), so it is a temporary magnet. Steel keeps most of its magnetism (14 pins), so it is a permanent magnet.",
        hints=["Which holds more while touching?", "Which keeps more after removal?", "Temporary or permanent?"],
        keywords="iron easily magnetised, temporary; steel permanent",
        sample_pass=["Iron is magnetised more easily but loses its magnetism; steel keeps it", "iron holds more pins while touching but is temporary, and steel is permanent"],
        sample_fail=["Steel is easier to magnetise", "Iron is a permanent magnet"])

written("w17x_compass_field_mapping", 17, 4, "17d",
        stem="Explain why a plotting compass gives the direction of a magnetic field, and why a small compass is used.",
        points=[P("the compass needle is a small magnet that turns to line up with the field", ["small magnet", "lines up", "aligns", "turns"]),
                P("its N pole points in the field direction", ["n pole", "north pole of the compass", "points in the direction"]),
                P("a small compass shows the field at one point and hardly disturbs it", ["one point", "small", "disturb", "precise", "local"])],
        min_points=2,
        model_answer="The needle is a small magnet that turns to line up with the field; its N pole points in the direction of the field. A small compass is used so it shows the field at one particular point and hardly disturbs the field being measured.",
        hints=["What is the needle?", "Which end shows the direction?", "Why small?"],
        keywords="needle aligns; N pole shows direction; small → one point",
        sample_pass=["The needle is a magnet that lines up with the field, its N pole showing the direction; small so it measures one point", "it aligns with the field and a small one gives the direction at one point"],
        sample_fail=["The compass creates the field", "The S pole shows the field"])

written("w17x_earth_field_written", 17, 4, "17d",
        stem="A student says the magnetic pole near the Earth's geographic North Pole must be a magnetic north pole. Explain why this is incorrect.",
        points=[P("the compass N pole is attracted to it", ["attracted", "points to"]),
                P("unlike poles attract, so it must be a magnetic south pole", ["unlike poles attract", "south pole", "s pole"])],
        model_answer="A compass needle's N pole is attracted towards the Earth's geographic North Pole. Since unlike poles attract, the magnetic pole there must be a magnetic south pole.",
        hints=["What attracts the compass N pole?", "Like or unlike?", "So what is the pole?"],
        keywords="compass N attracted; unlike attract → magnetic S pole",
        sample_pass=["The compass N pole is attracted there and unlike poles attract, so it is a magnetic south pole", "it must be an S pole since it attracts the N pole of a compass"],
        sample_fail=["It is a north pole because N points north", "It is not magnetic"])

# ---------------------------------------------------------------- L5
written("w17x_eval_attract_claim", 17, 5, "17a",
        stem="A student says: 'If two objects attract each other, they must both be magnets.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false", "not necessarily"]),
                P("a magnet attracts an unmagnetised magnetic material by induction", ["unmagnetised", "induction", "magnetic material", "iron"]),
                P("only one needs to be a magnet; repulsion would show both are magnets", ["only one", "one magnet", "repulsion"])],
        min_points=2,
        model_answer="The statement is wrong. A magnet attracts unmagnetised magnetic materials, such as iron, by induced magnetism, so only one of the objects needs to be a magnet. Only repulsion would show that both are magnets.",
        hints=["Can a magnet attract an unmagnetised object?", "How?", "What would prove both are magnets?"],
        keywords="wrong; induction; only one need be a magnet",
        sample_pass=["Wrong, a magnet attracts unmagnetised iron by induction, so only one has to be a magnet", "not necessarily: only one needs to be a magnet; repulsion would prove both are"],
        sample_fail=["Correct, both must be magnets", "Correct, only magnets attract"])

written("w17x_eval_magnet_design", 17, 5, "17a",
        stem="A designer wants a fridge door to stay shut using a magnet. Evaluate the use of a permanent magnet in the door and a steel strip on the frame.",
        points=[P("the permanent magnet attracts the steel strip (magnetic material) by induction", ["attracts", "induction", "steel strip", "magnetic material"]),
                P("no power is needed, and the force is strong only when close (door easy to open)", ["no power", "no electricity", "only when close", "easy to open", "weakens with distance"]),
                P("the steel need not be a magnet; it is attracted anyway", ["need not be a magnet", "does not need", "unmagnetised", "attracted anyway"])],
        min_points=2,
        model_answer="It works well: the permanent magnet attracts the steel strip, which is a magnetic material, by induction, so the strip does not need to be a magnet. No power is needed, and the force is strong only at very short distances, so the door shuts firmly but is easy to pull open.",
        hints=["Does the steel need to be a magnet?", "Does it need power?", "How does the force depend on distance?"],
        keywords="magnet attracts steel by induction; no power; strong only when close",
        sample_pass=["It works: the magnet attracts the steel by induction, needs no power, and is only strong when close so the door opens easily", "the steel strip does not need to be a magnet; it is attracted anyway"],
        sample_fail=["It will not work because steel is not magnetic", "Use copper instead"])

written("w17x_eval_demagnetise_claim", 17, 5, "17b",
        stem="A student says that placing a magnet in a coil carrying direct current and pulling it out will demagnetise it. Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("d.c. gives a steady field, which magnetises (or keeps it magnetised)", ["steady", "magnetise", "d.c.", "direct current"]),
                P("an alternating current is needed: its reversing field leaves the domains random as it is withdrawn", ["alternating", "a.c.", "reversing", "random"])],
        min_points=2,
        model_answer="The statement is wrong. A direct current gives a steady field in one direction, which magnetises the bar rather than demagnetising it. To demagnetise, an alternating current is used: its field keeps reversing, and as the magnet is slowly withdrawn the domains are left pointing in random directions.",
        hints=["What does a steady field do?", "Which current reverses?", "What happens to the domains?"],
        keywords="wrong; d.c. magnetises; a.c. demagnetises (random domains)",
        sample_pass=["Wrong, d.c. gives a steady field which magnetises it; you need a.c., whose reversing field leaves the domains random", "incorrect: use alternating current, not direct current"],
        sample_fail=["Correct, any current demagnetises", "Correct, pulling it out is what matters"])

written("w17x_eval_magnet_strength", 17, 5, "17b",
        stem="Suggest and explain two ways to make an electromagnet stronger.",
        points=[P("increase the current", ["increase the current", "more current", "larger current", "bigger current"]),
                P("increase the number of turns on the coil", ["more turns", "increase the number of turns", "more coils"]),
                P("use a soft iron core, which concentrates the field", ["soft iron core", "iron core", "core"])],
        min_points=2,
        model_answer="Increase the current, and increase the number of turns on the coil; both produce a stronger magnetic field. Adding a soft iron core also makes it much stronger, because the iron becomes magnetised and concentrates the field.",
        hints=["What about the current?", "What about the coil?", "What about the core?"],
        keywords="more current; more turns; iron core",
        sample_pass=["Increase the current and use more turns on the coil", "add a soft iron core and increase the current"],
        sample_fail=["Use a steel core and less current", "Make the wire longer only"])

written("w17x_eval_compass_use", 17, 5, "17d",
        stem="A student uses a large compass to map the field of a small magnet. Evaluate this method and suggest an improvement.",
        points=[P("a large compass covers a region where the field changes, so it does not show the direction at a point", ["region", "does not show", "one point", "averages", "large area"]),
                P("its own magnet may disturb the field of the small magnet", ["disturb", "affects", "its own field", "changes the field"]),
                P("use a small plotting compass", ["small plotting compass", "smaller compass", "small compass"])],
        min_points=2,
        model_answer="It is a poor method. A large compass covers a region over which the field changes, so it does not show the direction at one point, and its own magnetic needle can disturb the small magnet's field. A small plotting compass should be used.",
        hints=["Does a large compass show the field at one point?", "Could it change the field?", "What should be used?"],
        keywords="large compass: not one point, disturbs field; use small plotting compass",
        sample_pass=["A large compass does not show the field at one point and disturbs it; use a small plotting compass", "use a smaller compass because a large one affects the field"],
        sample_fail=["A large compass is more accurate", "Compasses cannot map fields"])

written("w17x_eval_compass_iron", 17, 5, "17d",
        stem="A walker's compass points in the wrong direction when held next to a steel car. Evaluate the reasons for this.",
        points=[P("steel is a magnetic material and may be magnetised (or magnetised by induction)", ["magnetised", "magnetic material", "induction", "steel"]),
                P("its field combines with the Earth's field at the compass, changing the direction", ["combines", "adds", "earth's field", "distorts", "changes the direction"]),
                P("moving away from the car makes the reading correct again", ["move away", "far from", "further away"])],
        min_points=2,
        model_answer="Steel is a magnetic material and may be magnetised, or magnetised by induction in the Earth's field. Its magnetic field adds to the Earth's field at the compass, changing the direction the needle points. Moving well away from the car gives a correct reading.",
        hints=["Is steel magnetic?", "What does its field do at the compass?", "How could the walker fix it?"],
        keywords="steel magnetised; field adds to Earth's; move away",
        sample_pass=["The steel is magnetised and its field adds to the Earth's field, distorting the compass; move away from the car", "steel is a magnetic material whose field changes the direction the needle points"],
        sample_fail=["The car is charged", "The compass is broken"])

written("w17x_eval_field_lines_cross", 17, 5, "17e",
        stem="A student draws field lines around two magnets and shows two lines crossing. Evaluate this drawing.",
        points=[P("the drawing is wrong: field lines never cross", ["never cross", "cannot cross", "wrong", "do not cross"]),
                P("because the field at any point has only one direction", ["one direction", "only one", "single direction"]),
                P("where fields combine, a single resultant line is drawn", ["resultant", "combine", "single line", "add together"])],
        min_points=2,
        model_answer="The drawing is wrong: field lines never cross, because the magnetic field at any point has only one direction (a compass there could point only one way). Where the two magnets' fields combine, a single line showing the resultant field should be drawn.",
        hints=["Can a compass point two ways at once?", "So can lines cross?", "What should be drawn?"],
        keywords="lines never cross; one direction at each point; resultant",
        sample_pass=["Wrong, field lines never cross because the field has only one direction at each point", "lines cannot cross; draw the resultant field instead"],
        sample_fail=["Lines can cross if the magnets are strong", "Crossing shows a strong field"])

written("w17x_eval_neutral_point", 17, 5, "17e",
        stem="A student says the field midway between two like poles is very strong because both magnets are close. Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("the two fields are equal and opposite there and cancel", ["equal and opposite", "cancel", "opposite directions"]),
                P("so there is a neutral point with zero field", ["neutral point", "zero", "no field"])],
        min_points=2,
        model_answer="The statement is wrong. Midway between two identical like poles, the two fields are equal in size but opposite in direction, so they cancel. This is a neutral point, where the resultant field is zero.",
        hints=["Which way does each field point midway?", "Are they equal?", "What is the result?"],
        keywords="wrong; equal and opposite fields cancel; neutral point",
        sample_pass=["Wrong, the fields are equal and opposite so they cancel, giving a neutral point", "incorrect: it is a neutral point with no field"],
        sample_fail=["Correct, it is the strongest point", "Correct because two magnets add"],
        figure=lambda: figs3.two_magnets("NN"))
