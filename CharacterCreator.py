import Character
from Race import Race
import Themes
import PySimpleGUI as sg

def choose_race():
    races = ["Android", "Human", "Kasatha",
            "Lashunta", "Shirren", "Vesk", "Ysoki"]
    layout = [
        [sg.Text('Please select your character race.')],
        [sg.Text('Race: '), sg.Combo(races)],
        [sg.OK(), sg.Cancel()]
    ]

    event, values = sg.Window("Choose Race", layout).Read()
    if event == "OK":
        race_name = values[0]
        if race_name == "Lashunta":
            layout = [
                [sg.Text("Please select your Lashunta subrace.")],
                [sg.Text("Subrace: "), sg.Combo(["Korasha", "Damaya"])],
                [sg.OK(), sg.Cancel()]
            ]
            event, values = sg.Window("Choose Subrace", layout).Read()
        return Race(race_name, values[0])
    else:
        return None



def choose_theme():
    themes = ["Ace Pilot", "Bounty Hunter", "Icon", "Mercenary", "Outlaw",
             "Priest", "Scholar", "Spacefarer", "Xenoseeker", "Themeless"]

    layout = [
        [sg.Text('Please select your character theme.')],
        [sg.Text('Theme: '), sg.Combo(themes)],
        [sg.OK(), sg.Cancel()]
    ]

    event, values = sg.Window("Choose Theme", layout).Read()
    chosen_theme = values[0]

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

my_race = choose_race()
my_theme = choose_theme()
dannie = Character.Character(my_race, my_theme)
# print(my_race.race_name)
# print(my_race.subrace)
# print(my_race.ability_improvements)
# print(my_race.hp_improvement)
# print(my_race.size_category)
# print(my_race.type_kw)
# print(my_race.subtype_kw)
# print(my_race.traits)
