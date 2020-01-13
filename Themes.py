import PySimpleGUI as sg
class AcePilot:
    def __init__(self):
        self.theme_name = "Ace Pilot"
        self.ability_improvement = {"DEX": 1}
        self.traits = {
            1: ("Ace Pilot Knowledge",
                "You are obsessed with starships and vehicles, and have "
                "committed to memory almost every related tidbit of knowledge "
                "you've ever come across. Reduce the DC of Culture checks to "
                "recall knowledge about starship and vehicle models and parts "
                "as well as famous hotshot pilots by 5.  Piloting is a class "
                "skill for you, though if it a class skill from the class you "
                "take at 1st level, you instead gain a +1 bonus to your "
                "Piloting checks. In addition, you gain an ability adjustment "
                "of +1 to Dexterity at character creation."),
            6: ("Lone Wolf",
                "Future Implement"),
            12: ("Need For Speed",
                "Future Implement"),
            18: ("Master Pilot",
                "Future Implement")
        }

class BountyHunter:
    def __init__(self):
        self.theme_name = "Bounty Hunter"
        self.ability_improvement = {"CON": 1}
        self.traits = {
            1: ("Bounty Hunter Knowledge",
                "Your mind is a cold steel trap when it comes to scraps of "
                "information about the creatures you're tracking down.  Choose "
                "a specific sentient creature that you can identify by name, "
                "alias, or specific identity to be your mark.  Reduce the DC "
                "of Culture or Profession (bounty hunter) checks to recall "
                "knowledge about your mark, as well as to recall knowledge "
                "about law-enforcement individuals and practices, by 5. "
                "If you choose a mark that is known only by an alias or secret "
                "identity, this ability helps you learn facts only about the "
                "identity you know about, not any other unknown identities. "
                "Once you defeat your mark, as an action that takes 1 minute, "
                "you can study dossiers and database information about another "
                "individual to be your new mark.  You can instead abandon your "
                "mark for a new one without defeating it, but if you do so, "
                "you take a -2 penalty to all skill checks for 1 week.  "
                "Survival is a class skill for you, though if it is a class "
                "skill from the class you take at 1st level, you instead gain "
                "a +1 bonus to Survival checks.  In addition, you gain an "
                "ability adjustment of +1 to Constitution at character "
                "creation."),
            6: ("Swift Hunter",
                "Future Implement"),
            12: ("Relentless",
                "Future Implement"),
            18: ("Master Hunter",
                "Future Implement")
        }

class Icon:
    def __init__(self):
        self.theme_name = "Icon"
        self.ability_improvement = {"CHA": 1}
        self.traits = {
            1: ("Icon Knowledge",
                "Choose a Profession skill. You are hooked deeply into the "
                "culture of your iconic profession.  When attempting a "
                "Profession or Culture check to recall knowledge about other "
                "icons of your profession or details about your profession's "
                "cultural aspects, increase the DC by 5.  You gain a +1 bonus "
                "to checks with your chosen Profession skill. "
                "Culture also becomes a class "
                "skill for you, though if it a class skill from the class you "
                "take at 1st level, you instead gain a +1 bonus to your "
                "Culture checks. In addition, you gain an ability adjustment "
                "of +1 to Charisma at character creation."),
            6: ("Celebrity",
                "Future Implement"),
            12: ("MegaCelebrity",
                "Future Implement"),
            18: ("Master Icon",
                "Future Implement")
        }

class Mercenary:
    def __init__(self):
        self.theme_name = "Mercenary"
        self.ability_improvement = {"STR": 1}
        self.traits = {
            1: ("Mercenary Knowledge",
                "You are knowledgeable about the military, from rival "
                "mercenary groups to standard military procedures to planetary "
                "armed forces, and you can draw upon this fount of information "
                "to aid your adventurous pursuits.  Reduce the DC of Culture "
                "checks and Profession (mercenary) checks to recall knowledge "
                "about hierarchies, practices, personnel, and so on in the "
                "military by 5. "
                "Athletics is a class skill for you, though if it is a class "
                "skill from the class you take at 1st level, you instead gain "
                "a +1 bonus to Athletics checks.  In addition, you gain an "
                "ability adjustment of +1 to Strength at character "
                "creation."),
            6: ("Grunt",
                "Future Implement"),
            12: ("Squad Leader",
                "Future Implement"),
            18: ("Commander",
                "Future Implement")
        }

class Outlaw:
    def __init__(self):
        self.theme_name = "Outlaw"
        self.ability_improvement = {"DEX": 1}
        self.traits = {
            1: ("Outlaw Knowledge",
                "You are well connected to shadowy secrets and back-alley "
                "deals, and you both know about key players and have handy "
                "skills of your own.  Reduce the DC of Culture checks to "
                "recall knowledge about the criminal underworld by 5. "
                "Sleight of Hand is a class skill for you, though if it is a "
                "class skill from the class you take at 1st level, you instead "
                "gain a +1 bonus to Sleight of Hand checks.  In addition, you "
                "gain an ability adjustment of +1 to Dexterity at character "
                "creation."),
            6: ("Legal Corruption",
                "Future Implement"),
            12: ("Black Market Connections",
                "Future Implement"),
            18: ("Master Outlaw",
                "Future Implement")
        }

class Priest:
    def __init__(self):
        self.theme_name = "Priest"
        self.ability_improvement = {"WIS": 1}
        self.traits = {
            1: ("Priest Knowledge",
                "Choose a deity or a philosophy whose alignment is within one "
                "step (on either the good-evil axis or the law-chaos axis) of "
                "your own.  Rduce the DC of Culture and Mysticism checks to "
                "recall knowledge about religious traditions, religious "
                "symbols, and famous religious leaders by 5. "
                "Mysticism is a class skill for you, though if it is a class "
                "skill from the class you take at 1st level, you instead gain "
                "a +1 bonus to Mysticism checks.  In addition, you gain an "
                "ability adjustment of +1 to Constitution at character "
                "creation."),
            6: ("Mantle of the Clergy",
                "Future Implement"),
            12: ("Divine Boon",
                "Future Implement"),
            18: ("True Communion",
                "Future Implement")
        }

class Scholar:
    def __init__(self):
        self.theme_name = "Scholar"
        self.ability_improvement = {"INT": 1}
        self.traits = {
            1: ("Scholar Knowledge",
                "You are an expert in one partiular field of study, and your "
                "passion for the subject shows.  Choose either Life Science or "
                "Physical Science and then choose a field of specialization.  "
                "If you pick Life Science, you can specialize in "
                "bioengineering, biology, botany, ecology, genetics, "
                "xenobiology, zoology, or another field of biological science. "
                "If you pick Physical Science, you can specialize in "
                "astronomy, chemistry, climatology, geography, geology, "
                "meteorology, oceanography, physics, or another field of "
                "physical science. The DC of skill checks to recall knowledge "
                "about your specialty is reduced by 5. "
                "Your chosen skill is a class skill for you, though if it is a "
                "class skill from the class you take at 1st level, you instead "
                "gain a +1 bonus to checks with your chosen skill.  In "
                "addition, you gain an ability adjustment of +1 to "
                "Intelligence at character creation."),
            6: ("Tip of the Tongue",
                "Future Implement"),
            12: ("Research Maven",
                "Future Implement"),
            18: ("Master Scholar",
                "Future Implement")
        }

class Spacefarer:
    def __init__(self):
        self.theme_name = "Spacefarer"
        self.ability_improvement = {"CON": 1}
        self.traits = {
            1: ("Spacefarer Knowledge",
                "You are obsessed with distant worlds, and you always mentally "
                "catalog everything you learn about new and strange places so "
                "you can recall it when you need it most.  Additionally, you "
                "use your knowledge of biology and topology to insure yourself "
                "to alien hazards. Reduce the DC of Physical Science checks to "
                "recall knowledge about strange new worlds or features of "
                "space by 5. "
                "Physical Science is a class skill for you, though if it is a "
                "class skill from the class you take at 1st level, you instead "
                "gain a +1 bonus to Physical Science checks.  In addition, you "
                "gain an ability adjustment of +1 to Constitution at character "
                "creation."),
            6: ("Eager Dabbler",
                "Future Implement"),
            12: ("Jack of All Trades",
                "Future Implement"),
            18: ("Master Explorer",
                "Future Implement")
        }

class Themeless:
    def __init__(self):
        self.theme_name = "Themeless"
        self.ability_improvement = {self.prompt_ability(): 1}
        self.traits = {
            1: ("General Knowledge",
                "You gain a class skill of your choice when you create a "
                "themeless character. Also, you gain an ability adjustment of "
                "+1 to any ability score you choose."),
            6: ("Certainty",
                "Future Implement"),
            12: ("Extensive Studies",
                "Future Implement"),
            18: ("Steely Determination",
                "Future Implement")
        }

    def prompt_ability(self):
        # placeholder with basic concept for method
        # No error handling in place yet.
        ability_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        layout = [
            [sg.Text('Please select your racial bonus.')],
            [sg.Text('+1 to: '), sg.Combo(ability_names)],
            [sg.OK()]
        ]
        event, values = sg.Window("Theme Bonus", layout).Read()
        return values[0]

class Xenoseeker:
    def __init__(self):
        self.theme_name = "Xenoseeker"
        self.ability_improvement = {"CHA": 1}
        self.traits = {
            1: ("Xenoseeker Knowledge",
                "You are trained to seek out, identify, and interact with "
                "alien life-forms. Reduce the DC to identify a rare creature "
                "using Life Science by 5. "
                "Life Science is a class skill for you, though if it is a "
                "class skill from the class you take at 1st level, you instead "
                "gain a +1 bonus to Life Science checks.  In addition, you "
                "gain an ability adjustment of +1 to Charisma at character "
                "creation."),
            6: ("Quick Pidgin",
                "Future Implement"),
            12: ("First Contact",
                "Future Implement"),
            18: ("Brilliant Discovery",
                "Future Implement")
        }
