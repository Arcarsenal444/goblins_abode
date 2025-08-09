

"""
goblins_abode
main.py
@author: arcarsenal444
created: late 2023 / early 2024
purpose: serves as the main file for playing this text-based adventure game
in the style of similar computer games from the 1980s.
"""

# NOTE: toggle between jetbrains mono font and segoe UI emoji for the color on the battle bars. (in settings)

# imports
import floor_1
from battle_decision import battle_chance
import battle_file
from decision_tree import decision
from create_goblin import create_goblin
from create_hero import create_hero
from opening_sequence import opening_sequence
from level_titles import play_titles
from level_up import level_increase
from scene_change_sfx import entry_sounds, investigating_sounds
import time
import persistence

"""
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
        print(f"--> DEBUG: {s}")
        
"""


# create json files dir
GAME_FILE_DIR='game_files'
persistence.make_json_output_dir( o_dir=GAME_FILE_DIR)

# initial character set-up
hero = create_hero()
hero.save(GAME_FILE_DIR)

# initiate opening sequence
opening_sequence(hero)  # turning off for now to speed up tests.

# game launches: this is the outer loop that runs even when switching between levels.
game_on = True

# level titles run
while game_on:
    if hero.character_hp <= 0:
        game_on = False  # just added this if/else and tabbed everything over one.
    else:
        play_titles(hero)

        # this wipes the room name/hold clean when the level advances
        room_name = ""
        room_name_hold = ""

        # this is where I will eventually build in how to transition between levels
        if hero.floor_level == 1:
            room_name = "Entry Way"
            room_name_hold = "Entry Way"
        elif hero.floor_level == 2:
            room_name = "Living Room"
            room_name_hold = "Living Room"

        # initiate level: we stay in this level loop until moving to a different level
        level_on = True
        room_name = room_name
        room_name_hold = room_name_hold
        entry_sounds_trigger = True  # doing this to trigger entry sounds when moving between rooms, not investigating.
        counter = 0

        while level_on:
            if counter < 1:
                pass
            else:
                # the chance for battle initiates
                battle = battle_chance()
                if battle:
                    # goblin created in separate .py file
                    goblin = create_goblin()
                    # determine winner and the next step of the game
                    battle_outcome = battle_file.do_battle(hero, goblin)
                    if battle_outcome:
                        level_increase(hero)  # 4/21/25: still returning to level beginning
                        pass
                    else:
                        # BJL orig
                        '''
                        break 
                        # entry_sounds_trigger = False
                        # level_on = False
                        # game_on = False
                        '''
                        # BJL new
                        entry_sounds_trigger = False
                        level_on = False
                        game_on = False
                        break

            if entry_sounds_trigger:
                entry_sounds()
            else:
                entry_sounds_trigger = True

            # increase the counter to trigger future goblin battles
            counter += 1  # putting this on hold so I can figure out why I'm not leaving after outdoors.

            # room descriptions and player choices: sends back the dictionary
            room_name_choices = floor_1.initiate_rooms(hero, room_name)
            if room_name_choices == "End Sinister":
                level_on = False
                game_on = False
            else:
                room_name = decision(room_name_choices)
                hero.save(GAME_FILE_DIR)
                # Here's where you put in something like:
                if "Level" in room_name:
                    # hero.level_attribute_undetermined_as_yet +=/-= 1 (this will have to account for going up and down)
                    # Looks like only going up for now.
                    hero.floor_level += 1
                    counter = 0
                    level_on = False
                if room_name == "Items":
                    investigating_sounds()
                    entry_sounds_trigger = False
                    hero.show_items()
                    counter = 0
                    room_name = room_name_hold
                    level_on = True
                else:
                    operations_list = ["Examine Bust", "Open Bust", "Try Lock", "Inspect Sphere", "Open Chest"]
                    if room_name in operations_list:
                        investigating_sounds()
                        entry_sounds_trigger = False
                        room_name_hold = room_name
                        counter = 0
                        level_on = True
                    else:
                        room_name_hold = room_name
                        level_on = True


# Game concludes
time.sleep(3)
# PUT IN A MOURNFUL DIRGE HERE. ALSO MAYBE ONE FOR IF HERO DIES.
print(f"Thus ends the quest of {hero.character_name}. You amassed {hero.character_gold} ivars.")
