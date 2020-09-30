# coding=utf-8
import PySimpleGUI as sg
import os


class Theme:
    def __init__(self, theme_name):
        self.theme_name = theme_name

        script_dir = os.path.realpath("themes")
        rel_path = self.theme_name.replace(" ", "_") + ".txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        sub_theme_file = open(abs_file_path, "r")

        lines = sub_theme_file.read().splitlines()

        if "*_*" in lines[0]:
            ability_names = lines[0].upper().split("*_*")
            self.ability_improvement = {self.prompt_ability(ability_names): 1}
        else:
            self.ability_improvement = {lines[0]: 1}

        self.traits = {
            1: (lines[2], lines[3]),
            6: (lines[4], lines[5]),
            12: (lines[6], lines[7]),
            18: (lines[8], lines[9])
        }

    def prompt_ability(self, ability_names):
        layout = [
            [sg.Text('Please select your theme bonus.')],
            [sg.Text('+1 to: '), sg.Combo(ability_names)],
            [sg.OK()]
        ]
        ability_prompt_window = sg.Window("Theme Bonus", layout)
        event, values = ability_prompt_window.Read()
        ability_prompt_window.close()
        del ability_prompt_window
        return values[0]


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

