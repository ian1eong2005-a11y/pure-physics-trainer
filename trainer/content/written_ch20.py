"""Chapter 20 Radioactivity: written-answer questions, two per level (atomic structure, isotopes, nature of radiation,
randomness, half-life, background radiation, uses and hazards, fission and fusion)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w20_define_isotope", 20, 1, "20b",
        stem="State what is meant by isotopes of an element.",
        points=[P("atoms (nuclei) with the same proton number", ["same proton number", "same number of protons", "same atomic number", "same z"]),
                P("but different nucleon numbers / different numbers of neutrons", ["different number of neutrons", "different neutron", "different nucleon number", "different mass number", "different numbers of neutrons", "different a"])],
        pitfalls=[PF(["different number of protons", "different proton number", "different atomic number"], "Isotopes of the SAME element have the same number of protons; it is the number of neutrons that differs.")],
        model_answer="Isotopes are atoms of the same element that have the same proton number (number of protons) but different nucleon numbers, i.e. different numbers of neutrons.",
        hints=["Isotopes belong to the same element. What does that fix?", "What can differ between them?", "Same protons, different neutrons."],
        keywords="same proton number, different number of neutrons (nucleon number)",
        sample_pass=["Atoms with the same number of protons but different numbers of neutrons", "same proton number but a different nucleon number"],
        sample_fail=["Atoms with different numbers of protons", "Atoms that are radioactive"])

written("w20_atom_structure", 20, 1, "20a",
        stem="Fig. 1 shows a model of an atom. Describe the structure of an atom.",
        points=[P("a small, positively charged nucleus at the centre", ["nucleus", "positive nucleus", "positively charged nucleus", "centre"]),
                P("containing protons (positive) and neutrons (no charge)", ["protons and neutrons", "protons", "neutrons"]),
                P("surrounded by negatively charged electrons", ["electrons", "negative electrons", "orbit", "surrounded by electrons", "shells"])],
        model_answer="An atom has a tiny, positively charged nucleus at its centre, made of protons (positive) and neutrons (uncharged), surrounded by negatively charged electrons.",
        hints=["What is at the centre, and what charge does it have?", "What two particles make up the nucleus?", "What surrounds the nucleus?"],
        keywords="positive nucleus of protons and neutrons, surrounded by negative electrons",
        figure=lambda: figs3.atom_diagram(3, 4, "lithium-7"),
        sample_pass=["A positive nucleus of protons and neutrons with electrons around it", "a nucleus containing protons and neutrons, surrounded by negatively charged electrons"],
        sample_fail=["A ball of positive charge with electrons stuck in it like a pudding", "Only electrons and neutrons"])

# ---------------------------------------------------------------- L2
written("w20_nature_alpha_beta_gamma", 20, 2, "20e",
        stem="State what alpha, beta and gamma radiation are.",
        points=[P("alpha: a helium nucleus (2 protons + 2 neutrons)", ["helium nucleus", "2 protons and 2 neutrons", "two protons and two neutrons", "helium"]),
                P("beta: a fast-moving electron (emitted from the nucleus)", ["fast electron", "electron", "high-speed electron", "fast-moving electron"]),
                P("gamma: electromagnetic radiation (a high-energy wave)", ["electromagnetic", "em wave", "wave", "high energy wave", "electromagnetic radiation", "photon"])],
        model_answer="An alpha particle is a helium nucleus, made of 2 protons and 2 neutrons. A beta particle is a fast-moving electron emitted from the nucleus. Gamma radiation is high-energy electromagnetic radiation.",
        hints=["Two are particles and one is a wave.", "Alpha is a nucleus of which element? Beta is which particle?", "Gamma is part of which spectrum?"],
        keywords="alpha: helium nucleus; beta: fast electron; gamma: electromagnetic wave",
        sample_pass=["Alpha is a helium nucleus, beta is a fast electron and gamma is an electromagnetic wave", "2 protons and 2 neutrons; a high speed electron; electromagnetic radiation"],
        sample_fail=["Alpha is an electron, beta is a proton and gamma is a neutron", "They are all types of sound"])

written("w20_random_spontaneous", 20, 2, "20d",
        stem="Radioactive decay is described as random and spontaneous. Explain what each of these words means.",
        points=[P("random: it is impossible to predict which nucleus will decay next, or when a particular nucleus will decay", ["cannot predict", "impossible to predict", "not predictable", "which nucleus", "when a particular", "chance"]),
                P("spontaneous: it is not affected by external conditions such as temperature, pressure or chemical reactions", ["not affected", "temperature", "pressure", "external", "cannot be changed", "cannot be speeded up", "chemical"])],
        model_answer="Random means it is impossible to predict which particular nucleus will decay next, or when; only the average behaviour of a large number is predictable. Spontaneous means the decay is not affected by external conditions such as temperature, pressure or chemical combination.",
        hints=["Can you say which nucleus will decay next?", "Can heating or squeezing a sample change its rate of decay?", "Explain both words."],
        keywords="random: cannot predict which or when; spontaneous: unaffected by temperature, pressure, chemistry",
        sample_pass=["Random means you cannot predict which nucleus will decay or when; spontaneous means it is not affected by temperature or pressure",
                     "it is impossible to predict when a nucleus decays, and external conditions do not change the rate"],
        sample_fail=["Random means it happens at the same rate always; spontaneous means it happens quickly", "Heating a sample makes it decay faster"])

# ---------------------------------------------------------------- L3
written("w20_define_half_life", 20, 3, "20h",
        stem="Fig. 1 shows a decay curve. Define half-life and describe how to find it from the curve.",
        points=[P("half-life is the time taken for half of the radioactive nuclei in a sample to decay (or for the activity/count rate to halve)", ["time taken for half", "half of the nuclei", "half the nuclei", "activity to halve", "count rate to halve", "fall to half"]),
                P("from the curve: read the initial count rate, halve it, find the time at which the curve reaches that value", ["halve", "half of the initial", "read across", "read off the time", "find the time", "go across to the curve"])],
        model_answer="The half-life is the time taken for half of the radioactive nuclei in a sample to decay, so that the activity (count rate) falls to half its value. On the curve, read the initial count rate, halve it, go across to the curve at that value and read down to find the time: that time is the half-life.",
        hints=["Half-life is a time. The time for what?", "On the graph, which value do you look for?", "Define it, then describe the reading."],
        keywords="time for half the nuclei to decay (activity halves); halve initial value, read time from curve",
        figure=lambda: figs3.decay_curve(800, 5, 25),
        sample_pass=["The time for half the nuclei to decay; halve the starting count rate and read the time from the curve", "time for the activity to fall to half; read across from half the initial value to the curve and down"],
        sample_fail=["Half the time it takes for a sample to stop being radioactive", "The time when the curve reaches zero"])

written("w20_background_sources", 20, 3, "20g",
        stem="State what is meant by background radiation, give two sources of it, and explain why it must be taken into account when measuring the half-life of a weak source.",
        points=[P("background radiation is the low level of ionising radiation that is always present around us", ["always present", "all around", "low level", "naturally present", "everywhere"]),
                P("sources: radon gas, rocks and soil, cosmic rays, food and drink, medical X-rays, nuclear industry", ["radon", "rocks", "granite", "soil", "cosmic", "food", "medical", "buildings", "space"]),
                P("the background count must be subtracted from every reading to get the count rate due to the source alone", ["subtract", "take away", "corrected", "minus the background", "deduct"])],
        min_points=2,
        model_answer="Background radiation is the low level of ionising radiation that is always present around us. Sources include radon gas from rocks and soil, cosmic rays from space, and radioactive substances in food and building materials. When measuring the half-life of a weak source, the background count rate must be measured and subtracted from every reading, so that the corrected count rate is due to the source alone.",
        hints=["Is there radiation even when no source is near the detector?", "Where does it come from?", "What do you do with it when analysing readings?"],
        keywords="always present radiation; radon, rocks, cosmic rays, food; subtract background from readings",
        sample_pass=["Radiation that is always around us, from radon gas and cosmic rays; it must be subtracted from each reading", "background comes from rocks and space and is present everywhere, so subtract it to get the corrected count"],
        sample_fail=["Radiation from mobile phones that can be ignored", "Background radiation is only found near nuclear power stations"])

# ---------------------------------------------------------------- L4
written("w20_ionising_vs_penetrating", 20, 4, "20e",
        stem="Fig. 1 shows the penetrating powers of alpha, beta and gamma radiation. Compare their ionising effects and explain how penetrating power is related to ionising power.",
        points=[P("alpha is the most strongly ionising, beta moderate, gamma weakly ionising", ["alpha is the most ionising", "alpha most strongly ionising", "alpha ionises the most", "gamma least ionising", "gamma weakly ionising", "beta moderate"]),
                P("alpha is the least penetrating (stopped by paper); gamma the most penetrating (reduced by thick lead)", ["stopped by paper", "least penetrating", "most penetrating", "thick lead", "aluminium"]),
                P("strongly ionising radiation loses its energy quickly in creating ions, so it travels only a short distance: the more ionising, the less penetrating", ["loses energy quickly", "loses its energy", "short distance", "more ionising the less penetrating", "inverse", "uses up its energy"])],
        min_points=2,
        model_answer="Alpha particles are the most strongly ionising, beta particles are moderately ionising and gamma rays are only weakly ionising. Alpha is the least penetrating, stopped by a sheet of paper; beta is stopped by a few millimetres of aluminium; gamma is only reduced by thick lead. Strongly ionising radiation loses its energy quickly as it creates ions along its path, so it cannot travel far: the more ionising the radiation, the less penetrating it is.",
        hints=["Rank the three for ionising power and for penetrating power.", "What does each absorber in the figure stop?", "Why would strongly ionising radiation not get far?"],
        keywords="ionising: α > β > γ; penetrating: γ > β > α; ionising uses up energy quickly, so more ionising = less penetrating",
        figure=lambda: figs3.penetration(),
        sample_pass=["Alpha is the most ionising but least penetrating, stopped by paper, gamma is the least ionising but most penetrating; the more ionising, the faster it loses its energy so the less it penetrates",
                     "alpha ionises strongly and loses energy quickly so travels a short distance; gamma ionises weakly and penetrates thick lead"],
        sample_fail=["Gamma is the most ionising and is stopped by paper", "All three have the same ionising power"])

written("w20_choose_tracer", 20, 4, "20i",
        stem="A doctor needs a radioactive tracer to inject into a patient so that it can be detected from outside the body. Explain what type of radiation and what half-life the tracer should have.",
        points=[P("gamma emitter: gamma penetrates the body and can be detected outside", ["gamma", "penetrate", "pass through the body", "detected outside", "escape the body"]),
                P("gamma is weakly ionising, so it does less damage to cells than alpha or beta inside the body", ["weakly ionising", "less ionising", "less damage", "not ionising much", "alpha would damage", "alpha cannot escape"]),
                P("short half-life (hours to a few days): long enough to complete the test but decays quickly so the patient is not exposed for long", ["short half-life", "few hours", "hours", "decays quickly", "not exposed for long", "long enough"])],
        min_points=2,
        model_answer="The tracer should emit gamma radiation, which penetrates the body and can be detected outside it, and which is only weakly ionising, so it causes less damage to cells than alpha or beta would. It should have a short half-life, of a few hours to a few days: long enough for the test to be carried out, but short enough that the activity in the patient falls quickly and exposure is minimised.",
        hints=["Which radiation can escape the body to reach a detector, and which would damage cells?", "Too long a half-life keeps the patient radioactive; too short and it decays before the test.", "State the radiation and half-life with reasons."],
        keywords="gamma: penetrates, detectable outside, weakly ionising; short half-life (hours): enough for test, quick decay",
        sample_pass=["A gamma emitter because it passes out of the body and is weakly ionising, with a short half-life of a few hours so it does not stay in the body long",
                     "gamma so it can be detected outside and causes less damage; short half-life so the patient's exposure is small"],
        sample_fail=["An alpha emitter with a half-life of thousands of years", "Any radiation is fine because it is only a small amount"])

# ---------------------------------------------------------------- L5
written("w20_fission_vs_fusion", 20, 5, "20j",
        stem="Compare nuclear fission and nuclear fusion, and state how each releases energy.",
        points=[P("fission: a large (heavy) nucleus such as uranium-235 splits into two smaller nuclei (and neutrons), usually after absorbing a neutron", ["large nucleus splits", "heavy nucleus splits", "splits into two", "uranium", "splitting", "neutron"]),
                P("fusion: two small (light) nuclei such as hydrogen isotopes join to form a larger nucleus, as in the Sun", ["light nuclei join", "small nuclei join", "join together", "combine", "hydrogen", "sun", "fuse"]),
                P("both release a large amount of energy because the products have less mass / the nuclei rearrange into a more stable state; the energy appears as kinetic energy of the products and radiation", ["release energy", "large amount of energy", "kinetic energy", "more stable", "energy is released", "releases energy"])],
        min_points=2,
        model_answer="In nuclear fission a large, heavy nucleus such as uranium-235 absorbs a neutron and splits into two smaller nuclei, releasing further neutrons. In nuclear fusion two small, light nuclei such as isotopes of hydrogen join to form a larger nucleus, as in the Sun. Both processes release a large amount of energy, which appears mainly as kinetic energy of the products and as gamma radiation.",
        hints=["One process splits a big nucleus, the other joins small ones.", "Give an example of each.", "What do both processes release, and in what form?"],
        keywords="fission: heavy nucleus splits (uranium, neutron); fusion: light nuclei join (hydrogen, Sun); both release large energy",
        sample_pass=["Fission is a heavy nucleus like uranium splitting into two smaller nuclei; fusion is light nuclei like hydrogen joining, as in the Sun; both release a lot of energy",
                     "in fission a large nucleus splits when hit by a neutron, in fusion small nuclei combine; both release energy as kinetic energy of the products"],
        sample_fail=["Fission joins nuclei and fusion splits them", "Both are chemical reactions that burn fuel"])

written("w20_evaluate_storage_claim", 20, 5, "20i",
        stem="A student says: 'Radioactive waste with a long half-life is safer than waste with a short half-life, because it decays more slowly.' Evaluate this statement.",
        points=[P("partly true: for the same number of nuclei, a long half-life means a lower activity (fewer decays per second) at any moment", ["lower activity", "fewer decays per second", "less active", "partly true", "decays more slowly so less", "less per second", "emits less", "less radiation per second"]),
                P("but it remains radioactive (hazardous) for a very long time, possibly thousands of years, so it must be stored securely for that long", ["remains radioactive", "stays radioactive", "thousands of years", "long time", "for a long time", "stored for"]),
                P("short half-life waste is intensely active at first but decays to a safe level quickly; safety also depends on the type of radiation and how it is stored", ["intensely active", "very active", "decays quickly", "short time", "type of radiation", "storage", "depends"])],
        min_points=2,
        model_answer="The statement is only partly true. For the same number of nuclei, waste with a long half-life has a lower activity, so it emits less radiation per second. However, it stays radioactive for a very long time, possibly thousands of years, so it must be stored securely and monitored for all that time. Short half-life waste is intensely active at first but decays to a safe level quickly. Overall safety also depends on the type of radiation emitted and on how the waste is stored.",
        hints=["How does half-life affect the activity at any instant?", "How does it affect how LONG the waste remains dangerous?", "Weigh both sides and reach a judgement."],
        keywords="long half-life: lower activity but hazardous for a very long time (secure storage); short: very active but decays fast; depends on radiation type",
        sample_pass=["Partly true, a long half-life gives a lower activity, but the waste stays radioactive for thousands of years and must be stored for that long; short half-life waste is very active but decays quickly",
                     "it emits less per second, but it remains dangerous for a long time so it is not necessarily safer"],
        sample_fail=["Correct, long half-life waste is never dangerous", "Half-life has nothing to do with how dangerous waste is"])
