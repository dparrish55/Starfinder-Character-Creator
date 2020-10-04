# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os


def get_themes():
    script_dir = os.path.realpath("themes")
    rel_path = "themes.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    themes_file = open(abs_file_path, "w")

    url = "https://www.starjammersrd.com/the-basics/character-themes/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    for theme in soup.find_all("li", {"class": "page new parent"}):
        theme_and_mod = theme.string.replace("(", "")
        theme_and_mod = theme_and_mod.replace(")", "")
        if '+' in theme_and_mod:
            trim = theme_and_mod.find('+')
        else:
            trim = theme.string.find('(')

        theme_space = theme_and_mod[0:trim-1]
        theme_mod = theme_and_mod[trim:] + '\n'
        theme_mod = theme_mod.replace("+1", "")
        theme_mod = theme_mod.replace(" ", "")
        theme_mod = theme_mod.replace(",", "or")
        theme_mod = theme_mod.replace("oror", "or")
        theme_mod = theme_mod.replace("or", "*_*")

        if theme_space == "Formless Emissary" or theme_space == "Infamous":
            theme_mod = "Cha"
        elif theme_space == "Shipbuilder":
            theme_mod = "Int"

        theme_name = theme_space.replace(" ", "_")

        themes_file.write(theme_space + '\n')

        rel_path = theme_name + ".txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        if os.path.exists(abs_file_path):
            continue

        sub_theme_file = open(abs_file_path, "w")

        theme_url = theme.a['href']
        theme_page = requests.get(theme_url)

        theme_soup = BeautifulSoup(theme_page.content, "html.parser")
        sub_theme_file.write(theme_mod + '\n')

        print(theme_url)

        prev_strong = False

        abilities_container = theme_soup.find("div", {"class": "article-content"})
        headings = theme_soup.find_all("p", {"class": "name"})

        first_line = True
        for ability in abilities_container.find_all("p"):
            ability_text = ability.getText()
            # ability_text = ability_text.replace("(1st)", "").replace("(6th)", "").replace("(12th)", "").replace("(18th)", "")
            ability_text = ability_text.encode("windows-1252", "replace").decode("windows-1252", "replace")

            if "Theme Knowledge" in ability_text:
                ability_text = ability_text.replace("Theme Knowledge", theme_space + " Knowledge")

            if "Starfinder" in ability_text:
                continue

            if theme_space == "Infamous" and "18th" in ability_text:
                rel_path = "Icon.txt"
                abs_file_path = os.path.join(script_dir, rel_path)
                icon_file = open(abs_file_path, "r")
                lines = icon_file.readlines()
                sub_theme_file.write("\nInfamous (6th)\n")
                sub_theme_file.write(lines[5])
                sub_theme_file.write("Dreaded (12th)\n")
                sub_theme_file.write(lines[7])
                prev_strong = True
                icon_file.close()

            elif headings != []:
                if ability in headings:
                    sub_theme_file.write('\n')
                    prev_strong = True
                else:
                    if prev_strong:
                        sub_theme_file.write('\n')
                    else:
                        sub_theme_file.write(' ')

                    prev_strong = False

                sub_theme_file.write(ability_text)

            else:
                if prev_strong or "(1st)" in ability_text:
                    sub_theme_file.write('\n')
                else:
                    sub_theme_file.write(' ')

                if "(1st)" in ability_text:
                    splitter = ability_text.find("(1st)")
                    sub_theme_file.write(ability_text[:splitter + 5] + '\n')
                    sub_theme_file.write(ability_text[splitter + 7:])
                    prev_strong = True
                elif "(6th)" in ability_text:
                    splitter = ability_text.find("(6th)")
                    sub_theme_file.write(ability_text[:splitter + 5] + '\n')
                    sub_theme_file.write(ability_text[splitter + 7:])
                    prev_strong = True
                elif "(12th)" in ability_text:
                    splitter = ability_text.find("(12th)")
                    sub_theme_file.write(ability_text[:splitter + 6] + '\n')
                    sub_theme_file.write(ability_text[splitter + 8:])
                    prev_strong = True
                elif "(18th)" in ability_text:
                    splitter = ability_text.find("(18th)")
                    sub_theme_file.write(ability_text[:splitter + 6] + '\n')
                    sub_theme_file.write(ability_text[splitter + 8:])
                    prev_strong = True
                else:
                    sub_theme_file.write(ability_text)
                    prev_strong = False

        sub_theme_file.write('\n')
        sub_theme_file.close()

    themes_file.close()

    rel_path = "Themeless.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    if not os.path.exists(abs_file_path):
        sub_theme_file = open(abs_file_path, "w")

        sub_theme_file.write("Str*_*Dex*_*Con*_*Int*_*Wis*_*Cha\n"
                             "Your background doesn't fit into any of the listed options.  But that doesn't stop you "
                             "from having an awesome backstory that gives you some equivalent boosts!\n"
                             "General Knowledge\n" 
                             "You gain a class skill of your choice when you create a themeless character.  Also, you "
                             "gain an ability adjustment of +1 to any ability score you choose.\n"
                             "Certainty\n"
                             "Once per day before you roll a skill check, you can gain a +2 bonus to that skill for "
                             "that check.\n"
                             "Extensive Studies\n"
                             "Choose a skill that is a class skill for you.  Once per day, you can reroll one such "
                             "skill check before learning the results of the roll.  You must take the second result, "
                             "even if it is worse.\n"
                             "Steely Determination\n" 
                             "Increase your pool of Resolve Points by 1.\n")
        sub_theme_file.close()


get_themes()
