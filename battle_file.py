
"""
goblins_abode
battle_file.py
@author: arcarsenal444
purpose: executes the battles between player-character and
the goblins when they materialize.
"""

# imports
import time
from random import randint
from tkinter import *
from health_bars import display_health_bars
from playsound3 import playsound
from level_up import level_increase
import json


# logging
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, # Minimum level to log
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log', # File to write logs to
                    filemode='a') # Append to the log file

# Get a logger instance
logger = logging.getLogger(__name__)

DEBUG = True
def _D(s = ""):
    global DEBUG
    if DEBUG == True:
        # logger.info(f"--> DEBUG: {s}")
        print(f"--> DEBUG: battle_2 {s}")


# global variables
hero_attack_roll = 0
hero_damage_roll = 0


# BATTLE FUNCTIONS

# 1. do_battle function
def do_battle(hero, goblin):
    ran_num = randint(1, 2)
    if ran_num == 1:
        fighter_1 = hero
        fighter_2 = goblin
    else:
        fighter_1 = goblin
        fighter_2 = hero

    battle_decision = attack(fighter_1, fighter_2)
    return battle_decision

"""
    # if battle_decision == "win":
    #     return True
    # elif battle_decision == "lose":
    #     return False
    # return None

# OLDER CODE
#     battle_decision = attack(fighter_1, fighter_2)
#     if battle_decision == "win":
#         return True
#     elif battle_decision == "lose":
#         return False

# OLDER CODE THAT DIDN'T END THE GAME WHEN I DIED

    # combat = True  # This line and the while combat: may not be needed.
    # while combat:
    #     battle_decision = attack(fighter_1, fighter_2)
    #     # NOTE: 9/28/2024 - i got killed but the game continued. What is the battle_decision I'm sending back?
    #     # print(battle_decision)  # None
    #     # print(type(battle_decision))  # <class 'NoneType'>
    #     return battle_decision

"""

# 2. attack function
def attack(fighter_1, fighter_2):
    verdict = True  # BJL: moved verdict definition/default here from orig (originally ~ line 15-ish)
    if hasattr(fighter_1, "character_hp"):
        print("You ready yourself to attack...\n")

        # Creating a new window and configurations
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=50)

        # Labels
        label = Label(text="Attack")
        label.pack()

        # Buttons
        def attack_roll():
            global hero_attack_roll
            hero_attack_roll = randint(5, 20)
            hero_attack_roll += fighter_1.character_attack_strength
            hero_attack_verbiage = ["Your trusty sword thrusts at your foe...\n",
                                    "You swing wildly like a beast possessed!\n",
                                    "Your sword flashes in the dim light as it swings toward the goblin!\n"]
            verbiage_select = randint(0, 2)
            print(hero_attack_verbiage[verbiage_select])
            playsound(r"sfx\sword_slash.mp3")
            time.sleep(2)
            print("Attack roll: " + str(hero_attack_roll) + "\n")
            return hero_attack_roll

        # calls action() when pressed
        button = Button(text="Roll", command=attack_roll)
        button.pack()
        window.mainloop()

        # this is new, this is getting the attack roll number from the attack_roll() function.
        # but it doesn't work; it duplicates the attack, no go.
        # hero_attack_roll = attack_roll()
        if hero_attack_roll >= 12:
            playsound(r"sfx\sword_cuts_flesh.mp3")
            hero_strike_verbiage = ["You slice into the goblin's crusty skin, eliciting a howl of pain and anger!",
                                    "Your swing lands, burying deep in the creature's hideous flesh!",
                                    "CRUNCH goes your sword through the goblin's feeble armor!"]
            verbiage_select_2 = randint(0, 2)
            print(hero_strike_verbiage[verbiage_select_2])
            damage(fighter_1)  # apparently no need to write hero_damage_roll = damage(fighter_1)
            fighter_2.goblin_hp -= hero_damage_roll  # because I guess this just pulls it down from above
            display_health_bars(fighter_1, fighter_2)

            if fighter_2.goblin_hp <= 0:
                playsound(r"sfx\goblin_death_rattle.wav")
                fighter_2.goblin_perish()
                fighter_1.character_gold += fighter_2.goblin_gold
                fighter_1.character_xp += fighter_2.goblin_xp
                # level_increase(fighter_1)  # activates but kicks me back to main
                # fighter_1 = level_increase(fighter_1)

                # BJL:  original/comment out and move original definition into higher scope
                # BJL NOTE 2: Restored this value, but kept higher defn of verdict near top with default-value up there.
                verdict = True
                # return verdict
            else:
                fighter_hold = fighter_1
                fighter_1 = fighter_2
                fighter_2 = fighter_hold
                verdict = attack(fighter_1, fighter_2)
        else:
            playsound(r"sfx\sword_hits_metal.mp3")
            hero_miss_verbiage = ["Your feint and parry fail...",
                                  "The air if filled with the sound of a great SWISH!",
                                  "The blow glances off the goblin's armor, the blade vibrating in your hand!"]
            verbiage_select_3 = randint(0, 2)
            print(hero_miss_verbiage[verbiage_select_3])
            display_health_bars(fighter_1, fighter_2)

            fighter_hold = fighter_1
            fighter_1 = fighter_2
            fighter_2 = fighter_hold
            # BJL orig:
            # attack(fighter_1, fighter_2)
            # BJL new
            verdict = attack(fighter_1, fighter_2)
    elif hasattr(fighter_1, "goblin_hp"):
        playsound(r"sfx\goblin_roar.wav")
        goblin_attack_verbiage = ["The goblin's corroded axe flashes through the air...\n",
                                  "The goblin emits a piercing shriek as it strikes at thee!\n",
                                  "The goblin grunts and flails in your direction!\n"]
        verbiage_select_4 = randint(0, 2)
        print(goblin_attack_verbiage[verbiage_select_4])
        time.sleep(1)

        attack_roll = randint(1, 20)

        if attack_roll >= 14:
            playsound(r"sfx\hero_cry.wav")
            goblin_strike_verbiage = ["The axe crunches through your armor into your flesh!\n",
                                      "You scream out as the goblin's rusty blade finds its mark!\n",
                                      "The goblin cackles with glee as it draws blood!\n"]
            verbiage_select_5 = randint(0, 2)
            print(goblin_strike_verbiage[verbiage_select_5])
            damage_to_hero = randint(1, 4)

            if getattr(fighter_1, "goblin_type") == "hobgoblin":
                damage_to_hero += 1
            if getattr(fighter_1, "goblin_type") == "trogo-goblin":
                damage_to_hero += 2

            time.sleep(1)
            print(f"The blow delivers {damage_to_hero} points of damage to {fighter_2.character_name}.")
            fighter_2.character_hp -= damage_to_hero
            display_health_bars(fighter_2, fighter_1)

            if fighter_2.character_hp <= 0:
                fighter_2.character_perish()
                verdict = False
                return verdict

            else:
                fighter_hold = fighter_1
                fighter_1 = fighter_2
                fighter_2 = fighter_hold
                verdict = attack(fighter_1, fighter_2)
        else:
            playsound(r"sfx\sword_hits_metal.mp3")
            goblin_miss_verbiage = ["The axe hisses by, missing your neck by a hair's breadth.",
                                    "The goblin's swing goes wide and clangs against the wall!",
                                    f"The blow glances off the {fighter_2.character_name}'s armor!"]
            verbiage_select_6 = randint(0, 2)
            print(goblin_miss_verbiage[verbiage_select_6])
            display_health_bars(fighter_2, fighter_1)

            fighter_hold = fighter_1
            fighter_1 = fighter_2
            fighter_2 = fighter_hold
            verdict = attack(fighter_1, fighter_2)

    return verdict


# 3. damage function
def damage(fighter_1):
    # Creating a new window and configurations
    window = Tk()
    window.title("Goblins' Abode")
    window.minsize(width=300, height=50)

    # Labels
    label = Label(text="Damage")
    label.pack()

    # Buttons
    def damage_roll():
        global hero_damage_roll
        if hasattr(fighter_1, "character_hp"):
            hero_damage_roll = randint(1, 7)
            hero_damage_roll += fighter_1.character_attack_strength
            print(f"The blow delivers {hero_damage_roll} points of damage to the goblin!")
        return hero_damage_roll

    # calls action() when pressed
    button = Button(text="Roll", command=damage_roll)
    button.pack()
    window.mainloop()
