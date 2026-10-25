"""Chapter 11 Electromagnetic Spectrum written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w11x_order_list", 11, 1, "11b",
        stem="List the seven regions of the electromagnetic spectrum in order, starting with the longest wavelength.",
        points=[P("radio waves, microwaves, infrared", ["radio", "microwave", "infrared"]),
                P("visible light, ultraviolet", ["visible", "ultraviolet"]),
                P("X-rays, gamma rays", ["x-ray", "x ray", "gamma"])],
        min_points=3,
        model_answer="Radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays.",
        hints=["Start with the longest wavelength.", "Visible light is in the middle.", "End with the shortest wavelength."],
        keywords="radio, microwave, IR, visible, UV, X-ray, gamma",
        sample_pass=["radio, microwaves, infrared, visible, ultraviolet, X-rays, gamma", "radio waves, microwaves, infrared, visible light, UV (ultraviolet), x rays, gamma rays"],
        sample_fail=["gamma, X-rays, visible", "red, orange, yellow"])

written("w11x_uv_hazard", 11, 1, "11d",
        stem="State one harmful effect of too much exposure to ultraviolet radiation.",
        points=[P("sunburn / skin cancer / eye damage (cataracts) / premature skin ageing", ["sunburn", "skin cancer", "cancer", "eye damage", "cataract", "blind", "ageing", "aging", "burn"])],
        model_answer="It can cause sunburn and increases the risk of skin cancer (it can also damage the eyes).",
        hints=["Think of a long day in the sun.", "What happens to the skin?", "Name one effect."],
        keywords="sunburn; skin cancer; eye damage",
        sample_pass=["skin cancer", "sunburn and damage to the eyes"],
        sample_fail=["It heats the bones", "It makes you deaf"])

written("w11x_xray_hazard", 11, 1, "11d",
        stem="State why X-rays are harmful to living cells.",
        points=[P("they are ionising", ["ionising", "ionizing", "ionise", "ionize", "ionisation"]),
                P("they can damage DNA / cells, causing cancer or mutations", ["dna", "damage cells", "kill cells", "cancer", "mutation", "damage"])],
        model_answer="X-rays are ionising: they can damage the DNA in cells, which can kill the cells or cause cancer.",
        hints=["What do X-rays do to atoms?", "Ionise them.", "What does that do to cells?"],
        keywords="ionising; damage DNA / cancer",
        sample_pass=["They are ionising and can damage DNA, causing cancer", "they ionise atoms and kill cells"],
        sample_fail=["They are hot", "They are loud"])

written("w11x_use_gamma", 11, 1, "11c",
        stem="State one use of gamma rays.",
        points=[P("sterilising medical equipment / food, or treating cancer (radiotherapy)", ["sterilising", "sterilise", "sterilizing", "sterilize", "sterilisation", "cancer", "radiotherapy", "kill bacteria", "tumour", "tumor", "kill cells"])],
        model_answer="Sterilising medical instruments (or treating cancer by radiotherapy).",
        hints=["Gamma rays kill living cells.", "Where is that useful?", "Name one use."],
        keywords="sterilising; radiotherapy",
        sample_pass=["Sterilising surgical instruments", "killing cancer cells in radiotherapy"],
        sample_fail=["Cooking food", "TV remote controls"])

written("w11x_em_vacuum_speed", 11, 1, "11a",
        stem="State two properties shared by all electromagnetic waves.",
        points=[P("they travel at 3.0 × 10⁸ m/s in a vacuum (the same speed)", ["3.0 × 10", "3 × 10", "3.0 x 10", "3 x 10", "same speed", "speed of light", "300 000 000"]),
                P("they are transverse / can travel through a vacuum / transfer energy", ["transverse", "vacuum", "no medium", "transfer energy", "carry energy"])],
        model_answer="They all travel at the same speed, 3.0 × 10⁸ m/s, in a vacuum, and they are all transverse waves that do not need a medium.",
        hints=["Think about their speed.", "Think about the type of wave.", "Do they need a medium?"],
        keywords="same speed c in vacuum; transverse; no medium",
        sample_pass=["They travel at 3.0 × 10⁸ m/s in a vacuum and are transverse", "same speed in a vacuum, and they can travel through a vacuum"],
        sample_fail=["They are all visible", "They are all longitudinal"])

# ---------------------------------------------------------------- L2
written("w11x_em_vs_sound", 11, 2, "11a",
        stem="Give two differences between light waves and sound waves.",
        points=[P("light is transverse; sound is longitudinal", ["transverse", "longitudinal"]),
                P("light can travel through a vacuum; sound needs a medium", ["vacuum", "medium"]),
                P("light is much faster (3 × 10⁸ m/s vs about 340 m/s in air)", ["faster", "3 × 10", "3.0 × 10", "340", "speed"])],
        min_points=2,
        model_answer="Light is a transverse wave, but sound is longitudinal. Light can travel through a vacuum, but sound needs a medium. Light is also far faster: 3.0 × 10⁸ m/s compared with about 340 m/s for sound in air.",
        hints=["Type of wave?", "Medium needed?", "Speed?"],
        keywords="transverse vs longitudinal; vacuum vs medium; speed",
        sample_pass=["Light is transverse and can travel through a vacuum; sound is longitudinal and needs a medium", "light is much faster and does not need a medium"],
        sample_fail=["Light is louder", "Sound is a type of light"])

written("w11x_use_infrared_two", 11, 2, "11c",
        stem="State two uses of infrared radiation.",
        points=[P("one use: remote controls / thermal imaging / grills and toasters / night-vision / optical fibre signals", ["remote", "thermal imaging", "grill", "toaster", "night", "heater", "optical fibre", "intruder"]),
                P("a second, different use", ["remote", "thermal imaging", "grill", "toaster", "night", "heater", "optical fibre", "intruder", "cooking"])],
        min_points=2,
        model_answer="TV remote controls and thermal imaging cameras (also grills, heaters and intruder alarms).",
        hints=["Think of devices at home.", "And of cameras that 'see' heat.", "Two uses."],
        keywords="remote controls; thermal imaging; heating",
        sample_pass=["Remote controls and thermal imaging", "grills for cooking and night-vision cameras"],
        sample_fail=["X-ray photos and sterilising", "Radio broadcasting"])

written("w11x_use_microwaves_two", 11, 2, "11c",
        stem="State two uses of microwaves.",
        points=[P("one use: cooking / mobile phones / satellite communication / Wi-Fi / radar", ["cooking", "oven", "mobile", "phone", "satellite", "wi-fi", "wifi", "radar", "bluetooth"]),
                P("a second, different use", ["cooking", "oven", "mobile", "phone", "satellite", "wi-fi", "wifi", "radar", "bluetooth"])],
        min_points=2,
        model_answer="Cooking food in microwave ovens and communicating with satellites (also mobile phones, Wi-Fi and radar).",
        hints=["Think of the kitchen.", "Think of communication.", "Two uses."],
        keywords="cooking; mobile phones; satellites; radar",
        sample_pass=["Microwave ovens and satellite communication", "mobile phones and radar"],
        sample_fail=["Sunbeds and X-ray photos", "Sterilising instruments"])

written("w11x_visible_position", 11, 2, "11b",
        stem="State where visible light lies in the electromagnetic spectrum, naming the regions on either side, and which colour has the longest wavelength.",
        points=[P("between infrared and ultraviolet", ["infrared", "ultraviolet"]),
                P("red has the longest wavelength", ["red"])],
        model_answer="Visible light lies between infrared and ultraviolet; red light has the longest wavelength of the visible colours.",
        hints=["What is just beyond red?", "What is just beyond violet?", "Which colour has the longest λ?"],
        keywords="between IR and UV; red longest",
        sample_pass=["Between infrared and ultraviolet; red has the longest wavelength", "it is between infrared and UV (ultraviolet), and red is longest"],
        sample_fail=["Between radio and X-rays; violet is longest", "At the end of the spectrum"])

written("w11x_microwave_hazard_written", 11, 2, "11d",
        stem="State one hazard of microwaves and explain how a microwave oven protects the user.",
        points=[P("microwaves can heat body tissue (internal heating / burns)", ["heat", "heating", "burn", "internal"]),
                P("the metal case and door mesh reflect microwaves and keep them inside", ["metal", "mesh", "reflect", "keep them inside", "case"])],
        model_answer="Microwaves can cause internal heating of body tissue. The oven's metal case and the metal mesh in the door reflect the microwaves and keep them inside.",
        hints=["What do microwaves do to water in tissue?", "What stops them leaving the oven?", "Name the parts."],
        keywords="internal heating; metal case/mesh reflects",
        sample_pass=["They heat body tissue; the metal case and mesh reflect them back inside", "internal heating, prevented by the metal walls reflecting microwaves"],
        sample_fail=["They cause cancer; the glass stops them", "They are radioactive"])

# ---------------------------------------------------------------- L3
written("w11x_em_wave_equation", 11, 3, "11a",
        stem="Explain why, for electromagnetic waves in a vacuum, a higher frequency always means a shorter wavelength.",
        points=[P("all EM waves have the same speed in a vacuum (c)", ["same speed", "c is constant", "constant speed", "3.0 × 10", "speed of light"]),
                P("c = f λ, so f × λ is constant / λ = c ÷ f", ["c = f λ", "c = fλ", "f × λ", "f x λ", "λ = c / f", "inversely proportional"])],
        model_answer="All EM waves travel at the same speed c in a vacuum. Since c = f λ, the product f × λ is constant, so a higher frequency means a shorter wavelength.",
        hints=["What is the same for all EM waves?", "Use the wave equation.", "If f increases…"],
        keywords="same speed c; c = f λ",
        sample_pass=["They all have the same speed, and c = f λ, so if f increases λ decreases", "speed is constant so frequency and wavelength are inversely proportional"],
        sample_fail=["Higher frequency waves are faster", "Wavelength does not depend on frequency"])

written("w11x_frequency_trend", 11, 3, "11b",
        stem="Describe how the frequency of EM waves changes from radio waves to gamma rays, and what happens to the energy they carry.",
        points=[P("frequency increases from radio to gamma", ["frequency increases", "increasing frequency", "higher frequency", "frequency rises"]),
                P("the energy carried (per photon) also increases, making them more dangerous", ["energy increases", "more energy", "higher energy", "more dangerous", "more penetrating"])],
        model_answer="The frequency increases from radio waves to gamma rays (and the wavelength decreases). The energy carried by each photon increases too, so the high-frequency end is more penetrating and more dangerous.",
        hints=["Which end has the highest frequency?", "How is energy linked to frequency?", "Link to danger."],
        keywords="frequency increases; energy increases",
        sample_pass=["The frequency increases from radio to gamma and the energy also increases", "higher frequency towards gamma, carrying more energy, so more dangerous"],
        sample_fail=["The frequency decreases", "They all carry the same energy"])

written("w11x_identify_hidden", 11, 3, "11b",
        stem="Fig. 1 shows the electromagnetic spectrum with two regions hidden, P and Q. Name the hidden regions and state one use of each.",
        points=[P("P = microwaves", ["microwave"]),
                P("Q = X-rays", ["x-ray", "x ray"]),
                P("a use of each, e.g. microwaves: cooking/satellites; X-rays: imaging bones/airport security", ["cooking", "satellite", "phone", "bones", "security", "radar", "medical"])],
        min_points=2,
        model_answer="P is microwaves, used for cooking and satellite communication. Q is X-rays, used to image broken bones and for airport security scanners.",
        hints=["Use the order of the spectrum.", "Which region is between radio and infrared?", "Which is between UV and gamma?"],
        keywords="P microwaves; Q X-rays; uses",
        sample_pass=["P is microwaves for cooking and Q is X-rays for seeing broken bones", "microwaves (satellites) and x-rays (airport security)"],
        sample_fail=["P is infrared and Q is gamma", "P is radio and Q is ultraviolet"],
        figure=lambda: sketches.em_spectrum(hidden=["microwaves", "X-rays"]))

written("w11x_airport_xray", 11, 3, "11c",
        stem="Explain how X-rays are used to check luggage at airports.",
        points=[P("X-rays pass through soft materials (clothes, bags)", ["pass through", "penetrate", "go through"]),
                P("dense materials such as metal absorb them, showing up on the screen", ["metal", "dense", "absorb", "shadow", "show up"])],
        model_answer="X-rays pass easily through soft materials such as clothes and bags, but dense materials such as metal absorb them, so metal objects show up as shadows on the screen.",
        hints=["What do X-rays pass through?", "What absorbs them?", "What appears on the screen?"],
        keywords="pass through soft materials; absorbed by dense metal → shadow",
        sample_pass=["X-rays pass through clothes but are absorbed by metal, which shows up on the screen", "dense objects absorb X-rays and appear as shadows, while X-rays pass through the clothes"],
        sample_fail=["X-rays heat the luggage", "X-rays make metal glow"])

written("w11x_gamma_hazard_dose", 11, 3, "11d",
        stem="Explain why workers using gamma-ray sources must keep their exposure time short and stay as far from the source as possible.",
        points=[P("gamma rays are ionising and damage cells / DNA", ["ionising", "ionizing", "damage", "dna", "cancer", "cells"]),
                P("a shorter time means a smaller dose", ["shorter time", "less time", "smaller dose", "less exposure", "dose"]),
                P("greater distance reduces the intensity received", ["distance", "further", "intensity", "weaker"])],
        min_points=2,
        model_answer="Gamma rays are ionising and can damage the DNA in cells, causing cancer. A shorter exposure time means a smaller total dose, and being further away reduces the intensity received, so the risk is reduced.",
        hints=["Why are gamma rays harmful?", "How does time affect dose?", "How does distance affect it?"],
        keywords="ionising; short time → smaller dose; distance → lower intensity",
        sample_pass=["Gamma rays are ionising; less time means a smaller dose and more distance means lower intensity", "they damage DNA, so reduce the dose by spending less time and staying further away"],
        sample_fail=["Gamma rays are hot", "Gamma rays are slow"])

# ---------------------------------------------------------------- L4
written("w11x_ionising_why_dangerous", 11, 4, "11d",
        stem="Explain why ultraviolet, X-rays and gamma rays are more dangerous to living cells than radio waves.",
        points=[P("they have higher frequencies and carry more energy per photon", ["higher frequency", "more energy", "higher energy", "high frequency"]),
                P("so they can ionise atoms in cells", ["ionise", "ionize", "ionising", "ionizing", "ionisation"]),
                P("ionisation damages DNA, which can cause cancer or kill cells", ["dna", "cancer", "kill cells", "mutation", "damage"])],
        min_points=2,
        model_answer="UV, X-rays and gamma rays have much higher frequencies, so each photon carries more energy. They can ionise atoms in cells, damaging DNA, which can kill cells or cause cancer. Radio waves are non-ionising.",
        hints=["Compare their frequencies.", "What can high-energy photons do?", "What does that do to cells?"],
        keywords="higher frequency/energy; ionise; damage DNA",
        sample_pass=["They have higher frequency and more energy so they ionise atoms, damaging DNA", "they are ionising because of their high energy and can cause cancer"],
        sample_fail=["They are faster than radio waves", "Radio waves are louder"])

written("w11x_em_same_speed_evidence", 11, 4, "11a",
        stem="During a solar eclipse, astronomers see light and detect radio waves and X-rays from the Sun's edge change at exactly the same moment. Explain what this shows.",
        points=[P("the different EM waves travel at the same speed", ["same speed", "equal speed", "travel equally fast", "speed of light"]),
                P("through the vacuum of space (they do not need a medium)", ["vacuum", "space", "no medium"])],
        model_answer="It shows that light, radio waves and X-rays all travel at the same speed through the vacuum of space, since they cover the same distance in the same time.",
        hints=["They left the Sun at the same time.", "They arrived at the same time.", "So what about their speeds?"],
        keywords="same speed; through vacuum",
        sample_pass=["All the EM waves travel at the same speed through the vacuum of space", "they have the same speed, the speed of light, in a vacuum"],
        sample_fail=["X-rays are fastest", "Radio waves need air"])

written("w11x_em_transfer_energy", 11, 4, "11a",
        stem="Explain how we know that electromagnetic waves transfer energy, giving one example.",
        points=[P("they can heat objects / cause chemical or electrical changes where absorbed", ["heat", "warm", "absorbed", "chemical", "electrical", "current", "cook"]),
                P("example: sunlight warming the Earth / microwaves cooking food / solar cells generating electricity", ["sun", "solar", "microwave", "cooking", "warms", "photosynthesis"])],
        model_answer="When EM waves are absorbed they cause changes, such as heating: for example, sunlight warms the Earth after crossing space, and microwaves heat food.",
        hints=["What happens when EM waves are absorbed?", "Give an everyday example.", "Energy must arrive."],
        keywords="absorption causes heating/changes; example",
        sample_pass=["They heat things when absorbed, e.g. sunlight warms the Earth", "microwaves cook food, so they must carry energy"],
        sample_fail=["They carry matter", "They are loud"])

written("w11x_order_frequency_explain", 11, 4, "11b",
        stem="A radio wave, a microwave and an X-ray all travel through a vacuum. Explain which has the shortest wavelength and which has the lowest frequency.",
        points=[P("the X-ray has the shortest wavelength", ["x-ray has the shortest", "x-ray shortest", "x-rays have the shortest", "shortest: x-ray", "x ray has the shortest"]),
                P("the radio wave has the lowest frequency", ["radio wave has the lowest", "radio lowest", "radio waves have the lowest", "lowest: radio"]),
                P("same speed, so λ ∝ 1/f / order of the spectrum", ["same speed", "c = f λ", "order", "spectrum"])],
        min_points=2,
        model_answer="The X-ray has the shortest wavelength and the radio wave has the lowest frequency. All travel at the same speed c, so from c = f λ the highest frequency (X-ray) has the shortest wavelength, and the radio wave, with the longest wavelength, has the lowest frequency.",
        hints=["Recall the order of the spectrum.", "Same speed: c = f λ.", "Which is at each end?"],
        keywords="X-ray shortest λ; radio lowest f; c = f λ",
        sample_pass=["The X-ray has the shortest wavelength and the radio wave has the lowest frequency, since c = f λ", "x-rays shortest, radio waves lowest frequency"],
        sample_fail=["The radio wave has the shortest wavelength", "They all have the same wavelength"])

written("w11x_spectrum_continuous", 11, 4, "11b",
        stem="Explain why the boundaries between regions of the EM spectrum (for example between ultraviolet and X-rays) are not sharp.",
        points=[P("the spectrum is continuous (wavelengths change smoothly)", ["continuous", "smoothly", "no gaps", "gradual"]),
                P("regions are named by how the waves are produced or used, so they overlap", ["overlap", "produced", "used", "source", "named"])],
        model_answer="The EM spectrum is continuous: the wavelength changes smoothly from one region to the next. The regions are named by how the waves are produced or used, so neighbouring regions overlap.",
        hints=["Are there gaps between regions?", "How are regions named?", "Can they overlap?"],
        keywords="continuous; named by source/use; overlap",
        sample_pass=["The spectrum is continuous and the regions overlap because they are named by how they are produced", "there are no gaps; regions overlap"],
        sample_fail=["Because the waves have different speeds", "Because X-rays are invisible"])

# ---------------------------------------------------------------- L5
written("w11x_eval_satellite_choice", 11, 5, "11c",
        stem="A company must choose between microwaves and long-wave radio for communicating with a satellite. Evaluate the choice.",
        points=[P("microwaves should be used", ["microwaves", "use microwaves", "microwave"]),
                P("microwaves pass through the ionosphere / atmosphere to reach the satellite", ["pass through", "ionosphere", "atmosphere", "reach the satellite"]),
                P("long radio waves are reflected by the ionosphere / diffract and cannot be beamed narrowly", ["reflected", "reflect", "diffract", "spread out", "cannot reach"])],
        min_points=2,
        model_answer="Microwaves should be used. They pass through the ionosphere and atmosphere to reach the satellite and can be sent as a narrow beam. Long-wave radio waves are reflected by the ionosphere and spread out by diffraction, so they would not reach the satellite.",
        hints=["What happens to each at the ionosphere?", "Which can be aimed narrowly?", "Make a choice."],
        keywords="microwaves; pass through ionosphere; long radio reflected",
        sample_pass=["Use microwaves because they pass through the ionosphere, while long radio waves are reflected", "microwaves reach the satellite; long-wave radio is reflected back down"],
        sample_fail=["Use long-wave radio because it is faster", "It does not matter"])

written("w11x_eval_wavelength_frequency_claim", 11, 5, "11a",
        stem="A student says: 'Gamma rays travel faster than radio waves because they have a higher frequency.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("all EM waves travel at the same speed in a vacuum", ["same speed", "3.0 × 10", "3 × 10", "speed of light", "equal speed"]),
                P("higher frequency gives a shorter wavelength (c = f λ), not a higher speed", ["shorter wavelength", "c = f λ", "wavelength", "not speed"])],
        min_points=2,
        model_answer="The statement is wrong. All EM waves travel at the same speed, 3.0 × 10⁸ m/s, in a vacuum. A higher frequency gives a shorter wavelength (c = f λ), not a higher speed.",
        hints=["Do EM waves have different speeds in a vacuum?", "What does a higher frequency change?", "Use c = f λ."],
        keywords="wrong; same speed; higher f → shorter λ",
        sample_pass=["Wrong, all EM waves have the same speed in a vacuum; higher frequency means shorter wavelength", "incorrect: they travel at 3.0 × 10⁸ m/s, frequency only changes the wavelength"],
        sample_fail=["Correct, higher frequency is faster", "Correct because gamma rays are dangerous"])

written("w11x_eval_em_medium", 11, 5, "11a",
        stem="A student claims that X-rays need air to travel, because they are 'like sound'. Evaluate this claim.",
        points=[P("the claim is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("X-rays are EM waves and can travel through a vacuum", ["vacuum", "em wave", "electromagnetic", "no medium", "space"]),
                P("evidence: X-rays from stars reach telescopes in space / EM waves are transverse unlike sound", ["stars", "telescope", "space", "transverse", "sun"])],
        min_points=2,
        model_answer="The claim is wrong. X-rays are electromagnetic waves, which can travel through a vacuum, unlike sound. X-rays from distant stars reach telescopes in space, where there is no air.",
        hints=["Are X-rays sound waves?", "Do EM waves need a medium?", "Give evidence."],
        keywords="wrong; EM wave, travels in vacuum; evidence from space",
        sample_pass=["Wrong, X-rays are electromagnetic waves which travel through a vacuum; X-rays from stars reach telescopes in space", "incorrect: they need no medium, unlike sound"],
        sample_fail=["Correct, all waves need air", "Correct, X-rays are a type of sound"])

written("w11x_eval_order_from_data", 11, 5, "11b",
        stem="Three EM waves have frequencies of 5 × 10¹⁴ Hz, 3 × 10¹⁰ Hz and 3 × 10¹⁸ Hz. Identify the region of each and explain your reasoning.",
        points=[P("5 × 10¹⁴ Hz: visible light (λ = 6 × 10⁻⁷ m)", ["visible", "light"]),
                P("3 × 10¹⁰ Hz: microwaves (λ = 1 cm)", ["microwave"]),
                P("3 × 10¹⁸ Hz: X-rays (λ = 10⁻¹⁰ m), using λ = c ÷ f", ["x-ray", "x ray", "λ = c", "c ÷ f", "c / f"])],
        min_points=3,
        model_answer="Using λ = c ÷ f: 5 × 10¹⁴ Hz gives λ = 6 × 10⁻⁷ m, visible light; 3 × 10¹⁰ Hz gives λ = 0.01 m, microwaves; 3 × 10¹⁸ Hz gives λ = 10⁻¹⁰ m, X-rays.",
        hints=["Convert each frequency to a wavelength.", "λ = c ÷ f.", "Match to the regions."],
        keywords="λ = c ÷ f; visible, microwaves, X-rays",
        sample_pass=["Visible light, microwaves and X-rays, found from λ = c ÷ f", "5e14 Hz is visible light, 3e10 Hz is microwaves, 3e18 Hz is x-rays because λ = c / f"],
        sample_fail=["All radio waves", "Gamma, infrared, radio"])

written("w11x_eval_uv_uses_risks", 11, 5, "11b",
        stem="Ultraviolet lies next to visible light but is more dangerous. Explain this using its position in the spectrum.",
        points=[P("UV has a higher frequency (shorter wavelength) than visible light", ["higher frequency", "shorter wavelength", "beyond violet"]),
                P("so each photon carries more energy and UV can ionise / damage cells", ["more energy", "ionise", "ionising", "damage", "dna", "cancer"])],
        model_answer="Ultraviolet lies beyond the violet end of the visible spectrum, so it has a higher frequency and shorter wavelength than visible light. Each photon carries more energy, so (high-frequency) UV can ionise atoms and damage skin cells.",
        hints=["Which side of visible light is UV?", "Higher or lower frequency?", "Link frequency to energy and damage."],
        keywords="higher frequency than visible; more energy → damage",
        sample_pass=["UV has a higher frequency than visible light, so it carries more energy and can damage cells", "it has a shorter wavelength and more energy, so it is ionising"],
        sample_fail=["UV is slower than light", "UV is louder"])
