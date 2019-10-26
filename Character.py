import Race
import Themes
import random
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
        self.ability_adjustments = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }
        for increase in self.my_race.ability_improvements:
            self.ability_adjustments[increase] += self.my_race.ability_improvements[increase]

        for increase in self.my_theme.ability_improvement:
            self.ability_adjustments[increase] += self.my_theme.ability_improvement[increase]

        self.get_abilities()

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


    def get_abilities(self):
        print()
        print("1) Point Buy - Use an assigned number of points to customize "
              "your ability scores.")
        print("2) Array - Choose from three arrays to distribute your ability "
              "scores quickly.")
        print("3) Roll Stats - Completely randomize your abilities.")

        which_method = int(input("How would you like to generate your ability"
                                 "scores?: "))

        if which_method == 1:
            return self.point_buy()
        elif which_method == 2:
            return self.pick_array()
        elif which_method == 3:
            return self.roll_stats()
        else:
            print("Invalid entry. Please enter 1, 2, or 3.")
            return self.get_abilities()


    def point_buy(self):
        for increase in self.ability_adjustments:
            self.abilities[increase] += self.ability_adjustments

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
                if add_how_many < 0:
                    add_how_many = 0
                remaining_points -= add_how_many


    def pick_array(self):
        focused_array = [18, 14, 11, 10, 10, 10]
        split_array = [16, 16, 11, 10, 10, 10]
        versatile_array = [14, 14, 14, 11, 10, 10]
        arrays = {1: focused_array, 2: split_array, 3: versatile_array}

        print()
        print("1)   Focused - {}".format(focused_array))
        print("2)     Split - {}".format(split_array))
        print("3) Versatile - {}".format(versatile_array))
        which_array = arrays[int(input("Which array would you like to take?: "))]

        print("You have chosen the array: {}".format(which_array))
        self.allocate_abilities(which_array)


    def roll_stats(self):
        print()
        print("Rolling...")
        random.seed()
        rolled_scores = []
        for h in range (0,6):
            d6_rolls = []
            for i in range(0,4):
                d6_rolls.append(random.randint(0,6))

            d6_rolls.sort()
            rolled_scores.append(d6_rolls[1] + d6_rolls[2] + d6_rolls[3])
        print("You've rolled {}".format(rolled_scores))
        self.allocate_abilities(rolled_scores)


    def allocate_abilities(self, scores):
        assigned_abilities = []
        for score in scores:
            loop_break = False
            while not loop_break:
                loop_break = True
                which_ability = input("To which stat shall you assign the "
                                    "score {}?: ".format(score))
                if which_ability not in assigned_abilities:
                    projection = score
                    projection += self.ability_adjustments[which_ability]
                    if projection > 18:
                        projection = 18
                        yes_or_no = input(which_ability + " will exceed 18 "
                        "after modifiers. All points exceeding 18 will be "
                        "lost. Do you wish to continue despite this?(Y/N): ")
                        if yes_or_no == 'N':
                            loop_break = False
                    if loop_break:
                        assigned_abilities.append(which_ability)
                        self.abilities[which_ability] = projection
                else:
                    loop_break = False


dannie = Character()
