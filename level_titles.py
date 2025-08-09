
"""
goblins_abode
level_titles.py
@author: arcarsenal444
purpose: this file plays the fanfare for each new
level of the game.

NOTE: currently refashioning to accommodate floor changes
"""

# imports
from playsound3 import playsound
import sys
import time


def play_titles(hero_obj):
    playsound(r"sfx\level.wav")
    time_delay = 0.3
    level_name = f"WELCOME TO LEVEL {hero_obj.floor_level}\n\n"
    for char in level_name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(time_delay)
