"""Chapter 13 Static Electricity (6091): charge bookkeeping and data-reading templates (teacher's choice for descriptive chapters):
attraction/repulsion tables, charge transferred by rubbing, field direction, induction, unit conversion, counting electrons,
precipitator data, total charge, sharing charge between spheres."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template, text_options

E = 1.6e-19


# ---------------------------------------------------------------- L1
@template("c13_which_pair_repels", chapter=13, level=1, lo="13b")
def which_pair_repels(rng):
    pos = set(rng.sample("PQRS", 2))
    q = [(n, "+" if n in pos else "−") for n in "PQRS"]
    names = {n: s for n, s in q}
    pairs = [("P", "Q"), ("P", "R"), ("Q", "S"), ("R", "S"), ("P", "S"), ("Q", "R")]
    rng.shuffle(pairs)
    repel = [f"{a} and {b}" for a, b in pairs if names[a] == names[b]]
    attract = [f"{a} and {b}" for a, b in pairs if names[a] != names[b]]
    ans = repel[0]
    wrongs = {p: f"{p.split(' and ')[0]} is {names[p.split(' and ')[0]]} and {p.split(' and ')[1]} is {names[p.split(' and ')[1]]}: unlike charges attract." for p in attract[:3]}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["sphere", "charge"], [[n, s] for n, s in sorted(q)])
    return dict(
        stem=f"Four small charged spheres hang on insulating threads. The table shows their charges.\n\n{table}\n\nWhich pair of spheres **repel** each other?",
        options=opts, key=key, misconceptions=mis,
        formula="like charges repel; unlike charges attract",
        working=[f"{ans.split(' and ')[0]} and {ans.split(' and ')[1]} are both {names[ans.split(' and ')[0]]}", "like charges repel", f"the pair that repel: **{ans}**"],
        hints=[
            "State the rule for forces between charges.",
            "Repulsion needs two charges of the SAME sign. Check each pair in the table.",
            "Find the pair where both signs match.",
        ],
    )


@template("c13_charge_on_cloth", chapter=13, level=1, lo="13f")
def charge_on_cloth(rng):
    qn = nice(rng, 4, 6, 8, 10, 12, 15)
    rod, sign = rng.choice([("polythene", "−"), ("acetate", "+")])
    rod_charge = f"{sign}{qn} nC"
    cloth_charge = f"{'+' if sign == '−' else '−'}{qn} nC"
    wrongs = {rod_charge: "The cloth gets the OPPOSITE charge: the electrons that one object loses, the other gains.",
              "0 nC": "Rubbing separates charge; it does not create or destroy it. The cloth must carry the equal and opposite charge.",
              f"{'+' if sign == '−' else '−'}{2 * qn} nC": "Charge is conserved: the cloth's charge is equal in size to the rod's, not double."}
    opts, key, mis = text_options(rng, cloth_charge, wrongs)
    table = md_table(["object", "charge after rubbing"], [[rod + " rod", rod_charge], ["cloth", "?"]])
    return dict(
        stem=f"A {rod} rod is rubbed with a dry cloth. Both were uncharged at the start.\n\n{table}\n\nWhat is the charge on the cloth?",
        options=opts, key=key, misconceptions=mis,
        formula="rubbing transfers electrons from one object to the other: the charges gained are equal in size and opposite in sign (charge is conserved)",
        working=[f"the rod becomes {rod_charge} because electrons were {'transferred to it' if sign == '−' else 'removed from it'}", "the same number of electrons left/joined the cloth", f"cloth charge = **{cloth_charge}**"],
        hints=[
            "Only electrons move when two insulators are rubbed. Where do the rod's extra (or missing) electrons come from or go to?",
            "The cloth loses exactly what the rod gains (or gains what the rod loses).",
            "Equal size, opposite sign.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c13_force_direction_in_field", chapter=13, level=2, lo="13d")
def force_direction_in_field(rng):
    src = rng.choice(["+", "−"])
    test = rng.choice(["positive", "negative"])
    away = (src == "+") == (test == "positive")
    ans = "directly away from the charge at the centre" if away else "directly towards the charge at the centre"
    wrongs = {("directly towards the charge at the centre" if away else "directly away from the charge at the centre"):
              f"Field lines show the force on a POSITIVE test charge. A {test} charge near a {'positive' if src == '+' else 'negative'} charge is {'repelled' if away else 'attracted'}.",
              "along a circle around the central charge": "Field lines of a point charge are radial (straight lines through the centre), so the force is along the radius, not round a circle.",
              "zero, because the test charge is small": "A small charge feels a small force, but not zero: any charge in a field experiences a force."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows the electric field of an isolated {'positive' if src == '+' else 'negative'} point charge. A small **{test}** test charge is placed in the field. In which direction is the force on the test charge?",
        figure=figs3.point_charge_field(src),
        options=opts, key=key, misconceptions=mis,
        formula="the direction of a field line is the direction of the force on a positive test charge; a negative charge feels the opposite force",
        working=[f"field lines point {'away from' if src == '+' else 'towards'} the {'positive' if src == '+' else 'negative'} charge", f"a {test} test charge feels a force {'along' if test == 'positive' else 'opposite to'} the field lines", f"force is **{ans}**"],
        hints=[
            "What do the arrows on field lines tell you? (For which sign of test charge?)",
            "Like charges repel, unlike attract. Compare the sign of the test charge with the central charge.",
            f"{'Same' if away else 'Opposite'} signs, so the force is {'away from' if away else 'towards'} the centre.",
        ],
    )


@template("c13_induction_sign", chapter=13, level=2, lo="13g")
def induction_sign(rng):
    rod = rng.choice(["-", "+"])
    near, far = ("positive", "negative") if rod == "-" else ("negative", "positive")
    ask = rng.choice(["A", "B"])
    ans = near if ask == "A" else far
    wrongs = {far if ask == "A" else near: f"Sphere {ask} is the {'near' if ask == 'A' else 'far'} one. Electrons are {'repelled away from' if rod == '-' else 'attracted towards'} the rod, so the {'near' if rod == '-' else 'far'} sphere ends up positive." if False else f"Sphere {ask} is the one {'nearest' if ask == 'A' else 'furthest from'} the rod. Think about which way the free electrons in the metal move.",
              "neutral": "The rod never touches the spheres, but it still moves the free electrons between them, so each sphere ends up charged.",
              ("the same sign as the rod" if ask == "A" else "equal to the rod's charge"): "Induction gives the NEAR sphere the opposite sign to the rod; the charges on the two spheres are equal and opposite to each other." if ask == "A" else "The spheres share the electrons moved by the rod; the far sphere's charge is not related to the size of the rod's charge."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows a {'negatively' if rod == '-' else 'positively'} charged rod held near two touching metal spheres A and B on insulating stands. The spheres are then separated while the rod is still in place, and the rod is removed. What is the final charge on sphere **{ask}**?",
        figure=figs3.induction_spheres(2, rod_sign=rod),
        options=opts, key=key, misconceptions=mis,
        formula="charging by induction: free electrons in the metal move away from a negative rod (towards a positive rod); separating the spheres traps the charges",
        working=[f"the {'negative' if rod == '-' else 'positive'} rod {'repels' if rod == '-' else 'attracts'} the free electrons in the spheres {'to the far sphere B' if rod == '-' else 'to the near sphere A'}",
                 f"near sphere A becomes {near}; far sphere B becomes {far}", f"separating the spheres with the rod present keeps these charges: sphere {ask} is **{ans}**"],
        hints=[
            "Only the free electrons in the metal can move. Does the rod push them away or pull them closer?",
            f"A {'negative' if rod == '-' else 'positive'} rod {'repels' if rod == '-' else 'attracts'} electrons, so they gather on the {'far' if rod == '-' else 'near'} sphere.",
            f"Sphere {ask} is the {'near' if ask == 'A' else 'far'} sphere. Which charge is left there?",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c13_microcoulomb_to_coulomb", chapter=13, level=3, lo="13a")
def microcoulomb_to_coulomb(rng):
    val = nice(rng, 2.5, 4.0, 6.4, 8.0, 12, 25, 40)
    prefix, mult = rng.choice([("µC", 1e-6), ("nC", 1e-9), ("mC", 1e-3)])
    ans = val * mult
    opts, key, mis = numeric_options(rng, ans, [
        (val * mult * 1000, f"Check the prefix: {prefix} means × {mult:g}, one power of a thousand smaller than you used."),
        (val * mult / 1000, f"Check the prefix: {prefix} means × {mult:g}, one power of a thousand larger than you used."),
        (val / mult, "You divided by the multiplier. To change a prefixed unit into the base unit, multiply."),
    ], unit="C", sf=2)
    table = md_table(["object", "charge"], [["charged balloon", f"{fmt(val)} {prefix}"]])
    return dict(
        stem=f"Charge is measured in coulombs (C).\n\n{table}\n\nWhat is this charge in coulombs?",
        options=opts, key=key, misconceptions=mis,
        formula=f"1 {prefix} = {mult:g} C",
        working=[f"{prefix} means × {mult:g}", f"{fmt(val)} {prefix} = {fmt(val)} × {mult:g} C", f"= **{fmt(ans, sf=2)} C**"],
        hints=[
            "Which power of ten does the prefix stand for? (milli 10⁻³, micro 10⁻⁶, nano 10⁻⁹)",
            f"Replace {prefix[:-1]} with its multiplier and keep the unit C.",
            f"{fmt(val)} × {mult:g}.",
        ],
    )


@template("c13_electrons_from_charge", chapter=13, level=3, lo="13f")
def electrons_from_charge(rng):
    n = nice(rng, 2.0e10, 5.0e10, 1.0e11, 2.5e11, 4.0e11)
    q = n * E
    opts, key, mis = numeric_options(rng, n, [
        (q / E * 1000, "Check the powers of ten when dividing by 1.6 × 10⁻¹⁹."),
        (q * E, "You multiplied the charge by the electron charge. Number of electrons = total charge ÷ charge of one electron."),
        (n / 10, "Check the powers of ten when dividing by 1.6 × 10⁻¹⁹."),
    ], unit="", sf=2)
    table = md_table(["quantity", "value"], [["charge gained by the rod", f"−{fmt(q * 1e9, sf=2)} nC"], ["charge of one electron", "−1.6 × 10⁻¹⁹ C"]])
    return dict(
        stem=f"A polythene rod is rubbed with a cloth and becomes negatively charged.\n\n{table}\n\nHow many electrons were transferred to the rod?",
        options=opts, key=key, misconceptions=mis,
        formula="number of electrons = total charge ÷ charge of one electron (charge in coulombs)",
        working=[f"charge = {fmt(q * 1e9, sf=2)} nC = {fmt(q * 1e9, sf=2)} × 10⁻⁹ C", f"number = ({fmt(q * 1e9, sf=2)} × 10⁻⁹) ÷ (1.6 × 10⁻¹⁹)", f"= **{fmt(n, sf=2)}** electrons"],
        hints=[
            "Each electron carries the same tiny charge. How many of them add up to the rod's charge?",
            "Convert nC to C first (× 10⁻⁹), then divide by 1.6 × 10⁻¹⁹ C.",
            f"({fmt(q * 1e9, sf=2)} × 10⁻⁹) ÷ (1.6 × 10⁻¹⁹).",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c13_precipitator_data", chapter=13, level=4, lo="13i")
def precipitator_data(rng):
    before = nice(rng, 200, 250, 400, 500, 800)
    frac = nice(rng, 0.90, 0.92, 0.95, 0.96, 0.98)
    after = round(before * (1 - frac))
    pct = (before - after) / before * 100
    opts, key, mis = numeric_options(rng, pct, [
        (after / before * 100, "That is the percentage that still ESCAPES. The question asks what percentage is removed."),
        (before - after, "That is the mass removed in grams per hour, not a percentage."),
        ((before - after) / after * 100, "Divide by the ORIGINAL amount, not by the amount that escapes."),
    ], unit="%", sf=3)
    table = md_table(["", "dust leaving the chimney / g per hour"], [["precipitator switched off", before], ["precipitator switched on", after]])
    return dict(
        stem=f"Fig. 1 shows an electrostatic precipitator in a factory chimney. The table shows measurements of the dust leaving the chimney.\n\n{table}\n\nWhat percentage of the dust does the precipitator remove?",
        figure=figs3.precipitator(),
        options=opts, key=key, misconceptions=mis,
        formula="percentage removed = (mass without − mass with) ÷ mass without × 100%",
        working=[f"dust removed = {before} − {after} = {before - after} g per hour", f"percentage = {before - after} ÷ {before} × 100", f"= **{fmt(pct, sf=3)}%**"],
        hints=[
            "The dust particles are charged by the wire and attracted to the oppositely charged plates. How much dust no longer leaves the chimney?",
            f"Removed = {before} − {after} g per hour. Compare it with the amount that would have left with the precipitator off.",
            f"({before} − {after}) ÷ {before} × 100.",
        ],
    )


@template("c13_total_charge_drops", chapter=13, level=4, lo="13i")
def total_charge_drops(rng):
    q_pc = nice(rng, 2.0, 4.0, 5.0, 8.0)             # pC per drop
    n = nice(rng, 2.0e6, 5.0e6, 1.0e7, 2.5e7)
    total = q_pc * 1e-12 * n
    opts, key, mis = numeric_options(rng, total, [
        (q_pc * n, "You left the charge per drop in pC. 1 pC = 10⁻¹² C."),
        (q_pc * 1e-12 / n, "You divided by the number of drops. Total charge = charge per drop × number of drops."),
        (total * 1000, "Check the powers of ten: pico means 10⁻¹²."),
    ], unit="C", sf=2)
    table = md_table(["quantity", "value"], [["charge on each paint droplet", f"{fmt(q_pc)} pC (1 pC = 10⁻¹² C)"], ["number of droplets sprayed per second", f"{fmt(n, sf=2)}"]])
    return dict(
        stem=f"In electrostatic spray painting the paint droplets are given a charge so that they are attracted to the earthed car body.\n\n{table}\n\nWhat total charge is sprayed each second?",
        options=opts, key=key, misconceptions=mis,
        formula="total charge = charge per droplet × number of droplets",
        working=[f"charge per droplet = {fmt(q_pc)} pC = {fmt(q_pc)} × 10⁻¹² C", f"total = {fmt(q_pc)} × 10⁻¹² × {fmt(n, sf=2)}", f"= **{fmt(total, sf=2)} C**"],
        hints=[
            "Every droplet carries the same charge, so multiply by how many there are.",
            "Convert pC to C first: pico = 10⁻¹².",
            f"{fmt(q_pc)} × 10⁻¹² × {fmt(n, sf=2)}.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c13_sharing_charge", chapter=13, level=5, lo="13b")
def sharing_charge(rng):
    q1, q2 = rng.choice([(6, -2), (8, 2), (10, -4), (7, 1), (12, -6), (9, -3)])
    each = (q1 + q2) / 2
    opts, key, mis = numeric_options(rng, each, [
        (q1 + q2, "That is the TOTAL charge. When identical spheres touch, the total is shared equally between them."),
        ((q1 - q2) / 2, "You subtracted the charges. Add them (with their signs) and then halve." if q2 < 0 else "Add the charges (both positive) and halve."),
        (q1, "The charges do not stay as they were: charge flows between the spheres until they share it equally."),
    ], unit="nC")
    table = md_table(["sphere", "charge before touching"], [["X", f"+{q1} nC"], ["Y", f"{'+' if q2 > 0 else '−'}{abs(q2)} nC"]])
    return dict(
        stem=f"Two identical metal spheres X and Y on insulating stands carry the charges shown.\n\n{table}\n\nThe spheres are touched together and then separated. What is the charge on each sphere afterwards?",
        options=opts, key=key, misconceptions=mis,
        formula="charge is conserved and identical conductors share it equally: each = (Q₁ + Q₂) ÷ 2",
        working=[f"total charge = (+{q1}) + ({'+' if q2 > 0 else '−'}{abs(q2)}) = +{q1 + q2} nC", f"shared equally: {q1 + q2} ÷ 2", f"= **+{fmt(each)} nC** on each sphere"],
        hints=[
            "When the spheres touch, electrons flow until both are at the same state. The total charge cannot change.",
            f"Add the charges, keeping the signs: {q1} + ({q2}).",
            "Identical spheres end up with equal charges: halve the total.",
        ],
    )
