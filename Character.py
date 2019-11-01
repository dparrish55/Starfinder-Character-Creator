import PySimpleGUI as sg
import Race
import Themes
import random
class Character:
    def __init__(self, my_race, my_theme):
        self.my_race = my_race
        self.my_theme = my_theme
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

        print("Your ability scores are: ")
        print(self.abilities)
        print()
        print("Your Racial Traits are: ")
        print(self.my_race.traits)


    def get_abilities(self):
        layout =  [
            [sg.Radio('Point Buy', "RADIO1", default=True),
             sg.Radio('Array', "RADIO1"),
             sg.Radio('Roll', "RADIO1")],
             [sg.OK()]
        ]
        event, values = sg.Window("Stat Generation Method", layout).Read()

        if values[0]:
            return self.point_buy()
        elif values[1]:
            return self.pick_array()
        else:
            return self.roll_stats()


    def point_buy(self):
        for increase in self.ability_adjustments:
            self.abilities[increase] += self.ability_adjustments[increase]

        points_allocated = False
        remaining_points = 10
        layout = [
            [sg.Text('Please allocate up to 10 points total.')],

            [sg.Text('You have '), sg.T('10',key='remaining_points'),
                               sg.Text(' points remaining.')],

            [sg.Text('STR: '), sg.Text(self.abilities["STR"]),
                               sg.Slider(key = "STR", range=(0,18),
                               default_value=self.abilities["STR"],
                               orientation='horizontal',
                               enable_events = True)],

            [sg.Text('DEX: '), sg.Text(self.abilities["DEX"]),
                               sg.Slider(key = "DEX", range=(0,18),
                               default_value=self.abilities["DEX"],
                               orientation='horizontal',
                               enable_events = True)],

            [sg.Text('CON: '), sg.Text(self.abilities["CON"]),
                               sg.Slider(key = "CON", range=(0,18),
                               default_value=self.abilities["CON"],
                               orientation='horizontal',
                               enable_events = True)],

            [sg.Text('INT: '), sg.Text(self.abilities["INT"]),
                               sg.Slider(key = "INT", range=(0,18),
                               default_value=self.abilities["INT"],
                               orientation='horizontal',
                               enable_events = True)],

            [sg.Text('WIS: '), sg.Text(self.abilities["WIS"]),
                               sg.Slider(key = "WIS", range=(0,18),
                               default_value=self.abilities["WIS"],
                               orientation='horizontal',
                               enable_events = True)],

            [sg.Text('CHA: '), sg.Text(self.abilities["CHA"]),
                               sg.Slider(key = "CHA", range=(0,18),
                               default_value=self.abilities["CHA"],
                               orientation='horizontal',
                               enable_events = True)],

            [sg.OK(), sg.Cancel()]
        ]
        my_window = sg.Window("Allocate Stats", layout)
        while not points_allocated:
            event, values = my_window.Read()

            if event == "OK":
                add_how_many = 0
                for abbrev in self.abilities.keys():
                    if values[abbrev]-self.abilities[abbrev] > 0:
                        add_how_many += values[abbrev]-self.abilities[abbrev]

                if add_how_many > 10:
                    sg.Popup("Please allocate only 10 points or fewer.")
                    continue
                elif add_how_many < 10:
                    remaining_points = int(10 - add_how_many)
                    event = sg.PopupYesNo("Forfeit " + str(remaining_points)
                                             + " unallocated points?")
                    if event == "Yes":
                        self.commit_improvements(values)
                        points_allocated = True
                    else:
                        continue
                else:
                    self.commit_improvements(values)
                    points_allocated = True

            elif event in (None, "Cancel"):
                break

            else:
                remaining_points = 10
                for abbrev in self.abilities.keys():
                    if values[abbrev]-self.abilities[abbrev] > 0:
                        remaining_points -= (values[abbrev]
                                           -self.abilities[abbrev])

                my_window.Element('remaining_points').Update(
                    str(int(remaining_points))
                )


    def commit_improvements(self, values):
        for abbrev in self.abilities.keys():
            self.abilities[abbrev] = int(values[abbrev])


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
                    print("That ability already has an assigned score.")
                    loop_break = False
