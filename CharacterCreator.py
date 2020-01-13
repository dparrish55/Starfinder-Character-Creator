import PySimpleGUI as sg
import Character

# my_race = choose_race()
# my_theme = choose_theme()
# my_character = Character.Character(my_race, my_theme)

# Character Name: [              ]  | Player Name: [              ]
# Class/Level: [------------] {Choose} | Race: [--------] {Choose}
# Theme: [--------------] {Choose} | Size: [--------] | Speed: [------]
# Homeworld: [        ] | Gender: [       ] | Alignment: [       ]
# Deity: [          ] | Initiative: [---] | SP: [--] | HP: [--] | RP: [--]
# ________________________________________________________________________
#       SCORE   MOD   |     ARMOR CLASS/ SAVING THROW     TOTAL
#  STR  [--]    [-]   |     Energy Armor Class            [--]
#  DEX  [--]    [-]   |     Kinetic Armor Class           [--]
#  CON  [--]    [-]   |     AC vs Combat Maneuvers        [--]
#  INT  [--]    [-]   |     Fortitude Save                [--]
#  WIS  [--]    [-]   |     Reflex Save                   [--]
#  CHA  [--]    [-]   |     Will Save                     [--]
#     {Generate}      |     DR: [--] | Resistances: [-------------]
# ________________________________________________________________________
#   ATTACK BONUSES               |          DETAIL VIEWERS
# Base Attack Bonus (BAB): [--]  |             {Skills}
# Melee Attack:  [--]            |             {Spells}
# Ranged Attack: [--]            |             {Traits}
# Thrown Attack: [--]            |
#                {OPEN}      {CANCEL}       {SAVE}

character_sheet = [
    [sg.Text('Character Name: '),
        sg.In("", key="char_name", size=(30,1), enable_events=True),
        sg.Text(" |   Player Name: "),
        sg.In("", key="player_name", size=(14,1), enable_events=True)],
    [sg.Text("Class/Level: "),
        sg.In("", key="class_level", disabled=True, size=(25,1)),
        sg.Button("Choose", key="btn_class_level", enable_events=True),
        sg.Text(" |   Race: "), sg.In("", key="race", disabled=True, size=(11,1)),
        sg.Button("Choose", key="btn_race", enable_events=True)],
    [sg.Text("Theme: "), sg.In("", key="theme", disabled=True, size=(14,1)),
        sg.Button("Choose", key="btn_theme", enable_events=True),
        sg.Text(" |   Size: "),
        sg.In("", key="size_cat", disabled=True, size=(8,1)),
        sg.Text(" |   Homeworld: "),
        sg.In("", key="homeworld", size=(14,1), enable_events=True)],
    [sg.Text("Speed: "),
        sg.In("", key="speed", disabled=True,  size=(6,1)),
        sg.Text(" |   Gender: "),
        sg.In("", key="gender", size=(12,1), enable_events=True),
        sg.Text(" |   Alignment: "),
        sg.In("", key="alignment", size=(26,1), enable_events=True)],
    [sg.Text("Deity: "), sg.In("", key="deity", size=(10,1)),
        sg.Text(" |   Initiative: "),
        sg.In("", key="initiative", disabled=True, size=(2,1)),
        sg.Text(" |   SP: "),
        sg.In("", key="stamina_points", disabled=True, size=(3,1)),
        sg.Text(" |   HP: "),
        sg.In("", key="hit_points", disabled=True, size=(3,1)),
        sg.Text(" |   RP: "),
        sg.In("", key="resolve_points", disabled=True, size=(3,1))],
    [sg.Text("_________________________________________________________________"
        "__________________")],
    [sg.Text("\tSCORE   MOD   |     ARMOR CLASS/ SAVING THROW     TOTAL")],
    [sg.Text("STR: "), sg.In("10", key="str_score", disabled=True, size=(3,1))],
    [sg.Text("DEX: "), sg.In("10", key="dex_score", disabled=True, size=(3,1))],
    [sg.Text("CON: "), sg.In("10", key="con_score", disabled=True, size=(3,1))],
    [sg.Text("INT: "), sg.In("10", key="int_score", disabled=True, size=(3,1))],
    [sg.Text("WIS: "), sg.In("10", key="wis_score", disabled=True, size=(3,1))],
    [sg.Text("CHA: "), sg.In("10", key="cha_score", disabled=True, size=(3,1))],
    [sg.Text("\t"), sg.Button("Generate", key="btn_generate", disabled=True, enable_events=True),
        sg.Button("View Traits", key="btn_traits", enable_events = True)]
]
new_character = Character.Character(character_sheet)
