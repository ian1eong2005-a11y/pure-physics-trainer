"""Chapter 10 General Properties of Waves written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs2, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w10x_cork_bobs", 10, 1, "10b",
        stem="A cork floats on a pond. Ripples pass it. Describe the motion of the cork and state what this shows about waves.",
        points=[P("the cork moves up and down (stays in about the same place)", ["up and down", "bobs", "same place", "does not move along", "oscillates"]),
                P("waves transfer energy without transferring matter", ["transfer energy", "energy is transferred", "carry energy", "not matter", "without transferring", "water does not move along"])],
        model_answer="The cork bobs up and down, staying in about the same place. This shows that waves transfer energy without transferring the water (matter) along with them.",
        hints=["Does the cork travel with the ripples?", "How does it move?", "What does that show?"],
        keywords="bobs up and down; energy transferred, not matter",
        sample_pass=["The cork bobs up and down in the same place, showing waves transfer energy but not matter", "it moves up and down; waves carry energy, the water does not move along"],
        sample_fail=["The cork moves to the shore", "The cork sinks"])

written("w10x_compression_name", 10, 1, "10g",
        stem="Name the regions of a sound wave where the air particles are (a) closest together and (b) furthest apart.",
        points=[P("(a) compressions", ["compression"]),
                P("(b) rarefactions", ["rarefaction"])],
        model_answer="(a) Compressions. (b) Rarefactions.",
        hints=["One region is squashed together.", "The other is spread out.", "Name both."],
        keywords="compression; rarefaction",
        sample_pass=["(a) compression (b) rarefaction", "compressions and rarefactions"],
        sample_fail=["crests and troughs", "peaks and valleys"])

written("w10x_transverse_example", 10, 1, "10e",
        stem="State what is meant by a transverse wave and give one example.",
        points=[P("the vibrations are at right angles (perpendicular) to the direction of travel", ["right angles", "perpendicular", "90"]),
                P("example: light / water waves / waves on a rope / electromagnetic waves", ["light", "water", "rope", "electromagnetic", "radio", "string", "ripple"])],
        model_answer="A transverse wave is one in which the particles vibrate at right angles to the direction the wave travels; for example, light or water ripples.",
        hints=["Which way do the particles vibrate?", "Compared with the direction of travel.", "Give an example."],
        keywords="perpendicular vibration; light, water waves",
        sample_pass=["The vibrations are perpendicular to the direction of travel, e.g. light", "particles vibrate at right angles to the wave's direction, like water waves"],
        sample_fail=["Vibrations along the direction of travel, e.g. sound", "A wave that is fast"])

written("w10x_longitudinal_example", 10, 1, "10e",
        stem="State what is meant by a longitudinal wave and give one example.",
        points=[P("the vibrations are parallel to (along) the direction of travel", ["parallel", "same direction", "along the direction", "back and forth along"]),
                P("example: sound / a slinky pushed in and out", ["sound", "slinky", "spring"])],
        model_answer="A longitudinal wave is one in which the particles vibrate parallel to the direction the wave travels; for example, sound.",
        hints=["Which way do the particles vibrate?", "Compared with the direction of travel.", "Give an example."],
        keywords="parallel vibration; sound",
        sample_pass=["The vibrations are parallel to the direction of travel, e.g. sound", "particles vibrate along the direction the wave travels, like a slinky"],
        sample_fail=["Vibrations at right angles, e.g. light", "A long wave"])

written("w10x_define_period", 10, 1, "10c",
        stem="Define the period of a wave and state its unit.",
        points=[P("the time taken for one complete oscillation (wave)", ["time for one", "time taken for one", "one complete", "one oscillation", "one cycle", "one wave"]),
                P("unit: second (s)", ["second", "s"])],
        model_answer="The period is the time taken for one complete oscillation (one complete wave to pass a point); its unit is the second (s).",
        hints=["It is a time.", "For how much of the wave?", "Unit?"],
        keywords="time for one complete oscillation; s",
        sample_pass=["The time taken for one complete oscillation, in seconds", "time for one wave to pass a point, measured in s"],
        sample_fail=["The number of waves per second", "Hz"])

# ---------------------------------------------------------------- L2
written("w10x_ripple_tank_wavefronts", 10, 2, "10a",
        stem="Fig. 1 shows straight wavefronts in a ripple tank. Describe how you would measure the wavelength accurately.",
        points=[P("measure the distance across several (n) wavefronts", ["several", "many", "across", "a number of", "ten"]),
                P("divide by the number of gaps (wavelengths) between them", ["divide", "number of gaps", "number of wavelengths", "n - 1"])],
        model_answer="Measure the total distance across several wavefronts (for example with a ruler on the screen below, using a stroboscope to freeze them), then divide by the number of gaps between the wavefronts to get one wavelength.",
        hints=["One wavelength is small.", "Measure many at once.", "Divide by the number of gaps."],
        keywords="measure across many wavefronts; divide by number of gaps",
        sample_pass=["Measure the distance across ten wavefronts and divide by the number of gaps", "measure across several wavelengths and divide by how many there are"],
        sample_fail=["Measure the height of a wave", "Count the waves per second"],
        figure=lambda: sketches.wavefronts_sketch(6, "distance across wavefronts"))

written("w10x_frequency_count", 10, 2, "10c",
        stem="Describe how you could measure the frequency of water waves passing a post in a harbour.",
        points=[P("count the number of waves passing the post", ["count", "number of waves", "how many waves"]),
                P("in a measured time (using a stopwatch)", ["time", "stopwatch", "measured time", "seconds"]),
                P("frequency = number ÷ time", ["divide", "number / time", "number of waves / time", "per second"])],
        min_points=2,
        model_answer="Count the number of waves passing the post in a measured time (for example 60 s with a stopwatch), then divide the number of waves by the time to get the frequency.",
        hints=["What does frequency mean?", "Waves per second.", "What do you count and time?"],
        keywords="count waves; measure time; f = n ÷ t",
        sample_pass=["Count the waves passing the post in 60 s with a stopwatch and divide the number by the time", "count how many waves pass in a measured time, then divide"],
        sample_fail=["Measure the height of the waves", "Measure the distance between waves"])

written("w10x_light_vs_sound_type", 10, 2, "10e",
        stem="Compare light and sound in terms of the type of wave and the direction of vibration.",
        points=[P("light is transverse: vibrations perpendicular to the direction of travel", ["light is transverse", "light: transverse", "light transverse"]),
                P("sound is longitudinal: vibrations parallel to the direction of travel", ["sound is longitudinal", "sound: longitudinal", "sound longitudinal"])],
        model_answer="Light is a transverse wave: its vibrations are at right angles to the direction of travel. Sound is a longitudinal wave: its vibrations are parallel to the direction of travel.",
        hints=["Which is transverse?", "Which is longitudinal?", "Describe each vibration."],
        keywords="light transverse; sound longitudinal",
        sample_pass=["Light is transverse with perpendicular vibrations; sound is longitudinal with parallel vibrations", "light transverse, sound longitudinal"],
        sample_fail=["Both are transverse", "Light is longitudinal"])

written("w10x_compression_pressure", 10, 2, "10g",
        stem="Describe how the air pressure varies along a sound wave.",
        points=[P("pressure is higher than normal in compressions", ["higher in compressions", "compressions have higher pressure", "high pressure", "higher pressure"]),
                P("pressure is lower than normal in rarefactions", ["lower in rarefactions", "rarefactions have lower pressure", "low pressure", "lower pressure"])],
        model_answer="The pressure is higher than normal in the compressions, where the particles are crowded together, and lower than normal in the rarefactions, where they are spread out. These regions alternate along the wave.",
        hints=["Where are the particles crowded?", "Where are they spread out?", "Link to pressure."],
        keywords="compressions: higher pressure; rarefactions: lower pressure",
        sample_pass=["The pressure is higher in compressions and lower in rarefactions", "high pressure at compressions and low pressure at rarefactions"],
        sample_fail=["The pressure is the same everywhere", "Pressure is highest in rarefactions"])

written("w10x_pitch_explain", 10, 2, "10h",
        stem="A guitar string is tightened so that its note becomes higher. State what has happened to the frequency of the sound and to its pitch.",
        points=[P("the frequency increases", ["frequency increases", "higher frequency", "frequency is higher", "frequency rises"]),
                P("so the pitch is higher", ["higher pitch", "pitch increases", "pitch is higher", "pitch rises"])],
        model_answer="The frequency of the sound increases, so its pitch is higher.",
        hints=["Pitch is linked to which property?", "Higher note…", "…higher frequency."],
        keywords="frequency increases; pitch higher",
        sample_pass=["The frequency increases so the pitch is higher", "higher frequency gives a higher pitch"],
        sample_fail=["The amplitude increases", "The speed increases"])

# ---------------------------------------------------------------- L3
written("w10x_stadium_wave", 10, 3, "10b",
        stem="In a 'Mexican wave' in a stadium, people stand up and sit down in turn. Explain how this models a wave transferring energy without transferring matter.",
        points=[P("each person only moves up and down in their own place", ["up and down", "own place", "stay in their seats", "do not move along", "same place"]),
                P("the disturbance (pattern) travels around the stadium", ["pattern travels", "disturbance travels", "wave travels", "moves around", "travels around"]),
                P("like a wave, energy moves along but the people (matter) do not", ["energy", "not matter", "people do not travel", "without transferring"])],
        min_points=2,
        model_answer="Each person only moves up and down in their own seat, but the disturbance travels around the stadium. Similarly, in a wave the particles only oscillate about fixed positions while the energy moves along; the matter is not transferred.",
        hints=["How does each person move?", "What travels around the stadium?", "Link to a real wave."],
        keywords="people oscillate in place; pattern travels; energy not matter",
        sample_pass=["Each person moves up and down in the same place but the wave travels around, like energy moving without matter", "the people stay in their seats while the disturbance travels around the stadium"],
        sample_fail=["People run around the stadium", "It shows waves carry people"])

written("w10x_wave_equation_explain", 10, 3, "10d",
        stem="Using the definitions of frequency and wavelength, explain why the speed of a wave is v = f λ.",
        points=[P("f waves pass a point each second", ["f waves", "waves per second", "each second", "every second"]),
                P("each wave is λ long", ["each wave", "λ long", "one wavelength", "length λ"]),
                P("so the wave travels f × λ each second", ["f × λ", "f x λ", "f λ", "distance per second", "each second"])],
        min_points=2,
        model_answer="In one second, f complete waves pass a point and each wave is λ long, so the wave travels a distance of f × λ every second. Speed is distance per second, so v = f λ.",
        hints=["How many waves pass in 1 s?", "How long is each wave?", "Distance in 1 s."],
        keywords="f waves per second × λ each = distance per second",
        sample_pass=["f waves pass each second and each is λ long, so the distance per second is f × λ", "in one second f wavelengths pass, so it travels f λ each second"],
        sample_fail=["Because v = d ÷ t", "Speed is frequency divided by wavelength"])

written("w10x_echo_measure_speed", 10, 3, "10i",
        stem="Describe how to measure the speed of sound using echoes from a large wall.",
        points=[P("stand a measured distance (e.g. 50 m) from the wall", ["measured distance", "measure the distance", "metres from", "measuring tape", "trundle wheel"]),
                P("clap and time the echo (or clap in time with echoes and time many claps)", ["clap", "time", "stopwatch", "echo"]),
                P("speed = 2 × distance ÷ time", ["2 × distance", "2d", "twice the distance", "2 x distance"])],
        min_points=2,
        model_answer="Stand a measured distance, such as 50 m, from a large wall. Clap in time with the echoes and time a large number of claps to find the time for one echo. The speed of sound = 2 × distance ÷ time for one echo.",
        hints=["What distance is measured?", "What is timed?", "How is the speed calculated?"],
        keywords="measured distance; time echo (many claps); v = 2d ÷ t",
        sample_pass=["Stand 50 m from a wall, clap and time the echoes; speed = 2d ÷ t", "measure the distance to the wall, time the echo with a stopwatch, and use twice the distance divided by time"],
        sample_fail=["Measure how loud the echo is", "Use a thermometer"])

written("w10x_sonar_explain", 10, 3, "10j",
        stem="Explain how a ship uses ultrasound to find the depth of the sea.",
        points=[P("a pulse of ultrasound is sent down from the ship", ["pulse", "sends", "emits", "transmitted"]),
                P("it reflects from the sea bed and the echo is detected; the time is measured", ["reflects", "echo", "time", "detected", "returns"]),
                P("depth = speed × time ÷ 2", ["÷ 2", "/ 2", "half", "speed × time", "speed x time"])],
        min_points=2,
        model_answer="A pulse of ultrasound is sent down from the ship. It reflects from the sea bed and the echo is detected back at the ship, and the time taken is measured. The depth = speed of sound in water × time ÷ 2.",
        hints=["What does the ship send out?", "What happens at the sea bed?", "How is depth calculated?"],
        keywords="pulse; echo timed; depth = v t ÷ 2",
        sample_pass=["A pulse of ultrasound is sent down, reflects off the sea bed, and the time is measured; depth = speed × time / 2", "it sends ultrasound, times the echo and halves speed x time"],
        sample_fail=["It uses radar", "The ship measures how loud the sea is"])

written("w10x_ultrasound_medical", 10, 3, "10j",
        stem="Give one medical use of ultrasound and one reason why it is preferred to X-rays for this use.",
        points=[P("use: scanning a foetus / imaging organs / breaking kidney stones / physiotherapy", ["foetus", "baby", "organs", "kidney stones", "scan", "pre-natal", "prenatal", "womb"]),
                P("it is not ionising / does not damage cells / safer", ["not ionising", "non-ionising", "does not damage", "safer", "no radiation", "harmless"])],
        model_answer="Ultrasound is used to scan a foetus in the womb. It is preferred to X-rays because it is not ionising, so it does not damage the cells of the developing baby.",
        hints=["Where is ultrasound used in hospitals?", "Why not X-rays?", "Think about safety."],
        keywords="foetus scanning; non-ionising, safer",
        sample_pass=["Scanning a baby in the womb; it is not ionising so it is safer than X-rays", "pre-natal scans, because ultrasound does not damage cells"],
        sample_fail=["Seeing broken bones", "Because it is cheaper"])

# ---------------------------------------------------------------- L4
written("w10x_ripple_depth_wavelength", 10, 4, "10a",
        stem="Straight water waves pass from deep water into shallow water in a ripple tank. Describe and explain what happens to their speed, frequency and wavelength.",
        points=[P("the speed decreases in shallow water", ["speed decreases", "slow down", "slower", "speed falls"]),
                P("the frequency stays the same (set by the dipper)", ["frequency stays", "same frequency", "frequency is unchanged", "frequency does not change"]),
                P("so the wavelength decreases (v = f λ)", ["wavelength decreases", "shorter wavelength", "wavelength gets shorter", "wavefronts closer"])],
        min_points=2,
        model_answer="The waves slow down in shallow water. The frequency stays the same because it is set by the dipper, so from v = f λ the wavelength decreases and the wavefronts get closer together.",
        hints=["What happens to the speed in shallow water?", "What sets the frequency?", "Use v = f λ."],
        keywords="speed decreases; f unchanged; λ decreases",
        sample_pass=["The speed decreases, the frequency stays the same, so the wavelength decreases", "they slow down; same frequency from the dipper, so shorter wavelength"],
        sample_fail=["The frequency increases", "Everything stays the same"])

written("w10x_graph_compare", 10, 4, "10c",
        stem="Explain how you can find the wavelength and the period of a wave from its graphs, and which graph you need for each.",
        points=[P("wavelength from a displacement–distance graph: distance for one complete wave", ["displacement-distance", "displacement–distance", "distance graph", "against distance"]),
                P("period from a displacement–time graph: time for one complete oscillation", ["displacement-time", "displacement–time", "time graph", "against time"])],
        model_answer="The wavelength is read from a displacement–distance graph, as the distance for one complete wave (e.g. crest to crest). The period is read from a displacement–time graph, as the time for one complete oscillation.",
        hints=["Which graph has distance on the x-axis?", "Which has time?", "Match each quantity."],
        keywords="λ: displacement–distance; T: displacement–time",
        sample_pass=["Wavelength from the displacement-distance graph, period from the displacement-time graph", "use the distance graph for wavelength and the time graph for period"],
        sample_fail=["Both from the same graph", "Period from the distance graph"])

written("w10x_speed_from_medium_change", 10, 4, "10d",
        stem="A sound of frequency 500 Hz passes from air into water. Explain what happens to its frequency, speed and wavelength.",
        points=[P("the frequency stays the same (500 Hz)", ["frequency stays", "same frequency", "frequency is unchanged", "500 hz", "frequency does not change"]),
                P("the speed increases (sound is faster in water)", ["speed increases", "faster", "speeds up", "higher speed"]),
                P("so the wavelength increases (v = f λ)", ["wavelength increases", "longer wavelength", "wavelength gets longer"])],
        min_points=2,
        model_answer="The frequency stays at 500 Hz, because it is set by the source. Sound travels faster in water, so its speed increases, and from v = f λ the wavelength increases.",
        hints=["What sets the frequency?", "Is sound faster in water?", "Use v = f λ."],
        keywords="f unchanged; v increases; λ increases",
        sample_pass=["The frequency stays the same, the speed increases so the wavelength increases", "same 500 Hz, faster in water, longer wavelength"],
        sample_fail=["The frequency increases", "The speed decreases"])

written("w10x_cro_compare", 10, 4, "10h",
        stem="Two sounds are shown on an oscilloscope with the same settings (Fig. 1). The dashed trace is shorter and has fewer waves than the solid trace. Compare the two sounds.",
        points=[P("the dashed sound is quieter (smaller amplitude)", ["quieter", "smaller amplitude", "less loud", "softer"]),
                P("the dashed sound has a lower pitch (lower frequency)", ["lower pitch", "lower frequency", "lower note"])],
        model_answer="The dashed sound has a smaller amplitude, so it is quieter, and fewer waves fit on the screen, so it has a lower frequency and a lower pitch.",
        hints=["What does the height show?", "What does the number of waves show?", "Compare both."],
        keywords="dashed: quieter (amplitude), lower pitch (frequency)",
        sample_pass=["The dashed sound is quieter with a smaller amplitude and has a lower pitch because of its lower frequency", "quieter and lower frequency"],
        sample_fail=["The dashed sound is louder and higher", "They are the same"],
        figure=lambda: figs2.cro_trace(2.5, 3, "same settings for both traces", (5, 1.5)))

written("w10x_echo_errors", 10, 4, "10i",
        stem="A student times a single echo from a wall 50 m away with a stopwatch and gets a poor value for the speed of sound. Explain why, and suggest two improvements.",
        points=[P("the time is very short (about 0.3 s), so reaction time causes a large percentage error", ["reaction time", "short time", "large percentage error", "too short"]),
                P("improvement: time many echoes (clap in rhythm) and divide", ["many", "repeat", "clap in rhythm", "number of claps", "several"]),
                P("improvement: use a greater distance / electronic timing / average repeats", ["greater distance", "further", "electronic", "microphone", "average", "data logger"])],
        min_points=2,
        model_answer="The echo time is very short (about 0.3 s), so the student's reaction time causes a large percentage error. Clap in time with the echoes and time many intervals, then divide; also stand further away or use microphones and electronic timing, and average repeated results.",
        hints=["How long is the echo time?", "What error does a stopwatch have?", "How can timing be improved?"],
        keywords="short time, reaction time; time many echoes; greater distance / electronic timing",
        sample_pass=["The time is too short so reaction time gives a large percentage error; time many claps and stand further away", "reaction time matters; repeat many echoes and use electronic timing"],
        sample_fail=["The wall was too big", "Sound is too fast to measure"])

# ---------------------------------------------------------------- L5
written("w10x_eval_sonar_design", 10, 5, "10j",
        stem="A student suggests using audible sound instead of ultrasound for a ship's sonar. Evaluate this suggestion.",
        points=[P("ultrasound gives a narrower beam / better detail because of its short wavelength", ["shorter wavelength", "short wavelength", "narrow beam", "more detail", "better detail", "directional"]),
                P("audible sound would disturb people and marine life / be confused with background noise", ["disturb", "noise", "background", "marine life", "people can hear", "confused"]),
                P("so ultrasound is the better choice", ["ultrasound is better", "better choice", "suggestion is poor", "not a good idea", "should use ultrasound"])],
        min_points=2,
        model_answer="It is a poor suggestion. Ultrasound has a much shorter wavelength, so it forms a narrow beam and gives more detail of small objects such as fish. Audible sound would be confused with background noise and could disturb people and marine life. Ultrasound is the better choice.",
        hints=["How does wavelength affect detail?", "What about noise?", "Which is better?"],
        keywords="ultrasound: short λ, narrow beam, detail; audible: noise, disturbance",
        sample_pass=["Not a good idea: ultrasound has a short wavelength giving more detail, and audible sound would be confused with background noise", "ultrasound is better because of its narrow beam; audible sound disturbs marine life"],
        sample_fail=["Good idea, audible sound is louder", "No difference"])

written("w10x_eval_ultrasound_cleaning", 10, 5, "10j",
        stem="Jewellers clean rings by placing them in a liquid through which ultrasound is passed. Suggest how this works and why ultrasound is suitable.",
        points=[P("the ultrasound makes the liquid particles vibrate rapidly", ["vibrate", "vibrations", "rapidly", "high frequency"]),
                P("these vibrations shake dirt loose from small gaps", ["dirt", "loosen", "shake", "dislodge", "remove"]),
                P("ultrasound is inaudible / can reach tiny gaps without damaging the ring", ["inaudible", "cannot be heard", "tiny gaps", "small gaps", "without damage", "does not damage"])],
        min_points=2,
        model_answer="The ultrasound makes the particles of the liquid vibrate very rapidly. These vibrations shake dirt loose from tiny gaps in the ring. Ultrasound is suitable because it reaches small gaps without damaging the ring and cannot be heard, so it is not annoying.",
        hints=["What does sound do to the particles of a medium?", "How could that clean a ring?", "Why ultrasound?"],
        keywords="rapid vibrations of liquid; loosen dirt; inaudible, no damage",
        sample_pass=["The ultrasound makes the liquid vibrate rapidly, shaking dirt from small gaps, and it cannot be heard", "high frequency vibrations loosen the dirt without damaging the ring"],
        sample_fail=["Ultrasound heats the ring", "It uses light to clean"])

written("w10x_eval_space_explosion", 10, 5, "10f",
        stem="In many science-fiction films, loud explosions are heard from spaceships in space. Evaluate whether this is realistic.",
        points=[P("it is not realistic", ["not realistic", "unrealistic", "wrong", "not possible", "impossible"]),
                P("space is (almost) a vacuum, with no particles to carry sound", ["vacuum", "no air", "no particles", "no medium"]),
                P("sound needs a medium; the light from the explosion could still be seen", ["needs a medium", "medium", "light can travel", "could be seen", "see the flash"])],
        min_points=2,
        model_answer="It is not realistic. Space is almost a vacuum, with no particles to carry the vibrations, and sound needs a medium to travel. The light from the explosion could still be seen, because light can travel through a vacuum.",
        hints=["What is space like?", "What does sound need?", "What about light?"],
        keywords="not realistic; vacuum, no medium; light still seen",
        sample_pass=["Not realistic because space is a vacuum and sound needs a medium; you would only see the flash", "unrealistic, there is no air to carry the sound in space"],
        sample_fail=["Realistic, explosions are loud", "Sound is faster in space"])

written("w10x_eval_speed_temperature", 10, 5, "10f",
        stem="A student finds the speed of sound in air is slightly greater on a hot day than on a cold day. Suggest an explanation using the particle model.",
        points=[P("on a hot day the air particles move faster", ["move faster", "faster particles", "more kinetic energy", "higher speed"]),
                P("so vibrations are passed on to neighbouring particles more quickly", ["passed on", "more quickly", "transmitted faster", "collide more often", "faster"])],
        model_answer="On a hot day the air particles move faster on average, so they collide more often and pass the vibrations on to neighbouring particles more quickly, making the sound travel faster.",
        hints=["How does temperature affect air particles?", "How is sound passed through air?", "Link the two."],
        keywords="faster particles; vibrations passed on more quickly",
        sample_pass=["The air particles move faster when hot so the vibrations are passed on more quickly", "particles have more kinetic energy and collide more often, transmitting sound faster"],
        sample_fail=["Hot air is denser", "Sound is louder on hot days"])

written("w10x_eval_loud_high", 10, 5, "10h",
        stem="A student says: 'A louder sound always has a higher pitch.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "incorrect", "not true", "false", "disagree"]),
                P("loudness depends on amplitude", ["amplitude"]),
                P("pitch depends on frequency, which can be changed independently", ["frequency", "independent", "separately"])],
        min_points=2,
        model_answer="The statement is wrong. Loudness depends on the amplitude of the wave, while pitch depends on its frequency. These can be changed independently, so a loud sound can have a low pitch.",
        hints=["What decides loudness?", "What decides pitch?", "Are they linked?"],
        keywords="wrong; loudness–amplitude; pitch–frequency; independent",
        sample_pass=["Wrong, loudness depends on amplitude and pitch on frequency, which are independent", "not true: a loud sound can have a low frequency"],
        sample_fail=["Correct, louder sounds are higher", "Correct because they have more energy"])
