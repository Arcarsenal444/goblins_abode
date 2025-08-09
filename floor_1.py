
"""
goblins_abode
floor_1.py
@author: arcarsenal444
purpose: this file assembles all the rooms from the first floor, each
of which contains a dictionary of choices that the player-character will
select from in order to advance.
"""


# imports

import time
from check_items import check_items

# climage is how I'm showing graphics at the moment, but it's not a good solution
# import climage

# Also trying to show graphics using PIL
# from PIL import Image

# Also trying to show graphics using os
# import os

# Also trying IPython
# from IPython.display import Image, display


# Initiate choice

def initiate_rooms(hero, room_name):
    if room_name == "Entry Way":
        destination_dict = entry_way(hero, room_name)
        return destination_dict
    if room_name == "Outdoors":
        destination_dict = outdoors()
        return destination_dict
    if room_name == "Main Hall":
        destination_dict = main_hall(hero, room_name)
        return destination_dict
    if room_name == "Luxuriant Hall":
        destination_dict = luxuriant_hall()
        return destination_dict
    if room_name == "Drawing Room":
        destination_dict = drawing_room()
        return destination_dict
    if room_name == "Eastern Alcove":
        destination_dict = eastern_alcove()
        return destination_dict
    if room_name == "Examine Bust":
        destination_dict = examine_bust()
        return destination_dict
    if room_name == "Open Bust":
        destination_dict = open_bust()
        return destination_dict
    if room_name == "Try Lock":
        destination_dict = try_lock(hero, room_name)
        return destination_dict
    if room_name == "Western Alcove":
        destination_dict = western_alcove()
        return destination_dict
    if room_name == "Inspect Sphere":
        destination_dict = inspect_sphere()
        return destination_dict
    if room_name == "Parlor":
        destination_dict = parlor(hero, room_name)
        return destination_dict
    if room_name == "Grand Staircase":
        destination_dict = grand_staircase()
        return destination_dict
    if room_name == "Second Floor Landing":
        destination_dict = second_floor_landing()
        return destination_dict
    if room_name == "Master Bedroom":
        destination_dict = master_bedroom()
        return destination_dict
    if room_name == "Open Chest":
        destination_dict = open_chest(hero, room_name)
        return destination_dict
    if room_name == "North Hall":
        destination_dict = north_hall()
        return destination_dict
    if room_name == "Garret Room":
        destination_dict = garret_room()
        return destination_dict
    if room_name == "Closet":
        destination_dict = closet(hero, room_name)
        return destination_dict
    if room_name == "Spiral Stair":
        destination_dict = spiral_stair(hero, room_name)
        return destination_dict


# room descriptions

def entry_way(hero, room_name):

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    # This is for loading the image when the time comes
    # output = climage.convert("4x4.jpg") # This is a placeholder
    # print(output)
    # time.sleep(2)

    # And here's my image attempt with PIL/Pillow (this shows it in a pop-up window though)
    # img = Image.open("4x4.jpg")
    # img.show()

    # And here's my attempt with os (also opens in pop-up window)
    # os.system("4x4.jpg")

    # And here's my attempt with IPython.display (this does not work)
    # display(Image(filename="4x4.jpg"))

    print("Entry Way\n\n"
          "You find yourself in entry way of rough-hewn stone and dark-stained panel wood, the fading light of the \n"
          "day filtering in at your back and creating long shadows on the parquet flooring beneath your feet.\n"
          "Before you to the north a doorway opens into a lushly appointed main foyer. The walls are cool to the \n"
          "touch, and in the corner of one panel to your left the words \"Go Away\" have been scratched into \n"
          "the wood.\n\n")
    time.sleep(2)
    check_items(hero, room_name)
    time.sleep(2)
    print("\nDo you proceed north or south?")
    destination_dict = {"North": "Main Hall", "South": "Outdoors", "Items": "Items", "room_name": "Entry Way"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------

def outdoors():
    print("Outdoors\n\n"
          "You find yourself back outside, standing in the fading light as the crisp autumn wind skirls around your \n"
          "body. You have elected not to solve the case of the goblins' abode. You opt instead to return to town \n"
          "and visit the local tavern.\n")
    return "End Sinister"

# ---------------------------------------------------------------------------------------------------


def main_hall(hero, room_name):

    print("Main Hall\n\n"
          "The main hallway, replete with standing suits of armor and tapestries, is lit by a dim chandelier, \n"
          "casting everything in a ghostly light. Three open doorways of stained oak stand at the north, east, and \n"
          "west of the room. Behind you to the south, the passageway leads back to daylight. The four walls abound \n"
          "with bookcases of old, leather-bound tomes. In the center of the room stands a low table, upon which \n"
          "rests an ancient-looking hourglass, a rusty dagger, and journal describing the writer's experience with \n"
          "astral projection. An ominous feeling pervades the room just as a stately grandfather clock in the corner \n"
          "chimes the hour.\n\n")
    time.sleep(2)
    check_items(hero, room_name)
    time.sleep(2)
    print("Do you go north, south, east, or west?")
    destination_dict = {"North": "Parlor", "South": "Entry Way", "East": "Luxuriant Hall", "West": "Western Alcove",
                        "room_name": "Main Hall"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------

def luxuriant_hall():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Luxuriant Hall\n\n"
          "To the east of the main hall, the corridor boasts wood-panel walls, ornate sconces, and iron torch \n"
          "holders, inside of which, guttering orange flames boil, casting the surroundings in a flickering, \n"
          "trance-inducing light. The tile floor is covered in a resplendent crimson carpet woven from tufts \n"
          "shaved from the hides of young Nepalese highland yaks. Standing in chest-height display cases, \n"
          "a set of canopic jars holds pride of place within the hallway. One large jar shows a hairline crack \n"
          "all the way down the side, and from it, an oozing yellow liquid has seeped. The air in the passageway \n"
          "is somewhat fogged with a shimmering green miasma.\n\n")
    time.sleep(2)
    print("Do you go east or west?")
    destination_dict = {"East": "Drawing Room", "West": "Main Hall", "Items": "Items", "room_name": "Luxuriant Hall"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def drawing_room():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Drawing Room\n\n"
          "You enter a drawing room that has clearly been ransacked and vandalized by intruders, everywhere \n"
          "showing signs of a destructive hand. A sopha, wingback chair, and chaise-longue have all \n"
          "been reduced to tatters. Claw marks score the wall paper. And in the fireplace, what remains \n"
          "of a child's doll has become ash and ember. Perhaps this room was where the former occupants \n"
          "made their last stand, for a large quantity of dark blood has dried into the rugs. \n"
          "The room opens into a small alcove to the north. \n\n")
    time.sleep(2)
    print("Do you look in the alcove or return to the west?")
    destination_dict = {"Alcove": "Eastern Alcove", "West": "Luxuriant Hall", "Items": "Items",
                        "room_name": "Drawing Room"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def eastern_alcove():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Eastern Alcove\n\n"
          "An alcove the size of a large walk-in closet extends to the north of the drawing room. One small portal \n"
          "window opens on the eastern wall, through which a slanting bolt of grey daylight is seen to highlight the \n"
          "manifold dust motes that dance in the air. Much like the grand foyer, the small room is lined with old \n"
          "bookshelves, though through the many gaps in volumes the walls behind can be seen plainly. It is almost \n"
          "as if someone...or something...has pillaged the collection. On a low pillar against the western wall, the \n"
          "marble bust of a gentleman from another era rests beneath a layer of dust. There appears to be something \n"
          "unusual about the bust.\n\n")
    time.sleep(2)
    print("Do you examine the bust or return to the drawing room?")
    destination_dict = {"Examine bust": "Examine Bust", "Drawing room": "Drawing Room", "Items": "Items",
                        "room_name": "Eastern Alcove"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def examine_bust():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("A closer examination of the marble bust reveals one curiousity. While indeed covered in a thick layer \n"
          "of dust, there is decidedly no dust along a line that extends around the circumference of the neck, just \n"
          "below the jawline. Indeed, peering behind the bust, you discover a small recessed hinge.\n\n")
    time.sleep(2)
    print("Do you open the bust along the hinge or return to the drawing room?")
    destination_dict = {"Open bust": "Open Bust", "Drawing room": "Drawing Room", "Items": "Items",
                        "room_name": "Examine Bust"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def open_bust():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("The head of the marble bust creaks backward along the neck seam to reveal a hollow compartment, inside \n"
          "of which sits a small box made of old wood with beaten copper fastenings. It is sealed by a rusty iron \n"
          "lock. You pick it up and examine it from all angles. Curiously, ancient runes have been etched into the \n"
          "bottom, though you are at a loss for what they may mean.\n\n")
    time.sleep(2)
    print("Do you try your luck at the rusty lock or return to the drawing room?")
    destination_dict = {"Try rusty lock": "Try Lock", "Drawing room": "Drawing Room", "Items": "Items",
                        "room_name": "Open Bust"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def try_lock(hero, room_name):

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("You examine the antique lock closely.")
    time.sleep(2)
    check_items(hero, room_name)
    time.sleep(2)
    destination_dict = {"Try lock again": "Try Lock", "Drawing room": "Drawing Room", "Items": "Items",
                        "room_name": "Try Lock"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def western_alcove():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Western Alcove\n\n"
          "The western passage leads into a small yet spacious alcove, the alabaster walls of which are lined \n"
          "with trophy skulls. The room carries a faint scent of ambergris and incense. On the floor rests what \n"
          "looks to be a large obsidian sphere, polished to a sheen.\n"
          "The only passageway out leads back to the east.\n\n")
    time.sleep(2)
    print("Do you backtrack to the east or inspect the sphere?")
    destination_dict = {"East": "Main Hall", "Inspect sphere": "Inspect Sphere", "Items": "Items",
                        "room_name": "Western Alcove"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def inspect_sphere():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("The sphere is jet black and in its surface you can see your faint reflection.\n"
          "Placing your palm on the surface, you feel a chill pass into your body.\n"
          "Suddenly a light in the center of the sphere flickers to life...it blazes forth...\n"
          "...and in it you see the watery image of a long silver key with a skull on the handle. \n"
          "A moment later the light dies.")
    destination_dict = {"Room description": "Western Alcove", "East": "Main Hall", "Items": "Items",
                        "room_name": "Inspect Sphere"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def parlor(hero, room_name):

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("The Parlor\n\n"
          "Within the dim interior of the parlor, a variety of games can be seen displayed on tables. \n"
          "Billiards, chess, backgammon, dice and cup for a game of han. A doorway leads to the east, \n"
          "through which can be seen the base of a resplendent, gently curving staircase. The room is carpeted \n"
          "in a thick, almost glossy, carpet of lavender shag. Flecks of dark, dried liquid can be seen dotting \n"
          "the carpet in the northeast corner near to where a glass case stands. The glass case contains a highly \n"
          "ornamented metal gauntlet, of the kind perhaps once worn by a medieval knight.\n")
    time.sleep(2)
    check_items(hero, room_name)
    time.sleep(2)
    print("\n\nDo you go east or back to the south?")
    destination_dict = {"East": "Grand Staircase", "South": "Main Hall", "Items": "Items", "room_name": "Parlor"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def grand_staircase():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Grand Staircase\n\n"
          "Made entirely of dark-stained mahogany, the staircase rises from the ground floor in a slowly turning \n"
          "arc, up and to the left, rimming the cylindrical stone wall, upon which are mounted many ornately \n"
          "framed oil paintings. The paintings hang at intervals of approximately five feet, and depict countrysides \n"
          "or, more often, portraits of genteel men and women from a past century.")
    time.sleep(2)
    print("\n\nDo you ascend the stairs to the second floor or return to the parlor?")
    destination_dict = {"Ascend": "Second Floor Landing", "Parlor": "Parlor", "Items": "Items",
                        "room_name": "Grand Staircase"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def second_floor_landing():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Upstairs Landing\n\n"
          "You stand at the head of a grand staircase, the balusters of which are carved into ornate, coiling \n"
          "serpents. Across the floor, a tall window on the north wall, reaching nearly to the vaulted celing, \n"
          "looks out onto the lawns, which are in a state of advanced disrepair, with vines coiling about the \n"
          "topiary, grasses grown wild, and a number of Ash trees in decline. The hallway runs to the east and \n"
          "west. To the east, a bedroom door of dark, carved Oak, stands imposingly next to a low-lit torch. To \n"
          "the west, the corridor runs off past a series of windows.")
    time.sleep(2)
    print("\n\nDo you go east or west?")
    destination_dict = {"East": "Master Bedroom", "West": "North Hall", "Items": "Items",
                        "room_name": "Second Floor Landing"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def master_bedroom():

    print("Master Bedroom\n\n"
          "Much like other rooms in the house, the master bedroom has been torn apart by capable hands. \n"
          "The mattress and comforter have been rendered into a mound of stuffing. The oil paintings have been \n"
          "slashed to ribbons. More blood stains cover the pearl-colored carpeting. Every article of furniture \n"
          "has either been overturned or reduced to matchwood. You turn to leave, but something catches your eye. \n"
          "A glint of metal flashes from beneath the bed.")
    time.sleep(2)
    print("\n\nDo you look under the bed, inspect the master bedroom again, or go west?")
    destination_dict = {"Look Under Bed": "Open Chest", "Master Bedroom": "Master Bedroom",
                        "West": "Second Floor Landing", "Items": "Items", "room_name": "Master Bedroom"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def open_chest(hero, room_name):

    print("The Copper Chest\n\n"
          "Tossing aside the remains of the blankets, you pull a shiny copper chest out from beneath the bedframe. \n"
          "Upon the gently sloping lid, the likeness of a sparrow has been beaten in. There is no lock upon the \n"
          "hasp, so you throw wide the lid to find an interior of padded velvet.")
    time.sleep(2)
    check_items(hero, room_name)
    time.sleep(2)
    print("Do you re-examine the chest, re-examine the master bedroom, or return to the west?")
    destination_dict = {"Chest": "Open Chest", "Master Bedroom": "Master Bedroom", "Items": "Items",
                        "West": "Second Floor Landing", "room_name": "Open Chest"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def north_hall():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("North Hall\n\n"
          "An opulent hallway runs east to west along the north side of the house. On the north wall, tall windows \n"
          "look out onto the wasted lawn below. The bleak light of an autumn sun filters in between the curtains \n"
          "and paints the drab wall paper on the southern wall with cold iridescence. In places, the runner carpet \n"
          "is rumpled up as though tripped over by persons in haste. The only additional feature of the room is a \n"
          "fallen chandelier, which lies on its side in a puddle of shadow. It has been shat upon, and urine stains \n"
          "have soaked into the carpet beneath it.")
    time.sleep(2)
    print("\n\nDo you go east or west?")
    destination_dict = {"East": "Second Floor Landing", "West": "Garret Room", "Items": "Items",
                        "room_name": "North Hall"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def garret_room():

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Garret Room\n\n"
          "The walls of the garret room are painted a murky green. An unmade single bed stands against the west \n"
          "wall, its covers and sheets lying in disarray. On a small writing desk built from grey wood, a few books \n"
          "and papers rest, but they appear to be uninteresting. From beneath the rickety floorboards, a yellowish \n"
          "fog rises to a height of about two feet. There is a closet on the south of the garret room.")
    time.sleep(2)
    print("\n\nDo you go east or look into the closet?")
    destination_dict = {"East": "North Hall", "Open Closet": "Closet", "Items": "Items",
                        "room_name": "Garret Room"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------

def closet(hero, room_name):

    # NOTE: I removed None: None from the fourth slot of the destination dict.

    print("Garret Room Closet\n\n"
          "Shoving aside some of the hanging clothes, you discover an ornately carved wooden door. On its surface \n"
          "you see myriad designs including great swooping herons, thunder bolts issuing from a turbulent heavens, \n"
          "and a coiled serpent at the base. Beneath the golden handle is a lock with a bas relief image of a skull \n"
          "above it.")
    time.sleep(2)
    check_items(hero, room_name)
    time.sleep(2)
    print("Do you enter the closet or turn back?")
    destination_dict = {"Enter Narrow Passage": "Spiral Stair", "Garret Room": "Garret Room", "Items": "Items",
                        "room_name": "Closet"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------

def spiral_stair(hero, room_name):

    # NOTE: I removed None: None from the fourth slot of the destination dict. May have to make another version
    # of the decision_tree that has a len(dict) == 3?

    print("Base of the Spiral Staircase\n\n"
          "You follow the cramped confines of the passage through a dank scent of mildew all the way to a stone door \n"
          "with the image of a sparrow engraved in relief. A tall, narrow coin slot is in the face of the door.")
    time.sleep(2)
    level_advance = check_items(hero, room_name)
    if level_advance:
        print("A tightly coiling metal staircase disappears upward into the gloom of the small alcove you find \n"
              "yourself in.")
        destination_dict = {"Climb the Stair": "Level 2", "Items": "Items", None: None, "room_name": "Spiral Stair"}
    else:
        print("You have not obtained the proper keys.")
        destination_dict = {"Closet": "Closet",  "Items": "Items", None: None, "room_name": "Closet"}
    return destination_dict
