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
        while not points_allocated:
            layout = [
                [sg.Text('Please allocate up to 10 points.')],

                [sg.Text('STR: '), sg.Text(self.abilities["STR"]),
                                   sg.Slider(range=(0,18),
                                            default_value=self.abilities["STR"],
                                            orientation='horizontal')],

                [sg.Text('DEX: '), sg.Text(self.abilities["DEX"]),
                                   sg.Slider(range=(0,18),
                                            default_value=self.abilities["DEX"],
                                            orientation='horizontal')],

                [sg.Text('CON: '), sg.Text(self.abilities["CON"]),
                                   sg.Slider(range=(0,18),
                                            default_value=self.abilities["CON"],
                                            orientation='horizontal')],

                [sg.Text('INT: '), sg.Text(self.abilities["INT"]),
                                   sg.Slider(range=(0,18),
                                            default_value=self.abilities["INT"],
                                            orientation='horizontal')],

                [sg.Text('WIS: '), sg.Text(self.abilities["WIS"]),
                                   sg.Slider(range=(0,18),
                                            default_value=self.abilities["WIS"],
                                            orientation='horizontal')],

                [sg.Text('CHA: '), sg.Text(self.abilities["CHA"]),
                                   sg.Slider(range=(0,18),
                                            default_value=self.abilities["CHA"],
                                            orientation='horizontal')],

                [sg.OK(), sg.Cancel()]
            ]
            event, values = sg.Window("Allocate Stats", layout).Read()
            if event == "OK":
                add_how_many = 0
                if values[0]-self.abilities["STR"] > 0:
                    add_how_many += values[0]-self.abilities["STR"]
                if values[1]-self.abilities["DEX"] > 0:
                    add_how_many += values[1]-self.abilities["DEX"]
                if values[2]-self.abilities["CON"] > 0:
                    add_how_many += values[2]-self.abilities["CON"]
                if values[3]-self.abilities["INT"] > 0:
                    add_how_many += values[3]-self.abilities["INT"]
                if values[4]-self.abilities["WIS"] > 0:
                    add_how_many += values[4]-self.abilities["WIS"]
                if values[5]-self.abilities["CHA"] > 0:
                    add_how_many += values[5]-self.abilities["CHA"]

                if add_how_many > 10:
                    layout = [
                        [sg.Text('Please allocate only 10 points or fewer.')],
                        [sg.OK()]
                    ]
                    sg.Window("Too many points!", layout).Read()
                    continue
                elif add_how_many < 10:
                    layout = [
                        [sg.Text("You've allocated fewer than 10 points.")],
                        [sg.Text("Are you sure you want to continue?")],
                        [sg.Button('Yes'), sg.Button('No')]
                    ]
                    event, trash = sg.Window("Forfeit " + str(add_how_many-10)
                                             + " points?", layout).Read()
                    if event == "Yes":
                        self.commit_improvements(values)
                        points_allocated = True
                    else:
                        continue
                else:
                    self.commit_improvements(values)
                    points_allocated = True
            else:
                break


    def commit_improvements(self, values):
        self.abilities["STR"] = values[0]
        self.abilities["DEX"] = values[1]
        self.abilities["CON"] = values[2]
        self.abilities["INT"] = values[3]
        self.abilities["WIS"] = values[4]
        self.abilities["CHA"] = values[5]


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
