"""Chapter 13 Static Electricity (6091) bank extension: calculation and data-reading templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2016-2025: polythene rod and cloth, spheres charged by induction, lightning,
petrol tankers, electrostatic precipitators, paint spraying, photocopiers; school papers 2024-2025)."""
from .. import figs3
from .base import fmt, md_table, mk, mkt, nice, sci, template

E = 1.6e-19


def sign_word(q):
    return "positive" if q > 0 else ("negative" if q < 0 else "neutral")


# ================================================================== L1
@template("c13x_like_unlike_table", chapter=13, level=1, lo="13b")
def like_unlike_table(rng):
    pairs = [("A", "+", "+"), ("B", "−", "+"), ("C", "−", "−"), ("D", "+", "−")]
    rng.shuffle(pairs)
    target = rng.choice(["repel", "attract"])
    goods = [n for n, a, b in pairs if (a == b) == (target == "repel")]
    ans = " and ".join(sorted(goods))
    opts = ["A and C", "B and D", "A and B", "C and D"]
    wrongs = {o: "Like charges repel; unlike charges attract." for o in opts if o != ans}
    table = md_table(["pair", "charge on first sphere", "charge on second sphere"], [[n, a, b] for n, a, b in pairs])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"Pairs of charged spheres are brought close together.\n\n{table}\n\nWhich pairs **{target}**?",
               "like charges repel, unlike charges attract", [f"pairs that {target}: **{ans}**"],
               ["Like or unlike?", "Like charges repel.", "Unlike charges attract."])


@template("c13x_rod_cloth_charge", chapter=13, level=1, lo="13f")
def rod_cloth_charge(rng):
    q = nice(rng, 20, 40, 50, 80)
    sign = rng.choice([-1, 1])
    rod = "polythene" if sign < 0 else "acetate"
    return mk(rng, q, [(2 * q, "The cloth gains exactly the charge the rod loses: equal size."), (q / 2, "The charges are equal and opposite."), (0.0001 + q * 0 if False else q + 10, "The charge on the cloth equals the charge on the rod in size.")],
              "nC", f"An {rod} rod is rubbed with a cloth.\n\n{md_table(['object', 'charge after rubbing'], [[f'{rod} rod', f'{q} nC ({sign_word(sign)})'], ['cloth', '?']])}\n\nWhat is the size of the charge on the cloth? (Charge is not created, only transferred.)" if False else f"A{'n' if rod[0] in 'aeiou' else ''} {rod} rod is rubbed with a cloth.\n\n{md_table(['object', 'charge after rubbing'], [[f'{rod} rod', f'{q} nC ({sign_word(sign)})'], ['cloth', '?']])}\n\nWhat is the size of the charge on the cloth? (Charge is not created, only transferred.)",
              "rod and cloth gain equal and opposite charges", [f"cloth: **{q} nC**, {sign_word(-sign)}"],
              ["Charge is conserved.", "Electrons move from one to the other.", "Equal size, opposite sign."], dp=0)


@template("c13x_charge_unit_convert", chapter=13, level=1, lo="13a")
def charge_unit_convert(rng):
    q_uc = nice(rng, 2, 5, 8, 15, 40)
    return mk(rng, q_uc * 1e-6, [(q_uc * 1e-3, "1 µC = 10⁻⁶ C, not 10⁻³ C."), (q_uc * 1e6, "Micro means × 10⁻⁶ (smaller)."), (q_uc * 1e-9, "That is for nC.")],
              "C", f"{md_table(['quantity', 'value'], [['charge on a balloon', f'{q_uc} µC']])}\n\nWhat is this charge in coulombs?",
              "1 µC = 1 × 10⁻⁶ C", [f"{q_uc} µC = **{sci(q_uc * 1e-6)} C**"],
              ["What does micro mean?", "× 10⁻⁶.", "Convert."])


@template("c13x_electron_charge_sign", chapter=13, level=1, lo="13a")
def electron_charge_sign(rng):
    gain = rng.choice([True, False])
    n = nice(rng, 1000, 5000, 20000)
    ans = "negative" if gain else "positive"
    wrongs = {("positive" if gain else "negative"): "Electrons are negative: gaining them makes an object negative; losing them makes it positive.",
              "neutral": "The object now has unequal numbers of protons and electrons.", "it depends on its size": "The sign depends only on gaining or losing electrons."}
    action = "gains" if gain else "loses"
    table = md_table(["object", "change"], [["balloon", f"{action} {n} electrons"]])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhat is the sign of the charge on the balloon afterwards?",
               "electrons carry negative charge", [f"{action} electrons → **{ans}**"],
               ["What is the charge of an electron?", "Negative.", "Gain → negative; lose → positive."])


@template("c13x_field_direction_point", chapter=13, level=1, lo="13d")
def field_direction_point(rng):
    sign = rng.choice(["+", "-"])
    ans = "outwards, away from the charge" if sign == "+" else "inwards, towards the charge"
    wrongs = {("inwards, towards the charge" if sign == "+" else "outwards, away from the charge"): "Field lines point in the direction of the force on a POSITIVE test charge.",
              "in circles around the charge": "Electric field lines of a point charge are radial.", "there is no field": "Every charge has a field around it."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows an isolated {'positive' if sign == '+' else 'negative'} point charge. In which direction do its electric field lines point?",
               "field direction = direction of force on a small positive charge", [f"a positive test charge is {'repelled' if sign == '+' else 'attracted'} → **{ans}**"],
               ["Imagine a small positive test charge.", "Is it pushed away or pulled in?", "That is the field direction."], figure=figs3.point_charge_field(sign))


@template("c13x_force_on_electron_field", chapter=13, level=1, lo="13d")
def force_on_electron_field(rng):
    fdir = rng.choice(["to the right", "upwards", "to the left", "downwards"])
    opp = {"to the right": "to the left", "to the left": "to the right", "upwards": "downwards", "downwards": "upwards"}[fdir]
    q = rng.choice(["an electron", "a proton"])
    ans = opp if q == "an electron" else fdir
    others = [d for d in ["to the right", "to the left", "upwards", "downwards"] if d != ans]
    wrongs = {d: ("A negative charge feels a force OPPOSITE to the field." if q == "an electron" and d == fdir else "Field lines show the force on a positive charge.") for d in others}
    table = md_table(["quantity", "direction"], [["electric field", fdir]])
    return mkt(rng, ans, wrongs, f"{table}\n\nIn which direction is the force on **{q}** placed in this field?",
               "positive: force along the field; negative: force opposite", [f"{q} → **{ans}**"],
               ["Field direction = force on a positive charge.", "Is the particle positive or negative?", "Reverse for negative."])


@template("c13x_precipitator_mass", chapter=13, level=1, lo="13i")
def precipitator_mass(rng):
    rate = nice(rng, 2, 3, 4, 5)
    t = nice(rng, 8, 10, 12, 24)
    return mk(rng, rate * t, [(rate / t, "Multiply the rate by the time."), (rate + t, "Multiply."), (rate * t * 60, "The rate is per HOUR.")],
              "kg", f"An electrostatic precipitator in a chimney removes ash (Fig. 1).\n\n{md_table(['quantity', 'value'], [['ash collected per hour', f'{rate} kg'], ['hours of operation', t]])}\n\nWhat mass of ash is collected?",
              "mass = rate × time", [f"= {rate} × {t} = **{rate * t} kg**"],
              ["Rate × time.", "Both are per hour.", "Multiply."], figure=figs3.precipitator(), dp=0)


@template("c13x_paint_saving", chapter=13, level=1, lo="13i")
def paint_saving(rng):
    used = nice(rng, 10, 12, 20)
    frac = nice(rng, 0.3, 0.4, 0.5)
    return mk(rng, used * frac, [(used * (1 - frac), "That is the paint still USED; find the amount saved."), (used, "Multiply by the fraction saved."), (frac, "Multiply by the amount used before.")],
              "litres", f"Charging the paint droplets and the car body oppositely makes the paint attracted to the car, so less is wasted.\n\n{md_table(['quantity', 'value'], [['paint used per car without charging', f'{used} litres'], ['fraction of paint saved by charging', f'{frac:g}']])}\n\nHow much paint is saved per car?",
              "saving = fraction × amount used", [f"= {frac:g} × {used} = **{fmt(used * frac)} litres**"],
              ["What fraction is saved?", "Multiply.", "Answer in litres."])


# ================================================================== L2
@template("c13x_n_electrons_simple", chapter=13, level=2, lo="13a")
def n_electrons_simple(rng):
    q = nice(rng, 1.6e-9, 3.2e-9, 8.0e-9, 1.6e-8)
    n = q / E
    return mk(rng, n, [(q * E, "Number of electrons = Q ÷ e."), (E / q, "Charge goes on top."), (n / 1000, "Check the powers of ten.")],
              "electrons", f"{md_table(['quantity', 'value'], [['charge on a rod', f'{sci(q)} C'], ['charge on one electron', '1.6 × 10⁻¹⁹ C']])}\n\nHow many electrons have been transferred?",
              "n = Q ÷ e", [f"n = {sci(q)} ÷ 1.6 × 10⁻¹⁹ = **{sci(n)}**"],
              ["Each electron carries e.", "n = Q ÷ e.", "Standard form."])


@template("c13x_charge_from_electrons", chapter=13, level=2, lo="13a")
def charge_from_electrons(rng):
    n = nice(rng, 5e10, 1e11, 2.5e11, 5e11)
    q = n * E * 1e9
    return mk(rng, q, [(n * E, "That is in C; the answer is in nC."), (n / E * 1e9, "Q = n × e."), (q * 1000, "Check the conversion to nC.")],
              "nC", f"{md_table(['quantity', 'value'], [['electrons gained by a comb', sci(n)], ['charge on one electron', '1.6 × 10⁻¹⁹ C']])}\n\nWhat is the size of the charge on the comb, in nC?",
              "Q = n e", [f"Q = {sci(n)} × 1.6 × 10⁻¹⁹ = {sci(n * E)} C", f"= **{fmt(q)} nC**"],
              ["Q = n × e.", "Multiply.", "1 nC = 10⁻⁹ C."])


@template("c13x_rubbing_sign_table", chapter=13, level=2, lo="13f")
def rubbing_sign_table(rng):
    series = ["glass", "wool", "silk", "acetate", "polythene"]
    a, b = sorted(rng.sample(range(5), 2))
    upper, lower = series[a], series[b]
    which = rng.choice([upper, lower])
    ans = "positive" if which == upper else "negative"
    wrongs = {("negative" if ans == "positive" else "positive"): f"The material higher in the list ({upper}) loses electrons and becomes positive.",
              "neutral": "Rubbing transfers electrons, so both become charged.", "both the same sign": "One gains electrons; the other loses them."}
    table = md_table(["position", "material (loses electrons most easily at the top)"], [[i + 1, m] for i, m in enumerate(series)])
    return mkt(rng, ans if ans != "both the same sign" else ans, wrongs,
               f"{table}\n\nA {upper} rod is rubbed with {lower}. What is the charge on the **{which}**?",
               "higher material loses electrons (+); lower gains electrons (−)", [f"{upper} loses electrons → +; {lower} gains → −", f"{which}: **{ans}**"],
               ["Which material loses electrons more easily?", "It becomes positive.", "The other becomes negative."])


@template("c13x_rubbing_electrons_mass", chapter=13, level=2, lo="13f")
def rubbing_electrons_mass(rng):
    q_nc = nice(rng, 16, 32, 48, 80)
    n = q_nc * 1e-9 / E
    return mk(rng, n, [(q_nc / E, "Convert nC to C first."), (q_nc * 1e-9 * E, "n = Q ÷ e."), (n * 1000, "Check the powers of ten.")],
              "electrons", f"A polythene rod rubbed with wool gains a charge of **−{q_nc} nC**.\n\n{md_table(['quantity', 'value'], [['charge on rod', f'−{q_nc} nC'], ['charge on an electron', '1.6 × 10⁻¹⁹ C']])}\n\nHow many electrons moved from the wool to the rod?",
              "n = Q ÷ e", [f"Q = {q_nc} × 10⁻⁹ C", f"n = {sci(q_nc * 1e-9)} ÷ 1.6 × 10⁻¹⁹ = **{sci(n)}**"],
              ["Convert to coulombs.", "n = Q ÷ e.", "Standard form."])


@template("c13x_attract_neutral", chapter=13, level=2, lo="13b")
def attract_neutral(rng):
    rod = rng.choice(["positively", "negatively"])
    wrongs = {"it is repelled": "A charged rod attracts small neutral objects by inducing opposite charge on the near side.",
              "nothing happens, because it is neutral": "Induced charges cause attraction.", "it becomes permanently charged": "The charges separate only while the rod is near."}
    table = md_table(["object", "charge"], [["rod", f"{rod} charged"], ["small piece of paper", "neutral"]])
    return mkt(rng, "it is attracted", wrongs, f"{table}\n\nThe rod is brought close to the piece of paper. What happens to the paper?",
               "induced opposite charge on the near side → attraction", ["opposite charge is induced on the near side, which is closer → **attracted**"],
               ["Can a neutral object be attracted?", "Charges separate (induction).", "Near side has opposite charge."])


@template("c13x_two_ball_forces", chapter=13, level=2, lo="13b")
def two_ball_forces(rng):
    qa = rng.choice(["+", "−"])
    qb = rng.choice(["+", "−"])
    ans = "they move apart" if qa == qb else "they move together"
    wrongs = {("they move together" if ans == "they move apart" else "they move apart"): "Like charges repel; unlike charges attract.",
              "they stay still": "Charged objects exert forces on each other.", "only one of them moves": "Forces act equally on both (Newton's third law)."}
    table = md_table(["ball", "charge"], [["X", qa], ["Y", qb]])
    return mkt(rng, ans, wrongs, f"Two light balls hang side by side on insulating threads.\n\n{table}\n\nWhat happens?",
               "like repel, unlike attract", [f"{qa} and {qb} → **{ans}**"],
               ["Like or unlike?", "Like repel.", "Unlike attract."])


@template("c13x_induction_final", chapter=13, level=2, lo="13g")
def induction_final(rng):
    rod = rng.choice(["+", "-"])
    near = "negative" if rod == "+" else "positive"
    far = "positive" if rod == "+" else "negative"
    which = rng.choice(["near", "far"])
    ans = near if which == "near" else far
    wrongs = {(far if ans == near else near): "The near sphere gets the charge OPPOSITE to the rod.",
              "neutral": "The spheres are separated while the rod is present, so they keep their charges.", "the same sign on both spheres": "One gains electrons and the other loses them."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows two touching metal spheres on insulating stands with a {'positively' if rod == '+' else 'negatively'} charged rod near sphere A. The spheres are separated, then the rod is removed. What is the charge on the **{'near (A)' if which == 'near' else 'far (B)'}** sphere?",
               "near side: opposite to rod; far side: same as rod", [f"near: {near}; far: {far} → **{ans}**"],
               ["Electrons move towards or away from the rod.", "The near sphere gets the opposite charge.", "Separate before removing the rod."], figure=figs3.induction_spheres(1, "-" if rod == "-" else "+"))


@template("c13x_field_two_charges", chapter=13, level=2, lo="13d")
def field_two_charges(rng):
    signs = rng.choice([("+", "-"), ("+", "+"), ("-", "-")])
    ans = "from the positive charge to the negative charge" if signs == ("+", "-") else ("outwards from both, with a neutral point between them" if signs == ("+", "+") else "into both, with a neutral point between them")
    allo = ["from the positive charge to the negative charge", "outwards from both, with a neutral point between them", "into both, with a neutral point between them", "in circles around the midpoint"]
    wrongs = {o: "Use the rule: field lines start on + and end on −." for o in allo if o != ans}
    names = {"+": "positive", "-": "negative"}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the field between a {names[signs[0]]} and a {names[signs[1]]} charge. Which describes the field lines?",
               "lines start on + charges and end on − charges", [f"**{ans}**"],
               ["Where do lines start?", "Where do they end?", "Like charges: neutral point between."], figure=figs3.two_charges_field(signs))


# ================================================================== L3
@template("c13x_charge_conservation_spheres", chapter=13, level=3, lo="13a")
def charge_conservation_spheres(rng):
    qa = nice(rng, 6, 8, 10, 12)
    qb = -nice(rng, 2, 4)
    each = (qa + qb) / 2
    return mk(rng, each, [((qa - qb) / 2, "Add the charges with their SIGNS."), (qa + qb, "That is the total; identical spheres share it equally."), (qa / 2, "Include the negative charge on B.")],
              "nC", f"Two identical metal spheres touch and are then separated.\n\n{md_table(['sphere', 'charge before / nC'], [['A', f'+{qa}'], ['B', f'{qb}']])}\n\nWhat is the charge on each sphere afterwards?",
              "total charge is conserved and shared equally", [f"total = {qa} + ({qb}) = {qa + qb} nC", f"each = **+{fmt(each)} nC**"],
              ["Charge is conserved.", "Add with signs.", "Share equally."])


@template("c13x_charge_lightning_current", chapter=13, level=3, lo="13a")
def charge_lightning_current(rng):
    I = nice(rng, 20000, 30000, 40000)
    t = nice(rng, 0.0005, 0.001, 0.002)
    return mk(rng, I * t, [(I / t, "Q = I × t."), (I * t * 1000, "t is already in seconds."), (I, "Multiply by the time.")],
              "C", f"A lightning strike is a huge flow of charge between a cloud and the ground.\n\n{md_table(['quantity', 'value'], [['average current', f'{I} A'], ['duration', f'{fmt(t)} s']])}\n\nHow much charge flows? (Q = I t)",
              "Q = I t", [f"Q = {I} × {fmt(t)} = **{fmt(I * t)} C**"],
              ["Current is the rate of flow of charge.", "Q = I t.", "Multiply."])


@template("c13x_repel_force_distance", chapter=13, level=3, lo="13b")
def repel_force_distance(rng):
    F1 = nice(rng, 8, 12, 16, 20)
    k = nice(rng, 2, 3)
    return mk(rng, F1 / k ** 2, [(F1 / k, "The force falls with distance SQUARED."), (F1 * k * k, "Further apart → SMALLER force."), (F1, "The force depends on the distance.")],
              "mN", f"The force between two small charged spheres is inversely proportional to the square of their separation.\n\n{md_table(['separation', 'force / mN'], [['d', F1], [f'{k}d', '?']])}\n\nWhat is the force at the larger separation?",
              "F ∝ 1/d²", [f"F = {F1} ÷ {k}² = **{fmt(F1 / k ** 2)} mN**"],
              ["How does force depend on distance?", "F ∝ 1/d².", f"Divide by {k}²."])


@template("c13x_deflection_compare", chapter=13, level=3, lo="13b")
def deflection_compare(rng):
    rows = [("P", "+", 5), ("Q", "−", 12), ("R", "+", 20), ("S", "0", 0)]
    rng.shuffle(rows)
    rod = "+"
    target = max(r for r in rows if r[1] == "−")[0] if False else "Q"
    ans = "Q"
    wrongs = {n: ("Like charges repel; the rod is positive." if s == "+" else "A neutral ball is only weakly attracted.") for n, s, d in rows if n != ans}
    table = md_table(["ball", "charge", "size of charge / nC"], [[n, s, d] for n, s, d in rows])
    return mkt(rng, ans, wrongs, f"A positively charged rod is held near each ball in turn.\n\n{table}\n\nWhich ball is attracted most strongly?",
               "unlike charges attract; larger charges → larger force", ["only Q is negative (unlike the rod) → **Q** is attracted most strongly"],
               ["Which balls are repelled?", "Those with + charge.", "Unlike → attract; large charge → strong."])


@template("c13x_tanker_charge_rate", chapter=13, level=3, lo="13h")
def tanker_charge_rate(rng):
    rate = nice(rng, 0.2, 0.5, 1.0)
    t = nice(rng, 60, 120, 300)
    return mk(rng, rate * t, [(rate / t, "Charge = rate × time."), (rate * t / 60, "The time is already in seconds."), (rate, "Multiply by the time.")],
              "µC", f"Petrol flowing through a pipe rubs against it, so charge builds up on an unearthed tanker.\n\n{md_table(['quantity', 'value'], [['rate of build-up of charge', f'{rate} µC per second'], ['time of flow', f'{t} s']])}\n\nHow much charge builds up if the tanker is not earthed?",
              "Q = rate × time", [f"Q = {rate} × {t} = **{fmt(rate * t)} µC**"],
              ["The charge builds up steadily.", "Multiply by the time.", "This could cause a dangerous spark."])


@template("c13x_lightning_energy", chapter=13, level=3, lo="13h")
def lightning_energy(rng):
    Q = nice(rng, 10, 20, 30)
    V = nice(rng, 1e8, 2e8, 5e8)
    E_ = Q * V
    return mk(rng, E_, [(V / Q, "Energy = Q × V."), (Q * V / 1000, "Keep joules."), (V, "Multiply by the charge.")],
              "J", f"{md_table(['quantity', 'value'], [['charge transferred in a lightning strike', f'{Q} C'], ['potential difference between cloud and ground', f'{sci(V)} V']])}\n\nHow much energy is transferred? (E = Q V)",
              "E = Q V", [f"E = {Q} × {sci(V)} = **{sci(E_)} J**"],
              ["Energy = charge × p.d.", "Multiply.", "Standard form."])


@template("c13x_precipitator_efficiency", chapter=13, level=3, lo="13i")
def precipitator_efficiency(rng):
    m_in = nice(rng, 50, 80, 100)
    m_out = m_in * nice(rng, 0.02, 0.05, 0.1)
    eff = (m_in - m_out) / m_in * 100
    return mk(rng, eff, [(m_out / m_in * 100, "That is the percentage that ESCAPES."), (m_in - m_out, "Express as a percentage."), ((m_in - m_out) / m_out * 100, "Divide by the mass entering.")],
              "%", f"An electrostatic precipitator is tested (Fig. 1).\n\n{md_table(['ash per hour', 'mass / kg'], [['entering the precipitator', m_in], ['leaving the chimney', fmt(m_out)]])}\n\nWhat percentage of the ash is removed?",
              "% removed = (in − out) ÷ in × 100%", [f"removed = {m_in} − {fmt(m_out)} = {fmt(m_in - m_out)} kg", f"% = **{fmt(eff)}%**"],
              ["Find the mass removed.", "Divide by the mass entering.", "× 100%."], figure=figs3.precipitator())


@template("c13x_photocopier_toner", chapter=13, level=3, lo="13i")
def photocopier_toner(rng):
    per = nice(rng, 0.02, 0.025, 0.05)
    pages = nice(rng, 2000, 4000, 5000)
    return mk(rng, per * pages, [(per, "Multiply by the number of pages."), (pages / per, "Mass = mass per page × pages."), (per * pages / 1000, "Keep grams.")],
              "g", f"In a photocopier, charged toner powder is attracted to the oppositely charged parts of a drum.\n\n{md_table(['quantity', 'value'], [['toner used per page', f'{fmt(per)} g'], ['number of pages', pages]])}\n\nWhat mass of toner is used?",
              "mass = per page × pages", [f"= {fmt(per)} × {pages} = **{fmt(per * pages)} g**"],
              ["Find the toner per page.", "Multiply by the pages.", "Answer in g."])


@template("c13x_strokes_charge", chapter=13, level=3, lo="13f")
def strokes_charge(rng):
    n = nice(rng, 1e9, 2e9, 5e9)
    k = nice(rng, 10, 20, 25)
    q = n * k * E * 1e9
    return mk(rng, q, [(n * E * 1e9, "Multiply by the number of strokes."), (n * k * E, "Convert C to nC."), (q * 10, "Check the powers of ten.")],
              "nC", f"Each stroke of a cloth moves electrons onto a polythene rod.\n\n{md_table(['quantity', 'value'], [['electrons moved per stroke', sci(n)], ['number of strokes', k], ['e', '1.6 × 10⁻¹⁹ C']])}\n\nWhat is the size of the charge on the rod afterwards, in nC (assuming none leaks away)?",
              "Q = (n × strokes) × e", [f"total electrons = {sci(n)} × {k} = {sci(n * k)}", f"Q = {sci(n * k)} × 1.6 × 10⁻¹⁹ = **{fmt(q)} nC** (negative)"],
              ["Find the total number of electrons.", "Multiply by e.", "Convert to nC."])


# ================================================================== L4
@template("c13x_e_from_drops", chapter=13, level=4, lo="13a")
def e_from_drops(rng):
    k = [nice(rng, 2, 3), nice(rng, 4, 5), nice(rng, 6, 7)]
    charges = [x * E for x in k]
    rng.shuffle(charges)
    return mk(rng, E, [(min(charges), "That is one drop's charge; find the largest common unit."), (sum(charges) / 3, "Find the common factor, not the average."), (2 * E, "The smallest unit divides all of them exactly.")],
              "C", f"In an experiment, the charges on oil drops are measured.\n\n{md_table(['drop', 'charge / C'], [[i + 1, sci(q)] for i, q in enumerate(charges)])}\n\nWhat is the smallest charge that each value is a whole-number multiple of?",
              "charges come in whole multiples of e", [", ".join(f"{sci(q)} = {round(q / E)} e" for q in charges), f"common unit = **{sci(E)} C**"],
              ["Charge comes in packets.", "Find a value that divides all of them.", "That is the electron's charge."])


@template("c13x_charge_mass_electrons", chapter=13, level=4, lo="13a")
def charge_mass_electrons(rng):
    q = nice(rng, 1e-6, 2e-6, 5e-6)
    m_e = 9.1e-31
    n = q / E
    m = n * m_e
    return mk(rng, m, [(n, "That is the NUMBER of electrons; multiply by the mass of each."), (q * m_e, "Find the number first: n = Q ÷ e."), (m * 1e6, "Check the powers of ten.")],
              "kg", f"A plastic sphere gains a charge of **−{sci(q)} C**.\n\n{md_table(['quantity', 'value'], [['charge on an electron', '1.6 × 10⁻¹⁹ C'], ['mass of an electron', '9.1 × 10⁻³¹ kg']])}\n\nBy how much does its mass increase?",
              "n = Q ÷ e; mass = n × m_e", [f"n = {sci(q)} ÷ 1.6 × 10⁻¹⁹ = {sci(n)}", f"mass = {sci(n)} × 9.1 × 10⁻³¹ = **{sci(m)} kg**"],
              ["How many electrons were gained?", "Each has a tiny mass.", "Multiply."])


@template("c13x_rubbing_both_objects", chapter=13, level=4, lo="13f")
def rubbing_both_objects(rng):
    n = nice(rng, 2e11, 5e11, 1e12)
    q = n * E * 1e9
    return mk(rng, q, [(2 * q, "The cloth has the same SIZE of charge as the rod."), (n * E, "That is in C; give nC."), (q / 2, "Each electron moved carries e.")],
              "nC", f"During rubbing, **{sci(n)}** electrons move from a woollen cloth to a polythene rod.\n\n{md_table(['quantity', 'value'], [['electrons transferred', sci(n)], ['e', '1.6 × 10⁻¹⁹ C']])}\n\nWhat is the size of the charge on the cloth, in nC?",
              "cloth loses n electrons: Q = n e (positive)", [f"Q = {sci(n)} × 1.6 × 10⁻¹⁹ = {sci(n * E)} C", f"= **+{fmt(q)} nC** on the cloth"],
              ["The rod gains what the cloth loses.", "Q = n e.", "Convert to nC."])


@template("c13x_rubbing_time_charge", chapter=13, level=4, lo="13f")
def rubbing_time_charge(rng):
    per = nice(rng, 2, 3, 5)
    strokes = nice(rng, 10, 20, 30)
    leak = nice(rng, 5, 10)
    net = per * strokes - leak
    return mk(rng, net, [(per * strokes, "Subtract the charge that leaked away."), (per * strokes + leak, "Leakage REDUCES the charge."), (per, "Multiply by the number of strokes first.")],
              "nC", f"A student rubs a rod with a cloth several times.\n\n{md_table(['quantity', 'value'], [['charge gained per stroke', f'{per} nC'], ['number of strokes', strokes], ['charge leaked away to the damp air', f'{leak} nC']])}\n\nWhat is the final charge on the rod?",
              "net = per stroke × strokes − leak", [f"= {per} × {strokes} − {leak} = **{net} nC**"],
              ["Find the total gained.", "Subtract the leakage.", "Answer in nC."], dp=0)


@template("c13x_earthing_current", chapter=13, level=4, lo="13h")
def earthing_current(rng):
    q = nice(rng, 2e-6, 5e-6, 1e-5)
    t = nice(rng, 1e-3, 2e-3, 5e-3)
    I = q / t * 1000
    return mk(rng, I, [(q / t, "That is in A; the answer is in mA."), (q * t * 1000, "I = Q ÷ t."), (I / 1000, "Convert A to mA.")],
              "mA", f"A charged car body is earthed by a strap as the driver touches it.\n\n{md_table(['quantity', 'value'], [['charge on car', f'{sci(q)} C'], ['time to discharge', f'{sci(t)} s']])}\n\nWhat is the average current through the strap, in mA?",
              "I = Q ÷ t", [f"I = {sci(q)} ÷ {sci(t)} = {fmt(q / t)} A", f"= **{fmt(I)} mA**"],
              ["Current = charge ÷ time.", "I = Q ÷ t.", "Convert to mA."])


@template("c13x_spark_risk", chapter=13, level=4, lo="13h")
def spark_risk(rng):
    rows = [("tanker earthed, dry day", 0.1), ("tanker unearthed, dry day", 15), ("tanker unearthed, humid day", 4), ("tanker earthed, humid day", 0.05)]
    thresh = 1.0
    rng.shuffle(rows)
    risky = [n for n, q in rows if q > thresh]
    ans = " and ".join(sorted(risky)) if len(risky) > 1 else risky[0]
    allo = ["tanker unearthed, dry day and tanker unearthed, humid day", "tanker earthed, dry day", "tanker earthed, humid day", "none of them"]
    ans = "tanker unearthed, dry day and tanker unearthed, humid day"
    wrongs = {o: "Compare each charge with the spark threshold." for o in allo if o != ans}
    table = md_table(["situation", "charge built up / µC"], [[n, q] for n, q in rows])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"A spark can ignite petrol vapour if more than **{thresh} µC** builds up.\n\n{table}\n\nIn which situations is there a risk of a spark?",
               "risk if charge > threshold; earthing removes charge", ["unearthed tankers exceed 1 µC → **both unearthed situations**"],
               ["Compare with the threshold.", "Which situations exceed it?", "Earthing keeps the charge low."])


@template("c13x_induction_earthing_charge", chapter=13, level=4, lo="13g")
def induction_earthing_charge(rng):
    rod = rng.choice(["+", "-"])
    ans = "negative" if rod == "+" else "positive"
    wrongs = {("positive" if ans == "negative" else "negative"): "Earthing lets electrons flow so the sphere ends with the charge OPPOSITE to the rod.",
              "neutral": "Remove the earth before the rod, so the induced charge stays.", "the same as the rod": "Induction gives the opposite charge."}
    return mkt(rng, ans, wrongs, f"A {'positively' if rod == '+' else 'negatively'} charged rod is held near an insulated metal sphere. The sphere is touched briefly with a finger (earthed), the finger is removed, and then the rod is removed (Fig. 1). What is the final charge on the sphere?",
               "charging by induction with earthing gives the opposite charge to the rod", [f"rod {rod} → electrons {'flow in from' if rod == '+' else 'flow to'} earth → sphere **{ans}**"],
               ["Which way do electrons move when earthed?", "Towards a + rod, away from a − rod.", "Remove the earth first."], figure=figs3.induction_spheres(2, rod))


@template("c13x_induction_electrons_count", chapter=13, level=4, lo="13g")
def induction_electrons_count(rng):
    q_nc = nice(rng, 8, 16, 24)
    n = q_nc * 1e-9 / E
    return mk(rng, n, [(q_nc / E, "Convert nC to C."), (q_nc * 1e-9 * E, "n = Q ÷ e."), (n / 2, "Each electron carries one e.")],
              "electrons", f"A sphere is charged by induction and ends with a charge of **+{q_nc} nC**.\n\n{md_table(['quantity', 'value'], [['final charge', f'+{q_nc} nC'], ['e', '1.6 × 10⁻¹⁹ C']])}\n\nHow many electrons flowed from the sphere to earth?",
              "n = Q ÷ e", [f"n = {q_nc} × 10⁻⁹ ÷ 1.6 × 10⁻¹⁹ = **{sci(n)}**"],
              ["Positive means electrons left.", "n = Q ÷ e.", "Convert nC first."])


# ================================================================== L5
@template("c13x_share_three_spheres", chapter=13, level=5, lo="13b")
def share_three_spheres(rng):
    qa = nice(rng, 12, 18, 24)
    qb = -nice(rng, 6)
    qc = 0
    ab = (qa + qb) / 2
    bc = (ab + qc) / 2
    return mk(rng, bc, [(ab, "That is B after touching A; B then shares with C."), ((qa + qb + qc) / 3, "They do not all touch at once."), (bc * 2, "B shares its charge equally with C.")],
              "nC", f"Three identical metal spheres. A touches B and they are separated; then B touches C and they are separated.\n\n{md_table(['sphere', 'starting charge / nC'], [['A', f'+{qa}'], ['B', f'{qb}'], ['C', '0']])}\n\nWhat is the final charge on C?",
              "each touch shares the total equally between two spheres", [f"A–B: ({qa} + ({qb})) ÷ 2 = {fmt(ab)} nC each", f"B–C: ({fmt(ab)} + 0) ÷ 2 = **{fmt(bc)} nC**"],
              ["Work through each touch in order.", "Identical spheres share equally.", "Add with signs."])


@template("c13x_force_ratio_charges", chapter=13, level=5, lo="13b")
def force_ratio_charges(rng):
    F = nice(rng, 6, 9, 12)
    k1, k2 = nice(rng, 2, 3), nice(rng, 2)
    F2 = F * k1 / k2 ** 2
    return mk(rng, F2, [(F * k1 / k2, "Force ∝ 1/d²: square the distance factor."), (F * k1 * k2 ** 2, "Larger distance → smaller force."), (F * k1, "Include the change in distance.")],
              "mN", f"The force between two charged spheres is proportional to the product of their charges and inversely proportional to the square of their separation.\n\n{md_table(['change', 'factor'], [['charge on one sphere', f'× {k1}'], ['separation', f'× {k2}']])}\n\nThe original force was **{F} mN**. What is the new force?",
              "F ∝ q₁q₂ ÷ d²", [f"F = {F} × {k1} ÷ {k2}² = **{fmt(F2)} mN**"],
              ["Apply the charge factor.", "Apply 1/d².", "Combine."])


@template("c13x_charge_electrons_net", chapter=13, level=5, lo="13a")
def charge_electrons_net(rng):
    gain = nice(rng, 5e10, 8e10, 1e11)
    lose = nice(rng, 2e10, 3e10)
    net = (gain - lose) * E * 1e9
    return mk(rng, -net, [(net, "More electrons were gained than lost: the charge is NEGATIVE."), (-(gain + lose) * E * 1e9, "Subtract the electrons lost."), (-(gain - lose) * E, "Convert C to nC.")],
              "nC", f"During a test a metal-free plastic plate first gains and then loses electrons.\n\n{md_table(['process', 'electrons'], [['gained', sci(gain)], ['lost', sci(lose)]])}\n\nWhat is its final charge, in nC? (e = 1.6 × 10⁻¹⁹ C)",
              "net electrons gained × e (negative)", [f"net gain = {sci(gain - lose)} electrons", f"Q = −{sci(gain - lose)} × 1.6 × 10⁻¹⁹ = **−{fmt(net)} nC**"],
              ["Find the net number of electrons gained.", "Each carries −e.", "Convert to nC."])


@template("c13x_cloud_discharge_number", chapter=13, level=5, lo="13a")
def cloud_discharge_number(rng):
    Q = nice(rng, 5, 10, 20)
    n = Q / E
    return mk(rng, n, [(Q * E, "n = Q ÷ e."), (n / 1e6, "Check the powers of ten."), (E / Q, "Charge on top.")],
              "electrons", f"{md_table(['quantity', 'value'], [['charge carried by a lightning strike', f'{Q} C'], ['e', '1.6 × 10⁻¹⁹ C']])}\n\nAbout how many electrons are transferred?",
              "n = Q ÷ e", [f"n = {Q} ÷ 1.6 × 10⁻¹⁹ = **{sci(n)}**"],
              ["n = Q ÷ e.", "Divide.", "Standard form."])


@template("c13x_precipitator_charge_flow", chapter=13, level=5, lo="13i")
def precipitator_charge_flow(rng):
    I_ma = nice(rng, 2, 5, 10)
    t_h = nice(rng, 1, 2)
    Q = I_ma / 1000 * t_h * 3600
    return mk(rng, Q, [(I_ma * t_h * 3600, "Convert mA to A."), (I_ma / 1000 * t_h, "Convert hours to seconds."), (Q / 3600, "Q = I t with t in s.")],
              "C", f"In a precipitator, charged ash particles reach the earthed plates, forming a small current (Fig. 1).\n\n{md_table(['quantity', 'value'], [['current to the plates', f'{I_ma} mA'], ['time', f'{t_h} h']])}\n\nHow much charge reaches the plates?",
              "Q = I t", [f"Q = {fmt(I_ma / 1000)} × {t_h * 3600} = **{fmt(Q)} C**"],
              ["Q = I t.", "Convert mA → A and h → s.", "Multiply."], figure=figs3.precipitator())


@template("c13x_paint_coverage", chapter=13, level=5, lo="13i")
def paint_coverage(rng):
    f_no = nice(rng, 0.5, 0.6)
    f_yes = nice(rng, 0.9, 0.95)
    paint = nice(rng, 8, 10)
    extra = paint * f_yes - paint * f_no
    return mk(rng, extra, [(paint * f_yes, "That is the paint reaching the car WITH charging; find the extra."), (paint * (f_yes - f_no) * 2, "Multiply the difference in fractions by the paint used."), (paint * f_no, "That is without charging.")],
              "litres", f"Electrostatic spraying makes more paint reach the car.\n\n{md_table(['method', 'fraction of sprayed paint reaching the car'], [['uncharged spray', f_no], ['charged spray, earthed car', f_yes]])}\n\nFor **{paint} litres** sprayed, how much MORE paint reaches the car with charging?",
              "extra = paint × (f_charged − f_uncharged)", [f"= {paint} × ({f_yes} − {f_no}) = **{fmt(extra)} litres**"],
              ["Find the paint reaching the car each way.", "Subtract.", "Answer in litres."])


@template("c13x_aircraft_refuel", chapter=13, level=5, lo="13h")
def aircraft_refuel(rng):
    rate = nice(rng, 0.5, 1.0, 2.0)
    limit = nice(rng, 30, 60, 90)
    t = limit / rate
    return mk(rng, t, [(limit * rate, "t = limit ÷ rate."), (rate / limit, "The limit goes on top."), (t / 60, "The answer is in seconds.")],
              "s", f"Fuel flowing into an aircraft that is not earthed builds up charge at a steady rate.\n\n{md_table(['quantity', 'value'], [['rate of build-up', f'{rate} µC per second'], ['charge at which a spark may jump', f'{limit} µC']])}\n\nAfter how long could a dangerous spark occur? (This is why aircraft are earthed before refuelling.)",
              "t = Q ÷ rate", [f"t = {limit} ÷ {rate} = **{fmt(t)} s**"],
              ["How much charge is dangerous?", "How fast does it build?", "Divide."])


@template("c13x_lightning_power", chapter=13, level=5, lo="13h")
def lightning_power(rng):
    Q = nice(rng, 10, 20)
    V = nice(rng, 1e8, 3e8)
    t = nice(rng, 1e-3, 2e-3)
    P = Q * V / t
    return mk(rng, P, [(Q * V, "That is the energy; divide by the time for power."), (Q * V * t, "P = E ÷ t."), (Q / t, "That is the current.")],
              "W", f"{md_table(['quantity', 'value'], [['charge', f'{Q} C'], ['p.d. between cloud and ground', f'{sci(V)} V'], ['duration of strike', f'{sci(t)} s']])}\n\nWhat is the average power of the lightning strike? (E = QV, P = E ÷ t)",
              "E = Q V; P = E ÷ t", [f"E = {Q} × {sci(V)} = {sci(Q * V)} J", f"P = {sci(Q * V)} ÷ {sci(t)} = **{sci(P)} W**"],
              ["Find the energy first.", "E = Q V.", "Then P = E ÷ t."])


@template("c13x_impossible_charge", chapter=13, level=5, lo="13a")
def impossible_charge(rng):
    good = rng.sample([2, 3, 5, 6, 8, 10], 3)
    bad = rng.choice([2.5, 4.5, 7.5])
    rows = [("P", good[0] * 1.6), ("Q", good[1] * 1.6), ("R", good[2] * 1.6), ("S", bad * 1.6)]
    rng.shuffle(rows)
    ans = next(n for n, v in rows if abs(v / 1.6 - round(v / 1.6)) > 0.01)
    wrongs = {n: f"{fmt(v)} × 10⁻¹⁹ C = {round(v / 1.6)} e, a whole number of electron charges." for n, v in rows if n != ans}
    table = md_table(["oil drop", "measured charge / 10⁻¹⁹ C"], [[n, fmt(v)] for n, v in rows])
    return mkt(rng, ans, wrongs, f"A student records the charges on four oil drops. Charge always comes in whole multiples of e = 1.6 × 10⁻¹⁹ C.\n\n{table}\n\nWhich reading must be a mistake?",
               "Q must equal n e with n a whole number", [", ".join(f"{n}: {fmt(v / 1.6)} e" for n, v in rows), f"not a whole number → **{ans}**"],
               ["Divide each charge by 1.6 × 10⁻¹⁹ C.", "Is the result a whole number?", "The one that is not is impossible."])
