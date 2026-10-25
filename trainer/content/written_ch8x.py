"""Chapter 8 Thermal Processes written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w8x_name_insulators", 8, 1, "8b",
        stem="Name two good conductors of heat and two poor conductors (insulators).",
        points=[P("conductors: two metals, e.g. copper, aluminium, iron, silver", ["copper", "aluminium", "iron", "silver", "steel", "gold", "metal"]),
                P("insulators: e.g. wood, plastic, air, wool, glass, polystyrene", ["wood", "plastic", "air", "wool", "glass", "polystyrene", "rubber", "cork"])],
        model_answer="Good conductors: copper and aluminium. Poor conductors: wood and plastic.",
        hints=["Which group of materials conducts well?", "Which materials are used for handles?", "Two of each."],
        keywords="metals conduct; wood, plastic, air insulate",
        sample_pass=["Copper and iron are good conductors; wood and plastic are insulators", "aluminium, silver; air and wool"],
        sample_fail=["water and steam", "light and sound"])

written("w8x_name_convection", 8, 1, "8c",
        stem="Name the process by which energy is transferred through a liquid or gas by the movement of the fluid itself.",
        points=[P("convection", ["convection"])],
        pitfalls=[PF(["conduction"], "Conduction does not involve the fluid moving as a whole."), PF(["radiation"], "Radiation does not need the fluid to move.")],
        model_answer="Convection.",
        hints=["The fluid itself moves.", "Hot fluid rises, cool fluid sinks.", "Name the process."],
        keywords="convection",
        sample_pass=["convection", "it is called convection"],
        sample_fail=["conduction", "radiation"])

written("w8x_convection_cause", 8, 1, "8c",
        stem="Explain why warm air rises.",
        points=[P("warm air expands", ["expands", "expand", "takes up more space", "particles move further apart", "spread out"]),
                P("so it becomes less dense than the cooler air around it", ["less dense", "lower density", "density decreases", "lighter than the surrounding"])],
        pitfalls=[PF(["particles expand"], "The particles do not expand; the air expands as they move further apart.")],
        model_answer="When air is warmed it expands, so it becomes less dense than the cooler air around it and rises.",
        hints=["What happens to air when it warms?", "What happens to its density?", "Less dense fluids rise."],
        keywords="expands; less dense",
        sample_pass=["Warm air expands, so it is less dense and rises", "it takes up more space, so its density decreases"],
        sample_fail=["Heat rises", "Warm air is attracted to the ceiling"])

written("w8x_flask_parts_l1", 8, 1, "8e",
        stem="Fig. 1 shows a vacuum flask. Name two features of the flask that reduce heat loss.",
        points=[P("a vacuum between the double walls", ["vacuum"]),
                P("silvered (shiny) surfaces / a stopper / insulated case", ["silvered", "shiny", "stopper", "cap", "lid", "plastic case", "cork"])],
        model_answer="The vacuum between the double walls, and the silvered surfaces of the walls (also the insulating stopper).",
        hints=["What is between the walls?", "What are the walls coated with?", "What is at the top?"],
        keywords="vacuum; silvered walls; stopper",
        sample_pass=["The vacuum and the silvered walls", "a vacuum between the walls and an insulating stopper"],
        sample_fail=["a handle and a strap", "a black outer case"],
        figure=lambda: sketches.flask_sketch())

written("w8x_home_insulation_l1", 8, 1, "8e",
        stem="State two ways of reducing heat loss from a house.",
        points=[P("one method, e.g. loft insulation, cavity wall insulation, double glazing, draught excluders, carpets, curtains", ["loft", "cavity", "double glazing", "draught", "carpet", "curtains", "insulation", "insulate"]),
                P("a second, different method", ["loft", "cavity", "double glazing", "draught", "carpet", "curtains", "foil", "wall"])],
        min_points=2,
        model_answer="Put insulation in the loft and fit double glazing (also cavity wall insulation, draught excluders, thick curtains).",
        hints=["Where does a house lose heat?", "Roof, walls, windows, gaps.", "One way for each of two places."],
        keywords="loft insulation; double glazing; cavity wall; draught excluders",
        sample_pass=["Loft insulation and double glazing", "cavity wall insulation and draught excluders"],
        sample_fail=["Open the windows", "Turn the heating up"])

# ---------------------------------------------------------------- L2
written("w8x_metal_vs_wood_feel", 8, 2, "8b",
        stem="A metal door handle and a wooden door are at the same temperature, yet the handle feels colder. Explain why.",
        points=[P("metal is a better conductor than wood", ["better conductor", "good conductor", "conducts heat better", "conducts better", "conducts faster"]),
                P("so it conducts energy away from the hand faster", ["away from the hand", "from your hand", "from the skin", "faster", "more quickly"])],
        pitfalls=[PF(["metal is colder"], "Both are at the same temperature; the metal only FEELS colder.")],
        model_answer="Metal is a much better conductor than wood, so it conducts energy away from your hand faster, making it feel colder even though both are at the same temperature.",
        hints=["Are they at different temperatures?", "Which conducts better?", "Where does the energy go?"],
        keywords="metal better conductor; takes energy from hand faster",
        sample_pass=["Metal is a better conductor so it conducts heat away from your hand faster", "the metal is a good conductor so it conducts energy from the skin more quickly"],
        sample_fail=["Metal is colder than wood", "Wood is warm"])

written("w8x_convection_beaker", 8, 2, "8c",
        stem="Fig. 1 shows a beaker of water heated at one side. Describe how a convection current forms.",
        points=[P("water above the flame is heated, expands, becomes less dense and rises", ["less dense", "rises", "expands"]),
                P("cooler, denser water sinks to take its place", ["denser", "sinks", "cooler water", "moves in"]),
                P("a circulating current is set up", ["circulat", "current", "cycle", "loop", "repeats"])],
        min_points=2,
        model_answer="The water above the flame is heated, expands and becomes less dense, so it rises. Cooler, denser water sinks to take its place and is heated in turn, setting up a circulating convection current.",
        hints=["What happens to the water above the flame?", "What replaces it?", "What is formed?"],
        keywords="heated water expands, less dense, rises; cooler denser sinks; circulation",
        sample_pass=["Heated water expands, becomes less dense and rises; cooler denser water sinks, forming a current", "warm water rises and cold water sinks to replace it, so it circulates"],
        sample_fail=["The water conducts the heat", "Heat rises by radiation"],
        figure=lambda: sketches.convection_sketch())

written("w8x_cool_box_ice", 8, 2, "8e",
        stem="Ice packs in a cool box are placed at the top, above the food. Explain why.",
        points=[P("air near the ice is cooled, becomes denser and sinks", ["denser", "sinks", "cold air sinks"]),
                P("this sets up convection currents that cool all the food", ["convection", "current", "circulat", "whole box", "all the food"])],
        model_answer="Air next to the ice packs is cooled, becomes denser and sinks onto the food. Warmer air rises to the ice to be cooled, setting up convection currents that cool all the food.",
        hints=["What does cold air do?", "Why does position matter?", "Name the process."],
        keywords="cold air denser, sinks; convection currents",
        sample_pass=["The cold air near the ice is denser so it sinks, setting up convection currents", "cold air sinks over the food and warm air rises to the ice, so convection cools everything"],
        sample_fail=["Ice is lighter", "So it does not get squashed"])

written("w8x_equilibrium_contact", 8, 2, "8a",
        stem="A hot metal block is placed in contact with a cold one inside an insulated box. Describe what happens to their temperatures, and when energy transfer stops.",
        points=[P("the hot block cools and the cold block warms", ["hot block cools", "cold block warms", "cools down", "warms up", "temperature falls", "temperature rises"]),
                P("until they reach the same temperature (thermal equilibrium), when net transfer stops", ["same temperature", "thermal equilibrium", "equal temperature", "equilibrium"])],
        model_answer="Energy flows from the hot block to the cold one, so the hot block cools and the cold block warms. The net transfer stops when they reach the same temperature: thermal equilibrium.",
        hints=["Which way does energy flow?", "What happens to each temperature?", "When does it stop?"],
        keywords="hot cools, cold warms; until same temperature",
        sample_pass=["The hot block cools and the cold block warms until they are at the same temperature", "they reach thermal equilibrium; the hot one cools down and the cold one warms up"],
        sample_fail=["Both get hotter", "The cold block gives cold to the hot one"])

written("w8x_temperature_vs_energy", 8, 2, "8a",
        stem="A bath of warm water at 40 °C contains more thermal energy than a cup of tea at 80 °C. Which way would energy flow if they were in contact? Explain.",
        points=[P("from the tea to the bath water", ["from the tea", "tea to the bath", "tea loses", "from the cup"]),
                P("energy flows from higher to lower temperature, regardless of total energy", ["higher temperature", "hot to cold", "hotter to colder", "temperature difference", "depends on temperature"])],
        model_answer="Energy flows from the tea to the bath water, because energy is transferred by heating from a higher temperature to a lower temperature; the total energy stored does not decide the direction.",
        hints=["Which is at the higher temperature?", "What decides the direction?", "Not the amount of energy."],
        keywords="tea → bath; flows from higher to lower temperature",
        sample_pass=["From the tea to the bath, because heat flows from hot to cold", "the tea loses energy since it is at the higher temperature"],
        sample_fail=["From the bath to the tea because it has more energy", "No flow"])

# ---------------------------------------------------------------- L3
written("w8x_radiation_cans", 8, 3, "8d",
        stem="Two identical cans, one dull black and one shiny silver, are filled with hot water at the same temperature (Fig. 1). Predict which cools faster and explain.",
        points=[P("the dull black can cools faster", ["black can cools faster", "dull black", "black one", "black cools faster", "black can"]),
                P("dull black surfaces are better emitters of infrared radiation", ["better emitter", "good emitter", "emits more", "emits infrared", "emits radiation", "emits better"])],
        pitfalls=[PF(["silver cools faster", "shiny cools faster"], "Shiny surfaces are POOR emitters.")],
        model_answer="The dull black can cools faster, because a dull black surface is a better emitter of infrared radiation than a shiny silver one.",
        hints=["Which surface emits best?", "Dull black.", "So which loses energy faster?"],
        keywords="dull black; better emitter of infrared",
        sample_pass=["The dull black can, because black is a better emitter of infrared radiation", "black cools faster since it emits more radiation"],
        sample_fail=["The silver can, because it is shiny", "They cool equally"],
        figure=lambda: sketches.two_cups_sketch())

written("w8x_equilibrium_cooling_rate", 8, 3, "8a",
        stem="A cup of hot coffee cools quickly at first and then more slowly. Explain why.",
        points=[P("the rate of cooling depends on the temperature difference with the surroundings", ["temperature difference", "difference in temperature", "depends on the difference"]),
                P("as the coffee cools, the difference gets smaller, so the rate falls", ["gets smaller", "decreases", "smaller difference", "less difference", "rate falls", "slower"])],
        model_answer="The rate of cooling depends on the temperature difference between the coffee and the room. As the coffee cools, this difference becomes smaller, so the rate of cooling falls.",
        hints=["What drives the heat flow?", "What happens to it as the coffee cools?", "Link to the rate."],
        keywords="rate ∝ temperature difference; difference falls",
        sample_pass=["The rate depends on the temperature difference, which gets smaller as it cools", "a smaller difference in temperature means slower cooling"],
        sample_fail=["The coffee runs out of heat", "The cup gets thicker"])

written("w8x_equilibrium_thermometer", 8, 3, "8a",
        stem="Explain why a clinical thermometer must stay in the mouth for a minute or so before it is read.",
        points=[P("the thermometer must reach the same temperature as the mouth (thermal equilibrium)", ["same temperature", "thermal equilibrium", "equilibrium", "reach the temperature"]),
                P("energy takes time to flow from the mouth to the thermometer", ["takes time", "energy flows", "heat flows", "energy is transferred", "needs time"])],
        model_answer="Energy takes time to flow from the mouth into the thermometer. It must be left until it reaches thermal equilibrium with the mouth, so that its reading equals the body temperature.",
        hints=["What has to happen to the thermometer's temperature?", "How does it get there?", "Why does it take time?"],
        keywords="reach thermal equilibrium; energy flow takes time",
        sample_pass=["It must reach thermal equilibrium with the mouth, which takes time as energy flows in", "energy flows into it until it is at the same temperature"],
        sample_fail=["So the mercury can freeze", "To kill germs"])

written("w8x_flask_how_works", 8, 3, "8e",
        stem="Explain how a vacuum flask (Fig. 1) keeps a hot drink hot. Refer to conduction, convection and radiation.",
        points=[P("the vacuum stops conduction and convection between the walls", ["vacuum"]),
                P("the silvered surfaces reduce radiation (reflect infrared)", ["silvered", "shiny", "reflect"]),
                P("the stopper reduces convection and evaporation at the top", ["stopper", "cap", "lid", "cork"])],
        min_points=2,
        model_answer="The vacuum between the double walls has no particles, so it stops conduction and convection. The silvered surfaces reflect infrared back and are poor emitters, reducing radiation. The insulating stopper reduces convection and evaporation from the top (and conduction through it).",
        hints=["What does the vacuum stop?", "What do the silvered surfaces do?", "What does the stopper do?"],
        keywords="vacuum: conduction + convection; silvering: radiation; stopper: convection/evaporation",
        sample_pass=["The vacuum stops conduction and convection, and the silvered walls reflect radiation", "the stopper stops convection at the top and the vacuum stops conduction"],
        sample_fail=["The flask produces heat", "The flask is thick"],
        figure=lambda: sketches.flask_sketch())

written("w8x_igloo", 8, 3, "8e",
        stem="People living in very cold places can keep warm inside a shelter made of blocks of snow. Explain how this is possible.",
        points=[P("snow contains trapped air", ["trapped air", "air", "air pockets"]),
                P("trapped air is a poor conductor and cannot set up convection currents", ["poor conductor", "insulator", "does not conduct", "cannot move", "no convection", "convection"])],
        model_answer="Snow contains a lot of trapped air. Air is a poor conductor, and because it is trapped it cannot set up convection currents, so the snow walls insulate the inside well.",
        hints=["What is snow full of?", "How well does air conduct?", "Can trapped air move?"],
        keywords="trapped air; poor conductor, no convection",
        sample_pass=["Snow has trapped air which is a poor conductor, so it insulates", "the air pockets are insulators and cannot move to cause convection"],
        sample_fail=["Snow produces heat", "Snow is a good conductor"])

# ---------------------------------------------------------------- L4
written("w8x_convection_fridge", 8, 4, "8c",
        stem="Explain why the cooling unit of a refrigerator is placed at the top, and describe how it cools the whole cabinet.",
        points=[P("air near the cooling unit is cooled, becomes denser and sinks", ["denser", "sinks", "cold air sinks"]),
                P("warmer air from below rises to the top to be cooled", ["warmer air rises", "warm air rises", "rises to the top", "replaced"]),
                P("a convection current circulates through the whole cabinet", ["convection", "circulat", "current"])],
        min_points=2,
        model_answer="Air near the cooling unit is cooled, contracts and becomes denser, so it sinks. Warmer air from lower down rises to take its place and is cooled in turn, so a convection current circulates and cools the whole cabinet.",
        hints=["What does cooled air do?", "What replaces it?", "What is set up?"],
        keywords="cold air denser, sinks; warm air rises; convection current",
        sample_pass=["The cold air is denser and sinks, warmer air rises to be cooled, setting up a convection current", "cold air sinks and warm air rises so it circulates through the fridge"],
        sample_fail=["Cold rises", "It is easier to reach the top"])

written("w8x_radiation_greenhouse", 8, 4, "8d",
        stem="Explain why the inside of a car parked in the sun becomes much hotter than the air outside.",
        points=[P("radiation from the Sun passes through the glass and is absorbed by the seats", ["passes through the glass", "through the windows", "absorbed", "absorb"]),
                P("the warm interior emits longer-wavelength infrared, which cannot easily pass back out through the glass", ["longer wavelength", "cannot pass", "trapped", "does not pass", "infrared"]),
                P("the closed car stops warm air escaping by convection", ["convection", "warm air cannot escape", "closed", "windows closed"])],
        min_points=2,
        model_answer="Radiation from the Sun passes through the glass and is absorbed by the seats and dashboard, which warm up. They emit longer-wavelength infrared that cannot easily pass back out through the glass, so energy is trapped; the closed car also stops warm air escaping by convection.",
        hints=["What passes through the windows?", "What do the warm seats emit?", "Can it get back out?"],
        keywords="sunlight in through glass, absorbed; longer-wavelength IR trapped; no convection out",
        sample_pass=["Radiation passes through the glass and is absorbed; the infrared emitted is trapped by the glass", "the seats absorb sunlight and the longer wavelength infrared cannot pass out; warm air cannot escape by convection"],
        sample_fail=["Cars produce heat", "The metal conducts heat from the road"])

written("w8x_conduction_free_electrons", 8, 4, "8b",
        stem="Explain, in terms of particles, why metals conduct heat much better than non-metals.",
        points=[P("in all solids, vibrating particles pass energy to their neighbours", ["vibrat", "neighbour", "pass on"]),
                P("metals also have free (delocalised) electrons", ["free electrons", "delocalised electrons", "mobile electrons"]),
                P("free electrons move quickly through the metal, carrying energy fast", ["move quickly", "carry energy", "transfer energy quickly", "travel through", "move freely", "fast"])],
        min_points=2,
        model_answer="In all solids, energy is passed on as vibrating particles hit their neighbours, which is slow. Metals also contain free electrons, which move quickly through the metal and carry energy rapidly from the hot end to the cold end.",
        hints=["How do non-metals conduct?", "What extra particles do metals have?", "Why are they effective?"],
        keywords="vibrations (slow); free electrons carry energy quickly",
        sample_pass=["Metals have free electrons that move quickly and carry energy; non-metals only pass energy by vibrations", "vibrating particles pass on energy, but metals also have free electrons that transfer energy fast"],
        sample_fail=["Metals are hotter", "Metals have more atoms"])

written("w8x_conduction_test_ice", 8, 4, "8b",
        stem="Ice is held at the bottom of a test tube of water by a metal gauze. The water near the top is boiled, but the ice does not melt. Explain what this shows.",
        points=[P("water is a poor conductor of heat", ["poor conductor", "bad conductor", "does not conduct well", "insulator"]),
                P("hot water rises, so convection does not carry energy down to the ice", ["hot water rises", "convection", "stays at the top", "does not sink"])],
        model_answer="It shows water is a poor conductor of heat. Convection cannot help either, because the hot water at the top is less dense and stays there, so little energy reaches the ice.",
        hints=["How could energy reach the ice?", "By conduction or convection?", "Why does neither work well here?"],
        keywords="water poor conductor; hot water stays at top (no convection down)",
        sample_pass=["Water is a poor conductor and the hot water rises so convection does not reach the ice", "it shows water is a bad conductor; convection only carries heat upwards"],
        sample_fail=["Ice cannot melt", "The gauze is too cold"])

written("w8x_thermos_cold_drink", 8, 4, "8e",
        stem="A student says a vacuum flask can only keep drinks hot. Explain why it also keeps cold drinks cold.",
        points=[P("the flask reduces energy transfer in both directions", ["both directions", "either direction", "into the flask", "reduces energy transfer", "slows heat transfer"]),
                P("so less energy flows in from the warmer surroundings", ["from the surroundings", "flows in", "into the drink", "warmer surroundings", "gains less"])],
        model_answer="The flask reduces energy transfer by conduction, convection and radiation in both directions. For a cold drink, less energy flows in from the warmer surroundings, so it stays cold.",
        hints=["Does the flask only stop heat leaving?", "Which way does energy flow for a cold drink?", "Link the two."],
        keywords="reduces transfer both ways; less energy flows in",
        sample_pass=["It reduces energy transfer in both directions, so less heat flows in from the surroundings", "the flask slows heat transfer into the cold drink"],
        sample_fail=["It makes the drink colder", "It only works for hot drinks"])

# ---------------------------------------------------------------- L5
written("w8x_eval_radiator_convection", 8, 5, "8c",
        stem="A 'radiator' is fixed under a window. A student says it heats the room mainly by radiation. Evaluate this, and explain how it warms the whole room.",
        points=[P("the statement is mostly wrong: it heats mainly by convection", ["mainly by convection", "mostly convection", "wrong", "convection"]),
                P("air next to it is warmed, expands, becomes less dense and rises", ["less dense", "rises", "warm air rises"]),
                P("cooler air sinks and flows towards it, setting up a convection current round the room", ["sinks", "circulat", "current", "cooler air"])],
        min_points=2,
        model_answer="The student is mostly wrong: a 'radiator' emits some infrared, but it heats the room mainly by convection. Air next to it is warmed, expands, becomes less dense and rises; cooler air sinks and flows in to replace it, setting up a convection current that circulates round the room.",
        hints=["What happens to the air next to it?", "What process moves that warm air?", "So is radiation the main process?"],
        keywords="mainly convection; warm air rises, cool air sinks; circulation",
        sample_pass=["It is mostly convection: warm air rises from it and cooler air sinks, so a current circulates", "wrong, the air is heated, becomes less dense and rises, causing convection currents"],
        sample_fail=["Correct, radiators only radiate", "It heats by conduction through the walls"])

written("w8x_eval_black_kettle", 8, 5, "8d",
        stem="A company advertises a dull black electric kettle as 'keeping water hotter for longer'. Evaluate this claim.",
        points=[P("the claim is wrong", ["wrong", "incorrect", "false", "not true"]),
                P("dull black surfaces are good emitters of infrared, so the water cools faster", ["good emitter", "better emitter", "emits more", "cools faster", "loses heat faster"]),
                P("a shiny surface would keep it hot for longer", ["shiny", "silver", "poor emitter"])],
        min_points=2,
        model_answer="The claim is wrong. A dull black surface is a good emitter of infrared radiation, so the kettle would lose energy faster and the water would cool more quickly. A shiny surface, a poor emitter, would keep the water hot for longer.",
        hints=["Is dull black a good or poor emitter?", "So does it lose energy faster or slower?", "What would be better?"],
        keywords="wrong; black good emitter → cools faster; shiny better",
        sample_pass=["Wrong, dull black is a good emitter so it cools faster; a shiny kettle would keep it hot", "false because black emits more radiation, so it loses heat faster"],
        sample_fail=["True, black absorbs heat", "True because black is warm"])

written("w8x_eval_mixing_claim", 8, 5, "8a",
        stem="A student mixes 100 g of water at 80 °C with 300 g of water at 20 °C and predicts the final temperature will be 50 °C. Evaluate the prediction and give the correct value.",
        points=[P("the prediction is wrong because the masses are not equal", ["wrong", "masses are not equal", "different masses", "not equal masses", "incorrect"]),
                P("energy lost by hot water = energy gained by cold water", ["energy lost", "energy gained", "lost = gained", "loses = gains"]),
                P("final temperature = 35 °C", ["35"])],
        min_points=2,
        model_answer="The prediction is wrong: 50 °C would only be correct for equal masses. Energy lost by the hot water equals the energy gained by the cold water, so the final temperature is (100 × 80 + 300 × 20) ÷ 400 = 35 °C.",
        hints=["When is the simple average correct?", "Energy lost = energy gained.", "Weight the temperatures by mass."],
        keywords="wrong (masses unequal); energy lost = gained; 35 °C",
        sample_pass=["Wrong, the masses are different; energy lost equals energy gained, so it is 35 °C", "incorrect: the final temperature is 35 °C because there is more cold water"],
        sample_fail=["Correct, it is 50 °C", "It will be 80 °C"])

written("w8x_eval_cooling_curve_room", 8, 5, "8a",
        stem="A student leaves a beaker of water at 90 °C in a room at 25 °C and says it will eventually cool to 0 °C. Evaluate the claim.",
        points=[P("the claim is wrong", ["wrong", "incorrect", "false", "not true"]),
                P("it cools only until it reaches room temperature, 25 °C (thermal equilibrium)", ["25", "room temperature", "thermal equilibrium", "same temperature as the room"]),
                P("then there is no temperature difference, so no net energy transfer", ["no temperature difference", "no net transfer", "no net energy", "stops"])],
        min_points=2,
        model_answer="The claim is wrong. The water cools only until it reaches room temperature, 25 °C, when it is in thermal equilibrium with the room. There is then no temperature difference, so there is no net energy transfer and it stops cooling.",
        hints=["What drives the cooling?", "When does it stop?", "What temperature is that?"],
        keywords="wrong; cools to room temperature 25 °C; no difference → no net transfer",
        sample_pass=["Wrong, it only cools to room temperature, 25 °C, then there is no net energy transfer", "it reaches thermal equilibrium at 25 °C and stops"],
        sample_fail=["Correct, all water cools to 0 °C", "It cools to 50 °C"])

written("w8x_eval_house_design", 8, 5, "8e",
        stem="An architect designs a house for a hot, sunny country. Suggest and explain three features that would keep the house cool.",
        points=[P("white or shiny walls/roof reflect radiation (poor absorbers)", ["white", "shiny", "reflect", "light-coloured", "light coloured"]),
                P("insulation in the roof/walls with trapped air reduces conduction", ["insulation", "insulate", "trapped air", "cavity"]),
                P("high vents or windows let hot air escape by convection", ["vent", "high windows", "convection", "hot air escape", "hot air rises"]),
                P("shading / small windows / overhanging roof reduce absorbed sunlight", ["shade", "shading", "overhang", "small windows", "blinds", "trees"])],
        min_points=3,
        model_answer="Paint the walls and roof white or shiny, so they reflect the Sun's radiation and absorb little. Put insulation with trapped air in the roof and walls to reduce conduction inwards. Fit high vents so hot air rises and escapes by convection, and use overhanging roofs or shading to stop sunlight entering.",
        hints=["How can the house absorb less radiation?", "How can it reduce conduction?", "How can hot air escape?"],
        keywords="white/shiny surfaces; insulation; high vents (convection); shading",
        sample_pass=["White walls reflect radiation, insulation with trapped air reduces conduction, and high vents let hot air escape by convection", "a shiny roof, cavity insulation and shading from an overhanging roof"],
        sample_fail=["Black walls and big windows", "Use metal walls"])
