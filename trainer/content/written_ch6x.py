"""Chapter 6 Energy written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w6x_name_stores", 6, 1, "6a",
        stem="Name the main energy store in each of these: (a) a stretched rubber band, (b) a book on a high shelf.",
        points=[P("(a) elastic potential store", ["elastic"]),
                P("(b) gravitational potential store", ["gravitational"])],
        model_answer="(a) Elastic potential store. (b) Gravitational potential store.",
        hints=["What has been done to the rubber band?", "What is special about the book's position?", "Elastic; gravitational."],
        keywords="elastic; gravitational",
        sample_pass=["(a) elastic potential (b) gravitational potential", "elastic store and gravitational store"],
        sample_fail=["kinetic and chemical", "thermal and nuclear"])

written("w6x_conservation_example", 6, 1, "6c",
        stem="A torch is switched on. Its battery transfers 50 J of energy. Only 5 J leaves as light. State what happens to the rest, and which principle this shows.",
        points=[P("45 J is transferred to the surroundings as thermal energy", ["45", "thermal", "heat", "heating", "surroundings"]),
                P("energy is conserved: it cannot be created or destroyed", ["conserved", "conservation", "cannot be created or destroyed", "not created or destroyed"])],
        model_answer="The other 45 J is transferred to the surroundings as thermal energy (heating the torch and the air). This shows the principle of conservation of energy: energy cannot be created or destroyed.",
        hints=["How much is not light?", "Where does it go?", "Which principle says the total stays the same?"],
        keywords="45 J thermal to surroundings; conservation of energy",
        sample_pass=["45 J heats the surroundings; energy is conserved", "the rest becomes thermal energy, showing conservation of energy"],
        sample_fail=["It is destroyed", "It is stored in the torch forever"])

written("w6x_work_needs_motion", 6, 1, "6d",
        stem="A student pushes on a heavy cupboard but it does not move. State how much work is done on the cupboard and explain why.",
        points=[P("zero work is done", ["zero", "no work", "0 j", "none"]),
                P("the cupboard does not move, so there is no distance in the direction of the force", ["does not move", "no distance", "distance is zero", "did not move", "zero distance", "not move"])],
        model_answer="Zero work is done on the cupboard, because work = force × distance moved in the direction of the force, and the cupboard does not move.",
        hints=["Work = force × distance.", "What is the distance moved?", "So what is the work?"],
        keywords="zero; no distance moved",
        sample_pass=["Zero, because the cupboard does not move", "no work is done since the distance is zero"],
        sample_fail=["A lot of work because she pushed hard", "Work = force × time"])

written("w6x_ke_formula", 6, 1, "6b",
        stem="Write down the equation for kinetic energy and state the unit of each quantity.",
        points=[P("KE = ½ m v²", ["1/2 m v2", "½ m v2", "half m v2", "1/2mv2", "½mv2", "0.5 m v2", "half mv2"]),
                P("units: J, kg, m/s", ["j", "joule", "kg", "m/s"])],
        model_answer="KE = ½ m v², where KE is in joules (J), m in kilograms (kg) and v in metres per second (m/s).",
        hints=["It involves mass and speed.", "Speed is squared.", "Give the SI units."],
        keywords="KE = ½ m v²; J, kg, m/s",
        sample_pass=["KE = ½ m v², in J, kg and m/s", "KE = 1/2 m v2 with KE in joules, m in kg and v in m/s"],
        sample_fail=["KE = m g h", "KE = m v"])

written("w6x_gpe_formula", 6, 1, "6b",
        stem="Write down the equation for the gravitational potential energy gained by an object raised through a height, and name each symbol.",
        points=[P("GPE = m g h", ["m g h", "mgh"]),
                P("m = mass, g = gravitational field strength, h = height", ["mass", "gravitational field strength", "height"])],
        model_answer="GPE = m g h, where m is the mass, g is the gravitational field strength and h is the height raised.",
        hints=["Three quantities are multiplied.", "One of them is g.", "Name each symbol."],
        keywords="GPE = m g h; mass, g, height",
        sample_pass=["GPE = m g h where m is mass, g is gravitational field strength and h is height", "mgh: mass times g times height"],
        sample_fail=["GPE = ½ m v²", "GPE = F ÷ A"])

# ---------------------------------------------------------------- L2
written("w6x_catapult_transfer", 6, 2, "6a",
        stem="A catapult fires a stone straight upwards. Describe the energy transfers from the moment it is released until the stone reaches its highest point.",
        points=[P("elastic store of the catapult to kinetic store of the stone", ["elastic", "elastic to kinetic"]),
                P("kinetic store to gravitational potential store as it rises", ["kinetic to gravitational", "gravitational potential", "gravitational"])],
        model_answer="Energy in the elastic store of the stretched catapult is transferred to the kinetic store of the stone. As the stone rises, its kinetic store decreases and its gravitational potential store increases.",
        hints=["What is stored in the stretched catapult?", "What does the stone gain at release?", "What happens as it rises?"],
        keywords="elastic → kinetic → gravitational",
        sample_pass=["Elastic energy becomes kinetic energy, which becomes gravitational potential energy as it rises", "elastic to kinetic to gravitational"],
        sample_fail=["Chemical to nuclear", "Kinetic energy is destroyed as it rises"])

written("w6x_define_efficiency", 6, 2, "6f",
        stem="Define efficiency and write it as an equation.",
        points=[P("useful energy (or power) output", ["useful output", "useful energy output", "useful energy", "useful power"]),
                P("divided by the total energy (or power) input, × 100%", ["total input", "total energy input", "energy input", "input energy", "power input"])],
        model_answer="Efficiency is the ratio of the useful energy output to the total energy input: efficiency = useful energy output ÷ total energy input × 100%.",
        hints=["It compares two energies.", "Useful output and total input.", "Write it as a fraction × 100%."],
        keywords="useful output ÷ total input × 100%",
        sample_pass=["Efficiency = useful output / total input × 100%", "the ratio of useful energy output to total energy input"],
        sample_fail=["Efficiency = power × time", "how fast a machine works"])

written("w6x_wasted_energy_motor", 6, 2, "6f",
        stem="An electric motor lifts a load. State one way energy is wasted and explain why this makes the motor less than 100% efficient.",
        points=[P("energy is wasted as thermal energy due to friction or resistance (or as sound)", ["thermal", "heat", "heating", "friction", "sound", "resistance"]),
                P("so the useful output is less than the input energy", ["less than the input", "useful output is less", "not all", "only part", "less useful"])],
        model_answer="Friction in the bearings and the resistance of the coils waste energy as thermal energy (and some as sound), so the useful output (the load's GPE) is less than the electrical energy input.",
        hints=["Where do moving parts lose energy?", "What form does it take?", "Compare useful output with input."],
        keywords="thermal (friction, resistance) or sound; useful output < input",
        sample_pass=["Friction wastes energy as heat so the useful output is less than the input", "some energy is lost as sound and thermal energy, so not all the input becomes useful"],
        sample_fail=["The motor creates less energy", "Energy is destroyed in the motor"])

written("w6x_name_renewables", 6, 2, "6g",
        stem="Name two renewable and two non-renewable energy resources.",
        points=[P("renewable: two of solar, wind, hydroelectric, tidal, geothermal, biomass, waves", ["solar", "wind", "hydro", "tidal", "geothermal", "biomass", "wave"]),
                P("non-renewable: two of coal, oil, natural gas, nuclear", ["coal", "oil", "natural gas", "gas", "nuclear", "petrol", "diesel"])],
        model_answer="Renewable: solar and wind. Non-renewable: coal and natural gas.",
        hints=["Renewables are replaced naturally.", "Non-renewables run out.", "Two of each."],
        keywords="renewable: solar, wind, hydro…; non-renewable: coal, oil, gas, nuclear",
        sample_pass=["Renewable: solar and wind. Non-renewable: coal and oil", "wind and hydroelectric; natural gas and nuclear fuel"],
        sample_fail=["Electricity and batteries", "Kinetic and potential"])

written("w6x_solar_advantage", 6, 2, "6g",
        stem="State one advantage and one disadvantage of using solar panels to generate electricity.",
        points=[P("advantage: renewable / no carbon dioxide or pollution while working / free energy source", ["renewable", "no carbon dioxide", "no pollution", "does not pollute", "free", "will not run out", "clean"]),
                P("disadvantage: no output at night / depends on weather / needs large area / expensive to set up", ["night", "cloudy", "weather", "large area", "expensive", "depends on sunlight", "unreliable"])],
        model_answer="Advantage: sunlight is renewable and the panels produce no carbon dioxide while working. Disadvantage: they produce no electricity at night and less on cloudy days.",
        hints=["Will sunlight run out?", "Do they pollute?", "When do they not work?"],
        keywords="renewable / no CO₂; not at night / weather / area",
        sample_pass=["It is renewable but does not work at night", "no pollution, but it depends on the weather"],
        sample_fail=["It is cheap and it is noisy", "It uses coal"])

# ---------------------------------------------------------------- L3
written("w6x_power_two_motors", 6, 3, "6e",
        stem="Two motors lift identical loads through the same height. Motor A takes 4 s and motor B takes 8 s. Compare the work done and the power of the two motors.",
        points=[P("the work done is the same", ["same work", "work is the same", "equal work", "work done is equal", "work done is the same"]),
                P("A has twice the power of B (it does the work in half the time)", ["twice the power", "double the power", "a has more power", "a has greater power", "a is more powerful", "half the time"])],
        model_answer="Both motors do the same work (m g h is the same), but A does it in half the time, so A has twice the power of B.",
        hints=["Is m g h the same?", "Power = work ÷ time.", "Compare the times."],
        keywords="same work; A twice the power",
        sample_pass=["The work is the same but A has twice the power", "equal work done; A is more powerful because it takes half the time"],
        sample_fail=["A does more work", "They have the same power"])

written("w6x_efficiency_improve", 6, 3, "6f",
        stem="Suggest two ways to improve the efficiency of a bicycle and explain how each helps.",
        points=[P("oil/lubricate the chain and bearings to reduce friction", ["oil", "lubricate", "grease", "reduce friction", "less friction"]),
                P("pump the tyres up / streamline the rider to reduce resistive forces", ["pump", "tyres", "streamline", "air resistance", "rolling resistance", "crouch"]),
                P("so less energy is wasted as thermal energy", ["less energy wasted", "less wasted", "less thermal", "less heat", "less energy lost"])],
        min_points=2,
        model_answer="Oil the chain and bearings to reduce friction, and pump up the tyres (or crouch to be streamlined) to reduce rolling and air resistance. Both mean less energy is wasted as thermal energy, so more of the rider's input becomes useful kinetic energy.",
        hints=["Where is energy wasted on a bicycle?", "Friction in moving parts.", "Resistive forces from the road and air."],
        keywords="oil (less friction); pump tyres / streamline; less energy wasted",
        sample_pass=["Oil the chain to reduce friction and pump the tyres up; less energy is wasted as heat", "lubricate the bearings and crouch to reduce air resistance so less energy is lost"],
        sample_fail=["Paint it red", "Make it heavier"])

written("w6x_sankey_reading", 6, 3, "6f",
        stem="A filament lamp takes in 100 J each second and gives out 10 J of light. Calculate its efficiency and explain why filament lamps are being replaced by LEDs.",
        points=[P("efficiency = 10 ÷ 100 = 10%", ["10%", "10 %", "0.1", "10 percent"]),
                P("most energy (90 J) is wasted as thermal energy", ["90", "wasted", "thermal", "heat"]),
                P("LEDs are more efficient, so less energy is wasted / less electrical energy needed", ["more efficient", "less energy wasted", "less wasted", "higher efficiency", "use less energy", "less electricity"])],
        min_points=2,
        model_answer="Efficiency = 10 ÷ 100 × 100% = 10%. 90 J of every 100 J is wasted as thermal energy. LEDs are much more efficient, so they give the same light while wasting less energy and needing less electrical energy.",
        hints=["Useful ÷ input × 100%.", "Where does the rest go?", "Why is an LED better?"],
        keywords="10%; 90 J wasted as heat; LEDs more efficient",
        sample_pass=["10%, because 90 J is wasted as heat; LEDs are more efficient", "efficiency is 10%; LEDs waste less energy"],
        sample_fail=["100%", "LEDs are brighter colours"])

written("w6x_coal_problem", 6, 3, "6g",
        stem="Explain two disadvantages of generating electricity by burning coal.",
        points=[P("coal is non-renewable and will run out", ["non-renewable", "run out", "will be used up", "finite", "limited"]),
                P("burning releases carbon dioxide (global warming) or other pollutants", ["carbon dioxide", "co2", "global warming", "climate change", "pollution", "acid rain", "sulfur dioxide"])],
        model_answer="Coal is non-renewable, so supplies will run out. Burning it releases carbon dioxide, which contributes to global warming, and other pollutants such as sulfur dioxide that cause acid rain.",
        hints=["Can coal be replaced?", "What is released when it burns?", "Effect on the environment."],
        keywords="non-renewable; CO₂ / pollution",
        sample_pass=["It is non-renewable and burning it releases carbon dioxide", "coal will run out and it causes pollution and global warming"],
        sample_fail=["Coal is too light", "Coal is renewable"])

written("w6x_hydro_compare", 6, 3, "6g",
        stem="Compare hydroelectric power with wind power as energy resources, giving one similarity and one difference.",
        points=[P("similarity: both are renewable / produce no carbon dioxide while working", ["both renewable", "both are renewable", "renewable", "no carbon dioxide", "no pollution", "both clean"]),
                P("difference: hydro can be controlled/stored and is reliable; wind depends on the weather", ["reliable", "controlled", "stored", "depends on the weather", "wind varies", "not always windy", "on demand"])],
        model_answer="Both are renewable and produce no carbon dioxide while working. However, hydroelectric power can be controlled and stored (water held behind a dam), so it is reliable, while wind power depends on the weather and varies.",
        hints=["Are both renewable?", "Which can be stored or switched on when needed?", "Which depends on the weather?"],
        keywords="both renewable; hydro controllable, wind variable",
        sample_pass=["Both are renewable, but hydro is more reliable because the water can be stored while wind depends on the weather", "both produce no carbon dioxide; wind varies but hydro can be controlled"],
        sample_fail=["Both burn fuel", "Wind is non-renewable"])

# ---------------------------------------------------------------- L4
written("w6x_work_ramp_same", 6, 4, "6d",
        stem="A box is lifted onto a lorry either straight up or by pushing it up a smooth ramp. Explain why the work done against gravity is the same, but the ramp makes the job easier.",
        points=[P("work against gravity = m g h and the height gained is the same", ["m g h", "mgh", "same height", "height is the same"]),
                P("the ramp needs a smaller force over a longer distance", ["smaller force", "less force", "longer distance", "greater distance", "further"])],
        model_answer="The work done against gravity is m g h, and the box gains the same height either way. The ramp lets you use a smaller force over a longer distance, which is easier, although the work is the same.",
        hints=["Which quantity decides the work against gravity?", "Is it the same?", "How does the ramp change force and distance?"],
        keywords="m g h same; smaller force, longer distance",
        sample_pass=["The work m g h is the same because the height is the same, but the ramp needs a smaller force over a longer distance", "same height so same work; less force but a greater distance"],
        sample_fail=["The ramp does less work", "The ramp creates energy"])

written("w6x_power_car_speed", 6, 4, "6e",
        stem="A car travels at a steady speed. Explain why the engine must keep transferring energy even though the kinetic energy of the car does not change.",
        points=[P("work is done against resistive forces (air resistance and friction)", ["air resistance", "friction", "resistive", "drag", "resistance"]),
                P("this energy is transferred to thermal energy of the surroundings", ["thermal", "heat", "heating", "surroundings"])],
        model_answer="At a steady speed the driving force balances air resistance and friction. The engine keeps doing work against these resistive forces, and this energy is transferred to the thermal store of the surroundings.",
        hints=["Which forces oppose the motion?", "Does work get done against them?", "Where does that energy go?"],
        keywords="work against resistive forces; thermal energy to surroundings",
        sample_pass=["The engine does work against air resistance and friction, which heats the surroundings", "energy is needed to overcome resistive forces and becomes thermal energy"],
        sample_fail=["To increase the car's kinetic energy", "Energy is destroyed at steady speed"])

written("w6x_efficiency_power_station", 6, 4, "6f",
        stem="A power station is 35% efficient. Explain what this means and where most of the wasted energy goes.",
        points=[P("35% of the energy from the fuel becomes useful electrical energy", ["35%", "35 %", "useful", "electrical"]),
                P("65% is wasted, mostly as thermal energy to the surroundings (cooling towers, hot gases)", ["65", "wasted", "thermal", "heat", "cooling", "surroundings"])],
        model_answer="Only 35% of the energy released from the fuel is transferred to useful electrical energy. The other 65% is wasted, mostly as thermal energy released to the surroundings through the cooling towers and hot exhaust gases.",
        hints=["What fraction is useful?", "What is the rest?", "Where does it go?"],
        keywords="35% useful electrical; 65% wasted as thermal energy",
        sample_pass=["35% of the input becomes electrical energy and 65% is wasted as heat to the surroundings", "only 35 % is useful; the rest is lost as thermal energy in the cooling towers"],
        sample_fail=["It runs 35% of the day", "35% of the energy is destroyed"])

written("w6x_efficiency_explain_lower", 6, 4, "6f",
        stem="A student measures the efficiency of a pulley system lifting a load as 70%. Explain why the efficiency is less than 100% and suggest one way to increase it.",
        points=[P("work is done against friction in the pulleys (and lifting the rope/pulley)", ["friction", "weight of the pulley", "lifting the pulley", "rope", "resistance"]),
                P("so some input energy is wasted as thermal energy", ["thermal", "heat", "wasted", "lost"]),
                P("improve by lubricating the pulleys or using lighter pulleys", ["lubricate", "oil", "grease", "lighter pulleys", "lighter rope", "reduce friction"])],
        min_points=2,
        model_answer="Some of the input work is done against friction in the pulley bearings and in lifting the pulleys and rope, so this energy is wasted as thermal energy. Lubricating the pulleys (or using lighter pulleys) would increase the efficiency.",
        hints=["What other work does the system do?", "Where does that energy go?", "How could it be reduced?"],
        keywords="friction / lifting pulleys; wasted as heat; lubricate / lighter pulleys",
        sample_pass=["Friction in the pulleys wastes energy as heat; oil the pulleys", "some energy lifts the pulley and is lost to friction; use lighter pulleys"],
        sample_fail=["The load is too heavy", "Energy is destroyed by the rope"])

written("w6x_efficiency_compare_kettles", 6, 4, "6f",
        stem="Kettle P is 90% efficient and kettle Q is 75% efficient. Both have the same power. Explain which boils the same water faster and why.",
        points=[P("P boils it faster", ["p is faster", "kettle p", "p boils", "p faster", "p takes less time"]),
                P("a larger fraction of P's input goes into heating the water, so the water gains energy at a greater rate", ["larger fraction", "more of the energy", "more useful", "greater rate", "less wasted", "less energy wasted"])],
        model_answer="Kettle P boils the water faster. Both take in energy at the same rate, but P transfers a larger fraction (90%) of it to the water and wastes less, so the water gains energy at a greater rate.",
        hints=["Same input power.", "Which transfers more of it to the water?", "Link to time."],
        keywords="P; more of the input heats the water, less wasted",
        sample_pass=["P boils faster, because more of its energy heats the water and less is wasted", "kettle P boils faster as a larger fraction of the input is useful"],
        sample_fail=["Q, because it is less efficient", "They take the same time"])

# ---------------------------------------------------------------- L5
written("w6x_eval_food_energy", 6, 5, "6a",
        stem="A student says: 'When I run, the energy in my food is used up and disappears.' Evaluate this statement and describe where the energy goes.",
        points=[P("the statement is wrong: energy cannot be destroyed", ["wrong", "incorrect", "cannot be destroyed", "not destroyed", "conserved"]),
                P("chemical store of food (muscles) is transferred to kinetic store", ["chemical", "kinetic"]),
                P("and mostly to thermal store of the body and surroundings (and sound)", ["thermal", "heat", "surroundings", "sweat", "sound"])],
        min_points=2,
        model_answer="The statement is wrong: energy is conserved and cannot disappear. Energy in the chemical store of the food (via the muscles) is transferred to the kinetic store of the body, and much of it ends up in the thermal store of the body and the surroundings, with a little as sound.",
        hints=["Can energy disappear?", "Which store is in food?", "Where does it end up?"],
        keywords="wrong, energy conserved; chemical → kinetic → thermal",
        sample_pass=["Wrong, energy is conserved: chemical energy becomes kinetic energy and heat to the surroundings", "incorrect; the chemical store transfers to kinetic and thermal energy"],
        sample_fail=["Correct, the energy is used up", "The energy turns into mass"])

written("w6x_eval_work_carrying", 6, 5, "6d",
        stem="A student carries a heavy bag at constant height along a level corridor and claims she did a lot of work against gravity. Evaluate the claim.",
        points=[P("the claim is wrong: no work is done against gravity", ["wrong", "no work against gravity", "zero work", "not true", "no work"]),
                P("the upward supporting force is perpendicular to the horizontal motion (no vertical distance)", ["perpendicular", "no vertical distance", "height does not change", "does not move upwards", "moves horizontally", "same height"]),
                P("she does get tired because her muscles transfer chemical energy to thermal energy", ["muscles", "chemical", "thermal", "heat", "tired"])],
        min_points=2,
        model_answer="The claim is wrong: no work is done against gravity, because the upward supporting force is perpendicular to the horizontal motion and the bag does not move vertically. She still gets tired because her muscles transfer chemical energy to thermal energy in holding the bag up.",
        hints=["Which way does the supporting force act?", "Which way does the bag move?", "Why does she still get tired?"],
        keywords="wrong; force ⟂ motion, no vertical distance; muscles → thermal",
        sample_pass=["Wrong, the bag stays at the same height so no work is done against gravity; her muscles still use chemical energy", "no work, because the force is perpendicular to the motion"],
        sample_fail=["Correct, the bag is heavy", "She did work equal to weight × distance walked"])

written("w6x_eval_power_rating", 6, 5, "6e",
        stem="A shop says a 2000 W heater 'uses twice as much energy' as a 1000 W heater. Evaluate this statement.",
        points=[P("it transfers energy at twice the rate", ["twice the rate", "twice as fast", "rate", "per second"]),
                P("the total energy depends on how long each is used (E = P t)", ["how long", "time", "e = p t", "p × t", "p x t", "depends on the time"]),
                P("so it is only true if both are on for the same time", ["same time", "only true if", "equal time", "same length of time"])],
        min_points=2,
        model_answer="The 2000 W heater transfers energy at twice the rate of the 1000 W heater. The total energy used depends on the time as well (E = P t), so the statement is only true if both are switched on for the same time.",
        hints=["What does power measure?", "What else decides the total energy?", "When is the statement true?"],
        keywords="twice the rate; E = P t; only if same time",
        sample_pass=["It uses energy at twice the rate, but the total depends on time, E = P t, so only if used for the same time", "only true if both are on for the same time, since energy = power × time"],
        sample_fail=["True, watts are energy", "False, both use the same energy"])

written("w6x_eval_efficiency_hybrid", 6, 5, "6f",
        stem="A hybrid car uses its motor as a generator when braking, charging its battery. Explain why this makes the car more efficient than a normal car.",
        points=[P("in a normal car the kinetic energy is wasted as thermal energy in the brakes", ["wasted", "thermal", "heat", "brakes"]),
                P("the hybrid transfers kinetic energy to the chemical store of the battery", ["chemical store", "battery", "stored", "charges"]),
                P("this stored energy is reused, so less fuel energy is needed for the same useful output", ["reused", "used again", "less fuel", "less input", "more useful"])],
        min_points=2,
        model_answer="In a normal car the kinetic energy is wasted as thermal energy in the brakes. The hybrid transfers much of it to the chemical store of the battery, which is reused later to drive the car, so less fuel energy is needed for the same useful output.",
        hints=["Where does a normal car's KE go when braking?", "Where does the hybrid's go?", "How does that reduce fuel use?"],
        keywords="normal: KE wasted in brakes; hybrid: KE → battery; reused → less fuel",
        sample_pass=["A normal car wastes the kinetic energy as heat in the brakes, but the hybrid stores it in the battery and reuses it, so less fuel is needed", "the energy is stored in the battery and used again instead of being wasted as heat"],
        sample_fail=["Hybrids are lighter", "Batteries create energy"])

written("w6x_eval_efficiency_elevator", 6, 5, "6f",
        stem="Two farmers' elevators lift identical bales to the same loft. Elevator X uses 5000 J per bale and elevator Y uses 4000 J per bale. Explain which is more efficient and suggest why.",
        points=[P("Y is more efficient", ["y is more efficient", "elevator y", "y more efficient", "y is better"]),
                P("same useful output (same m g h) with less energy input", ["same useful", "same m g h", "same work", "less input", "less energy", "same gpe"]),
                P("X wastes more, e.g. more friction or a heavier belt", ["more friction", "friction", "heavier", "wastes more", "more wasted", "more energy wasted"])],
        min_points=2,
        model_answer="Y is more efficient: both give the bale the same useful GPE (m g h), but Y uses less input energy. X probably wastes more energy, for example through more friction in its moving parts or lifting a heavier belt.",
        hints=["Is the useful output the same?", "Which uses less input?", "Why might X waste more?"],
        keywords="Y; same m g h, less input; X has more friction/waste",
        sample_pass=["Y, because it gives the same useful output with less input; X probably has more friction", "elevator Y is more efficient since the same work is done with less energy; X wastes more"],
        sample_fail=["X, because it uses more energy", "They are equally efficient"])
