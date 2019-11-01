import PySimpleGUI as sg
class Race:
    # placeholder with basic concept for race selection
    # No error handling in place yet.
    def __init__(self, race_name, subrace = None):
        self.race_name = race_name
        self.subrace = subrace
        (self.ability_improvements,
        self.hp_improvement,
        self.size_category,
        self.type_kw,
        self.subtype_kw,
        self.traits) = self.get_attributes()

    def get_attributes(self):
        by_name = {
            "Android": ({"DEX": 2, "INT": 2, "CHA": -2},
                        4,
                        "Medium",
                        "Humanoid",
                        "android",
                        ("Constructed", "Exceptional Vision",
                            "Flat Affect", "Upgrade Slot")),

            "Human":    ({self.prompt_ability(): 2},
                        4,
                        "Medium",
                        "Humanoid",
                        "human",
                        ("Bonus Feat", "Skilled")),

            "Kasatha":  ({"STR": 2, "WIS": 2, "INT": -2},
                        4,
                        "Medium",
                        "Humanoid",
                        "kasatha",
                        ("Desert Stride", "Four-Armed",
                            "Historian", "Natural Grace")),

            "Lashunta": (self.divine_from_subrace(),
                        4,
                        "Medium",
                        "Humanoid",
                        "lashunta",
                        ("Dimorphic", "Lashunta Magic",
                            "Limited Telepathy", "Student")),

            "Shirren": ({"CON": 2, "WIS": 2, "CHA": -2},
                        6,
                        "Medium",
                        "Humanoid",
                        "shirren",
                        ("Blindsense", "Communalism",
                            "Cultural Fascination", "Limited Telepathy")),

            "Vesk":     ({"STR": 2, "CON": 2, "INT": -2},
                        6,
                        "Medium",
                        "Humanoid",
                        "vesk",
                        ("Armor Savant", "Fearless",
                            "Low-Light Vision", "Natural Weapons")),

            "Ysoki":    ({"DEX": 2, "INT": 2, "STR": -2},
                        2,
                        "Small",
                        "Humanoid",
                        "ysoki",
                        ("Cheek Pouches", "Darkvision",
                            "Moxie", "Scrounger"))
        }

        return by_name[self.race_name]

    def prompt_ability(self):
        # placeholder with basic concept for method
        # No error handling in place yet.
        ability_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        if self.race_name == "Human":
            layout = [
                [sg.Text('Please select your racial bonus.')],
                [sg.Text('+2 to: '), sg.Combo(ability_names)],
                [sg.OK()]
            ]
            event, values = sg.Window("Racial Bonus", layout).Read()
            return values[0]

    def divine_from_subrace(self):
        ability_improvements = {
            "Korasha":{"STR": 2, "CHA": 2, "WIS": -2},
            "Damaya":{"INT": 2, "CHA": 2, "CON": -2}
        }
        # placeholder with basic concept for method
        # No error handling in place yet.
        if self.race_name == "Lashunta":
            return ability_improvements[self.subrace]

    racial_traits = {
        # android traits
        "Constructed":
            "For effects targeting creatures by type, androids count as both "
            "humanoids and constructs (whichever effect is worse). They "
            "receive a +2 racial bonus to saving throws against disease, "
            "mind-affecting effects, poison, and sleep, unless those effects "
            "specifically target constructs. In addition, androids do not "
            "breathe or suffer the normal environmental effects of being in a "
            "vacuum.",

        "Exceptional Vision":
            "Androids have low-light vision and darkvision. "
            "As a result, they can see in dim light as if it were normal "
            "light, and they can see with no light source at all to a range of "
            "60 feet in black and white only. See low-light vision and "
            "darkvision on pages 264 and 263 [of the Core Rulebook].",

        "Flat Affect":
            "Androids find emotions confusing and keep them bottled up.  They "
            "take a -2 penalty to Sense Motive checks, but the DCs of Sense "
            "Motive checks attempted against them increase by 2.",

        "Upgrade Slot":
            "Androids have a single armor upgrade slot in their bodies. "
            "Regardless of whether androids are wearing physical armor, they "
            "can use this slot to install any one armor upgrade that could be "
            "installed into light armor.",

        # human traits
        "Bonus Feat":
            "Humans select one extra feat at 1st level.",

        "Skilled":
            "Humans gain an additional skill rank at 1st level and each "
            "level thereafter.",

        # kasatha traits
        "Desert Stride":
            "Kasathas can move through nonmagical difficult terrain in "
            "deserts, hills, and mountains at their normal speed.",

        "Four-Armed":
            "Kasathas have four arms, whih allows them to wield and hold up to "
            "four hands' worth of weapons and equipment.  While their multiple "
            "arms increase the number of items they can have at the ready, it "
            "doesn't increase the number of attacks they can make during "
            "combat.",

        "Historian":
            "Due to their in-depth historical training and the wide-ranging "
            "academic background knowledge they possess, kasathas receive a +2 "
            "racial bonus to Culture checks.",

        "Natural Grace":
            "Kasathas receive a +2 racial bonus to Acrobatics and Athletics "
            "checks.",

        # lashunta traits
        "Dimorphic":
            "All lashuntas gain +2 Charisma at character creation.  Korasha "
            "lashuntas are muscular (+2 Strength at character creation) but "
            "often brash and unobservant (-2 Wisdom at character creation). "
            "Damaya lashuntas are typically clever and well-spoken (+2 "
            "Intelligence at character creation) but somewhat delicate (-2 "
            "Constitution at character creation).",

        "Lashunta Magic":
            "Lashuntas gain the following spell-like abilities:\n\t"
            "At will: daze, psychokinetic hand\n\t"
            "1/day: detect thoughts\n"
            "See Spell-like Abilities on page 262 [of the Core Rulebook]. The "
            "caster level for these effects is equal to the lashunta's level.",

        "Limited Telepathy":
            "Lashuntas can mentally communicate with any creatures within 30 "
            "feet with whom they share a language. Conversing telepathically "
            "with multiple creatures simultaneously is just as difficult as "
            "listening to multiple people speaking.",

        "Student":
            "Lashuntas love to learn, and they receive a +2 racial bonus to "
            "any two skills of their choice.",

        # shirren traits
        "Blindsense":
            "Shirrens' sensitive antennae grant them blindsense (vibration)-"
            "the abilitiy to sense vibrations in the air-out to 30 feet. A "
            "shirren ignores the Stealth bonuses from any form of visual "
            "camouflage, invisibility and the like when attempting a "
            "Perception check opposed by a creature's Stealth check. Even on a "
            "successful Perception check, any foe that can't be seen still has "
            "total concealment (50% miss chance) against a shirren, and the "
            "shirren still has the normal miss chance when attacking foes that "
            "have concealment. A shirren is still flat-footed against attacks "
            "from creatures it can't see.",

        "Communalism":
            "Shirrens are used to working with others as part of a team. Once "
            "per day, as long as an ally is within 10 feet, a shirren can roll "
            "a single attack roll or skill check twice and take the higher "
            "result.",

        "Cultural Fascination":
            "Shirrens are eager to learn about new cultures and societies. "
            "Shirrens receive a +2 racial bonus to Culture and Diplomacy "
            "checks.",

        # Limited Telepathy: shared with lashunta

        # vesk traits
        "Armor Savant":
            "Vesk use armor in a way that complements their uniquely sturdy "
            "physiology. When wearing armor, they gain a +1 racial bonus to "
            "AC. When they're wearing heavy armor, their armor check penalty "
            "is 1 less severe than normal.",

        "Fearless":
            "Vesk receive a +2 racial bonus to saving throws against fear "
            "effects.",

        "Low-Light Vision":
            "Vesk can see in dim light as if it were normal light. For more "
            "details, see page 264 [of the Core Rulebook]",

        "Natural Weapons":
            "Vesk are always considered armed. They can deal 1d3 lethal damage "
            "with unarmed strikes, and the attack doesn't count as archaic. "
            "Vesk gain a unique weapon specialization with their natural "
            "weapons at 3rd level, allowing them to add 1-1/2 x their "
            "character level to their damage rolls for their natural weapons "
            "(instead of just adding their character level, as usual).",

        # ysoki traits
        "Cheek Pouches":
            "Ysoki can store up to 1 cubic foot of items weighing up to 1 bulk "
            "in total in their cheek pouches, and they can transfer a single "
            "object between hand and cheek as a swift action. A ysoki can "
            "disgorge the entire contents of his pouch onto the ground in his "
            "square as a move action that does not provoke an attack of "
            "opportunity",

        "Darkvision":
            "Ysoki can see up to 60 feet in the dark. See page 263 [of the "
            "Core Rulebook] for more information.",

        "Moxie":
            "Ysoki are scrappy and nimble even when the odds are against them. "
            "A ysoki can stand from prone as a swift action. Additionally, "
            "when off-kilter (see page 276 [of the Core Rulebook]), a ysoki "
            "does not take the normal penalties to attacks or gain the "
            "flat-footed condition. When attempting an Acrobatics chck to "
            "tumble through the space of an opponent at least one size "
            "category larger than himself, a ysoki receives a +5 racial bonus "
            "to the check.",

        "Scrounger":
            "Ysoki receive a +2 racial bonus to Engineering, Stealth, and "
            "Survival checks."
    }
