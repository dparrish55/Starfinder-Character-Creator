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

        theme_name = theme_space.replace(" ", "_")

        themes_file.write(theme_space +'\n')

        rel_path = theme_name + ".txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        if os.path.exists(abs_file_path):
            continue

        sub_theme_file = open(abs_file_path, "w", encoding="utf-8")

        theme_url = theme.a['href']
        theme_page = requests.get(theme_url)

        theme_soup = BeautifulSoup(theme_page.content, "html.parser")
        sub_theme_file.write(theme_mod)

        print(theme_url)

        tooltip = True
        prev_strong = False

        abilities_container = theme_soup.find("div", {"class": "article-content"})

        for ability in abilities_container.find_all("p"):
            ability_text = ability.getText()
            ability_text = ability_text.replace("(1st)", "").replace("(6th)", "").replace("(12th)", "").replace("(18th)", "")
            if "Starfinder" in ability_text:
                continue

            if tooltip:
                # sub_theme_file.write("*%*")
                tooltip = False
                tooltip_text = '\n' + theme_mod.replace("*_*", " or ")
                tooltip_text += ability_text[:ability_text.find('.')+1]
                # themes_file.write("*!*" + theme_space + '\n' + tooltip_text + '\n')
                # continue

            elif ability in theme_soup.find_all("p", {"class": "name"}):
                sub_theme_file.write('\n')
                # sub_theme_file.write("*!*")
                prev_strong = True
            else:
                if prev_strong:
                    sub_theme_file.write('\n')
                else:
                    sub_theme_file.write(' ')

                prev_strong = False

            if "Theme Knowledge" in ability_text:
                ability_text = ability_text.replace("Theme Knowledge", theme_space + " Knowledge")
            sub_theme_file.write(ability_text)

        sub_theme_file.write('\n')
        sub_theme_file.close()

    themes_file.close()


get_themes()
