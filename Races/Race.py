class Race:
    # placeholder with basic concept for race selection
    # No error handling in place yet.
    def __init__(self):
        self.race_name = input(("Select from Android, Human, Kasatha, "
                                "Lashunta, Shirren, Vesk, Ysoki: "))
        self.ability_improvements, self.hp_improvement = self.get_attributes()

    def get_attributes(self):
        by_name = {
            "Android": ({"DEX": 2, "INT": 2, "CHA": -2}, 4),
            "Human": ({self.prompt_ability(): 2}, 4),
            "Kasatha": ({"STR": 2, "WIS": 2, "INT": -2}, 4),
            "Lashunta": (self.divine_from_subrace(), 4),
            "Shirren": ({"CON": 2, "WIS": 2, "CHA": -2}, 6),
            "Vesk": ({"STR": 2, "CON": 2, "INT": -2}, 6),
            "Ysoki": ({"DEX": 2, "INT": 2, "STR": -2}, 2)
        }

        return by_name[self.race_name]

    def prompt_ability(self):
        # placeholder with basic concept for method
        # No error handling in place yet.
        if self.race_name == "Human":
            return input("Select from STR, DEX, CON, INT, WIS, CHA: ")

    def divine_from_subrace(self):
        ability_improvements = {
            "Korasha":{"STR": 2, "CHA": 2, "WIS": -2},
            "Damaya":{"INT": 2, "CHA": 2, "CON": -2}
        }
        # placeholder with basic concept for method
        # No error handling in place yet.
        if self.race_name == "Lashunta":
            return ability_improvements[input("Select from Korasha, Damaya: ")]
