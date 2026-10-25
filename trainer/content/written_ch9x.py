"""Chapter 9 Thermal Properties of Matter written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs2
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w9x_internal_energy_define", 9, 1, "9a",
        stem="State the two kinds of energy that make up the internal energy of a substance.",
        points=[P("kinetic energy of the particles", ["kinetic"]),
                P("potential energy of the particles", ["potential"])],
        model_answer="The total kinetic energy and the total potential energy of its particles.",
        hints=["Think about the particles.", "They move and they are held by forces.", "Two kinds of energy."],
        keywords="kinetic + potential energy of particles",
        sample_pass=["The kinetic energy and potential energy of the particles", "kinetic and potential energy of its molecules"],
        sample_fail=["Heat and temperature", "Chemical and nuclear"])

written("w9x_internal_energy_heat", 9, 1, "9a",
        stem="A metal block is heated and its temperature rises. State what happens to its internal energy and to the motion of its particles.",
        points=[P("the internal energy increases", ["internal energy increases", "increases", "more internal energy", "rises", "goes up"]),
                P("the particles vibrate faster (more kinetic energy)", ["vibrate faster", "faster", "more kinetic energy", "vibrate more", "move faster"])],
        model_answer="The internal energy increases, and the particles vibrate faster, with more kinetic energy.",
        hints=["Energy is added.", "Where does it go?", "How do the particles move?"],
        keywords="internal energy increases; particles vibrate faster",
        sample_pass=["The internal energy increases and the particles vibrate faster", "it rises; the particles have more kinetic energy"],
        sample_fail=["It decreases", "The particles stop moving"])

written("w9x_define_shc", 9, 1, "9b",
        stem="Define specific heat capacity.",
        points=[P("the energy needed to raise the temperature", ["energy needed", "energy required", "energy to raise", "thermal energy", "amount of energy"]),
                P("of 1 kg (unit mass) by 1 °C (1 K)", ["1 kg", "one kilogram", "unit mass", "per kilogram", "per kg"]),
                P("by 1 °C or 1 K", ["1 °c", "1 k", "one degree", "1 degree", "by 1"])],
        min_points=3,
        model_answer="The specific heat capacity of a substance is the energy needed to raise the temperature of 1 kg of it by 1 °C (1 K).",
        hints=["It is an amount of energy.", "For what mass?", "For what temperature rise?"],
        keywords="energy to raise 1 kg by 1 °C",
        sample_pass=["The energy needed to raise the temperature of 1 kg of a substance by 1 °C", "energy required per kg to raise the temperature by 1 K"],
        sample_fail=["The energy to melt 1 kg", "How hot something is"])

written("w9x_define_heat_capacity", 9, 1, "9b",
        stem="Define the heat capacity of an object and give its unit.",
        points=[P("the energy needed to raise the temperature of the (whole) object by 1 °C (1 K)", ["energy needed", "energy required", "energy to raise", "by 1", "1 °c", "1 k"]),
                P("unit J/K (or J/°C)", ["j/k", "j/°c", "joules per kelvin", "joule per kelvin", "j k-1"])],
        model_answer="Heat capacity is the energy needed to raise the temperature of the whole object by 1 °C (1 K); its unit is J/K.",
        hints=["It is for the whole object.", "For a 1 °C rise.", "Give the unit."],
        keywords="energy to raise whole object by 1 °C; J/K",
        sample_pass=["The energy needed to raise the temperature of the object by 1 K, in J/K", "energy required to raise it by 1 °C, unit J/°C"],
        sample_fail=["The energy per kg", "J/kg"])

written("w9x_define_latent_vap", 9, 1, "9f",
        stem="Define the specific latent heat of vaporisation of a substance.",
        points=[P("the energy needed to change 1 kg from liquid to gas (vapour)", ["liquid to gas", "liquid to vapour", "liquid into gas", "liquid into vapour", "vaporise", "boil"]),
                P("1 kg (unit mass)", ["1 kg", "one kilogram", "unit mass", "per kilogram", "per kg"]),
                P("without a change in temperature", ["without a change in temperature", "constant temperature", "no change in temperature", "same temperature", "without changing"])],
        min_points=3,
        model_answer="It is the energy needed to change 1 kg of the substance from liquid to gas without a change in temperature.",
        hints=["Which change of state?", "For what mass?", "What stays constant?"],
        keywords="energy to change 1 kg liquid → gas at constant temperature",
        sample_pass=["The energy needed to change 1 kg of liquid to gas without a change in temperature", "energy per kg to turn liquid into vapour at constant temperature"],
        sample_fail=["Energy to raise 1 kg by 1 °C", "Energy to melt a solid"])

written("w9x_define_latent_fusion", 9, 1, "9f",
        stem="Define the specific latent heat of fusion and give its unit.",
        points=[P("the energy needed to change 1 kg from solid to liquid at constant temperature", ["solid to liquid", "solid into liquid", "melt"]),
                P("per kg (1 kg)", ["1 kg", "one kilogram", "unit mass", "per kilogram", "per kg"]),
                P("unit J/kg", ["j/kg", "joules per kilogram", "joule per kilogram"])],
        min_points=3,
        model_answer="It is the energy needed to change 1 kg of a substance from solid to liquid without a change in temperature; its unit is J/kg.",
        hints=["Fusion means melting.", "Per kilogram.", "Unit?"],
        keywords="energy to melt 1 kg at constant temperature; J/kg",
        sample_pass=["The energy needed to change 1 kg from solid to liquid without changing temperature, J/kg", "energy per kg to melt a solid at constant temperature, unit J/kg"],
        sample_fail=["Energy to boil a liquid", "J/(kg K)"])

written("w9x_evap_factors_l1", 9, 1, "9e",
        stem="State two factors that increase the rate of evaporation of a liquid.",
        points=[P("one factor: higher temperature / larger surface area / moving air (wind) / lower humidity", ["temperature", "surface area", "wind", "air movement", "moving air", "humidity", "fan", "draught"]),
                P("a second, different factor", ["temperature", "surface area", "wind", "air movement", "moving air", "humidity", "fan", "draught"])],
        min_points=2,
        model_answer="A higher temperature and a larger surface area (also moving air and low humidity).",
        hints=["Think about drying clothes.", "What helps them dry faster?", "Two factors."],
        keywords="temperature; surface area; wind; humidity",
        sample_pass=["Higher temperature and a larger surface area", "wind and low humidity"],
        sample_fail=["Making it heavier", "Using a smaller container"])

written("w9x_evap_cooling_l1", 9, 1, "9e",
        stem="State what happens to the temperature of a liquid that is evaporating, if no energy is supplied to it.",
        points=[P("its temperature falls (it cools)", ["falls", "decreases", "cools", "goes down", "drops", "lower"])],
        pitfalls=[PF(["rises", "increases"], "Evaporation COOLS the liquid left behind.")],
        model_answer="Its temperature falls: evaporation cools the liquid left behind.",
        hints=["Which molecules escape?", "What is left behind?", "Hotter or cooler?"],
        keywords="temperature falls",
        sample_pass=["It cools down", "the temperature decreases"],
        sample_fail=["It gets hotter", "It stays the same"])

# ---------------------------------------------------------------- L2
written("w9x_internal_more_particles", 9, 2, "9a",
        stem="A large and a small block of the same iron are at the same temperature. Explain which has more internal energy.",
        points=[P("the large block has more internal energy", ["large block", "larger block", "bigger block", "the large one", "larger one"]),
                P("it has more particles, each with the same average energy", ["more particles", "more atoms", "more molecules", "more mass"])],
        model_answer="The large block has more internal energy: at the same temperature each particle has the same average energy, but the large block has more particles.",
        hints=["Same temperature → same average particle energy.", "Which has more particles?", "Total energy."],
        keywords="large block; more particles",
        sample_pass=["The large block, because it has more particles", "the bigger block has more atoms so more internal energy"],
        sample_fail=["They are the same because they are at the same temperature", "The small block"])

written("w9x_boiling_flat", 9, 2, "9d",
        stem="Water is heated steadily until it boils. Explain why its temperature stays at 100 °C while it boils.",
        points=[P("the energy supplied is used to change the state (latent heat)", ["latent heat", "change of state", "change state", "boil", "turn into steam"]),
                P("it separates the molecules / increases their potential energy, not their kinetic energy", ["potential energy", "separate", "break", "overcome", "forces between", "not kinetic"])],
        model_answer="The energy supplied is used as latent heat to change the water into steam: it separates the molecules, increasing their potential energy, rather than their kinetic energy, so the temperature stays constant.",
        hints=["Where does the energy go?", "Not into raising the temperature.", "Into separating molecules."],
        keywords="latent heat; increases PE, not KE",
        sample_pass=["The energy is used as latent heat to separate the molecules, so the temperature stays the same", "the energy is latent heat: it increases the potential energy of the molecules, not the kinetic energy"],
        sample_fail=["The heater stops", "Water cannot go above 100 °C because it is hot"])

written("w9x_boil_vs_evap", 9, 2, "9e",
        stem="State two differences between boiling and evaporation.",
        points=[P("boiling at the boiling point; evaporation at any temperature", ["boiling point", "any temperature", "all temperatures", "fixed temperature"]),
                P("boiling throughout the liquid (bubbles); evaporation only at the surface", ["throughout", "surface", "bubbles"])],
        model_answer="Boiling happens only at the boiling point, while evaporation happens at any temperature. Boiling happens throughout the liquid, with bubbles, while evaporation happens only at the surface.",
        hints=["At what temperature does each happen?", "Where in the liquid?", "Two differences."],
        keywords="temperature; surface vs throughout",
        sample_pass=["Boiling happens at the boiling point throughout the liquid; evaporation happens at any temperature at the surface", "evaporation is only at the surface at any temperature, boiling forms bubbles at a fixed temperature"],
        sample_fail=["They are the same", "Boiling is faster"])

written("w9x_sweat_cooling", 9, 2, "9e",
        stem="Explain how sweating helps to cool the body.",
        points=[P("sweat evaporates from the skin", ["evaporates", "evaporation"]),
                P("the most energetic molecules escape, taking energy (latent heat) from the skin", ["most energetic", "fastest", "latent heat", "takes energy", "absorbs energy", "from the skin"])],
        model_answer="Sweat evaporates from the skin. The most energetic molecules escape, and the energy (latent heat) needed for evaporation is taken from the skin, cooling the body.",
        hints=["What happens to the sweat?", "Which molecules escape?", "Where does the energy come from?"],
        keywords="evaporation; energetic molecules escape; energy taken from skin",
        sample_pass=["Sweat evaporates and takes latent heat from the skin", "the sweat evaporates; the fastest molecules escape, taking energy from the skin"],
        sample_fail=["Sweat is cold", "Sweat reflects heat"])

written("w9x_shc_explain_sand", 9, 2, "9b",
        stem="On a sunny day, sand on a beach gets much hotter than the sea. Explain this in terms of specific heat capacity.",
        points=[P("water has a much higher specific heat capacity than sand", ["higher specific heat capacity", "larger specific heat capacity", "water has a high", "sand has a low", "lower specific heat capacity"]),
                P("so for the same energy, water has a smaller temperature rise", ["smaller temperature rise", "smaller rise", "heats up more slowly", "less temperature rise", "warms more slowly", "rises less"])],
        model_answer="Water has a much higher specific heat capacity than sand, so for the same energy absorbed per kilogram, the water's temperature rises much less than the sand's.",
        hints=["Compare the specific heat capacities.", "Same energy per kg.", "Which rises more?"],
        keywords="water high c; smaller temperature rise",
        sample_pass=["Water has a higher specific heat capacity so it has a smaller temperature rise", "sand has a low specific heat capacity, so it heats up more for the same energy while water warms more slowly"],
        sample_fail=["Sand is darker", "The sea is deeper"])

written("w9x_shc_measure_steps", 9, 2, "9b",
        stem="Fig. 1 shows a block with a heater and a thermometer. List the measurements needed to find the specific heat capacity of the block.",
        points=[P("the mass of the block", ["mass"]),
                P("the energy supplied (power × time, or a joulemeter reading)", ["power", "time", "energy supplied", "joulemeter", "voltage", "current"]),
                P("the starting and final temperatures (temperature rise)", ["temperature", "initial", "final", "rise"])],
        min_points=3,
        model_answer="Measure the mass of the block, the energy supplied by the heater (its power and the time it is on, or a joulemeter reading), and the starting and final temperatures to find the temperature rise.",
        hints=["c = Q ÷ (m Δθ).", "What do you need for each quantity?", "Three measurements."],
        keywords="mass; energy (P t); initial and final temperatures",
        sample_pass=["The mass of the block, the power and time of the heater, and the initial and final temperatures", "mass, energy supplied from a joulemeter and the temperature rise"],
        sample_fail=["The colour of the block", "The volume only"],
        figure=lambda: figs2.heater_block(["mass = ?", "power = ?", "time = ?", "Δθ = ?"]))

written("w9x_cooling_curve_describe", 9, 2, "9i",
        stem="Describe the shape of the cooling curve of a liquid that solidifies as it cools.",
        points=[P("the temperature first falls as the liquid cools", ["falls", "decreases", "drops", "goes down"]),
                P("it stays constant (flat) while the liquid solidifies", ["constant", "flat", "stays the same", "horizontal", "levels off"]),
                P("then falls again as the solid cools", ["falls again", "decreases again", "then falls", "drops again", "solid cools"])],
        min_points=2,
        model_answer="The temperature falls as the liquid cools, then stays constant (a flat section) while it solidifies, and then falls again as the solid cools.",
        hints=["What happens while it is liquid?", "While it solidifies?", "Afterwards?"],
        keywords="falls; flat while solidifying; falls again",
        sample_pass=["It falls, then stays constant while solidifying, then falls again", "the temperature decreases, levels off at the freezing point, then drops again"],
        sample_fail=["It rises steadily", "A straight line downwards"])

written("w9x_cooling_curve_freezing_point", 9, 2, "9i",
        stem="Explain how to find the freezing point of a substance from its cooling curve.",
        points=[P("find the flat (horizontal) section of the curve", ["flat", "horizontal", "constant", "levels off"]),
                P("read the temperature of that section", ["read", "temperature"])],
        model_answer="Find the flat (horizontal) section of the cooling curve, where the temperature stays constant, and read off that temperature: it is the freezing point.",
        hints=["Which part shows solidifying?", "What is constant there?", "Read it."],
        keywords="flat section; read its temperature",
        sample_pass=["Find the flat part of the curve and read the temperature there", "the freezing point is the temperature of the horizontal section"],
        sample_fail=["Read the final temperature", "Read the starting temperature"])

# ---------------------------------------------------------------- L3
written("w9x_melting_vs_heating", 9, 3, "9d",
        stem="A heating curve for ice has a sloping section and a flat section. Explain what the energy supplied is doing in each section.",
        points=[P("sloping section: raises the temperature / increases the kinetic energy of the particles", ["kinetic energy", "raises the temperature", "temperature rises", "speeds up", "vibrate faster"]),
                P("flat section: changes the state / increases the potential energy (breaks bonds)", ["potential energy", "change of state", "change the state", "breaks", "overcome", "latent heat"])],
        model_answer="In the sloping section, the energy increases the kinetic energy of the particles, so the temperature rises. In the flat section, the energy is used as latent heat to change the state, increasing the particles' potential energy by overcoming the forces between them, so the temperature stays constant.",
        hints=["What rises in the sloping part?", "What happens in the flat part?", "KE vs PE."],
        keywords="slope: KE, temperature rises; flat: PE, change of state",
        sample_pass=["In the sloping part the kinetic energy increases and the temperature rises; in the flat part the energy increases potential energy to change the state", "slope: particles speed up; flat: latent heat breaks the bonds"],
        sample_fail=["The energy is lost in the flat section", "Both sections raise the temperature"])

written("w9x_latent_freezing_release", 9, 3, "9h",
        stem="Explain, in terms of particles, why energy is released when water freezes.",
        points=[P("the molecules move closer and form bonds / are held in fixed positions", ["fixed positions", "form bonds", "closer together", "held together", "attractive forces"]),
                P("their potential energy decreases, so energy is released", ["potential energy decreases", "lose potential energy", "less potential energy", "energy is released", "releases energy"])],
        model_answer="As water freezes, the molecules are pulled into fixed positions by attractive forces, forming bonds. Their potential energy decreases, and this energy is released to the surroundings as latent heat.",
        hints=["What happens to the molecules' arrangement?", "What happens to their PE?", "Where does the energy go?"],
        keywords="molecules bond into fixed positions; PE decreases; energy released",
        sample_pass=["The molecules form bonds in fixed positions, so their potential energy decreases and energy is released", "they move closer together and lose potential energy, which is released"],
        sample_fail=["The molecules stop moving and lose all energy", "Ice is cold"])

written("w9x_evap_factors_explain", 9, 3, "9e",
        stem="Explain, using the particle model, why a puddle dries faster on a hot, windy day.",
        points=[P("higher temperature: more molecules have enough energy to escape", ["more molecules", "enough energy", "more energy", "faster molecules", "higher temperature"]),
                P("wind removes vapour molecules so fewer return to the liquid", ["removes", "blows away", "carries away", "fewer return", "do not return"])],
        model_answer="At a higher temperature more molecules have enough energy to escape from the surface. The wind blows the vapour molecules away, so fewer return to the liquid, and evaporation is faster.",
        hints=["How does temperature affect the molecules?", "What does the wind do to the vapour?", "Combine."],
        keywords="more molecules with enough energy; wind removes vapour",
        sample_pass=["More molecules have enough energy to escape when hot, and the wind blows the vapour away so fewer return", "higher temperature gives faster molecules; wind carries away the vapour"],
        sample_fail=["The wind pushes the water away", "The Sun boils the puddle"])

written("w9x_evap_cools_particles", 9, 3, "9e",
        stem="Explain, in terms of molecules, why a liquid cools as it evaporates.",
        points=[P("the most energetic (fastest) molecules escape from the surface", ["most energetic", "fastest", "higher energy", "more energy", "faster molecules"]),
                P("so the average kinetic energy of the remaining molecules falls", ["average kinetic energy", "average falls", "remaining", "left behind", "lower average"]),
                P("so the temperature falls", ["temperature falls", "temperature decreases", "cools", "lower temperature"])],
        min_points=2,
        model_answer="The most energetic molecules escape from the surface, so the average kinetic energy of the molecules left behind falls, and the temperature of the liquid falls.",
        hints=["Which molecules escape?", "What happens to the average of those left?", "Link to temperature."],
        keywords="fastest escape; average KE of rest falls; temperature falls",
        sample_pass=["The fastest molecules escape, so the average kinetic energy of those left falls and it cools", "the most energetic molecules leave, lowering the average and the temperature"],
        sample_fail=["The liquid loses heat to the air", "The molecules get smaller"])

written("w9x_latent_measure_ice", 9, 3, "9f",
        stem="Outline how to measure the specific latent heat of fusion of ice using a heater, a funnel of crushed ice and a balance.",
        points=[P("put the heater in crushed ice at 0 °C in a funnel and collect the meltwater in a beaker", ["funnel", "beaker", "collect", "meltwater", "crushed ice"]),
                P("measure the energy supplied (P × t or joulemeter) and the mass of water melted", ["energy", "joulemeter", "power", "time", "mass"]),
                P("use a control funnel without a heater; L = E ÷ (m_heater − m_control)", ["control", "subtract", "e / m", "l = e", "divide"])],
        min_points=2,
        model_answer="Place a heater in crushed ice at 0 °C in a funnel and collect the meltwater in a beaker on a balance. Measure the energy supplied (power × time or with a joulemeter) and the mass melted. A control funnel with no heater shows how much melts from the room; subtract this, then L = E ÷ m.",
        hints=["How is the ice melted and collected?", "What two quantities are measured?", "Why use a control?"],
        keywords="heater in ice, collect meltwater; measure E and m; control; L = E ÷ m",
        sample_pass=["Melt crushed ice in a funnel with a heater, collect the water, measure the energy and mass, use a control and divide E by m", "measure the mass of meltwater and the joulemeter reading; subtract the control funnel's mass and divide"],
        sample_fail=["Heat ice in a pan and use a thermometer", "Weigh the ice only"])

written("w9x_latent_steam_scald_written", 9, 3, "9f",
        stem="Explain why a scald from steam at 100 °C is more serious than one from the same mass of boiling water at 100 °C.",
        points=[P("steam condenses on the skin", ["condenses", "condensation"]),
                P("releasing its latent heat of vaporisation (a large amount of energy)", ["latent heat", "extra energy", "more energy", "releases energy", "large amount of energy"]),
                P("in addition to the energy released as the water cools", ["as well as", "in addition", "then cools", "also cools"])],
        min_points=2,
        model_answer="When steam touches the skin it condenses, releasing its latent heat of vaporisation, a large amount of energy. The water formed then also cools, releasing more energy, so steam gives much more energy to the skin than boiling water.",
        hints=["What does steam do on cool skin?", "What extra energy is released?", "Compare with water."],
        keywords="condenses; releases latent heat; plus cooling",
        sample_pass=["Steam condenses and releases latent heat, then the water also cools", "it releases a large amount of energy when it condenses on the skin"],
        sample_fail=["Steam is hotter than 100 °C", "Steam moves faster"])

written("w9x_cooling_curve_explain_flat", 9, 3, "9i",
        stem="A liquid loses energy steadily to the surroundings as it cools, yet its temperature stays constant for a while. Explain why.",
        points=[P("the liquid is solidifying (freezing)", ["solidifying", "freezing", "solidifies", "turning to solid", "change of state"]),
                P("latent heat is released, replacing the energy lost", ["latent heat", "energy released", "releases energy", "replaces"])],
        model_answer="The liquid is solidifying. As it does so, latent heat is released when the particles form bonds, and this replaces the energy lost to the surroundings, so the temperature stays constant.",
        hints=["What change of state is happening?", "Is energy released?", "Balance with the loss."],
        keywords="solidifying; latent heat released balances loss",
        sample_pass=["It is solidifying and the latent heat released replaces the energy lost", "freezing releases energy so the temperature stays the same"],
        sample_fail=["It has stopped losing energy", "The thermometer is broken"])

written("w9x_cooling_curve_purity", 9, 3, "9i",
        stem="The cooling curve of a liquid has no clear flat section; instead, the temperature falls slowly over a range. Suggest what this tells you about the liquid.",
        points=[P("the liquid is not pure / is a mixture", ["not pure", "impure", "mixture", "contains impurities", "salt"]),
                P("a pure substance freezes at a single fixed temperature", ["single temperature", "fixed temperature", "one temperature", "pure substances"])],
        model_answer="It suggests the liquid is impure (a mixture), because a pure substance freezes at a single fixed temperature, giving a clear flat section.",
        hints=["How does a pure substance freeze?", "At one temperature.", "So what if it doesn't?"],
        keywords="impure; pure freezes at a fixed temperature",
        sample_pass=["It is impure, because a pure substance freezes at one fixed temperature", "it is a mixture; pure substances have a single freezing point"],
        sample_fail=["It is very pure", "It has no latent heat"])

# ---------------------------------------------------------------- L4
written("w9x_internal_energy_boiling", 9, 4, "9a",
        stem="Water at 100 °C turns into steam at 100 °C. State and explain what happens to its internal energy.",
        points=[P("the internal energy increases", ["increases", "rises", "goes up", "more internal energy"]),
                P("the potential energy of the molecules increases (they separate), while the average KE stays the same", ["potential energy", "separate", "further apart", "average kinetic energy stays", "same temperature"])],
        model_answer="The internal energy increases. The temperature, and so the average kinetic energy of the molecules, stays the same, but the molecules separate, so their potential energy increases.",
        hints=["Is energy supplied?", "Does the temperature change?", "Which part of internal energy changes?"],
        keywords="internal energy increases; PE increases, KE constant",
        sample_pass=["It increases because the potential energy of the molecules increases as they separate", "the internal energy rises; the molecules move further apart so their potential energy goes up"],
        sample_fail=["It stays the same because the temperature is constant", "It decreases"])

written("w9x_latent_boiling_particles", 9, 4, "9h",
        stem="Explain, in terms of particles, why much more energy is needed to boil 1 kg of water than to melt 1 kg of ice.",
        points=[P("in boiling, molecules are separated completely, far apart", ["separated completely", "far apart", "completely separate", "break all"]),
                P("in melting, molecules only loosen and stay close together", ["close together", "only loosen", "stay close", "partly", "some bonds"]),
                P("so boiling requires a much larger increase in potential energy (L_v > L_f)", ["more energy", "larger increase", "potential energy", "much more"])],
        min_points=2,
        model_answer="In melting, the molecules only loosen from fixed positions and remain close together. In boiling, they must be separated completely and pushed far apart against the attractive forces, which needs a much larger increase in potential energy, so L_v is much greater than L_f.",
        hints=["How far apart are molecules in a liquid?", "And in a gas?", "Compare the energy needed."],
        keywords="melting: loosen, stay close; boiling: separate fully → more PE",
        sample_pass=["Boiling separates the molecules far apart while melting only loosens them, so boiling needs more energy", "in melting they stay close together; boiling separates them completely, a bigger increase in potential energy"],
        sample_fail=["Boiling is at a higher temperature", "Steam is heavier"])

written("w9x_cooling_curve_insulation", 9, 4, "9i",
        stem="Two equal masses of molten wax cool in identical tubes, one wrapped in cotton wool. Predict and explain how their cooling curves differ.",
        points=[P("the flat sections are at the same temperature", ["same temperature", "same freezing point", "same level"]),
                P("the insulated tube cools more slowly / its flat section lasts longer", ["more slowly", "longer", "lasts longer", "slower", "takes longer"]),
                P("because energy is lost to the surroundings at a lower rate", ["lower rate", "loses energy more slowly", "less energy lost", "insulation"])],
        min_points=2,
        model_answer="Both flat sections are at the same temperature (the freezing point of wax). The insulated tube loses energy at a lower rate, so its curve is less steep and its flat section lasts longer.",
        hints=["Does insulation change the freezing point?", "How does it change the rate of energy loss?", "Effect on the curve?"],
        keywords="same freezing temperature; insulated: slower, longer flat section",
        sample_pass=["The flat parts are at the same temperature but the insulated one lasts longer because it loses energy more slowly", "same freezing point; the wrapped tube cools more slowly"],
        sample_fail=["The insulated tube freezes at a higher temperature", "They are identical"])

written("w9x_evap_cold_drink_pot", 9, 4, "9e",
        stem="Water in an unglazed clay pot stays cool in hot weather because some water seeps through and evaporates from the outside. Explain how this keeps the water cool.",
        points=[P("water evaporates from the outer surface", ["evaporates", "evaporation"]),
                P("evaporation needs latent heat / the most energetic molecules leave", ["latent heat", "energetic", "fastest", "energy"]),
                P("this energy is taken from the pot and the water inside, lowering its temperature", ["from the pot", "from the water", "cools", "lowers the temperature", "takes energy"])],
        min_points=2,
        model_answer="Water evaporates from the outer surface of the pot. Evaporation needs latent heat, as the most energetic molecules escape; this energy is taken from the pot and the water inside, so their temperature falls.",
        hints=["What happens on the outside of the pot?", "What does evaporation need?", "Where does it come from?"],
        keywords="evaporation from surface; needs latent heat; taken from water inside",
        sample_pass=["Water evaporates from the outside, taking latent heat from the pot and the water inside", "the most energetic molecules evaporate, so energy is taken from the water, which cools"],
        sample_fail=["Clay is cold", "The pot reflects sunlight"])

written("w9x_evap_alcohol_skin", 9, 4, "9e",
        stem="A drop of alcohol on the skin feels much colder than a drop of water at the same temperature. Suggest why.",
        points=[P("alcohol evaporates faster than water", ["evaporates faster", "evaporates more quickly", "faster evaporation", "more volatile", "evaporates more"]),
                P("so it takes energy from the skin at a greater rate", ["greater rate", "faster", "more energy", "takes energy", "from the skin"])],
        model_answer="Alcohol evaporates much faster than water, so it takes energy (latent heat) from the skin at a greater rate, making the skin feel colder.",
        hints=["Which liquid evaporates faster?", "What does evaporation take from the skin?", "Link to the rate."],
        keywords="alcohol evaporates faster; takes energy from skin faster",
        sample_pass=["Alcohol evaporates faster, taking energy from the skin more quickly", "it evaporates more quickly so it removes more energy from the skin"],
        sample_fail=["Alcohol is colder", "Alcohol is denser"])

written("w9x_shc_coolant_choice", 9, 4, "9b",
        stem="An engineer must choose between water and oil as a coolant for an engine. Explain why water's higher specific heat capacity is an advantage.",
        points=[P("water can absorb more energy per kg for each degree rise", ["more energy", "absorbs more", "per kg", "per degree"]),
                P("so its temperature rises less / less coolant is needed", ["rises less", "smaller temperature rise", "less coolant", "smaller mass", "stays cooler"])],
        model_answer="Because water has a higher specific heat capacity, each kilogram absorbs more energy for each degree rise. Its temperature therefore rises less for the same energy, or a smaller mass of coolant is needed.",
        hints=["What does a high c mean?", "Same energy absorbed…", "…what happens to Δθ?"],
        keywords="more energy per kg per °C; smaller rise / less coolant",
        sample_pass=["Water absorbs more energy per kg so its temperature rises less", "it can take in more energy for a smaller temperature rise"],
        sample_fail=["Water is cheaper", "Water is a good conductor"])

written("w9x_shc_errors", 9, 4, "9b",
        stem="A student's measured specific heat capacity of an aluminium block is higher than the accepted value. Suggest two reasons and one improvement.",
        points=[P("energy was lost to the surroundings", ["lost to the surroundings", "energy lost", "heat lost", "losses"]),
                P("the thermometer was not in good thermal contact / read before the temperature evened out", ["thermal contact", "oil", "even out", "not in contact", "read too early"]),
                P("improvement: insulate the block / add oil in the thermometer hole", ["insulate", "lagging", "oil", "cover"])],
        min_points=2,
        model_answer="Energy from the heater was lost to the surroundings, so the measured temperature rise was too small; and the thermometer may not have been in good thermal contact. Insulate the block and put a little oil in the thermometer hole.",
        hints=["What makes Δθ too small?", "Is the thermometer reading the block's temperature?", "How to fix each?"],
        keywords="energy lost; poor thermal contact; insulate, oil",
        sample_pass=["Energy was lost to the surroundings and the thermometer had poor thermal contact; insulate the block", "heat lost to the air; put oil in the hole and insulate"],
        sample_fail=["The block was too light", "The heater was too powerful"])

# ---------------------------------------------------------------- L5
written("w9x_eval_internal_claim", 9, 5, "9a",
        stem="A student says: 'Two objects at the same temperature always contain the same amount of internal energy.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false", "disagree"]),
                P("same temperature means the same average KE per particle", ["average kinetic energy", "average", "per particle", "same average"]),
                P("internal energy also depends on the number of particles (mass), material and state", ["number of particles", "mass", "material", "state", "more particles"])],
        min_points=2,
        model_answer="The statement is wrong. The same temperature only means the same average kinetic energy per particle. Internal energy is the total energy of all the particles, so it also depends on the number of particles (mass), the material and its state.",
        hints=["What does temperature tell you?", "Is internal energy an average or a total?", "What else matters?"],
        keywords="wrong; same average KE; depends on mass, material, state",
        sample_pass=["Wrong, same temperature means the same average kinetic energy, but internal energy depends on the mass and material", "not true; a larger object with more particles has more internal energy"],
        sample_fail=["Correct, temperature is internal energy", "Correct, they are equal"])

written("w9x_eval_heating_curve_claim", 9, 5, "9d",
        stem="A student heats ice with a heater and finds the temperature stays at 0 °C for a long time. They conclude the energy is being 'lost'. Evaluate this conclusion.",
        points=[P("the conclusion is wrong / the energy is not lost", ["wrong", "not lost", "incorrect", "disagree"]),
                P("the energy is used as latent heat to melt the ice", ["latent heat", "melt", "change of state", "change state"]),
                P("it increases the potential energy of the molecules, not their kinetic energy", ["potential energy", "not kinetic", "separate", "break bonds"])],
        min_points=2,
        model_answer="The conclusion is wrong. The energy is not lost: it is used as latent heat to melt the ice, increasing the potential energy of the molecules rather than their kinetic energy, so the temperature stays at 0 °C until all the ice has melted.",
        hints=["What is happening at 0 °C?", "Where does the energy go?", "KE or PE?"],
        keywords="wrong; latent heat melts ice; PE not KE",
        sample_pass=["Wrong, the energy is used as latent heat to melt the ice, increasing potential energy", "not lost: it changes the state, so the temperature stays the same"],
        sample_fail=["Correct, the energy escapes", "The thermometer is broken"])

written("w9x_eval_latent_particles", 9, 5, "9h",
        stem="A student says: 'When ice melts, the energy supplied makes the molecules move faster.' Evaluate this statement using the particle model.",
        points=[P("the statement is wrong: the temperature is constant, so the average KE does not change", ["wrong", "temperature is constant", "temperature stays", "kinetic energy does not change", "same kinetic energy"]),
                P("the energy overcomes the attractive forces, increasing the potential energy", ["potential energy", "overcome", "break", "forces between", "attractive forces"]),
                P("the molecules leave their fixed positions and can move past each other", ["fixed positions", "move past", "slide past", "lattice"])],
        min_points=2,
        model_answer="The statement is wrong. While ice melts its temperature stays at 0 °C, so the average kinetic energy of the molecules does not change. The energy is used to overcome the attractive forces holding the molecules in fixed positions, increasing their potential energy, so they can move past one another.",
        hints=["Does the temperature change while melting?", "Then does average KE change?", "Where does the energy go?"],
        keywords="wrong; KE constant; PE increases as bonds break",
        sample_pass=["Wrong, the temperature is constant so the kinetic energy does not change; the energy overcomes the forces between molecules, increasing potential energy", "incorrect: the molecules leave their fixed positions as the energy breaks bonds"],
        sample_fail=["Correct, the molecules speed up", "The molecules expand"])

written("w9x_eval_refrigerator", 9, 5, "9h",
        stem="A refrigerator uses a liquid that evaporates in pipes inside the cabinet and condenses in pipes at the back. Explain, in terms of particles and latent heat, how this moves energy out of the cabinet.",
        points=[P("evaporation inside absorbs latent heat from the cabinet (molecules separate, PE increases)", ["evaporates inside", "absorbs", "takes energy", "inside the cabinet"]),
                P("condensation at the back releases latent heat to the room (PE decreases)", ["condenses", "releases", "back", "room", "surroundings"]),
                P("so energy is carried from inside to outside", ["carried", "transferred", "moved", "from inside to outside", "out of the cabinet"])],
        min_points=2,
        model_answer="Inside the cabinet the liquid evaporates: its molecules separate, gaining potential energy, and the latent heat needed is taken from the cabinet, cooling it. At the back the vapour condenses: the molecules come together, losing potential energy, and the latent heat is released to the room. So energy is carried from inside to outside.",
        hints=["What does evaporation need?", "What does condensation release?", "Where does each happen?"],
        keywords="evaporation inside absorbs latent heat; condensation outside releases it",
        sample_pass=["The liquid evaporates inside, absorbing latent heat from the cabinet, and condenses at the back, releasing it to the room", "evaporation takes energy from inside; condensation releases energy outside, so energy is carried out"],
        sample_fail=["The fridge makes cold", "The motor removes heat by itself"])

written("w9x_eval_evap_vs_boil_claim", 9, 5, "9e",
        stem="A student says: 'Water can only turn into a gas when it reaches 100 °C.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("water evaporates from its surface at any temperature", ["evaporates", "evaporation", "any temperature", "below 100"]),
                P("100 °C is the boiling point, when it turns to gas throughout (bubbles)", ["boiling", "throughout", "bubbles", "boiling point"])],
        min_points=2,
        model_answer="The statement is wrong. Water evaporates from its surface at any temperature (puddles dry without boiling). At 100 °C it boils, turning into gas throughout the liquid with bubbles.",
        hints=["Do puddles boil?", "How do they become a gas?", "What happens at 100 °C?"],
        keywords="wrong; evaporation at any temperature; boiling at 100 °C",
        sample_pass=["Wrong, water evaporates from the surface at any temperature; 100 °C is the boiling point", "not true, evaporation happens below 100 °C, boiling happens at 100 °C throughout"],
        sample_fail=["Correct, water needs 100 °C", "Water never becomes a gas"])

written("w9x_eval_evap_experiment", 9, 5, "9e",
        stem="A student wants to show that surface area affects the rate of evaporation. Describe a fair experiment.",
        points=[P("use dishes of different surface areas with the same volume (mass) of water", ["different surface areas", "different widths", "same volume", "same mass", "same amount"]),
                P("keep temperature, air movement and humidity the same", ["same temperature", "same place", "same air", "same room", "control"]),
                P("measure the mass lost after the same time", ["mass lost", "measure the mass", "weigh", "same time", "volume left"])],
        min_points=2,
        model_answer="Put the same volume of water in dishes with different surface areas, placed side by side so the temperature, air movement and humidity are the same. Weigh each dish at the start and after the same time to find the mass lost; the dish with the larger area should lose more.",
        hints=["What should change?", "What should stay the same?", "What should be measured?"],
        keywords="vary area, same volume; control conditions; measure mass lost in same time",
        sample_pass=["Use dishes with different surface areas but the same volume of water in the same room, and weigh them after the same time", "same amount of water, different widths, same temperature; measure the mass lost"],
        sample_fail=["Heat one dish more than the other", "Use different liquids"])

written("w9x_eval_shc_claim", 9, 5, "9b",
        stem="A student says: 'A substance with a high specific heat capacity always gets hotter than one with a low specific heat capacity.' Evaluate this.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("a high c means a SMALLER temperature rise for the same energy and mass", ["smaller temperature rise", "smaller rise", "heats up less", "heats more slowly", "less temperature rise"]),
                P("the final temperature also depends on the energy supplied and the mass", ["energy supplied", "mass", "depends on"])],
        min_points=2,
        model_answer="The statement is wrong. For the same energy and mass, a substance with a high specific heat capacity has a SMALLER temperature rise. How hot each gets also depends on the energy supplied and the mass.",
        hints=["Δθ = Q ÷ (m c).", "What does a larger c do to Δθ?", "What else matters?"],
        keywords="wrong; high c → smaller rise; depends on Q and m",
        sample_pass=["Wrong, a high specific heat capacity gives a smaller temperature rise for the same energy and mass", "not true: high c heats up less, and it also depends on the mass"],
        sample_fail=["Correct, high c means hotter", "Correct, it stores more heat so it is hotter"])

written("w9x_eval_shc_design_kettle", 9, 5, "9b",
        stem="A designer wants a kettle body that warms up as little as possible while boiling water. Explain whether the material should have a high or a low heat capacity, and why.",
        points=[P("a low heat capacity (small mass × c)", ["low heat capacity", "small heat capacity", "low specific heat capacity", "small mass"]),
                P("so less energy is wasted heating the kettle body itself, and more goes into the water", ["less energy", "less wasted", "more energy to the water", "more efficient", "less energy is used"])],
        model_answer="It should have a low heat capacity (a small mass of a material with low c), so that less of the energy supplied is wasted in heating the kettle body itself and more goes into heating the water.",
        hints=["Heat capacity = m c.", "What happens to energy that heats the kettle body?", "Which choice wastes less?"],
        keywords="low heat capacity; less energy wasted heating the kettle",
        sample_pass=["A low heat capacity so less energy is wasted heating the kettle and more goes to the water", "small heat capacity, making it more efficient"],
        sample_fail=["High heat capacity so it stays hot", "It does not matter"])
