
"""
goblins_abode
goblins.py
@author: arcarsenal444
purpose: the goblin class file, which creates a new goblin
object each time a battle is initiated.
"""


# imports

import time


# Goblin class

class Goblin:
    def __init__(self, goblin_hp, goblin_total_hp, goblin_gold, goblin_xp, goblin_type):
        self.goblin_hp = goblin_hp
        self.goblin_total_hp = goblin_total_hp
        self.goblin_gold = goblin_gold
        self.goblin_xp = goblin_xp
        self.goblin_type = goblin_type

    def goblin_perish(self):
        print("The creature dies in the throes of agony, its black blood pooling on the cobbles.\n")
        time.sleep(1)
        print(f"You obtain {self.goblin_gold} gold pieces and {self.goblin_xp} xp.\n")
