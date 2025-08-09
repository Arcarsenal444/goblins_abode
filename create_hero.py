
"""
goblins_abode
create_hero.py
@author: arcarsenal444
purpose: this file activates once per game, at the very beginning, and
links to the character class file (character.py) to create the player-character.

NOTE: this file is being modified to accommodate for moving from the first floor
to the second (and farther upwards as new floors are created); this is being achieved
through use of the floor_level attribute.
"""


# imports

from character import Character
import os
import persistence

def create_hero():
    char_name = input("What is your character's name? ")
    hero = Character(character_hp=20, character_total_hp=20, character_gold=0, character_name=char_name,
                     character_level=1, character_xp=0, character_attack_strength=0, floor_level=1)
    game_file_dir = 'game_files'
    hero.load_if_saved(game_file_dir)
    return hero

"""
NOTE: I haven't written in the character_attack_strength code yet.
So far it's just an attribute, but it will have to have an impact
on the attack and damage rolls, which means changing or adding to
the code in battle_file.py.
"""
