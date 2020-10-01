import PySimpleGUI as sg
import Race
import Themes
import random
import os


class Character:
    def __init__(self, character_sheet):
        self.my_race = None
        self.my_theme = None
        self.my_level = 1
        self.generated = False
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
        character_window = sg.Window("Character Sheet", character_sheet)
        while True:
            character_event, values = character_window.Read()
            if character_event is None:
                break

            elif character_event == "btn_generate":
                for increase in self.my_race.ability_improvements:
                    self.ability_adjustments[increase] += self.my_race.ability_improvements[increase]

                for increase in self.my_theme.ability_improvement:
                    self.ability_adjustments[increase] += self.my_theme.ability_improvement[increase]

                self.generated = self.get_abilities()

                if self.generated:
                    for i in self.abilities.keys():
                        character_window.Element(i.lower()+"_score").Update(
                            str(self.abilities[i])
                        )

            elif character_event == "btn_class_level":
                sg.Popup("This is not ready yet. Sorry.")

            elif character_event == "btn_race":
                if self.choose_race():
                    character_window.Element("race").Update(
                        self.my_race.race_name
                    )

                    character_window.Element("hit_points").Update(
                        self.my_race.hp_improvement
                    )

                    character_window.Element("size_cat").Update(
                        self.my_race.size_category
                    )

            elif character_event == "btn_theme":
                if self.choose_theme():
                    character_window.Element("theme").Update(
                        self.my_theme.theme_name
                    )

            elif character_event == "btn_traits":
                layout = [
                    [sg.Text("Theme____________________________________________"
                             "______________________________")]
                ] + [
                        [sg.In(self.my_theme.traits[trait_level][0], disabled = True, size=(30,1))] +
                        [sg.Multiline(
                            self.my_theme.traits[trait_level][1],
                            disabled=True,
                            size=(45,5)
                        )] for trait_level in (1, 6, 12, 18)
                        if trait_level <= self.my_level and self.my_theme is not None
                ] + [[sg.Text("")]] + [
                    [sg.Text("Race_____________________________________________"
                             "______________________________")]
                ] + [
                    [sg.In(trait, disabled = True, size=(30,1))]+
                    [sg.Multiline(
                        Race.Race.racial_traits[trait],
                        disabled=True,
                        size=(45,5)
                    )] for trait in self.my_race.traits
                    if self.my_race is not None
                ] + [[sg.Text("")]]
                trait_window = sg.Window("Your Traits", layout)
                event, values = trait_window.Read()
                trait_window.Close()
                del trait_window

            activate_btn_generate = (
                self.my_race is not None and
                self.my_theme is not None and
                self.generated is False)

            character_window.Element("btn_generate").Update(
                disabled=not activate_btn_generate
            )

    def choose_race(self):
        races = ["Android", "Human", "Kasatha",
                 "Lashunta", "Shirren", "Vesk", "Ysoki"]
        layout = [
            [sg.Text('Please select your character race.')],
            [sg.Text('Race: '), sg.Combo(races)],
            [sg.OK(), sg.Cancel()]
        ]

        race_window = sg.Window("Choose Race", layout)
        event, values = race_window.Read()
        if event == "OK":
            race_name = values[0]
            race_window.close()
            del race_window
            if race_name == "Lashunta":
                layout = [
                    [sg.Text("Please select your Lashunta subrace.")],
                    [sg.Text("Subrace: "), sg.Combo(["Korasha", "Damaya"])],
                    [sg.OK(), sg.Cancel()]
                ]
                subrace_window = sg.Window("Choose Subrace", layout)
                event, values = subrace_window.Read()
                subrace_window.close()
                del subrace_window
                if event in (None, "Cancel"):
                    return False
                subrace_name = values[0]
            else:
                subrace_name = "N/A"
            self.my_race = Race.Race(race_name, subrace_name)
            return True
        else:
            self.my_race = None
            return False

    def choose_theme(self):
        script_dir = os.path.realpath("themes")
        rel_path = "themes.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        themes_file = open(abs_file_path, "r")
        themes = themes_file.read().splitlines()
        themes_file.close()
        themes.append("Themeless")

        layout = [
            [sg.Text('Please select your character theme.')],
            [sg.Text('Theme: '), sg.Combo(themes)],
            [sg.OK(), sg.Cancel()]
        ]
        theme_window = sg.Window("Choose Theme", layout)
        event, values = theme_window.Read()

        theme_window.close()

        if event == "OK":
            chosen_theme = values[0]
            self.my_theme = Themes.Theme(chosen_theme)

        print(self.my_theme.theme_name)

        del theme_window
        return event not in (None, "Cancel")

    def get_abilities(self):
        layout = [
            [sg.Radio('Point Buy', "RADIO1", default=True),
             sg.Radio('Array', "RADIO1"),
             sg.Radio('Roll', "RADIO1")],
            [sg.OK()]
        ]
        stat_method_window = sg.Window("Stat Generation Method", layout)
        event, values = stat_method_window.Read()

        stat_method_window.close()
        del stat_method_window

        if event is None:
            return False

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
        layout = [
            [sg.Text('Please allocate up to 10 points total.')],

            [sg.Text('You have '), sg.T('10',key='remaining_points'),
                               sg.Text(' points remaining.')]
        ] + [
            [sg.Text(ability+": "), sg.Text(self.abilities[ability]),
             sg.Slider(key=ability, range=(0, 18),
             default_value=self.abilities[ability],
             orientation="horizontal",
             enable_events=True)]
            for ability in self.abilities.keys()
        ] + [
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
                                             - self.abilities[abbrev])

                my_window.Element('remaining_points').Update(
                    str(int(remaining_points))
                )

        my_window.close()
        del my_window
        return points_allocated

    def commit_improvements(self, values):
        for abbrev in self.abilities.keys():
            self.abilities[abbrev] = int(values[abbrev])

    def pick_array(self):
        arrays = {
            "Focused": [18, 14, 11, 10, 10, 10],
            "Split": [16, 16, 11, 10, 10, 10],
            "Versatile": [14, 14, 14, 11, 10, 10]
        }

        layout =  [
            [sg.Radio(array_name, "RADIO0", key=array_name,
             tooltip=arrays[array_name], default=(array_name == "Focused"))
                for array_name in arrays.keys()
            ]
        ] + [
             [sg.OK()]
        ]
        array_window = sg.Window("Choose Array", layout)
        event, values = array_window.Read()

        array_window.close()
        del array_window

        if event is None:
            return False
        else:
            for value in values.keys():
                if values[value]:
                    which_array = arrays[value]

            self.allocate_abilities(which_array)
            return True

    def roll_stats(self):
        random.seed()
        rolled_scores = []
        for h in range (0,6):
            d6_rolls = []
            for i in range(0,4):
                d6_rolls.append(random.randint(0,6))

            d6_rolls.sort()
            rolled_scores.append(d6_rolls[1] + d6_rolls[2] + d6_rolls[3])
        return self.allocate_abilities(rolled_scores)

    def allocate_abilities(self, scores):
        scores.sort()
        scores = scores[::-1]

        disable_buttons = {
            "STR": False,
            "DEX": False,
            "CON": False,
            "INT": False,
            "WIS": False,
            "CHA": False
        }

        where_allocated = {
            "STR": None,
            "DEX": None,
            "CON": None,
            "INT": None,
            "WIS": None,
            "CHA": None
        }

        score_prompts = [
            [sg.Text("Where will you allocate " + str(scores[i]) + "?")]
            for i in range(0,6)
        ]

        radio_buttons = [
            [sg.Radio(ability, "RADIO"+str(i), key = ability + str(i),
             enable_events = True, disabled = disable_buttons[ability])
             for ability in self.abilities.keys()]
            for i in range(0,6)
        ]

        layout = []
        for i in range(0,6):
            layout.append(score_prompts[i])
            layout.append(radio_buttons[i])
        layout.append([sg.OK()])

        my_window = sg.Window("Allocate Stats", layout)

        while True:
            event, values = my_window.Read()

            disable_buttons = {
                "STR": False,
                "DEX": False,
                "CON": False,
                "INT": False,
                "WIS": False,
                "CHA": False
            }

            for value in values.keys():
                if values[value]:
                    disable_buttons[value[0:3]] = True
                    where_allocated[value[0:3]] = int(value[3])

            for i in (disable_buttons.keys()):
                for j in range(0,6):
                    which_to_update = i + str(j)
                    my_window.Element(which_to_update).Update(
                            disabled = disable_buttons[i])
            if event is None:
                return False

            elif event == "OK":
                do_not_commit = False
                for i in (self.abilities.keys()):
                    self.abilities[i] = (scores[where_allocated[i]]
                                    + self.ability_adjustments[i])
                    if self.abilities[i] > 18:
                        new_event = sg.PopupYesNo(i + " exceeds 18 with bonuses"
                                                      " added. This will forfeit " +
                                                      str(self.abilities[i] - 18) + " ability "
                                                      "points.  Would you like to continue?")
                        if new_event == "Yes":
                            self.abilities[i] = 18
                            do_not_commit = False
                        else:
                            do_not_commit = True

                if do_not_commit:
                    for i in (self.abilities.keys()):
                        for j in range(0,6):
                            which_to_update = i + str(j)
                            my_window.Element(which_to_update).Update(
                                False, disabled = False)
                            if i == "CHA":
                                my_window.Element(which_to_update).TKIntVar.set(0)
                    continue

                break

        my_window.close()
        del my_window
        return True
