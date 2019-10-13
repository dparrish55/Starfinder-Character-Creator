class Themeless:
    def __init__(self):
        self.ability_improvement = {self.prompt_ability(): 1}
        self.traits = {
            1: {"General Knowledge":
                "You gain a class skill of your choice when you create a "
                "themeless character. Also, you gain an ability adjustment of "
                "+1 to any ability score you choose."},
            6: {"Certainty":
                "Future Implement"},
            12: {"Extensive Studies":
                "Future Implement"},
            18: {"Steely Determination":
                "Future Implement"}
        }

        def prompt_ability(self):
            # placeholder with basic concept for method
            # No error handling in place yet.
            return input("Select from STR, DEX, CON, INT, WIS, CHA: ")
