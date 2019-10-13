import Race
import Themes
class Character:
    def __init__(self):
        self.my_race = Race.Race()
        self.my_theme = self.choose_theme()
        self.abilities = {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 10,
            "WIS": 10,
            "CHA": 10
        }

        for increase in self.my_race.ability_improvements:
            self.abilities[increase] += self.my_race.ability_improvements[increase]

        for increase in self.my_theme.ability_improvement:
            self.abilities[increase] += self.my_theme.ability_improvement[increase]

        self.increment_abilities()

        print(self.abilities)


    def choose_theme(self):
        chosen_theme = input("Select from Ace Pilot, Bounty Hunter, Icon, "
            "Mercenary, Outlaw, Priest, Scholar, Spacefarer, Xenoseeker, "
            "Themeless: ")
        if chosen_theme == "Ace Pilot":
            return Themes.AcePilot()
        elif chosen_theme == "Bounty Hunter":
            return Themes.BountyHunter()
        elif chosen_theme == "Icon":
            return Themes.Icon()
        elif chosen_theme == "Mercenary":
            return Themes.Mercenary()
        elif chosen_theme == "Outlaw":
            return Themes.Outlaw()
        elif chosen_theme == "Priest":
            return Themes.Priest()
        elif chosen_theme == "Scholar":
            return Themes.Scholar()
        elif chosen_theme == "Spacefarer":
            return Themes.Spacefarer()
        elif chosen_theme == "Xenoseeker":
            return Themes.Xenoseeker()
        else:
            return Themes.Themeless()


    def increment_abilities(self):
        remaining_points = 10
        while remaining_points > 0:
            print()
            print(self.abilities)
            print("You have {} points left to spend.".format(remaining_points))
            which_ability = input("Select from STR, DEX, CON, INT, WIS, CHA: ")
            add_how_many = int(input("How many points?: "))
            if add_how_many > remaining_points:
                print("You don't have that many points to spend.")
                continue
            elif self.abilities[which_ability] + add_how_many > 18:
                print("Final score cannot exceed 18.")
                continue
            else:
                self.abilities[which_ability] += add_how_many
                remaining_points -= add_how_many

dannie = Character()
