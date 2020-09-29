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
        if '(' in theme.string:
            trim = theme.string.find('(')
        else:
            trim = theme.string.find('+')

        theme_space = theme.string[0:trim-1]

        themes_file.write(theme_space)
        themes_file.write('\n')

        theme_name = theme_space.replace(" ", "_")

        rel_path = theme_name + ".txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        sub_theme_file = open(abs_file_path, "w", encoding = "utf-8")

        theme_url = theme.a['href']
        theme_page = requests.get(theme_url)

        theme_soup = BeautifulSoup(theme_page.content, "html.parser")

        print(theme_url)

        tooltip = True
        prev_strong = False

        abilities_container = theme_soup.find("div", {"class": "article-content"})

        for ability in abilities_container.find_all("p"):
            ability_text = ability.getText()
            if "Starfinder" in ability_text:
                continue

            if tooltip == True:
                sub_theme_file.write("*%*")
                tooltip = False
            elif ability in theme_soup.find_all("p", {"class": "name"}):
                sub_theme_file.write('\n')
                sub_theme_file.write("*!*")
                prev_strong = True
            else:
                if prev_strong == True:
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
