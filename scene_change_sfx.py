
"""
goblins_abode
scene_change_sfx.py
@author: arcarsenal444
purpose: this file executes sound effects when player-character
moves between rooms or investigates objects.
"""


# imports
from playsound3 import playsound
from random import randint


def entry_sounds():
    transition_sounds = [r"sfx\footsteps.wav",
                         r"sfx\creaky_door.mp3",
                         r"sfx\old_church_door.wav"]
    rand_num = randint(0, 2)
    sound_choice = transition_sounds[rand_num]
    playsound(sound_choice)

def investigating_sounds():
    inv_sound = r"sfx\hmm_sound.wav"
    playsound(inv_sound)

def lets_see_here():
    pass
    # NOTE: need to find a sound effect for this function.
    # let_see = r"sfx\lets_see.mp3"
    # playsound(let_see)




# OLD CODE/ CUT

# transition_sounds = [r"C:\Users\Joshb\Desktop\goblins_abode\footsteps.wav",
#                          r"C:\Users\Joshb\Desktop\goblins_abode\creaky_door.mp3",
#                          r"C:\Users\Joshb\Desktop\goblins_abode\old_church_door.wav"]


# inv_sound = r"C:\Users\Joshb\Desktop\goblins_abode\hmm_sound.wav"
