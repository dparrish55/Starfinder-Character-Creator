import Races
import Themes
class Character:
    def __init__(self):
        self.my_race = Race()
        self.my_theme = self.choose_theme()

    def choose_theme():
        chosen_theme = input("Select from Ace Pilot, Bounty Hunter, Icon, "
            "Mercenary, Outlaw, Priest, Scholar, Spacefarer, Xenoseeker, "
            "Themeless: ")
        if chosen_theme == "Ace Pilot":
            return AcePilot()
        elif chosen_theme == "Bounty Hunter":
            return BountyHunter()
        elif chosen_theme == "Icon":
            return Icon()
        elif chosen_theme == "Mercenary":
            return Mercenary()
        elif chosen_theme == "Outlaw":
            return Outlaw()
        elif chosen_theme == "Priest":
            return Priest()
        elif chosen_theme == "Scholar":
            return Scholar()
        elif chosen_theme == "Spacefarer":
            return Spacefarer()
        elif chosen_theme == "Xenoseeker":
            return Xenoseeker()
        else:
            return Themeless()

dannie = Character()
