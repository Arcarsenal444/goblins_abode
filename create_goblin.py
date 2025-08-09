
"""
goblins_abode
create_goblin.py
@author: arcarsenal444
purpose: in goblins_abode, the player-character can fight one of three
types of goblin each time a battle is triggered. this file determines
which of the goblin types materializes.
"""


# imports

import time
from playsound3 import playsound
import random
from goblins import Goblin


def create_goblin():

    rand_num = random.randint(1, 15)

    if rand_num == 15:
        time.sleep(1)
        # playsound(r"C:\Users\Joshb\Desktop\goblins_abode\goblin_appears.wav")
        playsound(r"sfx\goblin_appears.wav")
        print("\nA trogo-goblin roars out from the dark shadows of the chamber!\n")

        # NOTE: Need image of trogo-goblin to appear here.

        goblin_hp = random.randint(16, 18)  # turning these off for now to fix battle
        # goblin_hp = 99  # REMOVE WHEN CLEANING
        goblin_total_hp = goblin_hp
        goblin_gold = random.randint(40, 75)
        goblin_xp = random.randint(45, 60)
        goblin_type = "trogo-goblin"
        goblin = Goblin(goblin_hp, goblin_total_hp, goblin_gold, goblin_xp, goblin_type)

        return goblin

    elif 15 > rand_num > 11:
        time.sleep(1)
        # playsound(r"C:\Users\Joshb\Desktop\goblins_abode\goblin_appears.wav")
        playsound(r"sfx\goblin_appears.wav")
        print("\nA hobgoblin leaps from the corner!\n")

        # NOTE: Need image of hobgoblin to appear here.

        goblin_hp = random.randint(12, 16)
        # goblin_hp = 99  # REMOVE WHEN CLEANING
        goblin_total_hp = goblin_hp
        goblin_gold = random.randint(20, 50)
        goblin_xp = random.randint(20, 45)
        goblin_type = "hobgoblin"
        goblin = Goblin(goblin_hp, goblin_total_hp, goblin_gold, goblin_xp, goblin_type)

        return goblin

    else:
        time.sleep(1)
        # playsound(r"C:\Users\Joshb\Desktop\goblins_abode\goblin_appears.wav")
        playsound(r"sfx\goblin_appears.wav")
        print("\nSuddenly a goblin appears!\n")

        # NOTE: Need image of goblin to appear here.

        goblin_hp = random.randint(4, 11)
        # goblin_hp = 99  # REMOVE WHEN CLEANING
        goblin_total_hp = goblin_hp
        goblin_gold = random.randint(1, 20)
        goblin_xp = random.randint(10, 20)
        goblin_type = "goblin"
        goblin = Goblin(goblin_hp, goblin_total_hp, goblin_gold, goblin_xp, goblin_type)

        return goblin
