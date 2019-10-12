class Race:
    # placeholder with basic concept for race selection
    # No error handling in place yet.
    def __init__(self):
        self.race_name = input(("Select from Android, Human, Kasatha, "
                                "Lashunta, Shirren, Vesk, Ysoki: "))
        self.ability_improvements = self.get_abilities()
        self.hit_point_improvement = self.get_hp()

    def get_abilities(self):
        by_name = {
            "Android": {"DEX": 2, "INT": 2, "CHA": -2},
            "Human": {self.prompt_ability(): 2},
            "Kasatha": {"STR": 2, "WIS": 2, "INT": -2},
            "Lashunta": self.divine_from_subrace(),
            "Shirren": {"CON": 2, "WIS": 2, "CHA": -2},
            "Vesk": {"STR": 2, "CON": 2, "INT": -2},
            "Ysoki": {"DEX": 2, "INT": 2, "STR": -2}
        }

        return by_name[self.race_name]

    def get_hp(self):
        by_name = {
            "Android": 4,
            "Human": 4,
            "Kasatha": 4,
            "Lashunta": 4,
            "Shirren": 6,
            "Vesk": 6,
            "Ysoki": 2
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
