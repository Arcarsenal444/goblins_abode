
"""
goblins_abode
battle_decision.py
@author: arcarsenal444
purpose: this file executes once per loop through the main file and
determines whether a goblin foe is created.
"""


# imports

from random import randint


# battle_chance function

def battle_chance():
    """
    turned off this function so that I can have a battle each time to fix the problems with battles.
    """
    ran_num = randint(1, 3)  # NOTE: adjusted b: from 2 to 3 (9/21/24)
    if ran_num == 1:
        return True
    else:
        return False

    # return True

