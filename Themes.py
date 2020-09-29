# coding=utf-8
import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup


def get_themes():
    url = "https://www.starjammersrd.com/the-basics/character-themes/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    themes_list = []
    for theme in soup.find_all("li", {"class": "page new parent"}):
        if '(' in theme.string:
            trim = theme.string.find('(')
            themes_list.append(theme.string[0:trim-1])
        else:
            trim = theme.string.find('+')
            themes_list.append(theme.string[0:trim-1])

    return themes_list



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
                "You know at least a little bit about handling every role on "
                "a starship, and you can sub in for certain tasks in a pinch. "
                "Whenever you need to attempt a skill check either during "
                "starship combat or to directly repair or otherwise maintain "
                "your starship, you can treat half your ranks in Piloting as "
                "your ranks in the appropriate skill for the check, if that "
                "would be better (since you effectively have ranks in the "
                "related skill, you are considered trained in the skill for "
                "the purposes of this check)."),
            12: ("Need For Speed",
                 "Speeding in a vehicle gives you a heady rush, and you can "
                 "easily handle operating vehicles at high velocities that "
                 "might send lesser pilots spinning out of control. Reduce any "
                 "penalties to Piloting checks you make when on a vehicle by 1. "
                 "When you take the double maneuver action during a vehicle "
                 "chase, reduce the penalty for each action by 1. Whenever a "
                 "Piloting check has a penalty for failing by 5 or more, you take "
                 "that penalty only if you fail by 10 or more."),
            18: ("Master Pilot",
                 "Your piloting accomplishments invigorate you, giving you renewed "
                 "purpose and zeal. Up to twice per day, when you defeat a significant "
                 "foe in starship combat as a pilot or succeed in a vehicle chase "
                 "(meaning that you’ve either escaped a pursuer or caught or defeated your "
                 "opponent), you recover 1 Resolve Point.")
        }


class Athlete:
    def __init__(self):
        self.theme_name = "Athlete"
        self.ability_improvement = {self.prompt_ability(): 1}
        self.traits = {
            1: ("Athlete Knowledge",
                "You’ve been involved in your sport or activity for years, and you know a "
                "great deal about the industry. When recalling knowledge regarding details "
                "of your industry, whether historical or current, reduce the DC of the "
                "Culture check by 5. In addition, based on the primary abilities required "
                "in your chosen sport, either Acrobatics (for Dexterity or Constitution) or "
                "Athletics (for Strength or Constitution) is a class skill for you, though "
                "if the relevant skill is a class skill from the class you take at 1st level, "
                "you instead gain a +1 bonus to your Acrobatics or Athletics checks. "
                " "
                "Likewise, you gain an ability adjustment of +1 to either Strength, Dexterity, "
                "or Constitution at character creation, depending on which ability is most "
                "relevant to your athletic endeavors."),
            6: ("Physical Prowess",
                "Athletes who chose Acrobatics at 1st level can move at full speed while "
                "balancing and do not fall prone on a failed attempt to tumble through an "
                "opponent’s square. Athletes who chose the Athletics skill at 1st level can "
                "move at full speed while climbing and can attempt a vertical or horizontal "
                "jump with merely a 5-foot running start, rather than the 10 feet normally required."),
            12: ("Fan Favorite",
                 "When you’re in a region that recognizes your sport and need an act of goodwill—"
                 "such as information from a journalist or medical assistance from a physician—you "
                 "can take 3d4 hours to locate a fan or industry professional whose attitude starts "
                 "as helpful toward you."),
            18: ("Champion",
                 "The memories of triumphs attained and challenges overcome can bolster you when "
                 "facing current difficulties. Up to twice per day when in an area with gravity you "
                 "have adjusted to, you can spend 10 minutes stretching, exercising, meditating, or "
                 "performing other sport-specific drills to regain 1 Resolve Point.")
        }

    def prompt_ability(self):
        # placeholder with basic concept for method
        # No error handling in place yet.
        ability_names = ["STR", "DEX", "CON"]
        layout = [
            [sg.Text('Please select your theme bonus.')],
            [sg.Text('+1 to: '), sg.Combo(ability_names)],
            [sg.OK()]
        ]
        event, values = sg.Window("Theme Bonus", layout).Read()
        return values[0]


class Biotechnician:
    def __init__(self):
        self.theme_name = "Biotechnician"
        self.ability_improvement = {"INT": 1}
        self.traits = {
            1: ("Biotechnician Knowledge",
                "You have a sharp mind for the intricacies of biotech augmentations and keep up-to-date "
                "on current research in the field, whether because you work to develop such technology or "
                "because you are the beneficiary of biotech augmentations — or, most likely, both. Reduce "
                "the DC of Life Science checks to identify biotech augmentations and to recall knowledge "
                "about famous biotech corporations and researchers by 5. Medicine is a class skill for "
                "you, though if it is a class skill from the class you take at 1st level, you instead gain "
                "a +1 bonus to your Medicine checks. In addition, you gain an ability adjustment of +1 to "
                "Intelligence at character creation."),
            6: ("Industry Connections",
                "You’ve forged and maintained a number of connections with significant players in the biotech "
                "industry, scoring yourself favors and preferred treatment. As long as you are able to contact "
                "your connections in the industry, you gain a 10% discount off the typical list price for "
                "biotech augmentations installed in you."),
            12: ("Test Subject",
                 "Thanks to your enthusiasm for biotech gear and constant tinkering with your DNA, you can "
                 "adopt experimental, cutting-edge augmentations in your body beyond what most people can "
                 "support. You can install one additional piece of biotech augmentation than a typical member "
                 "of your race. For example, a human could have both a dragon gland and a wildwise implant "
                 "even though they both occupy the throat system."),
            18: ("Adaptive Biotech",
                 "You have learned to leverage your biotech augmentations in ways their creators hardly "
                 "envisioned. Up to twice per day as a standard action, you can deactivate a piece of "
                 "biotech implanted in your body (except for a prosthetic limb), rendering it inert until "
                 "your next 8-hour rest, to regain 1 Resolve Point. An inert piece of biotech doesn’t grant "
                 "its usual benefits (for instance, an inert venom spur can’t be used to attack), and you "
                 "can shut down a single biotech implant only once per day.")
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
                "You know just how to ask around about your marks to gain information "
                "and insight in a hurry. You can use Diplomacy to gather information "
                "about a specific individual in half the normal time, and you reduce "
                "the penalty for following tracks using Survival while moving at full "
                "speed to 0."),
            12: ("Relentless",
                 "You never seem to get tired, even when working longer and harder than "
                 "everyone else in pursuit of your mark; some of your targets might even "
                 "refer to you as a tireless ghost or an all-seeing hunter. You can walk "
                 "or be otherwise active for 12 hours instead of 8 before needing to "
                 "attempt Constitution checks for a forced march, and you can hustle for "
                 "2 hours a day during overland travel instead of 1 hour. Reduce the "
                 "penalty for following tracks using Survival while moving at double speed "
                 "to –10."),
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
            [sg.Text('Please select your theme bonus.')],
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
