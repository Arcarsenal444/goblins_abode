
"""
goblins_abode
opening_sequence.py
@author: arcarsenal444
purpose: this file runs the opening sequence and
executes once per game.
"""

# imports
import time
from playsound3 import playsound
from images import goblin_image
from images import game_font


def opening_sequence(hero_obj):
    print(game_font.typeface)
    playsound(r"sfx\intro_drums.wav")
    time.sleep(0.5)
    print(goblin_image.goblin_art)
    playsound(r"sfx\intro_drums.wav")
    time.sleep(0.5)
    print(f"\n{hero_obj.character_name} enters the door to the goblins' abode.\n")
    time.sleep(0.5)
