import json
import random

class Outcomes:

    def __init__(self, health=3, max_health=3):
        self.health = health
        self.max_health = max_health

        with open("game_items.json", "r", encoding="utf-8") as file:
            self.game_items = json.load(file)

    def get_random_item(self, item_type):
        item_group = self.game_items["items"][item_type]
        return random.choice(list(item_group.values()))

        """Grabs random item from key value pair depending on where you choose to fish

        Args:
            bad_item (dict): An item to avoid that can negatively affect your health
            healing_item (dict): An item that can heal you if health is lost 
            junk_item (dict): An item that has no value whatsoever
            
        Side effects:
            Print to stdout
        """
        
    def status_health(self, item_symbol):
        
        """Deplete or keep health depending on what is caught

        Args: 
            health (int): Health while fishing
            amount (int): Amount of health bars added or subtracted from health

        Side effects: 
            Health lowers, heals, or remains the same
            Print to stdout
        """
        
        if item_symbol == "B":
            bad_item = self.get_random_item("bad_item")
            self.health -= 1
            print(f"Aw shucks! You caught a {bad_item}. Your health is now {self.health}/{self.max_health}.")

        elif item_symbol == "H":
            healing_item = self.get_random_item("healing_item")

            if self.health < self.max_health:
                self.health += 1

            print(f"Hip hip hooray! You caught a {healing_item}. Your health is now {self.health}/{self.max_health}.")

        elif item_symbol == "J":
            junk_item = self.get_random_item("junk_item")
            print(f"Eh, you caught a {junk_item}. Better luck next time!")

        else:
            print("You caught nothing!")

    def print_health(self):
        print(f"Health: {self.health}/{self.max_health}")