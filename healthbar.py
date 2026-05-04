health = 3
amount = 1

def status_health(self, health, amount):
    """Deplete or keep health depending on what is caught

    Args: 
        health (int): Health while fishing
        amount (int): Amount of health bars added or subtracted from health

    Side effects: 
        Health lowers, heals, or remains the same
        Print to stdout
    """
    for bar in health:
       if bad_item > 0:
           self.health -= amount
           print(f"Aw shucks! you caught a {bad_item}, your health is now at {health}/3!")
           
       elif healing_item > 0:
           self.health += amount
           print(f"Hip hip hooray! you caught a {healing_item}, your health is now at {health}/3!")
           
       elif junk_item > 0:
           print(f"Eh, you caught a {junk_item}, better luck next time!")
           
       else:
           print("You caught nothing!")
   
   
           
def items(self, bad_item, healing_item):
    """If this item is caught, it will affect health status

    Args:
        bad_item (_type_): Item hidden in grid that if caught, depletes health
    
    Side effects:
        health heals or lowers
        Print to stdout
    """