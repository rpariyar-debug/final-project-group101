import json
import random

class Outcomes:

    def caught_items(self, bad_item, healing_item, junk_item):
        """Grabs random item from key value pair depending on where you choose to fish

        Args:
            bad_item (dict): An item to avoid that can negatively affect your health
            healing_item (dict): An item that can heal you if health is lost 
            junk_item (dict): An item that has no value whatsoever
            
        Side effects:
            Print to stdout
        """
        self.bad_item = bad_item
        self.healing_item = healing_item
        self.junk_item = junk_item
        
        with open("game_items.json", "r", encoding="utf-8") as file:
            game_items = json.load(file)
        
        for selection in grid:
            random.choice(game_items["items"])
            



    def status_health(self, health, amount):
        """Deplete or keep health depending on what is caught

        Args: 
            health (int): Health while fishing
            amount (int): Amount of health bars added or subtracted from health

        Side effects: 
            Health lowers, heals, or remains the same
            Print to stdout
        """
        health = 3
        amount = 1
    
        for bar in health:
            if bad_item > 0:
                self.health -= amount
                print(f"Aw shucks! you caught a {bad_item}, your health is now at {health}!/3")
                
            elif healing_item > 0:
                self.health += amount
                print(f"Hip hip hooray! you caught a {healing_item}, your health is now at {health}!/3")
                
            elif junk_item > 0:
                print(f"Eh, you caught a {junk_item}, better luck next time!")
                
            else:
                print("You caught nothing!")